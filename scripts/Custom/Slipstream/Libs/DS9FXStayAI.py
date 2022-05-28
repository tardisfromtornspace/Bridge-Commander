# by USS Sovereign, a simple AI which stops a ship

import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI Stay at (257, 47)
	pStay = App.PlainAI_Create(pShip, "Stay")
	pStay.SetScriptModule("Stay")
	pStay.SetInterruptable(1)
	# Done creating PlainAI Stay
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (235, 182)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (247, 119)
	pPriorityList.AddAI(pStay, 1)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (88, 190)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (205, 230)
	pSequence.AddAI(pPriorityList)
	# Done creating SequenceAI Sequence
	#########################################
	return pSequence
