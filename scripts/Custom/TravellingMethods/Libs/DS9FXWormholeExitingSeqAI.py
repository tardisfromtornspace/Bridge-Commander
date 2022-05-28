# by USS Sovereign, move forward at high impulse

import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI Forward at (278, 71)
	pForward = App.PlainAI_Create(pShip, "Forward")
	pForward.SetScriptModule("GoForward")
	pForward.SetInterruptable(1)
	pScript = pForward.GetScriptInstance()
	pScript.SetImpulse(9)
	# Done creating PlainAI Forward
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (196, 183)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (306, 132)
	pPriorityList.AddAI(pForward, 1)
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
