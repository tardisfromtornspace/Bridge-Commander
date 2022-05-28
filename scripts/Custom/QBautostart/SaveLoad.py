import App
import nt
import string
import MissionLib
import loadspacehelper
import Lib.Ambiguity
import Libs.LibEngineering
from Libs.LibQBautostart import *

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.2",
                "License": "BSD",
                "Description": "Minimalistic Save & Load",
                "needBridge": 0
            }
            

MISSIONS_SAVE_DIR = "scripts/Custom/QBautostart/saves/Missions/"
ET_CLOSE = None

sCurSaveName = "Default"
sCurLoadName = ""
lMissions = []
g_dict_Ships = {}
MP_SET_POSITION_MSG = 200

# returns ship status values, such as damage and shield status in a dictionary
def getShipAttributes(pShip):
        dict_ShipAttrs = {}
        pPropSet = pShip.GetPropertySet()
        pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
        if pShipSubSystemPropInstanceList:
                iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                pShipSubSystemPropInstanceList.TGBeginIteration()
                for i in range(iNumItems):
                        pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                        pProperty = App.SubsystemProperty_Cast(pInstance.GetProperty())
                        sName = pProperty.GetName().GetCString()
                        # bad - find a better way!
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
                        dict_ShipAttrs[sName] = pSubsystem.GetConditionPercentage()
                pShipSubSystemPropInstanceList.TGDoneIterating()
        
        dict_ShipAttrs["MiscAttributes"] = {}
        # shields
        dict_ShipAttrs["MiscAttributes"]["shields"] = {}
        for iShield in range(App.ShieldClass.NUM_SHIELDS):
                dict_ShipAttrs["MiscAttributes"]["shields"][iShield] = pShip.GetShields().GetCurShields(iShield)
        
        return dict_ShipAttrs


# Restores the attributes of above
def RestoreShipAttributes(pShip, dict_ShipAttrs):
        for sSubsystemName in dict_ShipAttrs.keys():
                if sSubsystemName != "MiscAttributes":
                        pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystemName)
                        if pSubsystem:
                                pSubsystem.SetConditionPercentage(dict_ShipAttrs[sSubsystemName])
        # shields
        dict_Shields = dict_ShipAttrs["MiscAttributes"]["shields"]
        for iShield in range(App.ShieldClass.NUM_SHIELDS):
                pShip.GetShields().SetCurShields(iShield, dict_Shields[iShield])


# recreates all systems
def CreateSystems(dict_Systems):
        for sSetName in dict_Systems.keys():
                sSetScript = dict_Systems[sSetName]
                pSet = App.g_kSetManager.GetSet(sSetName)
                if not pSet:
                        pSetModule = __import__(sSetScript)
                        pSetModule.Initialize()	
                        sSetName = pSetModule.GetSetName()
                        try:
                                pModule = __import__("Systems." + sSetName + "." + sSetName)
                                pModule.CreateMenus()
                        except:
                                l = string.split(sSetScript, '.')
                                pModule = __import__("Systems." + l[1] + "." + l[1])
                pSet = App.g_kSetManager.GetSet(sSetName)
		

def CreateShip(sShipName, sShipType, sGroupName, Worldpos, lForward, lUp, sSetName, dict_ShipAttrs, iNetPlayerID):
	pSet = App.g_kSetManager.GetSet(sSetName)
	pPlayer = MissionLib.GetPlayer()
                
	if sShipType:
		pShip = MissionLib.GetShip(sShipName, bAnySet=1)
		if pShip:
			pOldSet = pShip.GetContainingSet()
			
			# TODO: moving from set to another doesn't work in MP right now
			if pOldSet.GetName() != pSet.GetName() and not App.g_kUtopiaModule.IsMultiplayer():
				pOldSet.RemoveObjectFromSet(pShip.GetName())
				pSet.AddObjectToSet(pShip, pShip.GetName())
				# addObjectToSet doesn't seem to freeze the game - fix it
				if pShip.GetObjID() == pPlayer.GetObjID():
					pTop = App.TopWindow_GetTopWindow()
					pTop.ForceTacticalVisible()
		# a player ship that does not exist yet?
		elif App.g_kUtopiaModule.IsMultiplayer() and iNetPlayerID > 0:
			return
		else:
			pShip = loadspacehelper.CreateShip(sShipType, pSet, sShipName, "", 0)
		if pShip:
			kLocation = App.TGPoint3()
			kforward = App.TGPoint3()
			kup = App.TGPoint3()
			kLocation.SetXYZ(Worldpos[0], Worldpos[1], Worldpos[2])
			kforward.SetXYZ(lForward[0], lForward[1], lForward[2])
			kup.SetXYZ(lUp[0], lUp[1], lUp[2])
			pShip.SetTranslate(kLocation)
			pShip.AlignToVectors(kforward, kup)
			if App.g_kUtopiaModule.IsMultiplayer():
				MPSendPositionMsg(pShip, kLocation, kforward, kup)
			addShipToGroup(sShipName, sGroupName)
			if pPlayer.GetObjID() != pShip.GetObjID() and pShip.GetNetPlayerID() <= 0:
				autoAI(pShip) # sets the normal Foundation AI
			RestoreShipAttributes(pShip, dict_ShipAttrs)
			pShip.UpdateNodeOnly()


def MPSendPositionMsg(pShip, kLocation, kforward, kup):
        pMessage = App.TGMessage_Create()
        pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
        kStream.OpenBuffer(256)
        kStream.WriteChar(chr(MP_SET_POSITION_MSG))
        pNetwork = App.g_kUtopiaModule.GetNetwork()
	
        kStream.WriteInt(pShip.GetObjID())
	kStream.WriteInt(1)
	kStream.WriteFloat(kLocation.GetX())
	kStream.WriteFloat(kLocation.GetY())
	kStream.WriteFloat(kLocation.GetZ())
	kStream.WriteFloat(kforward.GetX())
	kStream.WriteFloat(kforward.GetY())
	kStream.WriteFloat(kforward.GetZ())
	kStream.WriteFloat(kup.GetX())
	kStream.WriteFloat(kup.GetY())
	kStream.WriteFloat(kup.GetZ())
	
        pMessage.SetDataFromStream(kStream)
        if not App.IsNull(pNetwork):
		pNetwork.SendTGMessageToGroup("NoMe", pMessage)
        kStream.CloseBuffer()
	

# recreates all ships
def CreateShips(dict_Ships):
	global g_dict_Ships
	
	for sShipName in dict_Ships.keys():
		sShipType, sGroupName, Worldpos, lForward, lUp, sSetName, dict_ShipAttrs, iNetPlayerID = dict_Ships[sShipName]
		CreateShip(sShipName, sShipType, sGroupName, Worldpos, lForward, lUp, sSetName, dict_ShipAttrs, iNetPlayerID)
	g_dict_Ships = dict_Ships


def NewPlayerHandler(pObject, pEvent):
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	
	if pShip and pShip.GetNetPlayerID() > 0 and g_dict_Ships.has_key(pShip.GetName()):
		sShipType, sGroupName, Worldpos, lForward, lUp, sSetName, dict_ShipAttrs, iNetPlayerID = g_dict_Ships[pShip.GetName()]
		CreateShip(pShip.GetName(), sShipType, sGroupName, Worldpos, lForward, lUp, sSetName, dict_ShipAttrs, iNetPlayerID)
		
	
	
def Save(pObject, pEvent):
        CloseDialog(pObject)
        
        dict_Ships, dict_Systems = GetShipsAndSystems()
        
        sSaveFile = MISSIONS_SAVE_DIR + sCurSaveName + ".py"
        # delete the file if it does already exist
        try:
                nt.remove(sSaveFile)
        except:
                pass
        file = nt.open(sSaveFile, nt.O_CREAT | nt.O_RDWR)
        sSaveShip = string.replace(repr(dict_Ships), ", {", ",\\\n\t\t{")
        sSaveShip = string.replace(sSaveShip, "],", "],\\\n\t")
        nt.write(file, "Systems = " + repr(dict_Systems) + "\n")
        nt.write(file, "Ships = " + sSaveShip + "\n")
        nt.close(file)
        

# returns two dicts, one for all ships with all important values and one for all systems
def GetShipsAndSystems():
        dict_Ships = {}
        dict_Systems = {}
        
        for pSet in App.g_kSetManager.GetAllSets():
                if pSet.GetRegionModule():
                        dict_Systems[pSet.GetName()] = pSet.GetRegionModule()
                
                lObjects = pSet.GetClassObjectList(App.CT_SHIP)
                for pObject in lObjects:
                        pShip = App.ShipClass_Cast(pObject)
                        dict_ShipAttrs = getShipAttributes(pShip)
                        kLocation = pShip.GetWorldLocation()
			kForward = pShip.GetWorldForwardTG()
			kUp = pShip.GetWorldUpTG()
			lForward = [kForward.GetX(), kForward.GetY(), kForward.GetZ()]
			lUp = [kUp.GetX(), kUp.GetY(), kUp.GetZ()]
                        Worldpos = [kLocation.GetX(), kLocation.GetY(), kLocation.GetZ()]
                        sShipType = GetShipType(pShip)
                        dict_Ships[pShip.GetName()] = [sShipType, getGroupFromShip(pShip.GetName()), Worldpos, lForward, lUp, pSet.GetName(), dict_ShipAttrs, pShip.GetNetPlayerID()]
                        
        return dict_Ships, dict_Systems


def Load(pObject, pEvent):
        global sCurLoadName
        sCurLoadName = lMissions[pEvent.GetInt()]
	
	try:
        	pModule = __import__(sCurLoadName)
    
        	CreateSystems(pModule.Systems)
        	CreateShips(pModule.Ships)
	except:
		print "Bad Save file. Could be a too old format."
		print "Sorry: can not load that!"
		return
		
        # do postloading stuff if present
        if hasattr(pModule, "PostLoad"):
                pModule.PostLoad()


def CreateLoadMenuChilds(pMenu):
        global lMissions
        list = nt.listdir(MISSIONS_SAVE_DIR)
        list.sort()
        i = 0
        
        for plugin in list:
                s = string.split(plugin, '.')
                sExtension = s[-1]
                sSaveName = string.join(s[:-1], '.')

                if sSaveName != "__init__" and sExtension == "py":
                        sSaveModule = "BCROOT." + string.replace(MISSIONS_SAVE_DIR, '/', '.') + sSaveName
                        sSaveModule = string.replace(sSaveModule, "BCROOT.scripts.", "")
                        
                        lMissions.append(sSaveModule)
                        Libs.LibEngineering.CreateMenuButton(sSaveName, "XO", __name__ + ".Load", i, pMenu, "append")
                        i = i + 1


def CloseDialog(pPanel):
        global ET_CLOSE, sCurSaveName
        pTopWindow = App.TopWindow_GetTopWindow()
        App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pPanel, __name__ + ".Save")
        sCurSaveName = pText.GetCString()
        pPanel.KillChildren()
        pTopWindow.DeleteChild(pPanel)
        
        

def SaveDialog(pObject, pEvent):
        global ET_CLOSE, pText
        pTopWindow = App.TopWindow_GetTopWindow()
        ET_CLOSE = Lib.LibEngineering.GetEngineeringNextEventType()
        
        pPanel = Lib.Ambiguity.createPanel(pTopWindow, "Save State", 0.0, 0.0, 1.0, 1.0)
        pTopWindow.MoveToFront(pPanel)
        pText = Lib.Ambiguity.createEditBox(pPanel, 0.2, 0.2, "Name:", "", 0.25, 0.05, 256)
        pText.SetString(sCurSaveName)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_CLOSE)
        pEvent.SetDestination(pPanel)
        pButton = App.STRoundedButton_CreateW(App.TGString("Save"), pEvent, 0.1, 0.03)
        pButton.SetNormalColor(App.g_kMainMenuButtonColor)
        pPanel.AddChild(pButton, 0.25, 0.25)

        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pPanel, __name__ + ".Save")



def init():
        pButtonLoad = App.STMenu_CreateW(App.TGString("Load..."))
        Libs.LibEngineering.CreateMenuButton("-> Save <-", "XO", __name__ + ".SaveDialog", ToButton = pButtonLoad)
        pMenu = Libs.LibEngineering.GetBridgeMenu("XO")
        pMenu.PrependChild(pButtonLoad)

	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		CreateLoadMenuChilds(pButtonLoad)
	if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, MissionLib.GetMission(), __name__ + ".NewPlayerHandler")
