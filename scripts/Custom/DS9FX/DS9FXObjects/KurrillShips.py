# by Sov

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def KurrillSetShips():
    sSet = __import__("Systems.DS9FXKurill.DS9FXKurill1")
    pSet = sSet.GetSet()           

    reload(DS9FXSavedConfig)
    
    if DS9FXSavedConfig.DominionSide == 1:
                if DS9FXSavedConfig.KurrillShip1 == 1:
                        sShip = "Bugship 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip2 == 1:
                        sShip = "Bugship 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip3 == 1:
                        sShip = "Bugship 3"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip4 == 1:
                        sShip = "BugShip 4"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship4 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip5 == 1:
                        sShip = "Dreadnought"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Ship5 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))
    else:
                if DS9FXSavedConfig.KurrillShip1 == 1:
                        sShip = "Bugship 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip2 == 1:
                        sShip = "Bugship 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip3 == 1:
                        sShip = "Bugship 3"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip4 == 1:
                        sShip = "BugShip 4"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship4 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.KurrillShip5 == 1:
                        sShip = "Dreadnought"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Ship5 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
