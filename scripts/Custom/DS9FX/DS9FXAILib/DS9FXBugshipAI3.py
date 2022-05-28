# by USS Sovereign a 3rd Bugship AI

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pFriendlyGroup = pMission.GetFriendlyGroup ()
	#########################################
	# Creating CompoundAI DS9FXBughshipAI3 at (294, 183)
	import AI.Compound.BasicAttack
	pDS9FXBughshipAI3 = AI.Compound.BasicAttack.CreateAI(pShip, pFriendlyGroup, Easy_Difficulty = 1.0, Easy_MaxFiringRange = 1000.0, Easy_AvoidTorps = 0, Easy_AggressivePulseWeapons = 0, Easy_ChooseSubsystemTargets = 0, Difficulty = 1.0, MaxFiringRange = 1000.0, AvoidTorps = 0, AggressivePulseWeapons = 0, ChooseSubsystemTargets = 0, Hard_Difficulty = 1.0, Hard_MaxFiringRange = 1000.0, Hard_AvoidTorps = 0, Hard_AggressivePulseWeapons = 0, Hard_ChooseSubsystemTargets = 0)
	# Done creating CompoundAI DS9FXBughshipAI3
	#########################################
	#########################################
	# Creating PlainAI MoveFWD at (211, 67)
	pMoveFWD = App.PlainAI_Create(pShip, "MoveFWD")
	pMoveFWD.SetScriptModule("GoForward")
	pMoveFWD.SetInterruptable(1)
	pScript = pMoveFWD.GetScriptInstance()
	pScript.SetImpulse(2)
	# Done creating PlainAI MoveFWD
	#########################################
	#########################################
	# Creating PlainAI Loop at (333, 67)
	pLoop = App.PlainAI_Create(pShip, "Loop")
	pLoop.SetScriptModule("ManeuverLoop")
	pLoop.SetInterruptable(1)
	pScript = pLoop.GetScriptInstance()
	pScript.SetLoopFraction(fFraction = 2.0)
	pScript.SetTurnAxis(vAxis = App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Loop
	#########################################
	#########################################
	# Creating RandomAI AISeq at (50, 116)
	pAISeq = App.RandomAI_Create(pShip, "AISeq")
	pAISeq.SetInterruptable(1)
	# SeqBlock is at (180, 160)
	pAISeq.AddAI(pMoveFWD)
	pAISeq.AddAI(pLoop)
	# Done creating RandomAI AISeq
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (310, 279)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (117, 202)
	pSequence.AddAI(pAISeq)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (137, 458)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (252, 419)
	pPriorityList.AddAI(pDS9FXBughshipAI3, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (171, 588)
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
