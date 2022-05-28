import App
import Tactical.LensFlares

def Initialize(pSet):
	pSun = App.Sun_Create(800.0, 850, 950, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Blue Star")

	pSun.PlaceObjectByName( "Sun1" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare, attached to the sun
	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	pSun2 = App.Sun_Create(4000.0, 5000, 5600, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun2, "Red Star1")
	
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 2
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun2)

	pSun3 = App.Sun_Create(1500.0, 1700, 2000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun3, "Red Star2")
	
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 3
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun3)
	
	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.4, 4.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(9800.0, 945.0, -3600.0,  5000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(0.4, 4.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(10000.0, 1945.0, -1600.0,  5000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")
	
	pNebula3 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula3.SetupDamage(0.4, 4.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula3.AddNebulaSphere(9500.0, 2945.0, -4600.0,  5000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")
	
