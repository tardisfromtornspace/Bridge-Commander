4###############################################################################
#    
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import SelfDefenseAI
import AttackAI


def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(2500.0, 4000, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Promellian")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.WhiteLensFlare(pSet, pSun)
 
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):        
        
                # Create our static stations and such
                pHub11  = loadspacehelper.CreateShip("SFRD_Promellian", pSet, "ShipUnknown", "Transwarp6")
                if (pHub11 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub11)
                        pHub11.SetAlertLevel(App.ShipClass.GREEN_ALERT)
                                        
                # Create our static stations and such
                pHub4   = loadspacehelper.CreateShip("QuanTar", pSet, "Asteroid-1", "Inner3")
                if (pHub4 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub4)
                pHub4.SetAlertLevel(App.ShipClass.RED_ALERT)

                # Create our ships              
                pQuanTar = loadspacehelper.CreateShip("Asteroid", pSet, "Asteroid", "Shuttle Location")
                pQuanTar = loadspacehelper.CreateShip("QuanTar", pSet, "Asterod", "SL2")



                # Setup Affiliations
                global pFriendlies
                global pEnemies

                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pFriendlies = MissionLib.GetFriendlyGroup()
                pEnemies = MissionLib.GetEnemyGroup()
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("Asteroid")
                pEnemies.AddName("Asterod")



                pQuanTar.SetAI(AttackAI.CreateAI(pQuanTar))       