import App
import Foundation

def KeyBindings():

	pThrusterUp = App.WC_I
	pThrusterDown = App.WC_K
	pThrusterLeft = App.WC_J
	pThrusterRight = App.WC_L

	return pThrusterUp, pThrusterDown, pThrusterLeft, pThrusterRight

def AddKeyBind(KeyName, pEvent, EventInt, eType, Group, mode):
        if not hasattr(Foundation, "g_kKeyBucket"):
                return
        Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(KeyName, KeyName, pEvent, eType, EventInt, Group, dict = {"modes": [mode]}))
