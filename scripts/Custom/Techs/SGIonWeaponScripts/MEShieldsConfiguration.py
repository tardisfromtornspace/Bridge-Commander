# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19th December 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.1
# Meant to be used alongside the SGIonWeapon Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/SGIonWeaponScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This file takes care of how ME shielding is affected by SG Ion Weapons.
# The reason we make a tech for this, is because ME Shields behave differently from ST, SG shields or B5 defences against an Ion Weapon.
# For ME is a bit hazy, but it is known that weapons with a lot of electric charge can overlod a mass effect shield. For this I've decided to make them cause at least twice the damage like a heavy ME overload and consider shield piercing. As for any EMP effect, ME Ships tend to deal with electric charges a lot, so I would not see that much of a difference except maybe destabilizing the storage of excess charge.

# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

import string

IonMEShieldDamageMultiplier = 10.0
IonMEHullDamageMultiplier = 1.0
IonMEElectricChargeHullDamageMultiplier = 0.1


def interactionShieldBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	global lMEVulnerableLegacyList
	if pInstance and pInstancedict.has_key("ME Shields"): # ME shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1
		global IonMEShieldDamageMultiplier
		shieldDamageMultiplier = shieldDamageMultiplier + IonMEShieldDamageMultiplier
		shouldDealAllFacetDamage = shouldDealAllFacetDamage + 1
		considerPiercing = 1
		negateRegeneration = negateRegeneration + 1


	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration

def interactionHullBehaviour(pShip, sScript, sShipScript, pInstance, pEvent, pTorp, pInstancedict, pAttackerShipID, hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration):
	global lMEVulnerableLegacyList
	if pInstance and pInstancedict.has_key("ME Shields"): # ME shields are extremely weak to Ion Weapons, they are used to knock them out, albeit not destroy them
		wasChanged = wasChanged + 1

		global IonMEHullDamageMultiplier, IonMEElectricChargeHullDamageMultiplier
		# We reduce the damage... but your power plant gets damaged! Be careful or too many Ions may fry your hull!
		pPower = pShip.GetPowerSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - IonMEElectricChargeHullDamageMultiplier) * pTorp.GetDamage()
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		pPower = pShip.GetWarpEngineSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - IonMEElectricChargeHullDamageMultiplier) * pTorp.GetDamage()
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		pPower = pShip.GetShields()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - IonMEElectricChargeHullDamageMultiplier) * pTorp.GetDamage()
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		pPower = pShip.GetCloakingSubsystem()
		if pPower:
			myDamage = -hullDamageMultiplier * (1 - IonMEElectricChargeHullDamageMultiplier) * pTorp.GetDamage()
			myStatus = pPower.GetCondition() + myDamage
  			if (myStatus) < 0.1:
				myStatus = 0.1
			elif (pPower.GetCondition() + myDamage) >  pPower.GetMaxCondition():
				myStatus = pPower.GetMaxCondition()

			pPower.SetCondition(myStatus)

		hullDamageMultiplier = hullDamageMultiplier * IonMEHullDamageMultiplier
		negateRegeneration = negateRegeneration + 1

	return hullDamageMultiplier, shieldDamageMultiplier, shouldPassThrough, considerPiercing, shouldDealAllFacetDamage, wasChanged, negateRegeneration

