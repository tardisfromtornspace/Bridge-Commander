# by USS Sovereign, an AI for an incoming enemy AI ships. It's a generic one, only cause I'm too lazy to make more of them!

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pFriendlyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI DS9RandomAttackAI at (56, 526)
	import AI.Compound.FedAttack
	pDS9RandomAttackAI = AI.Compound.FedAttack.CreateAI(pShip, pFriendlyGroup)
	# Done creating CompoundAI DS9RandomAttackAI
	#########################################
	#########################################
	# Creating PlainAI Fwd at (183, 54)
	pFwd = App.PlainAI_Create(pShip, "Fwd")
	pFwd.SetScriptModule("GoForward")
	pFwd.SetInterruptable(1)
	pScript = pFwd.GetScriptInstance()
	pScript.SetImpulse(3)
	# Done creating PlainAI Fwd
	#########################################
	#########################################
	# Creating RandomAI MovementSeq at (46, 138)
	pMovementSeq = App.RandomAI_Create(pShip, "MovementSeq")
	pMovementSeq.SetInterruptable(1)
	# SeqBlock is at (100, 80)
	pMovementSeq.AddAI(pFwd)
	# Done creating RandomAI MovementSeq
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (85, 274)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (139, 227)
	pSequence.AddAI(pMovementSeq)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (144, 501)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (81, 401)
	pPriorityList.AddAI(pDS9RandomAttackAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (169, 581)
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
