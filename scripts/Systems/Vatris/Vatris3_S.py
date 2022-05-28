import App
import Tactical.LensFlares

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(1500.0, 1500, 6000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")

	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	pVatris3 = App.Planet_Create(410.17, "data/models/environment/RingPlanetZM2.NIF")
	pSet.AddObjectToSet(pVatris3, "Vatris3")

	# Place the object at the specified location.
	pVatris3.PlaceObjectByName( "Vatris3" )
	pVatris3.SetAtmosphereRadius(0.1)
	pVatris3.UpdateNodeOnly()

	pKatraul = App.Planet_Create(54.29, "data/models/environment/SulphuricPlanetZM1.NIF")
	pSet.AddObjectToSet(pKatraul, "Katraul")

	# Place the object at the specified location.
	pKatraul.PlaceObjectByName( "Katraul" )
	pKatraul.SetAtmosphereRadius(0.01)
	pKatraul.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pKatraul, "data/models/environment/SulphuricPlanetZM1.NIF", "Class D")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)

	pNebula = App.MetaNebula_Create(0.0 / 105.0, 90.0 / 255.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/anomaly1.tga", "data/Backgrounds/anomaly1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(10.0, 100.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (2000.0 in this case)
	pNebula.AddNebulaSphere(4800.0, 5945.0, -9600.0,  2000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")

	pNebula = App.MetaNebula_Create(0.0 / 105.0, 90.0 / 255.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/anomaly1.tga", "data/Backgrounds/anomaly1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(10.0, 100.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3000.0 in this case)
	pNebula.AddNebulaSphere(4600.0, 5945.0, -9200.0,  3000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula2")

	pNebula = App.MetaNebula_Create(0.0 / 105.0, 90.0 / 255.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/anomaly1.tga", "data/Backgrounds/anomaly1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(10.0, 100.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3000.0 in this case)
	pNebula.AddNebulaSphere(4700.0, 5545.0, -9600.0,  3000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula3")

	pNebula = App.MetaNebula_Create(0.0 / 105.0, 90.0 / 255.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/anomaly1.tga", "data/Backgrounds/anomaly1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(10.0, 100.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (2000.0 in this case)
	pNebula.AddNebulaSphere(5100.0, 5445.0, -9900.0,  2000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula4")



