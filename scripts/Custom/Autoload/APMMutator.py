import App
import Foundation

mode = Foundation.MutatorDef("Advanced Power control")

ET_KEY_EVENT = App.UtopiaModule_GetNextEventType()
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Advanced Power control", "Advanced Power control", ET_KEY_EVENT, App.KeyboardBinding.GET_INT_EVENT, 1, "General", dict = {"modes": [mode]}))
