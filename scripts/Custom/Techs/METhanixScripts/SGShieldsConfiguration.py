# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the METhanixMagneticHydrodynamicCannon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/METhanixScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by ME Thanix Weapons.
# For the most part, SG Shields would survive the brunt of the impact, but it would definetely do something.

# On this case, more info about SG shields will be reviewed on their main SG Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info
xWraithHullResistMultiplier = 0.25
xDefaultShieldResistMultiplier = 0.035
xAsgardShieldResistMultiplier = (1.0/2.0)

##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		if pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech == "Asgard" or RaceShieldTech == "Ori" or RaceShieldTech == "Nox" or RaceShieldTech == "Tau'ri": # Resistances
				global xAsgardShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldResistMultiplier

		shieldDamageMultiplier = shieldDamageMultiplier * xDefaultShieldResistMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"): # Own turf, SG Ion Weapons are meant to deal additional damage to weak Naquadah and some Neutronium hulls... and Replicator hulls
		RaceShieldTech = None
		if pTargetInstanceDict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceHullTech"]
		elif pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]

		if RaceShieldTech == "Wraith" or RaceShieldTech == "Ori":
			global xWraithHullResistMultiplier
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * (xWraithHullResistMultiplier)
			if pTargetInstanceDict["SG Shields"].has_key("Wraith Dampening"):
				hullDamageMultiplier = hullDamageMultiplier * pTargetInstanceDict["SG Shields"]["Wraith Dampening"]

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

