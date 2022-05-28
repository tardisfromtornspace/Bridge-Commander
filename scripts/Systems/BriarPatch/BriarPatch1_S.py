###############################################################################
#       Filename:       BriarPatch1_S.py
#       
#       Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#       
#       Creates BriarPatch 1 static objects.  Called by BriarPatch1.py when region is created
#       
#       Created:        09/17/00 
#       Modified:       10/04/01 - Tony Evans
#       Modified:       08/25/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(1900.0, 400, 500, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresBlue.tga")
        pSet.AddObjectToSet(pSun, "Brer Fox")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Add a sun, far far away
        pSun2 = App.Sun_Create(1800.0, 2500, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun2, "Brer Rabbit")
        
        # Place the object at the specified location.
        pSun2.PlaceObjectByName( "Sun2" )
        pSun2.UpdateNodeOnly()

        # Heeeeeeres Saturn
        pSaturn = App.Planet_Create(500.0, "data/models/environment/Saturn.nif")
        pSet.AddObjectToSet(pSaturn, "BakuRings")

        # Place the object at the specified location.
        pSaturn.PlaceObjectByName( "RingPlanet" )
        pSaturn.SetAtmosphereRadius(0.01)
        pSaturn.UpdateNodeOnly()
        
        pCentral = App.Planet_Create(245.0, "data/models/environment/AquaPlanet.nif")
        pSet.AddObjectToSet(pCentral, "Baku")

        # Place the object at the specified location.
        pCentral.PlaceObjectByName( "RingPlanet1" )
        pCentral.SetAtmosphereRadius(1.0)
        pCentral.UpdateNodeOnly()

        # MetaNebula_Create params are:
        # r, g, b : (floats [0.0 , 1.0]) 
        # visibility distance inside the nebula (float in world units)
        # sensor density of nebula(value to scale sensor range by)
         # name of internal texture (needs alpha)
        # name of external texture (no need for alpha)
        
        pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula.SetupDamage(1.0, 5.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula.AddNebulaSphere(4800.0, 4945.0, -3600.0,  5000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula, "Nebula1")
        
        pNebula2 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula2.SetupDamage(0.0, 5.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula2.AddNebulaSphere(-2900.0, 8004.0, 9100.0, 9000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula2, "Nebula2")
        
        pNebula4 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula4.SetupDamage(1.0, 10.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula4.AddNebulaSphere(300.0, 1245.0, -300.0, 1000.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula4, "Nebula4")
        
        pNebula5 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula5.SetupDamage(5.0, 50.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula5.AddNebulaSphere(250.0, 1245.0, 100.0, 850.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula5, "Nebula5")
        
        pNebula6 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 4.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula6.SetupDamage(95.0, 290.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula6.AddNebulaSphere(3800.0, 2945.0, -1600.0, 250.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula6, "Nebula6")
        
        pNebula7 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 4.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
        # Set nebula damage/sec to Hull/Shields.
        pNebula7.SetupDamage(25.0, 270.0)
        # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        pNebula7.AddNebulaSphere(1800.0, 2545.0, -2600.0, 450.0)
        # Puts the nebula in the set
        pSet.AddObjectToSet(pNebula7, "Nebula7")

        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
                pHulk1          = loadspacehelper.CreateShip("SunBuster", pSet, "Wreckage", "wreck")            
                DamageWrecks(pHulk1)

def DamageWrecks(pHulk1):

        # Import our damaged script ship and apply it to the Hulk1
        pHulk1.SetHailable(0)
        import DamageSun
        DamageSun.AddDamage(pHulk1)
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
        pHulk1.DamageSystem(pHulk1.GetHull(), 3500)
        pHulk1.DisableGlowAlphaMaps()
        # Dont allow the user to see the sub-systems
        MissionLib.HideSubsystems(pHulk1)
        # Spin the hulk
        MissionLib.SetRandomRotation(pHulk1, 10)
