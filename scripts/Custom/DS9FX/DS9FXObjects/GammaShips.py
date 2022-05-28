# Over here we'll save locations of Gamma Quadrant ships, the file is triggered when we enter Gamma Quadrant map

# by USS Sovereign


# Imports
import App
import loadspacehelper
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXShips, DS9FXLifeSupportLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Gamma Quadrant ship def
def GammaSetShips():
        # Grab the system name from the set file
        Gamma = __import__("Systems.GammaQuadrant.GammaQuadrant1")
        GammaSet = Gamma.GetSet()

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.DominionSide == 1:

                if DS9FXSavedConfig.Bugship1Selection == 1:
                        # Create the Bugship 1
                        Bug1 = "Bugship 1"
                        pBug1 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug1, "Bugship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Bug1)
                        pMission.GetFriendlyGroup().AddName(Bug1)

                        import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBughsipAI

                        Bugship1 = MissionLib.GetShip("Bugship 1", GammaSet) 

                        pBugship1 = App.ShipClass_Cast(Bugship1)

                        pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBughsipAI.CreateAI(pBugship1))


                if DS9FXSavedConfig.Bugship2Selection == 1:
                        # Create the Bugship 2
                        Bug2 = "Bugship 2"
                        pBug2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug2, "Bugship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Bug2)
                        pMission.GetFriendlyGroup().AddName(Bug2)

                        import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI2

                        Bugship2 = MissionLib.GetShip("Bugship 2", GammaSet) 

                        pBugship2 = App.ShipClass_Cast(Bugship2)

                        pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI2.CreateAI(pBugship2))


                if DS9FXSavedConfig.Bugship3Selection == 1:
                        # Create the Bugship 3
                        Bug3 = "Bugship 3"
                        pBug3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug3, "Bugship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Bug3)
                        pMission.GetFriendlyGroup().AddName(Bug3)

                        import Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI3

                        Bugship3 = MissionLib.GetShip("Bugship 3", GammaSet) 

                        pBugship3 = App.ShipClass_Cast(Bugship3)

                        pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXFriendlyBugshipAI3.CreateAI(pBugship3))


        else:
            
                if DS9FXSavedConfig.Bugship1Selection == 1:
                        # Create the Bugship 1
                        Bug1 = "Bugship 1"
                        pBug1 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug1, "Bugship1 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Bug1)
                        pMission.GetEnemyGroup().AddName(Bug1)

                        import Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI

                        Bugship1 = MissionLib.GetShip("Bugship 1", GammaSet) 

                        pBugship1 = App.ShipClass_Cast(Bugship1)

                        pBugship1.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBughsipAI.CreateAI(pBugship1))


                if DS9FXSavedConfig.Bugship2Selection == 1:
                        # Create the Bugship 2
                        Bug2 = "Bugship 2"
                        pBug2 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug2, "Bugship2 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Bug2)
                        pMission.GetEnemyGroup().AddName(Bug2)

                        import Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI2

                        Bugship2 = MissionLib.GetShip("Bugship 2", GammaSet) 

                        pBugship2 = App.ShipClass_Cast(Bugship2)

                        pBugship2.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI2.CreateAI(pBugship2))


                if DS9FXSavedConfig.Bugship3Selection == 1:
                        # Create the Bugship 3
                        Bug3 = "Bugship 3"
                        pBug3 = loadspacehelper.CreateShip(DS9FXShips.Bugship, GammaSet, Bug3, "Bugship3 Location")

                        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                        DS9FXLifeSupportLib.ClearFromGroup(Bug3)
                        pMission.GetEnemyGroup().AddName(Bug3)

                        import Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI3

                        Bugship3 = MissionLib.GetShip("Bugship 3", GammaSet) 

                        pBugship3 = App.ShipClass_Cast(Bugship3)

                        pBugship3.SetAI(Custom.DS9FX.DS9FXAILib.DS9FXBugshipAI3.CreateAI(pBugship3))


