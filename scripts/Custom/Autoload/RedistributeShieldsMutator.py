import Foundation
import App


#############################################################################################
#                                                                                           #
# Here we create the "Redistribute Shields" Main menu key config.							#
#                                                                                           #
#                                                                                           #
#                                                                                           #
#############################################################################################

mode = Foundation.MutatorDef("Redistribute Shields")

ET_KEY_EVENT = App.UtopiaModule_GetNextEventType()
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Redistribute Shields", "Redistribute Shields", ET_KEY_EVENT, App.KeyboardBinding.GET_INT_EVENT, 1, "General", dict = {"modes": [mode]}))