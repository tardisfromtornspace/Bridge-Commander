import App
import Foundation
from LoadEngineeringExtension import mode

ET_KEY_EVENT = App.UtopiaModule_GetNextEventType()
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Point Defence", "Point Defence", ET_KEY_EVENT, App.KeyboardBinding.GET_INT_EVENT, 1, "Ship", dict = {"modes": [mode]}))
