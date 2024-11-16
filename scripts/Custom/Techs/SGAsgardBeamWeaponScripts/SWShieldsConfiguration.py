# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.1
# Meant to be used alongside the SGAsgardBeamWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGAsgardBeamWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SW shielding is affected by SG Asgard Beam Weapons.
# On this case, this one was left for future expansions and to clarify SW shields are not ST or SG ones, and that a Plasma Beam weapon may affect some systems a bit.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

IonSWShieldDamageMultiplier = 1.0
IonSWHullDamageMultiplier = 0.91 # range 0-1

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


def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	global lSWVulnerableLegacyList
	if (pTargetInstance and pTargetInstanceDict.has_key("SW Shields")) or sShipScript in lSWVulnerableLegacyList: # SW shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1
		shieldDamageMultiplier = shieldDamageMultiplier * IonSWShieldDamageMultiplier


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged

def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	global lSWVulnerableLegacyList
	if (pTargetInstance and pTargetInstanceDict.has_key("SW Shields")) or sShipScript in lSWVulnerableLegacyList: # SW shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1

		global IonSWHullDamageMultiplier
		# We reduce the damage... but your power plant gets damaged! Be careful or too many Ions may make you explode!
		pPower = pTarget.GetPowerSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - IonSWHullDamageMultiplier) * pEvent.GetDamage()
			#print "myDamage = ", myDamage
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		hullDamageMultiplier = hullDamageMultiplier * IonSWHullDamageMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged

