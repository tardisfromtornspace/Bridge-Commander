# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 20th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGPlasmaWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGPlasmaWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SW shielding is affected by SG Plasma Weapons.
# The reason we make a tech for this, is because SW Shields behave differently from ST, SG shields or B5 defences against a Plasma Weapon.
# For Star Wars, plasma weapons are mostly used as disablers or exotic weapons that deal a gradual drain to the shields overtime, albeit less powerful than Ion weaponry. Since Go'auld weapons deal more of a punch, a compromise has been reached where they deal some effects.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

PlasmaSWShieldDamageMultiplier = 10.0
PlasmaSWHullDamageMultiplierBoost = 1.5
PlasmaSWHullDamageMultiplier = 0.8 # range 0-1

### Since the "SW Shields" tech does not exist for the public, no mods at the time of release have it, so we must ensure for legacy reasons that those old SW mod vessels are still picked up #### TO-DO COMPLETE THIS LIST ####
global lSWVulnerableLegacyList 
lSWVulnerableLegacyList = (
                "aaAssaultFrigate",
                "aaBulkCruiser",
                "aaBulkFreighter",
                "aaCarrack",
                "aaCorevette",
                "aaCorgun",
                "aaDreadnaught",
                "aaEscortCarrier",
                "aaInterdictor",
                "aaLancerFrigate",
                "aaMaurauderCorvette",
                "aaMobquet",
                "aaModcorvette",
                "aaModifiedNebulonB",
                "aaModularConveyor",
                "aaNebulonB",
                "aaStarGalleon",
                "aaStrikeCruiser",
                "aaSuprosa",
                "aaXiytiar",
                "Awing",
                "Bwing",
                "droidfighter",
                "Executor",
                "EWing",
                "Imperator",
                "ImperatorI",
                "ImperatorII",
                "ImperatorIII",
                "ISD",
                "ISS",
                "Millenium",
                "naboofighter",
                "SLAVE1",
                "TIEav",
                "TIEb",
                "TIEd",
                "TIEde",
                "TIEexM1",
                "TIEexM2",
                "TIEexM3",
                "TIEexM4",
                "TIEexM5",
                "TIEf",
                "TIEgt",
                "TIEi",
                "TIEph",
                "TIErc",
                "TIErpt",
                "TIEX1",
                "TWing",
                "venator",
                "venatorII",
                "venimp",
                "vicstar",
                "XWing",
                "YWing",
                "ZWing",
                "Z95",
                )


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global lSWVulnerableLegacyList
	if (pInstancedict and pInstancedict.has_key("SW Shields")) or sShipScript in lSWVulnerableLegacyList:
		global PlasmaSWShieldDamageMultiplier, PlasmaSWHullDamageMultiplier
		wasChanged = wasChanged + 1
		shouldDealAllFacetDamage = shouldDealAllFacetDamage + 1
		considerPiercing = considerPiercing + 1

		shieldDamageMultiplier = shieldDamageMultiplier * PlasmaSWShieldDamageMultiplier

		if pPower:
			print "SW POWER DAMAGE"
			myDamage = -hullDamageMultiplier * (1 - PlasmaSWHullDamageMultiplier) * pTorp.GetDamage()
			print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global lSWVulnerableLegacyList
	if (pInstancedict and pInstancedict.has_key("SW Shields")) or sShipScript in lSWVulnerableLegacyList:
		wasChanged = wasChanged + 1

		global PlasmaSWHullDamageMultiplier, PlasmaSWHullDamageMultiplierBoost
		# We reduce the damage... but your power plant gets damaged! Be careful!
		pPower = pShip.GetPowerSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - PlasmaSWHullDamageMultiplier) * pTorp.GetDamage() * PlasmaSWHullDamageMultiplierBoost
			print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		hullDamageMultiplier = hullDamageMultiplier * PlasmaSWHullDamageMultiplier * PlasmaSWHullDamageMultiplierBoost

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

