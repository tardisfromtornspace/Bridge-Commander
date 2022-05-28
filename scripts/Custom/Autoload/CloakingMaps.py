from bcdebug import debug
# Cloaking Maps Bridge Plugin Extension
# By MLeo
#
# Map key:
# CloakingMaps for when it cloaks
# DecloakingMaps for when it decloaks

import App
import Foundation

oBridgePlugin = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")

NonSerializedObjects = (
"oBridgePlugin"
)

class CloakingMaps(Foundation.BridgePluginDef):
    def __call__(self, Plug, pBridgeSet, oBridgeInfo):
        debug(__name__ + ", __call__")
        pass
    def PlayerCreated(self, Plug, pBridgeSet, oBridgeInfo, pShip):
        debug(__name__ + ", PlayerCreated")
        if oBridgeInfo.__dict__.has_key("CloakingMaps"):
            pShip.AddPythonFuncHandlerForInstance(App.ET_START_CLOAKING, __name__ + ".HandleCloaking")
        #if oBridgeInfo.__dict__.has_key("DecloakingMaps"):
        #    pShip.AddPythonFuncHandlerForInstance(App.ET_START_DECLOAKING, __name__ + ".HandleDecloaking")

oCloakingMaps = CloakingMaps("Cloaking Maps Bridge Plugin")

def HandleCloaking(pObject, pEvent):
    debug(__name__ + ", HandleCloaking")
    for key in oBridgePlugin.oBridgeInfo.CloakingMaps.keys():
        oBridgePlugin.SwitchMaps(key, oBridgePlugin.oBridgeInfo.CloakingMaps[key])
    if (pObject and pEvent):
        pObject.CallNextHandler(pEvent)

def HandleDecloaking(pObject, pEvent):
    debug(__name__ + ", HandleDecloaking")
    for key in oBridgePlugin.oBridgeInfo.DecloakingMaps.keys():
        oBridgePlugin.SwitchMaps(key, oBridgePlugin.oBridgeInfo.DecloakingMaps[key])
    if (pObject and pEvent):
        pObject.CallNextHandler(pEvent)

