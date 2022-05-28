###############################################################################
#       Filename:       JLWMP1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates JLWMP 1 static objects.  Called by JLWMP1.py when region is created
#       
#       Created:        10/02/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
#       Adapted for Earth 12/14/03 Chris Jones from a JWatts test system
###############################################################################
import App
##import Bridge.BridgeUtils
import MissionLib
##import Bridge.Characters.Graff
##import Bridge.HelmMenuHandlers
import Tactical.LensFlares
import loadspacehelper
##import StarbaseFriendlyAI
##import DockWithStarbase
import SelfDefenseAI
import RouteAI
import DefendAI

def Initialize(pSet):
        # 149.6 million km from the sun

        # Add a sun, far far away
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
        
        ######
        # Create the Planet - 12,756 km diameter
        pEarth = App.Planet_Create(728.91, "data/models/environment/earth.nif")
        pSet.AddObjectToSet(pEarth, "Earth")

        # Place the object at the specified location.
        pEarth.PlaceObjectByName( "Earth" )
        pEarth.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pEarth, "data/models/environment/Earth.nif", "Class-M")    

        ######
        # Create the Planet - 3,475 km diameter
        pMoon = App.Planet_Create(198.57, "data/models/environment/moon.nif")
        pSet.AddObjectToSet(pMoon, "Moon")

        # Place the object at the specified location.
        pMoon.PlaceObjectByName( "Moon" )
        pMoon.UpdateNodeOnly()
        pMoon.SetAtmosphereRadius(0.01)

        # Rotate Earth and Moon:
        import Custom.QBautostart.Libs.LibPlanet
        # Earth does need 8.62*10^4 seconds for a full Rotation
        # and 3.16*10^7 seconds for a full turn around the sun
        global pEarthRotation
        pEarthRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pEarth, 8.62e4, 3.16e7, pSun)
        # and the moon:
        global pMoonRotation
        pMoonRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pMoon, 2360622, 2360622, pEarth)

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
                # Create Starbase 12
                pStarbase       = loadspacehelper.CreateShip("FedStarbase", pSet, "Starbase 12", "Starbase Location")
                        
                # Create ship
                pTransport2     = loadspacehelper.CreateShip("Transport", pSet, "Lunar Voyage", "Lunar Voyage Location")
                
                # Create ship
                pTransport3     = loadspacehelper.CreateShip("Freighter", pSet, "Lunar Traveler", "Lunar Traveler Location")
                
                # Create ship
                pAkira  = loadspacehelper.CreateShip("Akira", pSet, "USS Geronimo", "Akira Location")
                
                # Create ship
                pAkiraD = loadspacehelper.CreateShip("Akira", pSet, "USS Full Moon", "Lunar Defender")
                        
                # Create ship
                pSutherland     = loadspacehelper.CreateShip("Nebula", pSet, "USS Sutherland", "Sutherland Location")
                
        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:                   
                # Setup Affiliations                         
                pGame = App.Game_GetCurrentGame() 
                pEpisode = pGame.GetCurrentEpisode() 
                pMission = pEpisode.GetCurrentMission()
                pNeutrals = pMission.GetNeutralGroup()
                pNeutrals.AddName("Lunar Traveler")
                pNeutrals.AddName("Lunar Voyage")
                pFriendlies = MissionLib.GetFriendlyGroup()
                pFriendlies.AddName("Starbase 12")
                pEnemies = MissionLib.GetEnemyGroup()
                if not pEnemies.GetNameTuple():
                        pEnemies.AddName("This ship probably wont exist")

                # Set up AI's
                import StarbaseMPAI
                pStarbase.SetAI(StarbaseMPAI.CreateAI(pStarbase))
                pTransport2.SetAI(SelfDefenseAI.CreateAI(pTransport2))
                pTransport3.SetAI(RouteAI.CreateAI(pTransport3, pMoon, pEarth))
                pAkira.SetAI(DefendAI.CreateAI(pAkira, pTransport2))
                pAkiraD.SetAI(DefendAI.CreateAI(pAkiraD, pTransport2))
                pSutherland.SetAI(DefendAI.CreateAI(pSutherland, pStarbase))


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
                pFriendyGroup = MissionLib.GetFriendlyGroup()
                pNeutralGroup = pMission.GetNeutralGroup ()

                
                pSet = App.g_kSetManager.GetSet("Earth1")
                pEarth = App.Planet_GetObject(pSet, "Earth")
                pMoon = App.Planet_GetObject(pSet, "Moon")
                pStarbase = App.ShipClass_GetObject(pSet, "Starbase 12")
                pTransport2 = App.ShipClass_GetObject(pSet, "Lunar Voyage")
                pTransport3 = App.ShipClass_GetObject(pSet, "Lunar Traveler")
                pAkira = App.ShipClass_GetObject(pSet, "USS Geronimo")
                pAkiraD = App.ShipClass_GetObject(pSet, "USS Full Moon")
                pSutherland = App.ShipClass_GetObject(pSet, "USS Sutherland")
                if pStarbase != None:
                   pFriendyGroup.AddName("Starbase 12")
                   import StarbaseMPAI
                   pEnemyGroup.AddName("Starbase 12")
                   pStarbase.SetAI(StarbaseMPAI.CreateAI(pStarbase))
                   pEnemyGroup.RemoveName("Starbase 12")
                if pTransport2 != None:
                   pNeutralGroup.AddName("Lunar Voyage")
                   pTransport2.SetAI(SelfDefenseAI.CreateAI(pTransport2))
                if pTransport3 != None:
                   pNeutralGroup.AddName("Lunar Traveler")
                   pTransport3.SetAI(RouteAI.CreateAI(pTransport3, pMoon, pEarth))
                if (pAkira != None) and (pTransport2 != None):
                   pAkira.SetAI(DefendAI.CreateAI(pAkira, pTransport2))
                if (pAkiraD != None) and (pTransport2 != None):
                   pAkiraD.SetAI(DefendAI.CreateAI(pAkiraD, pTransport2))
                if (pSutherland != None) and (pStarbase != None):
                   pSutherland.SetAI(DefendAI.CreateAI(pSutherland, pStarbase))
