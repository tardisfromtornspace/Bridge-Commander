# USS Lakota's AI which also moves rather pointlesly and later it circles USS Defiant making in appear they are exchanging cargo or something

# by USS Sovereign

import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI DS9FXLakotaAI at (159, 275)
	import AI.Compound.NonFedAttack
	pDS9FXLakotaAI = AI.Compound.NonFedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXLakotaAI
	#########################################
	#########################################
	# Creating PlainAI Forward at (186, 51)
	pForward = App.PlainAI_Create(pShip, "Forward")
	pForward.SetScriptModule("GoForward")
	pForward.SetInterruptable(1)
	pScript = pForward.GetScriptInstance()
	pScript.SetImpulse(4)
	# Done creating PlainAI Forward
	#########################################
	#########################################
	# Creating PlainAI CircleUSSDefiant at (284, 44)
	pCircleUSSDefiant = App.PlainAI_Create(pShip, "CircleUSSDefiant")
	pCircleUSSDefiant.SetScriptModule("IntelligentCircleObject")
	pCircleUSSDefiant.SetInterruptable(1)
	pScript = pCircleUSSDefiant.GetScriptInstance()
	pScript.SetFollowObjectName("USS Defiant")
	pScript.SetRoughDistances(fNearDistance = 10, fFarDistance = 20)
	pScript.SetCircleSpeed(fSpeed = 4.0)
	# Done creating PlainAI CircleUSSDefiant
	#########################################
	#########################################
	# Creating PlainAI MoveForwardAgain at (397, 47)
	pMoveForwardAgain = App.PlainAI_Create(pShip, "MoveForwardAgain")
	pMoveForwardAgain.SetScriptModule("GoForward")
	pMoveForwardAgain.SetInterruptable(1)
	pScript = pMoveForwardAgain.GetScriptInstance()
	pScript.SetImpulse(4)
	# Done creating PlainAI MoveForwardAgain
	#########################################
	#########################################
	# Creating RandomAI AISeq at (81, 98)
	pAISeq = App.RandomAI_Create(pShip, "AISeq")
	pAISeq.SetInterruptable(1)
	# SeqBlock is at (313, 108)
	pAISeq.AddAI(pForward)
	pAISeq.AddAI(pCircleUSSDefiant)
	pAISeq.AddAI(pMoveForwardAgain)
	# Done creating RandomAI AISeq
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (353, 229)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (114, 234)
	pSequence.AddAI(pAISeq)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (268, 470)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (260, 340)
	pPriorityList.AddAI(pDS9FXLakotaAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (177, 385)
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
