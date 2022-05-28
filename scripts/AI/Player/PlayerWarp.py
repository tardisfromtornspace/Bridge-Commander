from bcdebug import debug
import App
def CreateAI(pShip, pWarpSequence):
	#########################################
	# Creating PlainAI Warp at (231, 151)
	debug(__name__ + ", CreateAI")
	pWarp = App.PlainAI_Create(pShip, "Warp")
	pWarp.SetScriptModule("Warp")
	pWarp.SetInterruptable(1)
	pScript = pWarp.GetScriptInstance()
	pScript.SetSequence(pWarpSequence)
	# Done creating PlainAI Warp
	#########################################
	return pWarp
