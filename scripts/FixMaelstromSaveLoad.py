from bcdebug import debug
import App
import MissionLib


def EnableSelectedSPMods(pObject, pEvent):
	# Enable NanoFX
	debug(__name__ + ", EnableSelectedSPMods")
	import Custom.Autoload.LoadNanoFX
	mode = Custom.Autoload.LoadNanoFX.mode
	mode.Activate()


def DoPreSaveGameStuff():
        debug(__name__ + ", DoPreSaveGameStuff")
        print("Doing Pre Save game stuff")


def DoPostSaveGameStuff():
        debug(__name__ + ", DoPostSaveGameStuff")
        print("Doing Post Save game stuff")
        MissionLib.CreateTimer(App.Game_GetNextEventType(), __name__ + ".EnableSelectedSPMods", App.g_kUtopiaModule.GetGameTime() + 5.0, 0, 0)

