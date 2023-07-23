import App

def CreateAI(pShip):
	#########################################
	# Creating CompoundAI BattleShieldsUp at (474, 6)
	import AI.Compound.BSGAttackShieldsUP
	pBattleShieldsUp = AI.Compound.BSGAttackShieldsUP.CreateAI(pShip)
	# Done creating CompoundAI BattleShieldsUp
	#########################################
	#########################################
	# Creating PlainAI Scripted at (498, 87)
	pScripted = App.PlainAI_Create(pShip, "Scripted")
	pScripted.SetScriptModule("Defensive")
	pScripted.SetInterruptable(1)
	# Done creating PlainAI Scripted
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (348, 16)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(1)
	# SeqBlock is at (456, 55)
	pSequence.AddAI(pBattleShieldsUp)
	pSequence.AddAI(pScripted)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating ConditionalAI ToShieldsUpAI at (370, 72)
	## Conditions:
	#### Condition GettingAttackedEnough
	pGettingAttackedEnough = App.ConditionScript_Create("Conditions.ConditionAttacked", "ConditionAttacked", pShip, 0.000001, 0.000001, 120)
	## Evaluation function:
	def EvalFunc(bGettingAttackedEnough):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bGettingAttackedEnough):
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pToShieldsUpAI = App.ConditionalAI_Create(pShip, "ToShieldsUpAI")
	pToShieldsUpAI.SetInterruptable(1)
	pToShieldsUpAI.SetContainedAI(pSequence)
	pToShieldsUpAI.AddCondition(pGettingAttackedEnough)
	pToShieldsUpAI.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ToShieldsUpAI
	#########################################
	#########################################
	# Creating CompoundAI BattleShieldsDown at (457, 155)
	import AI.Compound.BSGAttackShieldsDOWN
	pBattleShieldsDown = AI.Compound.BSGAttackShieldsDOWN.CreateAI(pShip)
	# Done creating CompoundAI BattleShieldsDown
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (195, 144)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (362, 162)
	pPriorityList.AddAI(pToShieldsUpAI, 1)
	pPriorityList.AddAI(pBattleShieldsDown, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (54, 164)
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
