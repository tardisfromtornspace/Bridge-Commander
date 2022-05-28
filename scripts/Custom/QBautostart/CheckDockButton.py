from bcdebug import debug
import App
import MissionLib
import Lib.LibEngineering
import BridgeHandlers
import AI.Compound.DockWithStarbaseLong
import string

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.2",
                "License": "BSD",
                "Description": "Enables and Disables the Dock Button",
                "needBridge": 0
            }


def AreInSameGroup(pShip1, pShip2):
        debug(__name__ + ", AreInSameGroup")
        pFriendlys = MissionLib.GetFriendlyGroup()
        pEnemies = MissionLib.GetEnemyGroup()
        
        # if one is friendly and one enemy => false. Else: true
        if pFriendlys.IsNameInGroup(pShip1.GetName()) and pEnemies.IsNameInGroup(pShip2.GetName()):
                return 0
        elif pEnemies.IsNameInGroup(pShip1.GetName()) and pFriendlys.IsNameInGroup(pShip2.GetName()):
                return 0
        return 1
        

def HasDockingPoints(pStarbase):
        debug(__name__ + ", HasDockingPoints")
        vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, "Docking Entry Start")
        if vPos and vFwd and vUp:
                return 1
        return 0

def isConstructing(pShip):
        debug(__name__ + ", isConstructing")
        try:
                import Construct
                Construct.RequestDock(pShip) 
                if Construct.isConstructing(pShip):
                        return 1
                return 0
        except:
                return 0
        
        
def GetClosestStation(pShip):
        debug(__name__ + ", GetClosestStation")
        pSet = pShip.GetContainingSet()
	if not pSet:
		return None
        lObjects = pSet.GetClassObjectList(App.CT_SHIP)
        closestD = 0
        closestStation = None
        
        for pObject in lObjects:
                pShipCur = App.ShipClass_Cast(pObject)
                if pShipCur and pShipCur.GetShipProperty().IsStationary() and pShip.GetObjID() != pShipCur.GetObjID() and AreInSameGroup(pShip, pShipCur):
                        if not HasDockingPoints(pShipCur) or isConstructing(pShipCur):
                                continue
                        curD = Distance(pShip, pShipCur)
                        if not closestStation:
                                closestStation = pShipCur
                                closestD = curD
                        elif curD < closestD:
                                closestStation = pShipCur
                                closestD = curD
        
        return closestStation


def EnableDockButton():
        debug(__name__ + ", EnableDockButton")
        pButton = GetDockButton()
        if pButton:
                pButton.SetEnabled()


def EnterSet(pObject, pEvent):
        debug(__name__ + ", EnterSet")
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        pPlayer = MissionLib.GetPlayer()
        
        if pPlayer and pShip and pPlayer.GetObjID() == pShip.GetObjID():
                pStation = GetClosestStation(pPlayer)
                if pStation:
                        EnableDockButton()

        pObject.CallNextHandler(pEvent)
                
        
def ExitSet(pObject, pEvent):
        debug(__name__ + ", ExitSet")
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        pPlayer = MissionLib.GetPlayer()
        
        if pPlayer and pShip and pPlayer.GetObjID() == pShip.GetObjID():
                pButton = GetDockButton()
                if pButton:
                        pButton.SetDisabled()
        
        pObject.CallNextHandler(pEvent)


def GetDockButton():
        debug(__name__ + ", GetDockButton")
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        ButtonName = pDatabase.GetString("Dock")
        App.g_kLocalizationManager.Unload(pDatabase)
        
        pMenu = Lib.LibEngineering.GetBridgeMenu("Helm")
        pButton = Lib.LibEngineering.GetButton(ButtonName.GetCString(), pMenu)
        return pButton


# Get the Distance between two Objects
def Distance(pObject1, pObject2):
	debug(__name__ + ", Distance")
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()


# from QBR
def DockButtonClicked(pObject, pEvent):	
	debug(__name__ + ", DockButtonClicked")
	pPlayer = MissionLib.GetPlayer()
	if pPlayer:
		DockStarbase()

        # Don't call next Handler - the next Handler will only call the Starbase12 Handler in Bridge.HelmMenuHandlers
        # which does only work - guess it - with Starbase12
	#pObject.CallNextHandler(pEvent)
	BridgeHandlers.DropMenusTurnBack()


# from QBR
def DockStarbase():
	# Get Player.
	debug(__name__ + ", DockStarbase")
	pPlayer = MissionLib.GetPlayer()
	pStarbase = GetClosestStation(pPlayer)
	
	if not pStarbase:
		return

	MissionLib.SetTotalTorpsAtStarbase("Photon", -1)
	MissionLib.SetTotalTorpsAtStarbase("Quantum", -1)
	MissionLib.SetTotalTorpsAtStarbase("Adv. Photon", -1)
	MissionLib.SetTotalTorpsAtStarbase("Positron", -1)
	MissionLib.SetTotalTorpsAtStarbase("Phased", -1)

	pGraffAction = None
        
	# Set AI for docking/undocking.
	MissionLib.SetPlayerAI("Helm", AI.Compound.DockWithStarbaseLong.CreateAI(pPlayer, pStarbase, pGraffAction, NoRepair = 0, FadeEnd = 0))


def ObjectCreatedHandler(pObject, pEvent):
        debug(__name__ + ", ObjectCreatedHandler")
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        
        # check in 5 seconds
	if pShip:
        	pSeq = App.TGSequence_Create()
        	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "Check", pShip.GetObjID()), 5)
        	pSeq.Play()
        debug(__name__ + ", ObjectCreatedHandler End")
        pObject.CallNextHandler(pEvent)
        

def Check(pAction, iShipID):
        debug(__name__ + ", Check")
        pPlayer = MissionLib.GetPlayer()
	pShip = App.ShipClass_GetObjectByID(None, iShipID)

        if pShip and pPlayer and pShip.GetShipProperty().IsStationary() and AreInSameGroup(pPlayer, pShip) and HasDockingPoints(pShip):
                EnableDockButton()

	debug(__name__ + ", Check Done")
        return 0


def init():
        debug(__name__ + ", init")
        pMission = MissionLib.GetMission()
	
	# Don't do anything in maelstrom
	if pMission and string.find(pMission.GetScript(), "Maelstrom") != -1:
		return
        
	if Lib.LibEngineering.CheckActiveMutator("Enhanced Starbase Docking"):
		return
	
        # Ship entrance event
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".EnterSet")
        # Ship exit event
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_SET, pMission, __name__ + ".ExitSet")
        # Dock Button click
        pKiskaMenu = Lib.LibEngineering.GetBridgeMenu("Helm")
        pKiskaMenu.AddPythonFuncHandlerForInstance(App.ET_DOCK,	__name__ + ".DockButtonClicked")
	
        # check new ships
	# ET_OBJECT_CREATED doesn't work on MP clients
	if App.g_kUtopiaModule.IsMultiplayer():
        	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")
	else:
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED, pMission, __name__ + ".ObjectCreatedHandler")
