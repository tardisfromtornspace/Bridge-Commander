# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGIonWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGIonWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SW shielding is affected by SG Ion Weapons.
# The reason we make a tech for this, is because SW Shields behave differently from ST, SG shields or B5 defences against an Ion Weapon.
# For Star Wars it is pretty obvious, their shields and equipment are extremely weak against Ion Weapons in general - in fact, Ion Weapons on SW are used as disabler weapons, a-la-ST Breen Drainer. Because Asgard Ion Weapons are more damage-dealing, a middle-ground has been reached - they deal extra damage to SW shields overall, but if the shields were down, it won't cause any EMP-Fried systems effect, just the normal SG Ion cannon punch boost Basic Configuration provides, and slight damage to the Power plant.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

IonSWShieldDamageMultiplier = 30.0
IonSWHullDamageMultiplier = 0.7 # range 0-1

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


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	global lSWVulnerableLegacyList
	if pInstance and pInstancedict.has_key("SW Shields") or sShipScript in lSWVulnerableLegacyList: # SW shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1
		global IonSWShieldDamageMultiplier
		shieldDamageMultiplier = shieldDamageMultiplier + IonSWShieldDamageMultiplier
		shouldDealAllFacetDamage = shouldDealAllFacetDamage + 1
		considerPiercing = 0
		negateRegeneration = negateRegeneration + 1


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration

def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	global lSWVulnerableLegacyList
	if pInstance and pInstancedict.has_key("SW Shields") or sShipScript in lSWVulnerableLegacyList: # SW shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1

		global IonSWHullDamageMultiplier
		# We reduce the damage... but your power plant gets damaged! Be careful or too many Ions may make you explode!
		pPower = pShip.GetPowerSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - IonSWHullDamageMultiplier) * pTorp.GetDamage()
			print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		hullDamageMultiplier = hullDamageMultiplier * IonSWHullDamageMultiplier
		negateRegeneration = negateRegeneration + 1

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration

