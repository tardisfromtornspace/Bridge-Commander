# by USS Sovereign


import App
import MissionLib

def CreateAI(pShip):
        pMission = MissionLib.GetMission ()
	pEnemyGroup = pMission.GetEnemyGroup ()
	#########################################
	# Creating CompoundAI DS9FXGenericAI at (148, 290)
	import AI.Compound.FedAttack
	pDS9FXGenericAI = AI.Compound.FedAttack.CreateAI(pShip, pEnemyGroup)
	# Done creating CompoundAI DS9FXGenericAI
	#########################################
	#########################################
	# Creating PlainAI Forward1 at (167, 146)
	pForward1 = App.PlainAI_Create(pShip, "Forward1")
	pForward1.SetScriptModule("GoForward")
	pForward1.SetInterruptable(1)
	pScript = pForward1.GetScriptInstance()
	pScript.SetImpulse(3)
	# Done creating PlainAI Forward1
	#########################################
	#########################################
	# Creating PlainAI Forward2 at (190, 102)
	pForward2 = App.PlainAI_Create(pShip, "Forward2")
	pForward2.SetScriptModule("GoForward")
	pForward2.SetInterruptable(1)
	pScript = pForward2.GetScriptInstance()
	pScript.SetImpulse(7)
	# Done creating PlainAI Forward2
	#########################################
	#########################################
	# Creating PlainAI Stay at (299, 84)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(1)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating PlainAI Forward3 at (400, 101)
	pForward3 = App.PlainAI_Create(pShip, "Forward3")
	pForward3.SetScriptModule("GoForward")
	pForward3.SetInterruptable(1)
	pScript = pForward3.GetScriptInstance()
	pScript.SetImpulse(2)
	# Done creating PlainAI Forward3
	#########################################
	#########################################
	# Creating RandomAI AISequence at (413, 179)
	pAISequence = App.RandomAI_Create(pShip, "AISequence")
	pAISequence.SetInterruptable(1)
	# SeqBlock is at (315, 179)
	pAISequence.AddAI(pForward1)
	pAISequence.AddAI(pForward2)
	pAISequence.AddAI(pStay)
	pAISequence.AddAI(pForward3)
	# Done creating RandomAI AISequence
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (288, 289)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (397, 281)
	pSequence.AddAI(pAISequence)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (209, 371)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (244, 338)
	pPriorityList.AddAI(pDS9FXGenericAI, 1)
	pPriorityList.AddAI(pSequence, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (217, 432)
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
