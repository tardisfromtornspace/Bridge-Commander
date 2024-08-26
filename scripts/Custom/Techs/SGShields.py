#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         SGShields.py by Alex SL Gato
#         24th August 2024
#         Based strongly on Shields.py by the FoundationTechnologies team, ATPFunctions by Apollo, HelmMenuHandlers from the STBC Team, and SGGIonWeapon by Alex SL Gato.
#################################################################################################################
# This technology encompasses most of SG defences in a generic way, mostly for tagging, but also for referencing common shield protection strengths and weaknesses over standard STBC shields.
# Here are the main differences regarding strengths and weaknesses of SG Shields (in comparision with STBC shields, which are supposed to be an in-game simplified version of early post-Dominion War ST Federation shielding):
# * POINT 1: Excluding ST metaphasic shields and some trinesium-based hulls, SG Shields can withstand being inside a star's corona for quite a while longer than regular ST Federation shielding (and better than the Borg, at least, TNG Borg), capable of avoiding the radiation from leaking inside the vessel for a while. - ONGOING
# * POINT 2: While both ST Federation shielding and SG shields can do it, SG shields are often stronger when blocking an incoming physical object from colliding, with their shield bubbles at least. - DONE
# * POINT 3: SG Shields cannot usually block dimensional effects, such as certain dimensional disruptions like event horizons, wormholes or black holes. ST shields (at least, Federation, Klingon and Romulan ones) hold a bit better against those, with containment fields specifically built for holding micro-singularities and even those dissipating against polarized hull plating (ok that last statement is ridiculous, but it is what is mentioned in Memory Alpha). -ONGOING
# * POINT 4: Overall, SG shields, at least Go'auld and above, are stronger against strong impacts, but also seem to have some weaknesses towards lower-powered ones... or at least, they are strong against radiation and nuclear blasts but have some weakness to concentrated plasma bolts, even small (those are the only way to explain why a >1000 Megaton Nuke had no effect on a Go'auld vessel with shields up while a few Death Gliders can drain a Go'auld shields a bit with their shots, if we don't count possible plot armor). - ONGOING
# * POINT 5: Regarding Federation shielding, Plasma is quite a varied matter - small bolts and plasma projectiles do nothing to their shields, but big advanced ones can pack quite a punch or even drill a hole on their shields (of course the latter example is taken from TOS Balance of Terror and SNW versions against primitive plasma torpedoes and advanced plasma torpedoes, with 23rd century Constitution-class shielding being far weaker and less advanced than a 24th century Galaxy-class shield, but the point still stands) - DONE: This has already been taken care of in the SGPlasmaWeaponScript.
# * POINT 6: If properly tweaked, a SG Shield can perfectly block a certain frequency or type of weapon with (almost) no shield drain, even if before they could not block them... at least for Alteran-based shields which seem to be based on the frequency-antifrequency principle to negate damage, compared with the same-frequency-can-pass of ST Federation shielding that is only supposed to allow a single set of frequencies to pass, but all the others are blocked "almost" perfectly. - DONE here and in other scripts
# ** F.ex. traditional Go'auld shields cannot block an Ion Weapon, but upgraded Anubis ones can and also make them totally ineffective, while still only having shields a bit stronger overall. And talking about Ion Weapons...
# * POINT 7:  On SG, Ion Weapons work more as regular projectiles, lowering shields and then dealing hull damage, but with the twist that they deal a lot of Hull Damage, and standard Go'auld shields lack the ability to block them (for ST fans, Ion Weapons to a Go'auld shield are like a pre-Dominion-War Federation Galaxy-class shield against Phased Polaron Beams). Ion Weapons in ST work more as shield drainers - they rarely (if at all) lower all shields from one hit, requiring several even if they carry a kinetic charge, but they will definetely drain the shields and give problems to the shield regeneration. - DONE: This has already been taken care of in the SGIonWeaponScript.
# * POINT 8: excluding the exceptions from the other points, SG shields in general do not take as much hull bleedthrough damage when shields are at full strength, except on counted occasions. Mostly the damage they may receive when shields are still at full is more towards the power grids and similar, not to the hull proper, unless their shields cannot adapt. - DONE here
# * POINT 9: Since SG shields and ST Federation shields work on different principles, it is very likely that Phased Polaron weapons would do nothing to SG shields. - DONE here

# The following is not necessarily a point of difference between ST and SG shields, but it is important for our points to determine some SG Shields things to code:
# * POINT 10: Asgard Shields recover normally if a weapon hit is too-low yield, as if the weapon did not hit them. - DONE here
# * POINT 11: Some Ori prior shields use the energy of the impacts to become stronger, albeit that was only seen on the Ori Beachhead shield which was far more powerful than an Ori Warship shield. - DONE here
# * POINT 12: At least some SG Shields seem to be affected by merely being in an atmosphere. Or at least, only Anubis Superweapon's shields. - DONE here

from bcdebug import debug
import traceback

import App
import FoundationTech
#### TO-DO UPDATE THIS ####
# This should be the prime example of a special yield weapon defined
# according to Foundation Technologies.  The code is mostly based upon
# QuickBattleAddon.corboniteReflector() in Apollo's Advanced Technologies.


from ftb.Tech.ATPFunctions import *

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.1",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

NonSerializedObjects = (
"oSGShields",
)
try:
	import Foundation
	import FoundationTech
	import MissionLib
	import Multiplayer.SpeciesToTorp

	import nt
	import string

	from ftb.Tech.ATPFunctions import *
	from math import *

	g_pAtmosCollisionCheckProcess = None
	torpsNetTypeThatCanPhase = [Multiplayer.SpeciesToTorp.PHASEDPLASMA] # For the "torpedoes-going-through" issue
	defaultDummyNothing = "NaN"
	SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side
	torpCountersForInstance = 32 # Auxiliar value to fake a pEvent, for new collisions

	shieldPiercedThreshold = 0.25 # If that shield is below this percentage, then the shield is considered pierced
	shieldGoodThreshold = 0.400001 # if that shield is above or equal this percentage, then the shield is considered to be in good condition
	defaultPassThroughDmgMult = 0.1

	# A Dict of torpedoes that normally cannot deal damage through shields to STBC shields at full, but which could deal at least some guaranteed bleedthrough to SG shields.
	# The dict is built from a list of scripts, each dict works with the following fields (with an example)
	# "ProjectileName": {"GuaranteedBleedthrough": 0.1, "WhitelistFilename": ["Quantum", "QuantumTorpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"], "BlacklistFilename": ["AntiQuantum", "Quantumania"]}
	# "ProjectileName" refers to a certain projectile name that the projectile's name or sScript filename match or have a common string with, case-insenstitive.. #### TO-DO Make it so the fields and name go through a lowercase function for compatibility ####
	# "GuaranteedBleedthrough" indicates ther relative dmg through a shield the weapon will deal, according to a multiplier. 0.1 is the default
	# "WhitelistFilename": adds extra torpedo filenames that, if matched exactly (case-sensitive), will guarantee they are included and will ignore blacklists (this field is here if somebody wants to add a torpedo with that ProjectileName torpedo properties, but under a different name).
	# "BlacklistName": includes a list of projectile on-screen names that cannot apply to this. This one will be triggered if the torpedo names match or have that string of words, case-insenstitive.
	# "BlacklistFilename": includes a list of projectile filenames that if they match cannot be applied to this. This one does need to match the words exactly and is case-sensitive.

	vulnerableProjToSGShields = {}

	# A Dict of beams that normally cannot deal damage through shields to STBC shields, but which could deal at least some guaranteed bleedthrough to SG shields. I currently do not know of any in particular... hm, maybe lasers, but that would go into too many what-ifs, so no, I don't know of any and on the original install from this mod this dict field will be empty. However, I'm leaving this field open for expansion.
	# "BeamName": {"GuaranteedBleedthrough": 0.1, "WhitelistHardname": ["Quantum", "Quantum Torpedo"], "BlacklistName": ["not a quantum", "not quantum", "no quantum", "anti-quantum", "antiquantum", "quantumania"]}
	# "BeamName" refers to a certain App phaser bank property (that is what they are called mod-wise, to the player they could have any varied names: beams, lasers, phasers, particle beams, etc.) name that the hardpoint's name match or have a common string with, case-insenstitive.. #### TO-DO Make it so the fields and name go through a lowercase function for compatibility ####
	# "GuaranteedBleedthrough" indicates ther relative dmg through a shield the weapon will deal, according to a multiplier. 0.1 is the default
	# "WhitelistHardname": adds extra hardpoint names that, if matched exactly (case-sensitive), will guarantee they are included and will ignore blacklists (this field is here if somebody wants to add a phaser bank property with that BeamName properties, but under a different name).
	# "BlacklistName": includes a list of hardpoint property names that cannot apply to this. This one will be triggered if the hardpoint names match or have that string of words, case-insenstitive.

	vulnerableBeamsToSGShields = {}

	# "similarTechsNames" is a dict of technologies which can react to SGShields shield collision simulation. While I cannot immedaitely think of one in particular, this allwos expansion without editing this file
	# Structure would go like this, where "techName" is the name of the technology, and "multiplier" is a numeric value that increases or decreases the damage SGShields would receive
	# similarTechsNames = {"techName": multiplier}
	similarTechsNames = {}

	# For regular shields - as I said on 
	globalRegularShieldReduction = 0.5 # TO-DO ADD A WAY TO IMPORT THIS

	# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
	def NiPoint3ToTGPoint3(p, factor=1.0):
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x * factor, p.y * factor, p.z * factor)
		return kPoint

	def TGPoint3ToNiPoint3(p, factor=1.0):
		kPoint = App.NiPoint3(p.x * factor, p.y * factor, p.z * factor)
		#TO-DO SEE HOW TO CREATE THESE
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
		global vulnerableProjToSGShields, vulnerableBeamsToSGShields, defaultDummyNothing

		dir="scripts\\Custom\\Techs\\SGShieldsScripts" # I want to limit any vulnerability as much as I can while keeping functionality

		try:
			list = nt.listdir(dir)
			if not list:
				print "ERROR: Missing scripts/Custom/Techs/SGShieldsScripts folder for SGShields technology"
				return

		except:
			print "ERROR: Missing scripts/Custom/Techs/SGShieldsScripts folder for SGShields technology, or other error:"
			traceback.print_exc()
			return		

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
				#print "SGShields script is reviewing " + fileName + " of dir " + dir
				if dExcludePlugins.has_key(fileName):
					debug(__name__ + ": Ignoring plugin" + fileName)
					continue

				try:
					if not variableNames.has_key(fileName):
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
					
						if hasattr(banana, "ProjectileName") and banana.ProjectileName() != "": # These will not be affected at all by the hull or shield effects, period

							projName = banana.ProjectileName()
							if not vulnerableProjToSGShields.has_key(projName):
								vulnerableProjToSGShields[projName] = {}

							if not vulnerableProjToSGShields[projName].has_key("GuaranteedBleedthrough"):
								vulnerableProjToSGShields[projName]["GuaranteedBleedthrough"] = defaultDummyNothing

							if hasattr(banana, "ProjectileGuaranteedBleedthrough") and vulnerableProjToSGShields[projName]["GuaranteedBleedthrough"] == defaultDummyNothing:
								vulnerableProjToSGShields[projName]["GuaranteedBleedthrough"] = banana.ProjectileGuaranteedBleedthrough

							if not vulnerableProjToSGShields[projName].has_key("WhitelistFilename"):
								vulnerableProjToSGShields[projName]["WhitelistFilename"] = []

							if not vulnerableProjToSGShields[projName].has_key("BlacklistName"):
								vulnerableProjToSGShields[projName]["BlacklistName"] = []

							if not vulnerableProjToSGShields[projName].has_key("BlacklistFilename"):
								vulnerableProjToSGShields[projName]["BlacklistFilename"] = []

							if hasattr(banana, "ProjectileWhitelistFilename"):
								for item in banana.ProjectileWhitelistFilename:
									vulnerableProjToSGShields[projName]["WhitelistFilename"].append(item)

							if hasattr(banana, "ProjectileBlacklistName"):
								for item in banana.ProjectileBlacklistName:
									vulnerableProjToSGShields[projName]["BlacklistName"].append(item)

							if hasattr(banana, "ProjectileBlacklistFilename"):
								for item in banana.ProjectileBlacklistFilename:
									vulnerableProjToSGShields[projName]["BlacklistFilename"].append(item)

						if hasattr(banana, "BeamName") and banana.BeamName() != "": # These will not be affected at all by the hull or shield effects, period

							projName = banana.BeamName()
							if not vulnerableBeamsToSGShields.has_key(projName):
								vulnerableBeamsToSGShields[projName] = {}

							if not vulnerableBeamsToSGShields[projName].has_key("GuaranteedBleedthrough"):
								vulnerableBeamsToSGShields[projName]["GuaranteedBleedthrough"] = defaultDummyNothing

							if hasattr(banana, "BeamGuaranteedBleedthrough") and vulnerableBeamsToSGShields[projName]["GuaranteedBleedthrough"] == defaultDummyNothing:
								vulnerableBeamsToSGShields[projName]["GuaranteedBleedthrough"] = banana.BeamGuaranteedBleedthrough

							if not vulnerableBeamsToSGShields[projName].has_key("WhitelistHardname"):
								vulnerableBeamsToSGShields[projName]["WhitelistHardname"] = []

							if not vulnerableBeamsToSGShields[projName].has_key("BlacklistName"):
								vulnerableBeamsToSGShields[projName]["BlacklistName"] = []

							if hasattr(banana, "WhitelistHardname"):
								for item in banana.BeamWhitelistHardname:
									vulnerableBeamsToSGShields[projName]["WhitelistHardname"].append(item)

							if hasattr(banana, "BeamBlacklistName"):
								for item in banana.BeamBlacklistName:
									vulnerableBeamsToSGShields[projName]["BlacklistName"].append(item)

						if fileName == "BasicSGShieldsConfiguration":
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
						# TO-DO ADD THE CONFIG FILES!!!
						print "SGShields reviewing of this file is a success"
				except:
					print "someone attempted to add more than they should to the SG Shields script"
					traceback.print_exc()

	LoadExtraLimitedPlugins()
	print vulnerableProjToSGShields
	print vulnerableBeamsToSGShields

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
						raceShieldTech = None
						# Extra shield config things
						if instanceDict.has_key("SG Shields"):
							if instanceDict["SG Shields"].has_key("RaceShieldTech"):
								raceShieldTech = instanceDict["SG Shields"]["RaceShieldTech"]

						if instanceDict.has_key("SG Shields Active"):
							if wpnActiveState != instanceDict["SG Shields Active"]: # Means shields have changed
								if wpnActiveState == 0: # Shields have been deactivated:
									ActivateSGShieldCollisions(pShip, pInstance, instanceDict, 0, raceShieldTech, pShields)

								else: # Shields have been activated
									if not (pShields.IsDisabled() or not pShields.IsOn() or pShields.GetPowerPercentageWanted() <= 0.0): # A last check
										ActivateSGShieldCollisions(pShip, pInstance, instanceDict, 1, raceShieldTech, pShields)
									else:
										ActivateSGShieldCollisions(pShip, pInstance, instanceDict, 0, raceShieldTech, pShields)
				else:
					ActivateSGShieldCollisions(pShip, pInstance, instanceDict, 0)

	class weDidThisPair: # This is not a lock, not by far - in-game many things are taken sequentially, with one interlacing the other, including a collision call, where pShipA-pShipB collision message are followed by but hopefully this will prevent some issues # TO-DO ONLY ADD THIS LOCK IF BOTH SIDES HAPPEN TO HAVE SG SHIELDS OR SIMILAR, AND REMOVE THE LOCK BEFORE THAT
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

	def damageCalc(fTorpDamage, fShieldDamage, myShieldBroken, othersShieldBroken, myHull, otherHull, myShieldDirNearest, othersShieldDirNearest, pOtherShields, pMeShields, IhaveSGShields, OtherHasSGShields, pinstanceMeShieldRace, pinstanceOtherShieldRace, dummyDamage, massToMassRelation, otherHasSimilarShields, multiplierMyShieldFactor): # massToMassRelation needs tobe the inverse for the other

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
					print "Dummy hull damage"
					fShieldDamage = fShieldDamage + dummyDamage * 10
			else:
				#print "the other resists too", pOtherShields, othersShieldDirNearest
				if pOtherShields and othersShieldDirNearest != None: # If they have still some shield strength, add it to the damage
					fShieldDamage = fShieldDamage + pOtherShields.GetCurShields(othersShieldDirNearest)
				else:
					print "Dummy shield damage"
					fShieldDamage = fShieldDamage + dummyDamage * 10

			fShieldDamage = fShieldDamage * massToMassRelation

			if OtherHasSGShields <= 0 and otherHasSimilarShields <= 0:
				fShieldDamage = fShieldDamage * globalRegularShieldReduction

			else:
				if otherHasSimilarShields > 0:
					fShieldDamage = fShieldDamage * multiplierMyShieldFactor
				else:
					fShieldDamage = fShieldDamage * globalRegularShieldReduction

		if not myShieldBroken and (pinstanceMeShieldRace == "Asgard" or pinstanceMeShieldRace == "Ori"): # POINT 10.
				fShieldDamage = fShieldDamage * 0.8
				negateRegeneration = -1
				if pinstanceMeShieldRace == "Ori": # POINT 11 - this will make the Ori vessels impervious to low-grade shots, no more Death gliders crashing and lowering their shields willy-nilly
					multFactor = multFactor * 1000
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
			#self.thisown = 1 # TO-DO Maybe not if this does not work?
			#self.this = this
			self.firingObject = None # TO-DO ADD MISSING FIELDS
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

		def __del__(self, Appc=Appc): # TO-DO move to the end
			if self.thisown == 1 :
				self.firingObject = None # TO-DO ADD MISSING FIELDS
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

				pEvent1.SetObjectHitPoint(kPointpShipPerNi) # TO-DO CHECK THESE 
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

		
	def CollisionHappened(pObject, pEvent): # POINT 2. Future TO-DO maybe see what triggers a shield collision event?
		# On an ideal world we would enable and disable collisions damage. However, for some reason, Disabling collision damage permanently leaves it disabled, even if the "pShip.IsCollisionDamageDisabled()" says it is enabled

		#print pEvent.GetDamage() # Collision events funnily enough do not have dmg... at least if they don't have damage collisions on TO-DO check this without dmg col disabled later

		pInstanceMeDict = None
		pInstanceOtherDict = None

		pinstanceMeShieldRace = None
		pinstanceOtherShieldRace = None

		IhaveSGShields = 0
		OtherHasSGShields = 0

		IhaveSGShieldsButFailed = 0
		OtherhaveSGShieldsButFailed = 0
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

		if pInstanceMe and pInstanceMeDict.has_key("SG Shields"):
			#print ("me have key", end= '')
			pMeShields = pShip.GetShields()

			if pInstanceMeDict["SG Shields"].has_key("RaceShieldTech"):
				pinstanceMeShieldRace = pInstanceMeDict["SG Shields"]["RaceShieldTech"]
			if pinstanceMeShieldRace != "Wraith":
				if pMeShields:
					#pAuxShieldsProperty = pMeShields.GetProperty()
					maxShields = 0.0
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						fMax = pMeShields.GetMaxShields(shieldDir)
						maxShields = maxShields + fMax

					if maxShields > 0.0:
						IhaveSGShields = 1
						if pMeShields.IsDisabled() or not pMeShields.IsOn():
							IhaveSGShieldsButFailed = 1

		if IhaveSGShields <= 0: # If I don't have them, why or how am I here?
			return

		if pInstanceOther and pInstanceOtherDict.has_key("SG Shields"):
			#print ("others have key", end= '')
			pOtherShields = pOtherShip.GetShields()
			#print("other shields work", end= '')
			if pInstanceOtherDict["SG Shields"].has_key("RaceShieldTech"):
				pinstanceOtherShieldRace = pInstanceOtherDict["SG Shields"]["RaceShieldTech"]
			if pinstanceOtherShieldRace != "Wraith":
				if pOtherShields:
					maxShields = 0.0
					for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
						fMax = pOtherShields.GetMaxShields(shieldDir)
						maxShields = maxShields + fMax

					if maxShields > 0.0:
						OtherHasSGShields = 1
						if pOtherShields.IsDisabled() or not pOtherShields.IsOn():
							OtherhaveSGShieldsButFailed = 1

		# Actual collision calculations:
		otherHasSimilarShields = 0
		multiplierMyShieldFactor = 1.0
		if pInstanceOther and pInstanceOtherDict:
			for techName in similarTechsNames.keys():
				if pInstanceOtherDict.has_key(techName): # TO-DO ADD A WAY TO IMPORT THESE
					otherHasSimilarShields = otherHasSimilarShields + 1
					multiplierMyShieldFactor = multiplierMyShieldFactor * similarTechsNames[techName]

		meHasSimilarShields = 0
		multiplierOtherShieldFactor = 1.0
		if pInstanceMe and pInstanceMeDict:
			for techName in similarTechsNames.keys():
				if pInstanceMeDict.has_key(techName): # TO-DO ADD A WAY TO IMPORT THESE
					meHasSimilarShields = meHasSimilarShields + 1
					multiplierOtherShieldFactor = multiplierOtherShieldFactor * similarTechsNames[techName]

		#print "It is ", pShip.GetName(), "'s turn"
		#if IhaveSGShields > 0 and (OtherHasSGShields > 0 or otherHasSimilarShields > 0):
		#	saruman = weDidThisVerify.EnterPair(pTheOther.GetObjID(), pObject.GetObjID()) # This means we were here first, so gandalf can control those who arrive late
		#	#if saruman <= 0:
		#	#	print "the hit was already done for one side but the other did not take it or clean it in time" # TO-DO if this happens the hit was already done for one side but the other did not take it
			
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

		numCollisionPoints = pEvent.GetNumPoints()
		for i in range (pEvent.GetNumPoints()):
			kPointW = pEvent.GetPoint(i) # For use with the shields
			kPoint = NiPoint3ToTGPoint3(kPointW)

			pShipPositionV = pShip.GetWorldLocation()
			pShipPositionV.Subtract(kPoint) # For a torpedo that goes from THEIR ship to OURS

			pOtherShipPositionV = pOtherShip.GetWorldLocation()
			pOtherShipPositionV.Subtract(kPoint) # For a torpedo that goes from OUR ship to THEIRS

			kPointpShipPerNi = App.TGModelUtils_WorldToLocalPoint(pShipNode, kPointW)
			kPointpOtherShipPerNi = App.TGModelUtils_WorldToLocalPoint(pOtherShipNode, kPointW) # TO-DO IF YOU MOVE THIS ONE ABOVE THE OTHER ONE, WILL DUMMY DAMAGE STILL HAPPEN?

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

			myShieldBroken, fTorpDamageMe, fShieldDamageMe, multFactorMe, negateRegenerationMe = damageCalc(fTorpDamage, fShieldDamage, myShieldBroken, othersShieldBroken, myHull, otherHull, myShieldDirNearest, othersShieldDirNearest, pOtherShields, pMeShields, IhaveSGShields, OtherHasSGShields, pinstanceMeShieldRace, pinstanceOtherShieldRace, dummyDamage, massToMassRelation, otherHasSimilarShields, multiplierMyShieldFactor)

			othersShieldBroken2 = 0
			if OtherHasSGShields > 0 or otherHasSimilarShields > 0:
				othersShieldBroken, fTorpDamageYou, fShieldDamageYou, multFactorYou, negateRegenerationYou = damageCalc(fTorpDamage2, fShieldDamage2, othersShieldBroken, myShieldBroken, otherHull, myHull, othersShieldDirNearest, myShieldDirNearest, pMeShields, pOtherShields, OtherHasSGShields, IhaveSGShields, pinstanceOtherShieldRace, pinstanceMeShieldRace, dummyDamage, (1.0/massToMassRelation), meHasSimilarShields, multiplierOtherShieldFactor)

				othersShieldBroken2, othersShieldDirNearest = shieldRecalculationAndBroken(pOtherShip, kPointpOtherShipPer, -fShieldDamageYou, shieldPiercedThreshold, 0, negateRegenerationYou, othersShieldDirNearest, -fShieldDamageYou, multFactorYou)

			myShieldBroken2, myShieldDirNearest = shieldRecalculationAndBroken(pShip, kPointpShipPer, -fShieldDamageMe, shieldPiercedThreshold, 0, negateRegenerationMe, myShieldDirNearest, fShieldDamageMe, multFactorMe)

			# TO-DO for the thing below it may be better to just... damage the actual subsystems manually (check Borg adaptation!), to avoid possible torpedo-related errors. and then fake a Torpedo Event and broadcast it! Oh, also, fire just one torpedo if the vessel is about to die or something, to punch a hole

			mod = "Tactical.Projectiles.ExtraCollisionDamageDummy"
			if (myShieldBroken or myShieldBroken2) and not (pShip.IsDead() or pShip.IsDying()):
				performFakeTorpEvents(pShip, pInstanceMe, pOtherShip, mod, fTorpDamageMe, myHull, myShieldBroken, myShieldBroken2, otherShipRadius, pShipNode, kPointW, kPoint, kPointpShipPer, kPointpShipPerNi, pShipPositionV)

			if (OtherHasSGShields > 0 or otherHasSimilarShields > 0) and (othersShieldBroken or othersShieldBroken2) and not (pOtherShip.IsDead() or pOtherShip.IsDying()):
				performFakeTorpEvents(pOtherShip, pInstanceOther, pOtherShip, mod, fTorpDamageYou, otherHull, othersShieldBroken, othersShieldBroken, myShipRadius, pOtherShipNode, kPointW, kPoint, kPointpOtherShipPer, kPointpOtherShipPerNi, pOtherShipPositionV)

	def ActivateSGShieldCollisions(pShip, pInstance, instanceDict, activate=1, raceShieldTech=None, pShields=None):
		if pShip.IsDead() or pShip.IsDying():
			return
		maxShields = 0.0
		if pShields:
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fMax = pShields.GetMaxShields(shieldDir)
				maxShields = maxShields + fMax
		if activate == 1 and raceShieldTech != "Wraith" and maxShields > 0.0:
			#print "pShip to add collision shields: ", pShip.GetName()
			instanceDict["SG Shields Active"] = 1
			#if not pShip.IsCollisionDamageDisabled():
			pShip.DisableCollisionDamage(1)
			#pShip.DamageRefresh(1)
		else:
			instanceDict["SG Shields Active"] = 0
			if raceShieldTech != "Wraith":
				#if pShip.IsCollisionDamageDisabled():
				pShip.DisableCollisionDamage(0)
				pShip.SetCollisionsOn(0)
				pShip.SetCollisionsOn(1)
				#pShip.DamageRefresh(1)

		pShip.UpdateNodeOnly()

	def ShieldCollisionHappened(pObject, pEvent):
		print "Ok a shield collision happened"

	# POINT 12
	# # Future TO-DO: if you finally find where the App.ET_PLANET_ATMOSPHERE_COLLISION is sent to and in what channels it is sent, and is less bothersome than having to add a lsitener to the planets, please, replace ProcessWrapper and CollisionAtmosAlertCheck for a listener on the ship or tech and def AtmosCollisionHappened
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
						if shieldDirNearest == shieldDir and (fMax <= 0 or resultHeal < (shieldThreshold * fMax)):
							shieldHitBroken = shieldHitBroken + 1
			else:
				shieldHitBroken = 1
				

		else:
			shieldHitBroken = 1

		return shieldHitBroken, shieldDirNearest
				
	class SGShieldsDef(FoundationTech.TechDef):
		#TO-DO MAYBE ADD A COLLISION LISTENER? 
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

		def Col(self, pEvent):
			print "ET_OBJECT_COLLISION col event caught by broadcast"

		def OneCol(self, pEvent):
			print "shield col event caught by broadcast"
			ShieldCollisionHappened(self, pEvent)

		def AtmosCol(self, pEvent):
			print "atmos col event caught by broadcast"
			AtmosCollisionHappened(self, pEvent)

		def PCol(self, pEvent):
			print "planet col event caught by broadcast"
			PCollisionHappened(self, pEvent)

		def AttachShip(self, pShip, pInstance):	# TO-DO ALSO ADD A DETACH TO REMOVE THE SG shields Active field and the CollisionCheckProcess for the vessel
			debug(__name__ + ", AttachShip")

			raceShieldTech = None
			# Extra shield config things
			instanceDict = pInstance.__dict__
			if instanceDict.has_key("SG Shields"):
				if instanceDict["SG Shields"].has_key("RaceShieldTech"):
					raceShieldTech = instanceDict["SG Shields"]["RaceShieldTech"]

			#TO-DO if ship has Anubis Shield and is labeled as superweapon, add an atmospheric listener of sorts so if it's at 20 units from the sun's surface, it nerfs shields to 40%
			if raceShieldTech == "Anubis Go'auld":
				if instanceDict["SG Shields"].has_key("Superweapon") and instanceDict["SG Shields"]["Superweapon"] == 1:
				
					global g_pAtmosCollisionCheckProcess
					if not (g_pAtmosCollisionCheckProcess):
						g_pAtmosCollisionCheckProcess = TempProcessWrapper("CollisionAtmosAlertCheck", 5.0, App.TimeSliceProcess.LOW)
					g_pAtmosCollisionCheckProcess.AddShip(pShip.GetObjID(), pShip, pInstance)

			if raceShieldTech != "Wraith": # Don't do this to Wraith vessels, they lack these
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
							#print "adding SG forcefield shield tech listeners to ship: ", pShip.GetName()
							pShields.TurnOn()
							pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
							pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")

							pShip.RemoveHandlerForInstance(App.ET_OBJECT_COLLISION, __name__ + ".CollisionHappened")
							pShip.AddPythonFuncHandlerForInstance(App.ET_OBJECT_COLLISION, __name__ + ".CollisionHappened")

							#pShip.RemoveHandlerForInstance(App.ET_SHIELD_COLLISION, __name__ + ".ShieldCollisionHappened")
							#pShip.AddPythonFuncHandlerForInstance(App.ET_SHIELD_COLLISION, __name__ + ".ShieldCollisionHappened")

							#pShip.RemoveHandlerForInstance(App.ET_PLANET_ATMOSPHERE_COLLISION, __name__ + ".AtmosCollisionHappened")
							#pShip.AddPythonFuncHandlerForInstance(App.ET_PLANET_ATMOSPHERE_COLLISION, __name__ + ".AtmosCollisionHappened")

							#pShip.RemoveHandlerForInstance(App.ET_PLANET_COLLISION, __name__ + ".PCollisionHappened")
							#pShip.AddPythonFuncHandlerForInstance(App.ET_PLANET_COLLISION, __name__ + ".PCollisionHappened")

							instanceDict["SG Shields Active"] = 1
							ActivateSGShieldCollisions(pShip, pInstance, instanceDict, 1, raceShieldTech, pShields)

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
			if instanceDict.has_key("SG Shields Active"):
				del instanceDict["SG Shields Active"]
			

		def EventInformation(self, pEvent):
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

			return fRadius, fDamage, kPoint

		def OnDefense(self, pShip, pInstance, oYield, pEvent, pTorp=None):
			debug(__name__ + ", OnDefense")

			global shieldPiercedThreshold, shieldGoodThreshold, defaultPassThroughDmgMult, vulnerableProjToSGShields, vulnerableBeamsToSGShields

			instanceDict = pInstance.__dict__
			fRadius, fDamage, kPoint = self.EventInformation(pEvent)

			raceShieldTech = None
			raceHullTech = None
			negateRegeneration = 0
			multFactor = 1.0

			# Extra shield config things
			if instanceDict.has_key("SG Shields"):
				if instanceDict["SG Shields"].has_key("RaceShieldTech"):
					raceShieldTech = instanceDict["SG Shields"]["RaceShieldTech"]

				if instanceDict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity and to not add too many fields.
					raceHullTech = instanceDict["SG Shields"]["RaceHullTech"]
				else:
					raceHullTech = raceShieldTech

			if raceShieldTech == "Asgard" or raceShieldTech == "Ori": # POINT 10. TO-DO Maybe check if we need to verify if the hull was hit, to avoid some shield facet issues
				negateRegeneration = -1
				if raceShieldTech == "Ori": # POINT 11 - this will make the Ori vessels impervious to low-grade shots, no more Death gliders lowering their shields willy-nilly
					negateRegeneration = negateRegeneration / 2.0 # TO-DO Make this customizable via basicconfiguration, this needs to be half of the value from the one below, or a new value
					multFactor = multFactor * 4 # TO-DO Make this customizable via basicconfiguration
				if oYield and hasattr(oYield, "IsSGPlasmaWeaponYield") and oYield.IsSGPlasmaWeaponYield() != 0: # Some support to POINT 10 when it comes to SG Plasma weapons
					if pTorp:
						mod = pTorp.GetModuleName()
						importedTorpInfo = __import__(mod)
						if hasattr(importedTorpInfo, "ShieldDmgMultiplier"):
							multFactor = multFactor * importedTorpInfo.ShieldDmgMultiplier()

			shieldsArePierced, nearestPoint = shieldRecalculationAndBroken(pShip, kPoint, 0, shieldPiercedThreshold, 0, negateRegeneration, None, fDamage, multFactor)
			shieldsAreNotGood, nearestPoint = shieldInGoodCondition(pShip, kPoint, shieldGoodThreshold, 0, nearestPoint)

			if pEvent.IsHullHit():
				# POINT 8
				# While in theory this is handled by the "No damage through shields" option on DS9FX configuration we want to also check it manually because:
				# 1. - That is an option which can be turned on/off. Following POINT 8, we want to ensure that this no-dmg-through-shields behaviour happens regardless of the DS9FX option being active or inactive.
				# 2. - Sometimes the "No damage through shields", for one reason or another, does not properly cover when a ton of incoming fire is hitting a ship, or does not cover when a vessel presents a weird geometry. In STBC, some vessels' models (including SG) present certain geometry shapes that ensure there's bleedthrough even when shields are completely full, so we need to fix that ourselves!
				if not pTorp or not (pTorp.GetNetType() in torpsNetTypeThatCanPhase):
					# then we do the heal if shields are good TO-DO
					#print "valid type that cannot bypass shields"
					if not shieldsAreNotGood:
						#print "shields are good enough to block the damage, reverting it"
						theHull = pShip.GetHull()
						hullName = None
						if theHull:
							hullName = theHull.GetName()
						hullCounted = 0
						kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
						while (1):
							pSys = pShip.GetNextSubsystemMatch(kIterator)
							if not pSys:
								break

							#print pSys.GetName()

							# The method above does not cover the children, funnily enough. We need to cover subsystems personally
							# However, for SG shields this is fine, after all while they have taken no hull damage, we have still seen cases where with shields near to max, the Asgard Weapons or the power conduits linked to them suffered damage from the hit causing an overload (POINT 8). 
							# But if you want for the shields to cover everything, just expand and uncomment the section below
							#for i in range(pSys.GetNumChildSubsystems()):
							#	pChild = pSys.GetChildSubsystem(i)
								
							iCon = pSys.GetCondition()
							iMax = pSys.GetMaxCondition()

							if iCon <= 0.0 or iCon >= iMax or not pSys.IsTargetable(): # TO-DO remove the iCon <= 0.0 if this does not list destroyed subsystems
								continue

							pSysPos = pSys.GetPosition()

							vDistance = App.TGPoint3()
							vDistance.SetXYZ(pSysPos.x, pSysPos.y, pSysPos.z)
							vDistance.Subtract(kPoint)

							if vDistance.Length() > (pSys.GetRadius() + fRadius):
								continue

							iNewCon = iCon + fDamage

							if iNewCon > iMax:
								iNewCon = iMax

							pSys.SetCondition(iNewCon)
			
							if pSys.GetName() == hullName:
								hullNotCounted = hullNotCounted + 1

	

						pShip.EndGetSubsystemMatch(kIterator)

						if theHull != None and hullCounted <= 0:
							#print "hull was not counted... well we will count it anyways"
							iCon = theHull.GetCondition()
							iMax = theHull.GetMaxCondition()

							iNewCon = iCon + fDamage

							if iNewCon > iMax:
								iNewCon = iMax

							theHull.SetCondition(iNewCon)

							
				else:
					print "TO-DO 1"
				# TO-DO CERTAIN SG SHIELD ARMOURS MAY DO SOMETHING, IDK
				

			else:
				# First check, special Asgard or
				#First check, those weapons that can pass-through
				print "TO-DO 2"

			pShields = pShip.GetShields()

			if pShields:
				print "TO-DO 3"

			if oYield and hasattr(oYield, "IsPhasedPolaronYield") and oYield.IsPhasedPolaronYield() != 0 and pInstance and pInstance.__dict__.has_key('SG Shields'): # POINT 9.
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
			# print 'Attaching Multivectral to', pInstance, pInstance.__dict__

		# def Activate(self):
		# 	FoundationTech.oWeaponHit.Start()
		# def Deactivate(self):
		# 	FoundationTech.oWeaponHit.Stop()

	oSGShields = SGShieldsDef('SG Shields')
	# print 'SG Shields loaded'

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"
	traceback.print_exc()