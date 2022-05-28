# A simple ramming AI.

# by USS Sovereign

import App
def CreateAI(pShip):
	#########################################
	# Creating PlainAI Ramming at (193, 59)
	pRamming = App.PlainAI_Create(pShip, "Ramming")
	pRamming.SetScriptModule("Ram")
	pRamming.SetInterruptable(1)
	pScript = pRamming.GetScriptInstance()
	pScript.SetTargetObjectName("USS Odyssey")
	# Done creating PlainAI Ramming
	#########################################
	return pRamming
