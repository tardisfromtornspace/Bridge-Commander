# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
###############################################################################################
# A modfication of a modification, last modification by Alex SL Gato (CharaToLoki)
# TO-DO UPDATE THE README
# ###############3 BIG TO-DO RENAME THINGS ################
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# At the bottom of your torpedo projectile file add this (Between the """ and """):
# Note, your SpeciesToTorp value must be set to PHASEDPLASAMA for it to work
# pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)
"""
try:
	modSGIonWeaponTorp = __import__("Custom.Techs.SGIonWeapon")
	if(modSGIonWeaponTorp):
		modSGIonWeaponTorp.oSGIonWeaponTorp.AddTorpedo(__name__)
except:
	print "SGIonWeapon projectile script not installed, or you are missing Foundation Tech"
"""
# You can also add your ship to an immunity list, not only the one below, in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
# Also please note the value here has meaning:
# "0" means hull immunity only
# "1" means shield immunity only
# "2" means both shield and hull immunity
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"SG Ion Weapon Immune": 1
}
"""

import App

from bcdebug import debug
import traceback
import nt
import string

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.02",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }
# A. GENERAL BASIC CONFIGURATION
# Some generic info that would affect mostly everyone
IonHullDamageMultiplier = 10.0

# At the moment I cannot really think of one ship immune to both effects in particular legacy-wise... adding this Dummy
global lImmuneSGIonWeaponShips
lImmuneSGIonWeaponShips = []

# For every other ship (because since STBC is a ST game, the shields in-game behave more like ST shields, specifically simplified 24th century Post-Dominion War Federation ones, so we must take them as a base), excluding the examples mentioned below, this weapon causes a shield drain in each shield facet equivalent to the projectile damage received. If the hull is hit, it will deal 10 times the damage the normal projectile does.
IonGenericShieldDamageMultiplier = 2 # one from the normal shot, another from us

# "variableNames" is a global dictionary, filled automatically by the files in scripts/Custom/Techs/SGIonWeaponScripts 
# TO-DO UPDATE THIS README PROPERLY
# the purpose of this list is to append dicts f.ex. {"legacyImmunity": alist, "interactionHullBehaviour": functionObtained, "interactionShieldBehaviour": anotherfunctionObtained}
# the "legacyImmunity" field is there only to add some ships on a legacy list to fully immune to all effects of this weapon to hull and shields.
# the "interactionHullBehaviour" will have a function that will be called to calculate the damage reduction or amplification to the hull, those functions are meant to be stacked.
# the "interactionShieldBehaviour" will try to do the same, but for shields. On this case, due to certain franchise differences, while some effects will be stacked, it is recommended to only add one of a type, or create a hybrid function if you want multiple of these to be added (f.ex one function could tell the script that they can bypass always, while another says they cannot bypass).

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

	dir="scripts\\Custom\\Techs\\SGIonWeaponScripts" # I want to limit any vulnerability as much as I can while keeping functionality
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

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["legacyImmunity", "interactionShieldBehaviour", "interactionHullBehaviour"])
					except:
						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["IonHullDamageMultiplier", "IonGenericShieldDamageMultiplier"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals())
					
					if hasattr(banana, "legacyImmunity"): # These will not be affected at all by the hull or shield effects, period
						global lImmuneSGIonWeaponShips
						for item in banana.legacyImmunity:
							lImmuneSGIonWeaponShips.append(item)

					if hasattr(banana, "interactionShieldBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionShieldBehaviour"] = banana.interactionShieldBehaviour

					if hasattr(banana, "interactionHullBehaviour"):
						if not variableNames.has_key(fileName):
							variableNames[fileName] =  {}
						variableNames[fileName]["interactionHullBehaviour"] = banana.interactionHullBehaviour

					if fileName == "BasicSGIonWeaponConfiguration" and hasattr(banana, "IonHullDamageMultiplier"):
						global IonHullDamageMultiplier
						IonHullDamageMultiplier = banana.IonHullDamageMultiplier

					if fileName == "BasicSGIonWeaponConfiguration" and hasattr(banana, "IonGenericShieldDamageMultiplier"):
						global IonGenericShieldDamageMultiplier
						IonGenericShieldDamageMultiplier = banana.IonGenericShieldDamageMultiplier

					#print "SGIonWeapon reviewing of this subtech is a success"
			except:
				print "someone attempted to add more than they should to the SGIonWeapon script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print IonHullDamageMultiplier, IonGenericShieldDamageMultiplier
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

		if detectCollison != None: # We want to detect collision first TO-DO or maybe nerf the speed?
			pTorp.DetectCollision(detectCollison)
			pTorp.UpdateNodeOnly()

		# Give the torpedo an appropriate speed.
		kSpeed = CopyVector(kVector)
		kSpeed.Unitize()
		kSpeed.Scale(fSpeed)
		pTorp.SetVelocity(kSpeed)

		return pTorp

	class SGIonWeaponTorpedo(FoundationTech.TechDef):
		def __init__(self, name, dict = {}):
			FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
			self.lYields = []
			self.__dict__.update(dict)
			self.lFired = []

		def IsSGIonWeaponYield(self):
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
			if pShields and not pShields.IsDisabled():
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
			#TO-DO clean dried lava
			if not pShip:
				return

			sScript     = pShip.GetScript()
			sShipScript = string.split(sScript, ".")[-1]

			global lImmuneSGIonWeaponShips # This legacy list goes first - it is to reduce unnecessary calculations
			if sShipScript in lImmuneSGIonWeaponShips:
				return

			global torpsNetTypeThatCanPhase, variableNames
			fRadius, fDamage, kPoint = self.EventInformation(pEvent)

			pHitPoint = ConvertPointNiToTG(pTorp.GetWorldLocation())
			pVec = pTorp.GetVelocityTG()
			pVec.Scale(0.001)
			pHitPoint.Add(pVec)

			global IonHullDamageMultiplier, defenceGridMultiplier, hullPolarizerMultiplier, shadowDispersiveHullMultiplier
			hullDamageMultiplier = IonHullDamageMultiplier -1 # This represents the extra damage, so if something deals 2 times the damage to a shield facet or the hull, we only add that extra damage once, as the first time was already added normally.
			shieldDamageMultiplier = -1
			shouldPassThrough = 0
			considerPiercing = 0
			shouldDealAllFacetDamage = 0

			pInstancedict = pInstance.__dict__
			try:
				attackerID = pTorp.GetParentID()
			except:
				attackerID = App.NULL_ID

			if(pEvent.IsHullHit()):
				if pInstancedict.has_key('SG Ion Weapon Immune') and (pInstancedict['SG Ion Weapon Immune'] == 0 or pInstancedict['SG Ion Weapon Immune'] > 1):
					return
				wasHullChanged = 0
				for item in variableNames.keys():
					if variableNames[item].has_key("interactionHullBehaviour"): # These are reserved for when the hull has been hit! These are meant to be accumulative, for defenses.
						hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasHullChanged = variableNames[item]["interactionHullBehaviour"](pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, attackerID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasHullChanged)

				finalHullDamage = fDamage * hullDamageMultiplier

				# OPTION 2: IMPORT A DUMMY TORP, give it the damage radious factor and damage we have, and make it invisible. Pros compared with option 1 (manually dealing extra damage ourselves), Armours and special armour techs work better. Cons, point defence script might work twice and manage to shot it down (extremely unlikely, but not necessarily impossible).
				mod = "Tactical.Projectiles.ExtraPhasedDamageDummy" 
				try:
					pTempTorp = FireTorpFromPointWithVectorAndNetType(pTorp.GetWorldLocation(), pVec, mod, pShip.GetObjID(), attackerID, __import__(mod).GetLaunchSpeed(), torpsNetTypeThatCanPhase, finalHullDamage, pTorp.GetDamageRadiusFactor(), 1, pShip)
					#pTempTorp.SetLifetime(15.0)
					# MAYBE THIS PART BELOW IS NOT NECESSARY? TO-DO			
				except:
					print "You are missing 'Tactical.Projectiles.ExtraPhasedDamageDummy' torpedo on your install, without that the SG Ion Weapons here cannot deal extra hull damage... or another error happened"
					traceback.print_exc()

				return

			# Now we are doing shield stuff calculations
			# First, what kind of shield tech we have here?
			if pInstancedict.has_key('SG Ion Weapon Immune') and pInstancedict['SG Ion Weapon Immune'] > 0:
				return

			global lSWVulnerableLegacyList, IonB5LegacyShieldDamageMultiplier

			wasShieldChanged = 0
			for item in variableNames.keys():
				if variableNames[item].has_key("interactionShieldBehaviour"): # These are reserved for when the shield has been hit! Also be careful, since these are more likely to stack weaknesses! Preferable to only have one of this type per ship
					hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasShieldChanged = variableNames[item]["interactionShieldBehaviour"](pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, attackerID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasShieldChanged)

			if wasShieldChanged <= 0:
				# normal shields, we generate a slight generic shield drain
				global IonGenericShieldDamageMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier + IonGenericShieldDamageMultiplier
				shouldDealAllFacetDamage = 1
					
			finalShieldDamage = fDamage * shieldDamageMultiplier

			# Ok first we look for the nearest shield to the impact, drain the shields accordingly, and evaluate if the shield is broken
			shieldBroken = self.shieldRecalculationAndBroken(pShip, kPoint, -finalShieldDamage, 0.25, shouldDealAllFacetDamage)
			if considerPiercing != 0 and shouldPassThrough == 0:
				shouldPassThrough = shieldBroken
			
			if shouldPassThrough > 0: # If this weapon has not hit the hull already and meets the requirements, this weapon will "bypass" the shields then (actually it creates a short-lived clone or subTorp clone after the shield)
				mod = pTorp.GetModuleName()
				if(self.__dict__.has_key("SubTorp")):
					mod = self.SubTorp

				pTempTorp = FireTorpFromPointWithVectorAndNetType(pHitPoint, pVec, mod, pTorp.GetTargetID(), attackerID, __import__(mod).GetLaunchSpeed(), torpsNetTypeThatCanPhase, fDamage, pTorp.GetDamageRadiusFactor())

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

	oSGIonWeaponTorp = SGIonWeaponTorpedo("SGIonWeapon Torpedo")
	# Just a few standard torps I know of that are SGIonWeapon... 
	# All of these will also be added on the projectile script
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonCannon")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonCannon2")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonCannon3")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonCannon4")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonPulse")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonPulse2")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonPulse3")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonPulse4")
	oSGIonWeaponTorp.AddTorpedo("Tactical.Projectiles.IonPulse5")

except:
	print "FoundationTech, or the FTB mod, or both are not installed, \nTrasphasic Torpedoes are there but NOT enabled or present in your current BC installation"
	traceback.print_exc()

class SGIonWeaponDef(FoundationTech.TechDef):

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		self.OnProjectileDefense(pShip, pInstance, pTorp, oYield, pEvent)

	def OnProjectileDefense(self, pShip, pInstance, pTorp, oYield, pEvent): # TO-DO VERIFY THIS WORKS DONE THIS WAY
		if oYield and hasattr(oYield, "IsSGIonWeaponYield") and oYield.IsSGIonWeaponYield() != 0:
			return 1

	def Attach(self, pInstance):
		pInstance.lTorpDefense.append(self)
		pInstance.lPulseDefense.insert(self)


oSGIonWeaponImmunity = SGIonWeaponDef('SG Ion Weapon Immune')