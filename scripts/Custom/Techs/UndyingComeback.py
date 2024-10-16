#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         UndyingComeback.py by Alex SL Gato
#         15th October 2024
#         Based on AdvArmorTechThree by Alex SL Gato derived from a KM and ftb team file, B5Defenses (based on Shields.py by the Foundation Technologies team), loadspacehelper (Dasher, BANBURY and other ftb people), SlipstreamModule (by USS Sovereign) and HelmMenuHandlers by the stbc team Totally Games (also partially based on Defiant's FleetUtils).
#################################################################################################################
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech gives a "second chance" when a ship is dying. Basically the death script is altered for that ship so it can at least partially come back to life, restoring mostly everything except subsystem visibility, with more buffs along the way. Thus "the Undying".
# Apart from the obvious dependance on Foundation and FoundationTech, this script needs ftb.Tech.ATPFunctions (normally already present by default on KM) and Tactical.Projectiles.AutomaticSystemRepairDummy (from Automated Destroyed System Repair) to work fully. Also it is extremely recommended to have the Autoload file FIX-AblativeArmour1dot0.py since it fixes an issue with KM white-bar Ablative Armour.
# In order to add this tech to your ship, add this to your scripts/Custom/Ships/ file, replacing "Ambassador" and "nameoftheshipfile" with the proper abbrev and desired value, respectively.
# - "Damage Factor": how destructive the attack must be to trigger this second chance. It is a multiplier or fraction of the max hull health, so 0.5 means that any shot at half health will trigger it.
# - "Model": which vessel it will relaod into as a second chance. You can make it reload onto itself again by placing the scripts/ships/ filename between the ", or choose another ship file.
# - "Boost": overall boost, multiplying how many times more powerful than the killing blast(s) the ship becomes. Default is 25.0x.
# - "Energy Boost": how much energy boost after undying. Default is 25.0x.
# - "Shield Boost": how much shield boost after undying. Default is 25.0x.
# - "Weapon Boost": how much shield boost after undying. Default is 1.0x (no extra).
# - "LoadSound": when the ship is entering Undying phase, what sound would you like to play. Set to -1 to be none. Default is the one stated on the "defaultLoadSound" global variable below.
# - "Sound": when the ship has finally entered undying phase, what sound would you like to play. Set to -1 to be none. Default is the one stated on the "defaultSound" global variable below.
# - "TimeToUndie": the time, in seconds, between beginning to undie and finally reaching Undying phase. Default is 40.5 seconds.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Undying Comeback": {"Damage Factor": 1.0, "Model": "nameoftheshipfile", "Boost": 25, "Energy Boost": 25.0, "Shield Boost": 25.0, "Weapon Boost": 25.0, "LoadSound": -1, "Sound": -1, "TimeToUndie": 40.5},
}
"""
#
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.02",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
import App

import Foundation
import FoundationTech
import MissionLib

import nt
import math
import string

from bcdebug import debug
import traceback

#
#################################################################################################################
#

REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

DEFAULT_BOOST = 25.0
DEFAULT_WEAPON_BOOST = 1.0

ET_CRITICAL_SYSTEM_AT_100 = App.UtopiaModule_GetNextEventType()

g_dOverrideAIs = {}

defaultLoadSound = "sfx/Music/ButTheUndertaleEarthRefusedToDie.wav"
defaultSound = "sfx/Music/BattleAgainstATrueHeroPower.wav"
defaultTimeToUndie = 39.5 # In seconds

#
#################################################################################################################
#

# Multiplayer stuff
def MPIsPlayerShip(pShip):
	return App.g_kUtopiaModule.IsMultiplayer() and pShip.GetNetPlayerID() >= 0

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

#############

def findShipInstance(pShip):
	debug(__name__ + ", findShipInstance")
	pInstance = None
	try:
		if not pShip:
			return pInstance
		if FoundationTech.dShips.has_key(pShip.GetName()):
			pInstance = FoundationTech.dShips[pShip.GetName()]
	except:
		pass

	return pInstance

# In a multithreaded game we would really need to add Semaphores and similar to these state variables, but after contacting other modders I've been told several times that despite everything, the game is both single-threaded and performs a function fully before switching to another so these extremely sloppy variables would do the trick nicely

def PlayButTheEarthRefusedToDie(pAction, pShipID, phase, soundMusic, volume=0):
	if soundMusic != -1 and str(soundMusic) != "-1":
		try:
			soundName = "ButTheEarthRefusedToDie" + str(pShipID) + str(phase)
			pEnterSound = App.TGSound_Create(soundMusic, soundName, volume)
			pEnterSound.SetSFX(0) 
			pEnterSound.SetInterface(1)
			App.g_kSoundManager.PlaySound(soundName)
		except:
			print "Missing sound or other error while playing Undying load sound:"
			traceback.print_exc()
	return 0

def BoostSubsystem(pSubsystem, boost, weaponBoost, shieldboost, energyboost, lethalDamageWas, ratioDmgVsHealth, pHullMax, pInstanceDict, pSubName):
	# Common to all subsystems, a hitpoint boost
	pSubsystemMax = pSubsystem.GetMaxCondition() * ratioDmgVsHealth
	pSubsystemProperty = pSubsystem.GetProperty()
	pSubsystemProperty.SetMaxCondition(pSubsystemMax)
	pSubsystem.SetCondition(pSubsystemMax)
	if pSubsystemProperty.GetDisabledPercentage() > 0.001:
		pSubsystemProperty.SetDisabledPercentage(0.001)

	# If it's one of KM default Ablative Armours, we need to nudge it a bit
	if pSubName and pSubName == pSubsystem.GetName():
		try:
			# THIS IS A SUPPORT TO THE MONKEY PATCH I MADE TO PREVENT A SINGLETON ISSUE
			if str(pInstanceDict['Ablative Armour L'])[0] == "[":
				pInstanceDict['Ablative Armour L'][0] = pSubsystemMax
			else:
				pInstanceDict['Ablative Armour L'] = pSubsystemMax
			pSubsystemProperty.SetRepairComplexity(pSubsystemProperty.GetRepairComplexity()/5.0)
		except:
			try:
				# Just in case you don't have the fix
				if str(pInstanceDict['Ablative Armour'])[0] == "[":
					pInstanceDict['Ablative Armour'][0] = pSubsystemMax
				else:
					pInstanceDict['Ablative Armour'] = pSubsystemMax
			except:
				pass

	# If it's a weapon, we may want to adjust its damage.
	if (pSubsystem.IsTypeOf(App.CT_ENERGY_WEAPON)):
		pWeapon = App.EnergyWeapon_Cast(pSubsystem)
		pEWProperty = App.EnergyWeaponProperty_Cast(pSubsystemProperty)

		if pEWProperty:
			pCurrentProperty = pWeapon.GetProperty()
			pCurrentProperty.SetMaxDamage(pEWProperty.GetMaxDamage() * ratioDmgVsHealth)
			fPct = pWeapon.GetChargeLevel() / pWeapon.GetMaxCharge()
			pCurrentProperty.SetMaxCharge(pEWProperty.GetMaxCharge() * weaponBoost)
			pWeapon.SetChargeLevel(pCurrentProperty.GetMaxCharge() * weaponBoost)
			pCurrentProperty.SetMinFiringCharge(pEWProperty.GetMinFiringCharge() * weaponBoost)
			pCurrentProperty.SetRechargeRate(pEWProperty.GetRechargeRate() * weaponBoost)
			
	# If it's a shield, we should adjust the shield values.
	if (pSubsystem.IsTypeOf(App.CT_SHIELD_SUBSYSTEM)):
		pShields = App.ShieldClass_Cast(pSubsystem)
		pShieldProperty = App.ShieldProperty_Cast(pSubsystemProperty)

		pCurrentProperty = pShields.GetProperty()
		kShieldFacings = [App.ShieldProperty.FRONT_SHIELDS,
						  App.ShieldProperty.REAR_SHIELDS,
						  App.ShieldProperty.TOP_SHIELDS,
						  App.ShieldProperty.BOTTOM_SHIELDS,
						  App.ShieldProperty.LEFT_SHIELDS,
						  App.ShieldProperty.RIGHT_SHIELDS]

		for kFacing in kShieldFacings:
			fPct = pShields.GetSingleShieldPercentage(kFacing)
			pCurrentProperty.SetMaxShields(kFacing, pShieldProperty.GetMaxShields(kFacing) * shieldboost)
			pShields.SetCurShields(kFacing, pShields.GetMaxShields(kFacing) * shieldboost)
			pCurrentProperty.SetShieldChargePerSecond(kFacing, pShieldProperty.GetShieldChargePerSecond(kFacing) * shieldboost)

	# If it's an energy property, we should adjust the energy values.
	if (pSubsystem.IsTypeOf(App.CT_POWER_SUBSYSTEM)):
		pESubsystem = App.PowerSubsystem_Cast(pSubsystem)
		pESubsystemP = App.PowerProperty_Cast(pSubsystemProperty)
		if pESubsystem and pESubsystemP:
			batt_chg=pESubsystem.GetMainBatteryPower()
			batt_limit=pESubsystem.GetMainBatteryLimit()
			pESubsystemP.SetMainBatteryLimit(batt_chg * energyboost)
			pESubsystemP.SetBackupBatteryLimit(batt_limit * energyboost)
			pESubsystem.SetMainBatteryPower(pESubsystem.GetMainBatteryPower())
			pESubsystem.SetBackupBatteryPower(pESubsystem.GetMainBatteryLimit())


def OverrideAI(pShip, sAIModule, *lAICreateArgs, **dAICreateKeywords):
	# Try to override the AI.
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "OverrideAIMid", pShip.GetObjID(), sAIModule, lAICreateArgs, dAICreateKeywords))
	pSequence.Play()
	return 0

def OverrideAIMid(pAction, idShip, sAIModule, lAICreateArgs, dAICreateKeywords):
	debug(__name__ + ", OverrideAIMid")
	pShip = App.ShipClass_GetObjectByID(None, idShip)
	if not pShip:
		return 0

	# Check if the ship has building AI's.
	if pShip.HasBuildingAIs():
		# Can't override AI just yet...  Try again in a little while.
		#debug("Can't override AI yet.  Delaying attempt...")
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction( App.TGScriptAction_Create(__name__, "OverrideAIMid", idShip, sAIModule, lAICreateArgs, dAICreateKeywords), 0.5 )
		pSeq.Play()
		return 0

	# Ship has no building AI's.  We can safely replace its AI.
	# Create the new AI...
	pAIModule = __import__(sAIModule)
	pNewAI = apply(getattr(pAIModule, "CreateAI"), lAICreateArgs, dAICreateKeywords)
	if pNewAI:
		OverrideAIInternal(pShip, pNewAI)
	return 0

def OverrideAIInternal(pShip, pNewAI):
	# Check for an old AI.
	debug(__name__ + ", OverrideAIInternal")
	global g_dOverrideAIs
	pOldAI = pShip.GetAI()
	pOverrideAI = None
	if pOldAI:
		if g_dOverrideAIs.has_key(pShip.GetObjID()):
			# Already have an override AI for this ship.  Check if
			# that AI is still in place.
			pOverrideAI = App.ArtificialIntelligence_GetAIByID(g_dOverrideAIs[pShip.GetObjID()])
			if (not pOverrideAI)  or  (pOverrideAI.GetID() != pOldAI.GetID()):
				# It's not in place.  Gotta make a new one.
				pOverrideAI = None
			else:
				# It's still in place.  Remove whatever was in
				# the priority 1 slot (whatever the player told
				# this ship to do before).
				pOverrideAI.RemoveAIByPriority(1)

	if not pOverrideAI:
		# Make a new Override AI.
		pOverrideAI = App.PriorityListAI_Create(pShip, "FleetCommandOverrideAI")
		pOverrideAI.SetInterruptable(1)

		# Second AI in the list is the current AI.
		if pOldAI:
			pOverrideAI.AddAI(pOldAI, 2)

	# First AI in the list is the AI to override the old one.
	pOverrideAI.AddAI(pNewAI, 1)

	# Replace the ship's AI with the override AI.  The 0 here
	# tells the game not to delete the old AI.
	pShip.ClearAI(0, pOldAI)
	pShip.SetAI(pOverrideAI)

	# Save info about this override AI.
	g_dOverrideAIs[pShip.GetObjID()] = pOverrideAI.GetID()

def StopOverridingAI(pShip):
	debug(__name__ + ", StopOverridingAI")
	global g_dOverrideAIs
	pOldAI = pShip.GetAI()
	pOverrideAI = None
	if pOldAI:
		if g_dOverrideAIs.has_key(pShip.GetObjID()):
			# Have an override AI for this ship.  Check if
			# that AI is still in place.
			pOverrideAI = App.ArtificialIntelligence_GetAIByID(g_dOverrideAIs[pShip.GetObjID()])
			if pOverrideAI  and  (pOverrideAI.GetID() == pOldAI.GetID()):
				# It's still in place.  Remove whatever was in
				# the priority 1 slot (whatever the player told
				# this ship to do before).
				pOverrideAI.RemoveAIByPriority(1)
	return 0

def TransformIntoUndyingPhaseII(pAction, pShipID, musicToPlay):
	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	toChangeOntoUndyingFully = 0
	if pShip:
		pInstance = findShipInstance(pShip)
		if pInstance:
			pInstanceDict = pInstance.__dict__
			if pInstanceDict.has_key('Undying Comeback'):
				# So this ship should consider to be Undying
				pSubName = None
				if pInstanceDict.has_key('Ablative Armour'): # Support for ablative armour
					try:
						repair = pInstanceDict['Ablative Armour']

						pSubName = "Ablative Armour"
						if str(repair)[0] == "[":
							pSubName = repair[1]
					except:
						pSubName = None

				if not pInstanceDict.has_key('Undying Comeback state'):
					pInstanceDict['Undying Comeback state'] = 0

				factor = 1.0
				if pInstanceDict['Undying Comeback'].has_key("Damage Factor"):
					factor = pInstanceDict['Undying Comeback']["Damage Factor"]

				pHull = pShip.GetHull()
				if pInstanceDict.has_key('Undying Comeback damage'):
					undyneComebackDamage = pInstanceDict['Undying Comeback damage']
					if not pHull or pHull.GetMaxCondition() * factor > undyneComebackDamage:
						pInstanceDict['Undying Comeback state'] == 2 # We are gonna assume you went undying already
				else:
					if pInstanceDict.has_key('Undying Comeback last hit') and pInstanceDict['Undying Comeback last hit'] != None:
						# We had more attacks before, now to know if the last attack was the culprit
						if not pHull or pHull.GetMaxCondition() * factor > pInstanceDict['Undying Comeback last hit'] and pInstanceDict['Undying Comeback last hit'] > 0.0:
							pInstanceDict['Undying Comeback state'] == 2 # We are gonna assume you went undying already

				if pInstanceDict['Undying Comeback state'] == 1:
					undyneComebackState = pInstanceDict['Undying Comeback state']
					if pHull:
						global DEFAULT_BOOST, DEFAULT_WEAPON_BOOST

						toChangeOntoUndyingFully = 1
						
						boost = DEFAULT_BOOST
						if pInstanceDict['Undying Comeback'].has_key('Boost') and pInstanceDict['Undying Comeback']["Boost"] > 0.0:
							boost = pInstanceDict['Undying Comeback']["Boost"]

						shieldboost = DEFAULT_BOOST
						if pInstanceDict['Undying Comeback'].has_key('Shield Boost') and pInstanceDict['Undying Comeback']["Shield Boost"] > 0.0:
							shieldboost = pInstanceDict['Undying Comeback']["Shield Boost"]

						energyboost = DEFAULT_BOOST
						if pInstanceDict['Undying Comeback'].has_key('Energy Boost') and pInstanceDict['Undying Comeback']["Energy Boost"] > 0.0:
							energyboost = pInstanceDict['Undying Comeback']["Energy Boost"]
								
						weaponBoost = DEFAULT_WEAPON_BOOST
						if pInstanceDict['Undying Comeback'].has_key("Weapon Boost"):
							boost = pInstanceDict['Undying Comeback']["Weapon Boost"]

						pHullMax = pHull.GetMaxCondition()
						if pHullMax <= 0.0:
							pHullMax = 0.0000001
						if not pInstanceDict.has_key('Undying Comeback damage'):
							pInstanceDict['Undying Comeback damage'] = pHullMax

						lethalDamageWas = pInstanceDict['Undying Comeback damage']
						ratioDmgVsHealth = lethalDamageWas/pHullMax * boost # How much we need to multiply our health

						pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
						pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

						while pSubsystem:
							BoostSubsystem(pSubsystem, boost, weaponBoost, shieldboost, energyboost, lethalDamageWas, ratioDmgVsHealth, pHullMax, pInstanceDict, pSubName)
							iChildren = pSubsystem.GetNumChildSubsystems()
							if iChildren > 0:
								for iIndex in range(iChildren):
									pChild = pSubsystem.GetChildSubsystem(iIndex)
									if pChild:
										BoostSubsystem(pChild, boost, weaponBoost, shieldboost, energyboost, lethalDamageWas, ratioDmgVsHealth, pHullMax, pInstanceDict, pSubName)

							pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
						pShip.EndGetSubsystemMatch(pIterator)

					# Now refresh the damage:
					sNewShipScript = None
					if pInstanceDict['Undying Comeback'].has_key('Model') and pInstanceDict['Undying Comeback']['Model'] != "" and pInstanceDict['Undying Comeback']['Model'] != "__init__":
						sNewShipScript = pInstanceDict['Undying Comeback']['Model']
					else:
						sNewShipScript = pShip.GetScript()

					if sNewShipScript != None:
						ReplaceModel(pShip, sNewShipScript)

					#MissionLib.ShowSubsystems(1) #On a dead ship this does not work :/

					#pShip.ClearAI()
					pShip.UpdateNodeOnly()
					if toChangeOntoUndyingFully > 0:
						pInstanceDict['Undying Comeback state'] = 2
						pPlayer	= MissionLib.GetPlayer()
						if pShip.GetObjID() == pPlayer.GetObjID() or MPIsPlayerShip(pShip):
							try:
								pSequence = App.TGSequence_Create ()
								pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
								pSequence.Play()
							except:
								print "Error when leaving cutscene"
								traceback.print_exc()

						else:
							StopOverridingAI(pShip)
							#oldAI = pShip.GetAI()
							#if oldAI:
							#	oldAI.Reset()
							

						try:
							pSequence = App.TGSequence_Create()
							pAction = App.TGScriptAction_Create(__name__, "PlayButTheEarthRefusedToDie", pShipID, 2, musicToPlay)
							pSequence.AddAction(pAction, None, 0)
							pSequence.Play()
						except:
							print "Error on Undying second Sequence"
							traceback.print_exc()

						pShip.SetDeathScript(None)
				else:
					pShip.SetDeathScript(None)
					pShip.RunDeathScript()
	return 0

def TransformIntoUndyingPhaseI(pShip, pInstance, pInstanceDict, pHull):
	if not pInstanceDict.has_key('Undying Comeback state'):
		pInstanceDict['Undying Comeback state'] = 0
	if pInstanceDict['Undying Comeback state'] <= 0:
		pInstanceDict['Undying Comeback state'] = 0.5

		oldAI = pShip.GetAI()
					
		pPlayer	= MissionLib.GetPlayer()
		if pShip.GetObjID() != pPlayer.GetObjID() and not MPIsPlayerShip(pShip):
			OverrideAI(pShip, "AI.Player.Stay", pShip)


		pShipID = pInstance.pShipID
		if not pShipID:
			pShipID = pShip.GetObjID()
		if pShipID != App.NULL_ID:
			try:
				pSequence = App.TGSequence_Create()
				pAction = App.TGScriptAction_Create(__name__, "TransformIntoUndyingPhaseIa", pShipID)
				pSequence.AddAction(pAction, None, 1.5)
				pSequence.Play()
			except:
				print "Error on Undying Sequence"
				traceback.print_exc()
	return 0


def TransformIntoUndyingPhaseIa(pAction, pShipID):
	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	toChangeOntoUndyingFully = 0
	if pShip:
		pInstance = findShipInstance(pShip)
		if pInstance and pInstance.__dict__.has_key('Undying Comeback'):
			# So this ship should consider to be Undying
			pInstanceDict = pInstance.__dict__

			if not pInstanceDict.has_key('Undying Comeback state'):
				pInstanceDict['Undying Comeback state'] = 0
			if pInstanceDict['Undying Comeback state'] <= 0.5:
				pInstanceDict['Undying Comeback state'] = 1
				shouldIcontinue = 1
				factor = 1.0
				if pInstanceDict['Undying Comeback'].has_key("Damage Factor"):
					factor = pInstanceDict['Undying Comeback']["Damage Factor"]
				pHull = pShip.GetHull()
				if not pHull:
					shouldIcontinue = 0
				else:
					if pInstanceDict.has_key('Undying Comeback damage'):
						undyneComebackDamage = pInstanceDict['Undying Comeback damage']
						if pHull.GetMaxCondition() * factor > undyneComebackDamage:
							shouldIcontinue = 0
					else:
						if pInstanceDict.has_key('Undying Comeback last hit') and pInstanceDict['Undying Comeback last hit'] != None:
							# We had more attacks before, now to know if the last attack was the culprit
							if pHull.GetMaxCondition() * factor > pInstanceDict['Undying Comeback last hit'] and pInstanceDict['Undying Comeback last hit'] > 0.0:
								shouldIcontinue = 0

				if shouldIcontinue == 1:
					global defaultLoadSound, defaultSound, defaultTimeToUndie

					timeForUndeath = defaultTimeToUndie
					if pInstanceDict['Undying Comeback'].has_key("TimeToUndie") and pInstanceDict['Undying Comeback']["TimeToUndie"] >= 0.0:
						timeForUndeath = pInstanceDict['Undying Comeback']["TimeToUndie"]

					musicForLoading = defaultLoadSound
					if pInstanceDict['Undying Comeback'].has_key("LoadSound"):
						musicForLoading = pInstanceDict['Undying Comeback']["LoadSound"]

					musicForUndying = defaultSound
					if pInstanceDict['Undying Comeback'].has_key("Sound"):
						musicForUndying = pInstanceDict['Undying Comeback']["Sound"]

					pShipID = pInstance.pShipID
					if not pShipID:
						pShipID = pShip.GetObjID()
					if pShipID != App.NULL_ID:
						try:
							pSequence = App.TGSequence_Create()
							pAction = App.TGScriptAction_Create(__name__, "PlayButTheEarthRefusedToDie", pShipID, 1, musicForLoading)
							pSequence.AddAction(pAction, None, 0)
							pAction = App.TGScriptAction_Create(__name__, "TransformIntoUndyingPhaseII", pShipID, musicForUndying)
							pSequence.AddAction(pAction, None, timeForUndeath)
							pSequence.Play()
						except:
							print "Error on Undying Sequence"
							traceback.print_exc()
				else:
					#print "I will not die! I will not die! I  w i l l  n o t  d i e ! 'dies'"
					pShip.SetDeathScript(None)
					pShip.RunDeathScript()
	return 0

def newDeathSeq(*args, **kwargs):
	pShip = None
	for arg in args:
		if hasattr(arg, "GetObjID"):
			temppShipID = arg.GetObjID()
			if temppShipID:
				pShip = App.ShipClass_GetObjectByID(None, temppShipID)
				if pShip:
					pInstance = findShipInstance(pShip)
					if pInstance:
						pInstanceDict = pInstance.__dict__
						if pInstanceDict.has_key('Undying Comeback'):
							# So this ship should consider to be Undying
							if not pInstanceDict.has_key('Undying Comeback state'):
								pInstanceDict['Undying Comeback state'] = 0
							undyneComebackState = pInstanceDict['Undying Comeback state']
							pHull = pShip.GetHull()
							if pHull and not undyneComebackState == 2:
								factor = 1.0
								if pInstanceDict['Undying Comeback'].has_key("Damage Factor"):
									factor = pInstanceDict['Undying Comeback']["Damage Factor"]
								if undyneComebackState <= 0: # Avoid calling 346238523472349 times for undying if under too much pressure
									if pInstanceDict.has_key('Undying Comeback damage'):
										undyneComebackDamage = pInstanceDict['Undying Comeback damage']

										if pHull.GetMaxCondition() * factor < undyneComebackDamage:
											TransformIntoUndyingPhaseI(pShip, pInstance, pInstanceDict, pHull)
										else:
											TransformIntoUndyingPhaseI(pShip, pInstance, pInstanceDict, pHull)
										#	print "I will not die! I will not die! I  w i l l  n o t  d i e ! 'dies'"
										#	pShip.SetDeathScript(None)
										#	pShip.RunDeathScript()	
											
									else:
										if pInstanceDict.has_key('Undying Comeback last hit') and pInstanceDict['Undying Comeback last hit'] != None:
											# We had more attacks before, now to know if the last attack was the culprit
											if pHull.GetMaxCondition() * factor < pInstanceDict['Undying Comeback last hit'] and pInstanceDict['Undying Comeback last hit'] > 0.0:
												TransformIntoUndyingPhaseI(pShip, pInstance, pInstanceDict, pHull)
											else:
												TransformIntoUndyingPhaseI(pShip, pInstance, pInstanceDict, pHull)
											#	print "I will not die! I will not die! I  w i l l  n o t  d i e ! 'dies'"
											#	pShip.SetDeathScript(None)
											#	pShip.RunDeathScript()	
										else:
											# This means the attack was so frigging powerful it killed us before we could do a thing - so yeah, we need to remain undying
											TransformIntoUndyingPhaseI(pShip, pInstance, pInstanceDict, pHull)
							else:
								# Something's very wrong if you don't have a hull subsystem, or you have already gone Undying and cannot go Undying forever
								#print "I will not die! I will not die! I  w i l l  n o t  d i e ! 'dies'"
								pShip.SetDeathScript(None)
								pShip.RunDeathScript()	
						else:
							# This ship should not be undead
							#print "I will not die! I will not die! I  w i l l  n o t  d i e ! 'dies'"
							pShip.SetDeathScript(None)
							pShip.RunDeathScript()	
					else:
						# This ship should not be undead
						#print "I will not die! I will not die! I  w i l l  n o t  d i e ! 'dies'"
						pShip.SetDeathScript(None)
						pShip.RunDeathScript()

# Replaces the Model of pShip, modification from AdvArmorTechThree
def ReplaceModel(pShip, sNewShipScript):
	debug(__name__ + ", ReplaceModel")
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return 0

	ShipScript = __import__('ships.' + sNewShipScript)
	ShipScript.LoadModel()
	kStats = ShipScript.GetShipStats()
	pShip.SetupModel(kStats['Name'])
	if App.g_kUtopiaModule.IsMultiplayer():
		MPSentReplaceModelMessage(pShip, sNewShipScript)

	# Because hiding and unhiding the ship does not seem to do the job of fixing the weird lack of lights, but something like this dumb thing below does :/
	from ftb.Tech.ATPFunctions import *

	point = pShip.GetWorldLocation()
	pHitPoint = App.TGPoint3()
	pHitPoint.SetXYZ(point.x, point.y, point.z)

	pVec = pShip.GetVelocityTG()
	pVec.Scale(0.001)
	pHitPoint.Add(pVec)

	mod = "Tactical.Projectiles.AutomaticSystemRepairDummy" 
	try:
		pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pShip.GetObjID(), pShip.GetObjID(), __import__(mod).GetLaunchSpeed())
		pTempTorp.SetHidden(1)
		pTempTorp.SetLifetime(0.0)
	except:
		print "You are missing 'Tactical.Projectiles.AutomaticSystemRepairDummy' torpedo on your install, without that a weird black-texture-until-firing-or-fired bug may happen"


def SubDamage(pObject, pEvent):
	debug(__name__ + ", SubDamage")
	pShip = App.ShipClass_Cast(pObject)
	if pShip:
		pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
		if pShip:
			pInstance = findShipInstance(pShip)
			if pInstance:
				pInstanceDict = pInstance.__dict__
				if pInstanceDict.has_key('Undying Comeback'):
					# So this ship should consider to be Undying
					pHull = pShip.GetHull()
					if not pInstanceDict.has_key('Undying Comeback state'):
						pInstanceDict['Undying Comeback state'] = 0
					undyneComebackState = pInstanceDict['Undying Comeback state']
					if pHull and not undyneComebackState <= 0.5:
						hull_max=pHull.GetMaxCondition()
						hull_cond=pHull.GetCondition()
						if pInstanceDict.has_key("Undying Comeback I") and pInstanceDict["Undying Comeback I"].has_key("SystemsToCheck") and pInstanceDict["Undying Comeback I"]["SystemsToCheck"].has_key(pHull.GetObjID()):
							if pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()].has_key("Current"):
								currentOldStatus = pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Current"]
								if pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()].has_key("Old"):
									oldOldStatus = pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Old"]
									if hull_cond != currentOldStatus:
										finalDamage = currentOldStatus - hull_cond
										if finalDamage > 0.0: # That means the hull got more damaged than last time
											factor = 1.0
											if pInstanceDict['Undying Comeback'].has_key("Damage Factor"):
												factor = pInstanceDict['Undying Comeback']["Damage Factor"]

											if (hull_max * factor < finalDamage) or (hull_max <= finalDamage):
												if not pInstanceDict.has_key('Undying Comeback damage') or (pInstanceDict['Undying Comeback damage'] <= 0.0):
														pInstanceDict['Undying Comeback damage'] = finalDamage
												elif pInstanceDict['Undying Comeback damage'] < finalDamage:
														pInstanceDict['Undying Comeback damage'] = finalDamage
												
										
										pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Old"] = pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Current"]
										pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Current"] = hull_cond
	return 0


try:
	class UndyingComebackDef(FoundationTech.TechDef):
		def __init__(self, name):
			FoundationTech.TechDef.__init__(self, name)
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)
			App.g_kEventManager.RemoveBroadcastHandler(ET_CRITICAL_SYSTEM_AT_100, self.pEventHandler, "Test")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_CRITICAL_SYSTEM_AT_100, self.pEventHandler, "Test")

		def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnBeamDefense")
			if pEvent.IsHullHit():
				return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnPulseDefense")
			if pEvent.IsHullHit():
				return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnTorpDefense")
			if pEvent.IsHullHit():
				return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnDefense")
			pInstanceDict = pInstance.__dict__
			if pInstanceDict.has_key('Undying Comeback'):
				pHull = pShip.GetHull()
				if pHull:
					absDamage = abs(pEvent.GetDamage())
					factor = 1.0
					if pInstanceDict['Undying Comeback'].has_key("Damage Factor"):
						factor = pInstanceDict['Undying Comeback']["Damage Factor"]
					if pHull.GetMaxCondition() * factor < absDamage:
						if pInstanceDict.has_key('Undying Comeback damage'):
							if not pInstanceDict.has_key('Undying Comeback state'):
								pInstanceDict['Undying Comeback state'] = 0
							#None or 0 = Pre-undying, 1 = transforming, 2 = post-undying
							if pInstanceDict['Undying Comeback state'] <= 0.5:
								if absDamage > pInstanceDict['Undying Comeback damage']:
									pInstanceDict['Undying Comeback damage'] = absDamage
								pInstanceDict['Undying Comeback last hit'] = absDamage
							elif pInstanceDict['Undying Comeback state'] == 1:
								pInstanceDict['Undying Comeback damage'] = absDamage + pInstanceDict['Undying Comeback damage']	
						else:
							pInstanceDict['Undying Comeback damage'] = absDamage
					else:
						pInstanceDict['Undying Comeback last hit'] = absDamage
		

		def Test(self, pFloatEvent):
			fFraction = pFloatEvent.GetFloat()
			pSubsystem = App.ShipSubsystem_Cast(pFloatEvent.GetSource())
			pShip = pSubsystem.GetParentShip()
			if pShip:
				pInstance = findShipInstance(pShip)
				if pInstance:
					pInstanceDict = pInstance.__dict__
					if pInstanceDict.has_key("Undying Comeback") and pInstanceDict.has_key("Undying Comeback I") and pInstanceDict["Undying Comeback I"].has_key("SystemsToCheck"):
						myfFraction = 1.1 # Impossible to reach, ergo a good default value
						if pInstanceDict["Undying Comeback I"]["SystemsToCheck"].has_key(pSubsystem.GetObjID()) and pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()].has_key("Fraction"):
							myfFraction = pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()]["Fraction"]
					
						if fFraction >= myfFraction:
							pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()]["Complies"] = 1
							pHull = pShip.GetHull()
							if pHull.GetObjID() == pSubsystem.GetObjID():
								hull_max=pHull.GetMaxCondition()
								if pInstanceDict["Undying Comeback I"]["SystemsToCheck"].has_key(pHull.GetObjID()):
									if pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()].has_key("Current"):
										pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Current"] = fFraction * hull_max
									if pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()].has_key("Old"):
										pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pHull.GetObjID()]["Old"] = fFraction * hull_max						
						else:
							pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()]["Complies"] = 0

						totalComply = pInstanceDict["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()]["Complies"]
						for subSysID in pInstanceDict["Undying Comeback I"]["SystemsToCheck"].keys():
							if pInstanceDict["Undying Comeback I"]["SystemsToCheck"][subSysID]["Complies"] == 0:
								totalComply = 0
								break

						if totalComply == 1:
							try:
								if pInstanceDict.has_key('Undying Comeback last hit'):
									pInstanceDict['Undying Comeback last hit'] = None
							except:
								pass


		def Attach(self, pInstance):
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)
			pInstance.lBeamDefense.append(self)
			pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)
			if pShip != None:

				pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
				#import copy
		
				oldRunDeathSeq = pShip.RunDeathScript
				if oldRunDeathSeq != None:
					pShip.SetDeathScript(__name__ + ".newDeathSeq")

					pInstanceDict = pInstance.__dict__
					factor = 1.0
					if pInstanceDict['Undying Comeback'].has_key("Damage Factor"):
						factor = pInstanceDict['Undying Comeback']["Damage Factor"]
					else:
						pInstanceDict['Undying Comeback']["Damage Factor"] = factor

					if factor > 1.0:
						factor = 1.0

					global ET_CRITICAL_SYSTEM_AT_100

					pShipSet = pShip.GetPropertySet()
					pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
					iNumItems = pShipList.TGGetNumItems()

					pShipList.TGBeginIteration()
					for i in range(iNumItems):
						pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
						pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)
						if pSubsystem.IsCritical():

							pEvent = App.TGFloatEvent_Create()
							pEvent.SetEventType( ET_CRITICAL_SYSTEM_AT_100 )
							pEvent.SetDestination( self.pEventHandler )
							pEvent.SetSource( pSubsystem )

							maxCond = pSubsystem.GetMaxCondition()
							if maxCond <= 0.0:
								maxCond = 1.0
							fFraction = (1.0 - (1.0/maxCond)) * factor
							pWatcher = pSubsystem.GetConditionWatcher()
							iRangeID = pWatcher.AddRangeCheck( fFraction, App.FloatRangeWatcher.FRW_BOTH, pEvent )
							if pInstance and pInstance.__dict__.has_key("Undying Comeback"):
								if not pInstance.__dict__.has_key("Undying Comeback I"):
									pInstance.__dict__["Undying Comeback I"] = {}
								if not pInstance.__dict__["Undying Comeback I"].has_key("SystemsToCheck"):
									pInstance.__dict__["Undying Comeback I"]["SystemsToCheck"] = {}
								pInstance.__dict__["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()] = {"Complies": 1, "Fraction": fFraction, "Current": maxCond, "Old": maxCond}
								pInstance.__dict__["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()]["Watcher"] = iRangeID

					pShipList.TGDoneIterating()
					pShipList.TGDestroy()
			
		def Detach(self, pInstance):
			pInstance.lTorpDefense.remove(self)
			pInstance.lPulseDefense.remove(self)
			pInstance.lBeamDefense.remove(self)
			if pInstance:
				pInstanceDict = pInstance.__dict__
				try:
					if pInstanceDict.has_key('Undying Comeback damage'):
						del pInstanceDict['Undying Comeback damage']
				except:
					pass
				try:
					if pInstanceDict.has_key('Undying Comeback last hit'):
						del pInstanceDict['Undying Comeback last hit']
				except:
					pass
				try:
					if pInstanceDict.has_key('Undying Comeback state'):
						del pInstanceDict['Undying Comeback state']
				except:
					pass

				pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
				if pShip != None:
					pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_DAMAGED, __name__ + ".SubDamage")
					pShipSet = pShip.GetPropertySet()
					pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
					iNumItems = pShipList.TGGetNumItems()

					pShipList.TGBeginIteration()
					for i in range(iNumItems):
						pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
						pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)

						iInfo = None
						try:
							iInfo = pInstance.__dict__["Undying Comeback I"]["SystemsToCheck"][pSubsystem.GetObjID()]["Watcher"]
						except:
							iInfo = None

						if iInfo is not None:
							pWatcher = pSubsystem.GetConditionWatcher()
							pWatcher.RemoveRangeCheck( iInfo )

						try:
							App.g_kTimerManager.DeleteTimer(pInstance.__dict__['Undying Comeback I'][pSubsystem.GetObjID()]['Timer'].GetObjID())
						except:
							pass
					
				
					pShipList.TGDoneIterating()
					pShipList.TGDestroy()

				del pInstance.__dict__["Undying Comeback I"]["SystemsToCheck"]
				del pInstance.__dict__["Undying Comeback I"]
					
			pInstance.lTechs.remove(self)


	oUndyingComeback = UndyingComebackDef('Undying Comeback')
except:
	print "Something went wrong with 'Undying Comeback':"
	traceback.print_exc()