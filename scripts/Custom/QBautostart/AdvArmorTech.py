
import App
import FoundationTech
import MissionLib
import loadspacehelper
import Bridge.BridgeUtils
import Lib.LibEngineering

MODINFO = { "Author": "ed",
				"Download": "",
				"Version": "2.0",
				"License": "",
				"Description": "Support for armor and advanced armor"
	    		}

global sNewShipScript
sNewShipScript = None
global sOriginalShipScript
OriginalShipScript = None

# called when subsystem on any ship is damaged
def SubDamage(pObject, pEvent):
	AdvArmor()
	pObject.CallNextHandler(pEvent)

# Replaces the Model of pShip
def ReplaceModel(pShip, sNewShipScript):
	print __name__ + ", ReplaceModel"
	#pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	#if not pShip:
	#	return
	print sNewShipScript
        ShipScript = __import__('ships.' + sNewShipScript)
        ShipScript.LoadModel()
        kStats = ShipScript.GetShipStats()
        pShip.SetupModel(kStats['Name'])
	if App.g_kUtopiaModule.IsMultiplayer():
		MPSentReplaceModelMessage(pShip, sNewShipScript)

def AdvArmor():
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	armor_ratio=0.0
	pShip=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())
	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		OldArmor=GetAdvArmor(pShip)
		if (OldArmor==0):
			return
		armor_ratio=.3
	pPower=pShip.GetPowerSubsystem()
	if (pPower==None):
		return
	pHull=pShip.GetHull()
	if (pHull==None):
		return
	BtnName=App.TGString()
	ArmorButton.GetName(BtnName)
	if (BtnName.Compare(App.TGString("Plating Online"),1)):
		return
	batt_chg=pPower.GetMainBatteryPower()
	batt_limit=pPower.GetMainBatteryLimit()
	if (batt_chg<=(batt_limit*.05)):
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
		if (not sOriginalShipScript == None):
			ReplaceModel(pShip, sOriginalShipScript)
		return
	armor_pwr=batt_chg*armor_ratio
	hull_max=pHull.GetMaxCondition()
	hull_cond=pHull.GetCondition()
	hull_dmg=hull_max-hull_cond
	if (armor_pwr>=hull_dmg):
		armor_pwr=armor_pwr-hull_dmg
		pHull.SetCondition(hull_max)
	else:
		pHull.SetCondition(hull_cond+armor_pwr)
		armor_pwr=0
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)		
			if (not sOriginalShipScript == None):
				ReplaceModel(pShip, sOriginalShipScript)
	pPower.SetMainBatteryPower(armor_pwr/armor_ratio)
	return

def GetAdvArmor(pShip):
	pAdvArmor=0
	pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	while (pSubsystem != None):
		if(pSubsystem.GetName()=="Armored Hull"):
			pAdvArmor=pSubsystem
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
	pShip.EndGetSubsystemMatch(pIterator)
	return(pAdvArmor)

# called when armor button is clicked
def AdvArmorToggle(pObject, pEvent):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	pShip=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())
	try:
		kStats=pShipModule.GetShipStats
		if (kStats.has_key('DamageRadMod')):
			vd_rad_mod=kStats['DamageRadMod']
		else:
			vd_rad_mod=1
		if (kStats.has_key('DamageStrMod')):
			vd_str_mod=kStats['DamageStrMod']
		else:
			vd_str_mod=1
	except:
		try:
			vd_rad_mod=pShipModule.GetDamageRadMod()
			vd_str_mod=pShipModule.GetDamageStrMod()
			print vd_rad_mod
			print vd_str_mod
		except:
			print "No visual changes, understood"
			vd_rad_mod=1
			vd_str_mod=1
	try:
		if (kStats.has_key('ArmouredModel')):
			print "Hey I got it, extra model armour"
			sNewShipScript = kStats['ArmouredModel']
			print sNewShipScript
			sOriginalShipScript = kStats["OriginalModel"]
			#ReplaceModel(pShip, sNewShipScript)
	except:
		try:
			sNewShipScript=pShipModule.GetArmouredModel()
			sOriginalShipScript=pShipModule.GetOriginalShipModel()
			print sNewShipScript
			print sOriginalShipScript
		except:
			print "No visual armour, understood"
			sNewShipScript = None
			sOriginalShipScript = None
		
	BtnName=App.TGString()
	ArmorButton.GetName(BtnName)
	if not (BtnName.Compare(App.TGString("Plating Online"),1)):
		ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
			if not (sOriginalShipScript == None):
				ReplaceModel(pShip, sOriginalShipScript)
	else:
		ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord=MissionLib.HideSubsystems(pShip)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript:
			ReplaceModel(pShip, sNewShipScript)
		AdvArmor()
	return

# Initialize
def init():
	global ArmorButton
	global AdvArmorRecord
	global vd_rad_mod
	global vd_str_mod
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer=MissionLib.GetPlayer()
	pBridge = App.g_kSetManager.GetSet("bridge")
	g_pTactical = App.CharacterClass_GetObject(pBridge,"Tactical")
	pTacticalMenu = Bridge.BridgeUtils.GetBridgeMenu("Tactical")
	AdvArmorRecord=0
	vd_rad_mod=0.0
	vd_str_mod=0.0
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_DAMAGED, pMission, __name__ + ".SubDamage")
	ArmorButton=Lib.LibEngineering.CreateMenuButton("Plating Offline", "Tactical", __name__ + ".AdvArmorToggle")
	return

def Restart():
	global ArmorButton
	ArmorButton.SetName(App.TGString("Plating Offline"))
	return

def MPSentReplaceModelMessage(pShip, sNewShipScript):
        # Setup the stream.
        # Allocate a local buffer stream.
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	try:
		from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
		dReplaceModel[pShip.GetObjID()] = sNewShipScript
	except ImportError:
		pass

	# send Message
	kStream.WriteInt(pShip.GetObjID())
	iLen = len(sNewShipScript)
	kStream.WriteShort(iLen)
	kStream.Write(sNewShipScript, iLen)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def mp_send_settargetable(iShipID, iMode):
        # Setup the stream.
        # Allocate a local buffer stream.
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SET_TARGETABLE_MSG))

	# send Message
	kStream.WriteInt(iShipID)
	kStream.WriteInt(iMode)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()
