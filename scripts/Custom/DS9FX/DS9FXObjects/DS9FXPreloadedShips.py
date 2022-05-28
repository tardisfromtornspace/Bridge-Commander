# We'll preload needed ship models to prevent any problems :) well speed up game loading

# by USS Sovereign

# Imports
import loadspacehelper
from Custom.DS9FX.DS9FXLib import DS9FXShips
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Preloaded models
def PreLoadEverything(pMission):
        if not pMission:
                return

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.ModelPreloadingSelection == 1:                   
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Excalibur, 1)
                loadspacehelper.PreloadShip(DS9FXShips.DS9, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Defiant, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Miranda, 2)
                loadspacehelper.PreloadShip(DS9FXShips.Nebula, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Bugship, 17)
                loadspacehelper.PreloadShip(DS9FXShips.Cone, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone2, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone3, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone4, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone5, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone6, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone7, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone8, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone9, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone10, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone11, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone12, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Cone13, 4)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole2, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Lakota, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Dummy, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Distortion, 1)
                loadspacehelper.PreloadShip(DS9FXShips.DomBC, 10)
                loadspacehelper.PreloadShip(DS9FXShips.Comet, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole3, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole4, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole5, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole6, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole7, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Wormhole8, 1)
                loadspacehelper.PreloadShip(DS9FXShips.Vortex, 30)
                loadspacehelper.PreloadShip(DS9FXShips.Vortex2, 30)
                loadspacehelper.PreloadShip(DS9FXShips.Danube1, 7)
                loadspacehelper.PreloadShip(DS9FXShips.Danube2, 7)
                loadspacehelper.PreloadShip(DS9FXShips.Peregrine, 7)

        else:
                return
