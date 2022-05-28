# This script fixes the issue when small ships explode and the game crashes

# by Sov

# Imports
import App
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Functions
def FixExplosions(pObject, pEvent):
    reload(DS9FXSavedConfig)
    if not DS9FXSavedConfig.NanoFXExplosionFix == 1:
        return
    
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return 0

    pRadius = pShip.GetRadius()
    if not pRadius:
        return 0
    
    if pRadius < 0.1:
        scale = 0.1
        pShip.SetScale(scale)

