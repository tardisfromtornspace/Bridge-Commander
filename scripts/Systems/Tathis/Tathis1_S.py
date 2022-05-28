from bcdebug import debug
import App
import loadspacehelper
import Tactical.LensFlares

def Initialize(pSet):

        # Sun1
	debug(__name__ + ", Initialize")
	pSun = App.Sun_Create(6000.0, 6500, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.BlueGlareBright(pSet, pSun)

        # Sun2
	pSun2 = App.Sun_Create(600.0, 650, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 2
	Tactical.LensFlares.BlueLensFlare(pSet, pSun2)

	pTathis1 = App.Planet_Create(100.0, "data/models/environment/LuminousPlanetZM.NIF")
	pSet.AddObjectToSet(pTathis1, "Tathis 1")

	pTathis1.PlaceObjectByName("Planet")
	pTathis1.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTathis1, "data/models/environment/LuminousPlanetZM.NIF", "Luminious")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	

	# Model and placement for Moon 1
	pTathis1 = App.Planet_Create(25.0, "data/models/environment/moon.nif")
	pSet.AddObjectToSet(pTathis1, "Moon 1")

	#Place the object at the specified location.
	pTathis1.PlaceObjectByName("Moon1")
	pTathis1.UpdateNodeOnly()
	
	# Create the station here so we don't have to worry about it
	# when it appears in later missions
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        loadspacehelper.CreateShip("SpaceFacility", pSet, "Federation Research Station", "Station Location")

#Nebula info reads (R,G,B, Vision-distance, Sensor interference, "neblua texture", "nebula external texture")

	# Center Neb Placement
	pNebula1 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 5000.0, 2500.0, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula1.SetupDamage(2500.0, 500.0)

	pNebula1.AddNebulaSphere(0.0, -225500, 0.0, 16500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula1, "Nebula1")
