# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGPlasmaWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGPlasmaWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how ME shielding is affected by SG Ion Weapons.
# The reason we make a tech for this, is because ME Shields behave differently from ST, SG shields or B5 defences against an Ion Weapon.
# For ME is a bit hazy, but it is known that weapons with a lot of electric charge can overlod a mass effect shield. For this I've decided to make them cause at least twice the damage like a heavy ME overload and consider shield piercing. As for any EMP effect, ME Ships tend to deal with electric charges a lot, so I would not see that much of a difference except maybe destabilizing the storage of excess charge.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

PlasmaMEShieldDamageMultiplier = 12.0
PlasmaMEHullDamageMultiplierBoost = 4.0
PlasmaMEHullDamageMultiplier = 0.9


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global lMEVulnerableLegacyList
	if (pInstancedict and pInstancedict.has_key("ME Shields")):
		global PlasmaMEShieldDamageMultiplier, PlasmaMEHullDamageMultiplier
		wasChanged = wasChanged + 1
		shouldDealAllFacetDamage = shouldDealAllFacetDamage + 1
		considerPiercing = considerPiercing + 1

		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()

		shieldDamageMultiplier = shieldDamageMultiplier * PlasmaMEShieldDamageMultiplier

		pPower = pShip.GetShields()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - PlasmaMEHullDamageMultiplier) * pTorp.GetDamage()
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global lMEVulnerableLegacyList
	if (pInstancedict and pInstancedict.has_key("ME Shields")):
		wasChanged = wasChanged + 1

		global PlasmaMEHullDamageMultiplier, PlasmaMEHullDamageMultiplierBoost

		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		myHullMult = PlasmaMEHullDamageMultiplierBoost
		if hasattr(importedTorpInfo, "HullDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			myHullMult = importedTorpInfo.HullDmgMultiplier()

		hullDamageMultiplier = hullDamageMultiplier * PlasmaMEHullDamageMultiplier * myHullMult

		# We reduce the damage... but your power plant gets damaged! Be careful!
		pPower = pShip.GetPowerSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - PlasmaMEHullDamageMultiplier) * pTorp.GetDamage() * myHullMult
			#print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		pPower = pShip.GetWarpEngineSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - PlasmaMEHullDamageMultiplier) * pTorp.GetDamage() * myHullMult
			#print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		pPower = pShip.GetShields()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - PlasmaMEHullDamageMultiplier) * pTorp.GetDamage() * myHullMult
			#print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		pPower = pShip.GetCloakingSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - PlasmaMEHullDamageMultiplier) * pTorp.GetDamage() * myHullMult
			#print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

