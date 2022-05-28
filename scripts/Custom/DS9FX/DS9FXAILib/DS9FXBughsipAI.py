# by USS Sovereign Bugship 1 AI, nothing fancy over here and Intensive Scan AI usage isn't located over here anymore. It's in DS9FXmain.py
# from now on

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pFriendlyGroup = pMission.GetFriendlyGroup ()
	#########################################
	# Creating CompoundAI DS9FXBugshipAI at (196, 134)
	import AI.Compound.NonFedAttack
	pDS9FXBugshipAI = AI.Compound.NonFedAttack.CreateAI(pShip, pFriendlyGroup)
	# Done creating CompoundAI DS9FXBugshipAI
	#########################################
	#########################################
	# Creating PlainAI MoveForward at (103, 17)
	pMoveForward = App.PlainAI_Create(pShip, "MoveForward")
	pMoveForward.SetScriptModule("GoForward")
	pMoveForward.SetInterruptable(1)
	pScript = pMoveForward.GetScriptInstance()
	pScript.SetImpulse(2)
	# Done creating PlainAI MoveForward
	#########################################
	#########################################
	# Creating PlainAI Stop at (201, 11)
	pStop = App.PlainAI_Create(pShip, "Stop")
	pStop.SetScriptModule("GoForward")
	pStop.SetInterruptable(1)
	pScript = pStop.GetScriptInstance()
	pScript.SetImpulse(0)
	# Done creating PlainAI Stop
	#########################################
	#########################################
	# Creating PlainAI Turn at (298, 8)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 2.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI MoveForward2 at (358, 50)
	pMoveForward2 = App.PlainAI_Create(pShip, "MoveForward2")
	pMoveForward2.SetScriptModule("GoForward")
	pMoveForward2.SetInterruptable(1)
	pScript = pMoveForward2.GetScriptInstance()
	pScript.SetImpulse(1)
	# Done creating PlainAI MoveForward2
	#########################################
	#########################################
	# Creating RandomAI AISequence at (53, 116)
	pAISequence = App.RandomAI_Create(pShip, "AISequence")
	pAISequence.SetInterruptable(1)
	# SeqBlock is at (184, 94)
	pAISequence.AddAI(pMoveForward)
	pAISequence.AddAI(pStop)
	pAISequence.AddAI(pTurn)
	pAISequence.AddAI(pMoveForward2)
	# Done creating RandomAI AISequence
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (176, 284)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (243, 255)
	pSequence.AddAI(pAISequence)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (57, 256)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (172, 232)
	pPriorityList.AddAI(pDS9FXBugshipAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
        return pPriorityList

	#########################################
	# Creating PreprocessingAI AvoidObstacles at (76, 417)
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
