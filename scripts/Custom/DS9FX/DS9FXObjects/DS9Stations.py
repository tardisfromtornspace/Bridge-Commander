# Over here we'll save the locations of stations which we'll load when we enter DS9 Map

# by USS Sovereign

# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


# Define stations in DS9 Map
def DS9SetStations():
        # Grab the system's name directly from the set file
        DS9 = __import__("Systems.DeepSpace9.DeepSpace91")
        DS9Set = DS9.GetSet()

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.FederationSide == 1:

                if DS9FXSavedConfig.DS9Selection == 1:
                        # Create the station
                        DS9Name = "Deep_Space_9"
                        pDS9 = loadspacehelper.CreateShip(DS9FXShips.DS9, DS9Set, DS9Name, "DS9 Location")
                
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(DS9Name)
                        pMission.GetFriendlyGroup().AddName(DS9Name)
                    
                        import Custom.DS9FX.DS9FXAILib.DS9FXDS9AI

                        DeepSpace9 = MissionLib.GetShip("Deep_Space_9", DS9Set)

                        pDeepSpace9 = App.ShipClass_Cast(DeepSpace9)

                        pDeepSpace9.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXDS9AI.CreateAI(pDeepSpace9))

        else:
                if DS9FXSavedConfig.DS9Selection == 1:
                        # Create the station
                        DS9Name = "Deep_Space_9"
                        pDS9 = loadspacehelper.CreateShip(DS9FXShips.DS9, DS9Set, DS9Name, "DS9 Location")
                    
                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(DS9Name)
                        pMission.GetEnemyGroup().AddName(DS9Name)
                       
                        import Custom.DS9FX.DS9FXAILib.DS9FXEnemyDS9AI

                        DeepSpace9 = MissionLib.GetShip("Deep_Space_9", DS9Set)

                        pDeepSpace9 = App.ShipClass_Cast(DeepSpace9)

                        pDeepSpace9.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXEnemyDS9AI.CreateAI(pDeepSpace9))
