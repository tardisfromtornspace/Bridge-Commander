from bcdebug import debug
import App

def Setup():
        debug(__name__ + ", Setup")
        return
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_KEYBOARD, App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission(), "ftb.SecondTarget.ToggleForm")
#	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_INPUT_TALK_TO_TACTICAL, App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission(), "ftb.SecondTarget.ToggleForm")
#	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_INPUT_TALK_TO_TACTICAL, App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission(), "ftb.SecondTarget.ToggleForm")
#	import ftb.SecondTarget
#	ftb.SecondTarget.Init()
	return
