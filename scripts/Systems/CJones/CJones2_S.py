###############################################################################
#       Filename:       CJones2_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates CJones2 static objects.  Called by CJones2.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans 
#                       May/June 2003 - Chris Jones, Jeff Watts, Jr.
#                       Sept. 2003 - Chris Jones
#       MultiPlayer Version 12/16/03 Chris Jones
###############################################################################
import App
import loadspacehelper
import Tactical.LensFlares
import MissionLib
import SelfDefenseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(3000.0, 1000, 1000)
        pSet.AddObjectToSet(pSun, "Sun59")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun59" )
        pSun.UpdateNodeOnly()
        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.YellowLensFlare(pSet, pSun) 
        
        pSun2 = App.Sun_Create(1500.0, 4000, 600, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun2, "Unknown Dwarf")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()  
        
        # Model and placement for CJones
        pPlanet = App.Planet_Create(280.0, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "CJones2")
        
        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("CJones2")
        pPlanet.UpdateNodeOnly()        
        
        # Model and placement for Unknown Planet
        pPlanet2 = App.Planet_Create(4000.0, "data/models/environment/IcePlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Unknown Planet")
                
        # Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Omicron Location")
        pPlanet2.UpdateNodeOnly()
                
        # Model and placement for Plattsburgh
        # pPlanet3 = App.Planet_Create(160.0, "data/models/environment/RedPlanet.nif")
        # pSet.AddObjectToSet(pPlanet3, "Plattsburgh Colony")
                        
        #Place the object at the specified location.
        # pPlanet3.PlaceObjectByName("Plattsburgh Location")
        # pPlanet3.UpdateNodeOnly()
                
        # Model and placement for Neptune II
        pPlanet4 = App.Planet_Create(160.0, "data/models/environment/BrightGreenPlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Neogiah")
                                
        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Neogiah Location")
        pPlanet4.UpdateNodeOnly()
        
        # Model and placement for Red Giant Planet
        pPlanet5 = App.Planet_Create(2000.0, "data/models/environment/RedSwirlPlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Omicron")
                                
        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Omicron Location")
        pPlanet5.UpdateNodeOnly()
        
        pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaexternalblue.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(0.4, 4.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(8000.0, 945.0, -3600.0,  1000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")
                        
        pNebula2 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(0.4, 4.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(9000.0, 1945.0, -1600.0,  1000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
                        
        pNebula3 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlayyellow.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula3.SetupDamage(6.4, 24.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula3.AddNebulaSphere(8000.0, 2945.0, -4600.0,  1000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula3, "Nebula3")
                
        pNebula4 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/stars.tga", "data/stars.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula4.SetupDamage(12.0, 35.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula4.AddNebulaSphere(-1000.0, 12000.0, 0.0, 500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula4, "Nebula4")        
        
        # Asteroid Field Position "Asteroid Field 1"
        kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 1", pSet.GetName(), None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(900.0, 900.0, 900.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.000000, 0.997209, -0.074666)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.000345, 0.074666, 0.997209)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetFieldRadius(500.0000)
        kThis.SetNumTilesPerAxis(3)
        kThis.SetNumAsteroidsPerTile(2)
        kThis.SetAsteroidSizeFactor(5.000000)
        kThis.UpdateNodeOnly()
        kThis.ConfigField()
        kThis.Update(0)
        kThis = None
        # End position "Asteroid Field 1"
        
        # Asteroid Field Position "Asteroid Field 2"
        kThis = App.AsteroidFieldPlacement_Create("Asteroid Field 2", pSet.GetName(), None)
        kThis.SetStatic(0)
        kThis.SetNavPoint(0)
        kThis.SetTranslateXYZ(-1000.0, 12000.0, 0.0)
        kForward = App.TGPoint3()
        kForward.SetXYZ(-0.000000, 0.997209, -0.074666)
        kUp = App.TGPoint3()
        kUp.SetXYZ(-0.000345, 0.074666, 0.997209)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetFieldRadius(500.0000)
        kThis.SetNumTilesPerAxis(3)
        kThis.SetNumAsteroidsPerTile(1)
        kThis.SetAsteroidSizeFactor(5.000000)
        kThis.UpdateNodeOnly()
        kThis.ConfigField()
        kThis.Update(0)
        kThis = None
        # End position "Asteroid Field 2"

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                # Create ship
                pMarauder2      = loadspacehelper.CreateShip("Marauder", pSet, "Quark", "Quark Location")

                # Create ship
                pMarauder       = loadspacehelper.CreateShip("Marauder", pSet, "Aquisition", "AQ Location")
  
                # Create ship
                pShuttle2 = loadspacehelper.CreateShip("Shuttle", pSet, "Nanobyte", "Shuttle2 Location")
        
                # Create ship
                pShuttledam     = loadspacehelper.CreateShip("Shuttle", pSet, "Attacked Shuttle", "Shuttledam Location")
                if (pShuttledam != None):
                        # Damage the ship and give it rotation
                        MissionLib.SetRandomRotation(pShuttledam, 11.0)
                        # Damage it's hull
                        pRepair = pShuttledam.GetRepairSubsystem()
                        pProp   = pRepair.GetProperty()
                        pProp.SetMaxRepairPoints(0.0)
                        pShuttledam.DamageSystem(pShuttledam.GetHull(), pShuttledam.GetHull().GetMaxCondition() * 0.10)
                pShuttledam.SetAlertLevel(App.ShipClass.RED_ALERT)
        
                # Create ship
                pNeutralTransport       = loadspacehelper.CreateShip("Transport", pSet, "Transport 2", "T7 locale")
        
       

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
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("Quark")
                pNeutrals.AddName("Aquisition")
                pNeutrals.AddName("Transport 2")

                pMarauder2.SetAI(SelfDefenseAI.CreateAI(pMarauder2))
                pMarauder.SetAI(SelfDefenseAI.CreateAI(pMarauder))      
                pShuttle2.SetAI(SelfDefenseAI.CreateAI(pShuttle2))
                pNeutralTransport.SetAI(SelfDefenseAI.CreateAI(pNeutralTransport))      

###############################################################################
#       SetupEventHandlers()
#
#       Set up event handlers used by the Starbase 12 set.
#
#       Args:   pSet    - The Starbase 12 set.
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
                pNeutralGroup = pMission.GetNeutralGroup ()
                
                pSet = App.g_kSetManager.GetSet("CJones2")
                pMarauder2 = App.ShipClass_GetObject(pSet, "Quark")
                pMarauder = App.ShipClass_GetObject(pSet, "Aquisition")
                pNeutralTransport = App.ShipClass_GetObject(pSet, "Transport 2")
                pShuttle2 = App.ShipClass_GetObject(pSet, "Nanobyte")
                if pMarauder2 != None:
                        pNeutralGroup.AddName("Quark")
                        pMarauder2.SetAI(SelfDefenseAI.CreateAI(pMarauder2))
                if pMarauder != None:   
                        pNeutralGroup.AddName("Aquisition")
                        pMarauder.SetAI(SelfDefenseAI.CreateAI(pMarauder))      
                if pNeutralTransport != None:   
                        pNeutralGroup.AddName("Transport 2")
                        pNeutralTransport.SetAI(SelfDefenseAI.CreateAI(pNeutralTransport))      
                if pShuttle2 != None:   
                        pShuttle2.SetAI(SelfDefenseAI.CreateAI(pShuttle2))
