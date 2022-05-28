###############################################################################
#	Filename:	Nursery1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Nursery 1 static objects.  Called by Nursery1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	03/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(4.0, 30, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Protostar 1")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Add a sun, far far away
	pSun2 = App.Sun_Create(6.0, 12, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun2, "Protostar 2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Add a sun, far far away
	pSun3 = App.Sun_Create(8.0, 25, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun3, "Protostar 3")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Add a sun, far far away
	pSun4 = App.Sun_Create(3.0, 10, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun4, "Protostar 4")
	
	# Place the object at the specified location.
	pSun4.PlaceObjectByName( "Sun4" )
	pSun4.UpdateNodeOnly()

	# Add a sun, far far away
	pSun5 = App.Sun_Create(3.0, 15, 500, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresOrange.tga")
	pSet.AddObjectToSet(pSun5, "Protostar 5")
	
	# Place the object at the specified location.
	pSun5.PlaceObjectByName( "Sun5" )
	pSun5.UpdateNodeOnly()

	# Add a sun, far far away
	pSun6 = App.Sun_Create(20.0, 400, 500, "data/Textures/SunGreen.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun6, "Protostar 6")
	
	# Place the object at the specified location.
	pSun6.PlaceObjectByName( "Sun6" )
	pSun6.UpdateNodeOnly()

	# Add a sun, far far away
	pSun7 = App.Sun_Create(7.0, 25, 500, "data/Textures/SunBrown.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun7, "Protostar 7")
	
	# Place the object at the specified location.
	pSun7.PlaceObjectByName( "Sun7" )
	pSun7.UpdateNodeOnly()

	# Add a sun, far far away
	pSun8 = App.Sun_Create(5.0, 1250, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun8, "Protostar 8")
	
	# Place the object at the specified location.
	pSun8.PlaceObjectByName( "Sun8" )
	pSun8.UpdateNodeOnly()



	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
    # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(190.0 / 255.0, 40.0 / 255.0, 35.0  / 255.0, 250.0, 10.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(1.0, 5.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(100, 10000, 500.0,  2500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(190.0 / 255.0, 40.0 / 255.0, 35.0  / 255.0, 250.0, 10.5, "data/Backgrounds/nebulaoverlayred.tga", "data/Backgrounds/nebulaexternalred.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(0.0, 5.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(-500, 10000.0, -2500.0, 4000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")
	
	pNebula4 = App.MetaNebula_Create(190.0 / 255.0, 40.0 / 255.0, 35.0  / 255.0, 150.0, 10.5, "data/Backgrounds/nebulaoverlaybz1.tga", "data/Backgrounds/nebulaexternalbz1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula4.SetupDamage(50.0, 250.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula4.AddNebulaSphere(-1000.0, 12000.0, -1000.0, 800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula4, "Nebula4")
	
	pNebula5 = App.MetaNebula_Create(190.0 / 255.0, 40.0 / 255.0, 35.0  / 255.0, 10.0, 10.5, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula5.SetupDamage(250.0, 280.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula5.AddNebulaSphere(-100.0, 11000.0, -1500.0, 250.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula5, "Nebula5")
	
	