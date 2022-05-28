###############################################################################
#	Filename:	TheGalaxy1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates TheGalaxy1 static objects.  Called by TranswarpHub.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	09/25/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

	pSun = App.Sun_Create(1430.0, 1200, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Star")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Star" )
	pSun.UpdateNodeOnly()

	# Add a sun, far far away
	pSunq = App.Sun_Create(1424.0, 1200, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSunq, "Power Tap")

	# Place the object at the specified location.
	pSunq.PlaceObjectByName( "Sunq" )
	pSunq.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2 = App.Sun_Create(925.0, 1200, 500, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Add a sun, far far away
	pSun3 = App.Sun_Create(780.0, 950, 500, "data/Textures/SunGreen.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun3, "Sun3")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Add a sun, far far away
	pSun4 = App.Sun_Create(860.0, 500, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun4, "Sun4")
	
	# Place the object at the specified location.
	pSun4.PlaceObjectByName( "Sun4" )
	pSun4.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5 = App.Sun_Create(730.0, 650, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun5, "Sun5")
	
	# Place the object at the specified location.
	pSun5.PlaceObjectByName( "Sun5" )
	pSun5.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6 = App.Sun_Create(900.0, 400, 500, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun6, "Sun6")
	
	# Place the object at the specified location.
	pSun6.PlaceObjectByName( "Sun6" )
	pSun6.UpdateNodeOnly()

	# Add a sun, far far away
	pSun7 = App.Sun_Create(670.0, 950, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun7, "Sun7")
	
	# Place the object at the specified location.
	pSun7.PlaceObjectByName( "Sun7" )
	pSun7.UpdateNodeOnly()

	# Add a sun, far far away
	pSun8 = App.Sun_Create(750.0, 1250, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun8, "Sun8")
	
	# Place the object at the specified location.
	pSun8.PlaceObjectByName( "Sun8" )
	pSun8.UpdateNodeOnly()

	# Add a sun, far far away
	pSun9 = App.Sun_Create(670.0, 550, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun9, "Sun9")
	
	# Place the object at the specified location.
	pSun9.PlaceObjectByName( "Sun9" )
	pSun9.UpdateNodeOnly()

	# Add a sun, far far away
	pSun10 = App.Sun_Create(350.0, 1250, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun10, "Sun10")
	
	# Place the object at the specified location.
	pSun10.PlaceObjectByName( "Sun10" )
	pSun10.UpdateNodeOnly()

	# Add a sun, far far away
	pSun11 = App.Sun_Create(1050.0, 1250, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresRedOrange.tga")
	pSet.AddObjectToSet(pSun11, "Sun11")
	
	# Place the object at the specified location.
	pSun11.PlaceObjectByName( "Sun11" )
	pSun11.UpdateNodeOnly()

	# Add a sun, far far away
	pSun12 = App.Sun_Create(1050.0, 1250, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun12, "Sun12")
	
	# Place the object at the specified location.
	pSun12.PlaceObjectByName( "Sun12" )
	pSun12.UpdateNodeOnly()

	# Add a sun, far far away
	pSun13 = App.Sun_Create(1450.0, 2250, 500, "data/Textures/SunCyan.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun13, "Sun13")
	
	# Place the object at the specified location.
	pSun13.PlaceObjectByName( "Sun13" )
	pSun13.UpdateNodeOnly()

	# Add a sun, far far away
	pSun14 = App.Sun_Create(2050.0, 1250, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun14, "Sun14")
	
	# Place the object at the specified location.
	pSun14.PlaceObjectByName( "Sun14" )
	pSun14.UpdateNodeOnly()

	# Add a sun, far far away
	pSun15 = App.Sun_Create(1050.0, 1250, 500, "data/Textures/SunGreen.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun15, "Sun15")
	
	# Place the object at the specified location.
	pSun15.PlaceObjectByName( "Sun15" )
	pSun15.UpdateNodeOnly()

	# Add a sun, far far away
	pSun16 = App.Sun_Create(1750.0, 3250, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun16, "Sun16")
	
	# Place the object at the specified location.
	pSun16.PlaceObjectByName( "Sun16" )
	pSun16.UpdateNodeOnly()

        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return

	# Create our static stations and such
	pHub10	= loadspacehelper.CreateShip("CardStarbase", pSet, "Long Range Sensors", "Inner1")
	if (pHub10 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub10)
	
	# Create our static stations and such
	pHub11	= loadspacehelper.CreateShip("CardStation", pSet, "Distribution Node 1", "Inner2")
	if (pHub11 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub11)
	
	# Create our static stations and such
	pHub12	= loadspacehelper.CreateShip("CardStation", pSet, "Distribution Node 2", "Inner3")
	if (pHub12 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub12)
	
	# Create our static stations and such
	pHub13	= loadspacehelper.CreateShip("CardStation", pSet, "Distribution Node 3", "Inner4")
	if (pHub13 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub13)
	
	# Create our static stations and such
	pHub14	= loadspacehelper.CreateShip("CardStarbase", pSet, "Matter Coversion Interface", "Inner5")
	if (pHub14 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub14)
	
	# Create our static stations and such
	pHub15	= loadspacehelper.CreateShip("CardStarbase", pSet, "Transwarp Control 2", "Inner6")
	if (pHub15 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub15)

	# Create our static stations and such
	pHub9	= loadspacehelper.CreateShip("FedStarbase", pSet, "Fusion Tap 1", "Center1")
	if (pHub9 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub9)
	
	# Create our static stations and such
	pHub16	= loadspacehelper.CreateShip("FedStarbase", pSet, "Fusion Tap 2", "Center2")
	if (pHub16 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub16)
	
	# Create our static stations and such
	pHub17	= loadspacehelper.CreateShip("FedStarbase", pSet, "Fusion Tap 3", "Center3")
	if (pHub17 != None):
		# Turn off the ships repair
		MissionLib.HideSubsystems(pHub17)
