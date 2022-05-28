# by Sov

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def NewBajorSetShips():
    sName = __import__("Systems.DS9FXNewBajor.DS9FXNewBajor1")
    pSet = sName.GetSet()           

    reload(DS9FXSavedConfig)
    
    if DS9FXSavedConfig.FederationSide == 1:
                if DS9FXSavedConfig.NewBajorMajestic == 1:
                        sShip = "USS Majestic"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Miranda, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.NewBajorBonchune == 1:
                        sShip = "USS Bonchune"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Nebula, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))
    else:
                if DS9FXSavedConfig.NewBajorMajestic == 1:
                        sShip = "USS Majestic"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Miranda, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.NewBajorBonchune == 1:
                        sShip = "USS Bonchune"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Nebula, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
