from bcdebug import debug
import App
import MissionLib

def CreateAI(pShip, pTargetName):
	#########################################
	# Creating PlainAI ShuttleDocking at (324, 50)
	debug(__name__ + ", CreateAI")
	pShuttleDocking = App.PlainAI_Create(pShip, "ShuttleDocking")
	pShuttleDocking.SetScriptModule("EvilShuttleDocking")
	pShuttleDocking.SetInterruptable(1)
	pScript = pShuttleDocking.GetScriptInstance()
	pScript.SetObjectToDockWith(pTargetName)
	pScript.SetSpeed(9)
	# Done creating PlainAI ShuttleDocking
	#########################################
	return pShuttleDocking
