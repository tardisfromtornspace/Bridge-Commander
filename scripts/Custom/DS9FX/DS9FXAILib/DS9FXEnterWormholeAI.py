# An AI which simply allows the player to enter the Wormhole

# by USS Sovereign

import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI InterceptWormhole at (112, 93)
	pInterceptWormhole = App.PlainAI_Create(pShip, "InterceptWormhole")
	pInterceptWormhole.SetScriptModule("Intercept")
	pInterceptWormhole.SetInterruptable(1)
	pScript = pInterceptWormhole.GetScriptInstance()
	pScript.SetTargetObjectName("Bajoran Wormhole")
	pScript.SetMaximumSpeed(fSpeed = 5)
	pScript.SetInterceptDistance(fDistance = 8)
	pScript.SetMoveInFront(bMoveInFront = 1)
	# Done creating PlainAI InterceptWormhole
	#########################################
	#########################################
	# Creating PlainAI EnterWormhole at (334, 82)
	pEnterWormhole = App.PlainAI_Create(pShip, "EnterWormhole")
	pEnterWormhole.SetScriptModule("Ram")
	pEnterWormhole.SetInterruptable(1)
	pScript = pEnterWormhole.GetScriptInstance()
	pScript.SetTargetObjectName("Bajoran Wormhole Dummy")
	pScript.SetMaximumSpeed(fSpeed = 5)
	# Done creating PlainAI EnterWormhole
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (208, 295)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(0)
	# SeqBlock is at (212, 174)
	pPriorityList.AddAI(pInterceptWormhole, 1)
	pPriorityList.AddAI(pEnterWormhole, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (263, 395)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(0)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (349, 363)
	pSequence.AddAI(pPriorityList)
	# Done creating SequenceAI Sequence
	#########################################
	return pSequence
