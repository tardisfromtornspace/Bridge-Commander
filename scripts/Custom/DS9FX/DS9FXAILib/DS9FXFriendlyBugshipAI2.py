# by USS Sovereign and yet another Bugship AI, every bugship has a different AI

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pFriendlyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI DS9FXBugship2AI at (154, 246)
	import AI.Compound.FedAttack
	pDS9FXBugship2AI = AI.Compound.FedAttack.CreateAI(pShip, pFriendlyGroup)
	# Done creating CompoundAI DS9FXBugship2AI
	#########################################
	#########################################
	# Creating PlainAI MoveLeft at (50, 43)
	pMoveLeft = App.PlainAI_Create(pShip, "MoveLeft")
	pMoveLeft.SetScriptModule("ManeuverLoop")
	pMoveLeft.SetInterruptable(1)
	pScript = pMoveLeft.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 1.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelLeft())
	# Done creating PlainAI MoveLeft
	#########################################
	#########################################
	# Creating PlainAI GoFwd at (169, 22)
	pGoFwd = App.PlainAI_Create(pShip, "GoFwd")
	pGoFwd.SetScriptModule("GoForward")
	pGoFwd.SetInterruptable(1)
	pScript = pGoFwd.GetScriptInstance()
	pScript.SetImpulse(1)
	# Done creating PlainAI GoFwd
	#########################################
	#########################################
	# Creating PlainAI MoveRight at (257, 44)
	pMoveRight = App.PlainAI_Create(pShip, "MoveRight")
	pMoveRight.SetScriptModule("ManeuverLoop")
	pMoveRight.SetInterruptable(1)
	pScript = pMoveRight.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 1.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelRight())
	# Done creating PlainAI MoveRight
	#########################################
	#########################################
	# Creating RandomAI AIMovementSeq at (85, 147)
	pAIMovementSeq = App.RandomAI_Create(pShip, "AIMovementSeq")
	pAIMovementSeq.SetInterruptable(1)
	# SeqBlock is at (134, 108)
	pAIMovementSeq.AddAI(pMoveLeft)
	pAIMovementSeq.AddAI(pGoFwd)
	pAIMovementSeq.AddAI(pMoveRight)
	# Done creating RandomAI AIMovementSeq
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (211, 396)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (236, 328)
	pSequence.AddAI(pAIMovementSeq)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (56, 260)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (137, 337)
	pPriorityList.AddAI(pDS9FXBugship2AI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (80, 494)
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
