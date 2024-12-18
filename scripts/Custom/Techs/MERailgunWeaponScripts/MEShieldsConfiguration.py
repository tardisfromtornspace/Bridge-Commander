# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 18th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the SGRailgunWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGRailgunWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how ME shielding is affected by ME Railgun Weapons.
# The reason we make a tech for this, is because ME tech would work by blocking the projectile entirely from hitting, so shield drain needs to be considered.
# This Subtech adds a new option: mass effect mass - introduce this to the end of your ME projectile file and if it's greater than 1 it will bypass shields.
# NOTE: While this method works, it is better to use the MEShields file bypass because that style performs partial or full damage bypass in a more accurate way for smaller targets (albeit that method is a bit uglier since a bypassed torpedo is purporsefully made not visible) - the method implemented here may create a "phase-through" effect if the ship is too small.
"""
def MassEffectMass():
	return 0.1
"""

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

RailgunMEShieldDamageMultiplier = 3.0
RailgunMEHullDamageMultiplierBoost = 1.0
RailgunMEHullDamageMultiplier = 3.0
xReaperHullMultiplier = 0.8

def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global RailgunMEShieldDamageMultiplier
	if (pInstancedict and pInstancedict.has_key("ME Shields")):
		global RailgunMEShieldDamageMultiplier, RailgunMEHullDamageMultiplier
		wasChanged = wasChanged + 1
		considerPiercing = considerPiercing + 1

		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()
		else: # default multiplication dmg to shields
			shieldDamageMultiplier = shieldDamageMultiplier * RailgunMEShieldDamageMultiplier

		if hasattr(importedTorpInfo, "MassEffectMass"):
			extraMass = importedTorpInfo.MassEffectMass()
			if extraMass > 0:
				isCyclonicOrShieldsActive = 0
				if pInstancedict["ME Shields"].has_key("MaximumSpeedTrigger") and pInstancedict["ME Shields"]["MaximumSpeedTrigger"] < 0: # Granting it the ability to bypass ME Shields
					myShieldSubsys = pShip.GetShields()
					if myShieldSubsys != None:
						cdnPerc = myShieldSubsys.GetCombinedConditionPercentage()
						disabledPerc = myShieldSubsys.GetDisabledPercentage()
						if disabledPerc + 0.1 <= cdnPerc:
							isCyclonicOrShieldsActive = 1
				if isCyclonicOrShieldsActive == 0:
					shouldPassThrough = shouldPassThrough + 1
					hullDamageMultiplier = hullDamageMultiplier * extraMass


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	if pInstancedict and pInstancedict.has_key("ME Shields"):
		RaceShieldTech = None
		if pInstancedict["ME Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pInstancedict["ME Shields"]["RaceHullTech"]
		elif pInstancedict["ME Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pInstancedict["ME Shields"]["RaceShieldTech"]

		if RaceShieldTech != None:
			global xReaperHullMultiplier
			if RaceShieldTech == "Reaper":
				changed = changed + 1
				hullDamageMultiplier = hullDamageMultiplier * xReaperHullMultiplier

				mod = pTorp.GetModuleName()
				importedTorpInfo = __import__(mod)
				if hasattr(importedTorpInfo, "HullDmgMultiplier"): # If this torp has a special global multiplier, then we use it
					hullDamageMultiplier = hullDamageMultiplier * importedTorpInfo.HullDmgMultiplier()
				else:
					hullDamageMultiplier = hullDamageMultiplier * RailgunMEHullDamageMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged