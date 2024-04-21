# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19 April 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the FoolTargeting Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/FoolTargetingScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# This tech adds a miss to the values if the attacker's sensor range is below a threshold. Affects both phasers and torps/pulses
# How-to-use:
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev - note the number indicates how fast it learns, make it 0 so it never helps into learning and negative values so it instead makes it more difficult for others to adapt :P
# Special fields:
# - "Sensor": at this value or below, the attacker will have its attacks scrambled. Default is 100.
# - "Miss": this value will indicate by how much they will miss. Default is 2.0
# EXTRA NOTES: "Tachyon Sensors" is an ECM-amplifier and EECM. "Tachyon Sensors" is an entirely different tech, which will give pros and cons (pros, chance at detecting non-phased cloaked vessels upon scanning area; cons, this, being
# more vulnerable to Minbari Stealth), "Tachyon Sensors": 1. See more of this Minbari Stealth script for notes.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Fool Targeting": {
		"Minbari Stealth": {
			"Miss": 2.0,
			"Sensor": 600,
		}  
	}
}
"""
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import traceback

# Some global variables could be used as well
globalPrimitiveSensor = 100
globalfMissExtra = 2.0

def commonFunction(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, pTorp, fSensorRange, fAngleDiff, fObjectDistance):
	debug(__name__ + ", commonFunction")
	primitiveSensor = globalPrimitiveSensor
	if pInstanceFool and pInstanceFool[techName].has_key("Sensor"):
		primitiveSensor = pInstanceFool[techName]["Sensor"]
	fMissExtra = 0.0
	try:
		extraMultiplier = 1.0
		effortMultiplier = 1.0
		if pAttackerInstance and pAttackerInstance.__dict__.has_key("Tachyon Sensors"): # These are both an ECM-amplifier, and an EECM - set to 1.0 or lower for Minbari Vessels which are unaffected by their own Stealth, and advanced races with very advanced tachyon sensors, like the Vorlons and other First-One ships, higher than 1.0 for other ships using exclusively Tachyon sensors.
			extraMultiplier = pAttackerInstance.__dict__["Tachyon Sensors"]

		pDefendingShip = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
                if pDefendingShip:
			pShields = pDefendingShip.GetShields()
			if pShields:
				effortMultiplier = pShields.GetConditionPercentage() * pShields.GetPowerPercentageWanted()
			if effortMultiplier > 1.24:
				effortMultiplier = 1.24
		if extraMultiplier * effortMultiplier * primitiveSensor > fSensorRange:
			fMissExtra = globalfMissExtra
			if pInstanceFool and pInstanceFool[techName].has_key("Miss"):
				fMissExtra = pInstanceFool[techName]["Miss"]
			
	except:
		print "Error while doing Minbari Stealth beam condition"
		traceback.print_exc()
		fMissExtra = 0.0

	return fMiss + fMissExtra

###### One or both of these two following functions must always exist for the parent script to take into account their innacuracy. Both must return fMiss, with fMiss finally being the accumulated values for all subTechs ######
def beamCondition(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, fSensorRange, fAngleDiff, fObjectDistance): # Establishes a random factor - values must be >= 0. The greater the value, the more range can happen between sessions.
	debug(__name__ + ", beamCondition")
	#print "Minbari stealth beam function called"
	return commonFunction(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, None, fSensorRange, fAngleDiff, fObjectDistance)

def pulseTCondition(techName, pInstanceFool, fMiss, pAttackerShip, pAttackerInstance, pDefenderShip, pDefenderInstance, pTorp): # Establishes the minimum number of strikes before it adapts, stacking along the random value above - please notice some weapons deal multi-strikes. Values must be >= 0
	debug(__name__ + ", pulseTCondition")
	#print "Minbari stealth torp and pulse function called"

	pDefenderShip = App.ShipClass_GetObjectByID(None, pDefenderShip.GetObjID())
	if pDefenderShip:
		fSensorRange = 0.0
		pSensor = None
		pAttackerShip = App.ShipClass_GetObjectByID(None, pAttackerShip.GetObjID())
		if pAttackerShip:
			pSensor = pAttackerShip.GetSensorSubsystem()
		if pSensor:
			fSensorRange = pSensor.GetSensorRange()
	        	# calculate Sensor Damage and power into Range
			fSensorRange = fSensorRange * pSensor.GetConditionPercentage() * pSensor.GetPowerPercentageWanted()

		return commonFunction(techName, pInstanceFool, fMiss, pAttackerShip, pAttackerInstance, pDefenderShip, pDefenderInstance, pTorp, fSensorRange, None, None)
	else:
		return 0.0