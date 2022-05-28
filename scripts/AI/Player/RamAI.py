import App

def CreateAI(pShip, pTargetName, Speed = 9):
	#########################################
	# Creating PlainAI RamAI at (205, 50)
	pRamAI = App.PlainAI_Create(pShip, "RamAI")
	pRamAI.SetScriptModule("Ram")
	pRamAI.SetInterruptable(1)
	pScript = pRamAI.GetScriptInstance()
	pScript.SetTargetObjectName(pTargetName)
	pScript.SetMaximumSpeed(Speed)
	# Done creating PlainAI RamAI
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (50, 50)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 57)
	pPriorityList.AddAI(pRamAI, 1)
	# Done creating PriorityListAI PriorityList
	#########################################
	return pPriorityList
