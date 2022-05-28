import App
import MissionLib

MODINFO = { "needBridge": 0 }

def init():
	pMission = MissionLib.GetMission()
	
	if App.g_kUtopiaModule.IsMultiplayer():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, pMission, "Custom.QBautostart.Libs.LibCloakFire.ProcessMessageHandler")
