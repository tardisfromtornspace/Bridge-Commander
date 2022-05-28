import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun1
	pSun = App.Sun_Create(62500.0, 62600, 10000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	# Sun2
	pSun2 = App.Sun_Create(9000.0, 9500, 10000, "data/Textures/SunBlack.tga", "data/Textures/Effects/SunFlaresBlack.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

        # Builds a Black lens flare for this Sun
	Tactical.LensFlares.BlueGlareBright(pSet, pSun2)

	# Sun3
	pSun3 = App.Sun_Create(32500.0, 32600, 10000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun3, "Sun3")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 3
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun3)

	pPlanet = App.Planet_Create(68.0, "data/models/environment/Moon.NIF")
	pSet.AddObjectToSet(pPlanet, "Kavis Alpha 1 (Class D)")

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/Moon.NIF", "Class-D")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass 	

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 9000.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(200.0, 15.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(-38500.0, -150000.0, 4000.0,  20000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula")

	pNebula1 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 9000.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula1.SetupDamage(200.0, 15.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula1.AddNebulaSphere(-43500.0, -150000.0, 4000.0,  20000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula1, "Nebula1")

	pNebula2 = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 255.0, 9000.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(200.0, 15.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(-47500.0, -150000.0, 4000.0,  20000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")