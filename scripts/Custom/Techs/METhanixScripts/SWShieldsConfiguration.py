# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the METhanixMagneticHydrodynamicCannon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/METhanixScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SW shielding is affected by ME Thanix Weapons.
# On this case, this one was left for future expansions and to clarify SW shields are not ST or SG ones, and that a very long object going at a very fast speed could definetely do a lot of shield damage, but reduced hull damage

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

ThanixSWShieldDamageMultiplier = 3.0
ThanixSWHullDamageMultiplier = 0.25

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


def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	global lSWVulnerableLegacyList
	if (pTargetInstance and pTargetInstanceDict.has_key("SW Shields")) or sShipScript in lSWVulnerableLegacyList:
		wasChanged = wasChanged + 1
		shieldDamageMultiplier = shieldDamageMultiplier * ThanixSWShieldDamageMultiplier
		if pTargetInstanceDict["SW Shields"].has_key("EclipseRamReduction"):
			shieldDamageMultiplier = shieldDamageMultiplier * pTargetInstanceDict["SW Shields"]["EclipseRamReduction"]
			


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	global lSWVulnerableLegacyList
	if (pTargetInstance and pTargetInstanceDict.has_key("SW Shields")) or sShipScript in lSWVulnerableLegacyList: # SW shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1

		global ThanixSWHullDamageMultiplier
		hullDamageMultiplier = hullDamageMultiplier * ThanixSWHullDamageMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

