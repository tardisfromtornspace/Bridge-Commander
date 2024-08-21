# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th August 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGIonWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGIonWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by SG Ion Weapons.
# The reason we make a tech for this, is because SG Shields behave differently from ST, SW shields or B5 defences against an Ion Weapon.
# And even between SG shields, some behave differently:
# Early Go'auld shields could not handle Tollan nor Asgard Ion Guns - two shots from the Tollan guns shredded a single Ha'tak, bypassing the shield. The only way it makes sense for Anubis-grade shields to shrug an entire planetary defense grid of those while still being vulnerable to 3-6 unupgraded Ha'taks is for the shields to be more advanced to block this Ion weapon, and not only because of being stronger. Else we end up with a Ha'tak having 100 times more shields than normal, and if that was true, Anubis could have destroyed the other System Lords with a single Ha'tak, no superweapon needed.

# On this case, more info about SG shields will be reviewed on their main SG Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info
IonSGShieldDamageMultiplier = 10.0

## Because some SG shields could not block Ion Cannons (see more information below)
IonSGVulnerableShields = ["Go'auld"] # This excludes "Anubis Go'auld" shields.

## Some SG-related resistances - unless there's a new Stargate franchise adding more races and spaceship combat, these should do the job
xAnubisShieldMultiplier = 0.79
xAnubisVSTollanShieldMultiplier = -0.15
xAnubisVSPrimitiveAsgardShieldMultiplier = 0.15
xAsgardShieldMultiplier = 0.8
xAlteranShieldMultiplier = 0.68
xOriShieldMultiplier = 0.67

# Ion weaponry for the Asgard was developed also because it affects Replicator bonds, so we must give them plus damage against them
xVulnerableNaquadahOrNeutroniumBoost = 3.0

##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	if pInstancedict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		global IonSGShieldDamageMultiplier, xAnubisShieldMultiplier, xAnubisVSTollanShieldMultiplier, xAnubisVSPrimitiveAsgardShieldMultiplier, xAsgardShieldMultiplier, xAlteranShieldMultiplier, xOriShieldMultiplier
		shieldDamageMultiplier = shieldDamageMultiplier + IonSGShieldDamageMultiplier
		shouldDealAllFacetDamage = 0
		considerPiercing = considerPiercing + 1
		if pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech in IonSGVulnerableShields:
				shouldPassThrough = 1
			elif RaceShieldTech == "Anubis Go'auld": # Resistances	
				if pTorp and hasattr(pTorp, "GetDamageRadiusFactor"):
					dmgRadiusFactor = pTorp.GetDamageRadiusFactor() # Meaner weapons have usually meaner knockback
					if dmgRadiusFactor == 1.25: # Oh, the Tollan Weapon... quite an unorthodox way of knowing it tho
						considerPiercing = considerPiercing - 1
						shieldDamageMultiplier = shieldDamageMultiplier * xAnubisVSTollanShieldMultiplier
					elif dmgRadiusFactor <= 0.25: # Oh, Asgard Ion weapons - here the meanest ones have a meaner kick!
						considerPiercing = considerPiercing - 1
						shieldDamageMultiplier = shieldDamageMultiplier * xAnubisVSPrimitiveAsgardShieldMultiplier
					else:
						shieldDamageMultiplier = shieldDamageMultiplier * xAnubisShieldMultiplier
				else:
					shieldDamageMultiplier = shieldDamageMultiplier * xAnubisShieldMultiplier
						 
			elif RaceShieldTech == "Asgard": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldMultiplier
			elif RaceShieldTech == "Alteran" or RaceShieldTech == "Lantian" or RaceShieldTech == "Lantean" or RaceShieldTech == "Asuran": # Resistances, not including actual Replicator ships here because those will have their own tech
				shieldDamageMultiplier = shieldDamageMultiplier * xAlteranShieldMultiplier
			elif RaceShieldTech == "Ori": # Resistances
				shieldDamageMultiplier = shieldDamageMultiplier * xOriShieldMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	if pInstancedict.has_key("SG Shields"): # Own turf, SG Ion Weapons are meant to deal additional damage to weak Naquadah and some Neutronium hulls... and Replicator hulls
		RaceShieldTech = None
		if pInstancedict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pInstancedict["SG Shields"]["RaceHullTech"]
		elif pInstancedict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]

		if RaceShieldTech != None:
			global xVulnerableNaquadahOrNeutroniumBoost
			wasChanged = wasChanged + 1
			RaceShieldTech = pInstancedict["SG Shields"]["RaceShieldTech"]	
			if RaceShieldTech in IonSGVulnerableShields: # Go'auld classic naquadah hull is based on Naquadah absorbing energy and being tough... but while that gives it a very high resistance, its high amplifier properties  may also overload it! Since SG Ion weapons seem to mess with it, extra damage mod-wise!
				hullDamageMultiplier = hullDamageMultiplier * (xVulnerableNaquadahOrNeutroniumBoost)
			#elif RaceShieldTech == "Anubis Go'auld": # Their shields are powerful, but their hulls are still of the same material, if improved
			#	hullDamageMultiplier = hullDamageMultiplier * (xVulnerableNaquadahOrNeutroniumBoost)
			elif RaceShieldTech == "Replicator": # You may deal a bit more damage to the hulls... is not as if they cannot eventually adapt anyways
				hullDamageMultiplier = hullDamageMultiplier * (xVulnerableNaquadahOrNeutroniumBoost)




	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration

