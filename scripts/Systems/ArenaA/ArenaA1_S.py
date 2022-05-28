###############################################################################
#       Filename:       ArenaA1_S.py       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard       
#       Creates ArenaA 1 static objects.  Called by ArenaA1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       03/15/02 - Ben Howard
#       AIs/Ships/Arrays added: August 2003 - Chris Jones
#       Modified for MultiPlayer 12/17/03 - Chris Jones
#       Starbase AI for MultiPlayer by Jeff Watts, Jr. 12/13/03
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import RouteAI
import DefendAI
import SelfDefenseAI

def Initialize(pSet):
        # Add a sun, far far away
        pSun = App.Sun_Create(90.0, 200, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresOrange.tga")
        pSet.AddObjectToSet(pSun, "Sun")
        pSun.SetEnvironmentalShieldDamage(10)
        pSun.SetEnvironmentalHullDamage(25)
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()
        
        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.YellowLensFlare(pSet, pSun)

        # Model and placement for Asteroid Planet
        pPlanet = App.Planet_Create(40.0, "data/models/environment/GrayPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Cloud of Stones")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Ast Planet")
        pPlanet.UpdateNodeOnly()

        # Model and placement for Moon Planet
        pPlanetMP = App.Planet_Create(120.0, "data/models/environment/TanPlanet.nif")
        pSet.AddObjectToSet(pPlanetMP, "Many Orbits")
        pPlanetMP.SetAtmosphereRadius(80)

        #Place the object at the specified location.
        pPlanetMP.PlaceObjectByName("Moon Planet")
        pPlanetMP.UpdateNodeOnly()

        # Model and placement for Moon 1
        pPlanet1 = App.Planet_Create(30.0, "data/models/environment/moon.nif")
        pSet.AddObjectToSet(pPlanet1, "Moon 1")

        #Place the object at the specified location.
        pPlanet1.PlaceObjectByName("Moon1")
        pPlanet1.UpdateNodeOnly()

        # Model and placement for Moon 2
        pPlanet2 = App.Planet_Create(40.0, "data/models/environment/BrownPlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Moon 2")

        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Moon2")
        pPlanet2.UpdateNodeOnly()

        # Model and placement for Moon 3
        pPlanet3 = App.Planet_Create(10.0, "data/models/environment/RedPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Moon 3")

        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Moon3")
        pPlanet3.UpdateNodeOnly()

        # Model and placement for Moon 4
        pPlanet4 = App.Planet_Create(30.0, "data/models/environment/BlueGrayPlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Moon 4")

        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Moon4")
        pPlanet4.UpdateNodeOnly()

        # Model and placement for Moon 5
        pPlanet5 = App.Planet_Create(20.0, "data/models/environment/IcePlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Moon 5")

        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Moon5")
        pPlanet5.UpdateNodeOnly()

        # Model and placement for Moon 6
        pPlanet6 = App.Planet_Create(30.0, "data/models/environment/TanGasPlanet.nif")
        pSet.AddObjectToSet(pPlanet6, "Moon 6")

        #Place the object at the specified location.
        pPlanet6.PlaceObjectByName("Moon6")
        pPlanet6.UpdateNodeOnly()

        # Add Dwarf Star
        pSun = App.Sun_Create(40.0, 300, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Red Dwarf")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Dwarf Location" )
        pSun.UpdateNodeOnly()

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):

                # Create a Communications Relay
                pArray2 = loadspacehelper.CreateShip("CommArray", pSet, "Comm Array 2", "Array2 Location")
                pArray2.SetTargetable(0)        
        
                # Create a Communications Relay
                pArray  = loadspacehelper.CreateShip("CommLight", pSet, "Comm Array", "Array Location")
                pArray.SetTargetable(1)

                # Create ship
                pTransport2     = loadspacehelper.CreateShip("Transport", pSet, "Arena 1", "Arena1L")
                
                # Create our static stations and such
                pStarbase   = loadspacehelper.CreateShip("FedStarbase", pSet, "Starbase 457", "FSB Location")

                # Load the starbase with torpedoes
                MissionLib.SetTotalTorpsAtStarbase("Photon", -1)
                MissionLib.SetTotalTorpsAtStarbase("Quantum", -1)

                pAkira     = loadspacehelper.CreateShip("Akira", pSet, "JArcherII", "Akira locale")

                # Create our static stations and such
                pCardStation    = loadspacehelper.CreateShip("CardStarbase", pSet, "Sand Dollar", "CSB Location")  
                
                pKeldon     = loadspacehelper.CreateShip("Keldon", pSet, "Gul Dukat", "Keldon locale")

                pHybrid = loadspacehelper.CreateShip("CardHybrid", pSet, "Unknown Race", "URL")
                
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
                pFriendlies = MissionLib.GetFriendlyGroup()              
                pEnemies = MissionLib.GetEnemyGroup()
                pEnemies.AddName("Starbase 457")
                pEnemies.AddName("Sand Dollar")
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("Arena 1")   


                # Set up AI's
                import StarbaseMPAI
                pTransport2.SetAI(RouteAI.CreateAI(pTransport2, pPlanet, pArray2))
                pStarbase.SetAI(StarbaseMPAI.CreateAI(pStarbase))
                pAkira.SetAI(DefendAI.CreateAI(pAkira, pStarbase))
                pCardStation.SetAI(StarbaseMPAI.CreateAI(pCardStation))
                pKeldon.SetAI(DefendAI.CreateAI(pKeldon, pCardStation))
                pHybrid.SetAI(SelfDefenseAI.CreateAI(pHybrid))


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
                pFriendlyGroup = MissionLib.GetFriendlyGroup()
                pNeutralGroup = pMission.GetNeutralGroup ()

                
                pSet = App.g_kSetManager.GetSet("ArenaA1")
                pPlanet = App.Planet_GetObject(pSet, "Cloud of Stones")
                pTransport2 = App.ShipClass_GetObject(pSet, "Arena 1")
                pAkira = App.ShipClass_GetObject(pSet, "JArcherII")
                pKeldon = App.ShipClass_GetObject(pSet, "Gul Dukat")
                pHybrid = App.ShipClass_GetObject(pSet, "Unknown Race")
                pArray2 = App.ShipClass_GetObject(pSet, "Comm Array")
                pStarbase = App.ShipClass_GetObject(pSet, "Starbase 457")
                pCardStation = App.ShipClass_GetObject(pSet, "Sand Dollar")
                import StarbaseMPAI
                if pStarbase != None:
                   pFriendlyGroup.AddName("Starbase 457")
                   pStarbase.SetAI(StarbaseMPAI.CreateAI(pStarbase))
                if pCardStation != None:   
                   pFriendlyGroup.AddName("Sand Dollar")
                   pCardStation.SetAI(StarbaseMPAI.CreateAI(pCardStation))
                if (pTransport2 != None) and (pArray2 !=None):
                   pNeutralGroup.AddName("Arena 1")
                   pTransport2.SetAI(RouteAI.CreateAI(pTransport2, pPlanet, pArray2))
                if (pAkira != None) and (pStarbase != None):
                   pAkira.SetAI(DefendAI.CreateAI(pAkira, pStarbase))
                if (pKeldon != None) and (pCardStation != None):
                   pKeldon.SetAI(DefendAI.CreateAI(pKeldon, pCardStation))
                if pHybrid != None:   
                   pHybrid.SetAI(SelfDefenseAI.CreateAI(pHybrid))
