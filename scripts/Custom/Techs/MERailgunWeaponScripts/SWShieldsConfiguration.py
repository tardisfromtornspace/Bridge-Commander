# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MEPlasmaWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MEPlasmaWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by ME Railgun Weapons.
# The reason we make a tech for this, is because SG Shields behave differently from ST, SW shields or B5 defences against a Railgun Weapon.
# On this case, SG shields are supreme on blocking colliding objects regardless of speed, so shield damage should be reduced.

# On this case, more info about SG shields will be reviewed on the SG Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

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


RailgunSWShieldDamageMultiplier = 5.0

## Some SG-related resistances - unless there's a new Stargate franchise adding more races and spaceship combat, these should do the job
## Adding Asgard and Ori here, because the Asgard used neutronium on their vessel alloys, and for most of them the Plasma cannons were primitive enough that Asgard shields could handle them easier (excluding Anubis-grade ones)
## The Ori just because they may have some random ascended-knowledge thing going on, and as a way to reduce damage bleedthrough in certain models mod-wise.
xAsgardShieldMultiplier = 0.75
xAsgardHullMultiplier = 0.8
xAnubisShieldMultiplier = 0.9
xAlteranShieldMultiplier = 0.8
xAlteranHullMultiplier = 1.0
xOriShieldMultiplier = 0.4
xOriHullMultiplier = 0.95


##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstancedict and pInstancedict.has_key("SW Shields") or sShipScript in lSWVulnerableLegacyList:
		wasChanged = wasChanged + 1
		global RailgunSWShieldDamageMultiplier

		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()

		if hasattr(importedTorpInfo, "GetLaunchSpeed") and importedTorpInfo.GetLaunchSpeed() <= 5:
			shouldPassThrough = shouldPassThrough + 1

		shieldDamageMultiplier = shieldDamageMultiplier * RailgunSWShieldDamageMultiplier
		considerPiercing = 1


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged