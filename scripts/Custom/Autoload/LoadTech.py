from bcdebug import debug
import App
import Foundation
import techfunc
import sys


mode = Foundation.MutatorDef("New Technology System")
UseTryCatch = 1

App.ET_INPUT_CLEAR_SECONDARY_TARGETS = App.UtopiaModule_GetNextEventType()
App.ET_INPUT_TOGGLE_SECONDARY_TARGET = App.UtopiaModule_GetNextEventType()

class FTBTrigger(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                debug(__name__ + ", __init__")
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.name = name
		self.eventKey = eventKey
		self.dict = dict

        def __call__(self, pObject, pEvent, dict = {}):
                debug(__name__ + ", __call__")
		if not UseTryCatch:
			techfunc.ImportTechs()
		else:
			try:
                		techfunc.ImportTechs()
			except:
				errtype, errinfo, errtrace = sys.exc_info()
				print("Error %s: %s") % (errtype, errinfo)
				import traceback
				fulltrace = traceback.print_exc(errtrace)
				if fulltrace:
					print("Traceback: %s") % (fulltrace)
			

        def Deactivate(self):
                debug(__name__ + ", Deactivate")
                techfunc.pluginsLoaded = {}

FTBTrigger('FTB Trigger', App.ET_MISSION_START, dict = { 'modes': [ mode ] } )

if hasattr(Foundation, "g_kKeyBucket"):
	Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("take secondary Target", "take secondary Target", App.ET_INPUT_TOGGLE_SECONDARY_TARGET, App.KeyboardBinding.GET_INT_EVENT, 1, "Ship", dict = {"modes": [mode]}))
	Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("clear sec Targets", "clear sec Targets", App.ET_INPUT_CLEAR_SECONDARY_TARGETS, App.KeyboardBinding.GET_INT_EVENT, 1, "Ship", dict = {"modes": [mode]}))
