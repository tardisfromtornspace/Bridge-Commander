# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGIonWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGIonWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how Gene Rodenberry's Andromeda defences are affected by SG Ion Weapons.
# Gene Rodenberry's Andromeda - between the fact that lore-wise Andromeda has no energy shields except for a crazed scientist working under the Abyss; and that mod-wise the latest Andromeda mod already has alternatives of defense against these weapons such as Simulated Point Defense, and that for certain vessels a semblance of a shield was kept for imitating certain effects such as the gravity distortion field, we must guarantee that some Ion Weapons can still surpass that token shield threshold in some way to work as intended for certain vessels.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

global IonGRALegacyShieldDamageMultiplier
IonGRALegacyShieldDamageMultiplier = 2.0

### Some ships that from legacy reasons are extra vulnerable to this weapon in some way - this is a list of ship mods that I know existed from years ago, but were not necessarily released.
global lGRAVulnerableLegacyList 
lGRAVulnerableLegacyList = (
                "AndArchlike",
                "Andromeda",
                "Andromada",
                "AndromedaBattleForm",
                "AndSlipFighter",
                "AndSlipFighterMK1",
                "AndSlipFighterMK2",
                "AndSlipFighterMK3",
                "CrimsonSunrise",
                "EurekaMeru",
                "EurekaMaru",
                "HalcyonPromise",
                "ResolutionOfHector",
                "BalanceOfJudgement",
                "PaxMagellanic",
                )


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	if pInstance and pInstancedict.has_key('Reflector Shields') or pInstancedict.has_key('Reflector') or pInstancedict.has_key('Corbonite Reflector') and sShipScript in lGRAVulnerableLegacyList: # These ones will not add a "wasChanged", we want the normal to stack with this effect
		shieldDamageMultiplier = shieldDamageMultiplier + IonGRALegacyShieldDamageMultiplier
		negateRegeneration = negateRegeneration - 1

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration