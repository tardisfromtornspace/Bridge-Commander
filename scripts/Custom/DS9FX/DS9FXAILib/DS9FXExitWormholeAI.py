# by USS Sovereign, a very basic AI which moves a ship forward at impulse = 4

import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI MoveForward at (278, 71)
	pMoveForward = App.PlainAI_Create(pShip, "MoveForward")
	pMoveForward.SetScriptModule("GoForward")
	pMoveForward.SetInterruptable(1)
	pScript = pMoveForward.GetScriptInstance()
	pScript.SetImpulse(4)
	# Done creating PlainAI MoveForward
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (196, 183)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (306, 132)
	pPriorityList.AddAI(pMoveForward, 1)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (46, 165)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (152, 192)
	pSequence.AddAI(pPriorityList)
	# Done creating SequenceAI Sequence
	#########################################
	return pSequence
