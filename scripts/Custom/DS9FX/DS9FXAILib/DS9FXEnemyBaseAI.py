# by USS Sovereign, a basic Starbase Attack AI

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetFriendlyGroup ()
	#########################################
	# Creating CompoundAI BaseAttack at (278, 110)
	import AI.Compound.StarbaseAttack
	pBaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI BaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (161, 197)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 5, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pBaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait
