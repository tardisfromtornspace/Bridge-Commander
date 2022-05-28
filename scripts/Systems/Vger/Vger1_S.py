###############################################################################
#	Filename:	Vger1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Vger 1 static objects.  Called by Vger1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	03/15/02 - Ben Howard
###############################################################################
import App
import MissionLib
import loadspacehelper

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(90.0, 300, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Sensor Anomaly")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
    # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(30.0 / 255.0,  30.0 / 255.0, 40.0  / 255.0, 3000.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.1, 0.1)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(100.0, 20500.0, 50.000000, 3000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(100.0 / 255.0, 100.0 / 255.0, 125.0  / 255.0, 1000.0, 5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(0.1, 0.1)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(100.0, 20400.0, 50.000000, 1500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")
	
	pNebula3 = App.MetaNebula_Create(180.0 / 255.0, 180.0 / 255.0, 220.0  / 255.0, 10.0, 10, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula3.SetupDamage(0.1, 0.1)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula3.AddNebulaSphere(100.0, 20600.0, 50.000000, 550.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")

        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        # Create our static stations and such
	        pBasestar	= loadspacehelper.CreateShip("CardStarbase", pSet, "Vger", "evil")
	        if (pBasestar != None):
		        import VgerAI
		        pBasestar.SetAI(VgerAI.CreateAI(pBasestar))

	        # Create our static stations and such
	        pBasestar2	= loadspacehelper.CreateShip("CardStarbase", pSet, "V-ger", "evil2")
	        if (pBasestar2 != None):
		        import VgerAI
		        pBasestar2.SetAI(VgerAI.CreateAI(pBasestar2))


	        pHulk1		= loadspacehelper.CreateShip("Vorcha", pSet, "War Hammer", "wreck1")
	        pHulk2		= loadspacehelper.CreateShip("BirdOfPrey", pSet, "Raptor", "wreck2")
	        pHulk3		= loadspacehelper.CreateShip("BirdOfPrey", pSet, "Dagger", "wreck3")
	        pHulk4		= loadspacehelper.CreateShip("Nebula", pSet, "Magellan", "wreck4")
	
	        DamageWrecks(pHulk1, pHulk2, pHulk3, pHulk4)


def DamageWrecks(pHulk1, pHulk2, pHulk3, pHulk4):

	# Import our damaged script ship and apply it to the Hulk1
	pHulk1.SetHailable(0)
	import DamageVorcha
	DamageVorcha.AddDamage(pHulk1)
	# Turn off the ships repair
	pRepair = pHulk1.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
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
	MissionLib.SetRandomRotation(pHulk1, 6)
	
	# Import our damaged script ship and apply it to the Hulk2
	pHulk2.SetHailable(0)
	import DamageBoP1
	DamageBoP1.AddDamage(pHulk2)
	# Turn off the ships repair
	pRepair = pHulk2.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the Hulk2...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk2)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk2.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk2.DamageSystem(pHulk2.GetHull(), 1500)
	pHulk2.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk2)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk2, 3)
	
	# Import our damaged script ship and apply it to the Hulk3
	pHulk3.SetHailable(0)
	import DamageBoP2
	DamageBoP2.AddDamage(pHulk3)
	# Turn off the ships repair
	pRepair = pHulk3.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the Hulk3...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk3)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk3.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk3.DamageSystem(pHulk3.GetHull(), 1500)
	pHulk3.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk3)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk3, 8)
	
	# Import our damaged script ship and apply it to the Hulk4
	pHulk4.SetHailable(0)
	import DamageNeb2
	DamageNeb2.AddDamage(pHulk4)
	# Turn off the ships repair
	pRepair = pHulk4.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the Hulk4...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk4)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk4.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk4.DamageSystem(pHulk4.GetHull(), 2500)
	pHulk4.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk4)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk4, 15)
	