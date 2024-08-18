# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGIonWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGIonWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by SG Ion Weapons.
# The reason we make a tech for this, is because SG Shields behave differently from ST, SW shields or B5 defences against an Ion Weapon.
# And even between SG shields, some behave differently:
# Early Go'auld shields could not handle Tollan nor Asgard Ion Guns - two shots from the Tollan guns shredded a single Ha'tak, bypassing the shield. The only way it makes sense for Anubis-grade shields to shrug an entire planetary defense grid of those while still being vulnerable to 3-6 unupgraded Ha'taks is for the shields to be more advanced to block this Ion weapon, and not only because of being stronger. Else we end up with a Ha'tak having 100 times more shields than normal, and if that was true, Anubis could have destroyed the other System Lords with a single Ha'tak, no superweapon needed.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info
IonSGShieldDamageMultiplier = 10.0 # TO-DO ADJUST ALL THE SG SHIPS THAT HAVE SHIELDS TO ADD THIS TECH

## Because some SG shields could not block Ion Cannons (see more information below)
IonSGVulnerableShields = ["Go'auld"] # This excludes "Anubis Go'auld"

## Some SG-related resistances - unless there's a new Stargate franchise adding more races and spaceship combat, these should do the job
xAnubisShieldMultiplier = 0.75
xAsgardShieldMuliplier = 0.8
xAlteranShieldMultiplier = 0.71
xOriShieldMultiplier = 0.7

def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstancedict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		global IonSGShieldDamageMultiplier, xAnubisShieldMultiplier, xAsgardShieldMuliplier, xAlteranShieldMultiplier, xOriShieldMultiplier
		shieldDamageMultiplier = shieldDamageMultiplier + IonSGShieldDamageMultiplier
		shouldDealAllFacetDamage = 0
		considerPiercing = considerPiercing + 1
		if pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech in IonSGVulnerableShields:
				shouldPassThrough = 1
			elif RaceShieldTech == "Anubis Go'auld": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xAnubisShieldMultiplier
			elif RaceShieldTech == "Asgard": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldMuliplier
			elif RaceShieldTech == "Alteran" or RaceShieldTech == "Lantian" or RaceShieldTech == "Lantean" or RaceShieldTech == "Asuran": # Resistances, not including actual Replicator ships here because those will have their own tech
				shieldDamageMultiplier = shieldDamageMultiplier * xAlteranShieldMultiplier
			elif RaceShieldTech == "Ori": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xOriShieldMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

