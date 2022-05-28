# by Sov

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def CardassiaSetShips():
    sSet = __import__("Systems.DS9FXCardassia.DS9FXCardassia1")
    pSet = sSet.GetSet()           

    reload(DS9FXSavedConfig)
    
    if DS9FXSavedConfig.CardassianSide == 1:
                if DS9FXSavedConfig.CardassiaShip1 == 1:
                        sShip = "Hutet 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Hutet, pSet, sShip, "Pos1")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip2 == 1:
                        sShip = "Keldon 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Pos2")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip3 == 1:
                        sShip = "Keldon 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Pos3")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip4 == 1:
                        sShip = "Galor 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Pos4")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip5 == 1:
                        sShip = "Galor 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Pos5")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))
    else:
                if DS9FXSavedConfig.CardassiaShip1 == 1:
                        sShip = "Hutet 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Hutet, pSet, sShip, "Pos1")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip2 == 1:
                        sShip = "Keldon 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Pos2")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip3 == 1:
                        sShip = "Keldon 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Keldon, pSet, sShip, "Pos3")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip4 == 1:
                        sShip = "Galor 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Pos4")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.CardassiaShip5 == 1:
                        sShip = "Galor 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Galor, pSet, sShip, "Pos5")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
