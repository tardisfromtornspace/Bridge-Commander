###############################################################################
#       Filename:       BeyondTheGalaxy1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates BeyondTheGalaxy1 static objects.  Called by BeyondTheGalaxy1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       09/15/02 - Ben Howard - TheGalaxy7
#       Ships/Wrecks/AIs: Sept. 2003 - Chris Jones
#       Modified for MultiPlayer 12-16-03 Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import WeakSelfDefenseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(400.0, 800, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun, "Rogue Star")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):                
                # Create ship
                pCardassian     = loadspacehelper.CreateShip("Galor", pSet, "Gul Cardass", "Gul Cardass")
                # import Gul CardassDamage
                # Gul CardassDamage.AddDamage(pCardassian)      
                pRepair = pCardassian.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(30.0)
                # Damage the Hulk...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pCardassian)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pCardassian.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the shield generator
                pShields = pCardassian.GetShields()
                # Front
                pShields.SetCurShields(pShields.FRONT_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.0)
                # Rear
                pShields.SetCurShields(pShields.REAR_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.0)
                # Left
                pShields.SetCurShields(pShields.LEFT_SHIELDS, pShields.GetMaxShields(pShields.LEFT_SHIELDS) * 0.10)
                # Right
                pShields.SetCurShields(pShields.RIGHT_SHIELDS, pShields.GetMaxShields(pShields.RIGHT_SHIELDS)* 0.0)
                # Top
                pShields.SetCurShields(pShields.TOP_SHIELDS, pShields.GetMaxShields(pShields.TOP_SHIELDS) * 0.0)
                # Bottom
                pShields.SetCurShields(pShields.BOTTOM_SHIELDS, pShields.GetMaxShields(pShields.BOTTOM_SHIELDS) * 0.07)         
                # Damage the hull - 500 pts left
                pCardassian.DamageSystem(pCardassian.GetHull(), 3000)
                pCardassian.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                # MissionLib.HideSubsystems(pCardassian)
                # Spin the hulk
                MissionLib.SetRandomRotation(pCardassian, 100)
                pImpulseEngines = pCardassian.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pCardassian.DamageSystem(pCardassian.GetImpulseEngineSubsystem(), sImpulseEngine)               
                pProp = pCardassian.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()  
                maxSpeed = maxSpeed * 0.01
                pProp.SetMaxSpeed(maxSpeed)
                pCardassian.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )  
                pPhasers = pCardassian.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5    
                pCardassian.DamageSystem(pCardassian.GetPhaserSystem(), sPhaser)        
        
                # Create ship
                pGalor2 = loadspacehelper.CreateShip("Galor", pSet, "Son of Dukat", "Son of Dukat")
                # import Gul CardassDamage
                # Gul CardassDamage.AddDamage(pGalor2)  
                pRepair = pGalor2.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(30.0)
                # Damage the Hulk...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pGalor2)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pGalor2.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the shield generator
                pShields = pGalor2.GetShields()
                # Front
                pShields.SetCurShields(pShields.FRONT_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.0)
                # Rear
                pShields.SetCurShields(pShields.REAR_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.0)
                # Left
                pShields.SetCurShields(pShields.LEFT_SHIELDS, pShields.GetMaxShields(pShields.LEFT_SHIELDS) * 0.10)
                # Right
                pShields.SetCurShields(pShields.RIGHT_SHIELDS, pShields.GetMaxShields(pShields.RIGHT_SHIELDS)* 0.0)
                # Top
                pShields.SetCurShields(pShields.TOP_SHIELDS, pShields.GetMaxShields(pShields.TOP_SHIELDS) * 0.0)
                # Bottom
                pShields.SetCurShields(pShields.BOTTOM_SHIELDS, pShields.GetMaxShields(pShields.BOTTOM_SHIELDS) * 0.0)          
                # Damage the hull - 500 pts left
                pGalor2.DamageSystem(pGalor2.GetHull(), 3000)
                pGalor2.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                # MissionLib.HideSubsystems(pGalor2)
                # Spin the hulk
                MissionLib.SetRandomRotation(pGalor2, 100)
                pImpulseEngines = pGalor2.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pGalor2.DamageSystem(pGalor2.GetImpulseEngineSubsystem(), sImpulseEngine)               
                pProp = pGalor2.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()  
                maxSpeed = maxSpeed * 0.01
                pProp.SetMaxSpeed(maxSpeed)
                pGalor2.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )      
                pPhasers = pGalor2.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5    
                pGalor2.DamageSystem(pGalor2.GetPhaserSystem(), sPhaser)        
        
                # Create ship
                pGalor3 = loadspacehelper.CreateShip("Galor", pSet, "Son of Damar", "Son of Damar")
                # import Gul CardassDamage
                # Gul CardassDamage.AddDamage(pGalor3)  
                pRepair = pGalor3.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(30.0)
                # Damage the Hulk...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pGalor3)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pGalor3.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
               # Damage the shield generator
                pShields = pGalor3.GetShields()
                # Front
                pShields.SetCurShields(pShields.FRONT_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.0)
                # Rear
                pShields.SetCurShields(pShields.REAR_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.0)
                # Left
                pShields.SetCurShields(pShields.LEFT_SHIELDS, pShields.GetMaxShields(pShields.LEFT_SHIELDS) * 0.10)
                # Right
                pShields.SetCurShields(pShields.RIGHT_SHIELDS, pShields.GetMaxShields(pShields.RIGHT_SHIELDS)* 0.0)
                # Top
                pShields.SetCurShields(pShields.TOP_SHIELDS, pShields.GetMaxShields(pShields.TOP_SHIELDS) * 0.0)
                # Bottom
                pShields.SetCurShields(pShields.BOTTOM_SHIELDS, pShields.GetMaxShields(pShields.BOTTOM_SHIELDS) * 0.0)          
                # Damage the hull - 500 pts left
                pGalor3.DamageSystem(pGalor3.GetHull(), 3000)
                pGalor3.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                # MissionLib.HideSubsystems(pGalor3)
                # Spin the hulk
                MissionLib.SetRandomRotation(pGalor3, 100)
                pImpulseEngines = pGalor3.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pGalor3.DamageSystem(pGalor3.GetImpulseEngineSubsystem(), sImpulseEngine)               
                pProp = pGalor3.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()  
                maxSpeed = maxSpeed * 0.01
                pProp.SetMaxSpeed(maxSpeed)
                pGalor3.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )      
                pPhasers = pGalor3.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.0    
                pGalor3.DamageSystem(pGalor3.GetPhaserSystem(), sPhaser)        
                
                # Create ship
                pGalaxy = loadspacehelper.CreateShip("Nebula", pSet, "USS America", "Galaxy")
                # import GalaxyDamage
                # GalaxyDamage.AddDamage(pGalaxy)
                # Turn off the ships repair
                pRepair = pGalaxy.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(30.0)
                # Damage the Hulk...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pGalaxy)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pGalaxy.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the shield generator
                pShields = pGalaxy.GetShields()
                # Front
                pShields.SetCurShields(pShields.FRONT_SHIELDS, pShields.GetMaxShields(pShields.FRONT_SHIELDS) * 0.00)
                # Rear
                pShields.SetCurShields(pShields.REAR_SHIELDS, pShields.GetMaxShields(pShields.REAR_SHIELDS) * 0.00)
                # Left
                pShields.SetCurShields(pShields.LEFT_SHIELDS, pShields.GetMaxShields(pShields.LEFT_SHIELDS) * 0.05)
                # Right
                pShields.SetCurShields(pShields.RIGHT_SHIELDS, pShields.GetMaxShields(pShields.RIGHT_SHIELDS)* 0.05)
                # Top
                pShields.SetCurShields(pShields.TOP_SHIELDS, pShields.GetMaxShields(pShields.TOP_SHIELDS) * 0.10)
                # Bottom
                pShields.SetCurShields(pShields.BOTTOM_SHIELDS, pShields.GetMaxShields(pShields.BOTTOM_SHIELDS) * 0.00) 
                # Damage the hull - 500 pts left
                pGalaxy.DamageSystem(pGalaxy.GetHull(), 3000)
                pGalaxy.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                # MissionLib.HideSubsystems(pGalaxy)
                # Spin the hulk
                MissionLib.SetRandomRotation(pGalaxy, 79)
                pImpulseEngines = pGalaxy.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pGalaxy.DamageSystem(pGalaxy.GetImpulseEngineSubsystem(), sImpulseEngine)               
                pProp = pGalaxy.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()  
                maxSpeed = maxSpeed * 0.01
                pProp.SetMaxSpeed(maxSpeed)
                pGalaxy.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )      
                pPhasers = pGalaxy.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5    
                pGalaxy.DamageSystem(pGalaxy.GetPhaserSystem(), sPhaser)        

                pAsteroid = loadspacehelper.CreateShip ("Asteroidh1", pSet, "Unknown Debris", "Asteroid")
                if (pAsteroid):
                        # Set objects Genus to Asteroid.
                        pProperty = pAsteroid.GetShipProperty()
                        pProperty.SetGenus(App.GENUS_ASTEROID)
                        # Set the scale of the asteroid object
                        pAsteroid.SetScale (10.0)
                        
                        #Rotate the asteroid
                        vVelocity = App.TGPoint3_GetModelForward()      # Get the vector to rotate around
                        vVelocity.Scale( 15.0 * App.PI / 180.0 )                # Scale it to value in dictonary
                        pAsteroid.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
                        
                        # As an alternative to sending the asteroid forward along
                        # the direction of the placement, send the asteroid directly
                        # toward the center of the station.
                        vVelocity = pGalor2.GetWorldLocation()
                        vVelocity.Subtract(pAsteroid.GetWorldLocation())
                        vVelocity.Unitize()
                        vVelocity.Scale(3)
                        pAsteroid.SetVelocity(vVelocity)
        
        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pCardassian.SetAI(WeakSelfDefenseAI.CreateAI(pCardassian))   
                pGalor2.SetAI(WeakSelfDefenseAI.CreateAI(pGalor2))
                pGalor3.SetAI(WeakSelfDefenseAI.CreateAI(pGalor3))      
                pGalaxy.SetAI(WeakSelfDefenseAI.CreateAI(pGalaxy))

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
                pCardassian = App.ShipClass_GetObject(pSet, "Gul Cardass")
                pGalor2 = App.ShipClass_GetObject(pSet, "Son of Dukat")
                pGalor3 = App.ShipClass_GetObject(pSet, "Son of Damar")
                pGalaxy = App.ShipClass_GetObject(pSet, "USS America")
                if pCardassian != None:
                        pCardassian.SetAI(WeakSelfDefenseAI.CreateAI(pCardassian))
                if pGalor2 != None:
                        pGalor2.SetAI(WeakSelfDefenseAI.CreateAI(pGalor2))
                if pGalor3 != None:
                        pGalor3.SetAI(WeakSelfDefenseAI.CreateAI(pGalor3))
                if pGalaxy != None:
                        pGalaxy.SetAI(WeakSelfDefenseAI.CreateAI(pGalaxy))
