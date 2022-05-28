from bcdebug import debug
import App
import Foundation
import techfunc
import MissionLib
import Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu

mode = Foundation.MutatorDef("Blind Firing")


class TechExpansion(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                debug(__name__ + ", __init__")
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")

		# don't do anything in MP
		pMission = MissionLib.GetMission()
		import string
		if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
			return
		# No need to start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return
		
		Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu.LoadMenu()

TechExpansion('TechExpansion', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )

Custom.TechnologyExpansion.Scripts.BlindFiring.LoadMenu.CreateKeys(mode)
