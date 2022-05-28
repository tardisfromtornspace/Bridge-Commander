###############################################################################
#       Filename:       Ross_1281_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#       
#       Creates Ross_128 static objects.  Called by Ross_1281.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#                       August 2003 - Chris Jones
# Modified for Multiplayer with Banzai Wolf 359 ships added - 12/19/03 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares
import loadspacehelper
import MissionLib
import WeakSelfDefenseAI

def Initialize(pSet):

        pSun = App.Sun_Create(3000.0, 7000, 6000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Ross 128")   
        pSun.PlaceObjectByName( "Ross 128" )
        pSun.UpdateNodeOnly()
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
        
        pWolf359 = App.Sun_Create(200.0, 20, 3000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pWolf359, "Wolf 359")       
        pWolf359.PlaceObjectByName( "Wolf 359" )
        pWolf359.UpdateNodeOnly()
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pWolf359)

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()): 
        
                # Create ship
                pTransport      = loadspacehelper.CreateShip("Galaxy", pSet, "Galaxy Wreck", "Transport Location")
                pTransport.ReplaceTexture("data/Models/SharedTextures/FedShips/Venture.tga", "ID")
                import GalaxyHulk
                GalaxyHulk.AddDamage(pTransport)
                
                # Turn off the ships repair
                pRepair = pTransport.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the Hulk...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pTransport)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pTransport.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pTransport.DamageSystem(pTransport.GetHull(), 3000)
                pTransport.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pTransport)
                # Spin the hulk
                MissionLib.SetRandomRotation(pTransport, 8)
                pTransport.SetTargetable(0)
                
                # Create a Communications Relay
                pArray  = loadspacehelper.CreateShip("CommLight", pSet, "Comm Array", "Array Location")
                pArray.SetTargetable(0)

                pHulk1          = loadspacehelper.CreateShip("Ambassador", pSet, "Saratoga", "wreck1")
                pHulk2          = loadspacehelper.CreateShip("Nebula", pSet, "Kyushu", "wreck2")
                pHulk5          = loadspacehelper.CreateShip("Galaxy", pSet, "Yamaguchi", "wreck5")
                pHulk10         = loadspacehelper.CreateShip("Nebula", pSet, "Melbourne", "wreck10")
                pHulk13         = loadspacehelper.CreateShip("Ambassador", pSet, "Tolstoy", "wreck13")
                     
                # Import our damaged script ship and apply it to the Hulk1
                pHulk1.SetHailable(0)
                import DamageAmbas1
                DamageAmbas1.AddDamage(pHulk1)
                # Turn off the ships repair
                pRepair = pHulk1.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the Hulk1...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk1)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk1.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk1.DamageSystem(pHulk1.GetHull(), 2500)
                pHulk1.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk1)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk1, 5)
                
                # Import our damaged script ship and apply it to the Hulk2
                pHulk2.SetHailable(0)
                import DamageNebula1
                DamageNebula1.AddDamage(pHulk2)
                # Turn off the ships repair
                pRepair = pHulk2.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the Hulk2...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk2)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk2.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk2.DamageSystem(pHulk2.GetHull(), 3000)
                pHulk2.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk2)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk2, 10)
                
                # Import our damaged script ship and apply it to the Hulk5
                pHulk5.SetHailable(0)
                import DamageGal1
                DamageGal1.AddDamage(pHulk5)
                # Turn off the ships repair
                pRepair = pHulk5.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the pHulk5...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk5)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk5.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk5.DamageSystem(pHulk5.GetHull(), 3000)
                pHulk5.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk5)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk5, 8)
                
                # Import our damaged script ship and apply it to the pHulk10
                pHulk10.SetHailable(0)
                import DamageNeb2
                DamageNeb2.AddDamage(pHulk10)
                # Turn off the ships repair
                pRepair = pHulk10.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the pHulk10...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk10)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk10.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk10.DamageSystem(pHulk10.GetHull(), 4500)
                pHulk10.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk10)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk10, 6)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk10, 7)
                
                # Import our damaged script ship and apply it to the pHulk13
                pHulk13.SetHailable(0)
                import DamageAmbas2
                DamageAmbas2.AddDamage(pHulk13)
                # Turn off the ships repair
                pRepair = pHulk13.GetRepairSubsystem()
                pProp   = pRepair.GetProperty()
                pProp.SetMaxRepairPoints(0.0)
                # Damage the pHulk13...
                # Turn off the shields
                pAlertEvent = App.TGIntEvent_Create()
                pAlertEvent.SetDestination(pHulk13)
                pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
                pAlertEvent.SetInt(pHulk13.GREEN_ALERT)
                App.g_kEventManager.AddEvent(pAlertEvent)
                # Damage the hull - 500 pts left
                pHulk13.DamageSystem(pHulk13.GetHull(), 3000)
                pHulk13.DisableGlowAlphaMaps()
                # Dont allow the user to see the sub-systems
                MissionLib.HideSubsystems(pHulk13)
                # Spin the hulk
                MissionLib.SetRandomRotation(pHulk13, 7)

                # Create ship
                pGalaxy = loadspacehelper.CreateShip("Galaxy", pSet, "USS Enterprise", "ED locale")
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
                # Damage the hull - 500 pts left
                pGalaxy.DamageSystem(pHulk13.GetHull(), 2990)
                pGalaxy.DisableGlowAlphaMaps()
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
                        vVelocity = pHulk10.GetWorldLocation()
                        vVelocity.Subtract(pAsteroid.GetWorldLocation())
                        vVelocity.Unitize()
                        vVelocity.Scale(3)
                        pAsteroid.SetVelocity(vVelocity)


        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
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
                
                pSet = App.g_kSetManager.GetSet("Ross_1281")
                pGalaxy = App.ShipClass_GetObject(pSet, "USS Enterprise")
                if pGalaxy != None:
                   pGalaxy.SetAI(WeakSelfDefenseAI.CreateAI(pGalaxy))
