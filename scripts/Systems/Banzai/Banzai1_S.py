###############################################################################
#       Filename:       Banzai1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates Banzai 1 static objects.  Called by Banzai1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       03/15/02 - Ben Howard
#       Adapted for Multiplayer 12/16/03 Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import DefendAI
import RouteAI
import WarpToObjectSelfDefenseAI
import KeldonAI
import GalorAI
import Galor2AI
import FedsAI
import BOPAI

def Initialize(pSet):

#       To create a colored sun:
#       pSun = App.Sun_Create(fRadius, fAtmosphereThickness, fDamagePerSec, fBaseTexture , fFlareTexture)
#
#       for fBaseTexture you can use:
#               data/Textures/SunBase.tga 
#               data/Textures/SunRed.tga
#               data/Textures/SunRedOrange.tga
#               data/Textures/SunYellow.tga
#               data/Textures/SunBlueWhite.tga
#       for fFlareTexture you can use:
#               data/Textures/Effects/SunFlaresOrange.tga
#               data/Textures/Effects/SunFlaresRed.tga
#               data/Textures/Effects/SunFlaresRedOrange.tga
#               data/Textures/Effects/SunFlaresYellow.tga
#               data/Textures/Effects/SunFlaresBlue.tga
#               data/Textures/Effects/SunFlaresWhite.tga

        # Add a sun, far far away
        pSun = App.Sun_Create(7000.0, 5000, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Banzai Prime")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        pSun2 = App.Sun_Create(1500.0, 4000, 600, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
        pSet.AddObjectToSet(pSun2, "Banzai Dwarf")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()
        
        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.WhiteLensFlare(pSet, pSun2)

        # Model and placement for Banzai1
        pPlanet = App.Planet_Create(50.0, "data/models/environment/RedPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Banzai 1")

        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Planet1 Location")
        pPlanet.UpdateNodeOnly()

        # Model and placement for Banzai 2
        pPlanet1 = App.Planet_Create(600.0, "data/models/environment/TanPlanet.nif")
        pSet.AddObjectToSet(pPlanet1, "Banzai 2")

        #Place the object at the specified location.
        pPlanet1.PlaceObjectByName("Planet2 Location")
        pPlanet1.UpdateNodeOnly()

        # Model and placement for Banzai2Moon1
        pPlanet2 = App.Planet_Create(60.0, "data/models/environment/IcePlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Banzai 2 Alpha")

        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Moon1 Location")
        pPlanet2.UpdateNodeOnly()

        # Model and placement for Banzai2Moon2
        pPlanet3 = App.Planet_Create(70.0, "data/models/environment/TanGasPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Banzai 2 Beta")

        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Moon2 Location")
        pPlanet3.UpdateNodeOnly()

        # Model and placement for Banzai3
        pPlanet4 = App.Planet_Create(1000.0, "data/models/environment/PurpleWhitePlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Banzai 3")

        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Banzai3")
        pPlanet4.UpdateNodeOnly()

        # Model and placement for Banzai3Moon1
        pPlanet5 = App.Planet_Create(40.0, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Banzai 3 Alpha")

        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Moon3 Location")
        pPlanet5.UpdateNodeOnly()

        # Model and placement for Banzai4
        pPlanet6 = App.Planet_Create(40.0, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet6, "Banzai 4")

        #Place the object at the specified location.
        pPlanet6.PlaceObjectByName("Banzai4 Location")
        pPlanet6.UpdateNodeOnly()
        
        pNebula = App.MetaNebula_Create(30.0 / 255.0,  30.0 / 255.0, 40.0  / 255.0, 3000.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(0.1, 0.1)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(-30100, -120000, -1000, 3000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1") 
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                # Create our static stations and such
                pGekiStation    = loadspacehelper.CreateShip("FedOutpost", pSet, "Banzai Facility", "Station Location")
                if (pGekiStation != None):
                        # Damage the Geki station and give it rotation
                        MissionLib.SetRandomRotation(pGekiStation, 9.0)               
                        # Damage it's hull
                        pRepair = pGekiStation.GetRepairSubsystem()
                        pProp   = pRepair.GetProperty()
                        # pProp.SetMaxRepairPoints(0.0)
                        pGekiStation.DamageSystem(pGekiStation.GetHull(), pGekiStation.GetHull().GetMaxCondition() * 0.80)
                        # MissionLib.HideSubsystems(pGekiStation)
                        pGekiStation.DisableGlowAlphaMaps()

               # Create ship
                pTransport       = loadspacehelper.CreateShip("Transport", pSet, "Banzai Freighter", "BF Locale")
                
              # Create ship
                pTransport2       = loadspacehelper.CreateShip("Transport", pSet, "BZ Transport", "BZ4T Locale")
                
               # Create ship
                pFarragut        = loadspacehelper.CreateShip("Nebula", pSet, "USS Farragut", "Farragut Location")
        
               # Create a Communications Relay
                pArray   = loadspacehelper.CreateShip("CommArray", pSet, "Comm Array", "Array Location")             

              # Create ship
                pKeldon   = loadspacehelper.CreateShip("Keldon", pSet, "Weyoun", "Gul Locale")
         
              # Create ship
                pGalor    = loadspacehelper.CreateShip("Keldon", pSet, "Gul Dumar", "Galor Locale")

              # Create ship
                pGalor2    = loadspacehelper.CreateShip("Galor", pSet, "Galor Gul", "Galor2 Locale")

              # Create ship
                pBOP    = loadspacehelper.CreateShip("BirdOfPrey", pSet, "IKV Batleth", "BOP Locale")
         
              # Create ship
                pGalaxy   = loadspacehelper.CreateShip("Galaxy", pSet, "USS Yamato", "Galaxy Locale")
 
        
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
                pNeutrals.AddName("BZ Transport")
                pNeutrals.AddName("Banzai Freighter")

                pTransport.SetAI(WarpToObjectSelfDefenseAI.CreateAI(pTransport, pGekiStation, pPlanet))
                pTransport2.SetAI(RouteAI.CreateAI(pTransport2, pGekiStation, pPlanet2))
                pFarragut.SetAI(DefendAI.CreateAI(pFarragut, pGekiStation))       
                pKeldon.SetAI(KeldonAI.CreateAI(pKeldon))
                pGalor.SetAI(GalorAI.CreateAI(pGalor))
                pGalor2.SetAI(Galor2AI.CreateAI(pGalor2))
                pBOP.SetAI(BOPAI.CreateAI(pBOP))             
                pGalaxy.SetAI(DefendAI.CreateAI(pGalaxy, pGekiStation))   

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

                
                pSet = App.g_kSetManager.GetSet("BeyondTheGalaxy1")
                pPlanet = App.Planet_GetObject(pSet, "Banzai 1")
                pPlanet2 = App.Planet_GetObject(pSet, "Banzai 2 Alpha")
                pGekiStation = App.ShipClass_GetObject(pSet, "Banzai Facility")
                pTransport = App.ShipClass_GetObject(pSet, "Banzai Freighter")
                pTransport2 = App.ShipClass_GetObject(pSet, "BZ Transport")
                pFarragut = App.ShipClass_GetObject(pSet, "USS Farragut")
                pGalaxy = App.ShipClass_GetObject(pSet, "USS Yamato")
                pKeldon = App.ShipClass_GetObject(pSet, "Weyoun")
                pGalor = App.ShipClass_GetObject(pSet, "Gul Dumar")
                pGalor2 = App.ShipClass_GetObject(pSet, "Galor Gul")
                pBOP = App.ShipClass_GetObject(pSet, "IKV Batleth")

                if pTransport != None:
                        pNeutralGroup.AddName("Banzai Freighter")
                if (pTransport != None) and (pGekiStation != None):
                        pTransport.SetAI(WarpToObjectSelfDefenseAI.CreateAI(pTransport, pGekiStation, pPlanet))
                if (pTransport2 != None) and (pGekiStation != None):
                        pNeutralGroup.AddName("BZ Transport")
                if (pTransport2 != None) and (pGekiStation != None):
                        pTransport2.SetAI(RouteAI.CreateAI(pTransport2, pGekiStation, pPlanet2))
                if (pFarragut != None) and (pGekiStation != None):
                        pFarragut.SetAI(DefendAI.CreateAI(pFarragut, pGekiStation))
                if (pGalaxy != None) and (pGekiStation != None):
                        pGalaxy.SetAI(DefendAI.CreateAI(pGalaxy, pGekiStation))
                if pKeldon != None:
                        pKeldon.SetAI(KeldonAI.CreateAI(pKeldon))
                if pGalor != None:
                        pGalor.SetAI(GalorAI.CreateAI(pGalor))
                if pGalor2 != None:
                        pGalor2.SetAI(Galor2AI.CreateAI(pGalor2))
                if pBOP != None:
                        pBOP.SetAI(BOPAI.CreateAI(pBOP))
