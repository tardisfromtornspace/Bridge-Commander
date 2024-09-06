# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 4th September 2024, by Alex SL Gato (CharaToLoki)
#         Based on SGIonAdaptation.py, BorgAdaptation.py and PhasedTorp.py by Alex SL Gato, which were based on the Foundation import function by Dasher; the Shield.py scripts and KM Armour scripts and FoundationTechnologies team's PhasedTorp.py
#         Also based on ATPFunctions by Apollo.
#################################################################################################################
# A modification of a modification, last modification by Alex SL Gato (CharaToLoki)
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech is meant to adjust some SG Go'auld Plasma Weapons to behave a bit more like in the Stargate show, alongside its own sub-technologies that makes the behaviour even more canonical.
# On this case, the tech is here to adjust to the fact why a >1000 megaton naquadah-enhanced nuclear bomb dealt no visible damage to an Early Ha'tak Go'auld shields, yet a few bolts from a Death Glider (which has far less firepower than that bomb) could affect a Ha'tak shield.
# Additionally, it is added as a way to make another difference between SG Shields/Hulls and ST Shields/Hulls regarding plasma weapons:
## If the plasma weapon is small and/or primitive, ST shields block them extremely easily with no strain at all. However, if the weapon is big or extremely advanced, the shields may strain.
## On unshielded vessels, even primitive plasma weapons can be problematic to handle - at least on the 23rd century TOS ships.
# For this, we added a hull modifier (HullDmgMultiplier) and shield modifier (ShieldDmgMultiplier), with the option of being customizable since some weapon's damage may depend on entirely different factos we cannot forsee.
# Values of 1.0 to those modifierds will be counted as no damage, since the normal torpedo will have already dealt such damage, so values of 2.0, 3.0, etc. will actually make this script deal 1.0, 2.0, etc -1 times the base damage, for a total of 2.0, 3.0, etc. damage in the end
# At the bottom of your torpedo projectile file add this (Between the """ and """):
"""
def HullDmgMultiplier():
	return 4

def ShieldDmgMultiplier():
	return 4

try:
	modSGPlasmaWeaponTorp = __import__("Custom.Techs.SGPlasmaWeapon")
	if(modSGPlasmaWeaponTorp):
		modSGPlasmaWeaponTorp.oSGPlasmaWeaponTorp.AddTorpedo(__name__)
except:
	print "SGPlasmaWeapon projectile script not installed, or you are missing Foundation Tech"
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
	"SG Plasma Weapon Immune": 1
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
## "shieldDamageMultiplier": multiplies the damage done to the shields if they are hit. While you could totally overwrite the value a previous function did, it is polite to not ignore all values. On the case of hulls the functions must make sure the values are multiplied between each other (so if you make it 0.8 times something, then 2.0 times, it wil be 0.8 * 2.0 = 1.6). Careful with negative values, since they may counteract each other if an even amount of functions apply them.
## "shouldPassThrough": values greater than 1 means that this script will create a torpedo replica capable of bypassing the shields. Should be stacked with sums. Negative values are allowed. Default is no passing through.
## "considerPiercing": if the shield was not penetrated by the projectile hit, it will revise the shields, and if they are below a certain percentage, it will create a torpedo replica that will continue working past the shield
## "shouldDealAllFacetDamage": values greater than 0 will make the shield recalculation function to drain all shield facets, instead of 1. Default is not considering shield piercing.
## "wasChanged": if this value is lesser than 0, it will perform the default effect (shield drain where "shouldDealAllFacetDamage = 0" and "shieldDamageMultiplier = PlasmaGenericShieldDamageMultiplier" * maybe ShieldDmgMultiplier/"hullDamageMultiplier = pTorp.HullDmgMultiplier() - 1" or "hullDamageMultiplier = PlasmaHullDamageMultiplier -1"). When some script changes things it is recommended to stack "1" to this value, unless you want a default behaviour with modified "shouldPassThrough" and "considerPiercing".
# If you want an new specific subTech that modifies part of the SG Plasma Effect, you can do it by adding a file under the scripts\Custom\Techs\SGPlasmaWeaponScripts directory; if possible with a reasonable name related to the Technology(ies) it covers. 
# For example, if the special sub-tech is called "SG Shields" you can call the file "SGShieldsConfiguration.py"; Sometimes certain sub-techs may go together on the same function of a file because being related or being sub-components.
# Below there's an example used for the aforementioned SGShieldsConfiguration, at least the 1.0 version, but modified to include more function examples, clarify and with some parts commented so as to not trigger commentary issues - those sections have replaced the triple " with ####@@@
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGPlasmaWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGPlasmaWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by SG Plasma Weapons.
# The reason we make a tech for this, is because SG Shields behave differently from ST, SW shields or B5 defences against a Plasma Weapon.
# On this case, the tech is here to adjust to the fact why a >1000 megaton naquadah-enhanced nuclear bomb dealt no visible damage to an Early Ha'tak Go'auld shields, yet a few bolts from a Death Glider (which has far less firepower than that bomb) could affect a Ha'tak shield.

# On this case, more info about SG shields will be reviewed on their main SG Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info

##### This list (if the list has the SAME EXACT variable name) will add legacy immunity to the pShip files listed below... the names need to be a case-sensitive exact match.
# However the list is commented since it is unneeded for this subTech. Actually, it's preferable to have these legacy immunity lists on a separate file, less code modification issues later on that way.
# legacyImmunity = ["Greystar", "HexagonalNexul", "CharaToLoki"]

##### The commented parameters below, if uncommented, will be ignored unless they are on the appropiate file (see code comments below this sub-tech file example)
#PlasmaHullDamageMultiplier = 4
#PlasmaGenericShieldDamageMultiplier = 4
#SlowDownRatio = 3.0/75.0

PlasmaSGVulnerableShields = [] # No actual SG vessel is vulnerable to Go'auld Plasma cannons in the way the Go'auld were to Tollan or Asgard Ion ones. Just leaving this here in case someone randomly wants to add that for a fanmade ship or something
PlasmaSGShieldDamageMultiplier = 4.0

## Some SG-related resistances - unless there's a new Stargate franchise adding more races and spaceship combat, these should do the job
## Adding Asgard and Ori here, because the Asgard used neutronium on their vessel alloys, and for most of them the Plasma cannons were primitive enough that Asgard shields could handle them easier (excluding Anubis-grade ones)
## The Ori just because they may have some random ascended-knowledge thing going on, and as a way to reduce damage bleedthrough in certain models mod-wise.
xAsgardShieldMultiplier = 0.75
xAsgardHullMultiplier = 0.8
xAnubisShieldMultiplier = 0.6 # Seems fair that when Anubis upgraded his shields, it also made them more resistant to the mainstream weapons the Go'auld use
xAlteranShieldMultiplier = 1.0
xAlteranHullMultiplier = 1.0
xOriShieldMultiplier = 0.52
xOriHullMultiplier = 0.95


##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstance and pInstancedict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		global PlasmaSGShieldDamageMultiplier, xAnubisShieldMultiplier, xAsgardShieldMultiplier, xAlteranShieldMultiplier, xOriShieldMultiplier

		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()
		else: # default multiplication dmg to shields
			shieldDamageMultiplier = shieldDamageMultiplier * PlasmaSGShieldDamageMultiplier
		shouldDealAllFacetDamage = 0
		considerPiercing = considerPiercing + 1
		if pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech in PlasmaSGVulnerableShields:
				shouldPassThrough = 1
			elif RaceShieldTech == "Anubis Go'auld": # Resistances	
				shieldDamageMultiplier = shieldDamageMultiplier * xAnubisShieldMultiplier
						 
			elif RaceShieldTech == "Asgard": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldMultiplier
			elif RaceShieldTech == "Alteran" or RaceShieldTech == "Lantian" or RaceShieldTech == "Lantean" or RaceShieldTech == "Asuran": # Resistances, not including actual Replicator ships here because those will have their own tech
				shieldDamageMultiplier = shieldDamageMultiplier * xAlteranShieldMultiplier
			elif RaceShieldTech == "Ori": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xOriShieldMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstance and pInstancedict.has_key("SG Shields"):
		RaceShieldTech = None
		if pInstancedict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pInstancedict["SG Shields"]["RaceHullTech"]
		elif pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]

		if RaceShieldTech != None:
			global xAsgardHullMultiplier, xAlteranHullMultiplier, xOriHullMultiplier
			wasChanged = wasChanged + 1
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]	
			if RaceShieldTech == "Asgard":
				hullDamageMultiplier = hullDamageMultiplier * xAsgardHullMultiplier
			elif RaceShieldTech == "Alteran" or RaceShieldTech == "Lantian" or RaceShieldTech == "Lantean" or RaceShieldTech == "Asuran":
				hullDamageMultiplier = hullDamageMultiplier * xAlteranHullMultiplier
			elif RaceShieldTech == "Ori":
				hullDamageMultiplier = hullDamageMultiplier * xOriHullMultiplier




	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

"""

import App

from bcdebug import debug
import traceback
import nt
import string

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.93",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }
# A. GENERAL BASIC CONFIGURATION
# Some generic info that would affect mostly everyone
PlasmaHullDamageMultiplier = 10.0

# At the moment I cannot really think of one ship immune to both effects in particular legacy-wise... adding this Dummy
global lImmuneSGPlasmaWeaponShips
lImmuneSGPlasmaWeaponShips = []

# For every other ship (because since STBC is a ST game, the shields in-game behave more like ST shields, specifically simplified 24th century Post-Dominion War Federation ones, so we must take them as a base), excluding the examples mentioned below, this weapon causes a shield drain in each shield facet equivalent to the projectile damage received. If the hull is hit, it will deal 10 times the damage the normal projectile does.
PlasmaGenericShieldDamageMultiplier = 1 # one from the normal shot, another from us

SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side

# "variableNames" is a global dictionary, filled automatically by the files in scripts/Custom/Techs/SGPlasmaWeaponScripts 
# the purpose of this list is to append dicts f.ex. {"legacyImmunity": alist, "interactionHullBehaviour": functionObtained, "interactionShieldBehaviour": anotherfunctionObtained}
# the "legacyImmunity" field is there only to add some ships on a legacy list to be fully immune to all effects of this weapon to hull and shields.
# the "interactionHullBehaviour" will have a function that will be called to calculate the damage reduction or amplification to the hull, those functions are meant to be stacked.
# the "interactionShieldBehaviour" will try to do the same, but for shields. On this case, due to certain franchise differences, while some effects will be stacked, it is recommended to only add one of a type, or create a hybrid function if you want multiple of these to be added (f.ex one function could tell the script that they can bypass always, while another says they cannot bypass).
# Alongside these parameters, there are additional ones, but will be ignored unless they are on the "BasicSGPlasmaWeaponConfiguration.py" subTech file:
## "PlasmaHullDamageMultiplier": allows to edit the base damage multiplier to all hulls without needing to edit the main technology file. Default is 10 (10 -1, to deal 10 times the original damage, this script deals those 9 extra).
## "PlasmaGenericShieldDamageMultiplier": allows to edit the base damage multiplier to all shields without needing to edit the main technology file. Default is 2 (2 -1, means deal damage once more)
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

	dir="scripts\\Custom\\Techs\\SGPlasmaWeaponScripts" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	list = nt.listdir(dir)
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
				if not filesChecked.has_key(fileName):
					filesChecked[fileName] = 1
					myGoodPlugin = dotPrefix + fileName

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["legacyImmunity", "interactionShieldBehaviour", "interactionHullBehaviour"])
					except:
						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["PlasmaHullDamageMultiplier", "PlasmaGenericShieldDamageMultiplier", "SlowDownRatio"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals())
					
					if hasattr(banana, "legacyImmunity"): # These will not be affected at all by the hull or shield effects, period
						global lImmuneSGPlasmaWeaponShips
						for item in banana.legacyImmunity:
							lImmuneSGPlasmaWeaponShips.append(item)

					if hasattr(banana, "interactionShieldBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionShieldBehaviour"] = banana.interactionShieldBehaviour

					if hasattr(banana, "interactionHullBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionHullBehaviour"] = banana.interactionHullBehaviour

					if fileName == "SGPlasmaWeaponBasicConfiguration":
						if hasattr(banana, "PlasmaHullDamageMultiplier"):
							global PlasmaHullDamageMultiplier
							PlasmaHullDamageMultiplier = banana.PlasmaHullDamageMultiplier

						if hasattr(banana, "PlasmaGenericShieldDamageMultiplier"):
							global PlasmaGenericShieldDamageMultiplier
							PlasmaGenericShieldDamageMultiplier = banana.PlasmaGenericShieldDamageMultiplier

						if hasattr(banana, "SlowDownRatio"):
							global SlowDownRatio
							SlowDownRatio = banana.SlowDownRatio

					#print "SGPlasmaWeapon reviewing of this subtech is a success"
			except:
				print "someone attempted to add more than they should to the SGPlasmaWeapon script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print PlasmaHullDamageMultiplier, PlasmaGenericShieldDamageMultiplier
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

		return pTorp

	class SGPlasmaWeaponTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def IsSGPlasmaWeaponYield(self):
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

		def shieldRecalculationAndBroken(self, pShip, kPoint, extraDamageHeal, shieldThreshold = 0.25, multifacet = 0):

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
				
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					if shieldDirNearest == shieldDir or multifacet != 0:
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						resultHeal = fCurr + extraDamageHeal
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

		def OnYield(self, pShip, pInstance, pEvent, pTorp):
			if not pShip:
				return

			pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
			if not pShip:
				return

			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]

			global lImmuneSGPlasmaWeaponShips # This legacy list goes first - it is to reduce unnecessary calculations
			if sShipScript in lImmuneSGPlasmaWeaponShips:
				return

			global torpsNetTypeThatCanPhase, variableNames
			fRadius, fDamage, kPoint = self.EventInformation(pEvent)

			pHitPoint = ConvertPointNiToTG(pTorp.GetWorldLocation())
			pVec = pTorp.GetVelocityTG()
			pVec.Scale(0.001)

			global PlasmaHullDamageMultiplier, PlasmaGenericShieldDamageMultiplier, defenceGridMultiplier, hullPolarizerMultiplier, shadowDispersiveHullMultiplier
			hullDamageMultiplier = 1.0
			shieldDamageMultiplier = PlasmaGenericShieldDamageMultiplier

			shouldPassThrough = 0
			considerPiercing = 0
			shouldDealAllFacetDamage = 0

			pInstancedict = pInstance.__dict__
			try:
				attackerID = pTorp.GetParentID()
			except:
				attackerID = App.NULL_ID

			if(pEvent.IsHullHit()):
				if pInstancedict.has_key('SG Plasma Weapon Immune') and (pInstancedict['SG Plasma Weapon Immune'] == 0 or pInstancedict['SG Plasma Weapon Immune'] > 1):
					return
				wasHullChanged = 0
				for item in variableNames.keys():
					if variableNames[item].has_key("interactionHullBehaviour"): # These are reserved for when the hull has been hit! These are meant to be accumulative, for defenses.
						hullDamageMultiplier3 = 0
						shieldDamageMultiplier3 = 0
						shouldPassThrough3 = 0
						considerPiercing3 = 0
						shouldDealAllFacetDamage3 = 0
						wasHullChanged3 = 0
						try:
							hullDamageMultiplier3, shieldDamageMultiplier3, shouldPassThrough3, considerPiercing3, shouldDealAllFacetDamage3, wasHullChanged3 = variableNames[item]["interactionHullBehaviour"](pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, attackerID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasHullChanged)
						except:
							hullDamageMultiplier3 = hullDamageMultiplier
							shieldDamageMultiplier3 = shieldDamageMultiplier
							shouldPassThrough3 = shouldPassThrough
							considerPiercing3 = considerPiercing
							shouldDealAllFacetDamage3 = shouldDealAllFacetDamage
							wasHullChanged3 = wasHullChanged
							print "Some SGPlasmaWeapon hull subtech suffered an error"
							traceback.print_exc()

						hullDamageMultiplier = hullDamageMultiplier3
						shieldDamageMultiplier = shieldDamageMultiplier3
						shouldPassThrough = shouldPassThrough3
						considerPiercing = considerPiercing3
						shouldDealAllFacetDamage = shouldDealAllFacetDamage3
						wasHullChanged = wasHullChanged3

				if wasHullChanged <= 0: # If no changes were made, default damage for ST hulls
					if hasattr(pTorp, "HullDmgMultiplier"): # If this torp has a special global multiplier, then we use it
						hullDamageMultiplier = pTorp.HullDmgMultiplier() - 1
					else:
						hullDamageMultiplier = PlasmaHullDamageMultiplier -1 # This represents the extra damage, so if something deals 2 times the damage to a shield facet or the hull, we only add that extra damage once, as the first time was already added normally.

				finalHullDamage = fDamage * hullDamageMultiplier

				# OPTION 2: IMPORT A DUMMY TORP, give it the damage radious factor and damage we have, and make it invisible. Pros compared with first option (manually dealing extra damage ourselves), is that armours and special defense techs work better. Cons, point defence script might work twice and manage to shot it down (extremely unlikely, but not necessarily impossible if we are not careful).
				global SlowDownRatio
				mod = "Tactical.Projectiles.ExtraPhasedDamageDummyPlasma" # This torpedo was made so Automated Point Defence scripts stop harrasing us! 
				try:
					launchSpeed = __import__(mod).GetLaunchSpeed()

					pHitPoint.Add(pVec)

					pTempTorp = FireTorpFromPointWithVectorAndNetType(pTorp.GetWorldLocation(), pVec, mod, pShip.GetObjID(), attackerID, launchSpeed, pTorp.GetNetType(), finalHullDamage, pTorp.GetDamageRadiusFactor(), 1, pShip)
					pTempTorp.SetLifetime(15.0)			
				except:
					print "You are missing 'Tactical.Projectiles.ExtraPhasedDamageDummy' torpedo on your install, without that the SG Plasma Weapons here cannot deal extra hull damage... or another error happened"
					traceback.print_exc()

				return

			# Now we are doing shield stuff calculations
			# First, what kind of shield tech we have here?
			if pInstancedict.has_key('SG Plasma Weapon Immune') and pInstancedict['SG Plasma Weapon Immune'] > 0:
				return

			wasShieldChanged = 0
			for item in variableNames.keys():
				if variableNames[item].has_key("interactionShieldBehaviour"): # These are reserved for when the shield has been hit! Also be careful, since these are more likely to stack weaknesses! Preferable to only have one of this type per ship
					try:
						hullDamageMultiplier2 = 0
						shieldDamageMultiplier2 = 0
						shouldPassThrough2 = 0
						considerPiercing2 = 0
						shouldDealAllFacetDamage2 = 0
						wasShieldChanged2 = 0				
						hullDamageMultiplier2, shieldDamageMultiplier2, shouldPassThrough2, considerPiercing2, shouldDealAllFacetDamage2, wasShieldChanged2 = variableNames[item]["interactionShieldBehaviour"](pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, attackerID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasShieldChanged)
					except:
						hullDamageMultiplier2 = hullDamageMultiplier
						shieldDamageMultiplier2 = shieldDamageMultiplier
						shouldPassThrough2 = shouldPassThrough
						considerPiercing2 = considerPiercing
						shouldDealAllFacetDamage2 = shouldDealAllFacetDamage
						wasShieldChanged2 = wasShieldChanged
						print "Some SGPlasmaWeapon shield subtech suffered an error"
						traceback.print_exc()

					hullDamageMultiplier = hullDamageMultiplier2
					shieldDamageMultiplier = shieldDamageMultiplier2
					shouldPassThrough = shouldPassThrough2
					considerPiercing = considerPiercing2
					shouldDealAllFacetDamage = shouldDealAllFacetDamage2
					wasShieldChanged = wasShieldChanged2

			if wasShieldChanged <= 0:
				# normal shields, we generate a slight generic one-point drain
				shouldDealAllFacetDamage = 0
				# If no changes were made, default damage for ST shields
				shieldDamageMultiplier = PlasmaGenericShieldDamageMultiplier # nullify shield effects - that is, is immune
				mod = pTorp.GetModuleName()
				importedTorpInfo = __import__(mod)
				if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
					shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()
			
			shieldDamageMultiplier = shieldDamageMultiplier - PlasmaGenericShieldDamageMultiplier # That is, to compensate the "extra" time we added 1 damage
	
			finalShieldDamage = fDamage * shieldDamageMultiplier

			# Ok first we look for the nearest shield to the impact, drain the shields accordingly, and evaluate if the shield is broken
			shieldBroken = 0
			if shieldDamageMultiplier != 0:
				shieldBroken = self.shieldRecalculationAndBroken(pShip, kPoint, -finalShieldDamage, 0.25, shouldDealAllFacetDamage)
			if considerPiercing > 0 and shouldPassThrough <= 0:
				shouldPassThrough = shieldBroken
			
			if shouldPassThrough > 0 and shieldDamageMultiplier > 0: # If this weapon has not hit the hull already and meets the requirements, this weapon will "bypass" the shields then (actually it creates a short-lived clone or subTorp clone after the shield)
				global SlowDownRatio

				mod = pTorp.GetModuleName()
				if(self.__dict__.has_key("SubTorp")):
					mod = self.SubTorp

				launchSpeed = __import__(mod).GetLaunchSpeed()
				considerspeeddebuff = launchSpeed/(1.0 * pShip.GetRadius())
				shipNeeded = None
				theHitPoint = pHitPoint
				if considerspeeddebuff <= SlowDownRatio:
					NewScale =  considerspeeddebuff / (1000000.0 * SlowDownRatio)
					pVec.Scale((0.001 * NewScale))
					#launchSpeed = launchSpeed /  (100.0 * SlowDownRatio)
					shipNeeded = pShip
					theHitPoint = pTorp.GetWorldLocation()

				pHitPoint.Add(pVec)

				pTempTorp = FireTorpFromPointWithVectorAndNetType(theHitPoint, pVec, mod, pTorp.GetTargetID(), attackerID, launchSpeed, torpsNetTypeThatCanPhase, fDamage, pTorp.GetDamageRadiusFactor(), 0, shipNeeded)

				pTempTorp.SetLifetime(15.0)
				pTorp.SetLifetime(0.0)
				self.lFired.append(pTempTorp.GetObjID())
				pTempTorp.UpdateNodeOnly() 

		def AddTorpedo(self, path):
			FoundationTech.dYields[path] = self

	def ConvertPointNiToTG(point):
		retval = App.TGPoint3()
		retval.SetXYZ(point.x, point.y, point.z)
		return retval

	def IsInList(item, list):
		for i in list:
			if item == i:
				return 1
		return 0

	oSGPlasmaWeaponTorp = SGPlasmaWeaponTorpedo("SGPlasmaWeapon Torpedo")
	# Just a few standard torps I know of that are SGPlasmaWeapon... 

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"
	traceback.print_exc()

class SGPlasmaWeaponDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnProjectileDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		if oYield and hasattr(oYield, "IsSGPlasmaWeaponYield") and oYield.IsSGPlasmaWeaponYield() != 0 and pInstance and pInstance.__dict__.has_key('SG Plasma Weapon Immune') and pInstance.__dict__['SG Plasma Weapon Immune'] >= 2:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)
		pInstance.lPulseDefense.insert(self)


oSGPlasmaWeaponImmunity = SGPlasmaWeaponDef('SG Plasma Weapon Immune')