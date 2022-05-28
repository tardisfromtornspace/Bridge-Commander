###############################################################################
#       Filename:       Calufrax1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates Calufrax 1 static objects.  Called by Calufrax1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       08/14/03 - Ben Howard
#       Adapted for Multiplayer  12/15/03 - Chris Jones
###############################################################################
import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(8000.0, 5000, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Calufrax Prime")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        pSun2 = App.Sun_Create(1100.0, 4000, 600, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun2, "Calufrax Dwarf")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()
                
        pSun3 = App.Sun_Create(2500.0, 4000, 600, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun3, "Calufrax Companion")
        
        # Place the object at the specified location.
        pSun3.PlaceObjectByName( "Sun3" )
        pSun3.UpdateNodeOnly()
        
        Tactical.LensFlares.WhiteLensFlare(pSet, pSun3)

        # Model and placement for Calufrax1
        pPlanet = App.Planet_Create(350.0, "data/models/environment/RockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Calufrax 1")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Planet1 Location")
        pPlanet.UpdateNodeOnly()

        # Model and placement for Calufrax 2
        pPlanet1 = App.Planet_Create(800.0, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pPlanet1, "Calufrax 2")

        #Place the object at the specified location.
        pPlanet1.PlaceObjectByName("Planet2 Location")
        pPlanet1.UpdateNodeOnly()

        # Model and placement for Calufrax2Moon1
        pPlanet2 = App.Planet_Create(160.0, "data/models/environment/moon.nif")
        pSet.AddObjectToSet(pPlanet2, "Calufrax 2 Alpha")

        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Moon1 Location")
        pPlanet2.UpdateNodeOnly()

        # Model and placement for Calufrax2Moon2
        pPlanet3 = App.Planet_Create(70.0, "data/models/environment/BrownPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Calufrax 2 Beta")

        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Moon2 Location")
        pPlanet3.UpdateNodeOnly()

        # Model and placement for Calufrax3Moon1
        pPlanet5 = App.Planet_Create(120.0, "data/models/environment/DryPlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Calufrax 2 Gamma")

        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Moon3 Location")
        pPlanet5.UpdateNodeOnly()
        
        # Model and placement for Calufrax3
        pPlanet4 = App.Planet_Create(1000.0, "data/models/environment/PurpleWhitePlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Calufrax 3")

        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Calufrax3")
        pPlanet4.UpdateNodeOnly()

        # Model and placement for Calufrax3Moon1
        pPlanet5 = App.Planet_Create(140.0, "data/models/environment/IcePlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Calufrax 3 Alpha")

        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Moon4 Location")
        pPlanet5.UpdateNodeOnly()
        
        pNebula = App.MetaNebula_Create(160.0 / 255.0, 60.0 / 255.0, 195.0  / 255.0, 6800.0, 0.1, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(100.0, 100.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(12000.0, 49000.0, 300.0, 1000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula")
        
        pNebula2 = App.MetaNebula_Create(200.0 / 255.0, 140.0 / 255.0, 225.0  / 255.0, 6800.0, 0.1, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(300.0, 300.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(13200.0, 48000.0, 500.0, 700.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
        
        pNebula3 = App.MetaNebula_Create(140.0 / 255.0, 40.0 / 255.0, 95.0  / 255.0, 6800.0, 0.1, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula3.SetupDamage(50.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula3.AddNebulaSphere(10000.0, 50000.0, 200.0, 1700.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula3, "Nebula3")
        
        pNebula4 = App.MetaNebula_Create(90.0 / 255.0, 40.0 / 255.0, 45.0  / 255.0, 6800.0, 0.1, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula4.SetupDamage(50.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula4.AddNebulaSphere(7000.0, 51000.0, -300.0, 3500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula4, "Nebula4")

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
                # Create ship
                pAlien  = loadspacehelper.CreateShip("KessokLight", pSet, "Unknown", "Alien Location")
                pAlien.SetAI(SelfDefenseAI.CreateAI(pAlien))
                
                # Create a Communications Relay
                pArray  = loadspacehelper.CreateShip("CommArray", pSet, "Comm Array", "Array Location")

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:                   
                # Setup Affiliations 
                global pFriendlies 
                global pEnemies
                        
                pGame = App.Game_GetCurrentGame() 
                pEpisode = pGame.GetCurrentEpisode() 
                pMission = pEpisode.GetCurrentMission()
                pEnemies = MissionLib.GetEnemyGroup()
                pEnemies.AddName("Unknown")


                # Set up AI's
                import AttackAI
                pAlien.SetAI(AttackAI.CreateAI(pAlien))


###############################################################################
#       SetupEventHandlers()
#
#       Set up event handlers used by the Unknown Alien set.
#
#       Args:   pSet    - The Unknown Alien set.
#
#       Return: none
###############################################################################
def SetupEventHandlers(pMission):
        import Multiplayer.MissionShared
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")

        return 0


def ObjectCreatedHandler (TGObject, pEvent):
        import Multiplayer.SpeciesToShip

        # We only care about ships.
        pShip = App.ShipClass_Cast (pEvent.GetDestination ())
        if (pShip):
                # We only care about ships.
                if (pShip.IsPlayerShip ()):
                        ResetEnemyFriendlyGroups ()
                elif (pShip.GetNetType () == Multiplayer.SpeciesToShip.FEDSTARBASE):
                        pass
        return 0

def ResetEnemyFriendlyGroups ():
        # Go through player list, trying to find all the ships

        pNetwork = App.g_kUtopiaModule.GetNetwork ()
        pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

        if (pNetwork and pGame):
                pMission = MissionLib.GetMission ()
                pEnemyGroup = MissionLib.GetEnemyGroup ()

                pSet = App.g_kSetManager.GetSet("Calufrax1")
                pAIShip = App.ShipClass_GetObject(pSet, "Unknown")
                if pAIShip != None:    
                   pEnemyGroup.AddName("Unknown")
                   import AttackAI
                   pAIShip.SetAI(AttackAI.CreateAI(pAIShip))       

