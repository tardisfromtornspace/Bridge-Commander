# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 6th February 2026, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the AndromedanTractorRepulsorTech Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/AndromedanTractorBeamWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how SG shielding is affected by Andromedan Tractor Repulsor Beam Weapons.
# The reason we make a tech for this, is mostly because these shields are quite good at absorbing kinetic energy so this should be a different deal.
# And even between SG shields, some behave differently:

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

# SG-related info
xWraithHullResistMultiplier = 0.99
xAsgardShieldResistMultiplier = (1.0/3.0)
xOriShieldResistMultiplier = (1.0/3.14)

##### This function below is used for shield behaviour towards this weapon (when the hull has not been hit)
def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"):
		wasChanged = wasChanged + 1
		shouldPassThrough = shouldPassThrough - 1
		if pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]
			if RaceShieldTech == "Asgard": # Resistances
				global xAsgardShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xAsgardShieldResistMultiplier
			if RaceShieldTech == "Ori": # Resistances
				global xOriShieldResistMultiplier
				shieldDamageMultiplier = shieldDamageMultiplier * xOriShieldResistMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged

##### This function below is used for hull behaviour towards this weapon (when the hull has been hit)
def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged):
	if pTargetInstance and pTargetInstanceDict.has_key("SG Shields"): # Own turf, SG Ion Weapons are meant to deal additional damage to weak Naquadah and some Neutronium hulls... and Replicator hulls
		RaceShieldTech = None
		if pTargetInstanceDict["SG Shields"].has_key("RaceHullTech"): # We will assume shields and hull tech races are the same unless we say otherwise, for simplicity to not add too many fields.
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceHullTech"]
		elif pTargetInstanceDict["SG Shields"].has_key("RaceShieldTech"):
			RaceShieldTech = pTargetInstanceDict["SG Shields"]["RaceShieldTech"]

		if RaceShieldTech == "Wraith":
			global xWraithHullResistMultiplier
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * (xWraithHullResistMultiplier)
			if pTargetInstanceDict["SG Shields"].has_key("Wraith Dampening"):
				hullDamageMultiplier = hullDamageMultiplier * pTargetInstanceDict["SG Shields"]["Wraith Dampening"]

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged

