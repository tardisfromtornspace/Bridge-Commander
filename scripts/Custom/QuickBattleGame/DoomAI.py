import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI Turn at (399, 290)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn1 at (511, 297)
	pTurn1 = App.PlainAI_Create(pShip, "Turn1")
	pTurn1.SetScriptModule("ManeuverLoop")
	pTurn1.SetInterruptable(1)
	pScript = pTurn1.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn1
	#########################################
	#########################################
	# Creating RandomAI Random at (262, 214)
	pRandom = App.RandomAI_Create(pShip, "Random")
	pRandom.SetInterruptable(1)
	# SeqBlock is at (362, 206)
	pRandom.AddAI(pTurn)
	pRandom.AddAI(pTurn1)
	# Done creating RandomAI Random
	#########################################
	#########################################
	# Creating ConditionalAI ConditionFaceShip at (195, 254)
	## Conditions:
	#### Condition FaceShip
	pFaceShip = App.ConditionScript_Create("Conditions.ConditionFacingToward", "ConditionFacingToward", pShip.GetName(),  "player",  20,  App.TGPoint3_GetModelForward())
	## Evaluation function:
	def EvalFunc(bFaceShip):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bFaceShip):
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionFaceShip = App.ConditionalAI_Create(pShip, "ConditionFaceShip")
	pConditionFaceShip.SetInterruptable(1)
	pConditionFaceShip.SetContainedAI(pRandom)
	pConditionFaceShip.AddCondition(pFaceShip)
	pConditionFaceShip.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionFaceShip
	#########################################
	#########################################
	# Creating ConditionalAI ConditionInRange at (129, 297)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 240, pShip.GetName(), "player")
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if (bInRange):
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionInRange = App.ConditionalAI_Create(pShip, "ConditionInRange")
	pConditionInRange.SetInterruptable(1)
	pConditionInRange.SetContainedAI(pConditionFaceShip)
	pConditionInRange.AddCondition(pInRange)
	pConditionInRange.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionInRange
	#########################################
	#########################################
	# Creating CompoundAI Attack at (229, 153)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pFriendlies"), Difficulty = 0.5, FollowTargetThroughWarp = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn_1 at (241, 10)
	pTurn_1 = App.PlainAI_Create(pShip, "Turn_1")
	pTurn_1.SetScriptModule("ManeuverLoop")
	pTurn_1.SetInterruptable(1)
	pScript = pTurn_1.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_1
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (338, 9)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (434, 9)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (523, 9)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (434, 182)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (517, 124)
	pFlyPointlessly.AddAI(pTurn_1)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (296, 97)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (430, 141)
	pSequence.AddAI(pFlyPointlessly)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (53, 176)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (182, 83)
	pPriorityList.AddAI(pConditionInRange, 1)
	pPriorityList.AddAI(pAttack, 2)
	pPriorityList.AddAI(pSequence, 3)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (15, 329)
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
