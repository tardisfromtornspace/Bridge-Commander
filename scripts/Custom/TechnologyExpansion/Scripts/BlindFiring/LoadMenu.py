# Setup function - does whatever needed to be in LoadBridge.py
# This shouldn't need anything more...
import App
import Bridge.BridgeUtils
import Foundation

def LoadMenu():

        global g_BFRunOnce

        try:
            if (g_BFRunOnce == 1):
                return
            else:
                g_BFRunOnce = 1
        except:
            g_BFRunOnce = 1

	import Custom.TechnologyExpansion.Scripts.LoadGroupMenu
	Custom.TechnologyExpansion.Scripts.LoadGroupMenu.LoadGroupMenu()

	pSpecialMenu = Custom.TechnologyExpansion.Scripts.LoadGroupMenu.g_SpecialMenu
	
        import Custom.TechnologyExpansion.Scripts.BlindFiring.BlindFiring
        Custom.TechnologyExpansion.Scripts.BlindFiring.BlindFiring.BFCreateMenu(pSpecialMenu)


def CreateKeys(mode):
        import Custom.TechnologyExpansion.Scripts.BlindFiring.BlindFiring
        Custom.TechnologyExpansion.Scripts.BlindFiring.BlindFiring.CreateKeys(mode)


def AddKeyBind(KeyName, pEvent, EventInt, eType, Group, mode):
        if not hasattr(Foundation, "g_kKeyBucket"):
                return
        Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(KeyName, KeyName, pEvent, eType, EventInt, Group, dict = {"modes": [mode]}))
