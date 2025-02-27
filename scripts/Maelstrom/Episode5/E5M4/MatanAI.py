import App
def CreateAI(pShip):
	#########################################
	# Creating PlainAI Warp at (220, 169)
	pWarp = App.PlainAI_Create(pShip, "Warp")
	pWarp.SetScriptModule("Warp")
	pWarp.SetInterruptable(1)
	pScript = pWarp.GetScriptInstance()
	pScript.WarpBlindly(bWarpImmediately = 0)
	# Done creating PlainAI Warp
	#########################################
	#########################################
	# Creating ConditionalAI MatanDamaged at (220, 136)
	## Conditions:
	#### Condition Damaged
	pDamaged = App.ConditionScript_Create("Conditions.ConditionCriticalSystemBelow", "ConditionCriticalSystemBelow", "Matan's Keldon", 0.80)
	## Evaluation function:
	def EvalFunc(bDamaged):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bDamaged:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pMatanDamaged = App.ConditionalAI_Create(pShip, "MatanDamaged")
	pMatanDamaged.SetInterruptable(1)
	pMatanDamaged.SetContainedAI(pWarp)
	pMatanDamaged.AddCondition(pDamaged)
	pMatanDamaged.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI MatanDamaged
	#########################################
	#########################################
	# Creating CompoundAI Attack2 at (335, 163)
	import Ai.Compound.BasicAttack
	pAttack2 = Ai.Compound.BasicAttack.CreateAI(pShip, "player")
	# Done creating CompoundAI Attack2
	#########################################
	#########################################
	# Creating ConditionalAI Timer1 at (334, 130)
	## Conditions:
	#### Condition Timer
	pTimer = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 45, 0)
	## Evaluation function:
	def EvalFunc(bTimer):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimer:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTimer1 = App.ConditionalAI_Create(pShip, "Timer1")
	pTimer1.SetInterruptable(1)
	pTimer1.SetContainedAI(pAttack2)
	pTimer1.AddCondition(pTimer)
	pTimer1.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Timer1
	#########################################
	#########################################
	# Creating PlainAI Stay at (448, 56)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(1)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (167, 57)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (331, 65)
	pPriorityList.AddAI(pMatanDamaged, 1)
	pPriorityList.AddAI(pTimer1, 2)
	pPriorityList.AddAI(pStay, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (76, 56)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
