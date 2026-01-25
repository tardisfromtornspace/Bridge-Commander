#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         MEShields.py by Alex SL Gato
#         17th December 2024
#         Based on SGShields by Alex SL Gato, which was strongly based on Shields.py by the FoundationTechnologies team, ATPFunctions by Apollo, HelmMenuHandlers from the STBC Team, and MEGIonWeapon by Alex SL Gato.
#################################################################################################################
# === Introduction ===
# This technology encompasses most of ME shields in a generic way, mostly for tagging, but also for referencing common shield protection strengths and weaknesses over standard STBC shields.
# Here are the main differences regarding strengths and weaknesses of ME Shields (in comparision with STBC shields, which are supposed to be an in-game simplified version of early post-Dominion War ST Federation shielding):
# * POINT 1: ME Shields cannot block lasers, with the exception of Reaper shields, which can block them to an extent. Any form of radiation that does not have mass is at best only partially blocked, and at worst offer no protection so the hull must block it.
# * POINT 2: ME Shields are not triggered if a weapon moves too slowly in general.
# * POINT 3: ME Shields, excluding Cyclonic shields and similar, cannot block weapons that move too fast when using a Mass Effect field or similar (because the projectile gets additional mass), either.
# * POINT 4: Excluding the above, ME Shields can take a decent amount of Kinetic punishment, specially Reaper shields. Also they can resist a lot of gravity and space-time-distortion-related effects due to their Mass Effect, and have very little bleedthrough from kinetic-based impacts unless they are overwhelmed.
# * POINT 5: ME Shields could possibly overload against Plasma and Ion weaponry due to the electric charge affecting the ME Field emmiters.
# * POINT 6: Since ME Shields do not work like STBC shields, there would not be nothing in particular about Phased polaron Weapons that would make them phase through in any special way
# * POINT 7: ME vessels can alter gravity around them via Mass Effect fields.
# POINT 7 and partially POINT 4 can be covered by adding a Gravity Generator hardpoint property according to GravityFX. However, the rest need to be addressed in a more personal way, which is done either here, or on other scripts.

# === How to add this tech to a vessel:===
# just add to your Custom/Ships/shipFileName.py this, modifying the appropiate sub-fields.
# NOTE: replace "Ambassador" with the appropiate abbrev
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"ME Shields": { "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 1, "FacetRegeneration": 1, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": 150, "ShieldScaleMultiplier": 0.2, "AtmosphericNerf": -1, "IsHidden": 0},
}
"""
# The sub-fields are:
# * "CollisionBlock": if > 0, ME Shields on this vessel will block collision damage and use the shields first - by default it is 0 (disabled) because for most cases game-wise there is absolutely no difference between a regular ME shield stopping a huge ship and then the ship just colliding anyway at 0.0001 kmph, and the ship colliding as if no ME fields were there.
# * "BypassMultiplier": when a weapon bypasses your shields, how much actually gets through - this multiplies the value that the kind of weapon that would bypass your shield already had according to weapons configuration. Default is 1.0 because for most ME Shields, if a weapon can get pass through, then nothing of it is blocked (f.ex. GARDIAN lasers).
# * "FacetFactor": with a numeric value (f.ex. "FacetFactor" : 2), indicates how many times is the shield facet calculation multiplied when a too-low yield weapon is fired at them, so the shield will regenerate as if no weapon had been fired. This is for certain shields that could potentially shrug off lower-yields no matter the number. Default is 0 (disabled).
# * "FacetRegeneration": with a numeric value, indicates how many times it regenerates the damage when the FacetFactor condition is triggered. Default is 1 because normally there are no ME Shields which recover shield strength directly from impact.
# * "MinimumSpeedTrigger": with a numeric factor, indicates if a projectile weapon has to pass through if its speed is below a certain threshold. Default is 5. (that is, projectile speed 5 on the projectile file). Below this speed the bypass is full. A value below 0 means there's no lower threshold.
# * "MaximumSpeedTrigger": with a numeric factor, indicates if a projectile weapon has to pass through if its speed is above a certain threshold. Default is 260. (that is, projectile speed 100 on the projectile file). Above that threshold, damage will begin to pass through. A value below 0 means there's no upper threshold, unless the shield emmiter is damaged beyond its disabledPercentage + 0.1, when it will actually use the absolute value of the negative number as max speed threshold.
# * "AtmosphericNerf": Default is -1 (no change). If set to 1, being too close to a planetary atmosphere will temporarily reduce the shields to 40%.
# * "ShieldScaleMultiplier": When a ship is hit by a projectile or beam that should partially or totally pass through the shield, a new auxiliar torpedo is generated, spawned approximately where its parent torpedo collided. This value merely exists as a way to deal with ships with strange shapes being hit by a weapon that bypasses their shields, to multiply the regular torp-spawn scaling so it is guaranteed that the bypassing projectile manages to get past the shield, but does not pass over the entire ship. A greater value will make it spawn further from the shield collision point while a smaller value will make it spawn closer to the area. Default is 1.0.
 # * "IsHidden": developer feature, if 1, makes the projectiles used for the above visible, to help people get where something's going wrong or needs some polish or scale adjust factor. Default is 0 (keep hidden).
# "RaceShieldTech": indicates the type of shield your vessel has - it is basically a fast-configuration option which will fill the previous values (when not added) with specific settings. Currently these options are stored inside scripts/Custom/Techs/MEShieldScripts, on one or another file. A Race might also deterine a ship's immunity towards some types of weapons as well, which is useful for when a ship is immune to one kind of wepaon but still vulnerable to others.
# if "RaceShieldTech" : "Common", then "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 0, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": 260, "AtmosphericNerf": -1
# if "RaceShieldTech" : "Cyclonic", then "CollisionBlock": 0, "BypassMultiplier": 1, "FacetFactor": 0, "FacetRegeneration": 0, "MinimumSpeedTrigger": 5, "MaximumSpeedTrigger": -260, "AtmosphericNerf": -1
# if "RaceShieldTech" : "Reaper", then "CollisionBlock": 2, "BypassMultiplier": 0.5, "FacetFactor": 3, "FacetRegeneration": 1, "MinimumSpeedTrigger": -1, "MaximumSpeedTrigger": -512, "AtmosphericNerf": -1
#
# === Basic global configuration ===
# Inside the list of Subscripts, located at scripts/Custom/Techs/MEShieldScripts, there's a particular file , "BasicMEShieldsConfiguration", which allows to modify some global parameters of the script without modifying the main file itself, thus bringing less problems of multiple variants of the main file. Below is an example with all parameters being in use.
'''
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file is only added as base configuration, so if we need to change these parameters, we don't have to modify the main file.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes

import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
defaultPassThroughDmgMult = 1.0 # For things that need to actually do bleedtrough... how much?

shieldGoodThreshold = 0.400001 # From this value downwards, ME special bleedthrough block will not work.
shieldPiercedThreshold = 0.2 #0.25 # Below this value shields are definetely pierced, so full bleedthrough!

SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us when a ship is too small, to prevent a torpedo from just teleporting to the other side

globalRegularShieldReduction = 0.5 # When it's a ME shield vs normal shield during a collision, we take reduced shield damage

RaceShieldTechGlobalConfig = {
	"Name": "Default",
	"CollisionBlock" : 0,
	"BypassMultiplier": 1,
	"FacetFactor": 0,
	"FacetRegeneration": 0,
	"MinimumSpeedTrigger": 5,
	"MaximumSpeedTrigger": 260,
	"AtmosphericNerf": -1,
}
'''
# Below there is an example for Reaper rapid-config option.
'''
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds the rapid-config-option "Cyclonic" race to ME Shields.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

RaceShieldTechGlobalConfig = {
	"Name": "Reaper",
	"CollisionBlock" : 2,
	"BypassMultiplier": 0.5,
	"FacetFactor": 3,
	"FacetRegeneration": 1,
	"MinimumSpeedTrigger": -1,
	"MaximumSpeedTrigger": -512,
	"AtmosphericNerf": -1,
}
'''
#
# === Weapons configuration towards POINT 1, POINT 2, POINT 3 and POINT 5 ===
#
# Additionally, a file on the scripts/Custom/Techs/MEShieldScripts folder can contain certain attributes to make a certain weapon bypass shields, relative to POINT 1. The internal use is explained on the following indented area, and a file example has been added below that to guide modders with altering, adding or removing behaviours of a beam.
	# vulnerableProjToMEShields: A Dict of torpedoes that normally cannot deal damage through shields to STBC shields at full, but which could deal at least some guaranteed bleedthrough to ME shields.
	# The dict is built from a list of scripts, each dict works with the following fields (with an example)
	# {"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}
	# "ProjectileName" refers to a certain projectile name that the projectile's name or sScript filename match or have a common string with, case-insenstitive.
	# "GuaranteedBleedthrough" indicates ther relative dmg through a shield the weapon will deal, according to a multiplier. 0.1 is the default
	# "WhitelistFilename": adds extra torpedo filenames that, if matched exactly (case-sensitive), will guarantee they are included and will ignore blacklists (this field is here if somebody wants to add a torpedo with that ProjectileName torpedo properties, but under a different name).
	# "BlacklistName": includes a list of projectile on-screen names that cannot apply to this. This one will be triggered if the torpedo names match or have that string of words, case-insenstitive.
	# "BlacklistFilename": includes a list of projectile filenames that if they match cannot be applied to this. This one does need to match the words exactly and is case-sensitive.
	# vulnerableBeamsToMEShields: A Dict of beams that normally cannot deal damage through shields to STBC shields, but which could deal at least some guaranteed bleedthrough to ME shields. I currently do not know of any in particular... hm, maybe lasers, but that would go into too many what-ifs, so no, I don't know of any and on the original install from this mod this dict field will be empty. However, I'm leaving this field open for expansion.
	# {"BeamName": {"GuaranteedBleedthrough": 0.1, "WhitelistHardname": ["Quantum", "Quantum Torpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"]}
	# "BeamName" refers to a certain App phaser bank property (that is what they are called mod-wise, to the player they could have any varied names: beams, lasers, phasers, particle beams, etc.) name that the hardpoint's name match or have a common string with, case-insenstitive.
	# "GuaranteedBleedthrough" indicates ther relative dmg through a shield the weapon will deal, according to a multiplier. 0.1 is the default
	# "WhitelistHardname": adds extra hardpoint names that, if matched exactly (case-sensitive), will guarantee they are included and will ignore blacklists (this field is here if somebody wants to add a phaser bank property with that BeamName properties, but under a different name).
	# "BlacklistName": includes a list of hardpoint property names that cannot apply to this. This one will be triggered if the hardpoint names match or have that string of words, case-insenstitive.
	# "ProjRacesImmune": is a way to nullify bleedthrough of one type of weapon without setting the BypassMultiplier to 0, which would nullify other types of bleedthrough. It would be composed of a list of ME Shield races which would be immune to bleedthrough.

'''
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 17th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGShields Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGShieldScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file adds Quantum torpedoes to the list of guaranteed bleedthrough to SG Shields, according to SGShields in-script documentation. Due to the parent script implementation, we could add multiple files that add elements, and repeated elements on the lists will not be repeatedly included on the parent script

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
# On this case, we want to add the equivalent to this:
#{"ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}

ProjectileName = "laser"
ProjectileGuaranteedBleedthrough = 1.0
ProjectileWhitelistFilename = ["Laser", "LaserBeam"]  # Case-sensitive
ProjectileBlacklistName = ["not a laser", " not laser", " no laser", " anti-laser", "antilaser", "milaser"]  # Case-insensitive
ProjectileBlacklistFilename = ["AntiLaser", "NotALaser", "Turbolaser", "TurboLaser"]  # Case-sensitive
#ProjRacesImmune = ["Reaper"]

# Below here we have an example for beams
# {"BeamName": {"GuaranteedBleedthrough": 0.05, "WhitelistHardname": ["Ventral Phaser 1"], "BlacklistName": ["not a phaser", "notphaser", "laser", "nophaser"]}
BeamName = "laser"
BeamGuaranteedBleedthrough = 1.0
BeamWhitelistHardname = ["GARDIAN Laser 1", "GARDIAN Laser 2", "Laser Beam", "Laser beam"]
BeamBlacklistName = ["not a laser", "notlaser", "antilaser", "nolaser", "turbolaser", "turbo-laser"]
#BeamRacesImmune = ["Reaper"]
'''


from bcdebug import debug
import traceback

import App
import FoundationTech

from ftb.Tech.ATPFunctions import *

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.2",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

NonSerializedObjects = (
"oMEShields",
)
try:
	import Foundation
	import FoundationTech
	import MissionLib
	import Multiplayer.SpeciesToTorp

	from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

	import nt
	import string

	from ftb.Tech.ATPFunctions import *
	from math import *

	g_pAtmosCollisionCheckProcess = None
	torpsNetTypeThatCanPhase = Multiplayer.SpeciesToTorp.PHASEDPLASMA # For the "torpedoes-going-through" issue
	defaultDummyNothing = "NaN"
	SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side
	torpCountersForInstance = 32 # Auxiliar value to fake a pEvent, for new collisions

	shieldPiercedThreshold = 0.25 # If that shield is below this percentage, then the shield is considered pierced
	shieldGoodThreshold = 0.400001 # if that shield is above or equal this percentage, then the shield is considered to be in good condition
	defaultPassThroughDmgMult = 0.1 # How much damage from a dimensional projectile that STBC shields can easily resist, but ME shields cannot block?

	# Used for storing file entries

	vulnerableProjToMEShields = {}
	vulnerableBeamsToMEShields = {}

	# "similarTechsNames" is a dict of technologies which can react to MEShields shield collision simulation. While I cannot immediately think of one in particular, this allows expansion without editing this file
	# Structure would go like this, where "techName" is the name of the technology, and "multiplier" is a numeric value that increases or decreases the damage MEShields would receive
	# similarTechsNames = {"techName": multiplier}
	similarTechsNames = {}

	# So we can globally customize the Global configs without needing to modify the files
	raceShieldGlobalConfigs = {}

	# Something for race names, just in case a ship's shield race does not exist.
	gdefaultRaceName = "Default"
	
	# For regular shields against collisions
	globalRegularShieldReduction = 0.5

	# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
	def NiPoint3ToTGPoint3(p, factor=1.0):
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x * factor, p.y * factor, p.z * factor)
		return kPoint

	def TGPoint3ToNiPoint3(p, factor=1.0):
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
		import string
		global vulnerableProjToMEShields, vulnerableBeamsToMEShields, defaultDummyNothing

		dir="scripts\\Custom\\Techs\\MEShieldsScripts" # I want to limit any vulnerability as much as I can while keeping functionality

		try:
			list = nt.listdir(dir)
			if not list:
				print "ERROR: Missing scripts/Custom/Techs/MEShieldsScripts folder for MEShields technology"
				return

		except:
			print "ERROR: Missing scripts/Custom/Techs/MEShieldsScripts folder for MEShields technology, or other error:"
			traceback.print_exc()
			return		

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
				#print "MEShields script is reviewing " + fileName + " of dir " + dir
				if dExcludePlugins.has_key(fileName):
					debug(__name__ + ": Ignoring plugin" + fileName)
					continue

				try:
					if not filesChecked.has_key(fileName):
						filesChecked[fileName] = 1
						myGoodPlugin = dotPrefix + fileName

						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["ProjectileName", "BeamName", "interactionHullBehaviour"])
						except:
							try:
								banana = __import__(myGoodPlugin, globals(), locals(), ["defaultPassThroughDmgMult", "shieldPiercedThreshold", "shieldGoodThreshold", "SlowDownRatio", "globalRegularShieldReduction"])
							except:
								banana = __import__(myGoodPlugin, globals(), locals())

						if hasattr(banana, "similarTechNames"):
							global similarTechsNames
							for item in banana.similarTechNames.keys():
								if not similarTechsNames.has_key(item):
									similarTechsNames[item] = banana.similarTechNames[item]

						if hasattr(banana, "ProjectileName") and banana.ProjectileName != "": # These will not be affected at all by the hull or shield effects, period
							projName = string.lower(banana.ProjectileName)
							if not vulnerableProjToMEShields.has_key(projName):
								vulnerableProjToMEShields[projName] = {}

							if not vulnerableProjToMEShields[projName].has_key("GuaranteedBleedthrough"):
								vulnerableProjToMEShields[projName]["GuaranteedBleedthrough"] = defaultDummyNothing

							if hasattr(banana, "ProjectileGuaranteedBleedthrough") and vulnerableProjToMEShields[projName]["GuaranteedBleedthrough"] == defaultDummyNothing:
								vulnerableProjToMEShields[projName]["GuaranteedBleedthrough"] = banana.ProjectileGuaranteedBleedthrough

							if not vulnerableProjToMEShields[projName].has_key("WhitelistFilename"):
								vulnerableProjToMEShields[projName]["WhitelistFilename"] = []

							if not vulnerableProjToMEShields[projName].has_key("BlacklistName"):
								vulnerableProjToMEShields[projName]["BlacklistName"] = []

							if not vulnerableProjToMEShields[projName].has_key("BlacklistFilename"):
								vulnerableProjToMEShields[projName]["BlacklistFilename"] = []

							if not vulnerableProjToMEShields[projName].has_key("RacesImmune"):
								vulnerableProjToMEShields[projName]["RacesImmune"] = []

							if hasattr(banana, "ProjectileWhitelistFilename"):
								for item in banana.ProjectileWhitelistFilename:
									if not item in vulnerableProjToMEShields[projName]["WhitelistFilename"]:
										vulnerableProjToMEShields[projName]["WhitelistFilename"].append(item)

							if hasattr(banana, "ProjectileBlacklistFilename"):
								for item in banana.ProjectileBlacklistFilename:
									if not item in vulnerableProjToMEShields[projName]["BlacklistFilename"]:
										vulnerableProjToMEShields[projName]["BlacklistFilename"].append(item)

							if hasattr(banana, "ProjectileBlacklistName"):
								for item in banana.ProjectileBlacklistName:
									itemlower = string.lower(item)
									if not itemlower in vulnerableProjToMEShields[projName]["BlacklistName"]:
										vulnerableProjToMEShields[projName]["BlacklistName"].append(itemlower)

							if hasattr(banana, "ProjRacesImmune"):
								for item in banana.ProjRacesImmune:
									if not item in vulnerableProjToMEShields[projName]["RacesImmune"]:
										vulnerableProjToMEShields[projName]["RacesImmune"].append(item)

						if hasattr(banana, "BeamName") and banana.BeamName != "": # These will not be affected at all by the hull or shield effects, period

							projName = string.lower(banana.BeamName)
							if not vulnerableBeamsToMEShields.has_key(projName):
								vulnerableBeamsToMEShields[projName] = {}

							if not vulnerableBeamsToMEShields[projName].has_key("GuaranteedBleedthrough"):
								vulnerableBeamsToMEShields[projName]["GuaranteedBleedthrough"] = defaultDummyNothing

							if hasattr(banana, "BeamGuaranteedBleedthrough") and vulnerableBeamsToMEShields[projName]["GuaranteedBleedthrough"] == defaultDummyNothing:
								vulnerableBeamsToMEShields[projName]["GuaranteedBleedthrough"] = banana.BeamGuaranteedBleedthrough

							if not vulnerableBeamsToMEShields[projName].has_key("WhitelistHardname"):
								vulnerableBeamsToMEShields[projName]["WhitelistHardname"] = []

							if not vulnerableBeamsToMEShields[projName].has_key("BlacklistName"):
								vulnerableBeamsToMEShields[projName]["BlacklistName"] = []

							if not vulnerableBeamsToMEShields[projName].has_key("RacesImmune"):
								vulnerableBeamsToMEShields[projName]["RacesImmune"] = []

							if hasattr(banana, "BeamWhitelistHardname"):
								for item in banana.BeamWhitelistHardname:
									if not item in vulnerableBeamsToMEShields[projName]["WhitelistHardname"]:
										vulnerableBeamsToMEShields[projName]["WhitelistHardname"].append(item)

							if hasattr(banana, "BeamBlacklistName"):
								for item in banana.BeamBlacklistName:
									itemlower = string.lower(item)
									if not itemlower in vulnerableBeamsToMEShields[projName]["BlacklistName"]:
										vulnerableBeamsToMEShields[projName]["BlacklistName"].append(itemlower)

							if hasattr(banana, "BeamRacesImmune"):
								for item in banana.BeamRacesImmune:
									if not item in vulnerableBeamsToMEShields[projName]["RacesImmune"]:
										vulnerableBeamsToMEShields[projName]["RacesImmune"].append(item)

						if fileName == "BasicMEShieldsConfiguration":
							if hasattr(banana, "defaultPassThroughDmgMult"):
								global defaultPassThroughDmgMult
								defaultPassThroughDmgMult = banana.defaultPassThroughDmgMult

							if hasattr(banana, "shieldPiercedThreshold"):
								global shieldPiercedThreshold
								shieldPiercedThreshold = banana.shieldPiercedThreshold

							if hasattr(banana, "shieldGoodThreshold"):
								global shieldGoodThreshold
								shieldGoodThreshold = banana.shieldGoodThreshold

							if hasattr(banana, "SlowDownRatio"):
								global SlowDownRatio
								SlowDownRatio = banana.SlowDownRatio

							if hasattr(banana, "globalRegularShieldReduction"):
								global globalRegularShieldReduction
								globalRegularShieldReduction = banana.globalRegularShieldReduction

						if hasattr(banana, "RaceShieldTechGlobalConfig"):
							global raceShieldGlobalConfigs
							shieldConfig = banana.RaceShieldTechGlobalConfig
							if shieldConfig.has_key("Name"):
								shieldName = shieldConfig["Name"]
								if not shieldName in raceShieldGlobalConfigs.keys():
									raceShieldGlobalConfigs[shieldName] = shieldConfig
				except:
					print "someone attempted to add more than they should to the ME Shields script"
					traceback.print_exc()

	LoadExtraLimitedPlugins()

	# called when a ship changes Power of one of its subsystems
	# cause this is possibly also an alert event
	def SubsystemStateChanged(pObject, pEvent):
		debug(__name__ + ", SubsystemStateChanged")

		if pObject == None:
			return

		pShipID = pObject.GetObjID()
		pShip = App.ShipClass_GetObjectByID(None, pShipID)
		if not pShip:
			return

		if pEvent == None:
			pObject.CallNextHandler(pEvent)
			return

		pSubsystem = pEvent.GetSource()

		if not pSubsystem:
			pObject.CallNextHandler(pEvent)
			return

		if pSubsystem.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
			wpnActiveState = 0
			if hasattr(pEvent, "GetBool"):
				wpnActiveState = pEvent.GetBool()
				pShields = pShip.GetShields()
				if pShields:
					pInstance = findShipInstance(pShip)
					if pInstance:
						instanceDict = pInstance.__dict__
						raceShieldTech = 0
						# Extra shield config things
						if instanceDict.has_key("ME Shields"):
							if instanceDict["ME Shields"].has_key("CollisionBlock"):
								raceShieldTech = instanceDict["ME Shields"]["CollisionBlock"]

						if instanceDict.has_key("ME Shields Active"):
							if wpnActiveState != instanceDict["ME Shields Active"] and raceShieldTech != 0: # Means shields have changed
								if wpnActiveState == 0: # Shields have been deactivated:
									ActivateMEShieldCollisions(pShip, pInstance, instanceDict, 0, raceShieldTech, pShields)

								else: # Shields have been activated
									if not (pShields.IsDisabled() or not pShields.IsOn() or pShields.GetPowerPercentageWanted() <= 0.0): # A last check
										ActivateMEShieldCollisions(pShip, pInstance, instanceDict, 1, raceShieldTech, pShields)
									else:
										ActivateMEShieldCollisions(pShip, pInstance, instanceDict, 0, raceShieldTech, pShields)
				else:
					ActivateMEShieldCollisions(pShip, pInstance, instanceDict, 0, 0, None)

	class weDidThisPair: # This is not a lock, not by far - in-game many things are taken sequentially, with one interlacing the other, including a collision call, where pShipA-pShipB collision message are followed by but hopefully this will prevent some issues
		def __init__(self):
			debug(__name__ + ", __init__")
			self.shipPairs = {}

		def EnterPair(self, pShipID1, pShipID2): # On one call, it will be pShipID1-pShipID2, so on the other one it must be checked the other way around pShipID2-pShipID1
			if pShipID1 == App.NULL_ID or pShipID2 == App.NULL_ID:
				return -1 # ERROR HOW CAN YOU COLLIDE WITH THE NULL
			s = [str(pShipID1), str(pShipID2)]
			madeString = string.join(s[:], "-")
			if self.shipPairs.has_key(madeString):
				return 0 # cannot enter
			else:
				self.shipPairs[madeString] = 1
				return 1 # can enter

		def ExitPair(self, pShipID1, pShipID2): # On one call, it will be pShipID1-pShipID2, so on the other one it must be checked the other way around pShipID2-pShipID1
			s = [str(pShipID1), str(pShipID2)]
			madeString = string.join(s[:], "-")
			if self.shipPairs.has_key(madeString):
				del self.shipPairs[madeString]
				return 1
			else:
				self.shipPairs[madeString]
				return 0 # ERROR THAT ONE DID NOT EXIST

		def CheckPair(self, pShipID1, pShipID2): # On one call, it will be pShipID1-pShipID2, so on the other one it must be checked first the other way around pShipID2-pShipID1
			s = [str(pShipID1), str(pShipID2)]
			madeString = string.join(s[:], "-")
			if self.shipPairs.has_key(madeString):
				return 1 # We have that string here already
			else:
				return 0 # We don't have it

		def CheckAndDeleteOne(self, pShipID): # Cleanup issues
			vee = {}
			for stringbean in self.shipPairs.keys():
				vee[stringbean] = self.shipPairs[stringbean]
			for stringbean in vee.keys():
				s = string.split(stringbean, "-")
				for mush in s:
					if mush != None and mush != App.NULL_ID and int(mush) == pShipID:
						try:
							del self.shipPairs[stringbean]
						except:
							print "What in the blazes, a ship colliding with itself"
							traceback.print_exc()

	weDidThisVerify = weDidThisPair()

	def damageCalc(fTorpDamage, fShieldDamage, myShieldBroken, othersShieldBroken, myHull, otherHull, myShieldDirNearest, othersShieldDirNearest, pOtherShields, pMeShields, IhaveMEShields, OtherHasMEShields, pinstanceMeShieldRace, pinstanceOtherShieldRace, dummyDamage, massToMassRelation, otherHasSimilarShields, multiplierMyShieldFactor): # massToMassRelation needs tobe the inverse for the other

		global globalRegularShieldReduction
		negateRegeneration = 0
		multFactor = 1.0
		if myShieldBroken: # My shield will not protect - now we choose the damage for the torpedo
			if othersShieldBroken and otherHull:
				fTorpDamage = fTorpDamage + otherHull.GetCondition()
			elif pOtherShields and othersShieldDirNearest != None: # If they have still some shield strength and they have not fallen, add it to the damage
				fTorpDamage = fTorpDamage + pOtherShields.GetCurShields(othersShieldDirNearest)
				fShieldDamage = fShieldDamage + pOtherShields.GetCurShields(othersShieldDirNearest)

			fTorpDamage = fTorpDamage * massToMassRelation

		else: # My shield protects, now to choose the damage to the shield facet
			#print "my shield resists"
			if othersShieldBroken:
				#print "the other is broken"
				if otherHull:
					# then we add the hull
					fShieldDamage = fShieldDamage + otherHull.GetCondition()
				else:
					#print "Dummy hull damage"
					fShieldDamage = fShieldDamage + dummyDamage * 10
			else:
				#print "the other resists too", pOtherShields, othersShieldDirNearest
				if pOtherShields and othersShieldDirNearest != None: # If they have still some shield strength, add it to the damage
					fShieldDamage = fShieldDamage + pOtherShields.GetCurShields(othersShieldDirNearest)
				else:
					#print "Dummy shield damage"
					fShieldDamage = fShieldDamage + dummyDamage * 10

			fShieldDamage = fShieldDamage * massToMassRelation

			if OtherHasMEShields <= 0 and otherHasSimilarShields <= 0:
				fShieldDamage = fShieldDamage * globalRegularShieldReduction

			else:
				if otherHasSimilarShields > 0:
					fShieldDamage = fShieldDamage * multiplierMyShieldFactor
				else:
					fShieldDamage = fShieldDamage * globalRegularShieldReduction

		if not myShieldBroken and (pinstanceMeShieldRace != None and pinstanceMeShieldRace >= 1):
				fShieldDamage = fShieldDamage * 0.8
				negateRegeneration = -1
				multFactor = multFactor * pinstanceMeShieldRace

		#print "performing fShieldDamage ", fShieldDamage, " and torp dmg ", fTorpDamage
		return myShieldBroken, fTorpDamage, fShieldDamage, multFactor, negateRegeneration

	# "Fake" collision event. Same functions, quite a different inner implementation.
	import Appc
	class FakeWeaponHitEvent(App.TGEvent):
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
			return "<Python FakeWeaponHitEvent instance at %s>" % (self.this,)

	class FakeWeaponHitEventPtr(FakeWeaponHitEvent):
		def __init__(self,this):
			self.this = this
			self.thisown = 0
			self.__class__ = FakeWeaponHitEvent

	def TGFakeWeaponHitEvent_Create(*args, **kwargs):
		val = apply(Appc.TGEvent_Create,args,kwargs)
		if val:
			val = FakeWeaponHitEventPtr(val)
		return val


	def performFakeTorpEvents(pShip, pInstanceMe, pOtherShip, mod, theTorpDamage, myHull, myShieldBroken, myShieldBroken2, otherShipRadius, pShipNode, kPointW, kPoint, kPointpShipPer, kPointpShipPerNi, pShipPositionV):
				global torpCountersForInstance

				# First part, the torpedo, easy
				dmgRfactor = 0.01

				if myShieldBroken:
					dmgRfactor = otherShipRadius/5.0 #/10.0 

				leNetType = Multiplayer.SpeciesToTorp.DISRUPTOR
				if myShieldBroken:
					leNetType = Multiplayer.SpeciesToTorp.PHASEDPLASMA

				pTorp1 = App.Torpedo_Create(mod, kPoint)

				pTorp1.SetDamageRadiusFactor(dmgRfactor)
				pTorp1.SetDamage(theTorpDamage)
				pTorp1.SetNetType(leNetType)
				pTorp1.UpdateNodeOnly()

				# Set up its target and target subsystem, if necessary.
				pTorp1.SetTarget(pShip.GetObjID())
				pTorp1.SetParent(pOtherShip.GetObjID())
				pTorp1.SetTargetOffset(kPointpShipPer)
				pTorp1.UpdateNodeOnly()


				# Second part, the Event, harder. Down here is what we know about the Events that are given to the DefendVSTorp part of FoundationTech:
				# Basic App.TGEvent things:
				# 1º pEvent.GetSource(), pEvent.GetDestination() gives a C TGObject Instance, C TGEventHandlerObject
				# 2º pEvent.GetEventType() is always 8388708 (App.ET_WEAPON_HIT), for torpedo hits anyways
				# 3º pEvent.GetTimestamp(), pEvent.IsLogged(), pEvent.IsPrivate(), pEvent.IsNotSaved() will give -1.0 0 0 0
				# App.WeaponHitEvent things (they inherit the Basic App.TGEvent things by heritage)
				# 4º print pEvent.GetFiringObject(), " ", pEvent.GetTargetObject() ---> C ObjectClass Instance (pShip that fired), C ObjectClass Instance (pShip that got hit)
				# 5º print pEvent.GetObjectHitPoint(), pEvent.GetObjectHitNormal(), pEvent.GetWorldHitPoint(), pEvent.GetWorldHitNormal() ---> NiPoint3 Instances with same "at", but actually give two different results, position and normal vector, the two first on local coordinates and the two last being the same values but translated for World coordinates.
				# 6º self.this may give us hints, probably their ID or a memory allocation designation as they change between events of the same type
				# 7º print "cond: ", pEvent.GetCondition(), " wpnInstID: ", pEvent.GetWeaponInstanceID(), " rad: ", pEvent.GetRadius(), " dmg ", pEvent.GetDamage(), "wpnType: ", pEvent.GetWeaponType(), " hullHit: ", pEvent.IsHullHit(), " gfplayID: ", pEvent.GetFiringPlayerID()
				# When a player fired it once, it gave 0.9897142 (it is the condition of the shield or hull property), 32 (goes +1 after each event, maybe more if the hull was hit), 0.150000 (stays the same unless hull is hit, then it deals a lesser value, but closer to the original the worse the shields are... so with shields collapsed it should be the same), 144 (the damage), 1 (pEvent.TORPEDO), 0 (1 if hull was hit), 0 (no matter if the player or an AI are firing, at least on Single Player QB).

				# Thus, the Event needs to imitate those values according to what we have. Since App.WeaponHitEvent lacks visible setters for us, and the actual information for some of those parameters cannot be modified, we need to create a class inheriting from App.WeaponHitEvent but with most functions overriden to give the fake resutls we want, and overriding the __del__ method so we can clean those additional fields if necessary.
			
				pEvent1 = TGFakeWeaponHitEvent_Create() # This gives us a pointer, it has no arguments, but it is our "fake" event

				pEventSource = pTorp1
				pEventDestination = pShip

				pEvent1.SetSource(pEventSource)
				pEvent1.SetDestination(pEventDestination)
				pEvent1.SetEventType(App.ET_WEAPON_HIT)

				#pTorpAux = App.Torpedo_Cast(pEvent1.GetSource())
				#print pTorpAux.GetModuleName()
				
				pEvent1.SetFiringObject(pOtherShip)
				pEvent1.SetTargetObject(pShip)

				pEvent1.SetObjectHitPoint(kPointpShipPerNi)
				pShipPositionVI = TGPoint3ToNiPoint3(pShipPositionV, -1.0)
				pEvent1.SetObjectHitNormal(pShipPositionVI) 
				pEvent1.SetWorldHitPoint(kPointW)
				pShipPositionVW = TGPoint3ToNiPoint3(App.TGModelUtils_LocalToWorldUnitVector(pShipNode, pShipPositionVI), 1.0)
				pEvent1.SetWorldHitNormal(pShipPositionVW)
				
				eCondition = 1.0
				if myHull:
					eCondition = myHull.GetConditionPercentage()
				pEvent1.SetCondition(eCondition)

				valPlus = torpCountersForInstance + 1

				pEvent1.SetWeaponInstanceID(valPlus) # Not needed... at least, I am not aware of any scripts handling it for torpedo defense

				pEvent1.SetRadius(dmgRfactor)
				pEvent1.SetDamage(theTorpDamage)
				pEvent1.SetHullHit(1)
				pEvent1.SetFiringPlayerID(0)

				#print pEvent1

				# Third part, manual damage - actually quite easy
				affectedSys, nonTargetSys = FindAllAffectedSystems(pShip, kPointpShipPer, dmgRfactor, pEvent1)
				AdjustListedSubsystems(pShip, affectedSys, nonTargetSys, -theTorpDamage, 1.0, 1)

				# Fourth part, finally using the pEvent for something! This is also so more armours can work with these collisions, and not only one or two.
				pInstanceMe.DefendVSTorp(pShip, pEvent1, pTorp1)

				# While this below works, it has been deactivated. Why? Well, first it does not make that much of a difference. Second, the Ori Warship from stargate pack 3.0 already has a model issue where visual damage might crash the game, so let's not add something that makes little difference
				#if pShip.IsDead() or pShip.IsDying():
				#	pSet = pShip.GetContainingSet()
				#	if pSet:
				#		if theTorpDamage < 0.1:
				#			pTorp1.SetDamage(6000.0)
				#		pTorp1.SetTargetOffset(myHull.GetPosition())
				#		#pTorp1.SetHidden(1)
				#		pTorp1.UpdateNodeOnly()
				#		# If there was a target, then orient the torpedo towards it.
				#		kTorpLocation = pTorp1.GetWorldLocation()
				#		kTargetLocation = pShip.GetWorldLocation()
				#		kTargetLocation.Subtract(kTorpLocation)
				#		kFwd = kTargetLocation
				#		kFwd.Unitize()
				#		kPerp = kFwd.Perpendicular()
				#		kPerp2 = App.TGPoint3()
				#		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)
				#		pTorp1.AlignToVectors(kFwd, kPerp2)
				#		pTorp1.UpdateNodeOnly()
				#		# Give the torpedo an appropriate speed.
				#		kSpeed = CopyVector(kTargetLocation)
				#		kSpeed.Unitize()
				#		kSpeed.Scale(300)
				#		pTorp1.SetVelocity(kSpeed)
				#		pTorp1.UpdateNodeOnly()

		
	def CollisionHappened(pObject, pEvent): # POINT 4. Future TO-DO maybe see what triggers a shield collision event?
		# On an ideal world we would enable and disable collisions damage. However, for some reason, Disabling collision damage permanently leaves it disabled, even if the "pShip.IsCollisionDamageDisabled()" says it is enabled

		#print pEvent.GetDamage() # Collision events funnily enough do not have dmg... at least if they don't have damage collisions on

		pInstanceMeDict = None
		pInstanceOtherDict = None

		pinstanceMeShieldRace = None
		pinstanceOtherShieldRace = None

		IhaveMEShields = 0
		OtherHasMEShields = 0

		IhaveMEShieldsButFailed = 0
		OtherhaveMEShieldsButFailed = 0
		pMeShields = None
		pOtherShields = None

		pTheOther = App.ShipClass_Cast(pEvent.GetSource())
		if not pTheOther:
			return
		pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
		#print ("For the ship: ", pObject.GetName(), "and other ", pTheOther.GetName(), end= '')

		pOtherShip = App.ShipClass_GetObjectByID(None, pTheOther.GetObjID())
		if not pOtherShip or not pShip:
			# I guess the other/I am something else - maybe an asteroid, debris, a ghost, or something - to be safe, return
			return

		#global weDidThisVerify
		#gandalf = weDidThisVerify.CheckPair(pObject.GetObjID(), pTheOther.GetObjID())

		#if gandalf == 1: # We have Gandalf here
		#	weDidThisVerify.ExitPair(pObject.GetObjID(), pTheOther.GetObjID())
		#	# YOU SHALL NOT PASS!
		#	#print "returning from ", pShip.GetName(), "'s turn"
		#	return

		if pShip.IsDead() or pShip.IsDying():
			return

		pInstanceMe = findShipInstance(pShip)
		if not pInstanceMe:
			return

		pInstanceOther = findShipInstance(pOtherShip)

		if pInstanceMe:
			pInstanceMeDict = pInstanceMe.__dict__

		if pInstanceOther:
			pInstanceOtherDict = pInstanceOther.__dict__	

		if pInstanceMe and pInstanceMeDict.has_key("ME Shields"):
			#print ("me have key", end= '')
			pMeShields = pShip.GetShields()

			if pInstanceMeDict["ME Shields"].has_key("CollisionBlock"):
				pinstanceMeShieldRace = pInstanceMeDict["ME Shields"]["CollisionBlock"]
			if pinstanceMeShieldRace != 0:
				if pMeShields:
					#pAuxShieldsProperty = pMeShields.GetProperty()
					maxShields = 0.0
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						fMax = pMeShields.GetMaxShields(shieldDir)
						maxShields = maxShields + fMax

					if maxShields > 0.0:
						IhaveMEShields = 1
						if pMeShields.IsDisabled() or not pMeShields.IsOn():
							IhaveMEShieldsButFailed = 1
			else:
				return

		if IhaveMEShields <= 0: # If I don't have them, why or how am I here?
			return

		if pInstanceOther and pInstanceOtherDict.has_key("ME Shields"):
			#print ("others have key", end= '')
			pOtherShields = pOtherShip.GetShields()
			#print("other shields work", end= '')
			if pInstanceOtherDict["ME Shields"].has_key("CollisionBlock"):
				pinstanceOtherShieldRace = pInstanceOtherDict["ME Shields"]["CollisionBlock"]
			if pinstanceOtherShieldRace != 0:
				if pOtherShields:
					maxShields = 0.0
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						fMax = pOtherShields.GetMaxShields(shieldDir)
						maxShields = maxShields + fMax

					if maxShields > 0.0:
						OtherHasMEShields = 1
						if pOtherShields.IsDisabled() or not pOtherShields.IsOn():
							OtherhaveMEShieldsButFailed = 1

		# Actual collision calculations:
		otherHasSimilarShields = 0
		multiplierMyShieldFactor = 1.0
		if pInstanceOther and pInstanceOtherDict:
			for techName in similarTechsNames.keys():
				if pInstanceOtherDict.has_key(techName):
					otherHasSimilarShields = otherHasSimilarShields + 1
					multiplierMyShieldFactor = multiplierMyShieldFactor * similarTechsNames[techName]

		meHasSimilarShields = 0
		multiplierOtherShieldFactor = 1.0
		if pInstanceMe and pInstanceMeDict:
			for techName in similarTechsNames.keys():
				if pInstanceMeDict.has_key(techName):
					meHasSimilarShields = meHasSimilarShields + 1
					multiplierOtherShieldFactor = multiplierOtherShieldFactor * similarTechsNames[techName]

		#print "It is ", pShip.GetName(), "'s turn"
		#if IhaveMEShields > 0 and (OtherHasMEShields > 0 or otherHasSimilarShields > 0):
		#	saruman = weDidThisVerify.EnterPair(pTheOther.GetObjID(), pObject.GetObjID()) # This means we were here first, so gandalf can control those who arrive late
		#	#if saruman <= 0:
		#	#	print "the hit was already done for one side but the other did not take it or clean it in time"
			
		global shieldPiercedThreshold, globalRegularShieldReduction

		massToMassRelation = 1.0
		myShipProperty = pShip.GetShipProperty()
		otherShipProperty = pOtherShip.GetShipProperty()

		dummyDamage = pEvent.GetCollisionForce()

		otherHull = pOtherShip.GetHull()
		myHull = pShip.GetHull()

		if myShipProperty and otherShipProperty:
			massToMassRelation = (otherShipProperty.GetMass() + 0.1) /(myShipProperty.GetMass() + 0.1)

		pShipPosition = pShip.GetWorldLocation()
		pOtherShipPosition = pOtherShip.GetWorldLocation()

		pShipNode = pShip.GetNiObject()
		pOtherShipNode = pOtherShip.GetNiObject()

		myShipRadius = pShip.GetRadius()
		otherShipRadius = pOtherShip.GetRadius()

		myShipSpd = pShip.GetVelocityTG()
		otherShipSpd = pOtherShip.GetVelocityTG()

		myShipSpd.Subtract(otherShipSpd)
		spdDif = myShipSpd.Length()

		minSt = 5.0
		if IhaveMEShields and pInstanceMeDict and pInstanceMeDict["ME Shields"].has_key("MinimumSpeedTrigger"):
			minSt = pInstanceMeDict["ME Shields"]["MinimumSpeedTrigger"]

		othermSt = -1.0
		if OtherHasMEShields and pInstanceOtherDict and pInstanceOtherDict["ME Shields"].has_key("MinimumSpeedTrigger"):
			othermSt = pInstanceOtherDict["ME Shields"]["MinimumSpeedTrigger"]

		meBypass = 0
		otherBypass = 0
		if spdDif <= minSt:
			meBypass = 1
		if spdDif <= othermSt:
			otherBypass = 1

		numCollisionPoints = pEvent.GetNumPoints()
		for i in range (pEvent.GetNumPoints()):
			kPointW = pEvent.GetPoint(i) # For use with the shields
			kPoint = NiPoint3ToTGPoint3(kPointW)

			pShipPositionV = pShip.GetWorldLocation()
			pShipPositionV.Subtract(kPoint) # For a torpedo that goes from THEIR ship to OURS

			pOtherShipPositionV = pOtherShip.GetWorldLocation()
			pOtherShipPositionV.Subtract(kPoint) # For a torpedo that goes from OUR ship to THEIRS

			kPointpShipPerNi = App.TGModelUtils_WorldToLocalPoint(pShipNode, kPointW)
			kPointpOtherShipPerNi = App.TGModelUtils_WorldToLocalPoint(pOtherShipNode, kPointW)

			kPointpShipPer = NiPoint3ToTGPoint3(kPointpShipPerNi, 0.01)
			kPointpOtherShipPer = NiPoint3ToTGPoint3(kPointpOtherShipPerNi, 0.01)

			myShieldBroken = 0
			othersShieldBroken = 0

			myShieldDirNearest = None
			othersShieldDirNearest = None
		
			fTorpDamage = 0.0
			fShieldDamage = 0.0
			fTorpDamage2 = 0.0
			fShieldDamage2 = 0.0

			myShieldBroken, myShieldDirNearest = shieldInGoodCondition(pShip, kPointpShipPer, shieldPiercedThreshold, 0, None)
			othersShieldBroken, othersShieldDirNearest = shieldInGoodCondition(pOtherShip, kPointpOtherShipPer, shieldPiercedThreshold, 0, None)

			changeMebyp = 0
			changeOtherbyp = 0
			if myShieldBroken < 1 and (OtherHasMEShields or (meBypass > 0 and othersShieldBroken < 1)): # Workaround of sorts for some solid projectiles
				changeMebyp = 1

			if othersShieldBroken < 1 and (IhaveMEShields or (otherBypass > 0 and myShieldBroken < 1)):
				changeOtherbyp = 1

			if changeMebyp > 0:
				myShieldBroken = meBypass

			if changeOtherbyp > 0:
				othersShieldBroken = otherBypass				

			myShieldBroken, fTorpDamageMe, fShieldDamageMe, multFactorMe, negateRegenerationMe = damageCalc(fTorpDamage, fShieldDamage, myShieldBroken, othersShieldBroken, myHull, otherHull, myShieldDirNearest, othersShieldDirNearest, pOtherShields, pMeShields, IhaveMEShields, OtherHasMEShields, pinstanceMeShieldRace, pinstanceOtherShieldRace, dummyDamage, massToMassRelation, otherHasSimilarShields, multiplierMyShieldFactor)

			#othersShieldBroken2 = 0
			#if OtherHasMEShields > 0 or otherHasSimilarShields > 0: # Hm, maybe it would be nice to make this happen regardless? 
			othersShieldBroken, fTorpDamageYou, fShieldDamageYou, multFactorYou, negateRegenerationYou = damageCalc(fTorpDamage2, fShieldDamage2, othersShieldBroken, myShieldBroken, otherHull, myHull, othersShieldDirNearest, myShieldDirNearest, pMeShields, pOtherShields, OtherHasMEShields, IhaveMEShields, pinstanceOtherShieldRace, pinstanceMeShieldRace, dummyDamage, (1.0/massToMassRelation), meHasSimilarShields, multiplierOtherShieldFactor)

			othersShieldBroken2, othersShieldDirNearest = shieldRecalculationAndBroken(pOtherShip, kPointpOtherShipPer, -fShieldDamageYou, shieldPiercedThreshold, 0, negateRegenerationYou, othersShieldDirNearest, -fShieldDamageYou, multFactorYou)
			myShieldBroken2, myShieldDirNearest = shieldRecalculationAndBroken(pShip, kPointpShipPer, -fShieldDamageMe, shieldPiercedThreshold, 0, negateRegenerationMe, myShieldDirNearest, fShieldDamageMe, multFactorMe)

			mod = "Tactical.Projectiles.ExtraCollisionDamageDummy" # ADD THIS TO YOUR MOD
			if (myShieldBroken or myShieldBroken2) and not (pShip.IsDead() or pShip.IsDying()):
				performFakeTorpEvents(pShip, pInstanceMe, pOtherShip, mod, fTorpDamageMe, myHull, myShieldBroken, myShieldBroken2, otherShipRadius, pShipNode, kPointW, kPoint, kPointpShipPer, kPointpShipPerNi, pShipPositionV)

			if (OtherHasMEShields > 0 or otherHasSimilarShields > 0) and (othersShieldBroken or othersShieldBroken2) and not (pOtherShip.IsDead() or pOtherShip.IsDying()):
				performFakeTorpEvents(pOtherShip, pInstanceOther, pOtherShip, mod, fTorpDamageYou, otherHull, othersShieldBroken, othersShieldBroken, myShipRadius, pOtherShipNode, kPointW, kPoint, kPointpOtherShipPer, kPointpOtherShipPerNi, pOtherShipPositionV)

	def ActivateMEShieldCollisions(pShip, pInstance, instanceDict, activate=1, raceShieldTech=0, pShields=None):
		if pShip.IsDead() or pShip.IsDying():
			return
		maxShields = 0.0
		if pShields:
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fMax = pShields.GetMaxShields(shieldDir)
				maxShields = maxShields + fMax
		if activate == 1 and raceShieldTech > 0 and maxShields > 0.0:
			#print "pShip to add collision shields: ", pShip.GetName()
			instanceDict["ME Shields Active"] = 1
			#if not pShip.IsCollisionDamageDisabled():
			pShip.DisableCollisionDamage(1)
			#pShip.DamageRefresh(1)
		else:
			instanceDict["ME Shields Active"] = 0
			if raceShieldTech > 0:
				#print "pShip to remove collision shields: "
				#if pShip.IsCollisionDamageDisabled():
				pShip.DisableCollisionDamage(0)
				pShip.SetCollisionsOn(0)
				pShip.SetCollisionsOn(1)
				#pShip.DamageRefresh(1)

		pShip.UpdateNodeOnly()

	# A Future TO-DO: if you finally find where the App.ET_PLANET_ATMOSPHERE_COLLISION is sent to and in what channels it is sent, and is less bothersome than having to add a listener to the planets, please, replace ProcessWrapper and CollisionAtmosAlertCheck for a listener on the ship or tech and def AtmosCollisionHappened
	#
	# ProcessWrapper from HelmMenuHandlers
	#
	# PythonMethodProcess objects can't be saved directly.  This allows them to be saved
	# and wraps the functionality we want in the constructor.
	class TempProcessWrapper:
		def __init__(self, sFunctionName, fDelay, ePriority):
			debug(__name__ + ", __init__")
			self.sFunctionName = sFunctionName
			self.fDelay = fDelay
			self.ePriority = ePriority
			self.pShips = {}

			self.SetupProcess()

		def __getstate__(self):
			debug(__name__ + ", __getstate__")
			dState = self.__dict__.copy()
			del dState["pProcess"]
			return dState

		def __setstate__(self, dict):
			debug(__name__ + ", __setstate__")
			self.__dict__ = dict
			self.SetupProcess()

		def SetupProcess(self):
			debug(__name__ + ", SetupProcess")
			self.pProcess = App.PythonMethodProcess()
			self.pProcess.SetInstance(self)
			self.pProcess.SetFunction("ProcessFunc")
			self.pProcess.SetDelay( self.fDelay )
			self.pProcess.SetPriority( self.ePriority )

		def ProcessFunc(self, dTimeAvailable):
			# Call our function.
			debug(__name__ + ", ProcessFunc")
			pFunc = globals()[self.sFunctionName]
			pFunc(dTimeAvailable)

		def AddShip(self, pShipID, pShip, pInstance):
			self.pShips[pShipID] = {"pShip": pShip, "pInstance": pInstance}

		def RemoveShip(self, pShipID):
			if self.pShips.has_key(pShipID):
			 del self.pShips[pShipID]

		def SendShipsOriginal(self):
			return self.pShips

		def UpdateAtmosReentry(self, pShipID, value):
			if self.pShips.has_key(pShipID):
				self.pShips[pShipID]["WasInside"] = value
				 
		def SendShipsCopy(self):
			auxiliar = {}
			for pShipID in self.pShips.keys():
				auxiliar[pShipID] = self.pShips[pShipID]
			return auxiliar
				

	def CollisionAtmosAlertCheck(dTimeLeft): 
		
		global g_pAtmosCollisionCheckProcess
		if not (g_pAtmosCollisionCheckProcess):
			g_pAtmosCollisionCheckProcess = TempProcessWrapper("CollisionAtmosAlertCheck", 5.0, App.TimeSliceProcess.LOW)
		shipList = g_pAtmosCollisionCheckProcess.SendShipsCopy()
		for pShipID in shipList.keys():
			doShieldNerf = 0
			pShip = App.ShipClass_GetObjectByID(None, pShipID)
			if pShip:
				fRadius = 4 * pShip.GetRadius() # More or less same formula for when being too close to a planet or a sun
				pShipPosition = pShip.GetWorldLocation()
				pSet = pShip.GetContainingSet()
				if pSet:
					pProxManager = pSet.GetProximityManager()
					if pProxManager:
						pIterator = pProxManager.GetNearObjects(pShipPosition, fRadius)
						if (pIterator):
							pObject = pProxManager.GetNextObject(pIterator)
							while (pObject != None):
								if (pObject and pObject.GetObjID() != pShipID):
									pPlanet = App.Planet_Cast(pObject)
									if (pPlanet):
										doShieldNerf = doShieldNerf + 1

								pObject = pProxManager.GetNextObject(pIterator)

						pProxManager.EndObjectIteration(pIterator)

				if doShieldNerf > 0:
					g_pAtmosCollisionCheckProcess.UpdateAtmosReentry(pShipID, 1)
					pShields = pShip.GetShields()
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)

						if fCurr > 0.4 * fMax:
							pShields.SetCurShields(shieldDir, 0.4 * fMax)

				else:
					if shipList[pShipID].has_key("WasInside") and shipList[pShipID]["WasInside"] == 1:
						g_pAtmosCollisionCheckProcess.UpdateAtmosReentry(pShipID, 0)

						pShields = pShip.GetShields()
						for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
							fCurr = pShields.GetCurShields(shieldDir)
							fMax = pShields.GetMaxShields(shieldDir)
							fFinal = fCurr / 0.4
							if fFinal > fMax:
								fFinal = fMax
	
							pShields.SetCurShields(shieldDir, fFinal)


			else: # This should have been cleaned up already - anyways we will be cleaning it here, just in case
				g_pAtmosCollisionCheckProcess.RemoveShip(pShipID)

	#def AtmosCollisionHappened(pObject, pEvent):
	#	print "Ok an atmos collision happened"
					
	#def PCollisionHappened(pObject, pEvent):
	#	print "Ok a planet collision happened"

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

	def shieldRecalculationAndBroken(pShip, kPoint, extraDamageHeal, shieldThreshold = shieldPiercedThreshold, multifacet = 0, negateRegeneration=0, nearShields = None, damageSuffered = 0, multFactor = 1.0):

		pShields = pShip.GetShields()
		shieldHitBroken = 0
		shieldDirNearest = None
		if pShields:
			if nearShields == None:
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


				if pReferenciado:
					shieldDirNearest = lReferencias.index(pReferenciado)
				else:
					shieldHitBroken = 1
			else:
				shieldDirNearest = nearShields

			if not (pShields.IsDisabled() or not pShields.IsOn()):
				pShieldsProperty = pShields.GetProperty()
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					if shieldDirNearest == shieldDir or multifacet != 0:
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						fRecharge = 0
						if pShieldsProperty and negateRegeneration != 0 and damageSuffered <= ( multFactor * pShieldsProperty.GetShieldChargePerSecond(shieldDir)):
							fRecharge = -negateRegeneration * damageSuffered * multFactor
							
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
		else:
			shieldHitBroken = 1

		return shieldHitBroken, shieldDirNearest

	def shieldInGoodCondition(pShip, kPoint, shieldThreshold = shieldPiercedThreshold, multifacet = 0, nearShields = None):

		pShields = pShip.GetShields()
		shieldHitBroken = 0
		shieldDirNearest = None
		if pShields:
			if nearShields == None:
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

				
				if pReferenciado:
					shieldDirNearest = lReferencias.index(pReferenciado)
				else:
					shieldHitBroken = shieldHitBroken + 1

			else:
				shieldDirNearest = nearShields

			if not (pShields.IsDisabled() or not pShields.IsOn()):
				pShieldsProperty = pShields.GetProperty()
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					if shieldDirNearest == shieldDir or multifacet != 0:
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						resultHeal = fCurr
						if (shieldDirNearest == shieldDir or multifacet == 2) and (fMax <= 0 or resultHeal < (shieldThreshold * fMax)):
							shieldHitBroken = shieldHitBroken + 1
			else:
				shieldHitBroken = 1
				

		else:
			shieldHitBroken = 1

		return shieldHitBroken, shieldDirNearest

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
	
	class MEShieldsDef(FoundationTech.TechDef):
		#ET_ORBIT_PLANET ... does it consider it too when you get too close but don't perform an orbit planet?
		#def __init__(self, name):
		#	debug(__name__ + ", Initiated AutomatedDestroyedSystemRepair counter")
		#	FoundationTech.TechDef.__init__(self, name)
		#	self.pEventHandler = App.TGPythonInstanceWrapper()
		#	self.pEventHandler.SetPyWrapper(self)
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_SHIELD_COLLISION, self.pEventHandler, "OneCol")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SHIELD_COLLISION, self.pEventHandler, "OneCol")
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_PLANET_ATMOSPHERE_COLLISION, self.pEventHandler, "AtmosCol")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PLANET_ATMOSPHERE_COLLISION, self.pEventHandler, "AtmosCol")
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_PLANET_COLLISION, self.pEventHandler, "PCol")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PLANET_COLLISION, self.pEventHandler, "PCol")
		#	App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_COLLISION, self.pEventHandler, "Col")
		#	App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_COLLISION, self.pEventHandler, "Col")

		# Future TO-DO if you can catch App.ET_SHIELD_COLLISION, it may be better for collisions being more like ME ones
		#def OneCol(self, pEvent):
		#	print "shield col event caught by broadcast"
		#	ShieldCollisionHappened(self, pEvent)

		#def AtmosCol(self, pEvent):
		#	print "atmos col event caught by broadcast"
		#	AtmosCollisionHappened(self, pEvent)

		#def PCol(self, pEvent):
		#	print "planet col event caught by broadcast"
		#	PCollisionHappened(self, pEvent)

		def AttachShip(self, pShip, pInstance):
			debug(__name__ + ", AttachShip")

			# Extra shield config things
			instanceDict = pInstance.__dict__
			if instanceDict.has_key("ME Shields"):
				race = None
				if instanceDict["ME Shields"].has_key("RaceShieldTech"):
					race = instanceDict["ME Shields"]["RaceShieldTech"]

				global raceShieldGlobalConfigs, gdefaultRaceName
				if race == None  or not race in raceShieldGlobalConfigs.keys():
					race = gdefaultRaceName

				if (not instanceDict["ME Shields"].has_key("CollisionBlock")):
					if raceShieldGlobalConfigs[race].has_key("CollisionBlock"):
						instanceDict["ME Shields"]["CollisionBlock"] = raceShieldGlobalConfigs[race]["CollisionBlock"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("CollisionBlock"):
						instanceDict["ME Shields"]["CollisionBlock"] = raceShieldGlobalConfigs[gdefaultRaceName]["CollisionBlock"]
						
				if (not instanceDict["ME Shields"].has_key("BypassMultiplier")):
					if raceShieldGlobalConfigs[race].has_key("BypassMultiplier"):
						instanceDict["ME Shields"]["BypassMultiplier"] = raceShieldGlobalConfigs[race]["BypassMultiplier"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("BypassMultiplier"):
						instanceDict["ME Shields"]["BypassMultiplier"] = raceShieldGlobalConfigs[gdefaultRaceName]["BypassMultiplier"]

				if (not instanceDict["ME Shields"].has_key("FacetFactor")):
					if raceShieldGlobalConfigs[race].has_key("FacetFactor"):
						instanceDict["ME Shields"]["FacetFactor"] = raceShieldGlobalConfigs[race]["FacetFactor"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("FacetFactor"):
						instanceDict["ME Shields"]["FacetFactor"] = raceShieldGlobalConfigs[gdefaultRaceName]["FacetFactor"]

				if (not instanceDict["ME Shields"].has_key("FacetRegeneration")):
					if raceShieldGlobalConfigs[race].has_key("FacetRegeneration"):
						instanceDict["ME Shields"]["FacetRegeneration"] = raceShieldGlobalConfigs[race]["FacetRegeneration"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("FacetRegeneration"):
						instanceDict["ME Shields"]["FacetRegeneration"] = raceShieldGlobalConfigs[gdefaultRaceName]["FacetRegeneration"]
					
				if (not instanceDict["ME Shields"].has_key("MinimumSpeedTrigger")):
					if raceShieldGlobalConfigs[race].has_key("MinimumSpeedTrigger"):
						instanceDict["ME Shields"]["MinimumSpeedTrigger"] = raceShieldGlobalConfigs[race]["MinimumSpeedTrigger"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("MinimumSpeedTrigger"):
						instanceDict["ME Shields"]["MinimumSpeedTrigger"] = raceShieldGlobalConfigs[gdefaultRaceName]["MinimumSpeedTrigger"]

				if (not instanceDict["ME Shields"].has_key("MaximumSpeedTrigger")):
					if raceShieldGlobalConfigs[race].has_key("MaximumSpeedTrigger"):
						instanceDict["ME Shields"]["MaximumSpeedTrigger"] = raceShieldGlobalConfigs[race]["MaximumSpeedTrigger"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("MaximumSpeedTrigger"):
						instanceDict["ME Shields"]["MaximumSpeedTrigger"] = raceShieldGlobalConfigs[gdefaultRaceName]["MaximumSpeedTrigger"]

				if (not instanceDict["ME Shields"].has_key("AtmosphericNerf")):
					if raceShieldGlobalConfigs[race].has_key("AtmosphericNerf"):
						instanceDict["ME Shields"]["AtmosphericNerf"] = raceShieldGlobalConfigs[race]["AtmosphericNerf"]
					elif raceShieldGlobalConfigs[gdefaultRaceName].has_key("AtmosphericNerf"):
						instanceDict["ME Shields"]["AtmosphericNerf"] = raceShieldGlobalConfigs[gdefaultRaceName]["AtmosphericNerf"]

				if instanceDict["ME Shields"]["AtmosphericNerf"] == 1:
				
					global g_pAtmosCollisionCheckProcess
					if not (g_pAtmosCollisionCheckProcess):
						g_pAtmosCollisionCheckProcess = TempProcessWrapper("CollisionAtmosAlertCheck", 5.0, App.TimeSliceProcess.LOW)
					g_pAtmosCollisionCheckProcess.AddShip(pShip.GetObjID(), pShip, pInstance)

				pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)

				if pShip != None:
					# Checking when we need to change the collision features
					pShields = pShip.GetShields()
					if pShields:
						maxShields = 0.0
						for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
							fMax = pShields.GetMaxShields(shieldDir)
							maxShields = maxShields + fMax
						if maxShields > 0.0:
							#print "Adding ME forcefield shield tech listeners to ship: ", pShip.GetName()
							pShields.TurnOn()
							instanceDict["ME Shields Active"] = 1
							pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
							pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")

							shieldBehaviour = 0
							if instanceDict["ME Shields"].has_key("CollisionBlock") and instanceDict["ME Shields"]["CollisionBlock"] != 0:
								shieldBehaviour = instanceDict["ME Shields"]["CollisionBlock"]
								if shieldBehaviour > 0:
									pShip.RemoveHandlerForInstance(App.ET_OBJECT_COLLISION, __name__ + ".CollisionHappened")
									pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_COLLISION, __name__ + ".CollisionHappened")

							#pShip.RemoveHandlerForInstance(App.ET_SHIELD_COLLISION, __name__ + ".ShieldCollisionHappened")
							#pShip.AddPythonFuncHandlerForInstance(App.ET_SHIELD_COLLISION, __name__ + ".ShieldCollisionHappened")

							#pShip.RemoveHandlerForInstance(App.ET_PLANET_ATMOSPHERE_COLLISION, __name__ + ".AtmosCollisionHappened")
							#pShip.AddPythonFuncHandlerForInstance(App.ET_PLANET_ATMOSPHERE_COLLISION, __name__ + ".AtmosCollisionHappened")

							#pShip.RemoveHandlerForInstance(App.ET_PLANET_COLLISION, __name__ + ".PCollisionHappened")
							#pShip.AddPythonFuncHandlerForInstance(App.ET_PLANET_COLLISION, __name__ + ".PCollisionHappened")


							ActivateMEShieldCollisions(pShip, pInstance, instanceDict, 1, shieldBehaviour, pShields)

		def DetachShip(self, pShipID, pInstance):
			if not pShipID and pInstance:
				pShipID = pInstance.pShipID

			if pShipID:
				global weDidThisVerify
				weDidThisVerify.CheckAndDeleteOne(pShipID)

			global g_pAtmosCollisionCheckProcess
			if (g_pAtmosCollisionCheckProcess):
				g_pAtmosCollisionCheckProcess.RemoveShip(pShipID)

			pShip = App.ShipClass_GetObjectByID(None, pShipID)
			if pShip != None:
				try:
					pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
					pShip.RemoveHandlerForInstance(App.ET_OBJECT_COLLISION, __name__ + ".CollisionHappened")
					#pShip.RemoveHandlerForInstance(App.ET_SHIELD_COLLISION, __name__ + ".ShieldCollisionHappened")
					#pShip.RemoveHandlerForInstance(App.ET_PLANET_ATMOSPHERE_COLLISION, __name__ + ".AtmosCollisionHappened")
					#pShip.RemoveHandlerForInstance(App.ET_PLANET_COLLISION, __name__ + ".PCollisionHappened")
				except:
					print "Error while removing Handlers for DetachShip:"
					traceback.print_exc()
			
			instanceDict = pInstance.__dict__
			if instanceDict.has_key("ME Shields Active"):
				del instanceDict["ME Shields Active"]
			

		def EventInformation(self, pEvent):
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

			return fRadius, fDamage, kPoint

		def OnDefense(self, pShip, pInstance, oYield, pEvent, pTorp=None):
			debug(__name__ + ", OnDefense")

			if not pShip:
				return

			pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
			if not pShip:
				return

			global shieldPiercedThreshold, shieldGoodThreshold, defaultPassThroughDmgMult, defaultDummyNothing, vulnerableProjToMEShields, vulnerableBeamsToMEShields, torpsNetTypeThatCanPhase

			instanceDict = pInstance.__dict__
			fRadius, fDamage, kPoint = self.EventInformation(pEvent)

			pShDmgForDS9FX = 0
			myShieldSubsys = None
			if pShip.GetShields() != None:
				myShieldSubsys = pShip.GetShields()
				pShDmgForDS9FX = (myShieldSubsys.GetShieldPercentage() < 0.2)
			raceShieldTech = None
			raceHullTech = None
			negateRegeneration = 0
			multFactor = 1.0

			collisionBlock = 0
			bypassMultiplier = 1.0
			sfacetFactor = 0.0
			sfacetRegen = 1.0
			sScaleFMult = 1.0
			minSt = 5.0
			maxSt = 260.0
			atmosNerf = -1
			isHidden = 1

			forcedBleedthrough = 0
			forcedBleedthroughMultiplier = 0

			attackerID = App.NULL_ID

			pVec = None
			theHitPoint = None
			theOffset = None

			# Extra shield config things
			if instanceDict.has_key("ME Shields"):
				if instanceDict["ME Shields"].has_key("RaceShieldTech"):
					raceShieldTech = instanceDict["ME Shields"]["RaceShieldTech"]

				if instanceDict["ME Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity and to not add too many fields.
					raceHullTech = instanceDict["ME Shields"]["RaceHullTech"]
				else:
					raceHullTech = raceShieldTech

				if instanceDict["ME Shields"].has_key("CollisionBlock"):
					collisionBlock = instanceDict["ME Shields"]["CollisionBlock"]
				if instanceDict["ME Shields"].has_key("BypassMultiplier"):
					bypassMultiplier = instanceDict["ME Shields"]["BypassMultiplier"]
				if instanceDict["ME Shields"].has_key("FacetFactor"):
					sfacetFactor = instanceDict["ME Shields"]["FacetFactor"]
				if instanceDict["ME Shields"].has_key("FacetRegeneration"):
					sfacetRegen = instanceDict["ME Shields"]["FacetRegeneration"]
				if instanceDict["ME Shields"].has_key("MinimumSpeedTrigger"):
					minSt = instanceDict["ME Shields"]["MinimumSpeedTrigger"]
				if instanceDict["ME Shields"].has_key("MaximumSpeedTrigger"):
					maxSt = instanceDict["ME Shields"]["MaximumSpeedTrigger"]
				if instanceDict["ME Shields"].has_key("AtmosphericNerf"):
					atmosNerf = instanceDict["ME Shields"]["AtmosphericNerf"]
				if instanceDict["ME Shields"].has_key("ShieldScaleMultiplier"):
					sScaleFMult = instanceDict["ME Shields"]["ShieldScaleMultiplier"]
				if instanceDict["ME Shields"].has_key("IsHidden"):
					isHidden = instanceDict["ME Shields"]["IsHidden"]	

			if pTorp:
				attackerID = pTorp.GetParentID()
				mod = pTorp.GetModuleName()
				pVec = pTorp.GetVelocityTG()
				pVec.Scale(0.01)

				if mod:
					weaponFileName = string.split(mod, ".")[-1]
					importedMod = __import__(mod)
					
					if hasattr(importedMod, "GetLaunchSpeed"):
						try:
							weaponSpeed = importedMod.GetLaunchSpeed()
							if weaponSpeed <= minSt:
								forcedBleedthrough = 1
								forcedBleedthroughMultiplier = 1.0
								sfacetFactor = fDamage * 2
								sfacetRegen = 1.0	
								if fDamage > 0.0:
									negateRegeneration = -1

							else:
								if myShieldSubsys != None:
									cdnPerc = myShieldSubsys.GetCombinedConditionPercentage()
									disabledPerc = myShieldSubsys.GetDisabledPercentage()
									maxSpeed = maxSt
									if disabledPerc + 0.1 > cdnPerc:
										maxSpeed = abs(maxSpeed)

									if maxSpeed >= 0 and weaponSpeed >= maxSpeed:
										forcedBleedthrough = 1
										forcedBleedthroughMultiplier = 1.0
						except:
							forcedBleedthroughMultiplier =  0
							forcedBleedthrough = 0
							traceback.print_exc()
							
					if forcedBleedthrough == 0 and hasattr(importedMod, "GetName"):
						
						weaponName = importedMod.GetName()
						weaponname = string.lower(weaponName)

						for key in vulnerableProjToMEShields.keys():
							racesImmune = vulnerableProjToMEShields[key]["RacesImmune"]
							if raceShieldTech in racesImmune or (("Cyclonic" in racesImmune or "Reaper" in racesImmune) and maxSt < 0.0):
								continue
							foundThis = 0
							isinWhitelistFilename =  0
							if weaponFileName in vulnerableProjToMEShields[key]["WhitelistFilename"]:
								isinWhitelistFilename =  1
							isinBlacklistFilename = 0
							isinBlacklistname = 0
							if not isinWhitelistFilename:
								foundThis = string.find(weaponname, key) + 1
								isinBlacklistFilename = (weaponFileName in vulnerableProjToMEShields[key]["BlacklistFilename"])

								if not isinBlacklistFilename:
									for item in vulnerableProjToMEShields[key]["BlacklistName"]:
										isinBlacklistname = string.find(weaponname, item) + 1
										if isinBlacklistname:
											break

							if isinWhitelistFilename > 0 or (foundThis > 0 and not (isinBlacklistFilename > 0 or isinBlacklistname > 0)):
								if not vulnerableProjToMEShields[key].has_key("GuaranteedBleedthrough") or vulnerableProjToMEShields[key]["GuaranteedBleedthrough"] == defaultDummyNothing:
									vulnerableProjToMEShields[key]["GuaranteedBleedthrough"] = defaultPassThroughDmgMult
								if forcedBleedthrough <= 0:
									forcedBleedthrough = 1
									forcedBleedthroughMultiplier = vulnerableProjToMEShields[key]["GuaranteedBleedthrough"]
								else:
									forcedBleedthroughMultiplier = (forcedBleedthroughMultiplier * 2.0 + vulnerableProjToMEShields[key]["GuaranteedBleedthrough"]) / 2.0
									forcedBleedthrough = forcedBleedthrough + 1

			else:
				attackerShip = pEvent.GetFiringObject()
				if attackerShip:
					attackerID = attackerShip.GetObjID()
				pWeaponFired = None
				pEventSource = pEvent.GetSource()
				if pEventSource:
					pWeaponFired = App.Weapon_Cast(pEventSource)
				if pWeaponFired:
					if not attackerShip:
						pVec = NiPoint3ToTGPoint3(pEvent.GetWorldHitPoint())

						pWpnPos = NiPoint3ToTGPoint3(pWeaponFired.GetWorldLocation())
						pVec.Subtract(pWpnPos)
						pVec.Unitize()
						pVec.Scale(0.1 * sScaleFMult)

					else:
						pHitPointE = NiPoint3ToTGPoint3(pEvent.GetWorldHitPoint())
						pAttacker = App.ShipClass_GetObjectByID(None, attackerID)
						theOffset =  pAttacker.GetTargetOffsetTG() # This is given on the target's coordinates
						theOffsetNi = TGPoint3ToNiPoint3(theOffset)

						pShipShipNode = pShip.GetNiObject()

						pHitPointONi = App.TGModelUtils_LocalToWorldVector(pShipShipNode, theOffsetNi)
						pHitPointO = NiPoint3ToTGPoint3(pHitPointONi, 100.0)
						mod = "Tactical.Projectiles.ExtraPhasedDamageDummyME"
						torpImportedInfo = None
						torpImportedSpeed = 300.0
						try:
							torpImportedInfo = __import__(mod)
							if hasattr(torpImportedInfo, "GetLaunchSpeed"):
								torpImportedSpeed = torpImportedInfo.GetLaunchSpeed()	
						except:
							print "Tactical.Projectiles.ExtraPhasedDamageDummyME is missing from the install, or similar, we need that to deal damage!"
							traceback.print_exc()

						targetplacement = pShip.GetWorldLocation()
						targetplacement.Add(pHitPointO)

						pHitPointObj = targetplacement # Now THAT works


						pVec = CopyVector(pHitPointObj)
						pWpnPos = NiPoint3ToTGPoint3(pWeaponFired.GetWorldLocation())
						pVec.Subtract(pWpnPos)

						distTargetSubToMe = pVec.Length()

						planeD = -((pVec.x) * (pHitPointE.x) + (pVec.y) * (pHitPointE.y) + (pVec.z) * (pHitPointE.z))
						lambdai = -((pVec.x) * (pWpnPos.x) + (pVec.y) * (pWpnPos.y) + (pVec.z) * (pWpnPos.z) + planeD)/( (pVec.x) * (pVec.x) + (pVec.y) * (pVec.y) + (pVec.z) * (pVec.z) )
						proyEx = pWpnPos.x + pVec.x * lambdai
						proyEy = pWpnPos.y + pVec.y * lambdai
						proyEz = pWpnPos.z + pVec.z * lambdai

						theHitPoint = App.TGPoint3()
						theHitPoint.SetXYZ(proyEx, proyEy, proyEz)

						pVec.Unitize()

						pVec.Scale(1.0 * sScaleFMult)
						theHitPoint.Add(pVec) # add because we want to guarantee they bypass the shields



					weaponName = pWeaponFired.GetName()
					weaponname = string.lower(weaponName)

					for key in vulnerableBeamsToMEShields.keys():
							racesImmune = vulnerableBeamsToMEShields[key]["RacesImmune"]
							if raceShieldTech in racesImmune:
								continue
							isinWhitelistHardname = (weaponName in vulnerableBeamsToMEShields[key]["WhitelistHardname"])
							foundThis = 0
							isinBeamBlacklistName = 0
							if not isinWhitelistHardname:
								foundThis = string.find(weaponname, key) + 1
								for item in vulnerableBeamsToMEShields[key]["BlacklistName"]:
									isinBeamBlacklistName = string.find(weaponname, item) + 1
									if isinBeamBlacklistName:
										break

							if isinWhitelistHardname > 0 or (foundThis > 0 and not isinBeamBlacklistName > 0):
								if not vulnerableBeamsToMEShields[key].has_key("GuaranteedBleedthrough") or vulnerableBeamsToMEShields[key]["GuaranteedBleedthrough"] == defaultDummyNothing:
									vulnerableBeamsToMEShields[key]["GuaranteedBleedthrough"] = defaultPassThroughDmgMult
								if forcedBleedthrough <= 0:
									forcedBleedthrough = 1
									forcedBleedthroughMultiplier = vulnerableBeamsToMEShields[key]["GuaranteedBleedthrough"]
								else:
									forcedBleedthroughMultiplier = (forcedBleedthroughMultiplier * 2.0 + vulnerableBeamsToMEShields[key]["GuaranteedBleedthrough"]) / 2.0
									forcedBleedthrough = forcedBleedthrough + 1

			if negateRegeneration >= 0 and forcedBleedthroughMultiplier < 1.0:
				if sfacetFactor > 1.0:
					specialmultiplier = 1.0 * sfacetFactor * sfacetRegen
					negateRegeneration = -1.0 / sfacetFactor

					multFactor = multFactor * specialmultiplier

				if oYield and ((hasattr(oYield, "IsMERailgunWeaponYield") and oYield.IsMERailgunWeaponYield() != 0) or (hasattr(oYield, "IsSGRailgunWeaponYield") and oYield.IsSGRailgunWeaponYield() != 0)): # Some support to railguns
					if pTorp:
						mod = pTorp.GetModuleName()
						importedTorpInfo = __import__(mod)
						if hasattr(importedTorpInfo, "ShieldDmgMultiplier"):
							multFactor = multFactor * importedTorpInfo.ShieldDmgMultiplier()

			else:
				if fDamage > 0.0:
					specialmultiplier = 1.0 * fDamage
					negateRegeneration = negateRegeneration / fDamage
					multFactor = multFactor * specialmultiplier

			shieldsArePierced, nearestPoint = shieldInGoodCondition(pShip, kPoint, shieldPiercedThreshold, 0, None)

			if not pTorp: # For beams we have to do this or risk hardpoint heals
				shieldsAreNotGood, nearestPoint = shieldInGoodCondition(pShip, kPoint, shieldGoodThreshold, 2, nearestPoint)
			else: # This line below might be problematic on certain scenarios. If there are problems when firing torpedoes, please remove this if-else conditional while only leaving the line above for shieldsAreNotGood
				shieldsAreNotGood, nearestPoint = shieldInGoodCondition(pShip, kPoint, shieldGoodThreshold, 0, nearestPoint)	

			
			if pEvent.IsHullHit():
				# POINT 4: While in theory this is handled by the "No damage through shields" option on DS9FX configuration we want to also check it manually because:
				# 1. - That is an option which can be turned on/off. Following POINT 4, we want to ensure that this no-dmg-through-shields behaviour happens regardless of the DS9FX option being active or inactive.
				# 2. - Sometimes the "No damage through shields", for one reason or another, does not properly cover when a ton of incoming fire is hitting a ship, or does not cover when a vessel presents a weird geometry. In STBC, some vessels' models (including ME) present certain geometry shapes that ensure there's bleedthrough even when shields are completely full, so we need to fix that ourselves!
				if not pTorp or not (pTorp.GetNetType() == torpsNetTypeThatCanPhase):
					# then we do the heal if shields are good
					if (shieldsAreNotGood <= 0): #  and (shieldsArePierced <= 0)
						#print "shields are good enough to block the damage, reverting it"
						theHull = pShip.GetHull()
						hullName = None
						if theHull:
							hullName = theHull.GetName()
						hullCounted = 0
						ds9checks = 0

						try:
							reload (DS9FXSavedConfig)

							if DS9FXSavedConfig.NoDamageThroughShields == 1:
								ds9checks = 1
						except:
							print "Error while trying to import DS9FXSavedConfig"
							ds9checks = 0
							traceback.print_exc()

						# The method below does not cover the children, funnily enough. We would need to cover subsystems personally.
						kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
						while (1):
							pSys = pShip.GetNextSubsystemMatch(kIterator)
							if not pSys:
								break

							#print pSys.GetName()


							# But if you want for the shields to cover everything, just expand and uncomment the section below
							#for i in range(pSys.GetNumChildSubsystems()):
							#	pChild = pSys.GetChildSubsystem(i)
								
							iCon = pSys.GetCondition()
							iMax = pSys.GetMaxCondition()

							if iCon <= 0.0 or iCon >= iMax or not pSys.IsTargetable():
								continue

							pSysPos = pSys.GetPosition()

							vDistance = App.TGPoint3()
							vDistance.SetXYZ(pSysPos.x, pSysPos.y, pSysPos.z)
							vDistance.Subtract(kPoint)

							if vDistance.Length() > (pSys.GetRadius() + fRadius):
								continue

							if raceShieldTech == "Replicator":
								# We need to be very strict to avoid accidental slip-ups with damage for the Replicators
								if ds9checks == 1 and (pShDmgForDS9FX == 0) and not ((pTorp != None and (iMax - iCon) < (fDamage - 0.01)) or ((vDistance.Length() / pShip.GetRadius()) > (pSys.GetRadius() + fRadius))):
									if pSys.GetName() == hullName:
										hullCounted = hullCounted + 1
									# "DS9FX is already handling this part"
									continue
							else:	# For other ships that did not have that, this strategy worked better:
								# OG STRATEGY
								#if ds9checks == 1 and ((pTorp != None and (iMax - iCon) < (fDamage - 0.01)) or ((vDistance.Length() / pShip.GetRadius()) > (pSys.GetRadius() + fRadius))):
								#	# "DS9FX is already handling this part"
								#	continue
								if ds9checks == 1 and (pShDmgForDS9FX == 0) and not ((pTorp != None and (iMax - iCon) < (fDamage - 0.01)) or ((vDistance.Length() / pShip.GetRadius()) > (pSys.GetRadius() + fRadius))):
									continue

							iNewCon = iCon + fDamage

							if iNewCon > iMax:
								iNewCon = iMax

							pSys.SetCondition(iNewCon)
			
							if pSys.GetName() == hullName:
								hullCounted = hullCounted + 1

						pShip.EndGetSubsystemMatch(kIterator)

						if theHull != None and hullCounted <= 0:
							#print "hull was not counted... well we will count it anyways"
							iCon = theHull.GetCondition()
							iMax = theHull.GetMaxCondition()

							iNewCon = iCon + fDamage

							if iNewCon > iMax:
								iNewCon = iMax

							theHull.SetCondition(iNewCon)
		
				# Certain ME Armours may do something if the hull is hit. However for now this is more than enough and the extra armor-related events could be covered in another technology.

			else:
				# This line was moved here to avoid invulnerable edge cases
				shieldsArePierced, nearestPoint = shieldRecalculationAndBroken(pShip, kPoint, 0, shieldPiercedThreshold, 0, negateRegeneration, nearestPoint, fDamage, multFactor)
				#First check, those weapons that can pass-through
				if forcedBleedthrough > 0:
					myDamage = fDamage * forcedBleedthroughMultiplier * bypassMultiplier

					global SlowDownRatio
					mod = "Tactical.Projectiles.ExtraPhasedDamageDummyME"
					launchSpeed = __import__(mod).GetLaunchSpeed()
					considerspeeddebuff = launchSpeed/(1.0 * pShip.GetRadius())

					theSame = 0
					myRadius = 0.001
					if pTorp:
						myRadius = pTorp.GetDamageRadiusFactor()
						if pTorp.GetModuleName() == mod:
							theSame = 1
					else:
						myRadius = fRadius * 1.0
						
					shipNeeded = None
					if theHitPoint == None:
						theHitPoint = NiPoint3ToTGPoint3(pEvent.GetWorldHitPoint())

					#if considerspeeddebuff <= SlowDownRatio:
					#	shipNeeded = pShip

					if theSame == 0 and (pTorp or myDamage > 0.1): # If a phaser or torp deals less than certain damage, don't bother - this is both a strategy to produce less torps, and a way to avoid "floaty ghost torps"
						pTempTorp = FireTorpFromPointWithVectorAndNetType(theHitPoint, pVec, mod, pShip.GetObjID(), attackerID, launchSpeed, torpsNetTypeThatCanPhase, myDamage, myRadius, isHidden, shipNeeded, theOffset)
						if pTempTorp:
							pTempTorp.SetLifetime(15.0)
							pTempTorp.UpdateNodeOnly()

						if pShip.GetRadius() < 0.15:
							# Perform damage manually as well
							myHull = pShip.GetHull()
							if myHull:
								global torpCountersForInstance

								pEvent1 = TGFakeWeaponHitEvent_Create() # This gives us a pointer, it has no arguments, but it is our "fake" event
								pEventSource = pTorp
								pEventDestination = pShip

								pEvent1.SetSource(pEventSource)
								pEvent1.SetDestination(pEventDestination)
								pEvent1.SetEventType(App.ET_WEAPON_HIT)

								pAttacker = App.ShipClass_GetObjectByID(None, attackerID)
								pEvent1.SetFiringObject(pAttacker)
								pEvent1.SetTargetObject(pShip)

								myHullPos = NiPoint3ToTGPoint3(myHull.GetPosition())

								pEvent1.SetObjectHitPoint(myHullPos)

								pShipPositionV = pShip.GetWorldLocation()
								pShipPositionVI = TGPoint3ToNiPoint3(pShipPositionV, -1.0)
								pShipNode = pShip.GetNiObject()

								pEvent1.SetObjectHitNormal(pShipPositionVI) 
								pEvent1.SetWorldHitPoint(myHullPos)
								pShipPositionVW = TGPoint3ToNiPoint3(App.TGModelUtils_LocalToWorldUnitVector(pShipNode, pShipPositionVI), 1.0)
								pEvent1.SetWorldHitNormal(pShipPositionVW)

								eCondition = 1.0
								if myHull:
									eCondition = myHull.GetConditionPercentage()
								pEvent1.SetCondition(eCondition)

								valPlus = torpCountersForInstance + 1

								pEvent1.SetWeaponInstanceID(valPlus) # Not needed... at least, I am not aware of any scripts handling it for torpedo defense

								pEvent1.SetRadius(myRadius)
								pEvent1.SetDamage(myDamage)
								pEvent1.SetHullHit(1)
								pEvent1.SetFiringPlayerID(0)

								affectedSys, nonTargetSys = FindAllAffectedSystems(pShip, myHullPos, myRadius)
								AdjustListedSubsystems(pShip, affectedSys, nonTargetSys, -myDamage, len(affectedSys) + 1, 1)

								# Fourth part, finally using the pEvent for something! This is also so more armours can work with these collisions, and not only one or two.
								if pTempTorp:
									pInstance.DefendVSTorp(pShip, pEvent1, pTempTorp)

			if oYield and hasattr(oYield, "IsPhasedPolaronYield") and oYield.IsPhasedPolaronYield() != 0 and pInstance and pInstance.__dict__.has_key('ME Shields'): # POINT 6.
				return 1


		def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnBeamDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnPulseDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			return self.OnDefense(pShip, pInstance, oYield, pEvent, pTorp)


		# TODO:  Make this an activated technology
		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
			pInstance.lPulseDefense.insert(0, self)
			pInstance.lBeamDefense.insert(0, self)
			# print 'Attaching ME Shields to', pInstance, pInstance.__dict__

		# def Activate(self):
		# 	FoundationTech.oWeaponHit.Start()
		# def Deactivate(self):
		# 	FoundationTech.oWeaponHit.Stop()

	oMEShields = MEShieldsDef('ME Shields')
	# print 'ME Shields loaded'

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nME Shields are there but NOT enabled in your current BC installation"
	traceback.print_exc()