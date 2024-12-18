# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 31st October 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the MERailgunWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/MERailgunWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how B5 defences are affected by ME Railgun Weapons.
# Babylon 5 - between the fact that lore-wise Babylon 5 has no shields except Vree, Abbai, Vorlons, potentially other First Ones, and Thirdspace Aliens; and that mod-wise the latest Babylon 5 super-pack mods already have alternatives of defense against these weapons such as Simulated Point Defense, and that for certain vessels a semblance of a shield was kept for blocking or imitating phaser absorption, we must guarantee that some Railgun Weapons can still surpass that token shield threshold in some way to work as intended for certain vessels.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

global RailgunB5LegacyShieldDamageMultiplier
RailgunB5LegacyShieldDamageMultiplier = 2.0 

global RailgunB5LegacyGridDamageMultiplier
RailgunB5LegacyGridDamageMultiplier = 1.1 

### With that said, some B5 defences (as well as Hull Polarization) canonically would at least protect a bit from direct hull damage. Since we did the thing above to guarantee ships without shields lore-wise still take decent shield damage, we must ensure that those vessel's hull damage defences are not bypassed completely.
defenceGridMultiplier = 0.7 # Used for legacy reasons
hullPolarizerMultiplier = 0.65
shadowDispersiveHullMultiplier = 0.92
shadowDispersiveHullMin = 0.38

### Some ships that from legacy reasons are extra vulnerable to this weapon in some way - for these ones is because B5 defences and STBC shields work differently
global lB5VulnerableLegacyList 
lB5VulnerableLegacyList = (
                "bluestar",
                "DRA_Raider",
                "DRA_Shuttle",
                "MinbariNial",
                "MinbariSharlin",
                "Victory",
                "VOR_Destroyer",
                "VOR_DestroyerClosed",
                "VOR_Fighter",
                "VOR_FighterOpen",
                "whitestar",
                )


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global RailgunB5LegacyShieldDamageMultiplier
	changed = 0
	if pInstance:
		if pInstancedict.has_key('Gravimetric Defense'): # ohhhh Babylon 5 gravimetric defenses - they help quite a bit, a far-away watered-down cousin from a cyclonic mass effect shield - but you still need to consider piercing.
			changed = 1
			wasChanged = wasChanged + 1
			considerPiercing = considerPiercing + 1
		elif pInstancedict.has_key('Defense Grid'): # ohhhh Babylon 5 defence grids and gravimetric defenses - and if you already reached this point is because your point defence system failed to take this shot, sorry
			changed = 1
			wasChanged = wasChanged + 1
			shieldDamageMultiplier = shieldDamageMultiplier * RailgunB5LegacyGridDamageMultiplier
			considerPiercing = considerPiercing + 1

		elif pInstancedict.has_key('Shadow Dispersive Hull'): # ohhhh Babylon 5 Shadow Dispersive Hull - yeah, no shields against kinetic impact, sorry - but don't worry, at least your hull damage will be reduced
			changed = 1
			wasChanged = wasChanged + 1
			if hasattr(pShip, "GetRadius") and pShip.GetRadius() < 2.0: # Dumb way to fix a random issue with the shadow fighter model having some invulnerability from certain sides to this weapon and other phased weapons
				shieldDamageMultiplier = shieldDamageMultiplier * RailgunB5LegacyShieldDamageMultiplier
				shouldDealAllFacetDamage = shouldDealAllFacetDamage + 1
			
			shouldPassThrough = shouldPassThrough + 1
			considerPiercing = considerPiercing + 1

		elif pInstancedict.has_key("Vree Shields"): # Vree/Abbai/Shinindrea shields work very differently, in fact Abbai shields work in a simialr fashion to a gravity field, slowing matter to a halt
			changed = 1
			wasChanged = wasChanged + 1
			shieldDamageMultiplier = shieldDamageMultiplier + 0

	global lB5VulnerableLegacyList
	if sShipScript in lB5VulnerableLegacyList:
		changed = 1
		wasChanged = wasChanged + 1
		shieldDamageMultiplier = shieldDamageMultiplier * RailgunB5LegacyShieldDamageMultiplier
		considerPiercing = considerPiercing + 1

	if changed == 1:
		mod = pTorp.GetModuleName()
		importedTorpInfo = __import__(mod)
		if hasattr(importedTorpInfo, "ShieldDmgMultiplier"): # If this torp has a special global multiplier, then we use it
			shieldDamageMultiplier = shieldDamageMultiplier * importedTorpInfo.ShieldDmgMultiplier()

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged):
	global defenceGridMultiplier, hullPolarizerMultiplier, shadowDispersiveHullMultiplier, shadowDispersiveHullMin
	#INTERACTION Defence Grid reduces hull damage a tiiiiiny bit
	if pInstance:
		changed = 0
		if pInstancedict.has_key('Defense Grid'):
			changed = 1
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * defenceGridMultiplier

		#INTERACTION Hull Polarizer reduces hull damage a decent bit... at least if intact
		if pInstancedict.has_key('Hull Polarizer') or pInstancedict.has_key('Polarized Hull Plating'):
			changed = 1
			wasChanged = wasChanged + 1
			hullDamageMultiplier = hullDamageMultiplier * hullPolarizerMultiplier
		#INTERACTION Shadow Dispersive Hull reduces hull damage a significant bit
		if pInstancedict.has_key('Shadow Dispersive Hull'):
			changed = 1
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

		if changed == 1:
			mod = pTorp.GetModuleName()
			importedTorpInfo = __import__(mod)
			if hasattr(importedTorpInfo, "HullDmgMultiplier"): # If this torp has a special global multiplier, then we use it
				hullDamageMultiplier = hullDamageMultiplier * (importedTorpInfo.HullDmgMultiplier() -1)

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged

