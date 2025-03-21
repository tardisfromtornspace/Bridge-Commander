# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 4th September 2024, by Alex SL Gato (CharaToLoki)
#         Based on SGOriBeamWeapon and BorgAdaptation.py by Alex SL Gato, which were based on the Foundation import function by Dasher; the Shield.py scripts and KM Armour scripts and FoundationTechnologies team's PhasedTorp.py
#         Also based on ATPFunctions by Apollo.
#################################################################################################################
# A modification of a modification, last modification by Alex SL Gato (CharaToLoki)
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech makes ships gain Ori Beam tech, which will make the same damage from "phasers" regardless of distance, by creating a torp with a trail. It still makes beam yields variable to 3 damage-dealing status with the phaser level slider or button: full-power (100%), half-power (>= 50%) and fraction power (<50%). This technology came to mind to properly fix that issue that made the battles on STBC with the Ori beams either too overpowered when at very close range, or extremely underpowered everywhere else.
# No add it, just add to your Custom/Ships/shipFileName.py this:
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"SG Ori Beams Weapon": {"HullDmgMultiplier": 1.0, "ShieldDmgMultiplier": 1.0, "Beams": ["Beam name 1", "Beam name 2"]},
}
"""
# "HullDmgMultiplier" will multiply upon the base global multiplier for hull damage. Default is x1.0.
# "ShieldDmgMultiplier" will multiply upon the base global multiplier for shield damage. Default is x1.0.
# "Beams" is an optional list with Phaser Bank names, wich will narrow the Ori beams to a select few. Not adding the field or making it blank will mean all beams are Ori beams.

# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
# Also please note the value here has meaning:
# "0" means hull immunity only
# "1" means shield immunity only
# "2" means both shield and hull immunity
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"SG Ori Beams Weapon Immune": 1
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
## "shouldPassThrough", values greater than 1 means that this script will create a torpedo replica capable of bypassing the shields. Should be stacked with sums. Negative values are allowed.
## "wasChanged": if this value is lesser than 0, it will perform the default effect (torpedo where "shouldPassThrough" = 0 and shield damage is reduced to a third from the generic in some regards). When some script changes things it is recommended to stack "1" to this value, unless you want a default behaviour with modified "shieldDamageMultiplier"
##
# If you want an new specific subTech that modifies part of the SG OriBeams Effect, you can do it by adding a file under the scripts\Custom\Techs\SGOriBeamWeaponScripts directory; if possible with a reasonable name related to the Technology(ies) it covers. 
# For example, if the special sub-tech is called "SG Shields" you can call the file "SGShieldsConfiguration.py"; Sometimes certain sub-techs may go together on the same function of a file because being related or being sub-components.
# Below there's an example used for the aforementioned SGShieldsConfiguration, at least the 1.0 version, but modified to include more function examples, clarify and with some parts commented so as to not trigger commentary issues - those sections have replaced the triple " with ####@@@
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 27th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.1
# Meant to be used alongside the SGOriBeamWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGOriBeamWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by SG OriBeam Weapons.
# The reason we make a tech for this, is mostly as a way to allow a non-ZPM BC-304 to resist two Ori Beams, while not being so powerful it could shrug the most powerful SG weapons as if it were the ZPM-powered one.
# And even between SG shields, some behave differently:

# On this case, more info about SG shields will be reviewed on their main SG Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info
xWraithHullResistMultiplier = 0.5
xAsgardShieldResistMultiplier = (1.0/3.0)

##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"):
		if pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech != "Wraith": # Resistances
				wasChanged = wasChanged + 1
			if RaceShieldTech == "Asgard": # Resistances
				global xAsgardShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldResistMultiplier
		else:
			wasChanged = wasChanged + 1

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

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged

"""

import App

from bcdebug import debug
import traceback
import nt
import string

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.16",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }
# A. GENERAL BASIC CONFIGURATION
# Some generic info that would affect mostly everyone
OriBeamsGenericShieldDamageMultiplier = 300.0 # Required low damage with high multiplier to prevent possible bleedthrough issues.

OriBeamsHullDamageMultiplier = 300.0 # Because we may want the beam to take down an unupgraded BC-304 shields in 2-3 shots, but then instantly kill that vessel if the hull is hit, we need two separate multipliers.

# At the moment I cannot really think of one ship immune to both effects in particular legacy-wise... adding this Dummy
global lImmuneSGOriBeamsWeaponShips
lImmuneSGOriBeamsWeaponShips = []

SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side

# "variableNames" is a global dictionary, filled automatically by the files in scripts/Custom/Techs/SGOriBeamsWeaponScripts 
# the purpose of this list is to append dicts f.ex. {"legacyImmunity": alist, "interactionHullBehaviour": functionObtained, "interactionShieldBehaviour": anotherfunctionObtained}
# the "legacyImmunity" field is there only to add some ships on a legacy list to be fully immune to all effects of this weapon to hull and shields.
# the "interactionHullBehaviour" will have a function that will be called to calculate the damage reduction or amplification to the hull, those functions are meant to be stacked.
# the "interactionShieldBehaviour" will try to do the same, but for shields. On this case, due to certain franchise differences, while some effects will be stacked, it is recommended to only add one of a type, or create a hybrid function if you want multiple of these to be added (f.ex one function could tell the script that they can bypass always, while another says they cannot bypass).
# Alongside these parameters, there are additional ones, but will be ignored unless they are on the "BasicSGOriBeamsWeaponConfiguration.py" subTech file:
## "OriBeamsHullDamageMultiplier": allows to edit the base damage multiplier to all hulls without needing to edit the main technology file. Default is 10 (10 -1, to deal 10 times the original damage, this script deals those 9 extra).
## "OriBeamsGenericShieldDamageMultiplier": allows to edit the base damage multiplier to all shields without needing to edit the main technology file. Default is 2 (2 -1, means deal damage once more)
## "SlowDownRatio": an auxiliar value that is used for considering threshold speed reduction (it's a value meant to reduce the chances of firing a too-rapid regular projectile which then might go too fast and bypass a ship instead of hitting it)

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

	dir="scripts\\Custom\\Techs\\SGOriBeamWeaponScripts" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	try:
		list = nt.listdir(dir)
		if not list:
			print "ERROR: Missing scripts/Custom/Techs/SGOriBeamWeaponScripts folder for SGOriBeamWeapon technology"
			return 0

	except:
		print "ERROR: Missing scripts/Custom/Techs/SGOriBeamWeaponScripts folder for SGOriBeamWeapon technology, or other error:"
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
							banana = __import__(myGoodPlugin, globals(), locals(), ["OriBeamsHullDamageMultiplier", "OriBeamsGenericShieldDamageMultiplier", "SlowDownRatio"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals())
					
					if hasattr(banana, "legacyImmunity"): # These will not be affected at all by the hull or shield effects, period
						global lImmuneSGOriBeamsWeaponShips
						for item in banana.legacyImmunity:
							lImmuneSGOriBeamsWeaponShips.append(item)

					if hasattr(banana, "interactionShieldBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionShieldBehaviour"] = banana.interactionShieldBehaviour

					if hasattr(banana, "interactionHullBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionHullBehaviour"] = banana.interactionHullBehaviour

					if fileName == "SGOriBeamWeaponBasicConfiguration":
						if hasattr(banana, "OriBeamsHullDamageMultiplier"):
							global OriBeamsHullDamageMultiplier
							OriBeamsHullDamageMultiplier = banana.OriBeamsHullDamageMultiplier

						if hasattr(banana, "OriBeamsGenericShieldDamageMultiplier"):
							global OriBeamsGenericShieldDamageMultiplier
							OriBeamsGenericShieldDamageMultiplier = banana.OriBeamsGenericShieldDamageMultiplier

						if hasattr(banana, "SlowDownRatio"):
							global SlowDownRatio
							SlowDownRatio = banana.SlowDownRatio

					#print "SGOriBeamsWeapon reviewing of this subtech is a success"
			except:
				print "someone attempted to add more than they should to the SGOriBeamsWeapon script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print OriBeamsHullDamageMultiplier, OriBeamsGenericShieldDamageMultiplier
#print variableNames

try:
	import Foundation
	import FoundationTech
	import MissionLib
	import Multiplayer.SpeciesToTorp

	torpsNetTypeThatCanPhase = Multiplayer.SpeciesToTorp.PHASEDPLASMA # For the "torpedoes-going-through" issue

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

	#NetType=Multiplayer.SpeciesToTorp.PHASEDPLASMA
	def FireTorpFromPointWithVectorAndNetType(kPoint, kVector, pcTorpScriptName, idTarget, pShipID, fSpeed, NetType=torpsNetTypeThatCanPhase, damage=0.1, dmgRd=None, hidden=0, detectCollison= None, TGOffset = None):

		# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs

		debug(__name__ + ", FireTorpFromPointWithVector")
		pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
		pSet = pTarget.GetContainingSet()
		if not pSet:
			return None

		# Create the torpedo.
		pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
		if dmgRd:
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

	def PredictTargetLocation(pTarget, pSubsystem, targetplacement, fSpeed, targetDisplacement=None):
		# Find how far we are to our target.
		debug(__name__ + ", PredictTargetLocation")
		vDiff = pTarget.GetWorldLocation()
		if (pSubsystem == None):
			return vDiff

		vDiff.Subtract( pSubsystem.GetWorldLocation() )
		fDistance = vDiff.Length() # vDiff.Unitize()

		# Get a rough estimate of how long it'll take our weapon
		# to hit the target.
		fTime = fDistance / fSpeed
		
		# Predict the target's position in that amount of time.
		vPredicted = pTarget.GetWorldLocation()
		pPhysicsTarget = App.PhysicsObjectClass_Cast(pTarget)
		if (pPhysicsTarget != None):
			vPredicted.Set(pPhysicsTarget.GetPredictedPosition(pTarget.GetWorldLocation(), pPhysicsTarget.GetVelocityTG(), pPhysicsTarget.GetAccelerationTG(), fTime ))

		if targetDisplacement:
			vSubsystemPos = targetDisplacement
			vSubsystemPos.MultMatrixLeft( pTarget.GetWorldRotation() )
			vPredicted.Add(vSubsystemPos)
		
		return vPredicted

	def getChargeTo0(pSubsystem):
		#if hasattr(pSubsystem, "SetChargeLevel"):
		try:
			pWeapon = App.PhaserBank_Cast(pSubsystem)
			#pthisPhaser = App.PhaserProperty_Cast(pWeapon.GetProperty())
			return pWeapon.GetChargeLevel()
		except:
			print "error with slow start"
			traceback.print_exc()
			return 0.0

	def setChargeTo0(pSubsystem):
		#if hasattr(pSubsystem, "SetChargeLevel"):
		try:
			pWeapon = App.PhaserBank_Cast(pSubsystem)
			#pthisPhaser = App.PhaserProperty_Cast(pWeapon.GetProperty())
			pWeapon.SetChargeLevel(0.0)
		except:
			print "error with setting charge to 0"
			traceback.print_exc()

	class SGOriBeamsWeapon(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			debug(__name__ + ", __init__")
			FoundationTech.TechDef.__init__(self, name)
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit") 
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")

		def IsSGOriBeamsWeaponYield(self):
			debug(__name__ + ", IsSGOriBeamsWeaponYield")
			return 1

		def IsPhaseYield(self):
			debug(__name__ + ", IsPhaseYield")
			return 0

		def IsDrainYield(self):
			debug(__name__ + ", IsDrainYield")
			return 0

		def EventInformation(self, pEvent):
			debug(__name__ + ", EventInformation")
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

			return fRadius, fDamage, kPoint

		def shieldIsLesserThan(self, pShip, kPoint, extraDamageHeal, shieldThreshold = 0.2, multifacet = 0, negateRegeneration=0):
			debug(__name__ + ", shieldIsLesserThan")
			pShields = pShip.GetShields()
			shieldHitBroken = 0
			remainingShield = 0.0
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
						
						if (shieldDirNearest == shieldDir):
							remainingShield = resultHeal
						if (shieldDirNearest == shieldDir or multifacet == 2) and (fMax <= 0.0 or fMax <= extraDamageHeal or resultHeal <= (extraDamageHeal + shieldThreshold * fMax) or resultHeal < (shieldThreshold * fMax)):
							shieldHitBroken = 1

			else:
				shieldHitBroken = 1

			return shieldHitBroken, remainingShield

		def OneWeaponHit(self, pEvent):
			debug(__name__ + ", OneWeaponHit")
			try:
				if pEvent.GetWeaponType() != pEvent.PHASER:
					# Future TO-DO it would be nice to just create a torp whose damage is only the powerPercentageWanted and then to that you multiply the base damage or something, to prevent extra damage (or less)
					#if not pEvent.GetWeaponType() == pEvent.TRACTOR_BEAM:
					#	pTorp = App.Torpedo_Cast(pEvent.GetSource())
					#	if pTorp:
					#		mod = pTorp.GetModuleName() 
					#		if mod == "Tactical.Projectiles.SGOriBeamDummy":
					#			# This is a stub, from here we would then calculate damage according to impact and then generate a new torp with proper damage
					# 
					return 0

				# First check we have valid targets and attackers
				pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject()) # If we use App.ET_WEAPON_HIT, it is this
				pTarget = App.ShipClass_Cast(pEvent.GetDestination())

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
			
				if not pAttackerInstance or not pAttackerInstance.__dict__.has_key("SG Ori Beams Weapon"):
					return 0

				# Then check immunities before doing calculations
				sScript     = pTarget.GetScript()
				sShipScript = string.split(sScript, ".")[-1]

				global lImmuneSGOriBeamsWeaponShips # This legacy list goes first - it is to reduce unnecessary calculations
				if sShipScript in lImmuneSGOriBeamsWeaponShips:
					return 0

				pTargetInstanceDict = None
				if pTargetInstance:
					pTargetInstanceDict = pTargetInstance.__dict__
					if(pEvent.IsHullHit()):
						 if pTargetInstanceDict.has_key('SG Ori Beams Weapon Immune') and (pTargetInstanceDict['SG Ori Beams Weapon Immune'] == 0 or pTargetInstanceDict['SG Ori Beams Weapon Immune'] > 1):
							return 0
					else:
						if pTargetInstanceDict.has_key('SG Ori Beams Weapon Immune') and pTargetInstanceDict['SG Ori Beams Weapon Immune'] > 0:
							return 0

				pWeaponFired = App.Weapon_Cast(pEvent.GetSource())

				if pWeaponFired == None:
					print "no weapon stopped fired obj..."
					return 0

				pAttackerInstanceDict = pAttackerInstance.__dict__

				if pAttackerInstanceDict["SG Ori Beams Weapon"].has_key("Beams") and len(pAttackerInstanceDict["SG Ori Beams Weapon"]["Beams"]) > 0:
					#print "SGOriBeamWeapon: I have beams key, verifying the phaser bank is among them"
					lBeamNames = pAttackerInstanceDict["SG Ori Beams Weapon"]["Beams"]		

					if not pWeaponFired.GetName() in lBeamNames:
						#print "SGOriBeamWeapon: cancelling, ship has SGOriBeamWeapon equipped but not for that beam..."
						return
				#else:
				#	print "SGOriBeamWeapon: I do not have beams key, I will assume all phasers have SG Ori Beam weapons ability"

				# Ok now the shot is almost guaranteed, proceed with calculations

				fRadius, fDamage, kPoint = self.EventInformation(pEvent)
				#if fDamage <= 0.0:
				#	return

				if getChargeTo0(pWeaponFired) < 0.5:
					setChargeTo0(pWeaponFired)
					return 0

				setChargeTo0(pWeaponFired)

				global OriBeamsGenericShieldDamageMultiplier, OriBeamsHullDamageMultiplier

				baseHullMultiplier = 1.0 * OriBeamsHullDamageMultiplier
				baseShieldMultiplier = 1.0 * OriBeamsGenericShieldDamageMultiplier

				if pAttackerInstanceDict["SG Ori Beams Weapon"].has_key("HullDmgMultiplier") and pAttackerInstanceDict["SG Ori Beams Weapon"]["HullDmgMultiplier"] > 0.0:
					baseHullMultiplier = baseHullMultiplier * pAttackerInstanceDict["SG Ori Beams Weapon"]["HullDmgMultiplier"]

				if pAttackerInstanceDict["SG Ori Beams Weapon"].has_key("ShieldDmgMultiplier") and pAttackerInstanceDict["SG Ori Beams Weapon"]["ShieldDmgMultiplier"] > 0.0:
					baseShieldMultiplier = baseShieldMultiplier * pAttackerInstanceDict["SG Ori Beams Weapon"]["ShieldDmgMultiplier"]

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
							print "Some SGOriBeamsWeapon hull subtech suffered an error"
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
							print "Some SGOriBeamWeapon shield subtech suffered an error"
							traceback.print_exc()

						hullDamageMultiplier = hullDamageMultiplier2
						shieldDamageMultiplier = shieldDamageMultiplier2
						shouldPassThrough = shouldPassThrough2
						wasShieldChanged = wasShieldChanged2

				if wasShieldChanged <= 0:
					# normal shields
					shouldPassThrough = 0
					baseShieldMultiplier = baseShieldMultiplier * 0.34 # Reduced damage to STBC shields because of Plasma and shield shenanigans - don't worry it's still enough to break most ships in one or two shots, and a hull hit is still pretty much insta-death.
				else:
					baseShieldMultiplier = shieldDamageMultiplier

				# Since pHitPointE = NiPoint3ToTGPoint3(pEvent.GetWorldHitPoint()) works fine for shields, but is wonky for targeting subsystems in general, we need to do some kind of approximation where we later add a projection of it
				theOffset =  pAttacker.GetTargetOffsetTG() # This is given on the target's coordinates
				theOffsetNi = TGPoint3ToNiPoint3(theOffset)

				pTargetShipNode = pTarget.GetNiObject()

				pHitPointONi = App.TGModelUtils_LocalToWorldVector(pTargetShipNode, theOffsetNi)
				pHitPointO = NiPoint3ToTGPoint3(pHitPointONi, 100.0)

				pWpnPosNi = pWeaponFired.GetWorldLocation()
				pWpnPos = NiPoint3ToTGPoint3(pWpnPosNi) # We fire from here
				targetplacement = pTarget.GetWorldLocation() # Target placement
				#targetplacement.Add(pHitPointO)

				mod = "Tactical.Projectiles.SGOriBeamDummy" # This torpedo was made so Automated Point Defence scripts stop harrasing us
				torpImportedInfo = None
				torpImportedSpeed = 60.0
				try:
					torpImportedInfo = __import__(mod)
					if hasattr(torpImportedInfo, "GetLaunchSpeed"):
						torpImportedSpeed = torpImportedInfo.GetLaunchSpeed()	
				except:
					print "Tactical.Projectiles.SGOriBeamDummy is missing from the install, or similar, we need that to deal damage!"
					traceback.print_exc()
					return 0


				targetplacement = PredictTargetLocation(pTarget, pWeaponFired, targetplacement, torpImportedSpeed, theOffset) # We predict where to fire

				pVec = CopyVector(targetplacement)
				pVec.Subtract(pWpnPos)

				distTargetSubToMe = pVec.Length()

				pVec.Unitize()
				pVec.Scale(0.001)

				thePowerPercentageWanted = 1.0
				pParentFired = pAttacker.GetPhaserSystem()
				if pParentFired:
					thePowerPercentageWanted = (pParentFired.GetPowerLevel()/2.0) # The 2.0 is ebcause the phasers work that way, 100% is 2, 50% is 1, 0% is 0
				else:
					pParentFired = pWeaponFired.GetParentSubsystem()
					if pParentFired:
						thePowerPercentageWanted = (App.PoweredSubsystem_Cast(pParentFired).GetPowerLevel()/2.0)
				if thePowerPercentageWanted <= 0.0:
					thePowerPercentageWanted = 0.02

				pTargetBID = pWeaponFired.GetTargetID()
				pTargetB = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTargetBID))
				if pTargetB:
					targetID = pTargetB.GetObjID()			

				global SlowDownRatio

				try:
					baseTorpDamage = torpImportedInfo.GetDamage()
					leNetType = Multiplayer.SpeciesToTorp.DISRUPTOR

					torpVSHullDamage = thePowerPercentageWanted * baseTorpDamage * baseHullMultiplier
					torpVSShieldDamage = thePowerPercentageWanted * baseTorpDamage * baseShieldMultiplier
					shouldDoHull, remainingShield = self.shieldIsLesserThan(pTarget, kPoint, torpVSShieldDamage, 0.2, 0, 0)
					if pEvent.IsHullHit() or shouldPassThrough > 0 or shouldDoHull > 0:
						finalTorpDamage = torpVSHullDamage
						if shouldDoHull > 0:
							finalTorpDamage = finalTorpDamage + remainingShield
						leNetType = Multiplayer.SpeciesToTorp.PHASEDPLASMA
					else:
						finalTorpDamage = torpVSShieldDamage

					#if fRadius <= 0.0:
					#	fRadius = 0.13
					#else:
					#	fRadius = 0.13

					pTempTorp = FireTorpFromPointWithVectorAndNetType(pWpnPos, pVec, mod, targetID, attackerID, torpImportedSpeed, leNetType, finalTorpDamage, None, 0, pTarget, theOffset)
					if pTempTorp:
						pTempTorp.SetLifetime(12.0)
						pSet = pTarget.GetContainingSet()
						if pSet:
							pSound = App.TGSoundAction_Create("OriBeam Loop", 0, pSet.GetName())
							pSound.SetNode(pTempTorp.GetNode())
							pSound.Play()	
				except:
					print "You are missing 'Tactical.Projectiles.SGOriBeamDummy' torpedo on your install, without that the SG Ori Beam Weapons here cannot deal extra hull damage... or another error happened"
					traceback.print_exc()		
			
			except:
				print "	Error when handling SG Ori Beams Weapon Hit"
				traceback.print_exc()
			return 0

	oSGOriBeamsWeapon = SGOriBeamsWeapon("SG Ori Beams Weapon")

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"
	traceback.print_exc()

class SGOriBeamsWeaponDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnProjectileDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnProjectileDefense")
		if oYield and hasattr(oYield, "IsSGOriBeamsWeaponYield") and oYield.IsSGOriBeamsWeaponYield() != 0 and pInstance and pInstance.__dict__.has_key('SG OriBeams Weapon Immune') and pInstance.__dict__['SG OriBeams Weapon Immune'] >= 2:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)
		pInstance.lPulseDefense.append(self)


oSGOriBeamsWeaponImmunity = SGOriBeamsWeaponDef('SG Ori Beams Weapon Immune')