from bcdebug import debug
###############################################################################
#       Filename:       Borealis1_S.py       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard       
#       Creates ArenaA 1 static objects.  Called by Borealis1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       03/15/02 - Ben Howard
#       AIs/Ships added: August 2003 - Chris Jones
#       Modified for MultiPlayer 12/17/03 - Chris Jones
#       Starbase AI by Jeff Watts, Jr. 12/13/03
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):
        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(400.0, 400, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun, "Beta Hydrae")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Add a sun, far far away
        pSun1 = App.Sun_Create(1400.0, 1800, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun1, "Calufrax")
        
        # Place the object at the specified location.
        pSun1.PlaceObjectByName( "Sun 1" )
        pSun1.UpdateNodeOnly()

        # Add a sun, far far away
        pSun2 = App.Sun_Create(900.0, 200, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun2, "Tythonus")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun 2" )
        pSun2.UpdateNodeOnly()

        # Add a sun, far far away
        pSun3 = App.Sun_Create(1200.0, 1800, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun3, "Skaro")
        
        # Place the object at the specified location.
        pSun3.PlaceObjectByName( "Sun 3" )
        pSun3.UpdateNodeOnly()

        # Add a sun, far far away
        pSun4 = App.Sun_Create(1000.0, 800, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun4, "Gamma Epsilon")
        
        # Place the object at the specified location.
        pSun4.PlaceObjectByName( "Sun 4" )
        pSun4.UpdateNodeOnly()

        # Add a sun, far far away
        pSun5 = App.Sun_Create(500.0, 1800, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun5, "Draconis")
        
        # Place the object at the specified location.
        pSun5.PlaceObjectByName( "Sun 5" )
        pSun5.UpdateNodeOnly()

        # Add a sun, far far away
        pSun6 = App.Sun_Create(500.0, 1800, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun6, "Atrios")
        
        # Place the object at the specified location.
        pSun6.PlaceObjectByName( "Sun 6" )
        pSun6.UpdateNodeOnly()

        # Add a sun, far far away
        pSun7 = App.Sun_Create(500.0, 1800, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun7, "Xeos")
        
        # Place the object at the specified location.
        pSun7.PlaceObjectByName( "Sun 7" )
        pSun7.UpdateNodeOnly()

        # Add a sun, far far away
        pSun8 = App.Sun_Create(1500.0, 800, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun8, "Kallisti")
        
        # Place the object at the specified location.
        pSun8.PlaceObjectByName( "Sun 8" )
        pSun8.UpdateNodeOnly()

        # Add a sun, far far away
        pSun9 = App.Sun_Create(200.0, 50, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun9, "Cueball")
        
        # Place the object at the specified location.
        pSun9.PlaceObjectByName( "Sun 9" )
        pSun9.UpdateNodeOnly()

        # Model and placement for Kaled
        pPlanet = App.Planet_Create(400, "data/models/environment/RockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Kaled")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Kaled1")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(150)

        # Model and placement for Tiamat
        pPlanet = App.Planet_Create(1200, "data/models/environment/TanPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Tiamat")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Tiamat1")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(250)

        # Model and placement for Chimera
        pPlanet = App.Planet_Create(40, "data/models/environment/IcePlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Chimera")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Chimera1")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(10)

        # Model and placement for Borealis
        pPlanet = App.Planet_Create(340, "data/models/environment/Saturn.nif")
        pSet.AddObjectToSet(pPlanet, "Borealis")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Borealis1")
        pPlanet.UpdateNodeOnly()
        pPlanet.SetAtmosphereRadius(150)
                
        pNebula1 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula1.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula1.AddNebulaSphere(-10000.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula1, "Nebula1")
        
        pNebula2 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(0.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
        
        pNebula3 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula3.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula3.AddNebulaSphere(10000.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula3, "Nebula3")

        pNebula4 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula4.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula4.AddNebulaSphere(-20000.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula4, "Nebula4")
        
        pNebula5 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula5.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula5.AddNebulaSphere(20000.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula5, "Nebula5")
        
        pNebula6 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula6.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula6.AddNebulaSphere(-30000.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula6, "Nebula6")
        
        pNebula7 = App.MetaNebula_Create(130.0 / 255.0, 130.0 / 255.0, 130.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaygreen.tga", "data/Backgrounds/nebulaexternalgreen.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula7.SetupDamage(500.0, 500.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula7.AddNebulaSphere(30000.0, -60000.0, 0.000000, 12500.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula7, "Nebula7")

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):

                pStarbase       = loadspacehelper.CreateShip("CardOutpost", pSet, "Outpost 1", "1")

                pCardStation    = loadspacehelper.CreateShip("CardOutpost", pSet, "Outpost 2", "2")
                
        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:                   
                # Setup Affiliations 
                pFriendlies = MissionLib.GetFriendlyGroup()
                pEnemies = MissionLib.GetEnemyGroup()
        
                pGame = App.Game_GetCurrentGame() 
                pEpisode = pGame.GetCurrentEpisode() 
                pMission = pEpisode.GetCurrentMission() 
                pEnemies.AddName("Outpost 1")
                pEnemies.AddName("Outpost 2")

                # Set up AI's
                import StarbaseMPAI
                pStarbase.SetAI(StarbaseMPAI.CreateAI(pStarbase))
                pCardStation.SetAI(StarbaseMPAI.CreateAI(pCardStation))


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
        debug(__name__ + ", SetupEventHandlers")
        import Multiplayer.MissionShared
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")

        return 0


def ObjectCreatedHandler (TGObject, pEvent):
        debug(__name__ + ", ObjectCreatedHandler")
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

        debug(__name__ + ", ResetEnemyFriendlyGroups")
        pNetwork = App.g_kUtopiaModule.GetNetwork ()
        pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

        if (pNetwork and pGame):
                pMission = MissionLib.GetMission ()
                pEnemyGroup = MissionLib.GetEnemyGroup ()
                pFriendlyGroup = MissionLib.GetFriendlyGroup()
                
                pSet = App.g_kSetManager.GetSet("Borealis1")
                pAIShip = App.ShipClass_GetObject(pSet, "Outpost 1")
                pAIShip2 = App.ShipClass_GetObject(pSet, "Outpost 2")
                if pAIShip != None:
                   pFriendlyGroup.AddName("Outpost 1")
                   import StarbaseMPAI
                   pAIShip.SetAI(StarbaseMPAI.CreateAI(pAIShip))
                if pAIShip2 != None:
                   pFriendlyGroup.AddName("Outpost 2")
                   pAIShip2.SetAI(StarbaseMPAI.CreateAI(pAIShip2))
