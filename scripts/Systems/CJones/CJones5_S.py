###############################################################################
#       Filename:       CJones5_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates CJones5 static objects.  Called by CJones5.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans 
#                       August 2003 - Chris Jones
#       Multiplayer 12/16/03 - Chris Jones
###############################################################################
import App
import loadspacehelper
import Tactical.LensFlares
import MissionLib
import RouteAI
import SelfDefenseAI
import DefendAI

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
#       Lensflares available:
#               Tactical.LensFlares.RedOrangeLensFlare
#               Tactical.LensFlares.YellowLensFlare
#               Tactical.LensFlares.BlueLensFlare
#               Tactical.LensFlares.WhiteLensFlare


        pSun = App.Sun_Create(1500.0, 7000, 6000, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Kelios")     
        pSun.PlaceObjectByName( "Kelios" )
        pSun.UpdateNodeOnly()
        Tactical.LensFlares.YellowLensFlare(pSet, pSun)
        
        pSun2 = App.Sun_Create(1500.0, 4000, 600, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun2, "Unknown Dwarf")     
        pSun2.PlaceObjectByName( "Unknown Dwarf" )
        pSun2.UpdateNodeOnly()
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun2)     
        
        # Model and placement for Kelios 1
        pPlanet = App.Planet_Create(280.0, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Kelios 1")
        
        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Kelios 1")
        pPlanet.UpdateNodeOnly()        
        
        # Model and placement for Kelios 2
        pPlanet2 = App.Planet_Create(400.0, "data/models/environment/IcePlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Kelios 2")
                
        # Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Kelios 2 Location")
        pPlanet2.UpdateNodeOnly()
                
        # Model and placement for Kelios 3
        pPlanet3 = App.Planet_Create(160.0, "data/models/environment/RedPlanet.nif")
        pSet.AddObjectToSet(pPlanet3, "Kelios 3")
                        
        #Place the object at the specified location.
        pPlanet3.PlaceObjectByName("Kelios 3 Location")
        pPlanet3.UpdateNodeOnly()
                
        # Model and placement for Kelios 4
        pPlanet4 = App.Planet_Create(160.0, "data/models/environment/BrightGreenPlanet.nif")
        pSet.AddObjectToSet(pPlanet4, "Kelios 4")
                                
        #Place the object at the specified location.
        pPlanet4.PlaceObjectByName("Kelios 4 Location")
        pPlanet4.UpdateNodeOnly()
        
        # Model and placement for Kelios 5
        pPlanet5 = App.Planet_Create(2000.0, "data/models/environment/BlueTanPlanet.nif")
        pSet.AddObjectToSet(pPlanet5, "Kelios 5")
                                
        #Place the object at the specified location.
        pPlanet5.PlaceObjectByName("Kelios 5 Location")
        pPlanet5.UpdateNodeOnly()        
              
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
        kThis.SetFieldRadius(400.0000)
        kThis.SetNumTilesPerAxis(3)
        kThis.SetNumAsteroidsPerTile(1)
        kThis.SetAsteroidSizeFactor(3.000000)
        kThis.UpdateNodeOnly()
        kThis.ConfigField()
        kThis.Update(0)
        kThis = None
        # End position "Asteroid Field 1"

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
  
                # Create ship
                pDamagedShuttle = loadspacehelper.CreateShip("Shuttle", pSet, "Damaged Shuttle", "DamagedShuttle Location")
                if (pDamagedShuttle != None):
                      # Damage the ship and give it rotation
                      MissionLib.SetRandomRotation(pDamagedShuttle, 5.0)
                      # Damage it's hull
                      pRepair = pDamagedShuttle.GetRepairSubsystem()
                      pProp     = pRepair.GetProperty()
                      pProp.SetMaxRepairPoints(0.0)
                      pDamagedShuttle.DamageSystem(pDamagedShuttle.GetHull(), pDamagedShuttle.GetHull().GetMaxCondition() * 0.10)
                pDamagedShuttle.SetAlertLevel(App.ShipClass.RED_ALERT)
                pImpulseEngines = pDamagedShuttle.GetImpulseEngineSubsystem()
                pMax     = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5      
                pDamagedShuttle.DamageSystem(pDamagedShuttle.GetImpulseEngineSubsystem(), sImpulseEngine)
                
                pProp = pDamagedShuttle.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()
        
                maxSpeed = maxSpeed * 0.3
                pProp.SetMaxSpeed(maxSpeed)
                pDamagedShuttle.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )
        
                pPhasers = pDamagedShuttle.GetPhaserSystem()
                pMax     = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5     
                pDamagedShuttle.DamageSystem(pDamagedShuttle.GetPhaserSystem(), sPhaser)
        
               # Create ship
                pTransport       = loadspacehelper.CreateShip("Transport", pSet, "Transport", "Transport Location")
        
               # Create ship
                pDefendingAkira  = loadspacehelper.CreateShip("Akira", pSet, "USS Akira", "Akira")
        
    
        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pTransport.SetAI(RouteAI.CreateAI(pTransport, pPlanet, pPlanet5))
                pDefendingAkira.SetAI(DefendAI.CreateAI(pDefendingAkira, pDamagedShuttle))

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

                pSet = App.g_kSetManager.GetSet("CJones5")
                pPlanet = App.Planet_GetObject(pSet, "Kelios 1")
                pPlanet5 = App.Planet_GetObject(pSet, "Kelios 5")
                pTransport = App.ShipClass_GetObject(pSet, "Transport")
                pDefendingAkira = App.ShipClass_GetObject(pSet, "USS Akira")
                pDamagedShuttle = App.ShipClass_GetObject(pSet, "Damaged Shuttle")
                if pTransport != None:
                        pTransport.SetAI(RouteAI.CreateAI(pTransport, pPlanet, pPlanet5))
                if (pDefendingAkira != None) and (pDamagedShuttle != None):
                        pDefendingAkira.SetAI(DefendAI.CreateAI(pDefendingAkira, pDamagedShuttle))
