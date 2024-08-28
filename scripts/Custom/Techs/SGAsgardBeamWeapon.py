# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 20th August 2024, by Alex SL Gato (CharaToLoki)
#         Based on BorgAdaptation.py and PhasedTorp.py by Alex SL Gato, which were based on the Foundation import function by Dasher; the Shield.py scripts and KM Armour scripts and FoundationTechnologies team's PhasedTorp.py
#         Also based on ATPFunctions by Apollo.
#################################################################################################################
# TO-DO UPDATE THIS, ADD A WEAPON_HIT
# A modification of a modification, last modification by Alex SL Gato (CharaToLoki)
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech makes Asgard and Tollan Ion Weapons behave more like in the Stargate show, alongside its own sub-technologies that makes the behaviour even more canonical
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
try:
	modSGAsgardBeamsWeapon = __import__("Custom.Techs.SGAsgardBeamsWeapon")
	if(modSGAsgardBeamsWeapon):
		modSGAsgardBeamsWeapon.oSGAsgardBeamsWeapon.AddTorpedo(__name__)
except:
	print "SGAsgardBeamsWeapon projectile script not installed, or you are missing Foundation Tech"
"""
# NOTE, while on other similar phase-through torpedo mods your SpeciesToTorp value must be set to the NetType Multiplayer.SpeciesToTorp.PHASEDPLASAMA for it to work due to a conflict-bug fix that allows stock phased torpedoes to work regardless of having the no-dmg-through-shields mutator active or not... This mod will actually create a torpedo copy which will change to its appropiate NetType if it considers that the shields need to be pierced.
# pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
# Also please note the value here has meaning:
# "0" means hull immunity only
# "1" means shield immunity only
# "2" means both shield and hull immunity
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"SG AsgardBeams Weapon Immune": 1
}
"""
# Regarding subTechs
# As those with some idea of python language can see, you can stack more than 1 subtech.
# However, while for hulls it is recommended to be accumulative (with the ideally-coded function multiplying each effect with the old one on a percentage so it makes it stronger/weaker overall), for shields it is recommended to only add one affected sub-tech per ship in particular, since while some shield behaviours (f.ex. making the weapon pass through, or never) are more varied and sometimes could contradict each other (depending on the sub-techs handling of the "shouldPassThrough" and "considerPiercing"), the most important probable con is that shield weaknesses will stack instead of making an average value (for that you may sometimes need to make a hybrid technology).
# The fields shield and hull functions have are the following:
## "pShip": the Ship instance (not the pInstance Foundation one) of the ship that got hit by the projectile 
## "sScript": the Script from the above ship (not the hardpoint)
## "sShipScript": the filename of the ship script from above
## "pInstance": the Foundation ship Instance, which often holds the special races, techs and some more, specially in KM installs.
## "pEvent": the event in question when the projectile hit. Could be useful on certain situations
## "pTorp": the torpedo instance that hit the pShip
## "pInstancedict": the pInstance.__dict__, that way we can fetch it once without using the "hacky" __dict__ every single time we want the pInstance.__dict__
## "pAttackerShipID": the ID number of the vessel that attacked pShip, or at least the parent of the torpedo that hit pShip
## "hullDamageMultiplier": multiplies the base damage of the torpedo if it hits the hull. While you could totally overwrite the value a previous function did, it is polite to not ignore all values. On the case of hulls the functions must make sure the values are multiplied between each other (so if you make it 0.8 times something, then 2.0 times, it wil be 0.8 * 2.0 = 1.6). Careful with negative values, since they may counteract each other if an even amount of functions apply them.
## "shieldDamageMultiplier": multiplies the damage done to the shields if they are hit. While you could totally overwrite the value a previous function did, it is polite to not ignore all values. On the case of shields, functions often stack results between each other (so if you make it 0.8 times something, then 2.0 times, it wil be 0.8 + 2.0 = 2.8). Negative values are allowed.
## "shouldPassThrough": values greater than 1 means that this script will create a torpedo replica capable of bypassing the shields. Should be stacked with sums. Negative values are allowed.
## "considerPiercing": if the shield was not penetrated by the projectile hit, it will revise the shields, and if they are below a certain percentage, it will create a torpedo replica that will continue working past the shield 
## "shouldDealAllFacetDamage": values greater than 0 will make the shield recalculation function to drain all shield facets, instead of 1.
## "negateRegeneration": values greater than 0 mean that upon hitting, the shield drain will additionally perform a drain equal to each shield facet regeneration for each shield facet.
## "wasChanged": if this value is lesser than 0, it will perform the default effect (shield drain where "shouldPassThrough" = 0, "considerPiercing" = 0, "shouldPassThrough", "shieldDamageMultiplier = shieldDamageMultiplier + AsgardBeamsGenericShieldDamageMultiplier" and "negateRegeneration = negateRegeneration - 1" / default hull hit drain). When some script changes things it is recommended to stack "1" to this value, unless you want a default behaviour with modified "shieldDamageMultiplier" and "negateRegeneration"
# If you want an new specific subTech that modifies part of the SG AsgardBeams Effect, you can do it by adding a file under the scripts\Custom\Techs\SGAsgardBeamsWeaponScripts directory; if possible with a reasonable name related to the Technology(ies) it covers. 
# For example, if the special sub-tech is called "SG Shields" you can call the file "SGShieldsConfiguration.py"; Sometimes certain sub-techs may go together on the same function of a file because being related or being sub-components.
# Below there's an example used for the aforementioned SGShieldsConfiguration, at least the 1.0 version, but modified to include more function examples, clarify and with some parts commented so as to not trigger commentary issues - those sections have replaced the triple " with ####@@@
"""
TO-DO UPDATE THIS SECTION

"""

import App

from bcdebug import debug
import traceback
import nt
import string

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.92",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }
# A. GENERAL BASIC CONFIGURATION
# Some generic info that would affect mostly everyone
AsgardBeamsGenericShieldDamageMultiplier = 100.0 # An Asgard Beam in 4-6 hits can take down an Ori shield. Ori Mothership shields at the time of release have 150k shields, current asgard beams have 25000 * 0.75 dmg = 18750 ...so we need to deal at a minimum 150k * 0.75 (enough to bypass Ori shields) / 4 <= 29k dmg per shot. For bleedthrough control reasons the Asgard torpedo base damage needs to be a 100th part, so it deals 300 dmg, which we need to multiply by 100 to get the desired damage ##### TO-DO ####(for regular STBC compatibility, and because a Wraith cruiser has 12000 hull, either add a multiplier for Wraith ships that reduce that damage to 9000 (multiplier 30 in the end) )
AsgardBeamsHullDamageMultiplier = 50.0 # To avoid blasting the Ori hull almost always in one hit.

# At the moment I cannot really think of one ship immune to both effects in particular legacy-wise... adding this Dummy
global lImmuneSGAsgardBeamsWeaponShips
lImmuneSGAsgardBeamsWeaponShips = []

#### TO-DO ####


SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side

# "variableNames" is a global dictionary, filled automatically by the files in scripts/Custom/Techs/SGAsgardBeamsWeaponScripts 
# the purpose of this list is to append dicts f.ex. {"legacyImmunity": alist, "interactionHullBehaviour": functionObtained, "interactionShieldBehaviour": anotherfunctionObtained}
# the "legacyImmunity" field is there only to add some ships on a legacy list to be fully immune to all effects of this weapon to hull and shields.
# the "interactionHullBehaviour" will have a function that will be called to calculate the damage reduction or amplification to the hull, those functions are meant to be stacked.
# the "interactionShieldBehaviour" will try to do the same, but for shields. On this case, due to certain franchise differences, while some effects will be stacked, it is recommended to only add one of a type, or create a hybrid function if you want multiple of these to be added (f.ex one function could tell the script that they can bypass always, while another says they cannot bypass).
# Alongside these parameters, there are additional ones, but will be ignored unless they are on the "BasicSGAsgardBeamsWeaponConfiguration.py" subTech file:
## "AsgardBeamsHullDamageMultiplier": allows to edit the base damage multiplier to all hulls without needing to edit the main technology file. Default is 10 (10 -1, to deal 10 times the original damage, this script deals those 9 extra).
## "AsgardBeamsGenericShieldDamageMultiplier": allows to edit the base damage multiplier to all shields without needing to edit the main technology file. Default is 2 (2 -1, means deal damage once more)
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

	dir="scripts\\Custom\\Techs\\SGAsgardBeamsWeaponScripts" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	try:
		list = nt.listdir(dir)
		if not list:
			print "ERROR: Missing scripts/Custom/Techs/SGAsgardBeamsWeaponScripts folder for SGAsgardBeamWeapon technology"
			return 0

	except:
		print "ERROR: Missing scripts/Custom/Techs/SGAsgardBeamsWeaponScripts folder for SGAsgardBeamWeapon technology, or other error:"
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
							banana = __import__(myGoodPlugin, globals(), locals(), ["AsgardBeamsHullDamageMultiplier", "AsgardBeamsGenericShieldDamageMultiplier", "SlowDownRatio"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals())
					
					if hasattr(banana, "legacyImmunity"): # These will not be affected at all by the hull or shield effects, period
						global lImmuneSGAsgardBeamsWeaponShips
						for item in banana.legacyImmunity:
							lImmuneSGAsgardBeamsWeaponShips.append(item)

					if hasattr(banana, "interactionShieldBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionShieldBehaviour"] = banana.interactionShieldBehaviour

					if hasattr(banana, "interactionHullBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionHullBehaviour"] = banana.interactionHullBehaviour

					if fileName == "BasicSGAsgardBeamsWeaponConfiguration":
						if hasattr(banana, "AsgardBeamsHullDamageMultiplier"):
							global AsgardBeamsHullDamageMultiplier
							AsgardBeamsHullDamageMultiplier = banana.AsgardBeamsHullDamageMultiplier

						if hasattr(banana, "AsgardBeamsGenericShieldDamageMultiplier"):
							global AsgardBeamsGenericShieldDamageMultiplier
							AsgardBeamsGenericShieldDamageMultiplier = banana.AsgardBeamsGenericShieldDamageMultiplier

						if hasattr(banana, "SlowDownRatio"):
							global SlowDownRatio
							SlowDownRatio = banana.SlowDownRatio

					#print "SGAsgardBeamsWeapon reviewing of this subtech is a success"
			except:
				print "someone attempted to add more than they should to the SGAsgardBeamsWeapon script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
print AsgardBeamsHullDamageMultiplier, AsgardBeamsGenericShieldDamageMultiplier
print variableNames

try:
	import Foundation
	import FoundationTech
	import MissionLib
	import Multiplayer.SpeciesToTorp

	torpsNetTypeThatCanPhase = Multiplayer.SpeciesToTorp.PHASEDPLASMA # For the "torpedoes-going-through" issue

	from ftb.Tech.ATPFunctions import *
	from math import *

	# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
	def NiPoint3ToTGPoint3(p):
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x, p.y, p.z)
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
		pTorp.SetUsePhysics(0) # TO-DO CHECK IF THIS CAUSES MORE ISSUES
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

		print "Torpedo mass", pTorp.GetMass()

		return pTorp

	class SGAsgardBeamsWeapon(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name)
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")
			App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")

		def IsSGAsgardBeamsWeaponYield(self):
			return 1

		def IsPhaseYield(self):
			return 0

		def IsDrainYield(self):
			return 0

		def EventInformation(self, pEvent):
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

			return fRadius, fDamage, kPoint

		def shieldRecalculationAndBroken(self, pShip, kPoint, extraDamageHeal, shieldThreshold = 0.25, multifacet = 0, negateRegeneration=0):

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
						resultHeal = fCurr + extraDamageHeal + fRecharge
						if resultHeal < 0.0:
							resultHeal = 0.0
						elif resultHeal > fMax:
							resultHeal = fMax
						pShields.SetCurShields(shieldDir, resultHeal)
						
						if shieldDirNearest == shieldDir and (fMax <= 0 or resultHeal < (shieldThreshold * fMax)):
							shieldHitBroken = 1
			else:
				shieldHitBroken = 1

			return shieldHitBroken

		def OneWeaponHit(self, pEvent): # This throws attribute Error TO-DO CHECK WHY
			debug(__name__ + ", OneWeaponHit")
			try:
				# First check we have valid targets and attackers
				print "weapon hit"
				pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
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
			
				if not pAttackerInstance or not pAttackerInstance.__dict__.has_key("SG Asgard Beams Weapon"):
					print "attacker lacks asgard beams"
					return 0



				# Then check immunities before doing calculations
				sScript     = pTarget.GetScript()
				sShipScript = string.split(sScript, ".")[-1]

				global lImmuneSGAsgardBeamsWeaponShips # This legacy list goes first - it is to reduce unnecessary calculations
				if sShipScript in lImmuneSGAsgardBeamsWeaponShips:
					return 0

				if pTargetInstance:
					pTargetInstanceDict = pTargetInstance.__dict__
					if(pEvent.IsHullHit()):
						 if pTargetInstanceDict.has_key('SG Asgard Beams Weapon Immune') and (pTargetInstanceDict['SG Asgard Beams Weapon Immune'] == 0 or pTargetInstanceDict['SG Asgard Beams Weapon Immune'] > 1):
							return 0
					else:
						if pTargetInstanceDict.has_key('SG Asgard Beams Weapon Immune') and pTargetInstanceDict['SG Asgard Beams Weapon Immune'] > 0:
							return 0

				# Ok now the shot is almost guaranteed, proceed with calculations

				fRadius, fDamage, kPoint = self.EventInformation(pEvent)
				if fDamage <= 0.0:
					return

				# TO-DO MAYBE MOVE TO OTHER AREA TO BE MORE EFFICIENT?
				# TO-DO IF THE ORI KEEP GETTING INVULNERABLE SPOTS WHILE A REGULAR SHIP WITH HUGE SHIELDS LACKS THE ISSUE, THEN ADJUST THE SG SHIELDS THING SO IF DOES A WHOLE SHIELD CHECKOUT INSTEAD OF JUST ONE FACET
				# TO-DO CHECK ways to avoid the torpedo making the target spin like crazy if hit, also check if yo can make the Torp.SetUsePhysics(0) or something that disabled teh collision knockback for that torp in particular, also check pTorp.GetMass and such, or if you can apply to the object that was hit a negative force pShip.ApplyForce()
				# TO-DO MAYBE FOR HULL HIT VERIFY FOR TORPS IF THEIR DAMAGE RADIUS EQUALS THEIR TORP DAMAGE RADIUS, SO IF THE HULL WAS HIT MAYBE DO SOMETHING?
				hullDamageMultiplier = 1.0 
				shieldDamageMultiplier = 1.0
				shouldPassThrough = 0
				#considerPiercing = 0

				pAttackerInstanceDict = pAttackerInstance.__dict__

				global AsgardBeamsGenericShieldDamageMultiplier, AsgardBeamsHullDamageMultiplier

				baseHullMultiplier = 1.0 * AsgardBeamsHullDamageMultiplier
				baseShieldMultiplier = 1.0 * AsgardBeamsGenericShieldDamageMultiplier
	
				if pAttackerInstanceDict["SG Asgard Beams Weapon"].has_key("HullDmgMultiplier") and pAttackerInstanceDict["SG Asgard Beams Weapon"]["HullDmgMultiplier"] > 0.0:
					baseHullMultiplier = baseHullMultiplier * pAttackerInstanceDict["SG Asgard Beams Weapon"]["HullDmgMultiplier"]

				if pAttackerInstanceDict["SG Asgard Beams Weapon"].has_key("ShieldDmgMultiplier") and pAttackerInstanceDict["SG Asgard Beams Weapon"]["ShieldDmgMultiplier"] > 0.0:
					baseShieldMultiplier = baseShieldMultiplier * pAttackerInstanceDict["SG Asgard Beams Weapon"]["ShieldDmgMultiplier"]

				#### TO-DO CONTINUE HERE ####

				wasHullChanged = 0
				# TO-DO ADJUST CODE BELOW PROPERLY
				'''
				for item in variableNames.keys():
					if variableNames[item].has_key("interactionHullBehaviour"): # These are reserved for when the hull has been hit! These are meant to be accumulative, for defenses.
						hullDamageMultiplier3 = 0
						shieldDamageMultiplier3 = 0
						shouldPassThrough3 = 0
						considerPiercing3 = 0
						shouldDealAllFacetDamage3 = 0
						wasHullChanged3 = 0
						negateShieldRegeneration3 = 0
						try:
							hullDamageMultiplier3, shieldDamageMultiplier3, shouldPassThrough3, considerPiercing3, shouldDealAllFacetDamage3, wasHullChanged3, negateShieldRegeneration3 = variableNames[item]["interactionHullBehaviour"](pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, attackerID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasHullChanged, negateShieldRegeneration)
						except:
							hullDamageMultiplier3 = hullDamageMultiplier
							shieldDamageMultiplier3 = shieldDamageMultiplier
							shouldPassThrough3 = shouldPassThrough
							considerPiercing3 = considerPiercing
							shouldDealAllFacetDamage3 = shouldDealAllFacetDamage
							wasHullChanged3 = wasHullChanged
							negateShieldRegeneration3 = negateShieldRegeneration
							print "Some SGAsgardBeamsWeapon hull subtech suffered an error"
							traceback.print_exc()

						hullDamageMultiplier = hullDamageMultiplier3
						shieldDamageMultiplier = shieldDamageMultiplier3
						shouldPassThrough = shouldPassThrough3
						considerPiercing = considerPiercing3
						shouldDealAllFacetDamage = shouldDealAllFacetDamage3
						negateShieldRegeneration = negateShieldRegeneration3
						wasHullChanged = wasHullChanged3
				'''
				if wasHullChanged > 0:
					baseHullMultiplier = baseHullMultiplier * hullDamageMultiplier
				
				wasShieldChanged = 0
				# TO-DO ADJUST CODE BELOW PROPERLY
				'''
				for item in variableNames.keys():
					if variableNames[item].has_key("interactionShieldBehaviour"): # These are reserved for when the shield has been hit! Also be careful, since these are more likely to stack weaknesses! Preferable to only have one of this type per ship
						try:
							hullDamageMultiplier2 = 0
							shieldDamageMultiplier2 = 0
							shouldPassThrough2 = 0
							considerPiercing2 = 0
							shouldDealAllFacetDamage2 = 0
							wasShieldChanged2 = 0
							negateShieldRegeneration2 = 0				
							hullDamageMultiplier2, shieldDamageMultiplier2, shouldPassThrough2, considerPiercing2, shouldDealAllFacetDamage2, wasShieldChanged2, negateShieldRegeneration2 = variableNames[item]["interactionShieldBehaviour"](pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, attackerID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasShieldChanged, negateShieldRegeneration)
						except:
							hullDamageMultiplier2 = hullDamageMultiplier
							shieldDamageMultiplier2 = shieldDamageMultiplier
							shouldPassThrough2 = shouldPassThrough
							considerPiercing2 = considerPiercing
							shouldDealAllFacetDamage2 = shouldDealAllFacetDamage
							wasShieldChanged2 = wasShieldChanged
							negateShieldRegeneration2 = negateShieldRegeneration
							print "Some SGIonWeapon shield subtech suffered an error"
							traceback.print_exc()

						hullDamageMultiplier = hullDamageMultiplier2
						shieldDamageMultiplier = shieldDamageMultiplier2
						shouldPassThrough = shouldPassThrough2
						considerPiercing = considerPiercing2
						shouldDealAllFacetDamage = shouldDealAllFacetDamage2
						wasShieldChanged = wasShieldChanged2
						negateShieldRegeneration = negateShieldRegeneration2
				'''
				if wasShieldChanged <= 0:
					# normal shields
					shouldPassThrough = 0
					#considerPiercing = 1 # TO-DO remove unused fields
					#shouldDealAllFacetDamage = 0 
					#negateShieldRegeneration = 0
				else:
					baseShieldMultiplier = baseShieldMultiplier * shieldDamageMultiplier

				if pEvent.GetWeaponType() == pEvent.PHASER: # TO-DO if in the end torpedoes are only fired if they are phasers, maybe get considerations above inside this area
					# TO-DO ALSO ADD THE OPTION SO ONLY A FEW PHASERS ARE ASGARD BEAMS, LIKE WITH TACHYONBEAM TECH
					print "it is a phaser, generating the torp"

					pHitPoint = NiPoint3ToTGPoint3(pEvent.GetWorldHitPoint())

					pWeaponFired = App.Weapon_Cast(pEvent.GetSource())

					if pWeaponFired == None:
						print "no weapon stopped fired obj..."
						return 0

					pVec = CopyVector(pHitPoint) #NiPoint3ToTGPoint3(pEvent.GetWorldHitPoint())
					pWpnPos = NiPoint3ToTGPoint3(pWeaponFired.GetWorldLocation())
					pVec.Subtract(pWpnPos)
					pVec.Unitize()
					pVec.Scale(1)


					# TO-DO GET PHASER POWER
					thePowerPercentageWanted = 1.0
					pParentFired = pAttacker.GetPhaserSystem()
					if pParentFired:
						thePowerPercentageWanted = (pParentFired.GetPowerLevel()/2.0) # The 2.0 is ebcause the phasers work that way, 100% is 2, 50% is 1, 0% is 0
						print "power wanted for the phaser: ", thePowerPercentageWanted
					else:
						pParentFired = pWeaponFired.GetParentSubsystem() #TO-DO ACTUALLY CHECK THE PHASER INTENSITY PROPERTY? PhaserSystem.GetPowerLevel()
						if pParentFired:
							thePowerPercentageWanted = (App.PoweredSubsystem_Cast(pParentFired).GetPowerLevel()/2.0)
					if thePowerPercentageWanted <= 0.0:
						print "Nvm power percentage is no dmg"
						return 0

					pTargetBID = pWeaponFired.GetTargetID()
					pTargetB = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTargetBID))
					if pTargetB:
						targetID = pTargetB.GetObjID()			

					global SlowDownRatio
					mod = "Tactical.Projectiles.SGAsgardBeamDummy" # TO-DO CHANGE TO A NEW ONE This torpedo was made so Automated Point Defence scripts stop harrasing us! First we make 
					try:
						torpImportedInfo = __import__(mod)
						baseTorpDamage = torpImportedInfo.GetDamage()
						leNetType = Multiplayer.SpeciesToTorp.DISRUPTOR
						if shouldPassThrough > 0:
							print "bypassing shields"
							leNetType = Multiplayer.SpeciesToTorp.PHASEDPLASMA
							#pHitPoint.Add(pVec) # add because we want to guarantee they bypass the shields
						else:
							print "not bypassing shields"
							pHitPoint.Subtract(pVec) # subtract because we want to guarantee they always hit the shields

						if(pEvent.IsHullHit()):
							print "hull damage calc"
							finalTorpDamage = thePowerPercentageWanted * baseTorpDamage * baseHullMultiplier
						else:

							print "shield damage calc"
							finalTorpDamage = thePowerPercentageWanted * baseTorpDamage * baseShieldMultiplier

						launchSpeed = __import__(mod).GetLaunchSpeed()

						if fRadius <= 0.0:
							fRadius = 0.00125
						else:
							fRadius = fRadius * 0.0001

						print "final torp damage is ", finalTorpDamage

						pTempTorp = FireTorpFromPointWithVectorAndNetType(pHitPoint, pVec, mod, targetID, attackerID, launchSpeed, leNetType, finalTorpDamage, fRadius, 0, pTarget) # TO-DO 1, pTarget)
						#pTempTorp.SetUsePhysics(0)
						pTempTorp.SetLifetime(4.0)			
					except:
						print "You are missing 'Tactical.Projectiles.SGAsgardBeamDummy' torpedo on your install, without that the SG Asgard Beam Weapons here cannot deal extra hull damage... or another error happened"
						traceback.print_exc()

					else:
						print "The hull was not hit by the Asgard beam weapon"


				elif pEvent.GetWeaponType() != pEvent.TRACTOR_BEAM:
					#TO-DO It's a projectile, so we do nothing... I think?
					print "it's a torp"

				# We get first information about defences that the other may have.			
			
			except:
				print "	Error when handling SG Asgard Beams Weapon Hit"
				traceback.print_exc()
			return 0


		####TO-DO REMOVE UNUSED FUNCTONS####

	def ConvertPointNiToTG(point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	oSGAsgardBeamsWeapon = SGAsgardBeamsWeapon("SG Asgard Beams Weapon")
	print "Asgard Beams operational"

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"
	traceback.print_exc()

class SGAsgardBeamsWeaponDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnProjectileDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		if oYield and hasattr(oYield, "IsSGAsgardBeamsWeaponYield") and oYield.IsSGAsgardBeamsWeaponYield() != 0 and pInstance and pInstance.__dict__.has_key('SG AsgardBeams Weapon Immune') and pInstance.__dict__['SG AsgardBeams Weapon Immune'] >= 2:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)
		pInstance.lPulseDefense.insert(self)


oSGAsgardBeamsWeaponImmunity = SGAsgardBeamsWeaponDef('SG Asgard Beams Weapon Immune')