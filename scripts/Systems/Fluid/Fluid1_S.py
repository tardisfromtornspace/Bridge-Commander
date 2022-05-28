###############################################################################
#	Filename:	Fluid1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Fluid 1 static objects.  Called by Fluid1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	04/05/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import Tactical.LensFlares
import MissionLib

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(600.0, 900, 100, "data/Textures/SunPurple.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Oceanus")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)
	
	# Add a sun, far far away
	pSun2 = App.Sun_Create(1600.0, 900, 100, "data/Textures/SunCyan.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Aquarius")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Add a sun, far far away
	pSun3 = App.Sun_Create(3600.0, 2900, 100, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun3, "Poseidon")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
    	# name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(140.0 / 255.0, 240.0 / 255.0, 65.0  / 255.0, 6800.0, 0.0, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(1000.0, 6000.0, 3000.0, 7800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(40.0 / 255.0, 240.0 / 255.0, 165.0  / 255.0, 6800.0, 0.0, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(3500.0, -7800.0, -2000.0, 7800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")
	
	pNebula3 = App.MetaNebula_Create(40.0 / 255.0, 140.0 / 255.0, 45.0  / 255.0, 6800.0, 0.0, "data/Backgrounds/nebulaoverlaybz2.tga", "data/Backgrounds/nebulaexternalbz2.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula3.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula3.AddNebulaSphere(-6500.0, -4800.0, 0.0, 7800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")
