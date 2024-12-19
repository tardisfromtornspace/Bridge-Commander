# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the METhanixMagneticHydrodynamicCannon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/METhanixScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how B5 defences are affected by ME Thanix Weapons.
# Basically, most ships have no shields so the shots should go through

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

global METhanixB5LegacyShieldDamageMultiplier
METhanixB5LegacyShieldDamageMultiplier = 0.1

global METhanixB5LegacyHullDamageMultiplier
METhanixB5LegacyHullDamageMultiplier = 0.1 

### With that said, some B5 defences (as well as Hull Polarization) canonically would at least protect a bit from direct hull damage. Since we did the thing above to guarantee ships without shields lore-wise still take decent shield damage, we must ensure that those vessel's hull damage defences are not bypassed completely.
defenceGridMultiplier = 0.99
hullPolarizerMultiplier = 0.6
shadowDispersiveHullMultiplier = 0.9
shadowDispersiveHullMin = 0.2

### Some ships that from legacy reasons are extra vulnerable to this weapon in some way - for these ones is because B5 defences and STBC shields work differently
global lB5VulnerableLegacyList
lB5VulnerableLegacyList = (
		"bluestar",
		"MinbariSharlin",
		"MinbariNial"
		"Victory",
		"whitestar",
                )

global lB5ResistantLegacyList
lB5ResistantLegacyList = (
		"bluestar",
		"SigmaWalkerScienceLab",
		"Victory",
                "VOR_Cruiser",
                "VOR_Destroyer",
                "VOR_DestroyerClosed",
                "VOR_Fighter",
                "VOR_FighterOpen",
                "VOR_Planetkiller",
		"whitestar",
                )


def interactionShieldBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	global METhanixB5LegacyShieldDamageMultiplier
	if pTargetInstance:
		if pTargetInstanceDict.has_key('Defense Grid') or pTargetInstanceDict.has_key('Gravimetric Defense'):
			wasChanged = wasChanged + 1
			shieldDamageMultiplier = shieldDamageMultiplier * defenceGridMultiplier
			if pTargetInstanceDict.has_key('Defense Grid'):
				shouldPassThrough = shouldPassThrough + 1

		elif pTargetInstanceDict.has_key('Shadow Dispersive Hull'): # ohhhh Babylon 5 Shadow Dispersive Hull 
			wasChanged = wasChanged + 1
			shieldDamageMultiplier = shieldDamageMultiplier * METhanixB5LegacyShieldDamageMultiplier
			shouldPassThrough = shouldPassThrough + 1
		if pTargetInstanceDict.has_key("Vree Shields"): # Vree/Abbai/Shinindrea shields work very differently, they may care little about your weapon being Thanix...
			pShields = pTarget.GetShields()
			auxWea = 0
			if pShields:
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					fMax = pShields.GetMaxShields(shieldDir)
					if fMax > 4000:
						auxWea = auxWea + 1
			if auxWea <= 0:
				wasChanged = wasChanged + 1
				shieldDamageMultiplier = shieldDamageMultiplier * METhanixB5LegacyShieldDamageMultiplier * 0.5

	global lB5ResistantLegacyList
	if sShipScript in lB5ResistantLegacyList:
		wasChanged = wasChanged + 1
		shieldDamageMultiplier = shieldDamageMultiplier * METhanixB5LegacyShieldDamageMultiplier * 0.4

	global lB5VulnerableLegacyList
	if sShipScript in lB5VulnerableLegacyList:
		wasChanged = wasChanged + 1
		shouldPassThrough = shouldPassThrough + 1

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

def interactionHullBehaviour(attackerID, pAttacker, pAttackerInstance, pAttackerInstanceDict, targetID, pTarget, pTargetInstance, pTargetInstanceDict, sScript, sShipScript, pEvent, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass):
	global defenceGridMultiplier, hullPolarizerMultiplier, shadowDispersiveHullMultiplier, shadowDispersiveHullMin, METhanixB5LegacyHullDamageMultiplier
	if pTargetInstance:
		#INTERACTION Defence Grid reduces hull damage a tiiiiiny bit
		if pTargetInstanceDict.has_key('Defense Grid'):
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * defenceGridMultiplier

		#INTERACTION Hull Polarizer reduces hull damage a decent bit... at least if intact
		if pTargetInstanceDict.has_key('Hull Polarizer') or pTargetInstanceDict.has_key('Polarized Hull Plating'):
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * hullPolarizerMultiplier
		#INTERACTION Shadow Dispersive Hull reduces hull damage a significant bit
		if pTargetInstanceDict.has_key('Shadow Dispersive Hull'):
			wasChanged = wasChanged + 1
			radiusDispersion = 1.0
			if hasattr(pShip, "GetRadius"):
				radiusDispersion = pShip.GetRadius()
				if radiusDispersion > 2.0: # The bigger the hull, the better it will disperse the damage, up to a limit
					radiusDispersion = (shadowDispersiveHullMultiplier ** (1.0 * radiusDispersion))
					if radiusDispersion < shadowDispersiveHullMin:
						radiusDispersion = shadowDispersiveHullMin
					hullDamageMultiplier = hullDamageMultiplier * radiusDispersion
				else: # hull is too small, it may be tough, but not as tough
					hullDamageMultiplier = hullDamageMultiplier * (shadowDispersiveHullMultiplier)

	global lB5ResistantLegacyList
	if sShipScript in lB5ResistantLegacyList:
		wasChanged = wasChanged + 1
		hullDamageMultiplier = hullDamageMultiplier * METhanixB5LegacyHullDamageMultiplier

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, wasChanged, considerDisabledShieldPass

