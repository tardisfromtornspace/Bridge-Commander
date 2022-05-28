import App
import Foundation
import MissionLib
from Custom.Autoload.LoadGalaxyCharts import mode




class GCD(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.bWasEnabled = 0

	def __call__(self, pObject, pEvent, dict = {}):
		pGame = App.Game_GetCurrentGame()
		if mode.IsEnabled():
			if MissionLib.GetMission() and MissionLib.GetMission().GetScript() != "QuickBattle.QuickBattle":
				# only enable in QB right now
				print "non-QB-mode, Disabling GalaxyCharts"
				mode.Deactivate()
				mode.Disable()
				Foundation.SaveConfig()
				self.bWasEnabled = 1
        def Deactivate(self):
		if self.bWasEnabled:
			print "Re-enabling GalaxyCharts"
			mode.Enable()
			Foundation.SaveConfig()
			bWasEnabled = 0

		
oGCD = GCD('GalaxyCharts Disable', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )
