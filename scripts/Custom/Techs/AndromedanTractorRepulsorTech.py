# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 6th February 2026, by Alex SL Gato (CharaToLoki)
#         Based on SGAsgardBeamWeapon by Alex SL Gato, which was based on BorgAdaptation.py and PhasedTorp.py by Alex SL Gato, which were based on the Foundation import function by Dasher; the Shield.py scripts and KM Armour scripts and FoundationTechnologies team's PhasedTorp.py, on ATPFunctions by Apollo.
#         Also based on MEShields by Alex SL Gato, which was based on SGShields by Alex SL Gato, which was strongly based on Shields.py by the FoundationTechnologies team, ATPFunctions by Apollo, HelmMenuHandlers from the STBC Team, and MEGIonWeapon by Alex SL Gato.
#         Also upon noticing how App.WEAPON_HIT did not make the tractor work, based slightly on MLeo Daalder's Tractordef, but using Attach instead of AttachShip because of weird tech check errors.
#         This tech depends on FIX-FoundationTech20050703DefendVSTorpFix by Alex SL Gato to patch FoundationTech properly and make Tractor Events work continuously.
#################################################################################################################
#
# A modification of a modification, last modification by Alex SL Gato (CharaToLoki)
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech makes ships gain Andromedan Tractor Beam tech, which will 1. makes tractors be able to deal damage and 2. makes them deal the same damage regardless of distance. It still makes beam yields variable to 3 damage-dealing status with the phaser level slider or button: full-power (100%), half-power (>= 50%) and no damage (<50%) (useful for manually tractoring targets or when on green or yellow alert so a vessel does not harm another).
# To add it, just add to your Custom/Ships/shipFileName.py this:
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Andromedan Tractor-Repulsor Beams Weapon": [{"HullDmgMultiplier": 100.0, "ShieldDmgMultiplier": 1.0}, ["Beam Sound 1 to add", "Beam 2 sound to add"]],
}
"""
# "HullDmgMultiplier" will multiply upon the base global multiplier for hull damage. Default is x1.0.
# "ShieldDmgMultiplier" will multiply upon the base global multiplier for shield damage. Default is x1.0.
# "Beams" is an optional list with Phaser Bank names, wich will narrow the tractor beam projectors to a select few. Not adding the field or making it blank will mean all tractor beams are Andromedan Tractor-Repulsor beam yields... if they have the proper sound.
#
# The final list was added because of compatibilities with how FoundationTech handles phaser and tractor beam yields, by their sounds. Basically in order for a certain tractor property to have a yield on the first place, you need to make sure it has its sound (that is, the string inside the .SetFireSound("") function on that projector's hardpoint, not the actual .wav or .mp3 sound file) registered on the yields list, so basically all tractor beam projectors with that sound will have that yield (unless someone else decided to use that same sound for another type of yield). So please, whenever you have to add this yield or tractor/phaser yields, make sure the sound names on the list are distinctive and unique enough. By default, if that list is unavilable it will use the sound of the first tractor beam projector registered on the hardpoint.

# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
# Also please note the value here has meaning:
# "0" means hull immunity only
# "1" means shield immunity only
# "2" means both shield and hull immunity
# However also note that due to how Tractor Beam continuous hits do not carry certain values, it will assume by defect that the tractor is not hitting the hull for this immunity
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Andromedan Tractor Beams Weapon Immune": 1
}
"""
# Regarding subTechs
# As those with some idea of python language can see, you can stack more than 1 subtech.
# The fields shield and hull functions have are the following:
## "attackerID", the ID number of the vessel that attacked
## "pAttacker", the Ship instance (not the pInstance Foundation one) of the ship that attacked 
## "pAttackerInstance", the attacker ship's Foundation ship Instance, which often holds the special races, techs and some more, specially in KM installs.
## "pAttackerInstanceDict", __dict__ of the above, that way we can fetch it once without using the "hacky" __dict__ every single time we want the pInstance.__dict__
## "targetID", the ID number of the vessel that was attacked
## "pTarget", the Ship instance (not the pInstance Foundation one) of the ship that got hit 
## "pTargetInstance", the target ship's Foundation ship Instance
## "pTargetInstanceDict", __dict__ of the above, that way we can fetch it once without using the "hacky" __dict__ every single time we want the pInstance.__dict__
## "sScript", the Script from the Target ship (not the hardpoint)
## "sShipScript", the filename of the ship script from above
## "pEvent", the event in question when the projectile hit. Could be useful on certain situations
## "hullDamageMultiplier", multiplies the base damage of the torpedo if it hits the hull. While you could totally overwrite the value a previous function did, it is polite to not ignore all values. On the case of hulls the functions must make sure the values are multiplied between each other (so if you make it 0.8 times something, then 2.0 times, it wil be 0.8 * 2.0 = 1.6). Careful with negative values, since they may counteract each other if an even amount of functions apply them.
## "shieldDamageMultiplier", multiplies the base damage of the torpedo if it hits the shield. While you could totally overwrite the value a previous function did, it is polite to not ignore all values. On the case of shield the functions must make sure the values are multiplied between each other (so if you make it 0.8 times something, then 2.0 times, it wil be 0.8 * 2.0 = 1.6). Careful with negative values, since they may counteract each other if an even amount of functions apply them.
## "shouldPassThrough", values greater than 1 means that this script will create a torpedo replica capable of bypassing the shields (or will simulate it). Should be stacked with sums. Negative values are allowed.
## "wasChanged": if this value is lesser than 0, it will perform the default effect (torpedo where "shouldPassThrough" = 1). When some script changes things it is recommended to stack "1" to this value, unless you want a default behaviour with modified "shieldDamageMultiplier"
##
# If you want an new specific subTech that modifies part of Andromedan Tractor Beams Effect, you can do it by adding a file under the scripts\Custom\Techs\AndromedanTractorBeamWeaponScripts directory; if possible with a reasonable name related to the Technology(ies) it covers.
# For example, if the special sub-tech is called "SG Shields" you can call the file "SGShieldsConfiguration.py"; Sometimes certain sub-techs may go together on the same function of a file because being related or being sub-components.
# Below there's an example used for the aforementioned SGShieldsConfiguration, at least the 1.0 version, but modified to include more function examples, clarify and with some parts commented so as to not trigger commentary issues - those sections have replaced the triple " with ####@@@
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 6th February 2026, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the AndromedanTractorRepulsorTech Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/AndromedanTractorBeamWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by Andromedan Tractor Repulsor Beam Weapons.
# The reason we make a tech for this, is mostly because these shields are quite good at absorbing kinetic energy so this should be a different deal.
# And even between SG shields, some behave differently:

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info
xWraithHullResistMultiplier = 0.99
xAsgardShieldResistMultiplier = (1.0/3.0)
xOriShieldResistMultiplier = (1.0/3.14)

##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		shouldPassThrough = shouldPassThrough - 1
		if pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech == "Asgard": # Resistances
				global xAsgardShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldResistMultiplier
			if RaceShieldTech == "Ori": # Resistances
				global xOriShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xOriShieldResistMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"): # Own turf, SG Ion Weapons are meant to deal additional damage to weak Naquadah and some Neutronium hulls... and Replicator hulls
		RaceShieldTech = None
		if pTargetInstanceDict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceHullTech"]
		elif pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]

		if RaceShieldTech == "Wraith":
			global xWraithHullResistMultiplier
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * (xWraithHullResistMultiplier)
			if pTargetInstanceDict["SG Shields"].has_key("Wraith Dampening"):
				hullDamageMultiplier = hullDamageMultiplier * pTargetInstanceDict["SG Shields"]["Wraith Dampening"]

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged


"""

import App

from bcdebug import debug
import traceback
import nt
import string

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.1",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }
# A. GENERAL BASIC CONFIGURATION
# Some generic info that would affect mostly everyone
AndromedanTractorBeamsGenericShieldDamageMultiplier = 1.0
AndromedanTractorBeamsHullDamageMultiplier = 1.0

# At the moment I cannot really think of one ship immune to both effects in particular legacy-wise... adding this Dummy
global lImmuneAndromedanTractorBeamsWeaponShips
lImmuneAndromedanTractorBeamsWeaponShips = []

SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side

# "variableNames" is a global dictionary, filled automatically by the files in scripts/Custom/Techs/AndromedanTractorBeamsWeaponScripts 
# the purpose of this list is to append dicts f.ex. {"legacyImmunity": alist, "interactionHullBehaviour": functionObtained, "interactionShieldBehaviour": anotherfunctionObtained}
# the "legacyImmunity" field is there only to add some ships on a legacy list to be fully immune to all effects of this weapon to hull and shields.
# the "interactionHullBehaviour" will have a function that will be called to calculate the damage reduction or amplification to the hull, those functions are meant to be stacked.
# the "interactionShieldBehaviour" will try to do the same, but for shields. On this case, due to certain franchise differences, while some effects will be stacked, it is recommended to only add one of a type, or create a hybrid function if you want multiple of these to be added (f.ex one function could tell the script that they can bypass always, while another says they cannot bypass).
# Alongside these parameters, there are additional ones, but will be ignored unless they are on the "BasicAndromedanTractorBeamsWeaponConfiguration.py" subTech file:
## "AndromedanTractorBeamsHullDamageMultiplier": allows to edit the base damage multiplier to all hulls without needing to edit the main technology file. Default is 1 (1x Equal damage).
## "AndromedanTractorBeamsGenericShieldDamageMultiplier": allows to edit the base damage multiplier to all shields without needing to edit the main technology file. Default is 1 (deal damage x1)
## "SlowDownRatio": an auxiliar (unused) value that is used for considering threshold speed reduction (it's a value meant to reduce the chances of firing a too-rapid regular projectile which then might go too fast and bypass a ship instead of hitting it)

variableNames = {}

_g_dExcludeSomePlugins = {
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
}

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound

# Based on LoadExtraPlugins by Dasher42, but heavily modified so it only imports a few things
def LoadExtraLimitedPlugins(dExcludePlugins=_g_dExcludeSomePlugins):
	debug(__name__ + ", LoadExtraLimitedPlugins")

	dir="scripts\\Custom\\Techs\\AndromedanTractorBeamWeaponScripts" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	try:
		list = nt.listdir(dir)
		if not list:
			print "ERROR: Missing scripts/Custom/Techs/AndromedanTractorBeamWeaponScripts folder for AndromedanTractorBeamWeapon technology"
			return 0

	except:
		print "ERROR: Missing scripts/Custom/Techs/AndromedanTractorBeamWeaponScripts folder for AndromedanTractorBeamWeapon technology, or other error:"
		traceback.print_exc()
		return 0
	list.sort()

	dotPrefix = string.join(string.split(dir, "\\")[1:], ".") + "."

	filesChecked = {} 
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
					filesChecked[fileName] = 1
					myGoodPlugin = dotPrefix + fileName

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["legacyImmunity", "interactionShieldBehaviour", "interactionHullBehaviour"])
					except:
						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["AndromedanTractorBeamsHullDamageMultiplier", "AndromedanTractorBeamsGenericShieldDamageMultiplier", "SlowDownRatio"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals())
					
					if hasattr(banana, "legacyImmunity"): # These will not be affected at all by the hull or shield effects, period
						global lImmuneAndromedanTractorBeamsWeaponShips
						for item in banana.legacyImmunity:
							lImmuneAndromedanTractorBeamsWeaponShips.append(item)

					if hasattr(banana, "interactionShieldBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionShieldBehaviour"] = banana.interactionShieldBehaviour

					if hasattr(banana, "interactionHullBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionHullBehaviour"] = banana.interactionHullBehaviour

					if fileName == "AndromedanTractorBeamWeaponBasicConfiguration":
						if hasattr(banana, "AndromedanTractorBeamsHullDamageMultiplier"):
							global AndromedanTractorBeamsHullDamageMultiplier
							AndromedanTractorBeamsHullDamageMultiplier = banana.AndromedanTractorBeamsHullDamageMultiplier

						if hasattr(banana, "AndromedanTractorBeamsGenericShieldDamageMultiplier"):
							global AndromedanTractorBeamsGenericShieldDamageMultiplier
							AndromedanTractorBeamsGenericShieldDamageMultiplier = banana.AndromedanTractorBeamsGenericShieldDamageMultiplier

						if hasattr(banana, "SlowDownRatio"):
							global SlowDownRatio
							SlowDownRatio = banana.SlowDownRatio

					#print "AndromedanTractorBeamsWeapon reviewing of this subtech is a success"
			except:
				print "someone attempted to add more than they should to the AndromedanTractorRepulsorTech script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print AndromedanTractorBeamsHullDamageMultiplier, AndromedanTractorBeamsGenericShieldDamageMultiplier
#print variableNames

try:
	import Foundation
	import FoundationTech
	import MissionLib
	import Multiplayer.SpeciesToTorp

	torpsNetTypeThatCanPhase = Multiplayer.SpeciesToTorp.PHASEDPLASMA # For the "torpedoes-going-through" issue

	torpCountersForInstance = 32 # Auxiliar value to fake a pEvent, for new collisions

	from ftb.Tech.ATPFunctions import *
	from math import *

	# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
	def NiPoint3ToTGPoint3(p, factor = 1.0):
		debug(__name__ + ", NiPoint3ToTGPoint3")
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x * factor, p.y * factor, p.z * factor)
		return kPoint

	def TGPoint3ToNiPoint3(p, factor=1.0):
		debug(__name__ + ", TGPoint3ToNiPoint3")
		kPoint = App.NiPoint3(p.x * factor, p.y * factor, p.z * factor)
		return kPoint

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

	def CopyVector(kVect):
		debug(__name__ + ", CopyVector")
		kCopy = App.TGPoint3()
		kCopy.SetXYZ(kVect.GetX(),kVect.GetY(),kVect.GetZ())
		return kCopy

	def FireTorpFromPointWithVectorAndNetType(kPoint, kVector, pcTorpScriptName, idTarget, pShipID, fSpeed, NetType=torpsNetTypeThatCanPhase, damage=0.1, dmgRd=0.15, hidden=0, detectCollison= None, TGOffset = None):

		# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs

		debug(__name__ + ", FireTorpFromPointWithVector")
		pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
		pSet = pTarget.GetContainingSet()
		if not pSet:
			return None

		# Create the torpedo.
		pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
		pTorp.SetDamageRadiusFactor(dmgRd)
		pTorp.SetDamage(damage)
		pTorp.SetNetType(NetType)
		#pTorp.SetMass(0.00000001)
		#pTorp.SetUsePhysics(0)
		pTorp.UpdateNodeOnly()

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

		# Set up its target and target subsystem, if necessary.
		pTorp.SetTarget(idTarget)
		if not TGOffset and pShip:
			pTorp.SetTargetOffset(pShip.GetHull().GetPosition())
		else:
			pTorp.SetTargetOffset(TGOffset)
		pTorp.SetParent(pShipID)

		# Add the torpedo to the set, and place it at the specified placement.
		pSet.AddObjectToSet(pTorp, None)
		pTorp.UpdateNodeOnly()
		if hidden != 0:
			pTorp.SetHidden(1)
			pTorp.UpdateNodeOnly()

		# If there was a target, then orient the torpedo towards it.
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kTargetLocation.Subtract(kTorpLocation)
		kFwd = kTargetLocation
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)
		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

		if detectCollison != None: # We want to detect collision first
			pTorp.DetectCollision(detectCollison)
			pTorp.UpdateNodeOnly()

		# Give the torpedo an appropriate speed.
		kSpeed = CopyVector(kVector)
		kSpeed.Unitize()
		kSpeed.Scale(fSpeed)
		pTorp.SetVelocity(kSpeed)

		#print "Torpedo mass", pTorp.GetMass()

		return pTorp

	def PredictTargetLocation(pTarget, fSpeed):
		# Find how far we are to our target.
		debug(__name__ + ", PredictTargetLocation")
		
		# Get a rough estimate of how long it'll take our weapon
		# to hit the target.
		fTime = 0.5 #fDistance / fSpeed
		
		# Predict the target's position in that amount of time.
		vPredicted = pTarget.GetWorldLocation()
		pPhysicsTarget = App.PhysicsObjectClass_Cast(pTarget)
		if (pPhysicsTarget != None):
			vPredicted.Set(pPhysicsTarget.GetPredictedPosition( pTarget.GetWorldLocation(), pPhysicsTarget.GetVelocityTG(), pPhysicsTarget.GetAccelerationTG(), fTime ))
		
		return vPredicted

	# Slight modification from Borg Adaptation script, the Borg one is meant to weaken and be complemented by their base damage to destroy - here all the effort must be done on the same function
	def AdjustListedSubsystems(pShip, lAffectedSystems, lNonTargetableAffeSys, damageHealed, fAllocatedFactor, hurt = 0):
		pHull=pShip.GetHull()
		notInThere = 0
		lenaffectedSys = len(lAffectedSystems)
		systemsToDestroy = []
		for pSystem in lAffectedSystems:
			if pSystem.GetName() == pHull.GetName():
				notInThere = 1
			status = pSystem.GetConditionPercentage()
			# print "status" + str(status)
			if status > 0.0:
				fNewCondition = status + (damageHealed / pSystem.GetMaxCondition()) * fAllocatedFactor / lenaffectedSys
						
				if fNewCondition <= 0:
					fNewCondition = 0
					systemsToDestroy.append(pSystem)
				elif fNewCondition > 1:
					fNewCondition = 1
				pSystem.SetConditionPercentage(fNewCondition)

		lenaffecteduntSys = len(lNonTargetableAffeSys)
		if hurt == 0:
			for pSystem in lNonTargetableAffeSys:
				iamHull = 0
				if pSystem.GetName() == pHull.GetName():
					notInThere = 1
					iamHull = 1
				status = pSystem.GetConditionPercentage()
				# print "status" + str(status)
				if status > 0.0:
					dividerIs = lenaffecteduntSys
					if iamHull:
						dividerIs = 1 + lenaffectedSys
					fNewCondition = status + (damageHealed / pSystem.GetMaxCondition()) * fAllocatedFactor / dividerIs
							
					if fNewCondition <= 0:
						fNewCondition = 0
						systemsToDestroy.append(pSystem)
					elif fNewCondition > 1:
						fNewCondition = 1
					pSystem.SetConditionPercentage(fNewCondition)

		if notInThere == 0: # hull hit but no targetable subsystems affected? We must guess it's the hull only, then!
			if not(pHull==None):
				status = pHull.GetConditionPercentage()
				fNewCondition = status + (damageHealed / pHull.GetMaxCondition()) * fAllocatedFactor / (1 + lenaffectedSys)

				if fNewCondition <= 0:
					fNewCondition = 0
					systemsToDestroy.append(pHull)
				elif fNewCondition > 1.0:
					fNewCondition = 1.0
				pHull.SetConditionPercentage(fNewCondition)

		for system in systemsToDestroy:
			pShip.DestroySystem(system)
			
		return 0

	def FindAllAffectedSystems(pShip, kPoint, fRadius, pEvent = None):
		lSystems = []
		
		kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		while (1):
			pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
			if not pSubsystem:
				break
			lSystems.append(pSubsystem)
					
			for i in range(pSubsystem.GetNumChildSubsystems()):
				pChild = pSubsystem.GetChildSubsystem(i)
				lSystems.append(pChild)

		pShip.EndGetSubsystemMatch(kIterator)
		# get affected systems
		lAffectedSystems = []
		lNonTargetableAffeSys = []
		if kPoint == None and pEvent != None:
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
		for pSystem in lSystems:
			vDifference = NiPoint3ToTGPoint3(pSystem.GetPosition())
			vDifference.Subtract(kPoint)
			if pSystem.GetRadius() + fRadius >= vDifference.Length():
				if pSystem.IsTargetable():
					lAffectedSystems.append(pSystem)
				else:
					lNonTargetableAffeSys.append(pSystem)

		return lAffectedSystems, lNonTargetableAffeSys

	# "Fake" collision event. Same functions, quite a different inner implementation.
	import Appc
	class FakeTractorWeaponHitEvent(App.TGEvent):
		PHASER = App.WeaponHitEvent.PHASER
		TORPEDO = App.WeaponHitEvent.TORPEDO
		TRACTOR_BEAM = App.WeaponHitEvent.TRACTOR_BEAM
		# Just apply normal TGEvent stuff, then the extra values are adapted on the getters and setters, just in case

		def __init__(self, *args):

			self.this = apply(Appc.new_TGEvent,args)
			#self.thisown = 1 # Uncomment if this does not work
			self.firingObject = None
			self.targetObject = None
			self.objectHitPoint = None
			self.objectHitNormal = None
			self.worldHitPoint = None
			self.worldHitNormal =  None
			self.theCondition = 1.0 # This goes to a range
			self.theWpnInstance = 32 # This goes up each time
			self.evntDmg = 0.0
			self.evntRd = 0.0
			self.myHullWasHit = 0
			self.theFiringPlayerID = 0

		def SetFiringObject(self, pObject):
			self.firingObject = pObject
			
		def GetFiringObject(self, *args):
			val = self.firingObject
			if val: val = App.ObjectClassPtr(val) 
			return val

		def SetTargetObject(self, pObject):
			self.targetObject = pObject

		def GetTargetObject(self, *args):
			val = self.targetObject
			if val: val = App.ObjectClassPtr(val) 
			return val

		def SetObjectHitPoint(self, pNiPoint3):
			self.objectHitPoint = pNiPoint3

		def GetObjectHitPoint(self, *args):
			val = self.objectHitPoint
			if val:
				#val = App.NiPoint3Ptr(val) # We already gave a pointer, no need to give a pointer of a pointer
				val.thisown = 1
			return val

		def SetObjectHitNormal(self, pNiPoint3):
			self.objectHitNormal = pNiPoint3

		def GetObjectHitNormal(self, *args):
			val = self.objectHitNormal
			if val:
				val.thisown = 1
			return val

		def SetWorldHitPoint(self, pNiPoint3):
			self.worldHitPoint = pNiPoint3

		def GetWorldHitPoint(self, *args):
			val = self.worldHitPoint
			if val:
				val.thisown = 1
			return val

		def SetWorldHitNormal(self, pNiPoint3):
			self.worldHitNormal = pNiPoint3

		def GetWorldHitNormal(self, *args):
			val = self.worldHitNormal
			if val:
				val.thisown = 1
			return val

		def GetCondition(self, *args):
			val = self.theCondition
			return val

		def SetCondition(self, value0to1):
			if value0to1 < 0:
				value0to1 = 0.0
			elif value0to1 > 1:
				value0to1 = 1.0
			self.theCondition = value0to1

		def SetWeaponInstanceID(self, value=32):
			self.theWpnInstance = value

		def GetWeaponInstanceID(self, *args): # This grows according to projectiles that have hit, begins at 32
			val = self.theWpnInstance
			return val

		def SetRadius(self, rd):
			if rd <= 0.0:
				rd = 0.1
			self.evntRd = rd
			
		def GetRadius(self, *args):
			if self.evntRd <= 0.0:
				self.evntRd = 0.1
			return self.evntRd

		def SetDamage(self, rd):
			self.evntDmg = rd
			
		def GetDamage(self, *args):
			return self.evntDmg			

		def GetWeaponType(self, *args):
			return App.WeaponHitEvent.TORPEDO

		def IsHullHit(self, *args):
			return self.myHullWasHit

		def SetHullHit(self, rd):
			if rd < 1:
				rd = 0
			elif rd > 1:
				rd = 1
			self.myHullWasHit = rd

		def SetFiringPlayerID(self, somethingID):
			self.theFiringPlayerID = somethingID

		def GetFiringPlayerID(self, *args):
			return self.theFiringPlayerID

		def __del__(self, Appc=Appc):
			if self.thisown == 1 :
				self.firingObject = None
				self.targetObject = None
				self.objectHitPoint = None
				self.objectHitNormal = None
				self.worldHitPoint = None
				self.worldHitNormal =  None
				self.theCondition = None
				self.theWpnInstance = None
				self.evntRd = None
				self.evntDmg = None
				self.myHullWasHit = None
				self.theFiringPlayerID = None
				Appc.delete_TGEvent(self)
		def __repr__(self):
			return "<Python FakeTractorWeaponHitEvent instance at %s>" % (self.this,)

	class FakeTractorWeaponHitEventPtr(FakeTractorWeaponHitEvent):
		def __init__(self,this):
			self.this = this
			self.thisown = 0
			self.__class__ = FakeTractorWeaponHitEvent

	def TGFakeTractorWeaponHitEvent_Create(*args, **kwargs):
		val = apply(Appc.TGEvent_Create,args,kwargs)
		if val:
			val = FakeTractorWeaponHitEventPtr(val)
		return val

	class AndromedanTractorBeamsWeapon(FoundationTech.TechDef):
		#def __init__(self, name, dict = {}):
		#	debug(__name__ + ", __init__")
		#	FoundationTech.TractorTechDef.__init__(self, name)
		#	FoundationTech.TechDef.__init__(self, name)
		#	self.pEventHandler = App.TGPythonInstanceWrapper()
		#	self.pEventHandler.SetPyWrapper(self)
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, self.pEventHandler, "OneWeaponHit") 
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, self.pEventHandler, "OneWeaponHit")

		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			if pInstance != None:
				pInstance.lTechs.append(self)
				#pInstance.lTractorDefense.append(self)

				if pInstance.__dict__.has_key(self.name):
					pConfig = pInstance.__dict__[self.name][-1]
					if str(pConfig)[0] != "[":
						pShip = None
						if hasattr(pInstance, "pShipID"):
							pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)

						if pShip:
							pTractor = pShip.GetTractorBeamSystem()
							if not pTractor:
								return
							pProjector = App.TractorBeamProjector_Cast(pTractor.GetChildSubsystem(0))
							if not pProjector:
								return

							sProjector = str(pProjector)
							sFire = pProjector.GetFireSound()
							pConfig = [sProjector, sFire]
					for sound in pConfig:
						FoundationTech.dYields[sound] = self

		def Detach(self, pInstance):
			debug(__name__ + ", Detach")
			if pInstance != None and hasattr(pInstance, "lTechs"):
				pInstance.lTechs.remove(self)
				#pInstance.lTractorDefense.remove(self)

		def IsAndromedanTractorBeamsWeaponYield(self):
			debug(__name__ + ", IsAndromedanTractorBeamsWeaponYield")
			return 1

		def IsPhaseYield(self):
			debug(__name__ + ", IsPhaseYield")
			return 0

		def IsDrainYield(self):
			debug(__name__ + ", IsDrainYield")
			return 0

		def GetMySupportProjectile(self):
			return "Tactical.Projectiles.AndromedanTractorBeamDummy"

		def EventInformation(self, pEvent):
			debug(__name__ + ", EventInformation")
			fRadius = None
			fDamage = None
			kPoint = None
			kWPoint = None
			if hasattr(pEvent, "GetRadius"):
				fRadius = pEvent.GetRadius()
			if hasattr(pEvent, "GetRadius"):
				fDamage = pEvent.GetDamage()
			if hasattr(pEvent, "GetObjectHitPoint"):
				kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
			if hasattr(pEvent, "GetWorldHitPoint"):
				kWPoint = pEvent.GetWorldHitPoint()

			return fRadius, fDamage, kPoint, kWPoint

		def shieldIsLesserThan(self, pShip, kPoint, extraDamageHeal, shieldThreshold = 0.2, multifacet = 0, negateRegeneration=0):
			debug(__name__ + ", shieldIsLesserThan")
			pShields = pShip.GetShields()
			shieldHitBroken = 0
			if pShields and not (pShields.IsDisabled() or not pShields.IsOn()):
				# get the nearest reference
				pReferenciado = None
				dMasCercano = 0
				pointForward = App.TGPoint3_GetModelForward()
				pointBackward = App.TGPoint3_GetModelBackward()
				pointTop = App.TGPoint3_GetModelUp()
				pointBottom = App.TGPoint3_GetModelDown()
				pointRight = App.TGPoint3_GetModelRight()
				pointLeft = App.TGPoint3_GetModelLeft()
				lReferencias = [pointForward, pointBackward, pointTop, pointBottom, pointLeft, pointRight]

				for pPunto in lReferencias:
					pPunto.Subtract(kPoint)
					if pReferenciado == None or pPunto.Length() < dMasCercano:
						dMasCercano = pPunto.Length()
						pReferenciado = pPunto

				shieldDirNearest = None
				if pReferenciado:
					shieldDirNearest = lReferencias.index(pReferenciado)
				else:
					shieldHitBroken = 1

				pShieldsProperty = pShields.GetProperty()
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					if shieldDirNearest == shieldDir or multifacet != 0:
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						fRecharge = 0
						if pShieldsProperty and negateRegeneration != 0:
							fRecharge = -pShieldsProperty.GetShieldChargePerSecond(shieldDir)
						resultHeal = fCurr + fRecharge
						if resultHeal < 0.0:
							resultHeal = 0.0
						elif resultHeal > fMax:
							resultHeal = fMax
						pShields.SetCurShields(shieldDir, resultHeal)
						
						if (shieldDirNearest == shieldDir or multifacet == 2) and (fMax <= 0.0 or fMax <= extraDamageHeal or resultHeal <= extraDamageHeal or resultHeal < (shieldThreshold * fMax)):
							shieldHitBroken = 1
			else:
				shieldHitBroken = 1

			return shieldHitBroken

		def OnYield(self, pShip, pInstance, pEvent, pTorp = None, time = None):
			return self.OneWeaponHit(pEvent, pShip, pInstance, pTorp, time)

		def OneWeaponHit(self, pEvent, pPTarget = None, pTargetInstanceAux = None, pTorp = None, time = None):
			debug(__name__ + ", OneWeaponHit")
			try:
				#print "WEAPON HIT", pEvent, pEvent.__dict__
				evtHType = 0

				if hasattr(pEvent, "GetWeaponType") and pEvent.GetWeaponType() != pEvent.TRACTOR_BEAM:
					return 0

				# First check we have valid targets and attackers

				pWeaponFired = None
				pAttacker = None
				pTarget = None
				if hasattr(pEvent, "GetFiringObject"): # If we use App.ET_WEAPON_HIT, it is this
					pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
				elif hasattr(pEvent, "GetSource"): # OnYield-related events for tractors
					evtHType = 1
					pWeaponFired = App.TractorBeamProjector_Cast(pEvent.GetSource())
					if(pWeaponFired == None) or not hasattr(pWeaponFired, "GetParentShip"):
						return 0
					
					pAttacker = pWeaponFired.GetParentShip()

				if pPTarget == None:
					pTarget = App.ShipClass_Cast(pEvent.GetDestination())
				elif hasattr(pPTarget, "GetObjID"):
					pTarget = pPTarget

				if not pAttacker or not pTarget:
					return 0

				attackerID = pAttacker.GetObjID()
				targetID = pTarget.GetObjID()

				pAttacker = App.ShipClass_GetObjectByID(None, attackerID)
				pTarget = App.ShipClass_GetObjectByID(None, targetID)

				if not pAttacker or not pTarget:
					return 0

				pAttackerInstance = findShipInstance(pAttacker)
				pTargetInstance = findShipInstance(pTarget)
			
				if not pAttackerInstance or not pAttackerInstance.__dict__.has_key(self.name):
					return 0

				# Then check immunities before doing calculations
				sScript     = pTarget.GetScript()
				sShipScript = string.split(sScript, ".")[-1]

				global lImmuneAndromedanTractorBeamsWeaponShips # This legacy list goes first - it is to reduce unnecessary calculations
				if sShipScript in lImmuneAndromedanTractorBeamsWeaponShips:
					return 0

				pEventIsHullHit = 0
				if evtHType == 0 and hasattr(pEvent, "IsHullHit"): # We are gonna asumme at first that no, no hull has been hit - because of tractor event shenanigans, we can later on verify if that is not the case.
					pEventIsHullHit = pEvent.IsHullHit()

				immuTyp = -1 # No immunity
				pTargetInstanceDict = None
				if pTargetInstance:
					pTargetInstanceDict = pTargetInstance.__dict__
					if pTargetInstanceDict.has_key('Andromedan Tractor-Repulsor Beams Weapon Immune'):
						immuTyp = pTargetInstanceDict['Andromedan Tractor-Repulsor Beams Weapon Immune']
						if(pEventIsHullHit):
							if (immuTyp == 0 or immuTyp > 1):
								return 0
						else:
							if immuTyp > 0:
								return 0

				if evtHType == 0:
					pWeaponFired = App.Weapon_Cast(pEvent.GetSource())

				if pWeaponFired == None:
					print __name__, " no weapon stopped fired obj..."
					return 0

				pAttackerInstanceDict = pAttackerInstance.__dict__

				techIsAList = (type(pAttackerInstanceDict[self.name]) == type([]))
				tchllen = 0
				if techIsAList:
					tchllen = len(pAttackerInstanceDict[self.name])

				tchlEmpty = 1
				if tchllen > 0:
					tchlEmpty = 0

				cfg0dict = {}
				if (not tchlEmpty) and type(pAttackerInstanceDict[self.name][0]) == type({}):
					cfg0dict = pAttackerInstanceDict[self.name][0]
				#else:
				#	print "TO-DO Config is NOT a dict"					
					

				if cfg0dict.has_key("Beams") and len(cfg0dict["Beams"]) > 0:
					#print __name__, ": I have beams key, verifying the phaser bank is among them"
					lBeamNames = cfg0dict["Beams"]		

					if not pWeaponFired.GetName() in lBeamNames:
						#print "AndromedanTractorBeamWeapon: cancelling, ship has AndromedanTractorBeamWeapon equipped but not for that beam..."
						return
				#else:
				#	print __name__, ": I do not have beams key, I will assume all tractors have ", self.name, " ability"

				# Ok now the shot is almost guaranteed, proceed with calculations
				targetRadius = pTarget.GetRadius()
				fRadius, fDamage, kPoint, kWorldPoint = self.EventInformation(pEvent)
				myHull = None
				myHullPos = None
				global AndromedanTractorBeamsGenericShieldDamageMultiplier, AndromedanTractorBeamsHullDamageMultiplier

				if evtHType == 1:
					if fRadius == None:
						fRadius = targetRadius
					if fDamage == None:
						fDamage = AndromedanTractorBeamsHullDamageMultiplier
					if kPoint == None or kWorldPoint == None:
						myHull = pTarget.GetHull()
						if myHull:
							if kPoint == None:
								myHullPos = NiPoint3ToTGPoint3(myHull.GetPosition())	
								kPoint = myHullPos
							if kWorldPoint == None:
								kWorldPoint = myHull.GetWorldLocation()
						else:
							if kPoint == None:
								myHullPos =  App.TGPoint3()
								myHullPos.SetXYZ(0, 0, 0)
								kPoint = myHullPos
							if kWorldPoint == None:
								kWorldPoint = pTarget.GetWorldLocation()

				baseHullMultiplier = 1.0 * AndromedanTractorBeamsHullDamageMultiplier
				baseShieldMultiplier = 1.0 * AndromedanTractorBeamsGenericShieldDamageMultiplier

				if cfg0dict.has_key("HullDmgMultiplier") and cfg0dict["HullDmgMultiplier"] > 0.0:
					baseHullMultiplier = baseHullMultiplier * cfg0dict["HullDmgMultiplier"]

				if cfg0dict.has_key("ShieldDmgMultiplier") and cfg0dict["ShieldDmgMultiplier"] > 0.0:
					baseShieldMultiplier = baseShieldMultiplier * cfg0dict["ShieldDmgMultiplier"]

				hullDamageMultiplier = baseHullMultiplier
				shieldDamageMultiplier = baseShieldMultiplier
				shouldPassThrough = 0

				wasHullChanged = 0

				for item in variableNames.keys():
					if variableNames[item].has_key("interactionHullBehaviour"): # These are reserved for when the hull has been hit! These are meant to be accumulative, for defenses.
						hullDamageMultiplier3 = 0
						shieldDamageMultiplier3 = 0
						shouldPassThrough3 = 0
						wasHullChanged3 = 0
						try:
							hullDamageMultiplier3, shieldDamageMultiplier3, shouldPassThrough3, wasHullChanged3 = variableNames[item]["interactionHullBehaviour"](attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasHullChanged)
						except:
							hullDamageMultiplier3 = hullDamageMultiplier
							shieldDamageMultiplier3 = shieldDamageMultiplier
							shouldPassThrough3 = shouldPassThrough
							wasHullChanged3 = wasHullChanged
							print "Some ", __name__, " hull subtech suffered an error"
							traceback.print_exc()

						hullDamageMultiplier = hullDamageMultiplier3
						shieldDamageMultiplier = shieldDamageMultiplier3
						shouldPassThrough = shouldPassThrough3
						wasHullChanged = wasHullChanged3

				if wasHullChanged > 0:
					baseHullMultiplier = hullDamageMultiplier

				wasShieldChanged = 0
				for item in variableNames.keys():
					if variableNames[item].has_key("interactionShieldBehaviour"): # These are reserved for when the shield has been hit! Also be careful, since these are more likely to stack weaknesses! Preferable to only have one of this type per ship
						try:
							hullDamageMultiplier2 = 0
							shieldDamageMultiplier2 = 0
							shouldPassThrough2 = 0
							wasShieldChanged2 = 0			
							hullDamageMultiplier2, shieldDamageMultiplier2, shouldPassThrough2, wasShieldChanged2 = variableNames[item]["interactionShieldBehaviour"](attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasShieldChanged)

						except:
							hullDamageMultiplier2 = hullDamageMultiplier
							shieldDamageMultiplier2 = shieldDamageMultiplier
							shouldPassThrough2 = shouldPassThrough
							wasShieldChanged2 = wasShieldChanged
							print "Some ", __name__, " shield subtech suffered an error"
							traceback.print_exc()

						hullDamageMultiplier = hullDamageMultiplier2
						shieldDamageMultiplier = shieldDamageMultiplier2
						shouldPassThrough = shouldPassThrough2
						wasShieldChanged = wasShieldChanged2

				if wasShieldChanged <= 0:
					# normal shields
					shouldPassThrough = 1
					#baseShieldMultiplier = baseShieldMultiplier
				else:
					baseShieldMultiplier = shieldDamageMultiplier

				mod = self.GetMySupportProjectile() # This torpedo was made so Automated Point Defence scripts stop harrasing us and so DS9FX can ignore a damage bypass if necessary
				torpImportedInfo = None
				torpImportedSpeed = 300.0
				torp404Fallback = 0
				try:
					torpImportedInfo = __import__(mod)
					if hasattr(torpImportedInfo, "GetLaunchSpeed"):
						torpImportedSpeed = torpImportedInfo.GetLaunchSpeed()	
				except:
					print __name__, "WARNING: ", mod, " is missing from the install, or another issue:"
					traceback.print_exc()
					torpImportedSpeed = 300.0 # we will have a fallback to a special thing
					torp404Fallback = 1

				theOffset =  pAttacker.GetTargetOffsetTG() # This is given on the target's coordinates
				theOffsetNi = TGPoint3ToNiPoint3(theOffset)
				pTargetShipNode = pTarget.GetNiObject()

				pHitPointE = NiPoint3ToTGPoint3(kWorldPoint)

				pHitPointONi = App.TGModelUtils_LocalToWorldVector(pTargetShipNode, theOffsetNi)
				pHitPointO = NiPoint3ToTGPoint3(pHitPointONi, 100.0)

				pHitPointObj = PredictTargetLocation(pTarget, torpImportedSpeed)
				pHitPointObj.Add(pHitPointO)

				pVec = CopyVector(pHitPointObj)
				pWpnPos = NiPoint3ToTGPoint3(pWeaponFired.GetWorldLocation())
				pVec.Subtract(pWpnPos)

				distTargetSubToMe = pVec.Length()

				planeD = -((pVec.x) * (pHitPointE.x) + (pVec.y) * (pHitPointE.y) + (pVec.z) * (pHitPointE.z))
				lambdai = -((pVec.x) * (pWpnPos.x) + (pVec.y) * (pWpnPos.y) + (pVec.z) * (pWpnPos.z) + planeD)/( (pVec.x) * (pVec.x) + (pVec.y) * (pVec.y) + (pVec.z) * (pVec.z) )
				proyEx = pWpnPos.x + pVec.x * lambdai
				proyEy = pWpnPos.y + pVec.y * lambdai
				proyEz = pWpnPos.z + pVec.z * lambdai

				pHitPoint = App.TGPoint3()
				pHitPoint.SetXYZ(proyEx, proyEy, proyEz)

				pVec.Unitize()

				thePowerPercentageWanted = 1.0
				pParentFired = pAttacker.GetPhaserSystem()
				if pParentFired:
					thePowerPercentageWanted = (pParentFired.GetPowerLevel()/2.0) # The 2.0 is because the phasers work that way, 100% is 2, 50% is 1, 0% is 0
				else:
					pParentFired = pWeaponFired.GetParentSubsystem()
					if pParentFired:
						thePowerPercentageWanted = (App.PoweredSubsystem_Cast(pParentFired).GetPowerLevel()/2.0)
				if thePowerPercentageWanted <= 0.0: # Interesting measure - if phasers intensity is set to minimum then these vessels will be able to tow others without causing damage
					thePowerPercentageWanted = 0.0
					return 0

				pTargetBID = pWeaponFired.GetTargetID()
				pTargetB = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTargetBID))
				if pTargetB:
					targetID = pTargetB.GetObjID()			

				global SlowDownRatio

				try:
					baseTorpDamage = 1
					finalTorpDamage = 0
					if not torp404Fallback:
						baseTorpDamage = torpImportedInfo.GetDamage()

					leNetType = Multiplayer.SpeciesToTorp.DISRUPTOR

					torpVSHullDamage = thePowerPercentageWanted * baseTorpDamage * baseHullMultiplier
					torpVSShieldDamage = thePowerPercentageWanted * baseTorpDamage * baseShieldMultiplier
					shouldDoHull = self.shieldIsLesserThan(pTarget, kPoint, torpVSShieldDamage, 0.2, 0, 0)

					if shouldPassThrough > 0:
						pVec.Scale(0.001)
						leNetType = torpsNetTypeThatCanPhase
						pHitPoint.Add(pVec) # add because we want to guarantee they bypass the shields
					else:

						pDistanceShieldToSubsys = CopyVector(pHitPointObj)
						pDistanceShieldToSubsys.Subtract(pHitPoint)
						lengthShieldToSubSys = pDistanceShieldToSubsys.Length()
						lengthMeToShields = distTargetSubToMe - lengthShieldToSubSys
						if (lengthShieldToSubSys + 2.5) * 2 < distTargetSubToMe: # One thing is sure, we are closer to the shield than to the subsystem
							if (lengthShieldToSubSys + 3) > distTargetSubToMe: # One thing is sure, we are inside the shields or so close we cannot do much else
								pVec.Scale(distTargetSubToMe + 0.5)
							else:
								pVec.Scale((lengthShieldToSubSys + 2))
						else:
							pVec.Scale(lengthShieldToSubSys + 2.5)

						pHitPoint = pHitPointObj
						pHitPoint.Subtract(pVec) # subtract because we want to guarantee they always hit the shields

					if pEventIsHullHit or ((shouldPassThrough > 0 or shouldDoHull > 0) and (immuTyp == 0 or immuTyp > 1)):
						finalTorpDamage = torpVSHullDamage
						leNetType = torpsNetTypeThatCanPhase
					else:
						finalTorpDamage = torpVSShieldDamage

					if fRadius <= 0.0:
						fRadius = 0.00125
					elif evtHType == 0:
						fRadius = fRadius * 0.0004

					pTempTorp = None

					if not torp404Fallback:
						pTempTorp = FireTorpFromPointWithVectorAndNetType(pHitPoint, pVec, mod, targetID, attackerID, torpImportedSpeed, leNetType, finalTorpDamage, fRadius, 1, pTarget, theOffset)
					if pTempTorp:
						pTempTorp.SetLifetime(1.0)

					if targetRadius < 0.15 or evtHType == 1:
						# Perform damage manually as well
						if myHull == None:
							myHull = pTarget.GetHull()
						if myHull:
							global torpCountersForInstance

							pEvent1 = TGFakeTractorWeaponHitEvent_Create() # This gives us a pointer, it has no arguments, but it is our "fake" event
							pEventSource = pTempTorp
							pEventDestination = pTarget

							pEvent1.SetSource(pEventSource)
							pEvent1.SetDestination(pEventDestination)
							pEvent1.SetEventType(App.ET_WEAPON_HIT)

							pEvent1.SetFiringObject(pAttacker)
							pEvent1.SetTargetObject(pTarget)

							if myHullPos == None:
								myHullPos = NiPoint3ToTGPoint3(myHull.GetPosition())

							pEvent1.SetObjectHitPoint(myHullPos)

							pTargetPositionV = pTarget.GetWorldLocation()
							pTargetPositionVI = TGPoint3ToNiPoint3(pTargetPositionV, -1.0)
							pTargetNode = pTarget.GetNiObject()

							pEvent1.SetObjectHitNormal(pTargetPositionVI) 
							pEvent1.SetWorldHitPoint(myHullPos)
							pTargetPositionVW = TGPoint3ToNiPoint3(App.TGModelUtils_LocalToWorldUnitVector(pTargetNode, pTargetPositionVI), 1.0)
							pEvent1.SetWorldHitNormal(pTargetPositionVW)

							eCondition = 1.0
							if myHull:
								eCondition = myHull.GetConditionPercentage()
							pEvent1.SetCondition(eCondition)

							valPlus = torpCountersForInstance + 1
							pEvent1.SetWeaponInstanceID(valPlus) # Not needed... at least, I am not aware of any scripts handling it for torpedo defense

							pEvent1.SetRadius(fRadius)
							pEvent1.SetDamage(finalTorpDamage)
							pEvent1.SetHullHit(1)
							pEvent1.SetFiringPlayerID(0)

							affectedSys, nonTargetSys = FindAllAffectedSystems(pTarget, myHullPos, fRadius)
							AdjustListedSubsystems(pTarget, affectedSys, nonTargetSys, -finalTorpDamage, len(affectedSys) + 1, 1)

							# Fourth part, finally using the pEvent for something! This is also so more armours can work with these collisions, and not only one or two.
							if pTempTorp:
								pTargetInstance.DefendVSTorp(pTarget, pEvent1, pTempTorp)

				except:
					print "You are missing '", self.GetMySupportProjectile() ,"' torpedo on your install, or another error happened"
					traceback.print_exc()		
			
			except:
				print "	Error when handling ", __name__, " Weapon Hit"
				traceback.print_exc()
			return 0

	oAndromedanTractorBeamsWeapon = AndromedanTractorBeamsWeapon("Andromedan Tractor-Repulsor Beams Weapon")

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \n", __name__," are there but NOT enabled or present in your current BC installation"
	traceback.print_exc()

class AndromedanTractorBeamsWeaponDef(FoundationTech.TechDef):
	def OnTractorDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnProjectileDefense")
		if oYield and hasattr(oYield, "IsAndromedanTractorBeamsWeaponYield") and oYield.IsAndromedanTractorBeamsWeaponYield() != 0 and pInstance and pInstance.__dict__.has_key(self.name) and pInstance.__dict__[self.name] >= 2:
			return 1

	def Attach(self, pInstance):
		pInstance.lTractorDefense.append(self)


oAndromedanTractorBeamsWeaponImmunity = AndromedanTractorBeamsWeaponDef('Andromedan Tractor-Repulsor Beams Weapon Immune')