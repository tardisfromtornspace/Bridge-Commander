###############################################################################
#       Filename:       Vulcan1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates TheGalaxy4 static objects.  Called by Vulcan1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       08/25/02 - Ben Howard - TheGalaxy4
#       Modified:       Sept. 2003 - Chris Jones
# Adapted for MultiPlayer 12/15/03 - Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import SelfDefenseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(2500.0, 4000, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Vulcan")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

        # Model and placement for Romulus
        pPlanet = App.Planet_Create(1202, "data/models/environment/PurpleWhitePlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Vulcania")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("RomulusL")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(150)

        # Model and placement for Moon
        pPlanet2 = App.Planet_Create(500, "data/models/environment/Saturn.nif")
        pSet.AddObjectToSet(pPlanet2, "Rings of Muraan")

        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Inner6")
        pPlanet2.UpdateNodeOnly()

        # Model and placement for Moon
        pPlanet3 = App.Planet_Create(245, "data/models/environment/BrightGreenPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Muraan")

        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Inner6a")
        pPlanet3.UpdateNodeOnly()

        # Model and placement for Moon
        pPlanet4 = App.Planet_Create(400, "data/models/environment/TanGasPlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Kallisti")

        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Kali")
        pPlanet4.UpdateNodeOnly()       
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):        
                # Create our static stations and such
                pHub2   = loadspacehelper.CreateShip("City", pSet, "Temple Complex", "Inner2")
                if (pHub2 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub2)
                        pHub2.SetAlertLevel(App.ShipClass.GREEN_ALERT)
        
                # Create our static stations and such
                pHub11  = loadspacehelper.CreateShip("City", pSet, "Gardens of Surak", "Transwarp6")
                if (pHub11 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub11)
                        pHub11.SetAlertLevel(App.ShipClass.GREEN_ALERT)
                
                # Create our static stations and such
                pHub8   = loadspacehelper.CreateShip("City", pSet, "Council Chambers", "Transwarp8")
                if (pHub8 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub8)
                        pHub8.SetAlertLevel(App.ShipClass.GREEN_ALERT)
                
                # Create our static stations and such
                pHub7   = loadspacehelper.CreateShip("City", pSet, "Science Academy", "Transwarp2")
                if (pHub7 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub7)
                        pHub7.SetAlertLevel(App.ShipClass.GREEN_ALERT)
        
                # Create our static stations and such
                pHub4   = loadspacehelper.CreateShip("City", pSet, "Space Port", "Inner3")
                if (pHub4 != None):
                        # Turn off the ships repair
                        MissionLib.HideSubsystems(pHub4)
                pHub4.SetAlertLevel(App.ShipClass.GREEN_ALERT)

                # Create our ships              
                pShuttle = loadspacehelper.CreateShip("Shuttle", pSet, "Tuvok", "Shuttle Location")
                pTransport      = loadspacehelper.CreateShip("Freighter", pSet, "Vulcania II", "Transport")
                pFreighter = loadspacehelper.CreateShip("Transport", pSet, "TPring", "FR")
                pTransport2     = loadspacehelper.CreateShip("Transport", pSet, "TPau", "Transport2")
                pTransport3     = loadspacehelper.CreateShip("Transport", pSet, "Spock", "Transport3")

                # Setup Affiliations
                global pFriendlies
                global pEnemies

                pGame = App.Game_GetCurrentGame()
                pEpisode = pGame.GetCurrentEpisode()
                pMission = pEpisode.GetCurrentMission()
                pFriendlies = MissionLib.GetFriendlyGroup()
                pEnemies = MissionLib.GetEnemyGroup()
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("Tuvok")
                pNeutrals.AddName("Vulcania II")
                pNeutrals.AddName("TPring")
                pNeutrals.AddName("TPau")
                pNeutrals.AddName("Spock")

                pShuttle.SetAI(SelfDefenseAI.CreateAI(pShuttle))
                pTransport.SetAI(SelfDefenseAI.CreateAI(pTransport))
                pFreighter.SetAI(SelfDefenseAI.CreateAI(pFreighter))            
                pTransport2.SetAI(SelfDefenseAI.CreateAI(pTransport2)) 
                pTransport3.SetAI(SelfDefenseAI.CreateAI(pTransport3))
