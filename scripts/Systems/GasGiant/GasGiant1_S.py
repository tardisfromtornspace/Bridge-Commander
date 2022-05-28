###############################################################################
#       Filename:       GasGiant_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates GasGiant static objects.  Called by GasGiant1_S.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       July 2003 - Chris Jones
# MultiPlayer version 12/17/03 - Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import SelfDefenseNoWarpAI
##import BreenAI
import RouteAI

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

        pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 445.0, 10.5, "data/Backgrounds/BlueGasPlanet.tga", "data/Backgrounds/BlueGasPlanet.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(5.4, 54.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(20000, 20000, 0,  20000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")
        
        # Model and placement for Neogiah
        pPlanet = App.Planet_Create(7790.0, "data/models/environment/BrightGreenPlanet.nif")
        pSet.AddObjectToSet(pPlanet, "Neogiah")
        
        #Place the object at the specified location.
        pPlanet.PlaceObjectByName("Neogiah Location")
        pPlanet.UpdateNodeOnly()
        
        # Model and placement for Unknown Planet
        pPlanet2 = App.Planet_Create(200.0, "data/models/environment/BlueRockyPlanet.nif")
        pSet.AddObjectToSet(pPlanet2, "Unknown Planet")
        
        #Place the object at the specified location.
        pPlanet2.PlaceObjectByName("Unknown Planet Location")
        pPlanet2.UpdateNodeOnly()
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                #hulk
                pHulk27 = loadspacehelper.CreateShip("Transport", pSet, "Scenic Tour", "Tour Location")
                import LightDamage
                LightDamage.AddDamage(pHulk27)  
                
                pImpulseEngines = pHulk27.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pHulk27.DamageSystem(pHulk27.GetImpulseEngineSubsystem(), sImpulseEngine)
                        
                pProp = pHulk27.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()
                
                maxSpeed = maxSpeed * 0.1
                pProp.SetMaxSpeed(maxSpeed)
                pHulk27.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )
                
                # Create ship
                pGalaxy = loadspacehelper.CreateShip("Galaxy", pSet, "USS Galaxy", "Galaxy location")
                import LightDamage
                LightDamage.AddDamage(pGalaxy)  
                
                pImpulseEngines = pGalaxy.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pGalaxy.DamageSystem(pGalaxy.GetImpulseEngineSubsystem(), sImpulseEngine)
                        
                pProp = pGalaxy.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()
                
                maxSpeed = maxSpeed * 0.1
                pProp.SetMaxSpeed(maxSpeed)
                pGalaxy.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )
                
                pPhasers = pGalaxy.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5    
                pGalaxy.DamageSystem(pGalaxy.GetPhaserSystem(), sPhaser)        
                
                # Create ship
                pWarbird        = loadspacehelper.CreateShip("Warbird", pSet, "RIS Senator", "Warbird Location")
                


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
                pNeutrals.AddName("Scenic Tour")
                pHulk27.SetAI(SelfDefenseNoWarpAI.CreateAI(pHulk27))
                pGalaxy.SetAI(SelfDefenseNoWarpAI.CreateAI(pGalaxy))
                pWarbird.SetAI(RouteAI.CreateAI(pWarbird, pPlanet2, pPlanet))   

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

                pSet = App.g_kSetManager.GetSet("GasGiant1")
                pPlanet = App.Planet_GetObject(pSet, "Neogiah")
                pPlanet2 = App.Planet_GetObject(pSet, "Unknown Planet")
                pHulk27 = App.ShipClass_GetObject(pSet, "Scenic Tour")
                pGalaxy = App.ShipClass_GetObject(pSet, "USS Galaxy")
                pWarbird = App.ShipClass_GetObject(pSet, "RIS Senator")
                if pHulk27 != None:
                   pNeutralGroup.AddName("Scenic Tour")
                   pHulk27.SetAI(SelfDefenseNoWarpAI.CreateAI(pHulk27))
                if pGalaxy != None:   
                   pGalaxy.SetAI(SelfDefenseNoWarpAI.CreateAI(pGalaxy))
                if pWarbird != None:   
                   pWarbird.SetAI(RouteAI.CreateAI(pWarbird, pPlanet2, pPlanet))   
