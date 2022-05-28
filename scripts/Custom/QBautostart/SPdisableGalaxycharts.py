import App
import Foundation
from Custom.Autoload.LoadGalaxyCharts import mode

bWasEnabled = 0


def exit():
	return #disable for now
	global bWasEnabled
	if bWasEnabled:
		print "Re-enabling GalaxyCharts"
		mode.Enable()
		Foundation.SaveConfig()
		bWasEnabled = 0


def init():
	return #disable for now
	global bWasEnabled
	
	pGame = App.Game_GetCurrentGame()
	if mode.IsEnabled():
		if pGame and pGame.GetScript() == "Maelstrom.Maelstrom":
			print "SP mode, Disabling GalaxyCharts"
			mode.Disable()
			Foundation.SaveConfig()
			bWasEnabled = 1
		#elif not App.g_kUtopiaModule.IsMultiplayer():
		#	# fake open/close to init GC
		#	import Custom.GalaxyCharts.GalaxyMapGUI
		#	Custom.GalaxyCharts.GalaxyMapGUI.GMOpenClose(None, None)
		#	Custom.GalaxyCharts.GalaxyMapGUI.GMClose(None, None)
