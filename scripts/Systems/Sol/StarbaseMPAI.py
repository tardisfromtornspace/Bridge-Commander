from bcdebug import debug
import App
import MissionLib

def CreateAI(pShip):
	debug(__name__ + ", CreateAI")
	pMission = MissionLib.GetMission ()
	pEnemyGroup = MissionLib.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait
