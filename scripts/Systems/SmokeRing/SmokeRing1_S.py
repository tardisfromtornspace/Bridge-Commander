###############################################################################
#       Filename:       SmokeRing1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates SmokeRing 1 static objects.  Called by SmokeRing1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       03/15/02 - Ben Howard
#     Ships/Wrecks/AIs  08/29/03 - Chris Jones
#     Adapted for Multiplayer 12/16/03 Chris Jones
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares
import WeakSelfDefenseAI

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(8.0, 10, 500, "data/Textures/SunGreen.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Neutron Star")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.WhiteLensFlare(pSet, pSun)

        # MetaNebula_Create params are:
        # r, g, b : (floats [0.0 , 1.0]) 
        # visibility distance inside the nebula (float in world units)
        # sensor density of nebula(value to scale sensor range by)
        # name of internal texture (needs alpha)
        # name of external texture (no need for alpha)
        
        pNebula = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 10.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(300.0, 1800.0, -270.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")
        
        pNebula2 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(300.0, 1400.0, -330.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
        
        pNebula3 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 15.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula3.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula3.AddNebulaSphere(500.0, 1600.0, -300.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula3, "Nebula3")
        
        pNebula4 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 20.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula4.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula4.AddNebulaSphere(100.0, 1600.0, -300.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula4, "Nebula4")
        
        pNebula5 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 10.0, 70.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula5.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula5.AddNebulaSphere(420.0, 1720.0, -285.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula5, "Nebula5")
        
        pNebula6 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 15.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula6.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula6.AddNebulaSphere(180.0, 1480.0, -315.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula6, "Nebula6")
        
        pNebula7 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0  / 255.0, 20.0, 40.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula7.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula7.AddNebulaSphere(420.0, 1480.0, -315.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula7, "Nebula7")
        
        pNebula8 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0 / 255.0, 10.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula8.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula8.AddNebulaSphere(180.0, 1720.0, -285.000000, 125.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula8, "Nebula8")
        
        pNebula9 = App.MetaNebula_Create(30.0 / 255.0, 160.0 / 255.0, 45.0 / 255.0, 15.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula9.SetupDamage(10.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula9.AddNebulaSphere(380.0, 1760.0, -310.000000, 100.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula9, "Nebula9")
        
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
        
                # Create an asteroid
                pMyAsteroid     = loadspacehelper.CreateShip("Asteroidh3", pSet, "Organic Matter", "Matter1")
                if (pMyAsteroid != None):
                        pProperty = pMyAsteroid.GetShipProperty()
                        pProperty.SetGenus(App.GENUS_ASTEROID)
                        MissionLib.SetRandomRotation(pMyAsteroid, 11.0)
                
                # Create another asteroid
                pMyAsteroid2    = loadspacehelper.CreateShip("Asteroidh2", pSet, "Inert Debris", "Matter2")
                if (pMyAsteroid2 != None):
                        pProperty = pMyAsteroid2.GetShipProperty()
                        pProperty.SetGenus(App.GENUS_ASTEROID)
                        MissionLib.SetRandomRotation(pMyAsteroid2, 7.0) 
        
                # Create ship
                pCardassian     = loadspacehelper.CreateShip("Galor", pSet, "Cardassia7", "Cardassia7")
                import GalorDamage
                GalorDamage.AddDamage(pCardassian)      
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
                pShields.SetCurShields(pShields.FRONT_SHIELDS, pShields.GetMaxShields(pShields.FRONT_SHIELDS) * 0.0)
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
                MissionLib.HideSubsystems(pCardassian)
                # Spin the hulk
                MissionLib.SetRandomRotation(pCardassian, 5)
                pImpulseEngines = pCardassian.GetImpulseEngineSubsystem()
                pMax    = pImpulseEngines.GetMaxCondition()     
                sImpulseEngine = pMax * 0.5     
                pCardassian.DamageSystem(pCardassian.GetImpulseEngineSubsystem(), sImpulseEngine)               
                pProp = pCardassian.GetImpulseEngineSubsystem().GetProperty()
                maxSpeed = pProp.GetMaxSpeed()  
                maxSpeed = maxSpeed * 0.2
                pProp.SetMaxSpeed(maxSpeed)
                pCardassian.SetSpeed( maxSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )  
                pPhasers = pCardassian.GetPhaserSystem()
                pMax    = pPhasers.GetMaxCondition()    
                sPhaser = pMax * 0.5    
                pCardassian.DamageSystem(pCardassian.GetPhaserSystem(), sPhaser)        
        
                # Create ship
                pGalaxy = loadspacehelper.CreateShip("Galaxy", pSet, "USS Galaxy", "Galaxy")
                import GalaxyDamage
                GalaxyDamage.AddDamage(pGalaxy)
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
                MissionLib.SetRandomRotation(pGalaxy, 6)
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

                pCardassian.SetAI(WeakSelfDefenseAI.CreateAI(pCardassian))
                pGalaxy.SetAI(WeakSelfDefenseAI.CreateAI(pGalaxy))
