import App
import Tactical.LensFlares

def Initialize(pSet):
	pSun = App.Sun_Create(300.0, 400, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Blue Star")

	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	pSun2 = App.Sun_Create(1100.0, 2000, 2500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun2, "Red Star")
	
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 2
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun2)

	pPR1 = App.Planet_Create(100.0, "data/models/environment/PoisonPlanet.nif")
	pSet.AddObjectToSet(pPR1, "Procyon 1")

	pPR1.PlaceObjectByName("Planet Location")
	pPR1.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPR1, "data/models/environment/PoisonPlanet.NIF", "Class-D")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass 	
	
	pMoon1 = App.Planet_Create(25.0, "data/models/environment/Titan.nif")
	pSet.AddObjectToSet(pMoon1, "Moon 1")

	pMoon1.PlaceObjectByName("Moon1 Location")
	pMoon1.UpdateNodeOnly()

	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon1, "data/models/environment/Titan.nif", "Class-K")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	
	
	pMoon2 = App.Planet_Create(35.0, "data/models/environment/SulphuricPlanetZM1.NIF")
	pSet.AddObjectToSet(pMoon2, "Moon 2")

	pMoon2.PlaceObjectByName("Moon2 Location")
	pMoon2.UpdateNodeOnly()
	
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
	pNebula.AddNebulaSphere(9800.0, 4945.0, -3600.0,  5000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
