import App
def CreateAI(pShip):
	#########################################
	# Creating CompoundAI StarbaseAttackNeutrals at (250, 54)
	import AI.Compound.StarbaseAttack
	pStarbaseAttackNeutrals = AI.Compound.StarbaseAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pNeutrals"))
	# Done creating CompoundAI StarbaseAttackNeutrals
	#########################################
	#########################################
	# Creating CompoundAI StarbaseAttack at (433, 58)
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pFriendlies"))
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (328, 191)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (355, 110)
	pPriorityList.AddAI(pStarbaseAttackNeutrals, 1)
	pPriorityList.AddAI(pStarbaseAttack, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
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
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pPriorityList)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait
