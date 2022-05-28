import App
import Tactical.LensFlares

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(7000.0, 7500, 8000, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRedOrange.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	# Add a sun, far far away
	pSun2 = App.Sun_Create(9000.0, 10200, 15000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")

	Tactical.LensFlares.BlueLensFlare(pSet, pSun2)
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	pJ25 = App.Planet_Create(285.0, "data/models/environment/LeadPlanet.NIF")
	pSet.AddObjectToSet(pJ25, "J25 1")

	pJ25.PlaceObjectByName("Planet Location")
	pJ25.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pJ25, "data/models/environment/LeadPlanet.NIF", "Class K")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)

	pNebula = App.MetaNebula_Create(245.0 / 155.0, 90.0 / 155.0, 105.0 / 105.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.5, 3.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3500.0 in this case)
	pNebula.AddNebulaSphere(20800.0, 5000.0, 250.0, 3500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)

	pNebula = App.MetaNebula_Create(245.0 / 155.0, 90.0 / 155.0, 105.0 / 105.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.5, 3.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3500.0 in this case)
	pNebula.AddNebulaSphere(21800.0, 7000.0, 250.0, 3500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula2")

	pNebula = App.MetaNebula_Create(245.0 / 155.0, 90.0 / 155.0, 105.0 / 105.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.5, 3.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3500.0 in this case)
	pNebula.AddNebulaSphere(24800.0, 8000.0, 250.0, 3500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula3")

	pNebula = App.MetaNebula_Create(245.0 / 155.0, 90.0 / 155.0, 105.0 / 105.0, 145.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(0.5, 3.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3500.0 in this case)
	pNebula.AddNebulaSphere(18800.0, 4000.0, 500.0, 3500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula4")
