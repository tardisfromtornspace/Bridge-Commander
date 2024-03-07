# by USS Sovereign, do a 360 degree spin in an attempt to search for an open jump position.

import App
import MissionLib

def CreateAI(pShip):
        pPlayer = MissionLib.GetPlayer()
	#########################################
	# Creating PlainAI TurnAround at (209, 92)
	pTurnAround = App.PlainAI_Create(pShip, "TurnAround")
	pTurnAround.SetScriptModule("TurnToOrientation")
	pTurnAround.SetInterruptable(1)
	pScript = pTurnAround.GetScriptInstance()
	pScript.SetObjectName(pPlayer.GetName())
	# Done creating PlainAI TurnAround
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (218, 149)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pTurnAround)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
