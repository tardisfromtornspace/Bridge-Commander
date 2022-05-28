import App

def CreateAI(pShip, pPlanet, pPlanet2):
	print pShip.GetName(), pPlanet.GetName(), pPlanet2.GetName()



	#########################################
	# Creating PlainAI FlyToPlanet at (262, 62)
	pFlyToPlanet = App.PlainAI_Create(pShip, "FlyToPlanet")
	pFlyToPlanet.SetScriptModule("Intercept")
	pFlyToPlanet.SetInterruptable(1)
	pScript = pFlyToPlanet.GetScriptInstance()
	pScript.SetTargetObjectName(pPlanet.GetName())
	pScript.SetInterceptDistance(fDistance = 285.0)
	pScript.SetAddObjectRadius(bUseRadius = 1)
	# Done creating PlainAI FlyToPlanet
	#########################################
	#########################################
	# Creating ConditionalAI CloseEnough at (261, 138)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 200, pShip.GetName(), pPlanet.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bInRange:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pCloseEnough = App.ConditionalAI_Create(pShip, "CloseEnough")
	pCloseEnough.SetInterruptable(1)
	pCloseEnough.SetContainedAI(pFlyToPlanet)
	pCloseEnough.AddCondition(pInRange)
	pCloseEnough.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseEnough
	#########################################
	#########################################
	# Creating PlainAI FlyToPlanet_2 at (254, 374)
	pFlyToPlanet_2 = App.PlainAI_Create(pShip, "FlyToPlanet_2")
	pFlyToPlanet_2.SetScriptModule("Intercept")
	pFlyToPlanet_2.SetInterruptable(1)
	pScript = pFlyToPlanet_2.GetScriptInstance()
	pScript.SetTargetObjectName(pPlanet2.GetName())
	pScript.SetInterceptDistance(fDistance = 285.0)
	pScript.SetAddObjectRadius(bUseRadius = 1)
	# Done creating PlainAI FlyToPlanet_2
	#########################################
	#########################################
	# Creating ConditionalAI CloseEnough_2 at (257, 291)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 200, pShip.GetName(), pPlanet2.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bInRange:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pCloseEnough_2 = App.ConditionalAI_Create(pShip, "CloseEnough_2")
	pCloseEnough_2.SetInterruptable(1)
	pCloseEnough_2.SetContainedAI(pFlyToPlanet_2)
	pCloseEnough_2.AddCondition(pInRange)
	pCloseEnough_2.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseEnough_2
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (48, 195)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(1)
	# SeqBlock is at (151, 231)
	pSequence.AddAI(pCloseEnough)
	pSequence.AddAI(pCloseEnough_2)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (50, 50)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pSequence)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
