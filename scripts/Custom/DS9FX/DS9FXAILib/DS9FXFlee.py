# by USS Sovereign


import App

def CreateAI(pShip):
	#########################################
	# Creating PlainAI Flee at (232, 110)
	pFlee = App.PlainAI_Create(pShip, "Flee")
	pFlee.SetScriptModule("Warp")
	pFlee.SetInterruptable(1)
	pScript = pFlee.GetScriptInstance()
	pScript.WarpBlindly(bWarpImmediately = 1)
	pScript.WarpBlindlyNoCollisionsIfImpulseDisabled(bWarpBlindly = 1)
	# Done creating PlainAI Flee
	#########################################
	return pFlee
