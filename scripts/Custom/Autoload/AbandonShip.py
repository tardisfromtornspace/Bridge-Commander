import App
import Foundation
from LoadEngineeringExtension import mode

Foundation.MutatorDef("AI Abandon Ship")

ET_KEY_EVENT = App.UtopiaModule_GetNextEventType()
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Abandon Ship", "Abandon Ship", ET_KEY_EVENT, App.KeyboardBinding.GET_INT_EVENT, 1, "Ship", dict = {"modes": [mode]}))
