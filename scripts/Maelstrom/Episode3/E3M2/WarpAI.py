import App
def CreateAI(pShip):




	#########################################
	# Creating PlainAI Warp at (54, 36)
	pWarp = App.PlainAI_Create(pShip, "Warp")
	pWarp.SetScriptModule("Warp")
	pWarp.SetInterruptable(1)
	# Done creating PlainAI Warp
	#########################################
	return pWarp
