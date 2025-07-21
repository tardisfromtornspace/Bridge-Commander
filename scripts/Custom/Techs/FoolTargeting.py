#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         FoolTargeting.py by Alex SL Gato
#         Version 0.45
#         21st July 2025
#         Based on BorgAdaptation.py by Alex SL Gato, which was based on the Shield.py script by the Foundation Technologies team and Dasher42's FoundationTech script.
#         Also based on ATPFunctions by Apollo and Sneaker's Innacurate Phaser mod.
#################################################################################################################
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech modifies Innacurate Phaser Fire and adds the option to adjust the innacuracy for phasers, torps and disruptors as well.
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev. Also this technology works as "1" technology ("Fool Targeting") with associated "subTechnologies" that people can create without the need to modify this file. On this case there's
# "Minbari Stealth", if you want another tech, replace "Minbari Stealth" with another name.
# Also, there is a special subTech here "Accurate", which is made explicitly to modify the regular fMiss, and acts as a multiplier - a factor of 0.0 will make it always hit (unless another Tech interferes) while 2.0 
#  will make it miss twice as much. As this is a special subTech, it will not attempt to load any other subTech called "Accurate" (nor "accurate", either, for preventing issues with case-insensitive os).
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Fool Targeting": {
		"Minbari Stealth": {
			"sensor": 600
		},
		"Accurate": 0.0  
	}
}
"""
# As those with some idea of python language can see, you can stack more than 1 subtech, that is, if you wanted to add "Electronic-Counter Measures" alongside "Minbari Stealth", you could do the following. Also please take into account 
# that since people can create a sub-Tech, all parameters inside the scope of the Electronic-Counter Measures "{}" are custom parameters for such Custom techs.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Fool Targeting": {
		"Electronic-Counter Measures": {
			"sensor": 600
		},
		"Minbari Stealth": {
			"sensor": 600
		},
		"Accurate": 0.0 # regular innacurate fire things will not affect this ship fire     
	}
}
"""
# If you want an new specific subTech that modifies part of the accuracy, you can do it by adding a file under the scripts\Custom\Techs\FoolTargetingScripts directory; named like the Technology. For example, if the special sub-tech
# is called "Minbari Stealth" you can call the file "Minbari Stealth.py";
# Below there's an example used for the aforementioned Minbari Stealth, at least the 1.0 version, but with some parts commented so as to not trigger commentary issues - those sections have replaced the triple " with ####@@@
# From version 0.4 onwards, subTechs can also return a dictionary for fMiss to not only modify a fMiss factor, but where that fMiss is gonna be located:
# * If a dictionary, the key "fMiss" will store the actual fMiss value, while the key "kNewLocation" will store the fMiss vector to use as direction of the miss - if the latter is not added, the targeting goes for a random unit vector.
# On both cases, if the "kNewLocation" is not added, it will use the normal random unit vector, as usual. Please notice that while this vector can also be used to assign magnitude of miss, that is fMiss's job and any changes done to the "kNewLocation" are not directly stackable!
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19 April 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the FoolTargeting Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/FoolTargetingScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This tech adds a miss to the values if the attacker's sensor range is below a threshold. Affects both phasers and torps/pulses
# How-to-use:
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
# Special fields:
# - "Sensor": at this value or below, the attacker will have its attacks scrambled. Default is 100.
# - "Miss": this value will indicate by how much they will miss. Default is 2.0
# EXTRA NOTES: "Tachyon Sensors" is an ECM-amplifier and EECM. "Tachyon Sensors" is an entirely different tech, which will give pros and cons (pros, chance at detecting non-phased cloaked vessels upon scanning area; cons, this, being
# more vulnerable to Minbari Stealth), "Tachyon Sensors": 1. See more of this Minbari Stealth script for notes.
####@@@
Foundation.ShipDef.Ambassador.dTechs = {
	"Fool Targeting": {
		"Minbari Stealth": {
			"Miss": 2.0,
			"Sensor": 600,
		}  
	}
}
####@@@
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
globalPrimitiveSensor = 100
globalfMissExtra = 2.0

def commonFunction(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, pTorp, fSensorRange, fAngleDiff, fObjectDistance):
	debug(__name__ + ", commonFunction")
	primitiveSensor = globalPrimitiveSensor
	if pInstanceFool and pInstanceFool[techName].has_key("Sensor"):
		primitiveSensor = pInstanceFool[techName]["Sensor"]
	fMissExtra = 0.0
	try:
		extraMultiplier = 1.0
		effortMultiplier = 1.0
		if pAttackerInstance and pAttackerInstance.__dict__.has_key("Tachyon Sensors"): # These are both an ECM-amplifier, and an EECM - set to 1.0 or lower for Minbari Vessels which are unaffected by their own Stealth, and advanced races with very advanced tachyon sensors, like the Vorlons and other First-One ships, higher than 1.0 for other ships using exclusively Tachyon sensors.
			extraMultiplier = pAttackerInstance.__dict__["Tachyon Sensors"]

		pDefendingShip = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
                if pDefendingShip:
			pShields = pDefendingShip.GetShields()
			if pShields:
				effortMultiplier = pShields.GetConditionPercentage() * pShields.GetPowerPercentageWanted()
			if effortMultiplier > 1.24:
				effortMultiplier = 1.24
		if extraMultiplier * effortMultiplier * primitiveSensor > fSensorRange:
			fMissExtra = globalfMissExtra
			if pInstanceFool and pInstanceFool[techName].has_key("Miss"):
				fMissExtra = pInstanceFool[techName]["Miss"]
			
	except:
		print "Error while doing Minbari Stealth beam condition"
		traceback.print_exc()
		fMissExtra = 0.0

	return fMiss + fMissExtra

###### One or both of these two following functions must always exist for the parent script to take into account their innacuracy. Both must return fMiss, with fMiss finally being the accumulated values for all subTechs ######
# if instead of being called "beamCondition" it is called "beamAttackerOnlyCondition", it will be used exclusively from the attacker's instance standpoint - this uses a slightly modified logic where pInstanceFool is the attacker's not the defender's
def beamCondition(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, fSensorRange, fAngleDiff, fObjectDistance): # Establishes a random factor - values must be >= 0. The greater the value, the more range can happen between sessions.
	debug(__name__ + ", beamCondition")
	#print "Minbari stealth beam function called"
	return commonFunction(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, None, fSensorRange, fAngleDiff, fObjectDistance)

def pulseTCondition(techName, pInstanceFool, fMiss, pAttackerShip, pAttackerInstance, pDefenderShip, pDefenderInstance, pTorp): # Establishes the minimum number of strikes before it adapts, stacking along the random value above - please notice some weapons deal multi-strikes. Values must be >= 0
	debug(__name__ + ", pulseTCondition")
	#print "Minbari stealth torp and pulse function called"

	pDefenderShip = App.ShipClass_GetObjectByID(None, pDefenderShip.GetObjID())
	if pDefenderShip:
		fSensorRange = 0.0
		pSensor = None
		pAttackerShip = App.ShipClass_GetObjectByID(None, pAttackerShip.GetObjID())
		if pAttackerShip:
			pSensor = pAttackerShip.GetSensorSubsystem()
		if pSensor:
			fSensorRange = pSensor.GetSensorRange()
	        	# calculate Sensor Damage and power into Range
			fSensorRange = fSensorRange * pSensor.GetConditionPercentage() * pSensor.GetPowerPercentageWanted()

		return commonFunction(techName, pInstanceFool, fMiss, pAttackerShip, pAttackerInstance, pDefenderShip, pDefenderInstance, pTorp, fSensorRange, None, None)
	else:
		return 0.0
"""

# EXTRA!!!! THIS SCRIPT SUPPORTS 'DISABLING' REGULAR INACCURATE PHASER FIRE WHILE KEEPING INACCURATEFIRE WORKING SO TECHS CAN STILL MAKE IT MISS - YOu just need to create a scripts.Custom.Autoload fire where the commented example below is pasted - recommended to call the file "TWEAK-InaccuratePhasersTechMissRedu.py" so we all know what it does.
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 21st July 2025
# VERSION 0.1
# By Alex SL Gato
#
# Changes: 
# - This file is related to the FoolTargeting Tech and makes all phasers to not miss.

from bcdebug import debug
import App


necessaryToUpdate = 0
FoolTargeting = None
try:
	import Foundation
	import FoundationTech
	necessaryToUpdate = 1
except:
	print "Unable to find fTech"
	necessaryToUpdate = 0
	pass

if necessaryToUpdate == 1:
	try:
		FoolTargeting = __import__("Custom.Techs.FoolTargeting") #from ftb.Tech import FoolTargeting
	except:
		FoolTargeting = None
	if FoolTargeting != None and hasattr(FoolTargeting,"ApplyPseudoMonkeyPatch") and hasattr(FoolTargeting,"necessaryToUpdate") and hasattr(FoolTargeting,"basicMissMult"):
			FoolTargeting.ApplyPseudoMonkeyPatch()
			FoolTargeting.necessaryToUpdate = 0
			FoolTargeting.basicMissMult = 0.0
			print "Patched FoolTargeting to not miss from regular InaccurateFire"
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.45",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

import App

import Foundation
import FoundationTech
import MissionLib

import nt
import math
import string

from bcdebug import debug
import traceback

necessaryToUpdate = 0 # Who knows, we may not need to update this on newer versions...
ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer
totalShips = 0 # We count how many ships we have with this technology.
basicMissMult = 1.0 # We can use this to patch this later to outright disable missing from typical inaccurate phaser effects.
oldInnacurateFire = FoundationTech.InaccurateFire # The old function we have for InnacurateFire - yes, in a way part of this is a bit like Monkey Patching, but temporary

# "variableNames" is a global dictionary, filled automatically by the files in scripts/Custom/Techs/FoolTargetingScripts 
# the purpose of this list is to append dicts f.ex. {"name": "Minbari Stealth", "beamcondition": functionObtained, "pulsetcondition": anotherfunctionObtained}
# the "name" field indicates which sub-tech is being used to fool or improve the accuracy.
# the "beamcondition" will have a function that will be called to calculate the new innacurate fire for phasers, those functions will stack.
# the "pulsetcondition" will try to do the same, but for torpedoes and pulses.
# "attackerOnly" is reserved ONLY for things the attacker can do - this is often reserved to beams only, as torpedoes can be handled pretty much in every other way via guidanceLifetime or any other projectile stats.

variableNames = {}
attackerOnly = {}

if int(Foundation.version[0:8]) < 20231231: # we are gonna assume the 2023 version and previous versions lack this
	necessaryToUpdate = 1

_g_dExcludeBorgPlugins = {
	# Some random plugins that I don't want to risk people attempting to load using this tech
	"000-Fixes20030217": 1,
	"000-Fixes20030221": 1,
	"000-Fixes20030305-FoundationTriggers": 1,
	"000-Fixes20030402-FoundationRedirect": 1,
	"000-Fixes20040627-ShipSubListV3Foundation": 1,
	"000-Fixes20040715": 1,
	"000-Fixes20230424-ShipSubListV4_7Foundation": 1,
	"000-Utilities-Debug-20040328": 1,
	"000-Utilities-FoundationMusic-20030410": 1,
	"000-Utilities-GetFileNames-20030402": 1,
	"000-Utilities-GetFolderNames-20040326": 1,
	"Accurate": 1,
	"accurate": 1,
}

# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
def NiPoint3ToTGPoint3(p):
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		#print "Error while looking for pInstance for Borg technology:"
		#traceback.print_exc()
		pass

		
	#finally:
	return pInstance

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound

# Based on LoadExtraPlugins by Dasher42, but heavily modified so it only imports a thing
def LoadExtraLimitedPlugins(dExcludePlugins=_g_dExcludeBorgPlugins):

	dir="scripts\\Custom\\Techs\\FoolTargetingScripts" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	list = nt.listdir(dir)
	list.sort()

	dotPrefix = string.join(string.split(dir, "\\")[1:], ".") + "."

	for plugin in list:
		s = string.split(plugin, ".")
		if len(s) <= 1:
			continue
		
		# Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
		extension = s[-1]
		fileName = string.join(s[:-1], ".")

		# We don't want to accidentally load wrong things
		if (extension == "py") and not fileName == "__init__": # I am not allowing people to just use the .pyc directly, I don't want people to not include source scripts - Alex SL Gato
			#print "FoolTargeting script is reviewing " + fileName + " of dir " + dir
			if dExcludePlugins.has_key(fileName):
				debug(__name__ + ": Ignoring plugin" + fileName)
				continue

			try:
				if not variableNames.has_key(fileName):
					myGoodPlugin = dotPrefix + fileName
					
					# I really wanted to make it so it only imports these two methods, but it is not letting me do it :(
					# The only other secure option I could think about is making random files with the name and those two values in the name and then splitting them up, but if there's an update you would end up with rubbish as well
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounterRdm"])
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounter"])

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["beamCondition", "pulseTCondition"])
					except:
						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["beamCondition"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals(), ["pulseTCondition"])
					#banana = __import__(myGoodPlugin, globals(), locals())

					if hasattr(banana, "beamCondition"):
						variableNames[fileName] =  {}
						variableNames[fileName]["beamCondition"] = banana.beamCondition

					if hasattr(banana, "beamAttackerOnlyCondition"):
						attackerOnly[fileName] =  {}
						attackerOnly[fileName]["beamCondition"] = banana.beamAttackerOnlyCondition

					if hasattr(banana, "pulseTCondition"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["pulseTCondition"] = banana.pulseTCondition

					#print "Fool Targeting reviewing of this subtech is a success"
			except:
				print "someone attempted to add more than they should to the Fool Targeting script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print variableNames
#print necessaryToUpdate

# Alex SL Gato's change from Dasher42's slightly adjusted and refactored Inaccurate phasers, which were modifications from Sneaker's innaccurate phaser mod
global newInaccurateFire
def newInaccurateFire(pShip, pSystem, pTarget):
	debug(__name__ + ", InaccurateFire")
	if totalShips <= 0 and necessaryToUpdate:
		#print("Old Innacurate phasers function called")
		oldInnacurateFire(pShip, pSystem, pTarget)
	else:
		#print("New Innacurate phasers function called")
		fMiss = 0.0
		fSensorRange = 200.0

		vAngle = pTarget.GetAngularVelocity()
		fAngleDiff = vAngle.x + vAngle.y + vAngle.z
		vAngle = pTarget.GetAcceleration()
		fAngleDiff = fAngleDiff + vAngle.x + vAngle.y + vAngle.z

		if fAngleDiff < 0.0:
			fAngleDiff = fAngleDiff * -5.0
		else:
			fAngleDiff = fAngleDiff * 5.0

		vTargetLocation = pTarget.GetWorldLocation()
		vTargetLocation.Subtract(pSystem.GetWorldLocation())
		fObjectDistance = vTargetLocation.Unitize()
	
		#fSizeFactor = 1.5 / (pTarget.GetRadius() + 0.01)
		pSensor = pShip.GetSensorSubsystem()
		if pSensor:
			fSensorRange = pSensor.GetSensorRange()
		else:
			fSensorRange = 0.0

	        #fSensorRange = fSensorRange * (1.5 / (pTarget.GetRadius() + 0.01))
	        # calculate Sensor Damage and power into Range
		if pSensor:
			fSensorRange = fSensorRange * pSensor.GetConditionPercentage() * pSensor.GetPowerPercentageWanted()

		# Alex SL Gato: We love innacurate phasers, but not that much when the target is literally still at 10 units from you and keep missing. Changing 2.2 to 1.0 and 0.15, and made it so sensors are better
		# If you want your ship to miss more or less, just add a sub-Tech from this that adjust the fMiss accordingly
		# fMiss = ((fAngleDiff * fObjectDistance) * 2.2) / (fSensorRange + 1.0)
		fMiss = basicMissMult * (fAngleDiff * (1.0 + fObjectDistance * 0.15)) / (16 * fSensorRange + 1.0)

		# Now comes the really extra thing - we are adding countermeasures for both sides - there is going to be a sub-tech "Accurate" that will make normal non sub-Tech fire miss more or less, or nothing.
		# Additionally, the victim will have multiple ECM (Electronic Counter-Measures) and ECCM (Electronic Counter-Counter-Measures) that will add a Miss factor.
		# For those modders that want to add an ECCM for an ECM, remember it can be done in many ways, among them using things like SensorRange, customized options and even the Attacker's pInstance (so you can add ECCMs to those)
		pAttackerInstance = findShipInstance(pShip)
		pDefenderInstance = findShipInstance(pTarget)

		kNewLocation = App.TGPoint3_GetRandomUnitVector()
		if pAttackerInstance:
			pAttackerInstanceDict = pAttackerInstance.__dict__
			if pAttackerInstanceDict.has_key("Fool Targeting"):
				if pAttackerInstance.__dict__["Fool Targeting"].has_key("Accurate"): # This ship just cannot miss from regular innacurate fire things
					#print("Attacker has Fool Targeting Accuracy subTech")
					fMiss = fMiss * pAttackerInstance.__dict__["Fool Targeting"]["Accurate"]

				pInstanceFool = pAttackerInstanceDict["Fool Targeting"]
				for techName in attackerOnly.keys():
					if pInstanceFool.has_key(techName) and attackerOnly[techName].has_key("beamCondition"):
						try:
							#ok, it's a miss (or not), let's modifiy the Miss value so it is guaranteed to miss
							fMiss2 = attackerOnly[techName]["beamCondition"](techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, fSensorRange, fAngleDiff, fObjectDistance) # More liberty for a new tech to add incremental fMiss or totally ignore the other fMiss

							if type(fMiss2)==type({}):
								if fMiss2.has_key("kNewLocation"):
									kNewLocation = fMiss2["kNewLocation"]
								if fMiss2.has_key("fMiss"):
									fMiss = float(fMiss2["fMiss"])
							else:
								fMiss = fMiss2
						except:
							print("Error while reviewing a Fool Targeting tech beam attack function")
							traceback.print_exc()

		if pDefenderInstance:
			pInstanceDict = pDefenderInstance.__dict__ # Because all techs use this __dict__ thing to fetch their keys, sorry for the hacky code USS Sovereign
			if pInstanceDict.has_key("Fool Targeting"): # The real technology to use
				#print("Defender has Fool Targeting")
				global variableNames
				pInstanceFool = pInstanceDict["Fool Targeting"]
				for techName in variableNames.keys():
					if pInstanceFool.has_key(techName) and variableNames[techName].has_key("beamCondition"):
						try:
							#ok, it's a miss (or not), let's modifiy the Miss value so it is guaranteed to miss
							fMiss2 = variableNames[techName]["beamCondition"](techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, fSensorRange, fAngleDiff, fObjectDistance) # More liberty for a new tech to add incremental fMiss or totally ignore the other fMiss

							if type(fMiss2)==type({}): #fMiss2type is dictionary:
								if fMiss2.has_key("kNewLocation"):
									kNewLocation = fMiss2["kNewLocation"]
								if fMiss2.has_key("fMiss"):
									fMiss = float(fMiss2["fMiss"])
							else:
								fMiss = fMiss2
						except:
							print("Error while reviewing a Fool Targeting tech beam function")
							traceback.print_exc()						

		if fMiss > 2.0:
			fMiss = 2.0 + fMiss / 100.0

		#print 'miss', fMiss, ':', pShip.GetName(), ': a', fAngleDiff, 'd', fObjectDistance, 's', fSensorRange, pSensor.GetSensorRange()

		# Make Mark (Ignis) happier.:P
		#if App.Game_GetCurrentPlayer().GetObjID() != pShip.GetObjID() and not App.g_kUtopiaModule.IsMultiplayer():
		#	fMiss=fMiss*2.0

		if fMiss <= 0.0:
			pSystem.StartFiring(pTarget, pShip.GetTargetOffsetTG())
			pSystem.SetForceUpdate(1) # update and fire immediately

		else:
			# fMinDistance = 0.0
			# fDistance = fMinDistance + (fMaxDistance - fMinDistance) * fMiss

			# Scale the direction by the distance to get the position...
			kNewLocation.Scale(fMiss)
			kLocation = pShip.GetTargetOffsetTG()
			kLocation.Add(kNewLocation)

			pSystem.StartFiring(pTarget, kLocation)
			pSystem.SetForceUpdate(1) # update and fire immediately

def ApplyPseudoMonkeyPatch():
	global newInnacurateFire, oldInnacurateFire
	oldInnacurateFire = FoundationTech.InaccurateFire
	#print "oldInnacurateFire:", oldInnacurateFire
	#FoundationTech.InaccurateFire = newInnacurateFire # For some reason this does not work, why TO-DO???

	def whyNotWork(pShip, pSystem, pTarget):
		return newInaccurateFire(pShip, pSystem, pTarget)
	FoundationTech.InaccurateFire = whyNotWork

def RemovePseudoMonkeyPatch():
	global newInnacurateFire, oldInnacurateFire
	FoundationTech.InnacurateFire = oldInnacurateFire

class FoolTargetingDef(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated Reality Bomb counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		if necessaryToUpdate:
			ApplyPseudoMonkeyPatch()

	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		#pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		#pInstance.lPulseDefense.insert(0, self)
		#pInstance.lBeamDefense.insert(0, self)
		#print 'Attaching Fool Targeting to', pInstance, pInstance.__dict__
		global necessaryToUpdate, totalShips, oldInnacurateFire

		if totalShips <= 0: # First time, we set it to 1 and do the InnacurateFire change
			totalShips = 1
			#print("First time, or already went to 0, then a new one appeared")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpEnteredSet") # ET_TORPEDO_ENTERED_SET is better, specially to prevent MIRVs from all of a sudden recovering the lock
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpEnteredSet")
			#if necessaryToUpdate:
			#	#print "oldInnacurateFire:", oldInnacurateFire
			#	ApplyPseudoMonkeyPatch()
			#	#print "oldInnacurateFire:", oldInnacurateFire
		else:
			totalShips = totalShips + 1

	def Detach(self, pInstance):
		global necessaryToUpdate, totalShips, oldfunction
		totalShips = totalShips - 1
		if totalShips <= 0:
			#RemovePseudoMonkeyPatch()
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpFired") 
		pInstance.lTechs.remove(self)
		#print "FoolTargeting: detached from ship."	

	def TorpEnteredSet(self, pEvent):
		debug(__name__ + ", TorpFired")

		pTorp=App.Torpedo_Cast(pEvent.GetDestination())
		if (pTorp==None):
			return

		pAttackerShip = App.ShipClass_GetObjectByID(None, pTorp.GetParentID())
		pDefenderShip = App.ShipClass_GetObjectByID(None, pTorp.GetTargetID())

		# For torpedoes the things are a bit different - hit or miss, there's no torpedo innacuracy mod that existed beforehand... as far as I know. As such, we only get Attacker data for merely ECCM and ECM reasons.
		if pDefenderShip:
			fMiss = 0.0
			pAttackerInstance = None
			if pAttackerShip:
				pAttackerInstance = findShipInstance(pAttackerShip)
			pDefenderInstance = findShipInstance(pDefenderShip)
			if pDefenderInstance:
				pInstanceDict = pDefenderInstance.__dict__ # Sorry for the hacky code USS Sovereign
				if pInstanceDict.has_key("Fool Targeting"):
					#print("Defender has Fool Targeting")
					global variableNames
					pInstanceFool = pInstanceDict["Fool Targeting"]
					for techName in variableNames.keys():
						if pInstanceFool.has_key(techName) and variableNames[techName].has_key("pulseTCondition"):
							try:
								#ok, it's a miss (or not), let's modifiy the Miss value so it is guaranteed to miss
								fMiss = variableNames[techName]["pulseTCondition"](techName, pInstanceFool, fMiss, pAttackerShip, pAttackerInstance, pDefenderShip, pDefenderInstance, pTorp) # More liberty for a new tech to add incremental fMiss or totally ignore the other fMiss
							except:
								print "Error while reviewing a Fool Targeting tech pulseTorp function"
								traceback.print_exc()

			if fMiss > 2.0: # To keep with the regular innacurate phasers standards
				fMiss = 2.0 + fMiss / 100.0

			if fMiss > 0.0:
				#print ("Proceeding to make the torpedo miss with fMiss ", fMiss)
				# First we make the torpedo follow a straight line, then we re-orient it to a random offset according to fMiss
				pTorp.SetGuidanceLifetime(0.0)

				vTargetLocation = pDefenderShip.GetWorldLocation()
				vTorpLocation = pTorp.GetWorldLocation()

				kNewLocation = App.TGPoint3_GetRandomUnitVector()
				# Scale the direction by the distance to get the position...
				kNewLocation.Scale(fMiss)

				#vTargetLocation.Add(kNewLocation) # if this doesn't work, try to do SetX(GetX + kNewLocationX) and such

				vTargetLocation.SetX(vTargetLocation.GetX()+kNewLocation.GetX())
				vTargetLocation.SetY(vTargetLocation.GetY()+kNewLocation.GetY())
				vTargetLocation.SetZ(vTargetLocation.GetZ()+kNewLocation.GetZ())

				vTargetLocation.Subtract(vTorpLocation)

				kFwd = vTargetLocation
				kFwd.Unitize()

				kPerp = kFwd.Perpendicular()
				kPerp2 = App.TGPoint3()
				kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

				pTorp.AlignToVectors(kFwd, kPerp2)
				pTorp.UpdateNodeOnly()

				kVelocity = pTorp.GetWorldForwardTG()
				kVelocity.Scale(pTorp.GetLaunchSpeed())

				pTorp.SetVelocity(kVelocity)
				pTorp.UpdateNodeOnly()


		return



oFoolTargeting = FoolTargetingDef('Fool Targeting')