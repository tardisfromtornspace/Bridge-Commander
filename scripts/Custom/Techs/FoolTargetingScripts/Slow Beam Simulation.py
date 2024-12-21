# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 19 April 2024, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used alongside the FoolTargeting Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/FoolTargetingScripts
# As these are Sub-techs with some leeway, their manuals must be explained here:
##################################
# SPECIFIC SUB-TECH MANUAL:
# If this tech is added to the attacker, beam hits will begin to be partially innacurate past a certain distance and target speed threshold. The purpose of this tech is to simulate beams that take a while to reach a target and cannot be simulated any other way, while the computers are still trying to predict where the hit will go, so instead of needing to be totally random the miss-related vector will be a bit more straightforward.
# How-to-use:
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev
# Special fields:
# - "Distance Threshold": from what distance from the target onwards these start to miss - in aproximated in-game "km". Default is 50.
# - "Speed Threshold": from what target speed onwards these start to miss. Default is 10.
# - "Distance Multiplier": multiply the miss according to this distance-related factor. Default is 1.0.
# - "Speed Multiplier": multiply the miss according to the speed-related factor. Default is 1.0.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Fool Targeting": {
		"Slow Beam Simulation": {
			"Distance Threshold": 50.0,
			"Speed Threshold": 10,
			"Distance Multiplier": 1.0,
			"Speed Multiplier": 1.0,
		}  
	}
}
"""
# NOTE: Imports and additional functions may be necessary here as well, depending on how creative the sub-tech becomes
import App
from bcdebug import debug
import math
import traceback

# Some global variables could be used as well
ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer
defaultD = 50.0
defaultS = 10.0
defaultDmult = 1.0
defaultSmult = 1.0

def commonFunction(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, pTorp, fSensorRange, fAngleDiff, fObjectDistance):
	debug(__name__ + ", commonFunction")

	fMissExtra = 0.0

	try:
		if pAttackerInstance:
			pAttackerInstanceDict = pAttackerInstance.__dict__
			if pAttackerInstanceDict.has_key("Fool Targeting") and pAttackerInstanceDict["Fool Targeting"].has_key("Slow Beam Simulation"):
				thresholdD = defaultD
				thresholdS = defaultS
				iDmult = defaultDmult
				iSmult = defaultSmult
				if pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"].has_key("Distance Threshold"):
					thresholdD = pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"]["Distance Threshold"]
				if pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"].has_key("Speed Threshold"):
					thresholdS = pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"]["Speed Threshold"]
				if pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"].has_key("Distance Multiplier"):
					iDmult = pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"]["Distance Multiplier"]
				if pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"].has_key("Speed Multiplier"):
					iSmult = pAttackerInstanceDict["Fool Targeting"]["Slow Beam Simulation"]["Speed Multiplier"]

				thresholdD = thresholdD * ticksPerKilometer
				if fObjectDistance > thresholdD:
					targetID = pTarget.GetObjID()
					if targetID:
						pTargetCareful = App.ShipClass_GetObjectByID(None, targetID)
						if pTargetCareful:
							v = pTarget.GetVelocityTG()
							if v:
								vMod = math.sqrt((v.x ** 2) + (v.y ** 2) + (v.z ** 2))
								if vMod > 0.0 and vMod * ticksPerKilometer > thresholdS:
									a = pTarget.GetAccelerationTG()
									if a:
										aMod = math.sqrt((a.x ** 2) + (a.y ** 2) + (a.z ** 2))
										if aMod > 0.1:
											newMissVector = App.TGPoint3()
											newMissVector.SetXYZ(-a.x, -a.y, -a.z)
											newMissVector.Unitize()

											#aa = pTarget.GetAngularAccelerationTG()
											#aaMod = math.sqrt((aa.x ** 2) + (aa.y ** 2) + (aa.z ** 2))

											distanceCalc = (fObjectDistance - thresholdD)/thresholdD
											velCalc = 1
											if thresholdS > 0.0:
												(vMod * ticksPerKilometer - thresholdS) / thresholdS
							
											fMissExtra = aMod * (distanceCalc * iDmult + velCalc * iSmult)
										else:
											newMissVector = App.TGPoint3()
											newMissVector.SetXYZ(-v.x, -v.y, -v.z)
											newMissVector.Unitize()
											fMissExtra = 0.01 * (iDmult + iSmult)

										fMissA = fMiss + fMissExtra
							
										return {"fMiss" : fMissA, "kNewLocation" : newMissVector}
					

			
	except:
		print "Error while doing Slow Beam Simulation condition"
		traceback.print_exc()
		fMissExtra = 0.0

	return fMiss + fMissExtra

###### One or both of these two following functions must always exist for the parent script to take into account their innacuracy. Both must return fMiss, with fMiss finally being the accumulated values for all subTechs ######
# if instead of being called "beamCondition" it is called "beamAttackerOnlyCondition", it will be used exclusively from the attacker's instance standpoint - this uses a slightly modified logic where pInstanceFool is the attacker's not the defender's
def beamAttackerOnlyCondition(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, fSensorRange, fAngleDiff, fObjectDistance): # Establishes a random factor - values must be >= 0. The greater the value, the more range can happen between sessions.
	debug(__name__ + ", beamCondition")
	return commonFunction(techName, pInstanceFool, fMiss, pShip, pAttackerInstance, pTarget, pDefenderInstance, None, fSensorRange, fAngleDiff, fObjectDistance)
"""
def pulseTCondition(techName, pInstanceFool, fMiss, pAttackerShip, pAttackerInstance, pDefenderShip, pDefenderInstance, pTorp): # Establishes the minimum number of strikes before it adapts, stacking along the random value above - please notice some weapons deal multi-strikes. Values must be >= 0
	debug(__name__ + ", pulseTCondition")
	#print "Slow Beam Simulation torp and pulse function called - this should not be called"

	return 0.0
"""