# USS Defiant's AI which moves rather pointlesly

# by USS Sovereign

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI DS9FXDefiantAI at (59, 413)
	import AI.Compound.FedAttack
	pDS9FXDefiantAI = AI.Compound.FedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXDefiantAI
	#########################################
	#########################################
	# Creating PlainAI Forward at (161, 9)
	pForward = App.PlainAI_Create(pShip, "Forward")
	pForward.SetScriptModule("GoForward")
	pForward.SetInterruptable(1)
	pScript = pForward.GetScriptInstance()
	pScript.SetImpulse(4)
	# Done creating PlainAI Forward
	#########################################
	#########################################
	# Creating PlainAI MoveLeft at (258, 9)
	pMoveLeft = App.PlainAI_Create(pShip, "MoveLeft")
	pMoveLeft.SetScriptModule("ManeuverLoop")
	pMoveLeft.SetInterruptable(1)
	pScript = pMoveLeft.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 1.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelLeft())
	# Done creating PlainAI MoveLeft
	#########################################
	#########################################
	# Creating PlainAI MoveRight at (343, 7)
	pMoveRight = App.PlainAI_Create(pShip, "MoveRight")
	pMoveRight.SetScriptModule("ManeuverLoop")
	pMoveRight.SetInterruptable(1)
	pScript = pMoveRight.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 1.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelRight())
	# Done creating PlainAI MoveRight
	#########################################
	#########################################
	# Creating RandomAI Sequences at (144, 231)
	pSequences = App.RandomAI_Create(pShip, "Sequences")
	pSequences.SetInterruptable(1)
	# SeqBlock is at (194, 198)
	pSequences.AddAI(pForward)
	pSequences.AddAI(pMoveLeft)
	pSequences.AddAI(pMoveRight)
	# Done creating RandomAI Sequences
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (280, 277)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (313, 227)
	pSequence.AddAI(pSequences)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (53, 127)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (144, 346)
	pPriorityList.AddAI(pDS9FXDefiantAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (17, 233)
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
