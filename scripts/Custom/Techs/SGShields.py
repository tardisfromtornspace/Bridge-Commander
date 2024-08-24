#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         SGShields.py by Alex SL Gato
#         24th August 2024
#         Based strongly on Shields.py by the FoundationTechnologies team, ATPFunctions by Apollo, and SGGIonWeapon by Alex SL Gato.
#################################################################################################################
# This technology encompasses most of SG defences in a generic way, mostly for tagging, but also for referencing common shield protection strengths and weaknesses over standard STBC shields.
# Here are the main differences regarding strengths and weaknesses of SG Shields (in comparision with STBC shields, which are supposed to be an in-game simplified version of early post-Dominion War ST Federation shielding):
# * POINT 1: Excluding ST metaphasic shields and some trinesium-based hulls, SG Shields can withstand being inside a star's corona for quite a while longer than regular ST Federation shielding (and better than the Borg, at least, TNG Borg), capable of avoiding the radiation from leaking inside the vessel for a while.
# * POINT 2: While both ST Federation shielding and SG shields can do it, SG shields are often stronger when blocking an incoming physical object from colliding, with their shield bubbles at least.
# * POINT 3: SG Shields cannot usually block dimensional effects, such as certain dimensional disruptions like event horizons, wormholes or black holes. ST shields (at least, Federation, Klingon and Romulan ones) hold a bit better against those, with containment fields specifically built for holding micro-singularities and even those dissipating against polarized hull plating (ok that last statement is ridiculous, but it is what is mentioned in Memory Alpha).
# * POINT 4: Overall, SG shields, at least Go'auld and above, are stronger against strong impacts, but also seem to have some weaknesses towards lower-powered ones... or at least, they are strong against radiation and nuclear blasts but have some weakness to concentrated plasma bolts, even small (those are the only way to explain why a >1000 Megaton Nuke had no effect on a Go'auld vessel with shields up while a few Death Gliders can drain a Go'auld shields a bit with their shots, if we don't count possible plot armor).
# * POINT 5: Regarding Federation shielding, Plasma is quite a varied matter - small bolts and plasma projectiles do nothing to their shields, but big advanced ones can pack quite a punch or even drill a hole on their shields (of course the latter example is taken from TOS Balance of Terror and SNW versions against primitive plasma torpedoes and advanced plasma torpedoes, with 23rd century Constitution-class shielding being far weaker and less advanced than a 24th century Galaxy-class shield, but the point still stands) - This has already been taken care of in the SGPlasmaWeaponScript.
# * POINT 6: If properly tweaked, a SG Shield can perfectly block a certain frequency or type of weapon with (almost) no shield drain, even if before they could not block them... at least for Alteran-based shields which seem to be based on the frequency-antifrequency principle to negate damage, compared with the same-frequency-can-pass of ST Federation shielding that is only supposed to allow a single set of frequencies to pass, but all the others are blocked "almost" perfectly.
# ** F.ex. traditional Go'auld shields cannot block an Ion Weapon, but upgraded Anubis ones can and also make them totally ineffective, while still only having shields a bit stronger overall. And talking about Ion Weapons...
# * POINT 7:  On SG, Ion Weapons work more as regular projectiles, lowering shields and then dealing hull damage, but with the twist that they deal a lot of Hull Damage, and standard Go'auld shields lack the ability to block them (for ST fans, Ion Weapons to a Go'auld shield are like a pre-Dominion-War Federation Galaxy-class shield against Phased Polaron Beams). Ion Weapons in ST work more as shield drainers - they rarely (if at all) lower all shields from one hit, requiring several even if they carry a kinetic charge, but they will definetely drain the shields and give problems to the shield regeneration. - This has already been taken care of in the SGIonWeaponScript.
# * POINT 8: excluding the exceptions from the other points, SG shields in general do not take as much hull bleedthrough damage when shields are at full strength, except on counted occasions. Mostly the damage they may receive when shields are still at full is more towards the power grids and similar, not to the hull proper, unless their shields cannot adapt.
# * POINT 9: Since SG shields and ST Federation shields work on different principles, it is very likely that Phased Polaron weapons would do nothing to SG shields.

# The following is not necessarily a point of difference between ST and SG shields, but it is important for our points to determine some SG Shields things to code:
# * POINT 10: Asgard Shields recover normally if a weapon hit is too-low yield, as if the weapon did not hit them.
# * POINT 11: Some Ori prior shields use the energy of the impacts to become stronger, albeit that was only seen on the Ori Beachhead shield which was far more powerful than an Ori Warship shield.

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
            "Version": "0.02",
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

	torpsNetTypeThatCanPhase = [Multiplayer.SpeciesToTorp.PHASEDPLASMA] # For the "torpedoes-going-through" issue
	defaultDummyNothing = "NaN"
	SlowDownRatio = 3.0/70.0 # This is an auxiliar value, it helps us for when a ship is too small, to prevent a torpedo from just teleporting to the other side

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
				#print "FoolTargeting script is reviewing " + fileName + " of dir " + dir
				if dExcludePlugins.has_key(fileName):
					debug(__name__ + ": Ignoring plugin" + fileName)
					continue

				try:
					if not variableNames.has_key(fileName):
						myGoodPlugin = dotPrefix + fileName

						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["legacyImmunity", "interactionShieldBehaviour", "interactionHullBehaviour"])
						except:
							try:
								banana = __import__(myGoodPlugin, globals(), locals(), ["defaultPassThroughDmgMult", "SlowDownRatio"])
							except:
								banana = __import__(myGoodPlugin, globals(), locals())
					
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

						print "SGShields reviewing of this file is a success"
				except:
					print "someone attempted to add more than they should to the SG Shields script"
					traceback.print_exc()

	LoadExtraLimitedPlugins()
	print vulnerableProjToSGShields
	print vulnerableBeamsToSGShields

	class SGShieldsDef(FoundationTech.TechDef):

		def EventInformation(self, pEvent):
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

			return fRadius, fDamage, kPoint

		def shieldRecalculationAndBroken(self, pShip, kPoint, extraDamageHeal, shieldThreshold = shieldPiercedThreshold, multifacet = 0, negateRegeneration=0, nearShields = None, damageSuffered = 0, multFactor = 1.0):

			pShields = pShip.GetShields()
			shieldHitBroken = 0
			shieldDirNearest = None
			if pShields and not (pShields.IsDisabled() or not pShields.IsOn()):
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

			return shieldHitBroken, shieldDirNearest

		def shieldInGoodCondition(self, pShip, kPoint, shieldThreshold = shieldPiercedThreshold, multifacet = 0, nearShields = None):

			pShields = pShip.GetShields()
			shieldHitBroken = 0
			shieldDirNearest = None
			if pShields and not (pShields.IsDisabled() or not pShields.IsOn()):
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
				
				pShieldsProperty = pShields.GetProperty()
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					if shieldDirNearest == shieldDir or multifacet != 0:
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						resultHeal = fCurr # TO-DO Add an extra value for Asgard shielding so it regenerates more if the damage was less than a certain threshold?
						if shieldDirNearest == shieldDir and (fMax <= 0 or resultHeal < (shieldThreshold * fMax)):
							shieldHitBroken = shieldHitBroken + 1
			else:
				shieldHitBroken = 1

			return shieldHitBroken, shieldDirNearest


		def OnDefense(self, pShip, pInstance, oYield, pEvent, pTorp=None):
			debug(__name__ + ", OnDefense")

			global shieldPiercedThreshold, shieldGoodThreshold, defaultPassThroughDmgMult, vulnerableProjToSGShields, vulnerableBeamsToSGShields
			#if oYield:
			#	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 	#		return

			pInstancedict = pInstance.__dict__
			fRadius, fDamage, kPoint = self.EventInformation(pEvent)

			raceShieldTech = None
			raceHullTech = None
			negateRegeneration = 0
			multFactor = 1.0

			# Extra shield config things
			if pInstancedict.has_key("SG Shields"):
				if pInstancedict["SG Shields"].has_key("RaceShieldTech"):
					raceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]

				if pInstancedict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity and to not add too many fields.
					raceHullTech = pInstancedict["SG Shields"]["RaceHullTech"]
				else:
					raceHullTech = raceShieldTech

			if raceShieldTech == "Asgard" or raceShieldTech == "Ori": # POINT 10. TO-DO Maybe check if we need to verify if the hull was hit, to avoid some shield facet issues
				negateRegeneration = -1
				if raceShieldTech == "Ori": # POINT 11 - this will make the Ori vessels impervious to low-grade shots, no more Death gliders lowering their shields willy-nilly
					negateRegeneration = negateRegeneration / 2.0
					multFactor = multFactor * 4
				if oYield and hasattr(oYield, "IsSGPlasmaWeaponYield") and oYield.IsSGPlasmaWeaponYield() != 0: # Some support to POINT 10 when it comes to SG Plasma weapons
					if pTorp:
						mod = pTorp.GetModuleName()
						importedTorpInfo = __import__(mod)
						if hasattr(importedTorpInfo, "ShieldDmgMultiplier"):
							multFactor = multFactor * importedTorpInfo.ShieldDmgMultiplier()

			shieldsArePierced, nearestPoint = self.shieldRecalculationAndBroken(pShip, kPoint, 0, shieldPiercedThreshold, 0, negateRegeneration, None, fDamage, multFactor)
			shieldsAreNotGood, nearestPoint = self.shieldInGoodCondition(pShip, kPoint, shieldGoodThreshold, 0, nearestPoint)

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















