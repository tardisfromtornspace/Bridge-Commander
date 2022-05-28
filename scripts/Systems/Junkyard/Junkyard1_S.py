###############################################################################
#	Filename:	Junkyard1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Junkyard 1 static objects.  Called by Junkyard1.py when region is created
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

#	To create a colored sun:
#	pSun = App.Sun_Create(fRadius, fAtmosphereThickness, fDamagePerSec, fBaseTexture , fFlareTexture)
#
#	for fBaseTexture you can use:
#		data/Textures/SunBase.tga 
#		data/Textures/SunRed.tga
#		data/Textures/SunRedOrange.tga
#		data/Textures/SunYellow.tga
#		data/Textures/SunBlueWhite.tga
#	for fFlareTexture you can use:
#		data/Textures/Effects/SunFlaresOrange.tga
#		data/Textures/Effects/SunFlaresRed.tga
#		data/Textures/Effects/SunFlaresRedOrange.tga
#		data/Textures/Effects/SunFlaresYellow.tga
#		data/Textures/Effects/SunFlaresBlue.tga
#		data/Textures/Effects/SunFlaresWhite.tga

	# Add a sun, far far away
	pSun = App.Sun_Create(3000.0, 3000, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()
	
	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)


	# Create our static stations and such
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        pGessiks	= loadspacehelper.CreateShip("CardStarbase", pSet, "Gessiks Castle", "CSB Location")
	        if (pGessiks != None):
		        import GessiksAI
		        pGessiks.SetAI(GessiksAI.CreateAI(pGessiks))

	        pHulk1		= loadspacehelper.CreateShip("Galaxy", pSet, "Galactica", "wreck1")
	        pHulk2		= loadspacehelper.CreateShip("Nebula", pSet, "Rodger Young", "wreck2")
	        pHulk3		= loadspacehelper.CreateShip("Ambassador", pSet, "Joshua Norton", "wreck3")
	        pHulk5		= loadspacehelper.CreateShip("Warbird", pSet, "Golden Apple", "wreck5")
	        pHulk6		= loadspacehelper.CreateShip("Marauder", pSet, "Marie Celeste", "wreck6")
	        pHulk8		= loadspacehelper.CreateShip("KessokHeavy", pSet, "Nosferatu", "wreck8")
	        pHulk10		= loadspacehelper.CreateShip("Nebula", pSet, "Lusitania", "wreck10")
	        pHulk11		= loadspacehelper.CreateShip("CardFreighter", pSet, "Heart of Gold", "wreck11")
	        pHulk12		= loadspacehelper.CreateShip("Ambassador", pSet, "Enterpoop", "wreck12")
	        pHulk13		= loadspacehelper.CreateShip("Vorcha", pSet, "SunStrider", "wreck13")
	        pHulk14		= loadspacehelper.CreateShip("Keldon", pSet, "Titanic", "wreck14")
	
	        DamageWrecks(pHulk1, pHulk2, pHulk3, pHulk5, pHulk6, pHulk8, pHulk10, pHulk11, pHulk12, pHulk13, pHulk14)
		
def DamageWrecks(pHulk1, pHulk2, pHulk3, pHulk5, pHulk6, pHulk8, pHulk10, pHulk11, pHulk12, pHulk13, pHulk14):
	
	# Import our damaged script ship and apply it to the Hulk1
	import Hulk3Damaged
	Hulk3Damaged.AddDamage(pHulk1)
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
	pHulk1.DamageSystem(pHulk1.GetHull(), 5000)
	pHulk1.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk1)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk1, 7)
	
	# Import our damaged script ship and apply it to the Hulk2
	import Hulk3Damaged
	Hulk3Damaged.AddDamage(pHulk2)
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
	import Hulk3Damaged
	Hulk3Damaged.AddDamage(pHulk3)
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
	MissionLib.SetRandomRotation(pHulk3, 15)
	
	# Import our damaged script ship and apply it to the Hulk5
	import DamageWarbird1
	DamageWarbird1.AddDamage(pHulk5)
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
	MissionLib.SetRandomRotation(pHulk5, 12)
		
	# Import our damaged script ship and apply it to the Hulk6
	import Hulk2Damaged
	Hulk2Damaged.AddDamage(pHulk6)
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
	MissionLib.SetRandomRotation(pHulk6, 15)

	# Import our damaged script ship and apply it to the Hulk8
	import Hulk2Damaged
	Hulk2Damaged.AddDamage(pHulk8)
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
	pHulk8.DamageSystem(pHulk8.GetHull(), 3000)
	pHulk8.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk8)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk8, 10)
		
	# Import our damaged script ship and apply it to the pHulk10
	import Hulk3Damaged
	Hulk3Damaged.AddDamage(pHulk10)
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
	MissionLib.SetRandomRotation(pHulk10, 15)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk10, 7)
	
	# Import our damaged script ship and apply it to the pHulk11
	import Hulk2Damaged
	Hulk2Damaged.AddDamage(pHulk11)
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
	pHulk11.DamageSystem(pHulk11.GetHull(), 3000)
	pHulk11.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk11)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk11, 10)
		
	# Import our damaged script ship and apply it to the pHulk12
	import Hulk3Damaged
	Hulk3Damaged.AddDamage(pHulk12)
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
	MissionLib.SetRandomRotation(pHulk12, 5)
	
	# Import our damaged script ship and apply it to the pHulk13
	import Hulk2Damaged
	Hulk2Damaged.AddDamage(pHulk13)
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
	MissionLib.SetRandomRotation(pHulk13, 10)
		
	# Import our damaged script ship and apply it to the pHulk14
	import Hulk1Damaged
	Hulk1Damaged.AddDamage(pHulk14)
	# Turn off the ships repair
	pRepair = pHulk14.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the pHulk14...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk14)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk14.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk14.DamageSystem(pHulk14.GetHull(), 4500)
	pHulk14.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk14)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk14, 8)
