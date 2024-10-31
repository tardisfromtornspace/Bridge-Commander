# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 31st October 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGRailgunWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGRailgunWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how ME shielding is affected by SG Railgun Weapons.
# The reason we make a tech for this, is because ME tech would work by blocking the projectile entirely from hitting, so shield drain needs to be considered.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

RailgunMEShieldDamageMultiplier = 1.0
RailgunMEHullDamageMultiplierBoost = 1.0
RailgunMEHullDamageMultiplier = 1.0 # range 0-1

### Since the "ME Shields" tech does not exist for the public, no mods at the time of release have it, so we must ensure for legacy reasons that those old ME mod vessels are still picked up #### TO-DO COMPLETE THIS LIST ####
global lMEVulnerableLegacyList 
lMEVulnerableLegacyList = (
                "MENormandy",
                "SSVNormandy",
                "MEDestinyAscension",
                "MENazara",
                "MEHarbinger",
                )


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global lMEVulnerableLegacyList
	if (pInstancedict and pInstancedict.has_key("ME Shields")) or sShipScript in lMEVulnerableLegacyList:
		global RailgunMEShieldDamageMultiplier, RailgunMEHullDamageMultiplier
		wasChanged = wasChanged + 1
		considerPiercing = considerPiercing + 1

		shieldDamageMultiplier = shieldDamageMultiplier +  hullDamageMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged