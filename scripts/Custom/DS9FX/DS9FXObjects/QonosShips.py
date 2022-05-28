import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def QonosSetShips():
    sName = __import__("Systems.DS9FXQonos.DS9FXQonos1")
    pSet = sName.GetSet()           

    reload(DS9FXSavedConfig)    
    
    if DS9FXSavedConfig.KlingonSide == 1:
                if DS9FXSavedConfig.QonosShip1 == 1:
                        sShip = "IKS K'mpec"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Neghvar, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))

                if DS9FXSavedConfig.QonosShip2 == 1:
                        sShip = "IKS Amar"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Ktinga, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))        
                        
                if DS9FXSavedConfig.QonosShip3 == 1:
                        sShip = "IKS Ki'Tang"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, sShip, "Ship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetFriendlyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericFriendlyAI.CreateAI(pShip))    
                        
    else:
                if DS9FXSavedConfig.QonosShip1 == 1:
                        sShip = "IKS K'mpec"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Neghvar, pSet, sShip, "Ship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))

                if DS9FXSavedConfig.QonosShip2 == 1:
                        sShip = "IKS Amar"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.Ktinga, pSet, sShip, "Ship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))
                        
                if DS9FXSavedConfig.QonosShip3 == 1:
                        sShip = "IKS Ki'Tang"
                        pShip = loadspacehelper.CreateShip(DS9FXShips.BirdOfPrey, pSet, sShip, "Ship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(sShip)
                        pMission.GetEnemyGroup().AddName(sShip)

                        import Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI

                        pShip = MissionLib.GetShip(sShip, pSet) 

                        pShip = App.ShipClass_Cast(pShip)

                        pShip.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXGenericEnemyAI.CreateAI(pShip))                        
                        
                        
