import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI Cruise at (288, 109)
	pCruise = App.PlainAI_Create(pShip, "Cruise")
	pCruise.SetScriptModule("FollowWaypoints")
	pCruise.SetInterruptable(1)
	pScript = pCruise.GetScriptInstance()
	pScript.SetTargetWaypointName("Comet Location")
	# Done creating PlainAI Cruise
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (294, 258)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(-1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(1)
	# SeqBlock is at (320, 192)
	pSequence.AddAI(pCruise)
	# Done creating SequenceAI Sequence
	#########################################
	return pSequence
