# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the METhanixMagneticHydrodynamicCannon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/METhanixScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how ME shielding is affected by ME Thanix Magnetic Hydrodynamic Cannon Weapons.
# The reason we make a tech for this, is mostly as a way to allow the Thanix to deal appropiate damage to a ME Shield.
# Additionally, a new field has been added to the "ME Shields" technology, "Reaper Dampening" : <multiplier>, where <multiplier> is the value which will affect the final hull damage, a way to simulate a Reaper having inner ME fields reducing the damage. 

# On this case, more info about ME shields will be reviewed on their main ME Shields technology
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info

xReaperHullResistMultiplier = 0.25
xReaperShieldResistMultiplier = (1.0/4.0)

##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	if pTargetInstance and pTargetInstanceDict.has_key("ME Shields"):
		wasChanged = wasChanged + 1
		if pTargetInstanceDict["ME Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["ME Shields"]["RaceShieldTech"]
			if RaceShieldTech == "Reaper": # Resistances
				global xReaperShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xReaperShieldResistMultiplier
			else:
				considerDisabledShieldPass = considerDisabledShieldPass + 1
		else:
			considerDisabledShieldPass = considerDisabledShieldPass + 1

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	if pTargetInstance and pTargetInstanceDict.has_key("ME Shields"):
		RaceShieldTech = None
		if pTargetInstanceDict["ME Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pTargetInstanceDict["ME Shields"]["RaceHullTech"]
		elif pTargetInstanceDict["ME Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["ME Shields"]["RaceShieldTech"]

		if RaceShieldTech == "Reaper":
			global xReaperHullResistMultiplier
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * (xReaperHullResistMultiplier)
			if pTargetInstanceDict["ME Shields"].has_key("Reaper Dampening"):
				hullDamageMultiplier = hullDamageMultiplier * pTargetInstanceDict["ME Shields"]["Reaper Dampening"]

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass