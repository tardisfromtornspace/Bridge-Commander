from bcdebug import debug
###############################################################################
#	Filename:	Wolf3591_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Wolf359 1 static objects.  Called by Wolf3591.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	03/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

	# Add a sun, far far away
	debug(__name__ + ", Initialize")
	pSun = App.Sun_Create(500.0, 2000, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()
	
	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.WhiteLensFlare(pSet, pSun)
	
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        pHulk1		= loadspacehelper.CreateShip("Ambassador", pSet, "Saratoga", "wreck1")
	        pHulk2		= loadspacehelper.CreateShip("Nebula", pSet, "Kyushu", "wreck2")
	        pHulk3		= loadspacehelper.CreateShip("Akira", pSet, "Gage", "wreck3")
	        pHulk4		= loadspacehelper.CreateShip("Galaxy", pSet, "Buran", "wreck4")
	        pHulk5		= loadspacehelper.CreateShip("Ambassador", pSet, "Yamaguchi", "wreck5")
	        pHulk6		= loadspacehelper.CreateShip("Ambassador", pSet, "Bonestell", "wreck6")
	        pHulk7		= loadspacehelper.CreateShip("Nebula", pSet, "Golden Apple", "wreck7")
	        pHulk8		= loadspacehelper.CreateShip("Akira", pSet, "FireBrand", "wreck8")
	        pHulk9		= loadspacehelper.CreateShip("Nebula", pSet, "Chekov", "wreck9")
	        pHulk10		= loadspacehelper.CreateShip("Galaxy", pSet, "Melbourne", "wreck10")
	        pHulk11		= loadspacehelper.CreateShip("Nebula", pSet, "Bellerophon", "wreck11")
	        pHulk12		= loadspacehelper.CreateShip("Akira", pSet, "Princeton", "wreck12")
	        pHulk13		= loadspacehelper.CreateShip("Ambassador", pSet, "Tolstoy", "wreck13")
	
	        DamageWrecks(pHulk1, pHulk2, pHulk3, pHulk4, pHulk5, pHulk6, pHulk7, pHulk8, pHulk9, pHulk10, pHulk11, pHulk12, pHulk13)


def DamageWrecks(pHulk1, pHulk2, pHulk3, pHulk4, pHulk5, pHulk6, pHulk7, pHulk8, pHulk9, pHulk10, pHulk11, pHulk12, pHulk13):

	# Import our damaged script ship and apply it to the Hulk1
	debug(__name__ + ", DamageWrecks")
	pHulk1.SetHailable(0)
	import DamageAmbas1
	DamageAmbas1.AddDamage(pHulk1)
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
	MissionLib.SetRandomRotation(pHulk1, 5)
	
	# Import our damaged script ship and apply it to the Hulk2
	pHulk2.SetHailable(0)
	import DamageNebula1
	DamageNebula1.AddDamage(pHulk2)
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
	pHulk2.DamageSystem(pHulk2.GetHull(), 3000)
	pHulk2.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk2)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk2, 10)
		
	# Import our damaged script ship and apply it to the Hulk3
	pHulk3.SetHailable(0)
	import DamageAkira1
	DamageAkira1.AddDamage(pHulk3)
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
	pHulk3.DamageSystem(pHulk3.GetHull(), 4500)
	pHulk3.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk3)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk3, 9)
	
	# Import our damaged script ship and apply it to the Hulk4
	pHulk4.SetHailable(0)
	import DamageGal1
	DamageGal1.AddDamage(pHulk4)
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
	pHulk4.DamageSystem(pHulk4.GetHull(), 5000)
	pHulk4.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk4)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk4, 7)
	
	# Import our damaged script ship and apply it to the Hulk5
	pHulk5.SetHailable(0)
	import DamageAmbas2
	DamageAmbas2.AddDamage(pHulk5)
	# Turn off the ships repair
	pRepair = pHulk5.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
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
		
	# Import our damaged script ship and apply it to the Hulk6
	pHulk6.SetHailable(0)
	import DamageAmbas3
	DamageAmbas3.AddDamage(pHulk6)
	# Turn off the ships repair
	pRepair = pHulk6.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the Hulk6...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk6)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk6.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk6.DamageSystem(pHulk6.GetHull(), 4500)
	pHulk6.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk6)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk6, 4)

	# Import our damaged script ship and apply it to the Hulk7
	pHulk7.SetHailable(0)
	import DamageNeb2
	DamageNeb2.AddDamage(pHulk7)
	# Turn off the ships repair
	pRepair = pHulk7.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the Hulk7...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk7)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk7.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk7.DamageSystem(pHulk7.GetHull(), 3000)
	pHulk7.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk7)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk7, 3)
	
	# Import our damaged script ship and apply it to the Hulk8
	pHulk8.SetHailable(0)
	import DamageAkira2
	DamageAkira2.AddDamage(pHulk8)
	# Turn off the ships repair
	pRepair = pHulk8.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the pHulk8...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk8)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk8.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk8.DamageSystem(pHulk8.GetHull(), 3200)
	pHulk8.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk8)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk8, 2)
	
	# Import our damaged script ship and apply it to the Hulk9
	pHulk9.SetHailable(0)
	import DamageNeb3
	DamageNeb3.AddDamage(pHulk9)
	# Turn off the ships repair
	pRepair = pHulk9.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the pHulk9...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk9)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk9.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk9.DamageSystem(pHulk9.GetHull(), 3000)
	pHulk9.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk9)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk9, 1)
		
	# Import our damaged script ship and apply it to the pHulk10
	pHulk10.SetHailable(0)
	import Hulk1Damaged
	Hulk1Damaged.AddDamage(pHulk10)
	# Turn off the ships repair
	pRepair = pHulk10.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
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
	
	# Import our damaged script ship and apply it to the pHulk11
	pHulk11.SetHailable(0)
	import Hulk1Damaged
	Hulk1Damaged.AddDamage(pHulk11)
	# Turn off the ships repair
	pRepair = pHulk11.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the pHulk11...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk11)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk11.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk11.DamageSystem(pHulk11.GetHull(), 4000)
	pHulk11.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk11)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk11, 3)
	"""	
	# Import our damaged script ship and apply it to the pHulk12
	pHulk12.SetHailable(0)
	import Hulk2Damaged
	Hulk2Damaged.AddDamage(pHulk12)
	# Turn off the ships repair
	pRepair = pHulk12.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the pHulk12...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk12)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk12.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk12.DamageSystem(pHulk12.GetHull(), 4500)
	pHulk12.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk12)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk12, 11)
	"""
	# Import our damaged script ship and apply it to the pHulk13
	pHulk13.SetHailable(0)
	import DauntlessDamaged
	DauntlessDamaged.AddDamage(pHulk13)
	# Turn off the ships repair
	pRepair = pHulk13.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
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
	
