# by Sov

import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def FoundersSetShips():
    sSet = __import__("Systems.DS9FXFoundersHomeworld.DS9FXFoundersHomeworld1")
    pSet = sSet.GetSet()           

    reload(DS9FXSavedConfig)
    
    if DS9FXSavedConfig.DominionSide == 1:
                if DS9FXSavedConfig.FoundersShip1 == 1:
                        sShip = "Dreadnought"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.FoundersShip2 == 1:
                        sShip = "Bugship 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.FoundersShip3 == 1:
                        sShip = "Bugship 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.FoundersShip4 == 1:
                        sShip = "BugShip 3"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship4 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

    else:
                if DS9FXSavedConfig.FoundersShip1 == 1:
                        sShip = "Dreadnought"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.FoundersShip2 == 1:
                        sShip = "Bugship 1"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.FoundersShip3 == 1:
                        sShip = "Bugship 2"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.FoundersShip4 == 1:
                        sShip = "BugShip 3"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Ship4 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
