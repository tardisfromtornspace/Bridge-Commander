# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGPlasmaWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGPlasmaWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by SG Plasma Weapons.
# The reason we make a tech for this, is because SG Shields behave differently from ST, SW shields or B5 defences against a Plasma Weapon.
# On this case, the tech is here to adjust to the fact why a >1000 megaton naquadah-enhanced nuclear bomb dealt no visible damage to an Early Ha'tak Go'auld shields, yet a few bolts from a Death Glider (which has far less firepower than that bomb) could affect a Ha'tak shield.

# On this case, more info about SG shields will be reviewed on their main SG Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info

PlasmaSGVulnerableShields = [] # No actual SG vessel is vulnerable to Go'auld Plasma cannons in the way the Go'auld were to Tollan or Asgard Ion ones. Just leaving this here in case someone randomly wants to add that for a fanmade ship or something
PlasmaSGShieldDamageMultiplier = 4.0

## Some SG-related resistances - unless there's a new Stargate franchise adding more races and spaceship combat, these should do the job
## Adding Asgard and Ori here, because the Asgard used neutronium on their vessel alloys, and for most of them the Plasma cannons were primitive enough that Asgard shields could handle them easier (excluding Anubis-grade ones)
## The Ori just because they may have some random ascended-knowledge thing going on, and as a way to reduce damage bleedthrough in certain models mod-wise.
xAsgardShieldMuliplier = 0.75
xAnubisShieldMultiplier = 0.7 # Seems fair that when Anubis upgraded his shields, it also made them more resistant to the mainstream weapons the Go'auld use
xAsgardHullMuliplier = 0.8
xAlteranShieldMultiplier = 1.0
xAlteranHullMultiplier = 1.0
xOriShieldMultiplier = 0.6
xOriHullMultiplier = 0.95


##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstancedict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		global PlasmaSGShieldDamageMultiplier, xAnubisShieldMultiplier, xAsgardShieldMuliplier, xAlteranShieldMultiplier, xOriShieldMultiplier

		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()
		else: # default multiplication dmg to shields
			shieldDamageMultiplier = shieldDamageMultiplier * PlasmaSGShieldDamageMultiplier
		shouldDealAllFacetDamage = 0
		considerPiercing = considerPiercing + 1
		if pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech in PlasmaSGVulnerableShields:
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

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstancedict.has_key("SG Shields"):
		RaceShieldTech = None
		if pInstancedict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pInstancedict["SG Shields"]["RaceHullTech"]
		elif pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]

		if RaceShieldTech != None:
			global xAsgardHullMuliplier, xAlteranHullMultiplier, xOriHullMultiplier
			wasChanged = wasChanged + 1
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]	
			if RaceShieldTech == "Asgard":
				hullDamageMultiplier = hullDamageMultiplier * xAsgardHullMuliplier
			elif RaceShieldTech == "Alteran" or RaceShieldTech == "Lantian" or RaceShieldTech == "Lantean" or RaceShieldTech == "Asuran":
				hullDamageMultiplier = hullDamageMultiplier * xAlteranHullMuliplier
			elif RaceShieldTech == "Ori":
				hullDamageMultiplier = hullDamageMultiplier * xOriHullMuliplier




	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

