from bcdebug import debug
import App
import MissionLib
def CreateAI(pShip):
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateAI")

	# Add the starbase itself to the attacker list -- the AI needs to have
	# *something* on the attacker list so as not to crash, but it won't
	# try to attack itself
	pEnemies = MissionLib.GetEnemyGroup()
	if not pEnemies.GetNameTuple():
		pEnemies.AddName("This ship probably wont exist")
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pEnemies"))
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
