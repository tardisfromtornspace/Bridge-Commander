import App

def CreateAI(pShip):
	#########################################
	# Creating CompoundAI DefendStation at (50, 50)
	import AI.Compound.DefendNoWarpOut
	pDefendStation = AI.Compound.DefendNoWarpOut.CreateAI(pShip)
	# Done creating CompoundAI DefendStation
	#########################################
	#########################################
	# Creating PlainAI MoveForward at (432, 132)
	# pMoveForward = App.PlainAI_Create(pShip, "MoveForward")
	# pMoveForward.SetScriptModule("GoForward")
	# pMoveForward.SetInterruptable(1)
	# pScript = pMoveForward.GetScriptInstance()
	# pScript.SetImpulse(fImpulse = 19.0)
	# Done creating PlainAI MoveForward
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (230, 88)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (346, 79)
	pPriorityList.AddAI(pDefendStation, 1)
	# pPriorityList.AddAI(pMoveForward, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating SequenceAI Forever at (181, 203)
	pForever = App.SequenceAI_Create(pShip, "Forever")
	pForever.SetInterruptable(1)
	pForever.SetLoopCount(-1)
	pForever.SetResetIfInterrupted(1)
	pForever.SetDoubleCheckAllDone(0)
	pForever.SetSkipDormant(0)
	# SeqBlock is at (260, 145)
	pForever.AddAI(pPriorityList)
	# Done creating SequenceAI Forever
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (49, 197)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pForever)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles
