from bcdebug import debug
import App
import FoundationTech
import MissionLib
import loadspacehelper
import Bridge.BridgeUtils
import Lib.LibEngineering
import math

"""

Sample Setup:
# In scripts/Custom/ships/yourShip.py
# NOTE: replace "AMVoyager" with your abbrev
Foundation.ShipDef.AMVoyager.dTechs = {
	'Adv Armor Tech': 1
}
# In scripts/ships/yourShip.py

def GetArmorRatio(): # Strength of the armor, in a way
      return 2.5

def GetDamageStrMod(): # visual damage strength
	return 0

def GetDamageRadMod(): # visual damage radius
	return 0

def GetForcedArmor(): # If everyone is forced to wear it once it loads
	return 1

def GetArmouredModel(): # OPTIONAL: Select another scripts/ships/yourShip2.py with a adifferent model so when you are armored you change to this
	return "DiamondsArmorVoyager"

def GetOriginalShipModel(): # Should be the same script scripts/ships/yourShip2.py, but for more flexibility, here you can change it to never return when the armor drops
	return "DiamondsAMVoyager"
# In scripts/ships/Hardpopints/yourShip.py
# Add armored hull property, optional if you added GetArmorRatio above
#################################################
ArmourGenerator = App.HullProperty_Create("Armored Hull")

ArmourGenerator.SetMaxCondition(295000.000000)
ArmourGenerator.SetCritical(0)
ArmourGenerator.SetTargetable(1)
ArmourGenerator.SetPrimary(0)
ArmourGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ArmourGenerator.SetPosition2D(0.000000, 0.000000)
ArmourGenerator.SetRepairComplexity(1.000000)
ArmourGenerator.SetDisabledPercentage(0.500000)
ArmourGenerator.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ArmourGenerator)

# on the Property load function.
	prop = App.g_kModelPropertyManager.FindByName("Armored Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)

"""

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

global sNewShipScript
sNewShipScript = None
global sOriginalShipScript
OriginalShipScript = None

#global LastShipType
LastShipType = "nonArmored"

# This class does control the attach and detach of the Models
class AdvArmorTechTwoDef(FoundationTech.TechDef):
	
	# called by FoundationTech when a ship is created
        def AttachShip(self, pShip, pInstance):
                debug(__name__ + ", AttachShip")
                print "Ship %s with AdvArmorTech2 support added" % pShip.GetName()

                sNamePrefix = pShip.GetName() + "_"

                self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once

                ModelList = 0
                try:
			ModelList = pInstance.__dict__["Adv Armor Tech"]
                except:
			ModelList = 0
                
		if not ModelList:
		        return
                
		try:
			global ArmorButton
			global AdvArmorRecord
			global vd_rad_mod
			global vd_str_mod
			global pShipp
			global LastShipType

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
			pShipp = pShip
			mustGo = 0
			if (pShip.GetName() == pPlayer.GetName()):
				if not self.bAddedWarpListener.has_key(pShip.GetName()):
					if LastShipType == "nonArmored":
						print ("Ok the previous was not armored")
						ArmorButton = Lib.LibEngineering.CreateMenuButton("Plating Offline", "Tactical", __name__ + ".AdvArmorToggle")
					else:
						print ("Ok the previous WAS armored, attempting to get the past button")
						try:
							theMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
							ArmorButton = Libs.LibEngineering.GetButton("Plating Offline", theMenu)
							#DeleteMenuButton("Tactical", "Plating Offline")
						except:
							try:
								theMenu = Libs.LibEngineering.GetBridgeMenu("Tactical")
								ArmorButton = Libs.LibEngineering.GetButton("Plating Online", theMenu)
								#DeleteMenuButton("Tactical", "Plating Online")
							except:
								print("No armor button to grab, huh")
					#ArmorButton = Lib.LibEngineering.CreateMenuButton("Plating Offline", "Tactical", __name__ + ".AdvArmorToggle")
					try:
						LastShipType = "yesArmored"
					except:
						print("It doesn't let me change the LastShipType witb")
					self.bAddedWarpListener[pShip.GetName()] = 1
			else:
				if not self.bAddedWarpListener.has_key(pShip.GetName()):
					pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
					self.bAddedWarpListener[pShip.GetName()] = 1
				mustGo = 1

			imForced = 0
			try:
				pShipModule=__import__(pShip.GetScript())
				imForced = pShipModule.GetForcedArmor()
				print "I am forced, understood"
			except:
				print "I am not forced, understood"
				imForced = 0

			if (mustGo == 1 or imForced == 1):
				AdvArmorToggleFirst(pShip)

			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_DAMAGED, pMission, __name__ + ".SubDamage")
			print("SUCCESS while attaching advarmortechthree")
		except:
			print("ERROR while attaching advarmortechthree")                

	# Called by FoundationTech when a Ship is removed from set (eg destruction)
        def DetachShip(self, iShipID, pInstance):
		# get our Ship
                debug(__name__ + ", DetachShip")
                pShip = App.ShipClass_GetObjectByID(None, iShipID)
                if pShip:
			# remove the listeners
			print("Have to detach advarmortechtwo")
			if (pShip == pPlayer or pShip.GetName() == pPlayer.GetName()):
				try:
					DeleteMenuButton("Tactical", "Plating Offline")
				except:
					try:
						DeleteMenuButton("Tactical", "Plating Online")
					except:
						print("No armor button to delete, huh")
			else:
				pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
			if self.bAddedWarpListener.has_key(pShip.GetName()):
				del self.bAddedWarpListener[pShip.GetName()]
                
oAdvArmorTechTwo = AdvArmorTechTwoDef("Adv Armor Tech")

def SubsystemStateChanged(pObject, pEvent):
        debug(__name__ + ", SubsystemStateChanged")
        pShip = App.ShipClass_Cast(pObject)
        pSubsystem = pEvent.GetSource()
        print "Ship %s with AdvArmorTech2 has changed a subsystem" % pShip.GetName()

	# if the subsystem that changes its power is a weapon
        if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
		# set wings for this alert state
		print "Ship %s with AdvArmorTech2 has changed the weapon subsystem" % pShip.GetName()
                AdvArmorToggleAI(pObject, pEvent, pShip)
		
        pObject.CallNextHandler(pEvent)

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
	global pShipp
	armor_ratio=0.0
	pShip=pShipp
	pPlayer=MissionLib.GetPlayer()
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
	theCondition = 0
	if (pShip == pPlayer):
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		theCondition = BtnName.Compare(App.TGString("Plating Online"),1)
	else:
		theCondition = not AdvArmorRecord
	
	if (theCondition):
		return

	batt_chg=pPower.GetMainBatteryPower()
	batt_limit=pPower.GetMainBatteryLimit()
	if (batt_chg<=(batt_limit*.05)):
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetInvincible(0)
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
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetInvincible(0)
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
	global pShipp
	pShip=pShipp
	pPlayer=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

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

	theCondition = 0
	if (pShip == pPlayer):
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		theCondition = BtnName.Compare(App.TGString("Plating Online"),1)
	else:
		theCondition = not AdvArmorRecord
	
		
	if not (theCondition):
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetInvincible(0)
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
			if not (sOriginalShipScript == None):
				ReplaceModel(pShip, sOriginalShipScript)
	else:
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript:
			ReplaceModel(pShip, sNewShipScript)
		AdvArmor()
	return

# called when armor button is clicked
def AdvArmorToggleAI(pObject, pEvent, pShip):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	#global pShipp
	#pShip=pShipp
	pPlayer=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

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

	theCondition = 0
	if (pShip == pPlayer):
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		theCondition = BtnName.Compare(App.TGString("Plating Online"),1)
	else:
		theCondition = not AdvArmorRecord
	
		
	if not (theCondition):
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetInvincible(0)
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
			if not (sOriginalShipScript == None):
				ReplaceModel(pShip, sOriginalShipScript)
	else:
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript:
			ReplaceModel(pShip, sNewShipScript)
		AdvArmor()
	return

# called when armor button is clicked
def AdvArmorToggleFirst(pShip):
	global AdvArmorRecord
	global ArmorButton
	global vd_rad_mod
	global vd_str_mod
	global sNewShipScript
	global sOriginalShipScript
	#global pShipp
	#pShip=pShipp
	pPlayer=MissionLib.GetPlayer()
	pShipModule=__import__(pShip.GetScript())

	try:
		armor_ratio=pShipModule.GetArmorRatio()
	except:
		try:
			OldArmor=GetAdvArmor(pShip)
		except:
			return # this ship has no armor don't try to make it invincible

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

	theCondition = 0
	if (pShip == pPlayer):
		BtnName=App.TGString()
		ArmorButton.GetName(BtnName)
		theCondition = BtnName.Compare(App.TGString("Plating Online"),1)
	else:
		theCondition = not AdvArmorRecord
	
		
	if not (theCondition):
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Offline"))
		if (AdvArmorRecord):
			MissionLib.ShowSubsystems(AdvArmorRecord)
			AdvArmorRecord=0
			pShip.SetInvincible(0)
			pShip.SetVisibleDamageRadiusModifier(vd_rad_mod)
			pShip.SetVisibleDamageStrengthModifier(vd_str_mod)
			if not (sOriginalShipScript == None):
				ReplaceModel(pShip, sOriginalShipScript)
	else:
		if (pShip == pPlayer):
			ArmorButton.SetName(App.TGString("Plating Online"))
		AdvArmorRecord=MissionLib.HideSubsystems(pShip)
		pShip.SetInvincible(1)
		pShip.SetVisibleDamageRadiusModifier(0.0)
		pShip.SetVisibleDamageStrengthModifier(0.0)
		if sNewShipScript:
			ReplaceModel(pShip, sNewShipScript)
		AdvArmor()
	return

def Restart():
	global ArmorButton
	global pShipp
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer=MissionLib.GetPlayer()
	if (pShipp == pPlayer):
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
