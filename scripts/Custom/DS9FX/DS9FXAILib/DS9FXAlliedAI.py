# by USS Sovereign. Mission AlliedAI being used in Campaign Mission

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI AlliedAI at (478, 151)
	import AI.Compound.NonFedAttack
	pAlliedAI = AI.Compound.NonFedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI AlliedAI
	#########################################
	#########################################
	# Creating ConditionalAI Waiting at (302, 202)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWaiting = App.ConditionalAI_Create(pShip, "Waiting")
	pWaiting.SetInterruptable(1)
	pWaiting.SetContainedAI(pAlliedAI)
	pWaiting.AddCondition(pTimePassed)
	pWaiting.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Waiting
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (157, 271)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWaiting)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
