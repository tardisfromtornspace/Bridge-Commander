import App
import Tactical.LensFlares

def Initialize(pSet):
	# Add a sun, far far away
	pSun = App.Sun_Create(2000.0, 2000, 6000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	pPlanet = App.Planet_Create(115.0, "data/models/environment/BlackPlanet.NIF")
	pSet.AddObjectToSet(pPlanet, "Vatris 2")

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/BlackPlanet.NIF", "Black")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	
	
	pMoon1 = App.Planet_Create(30.0, "data/models/environment/PoisonPlanet.NIF")
	pSet.AddObjectToSet(pMoon1, "Moon 1")
	
	pMoon1.PlaceObjectByName("Moon1 Location")
	pMoon1.UpdateNodeOnly()
	
	pMoon2 = App.Planet_Create(25.0, "data/models/environment/GrayPlanet.nif")
	pSet.AddObjectToSet(pMoon2, "Moon 2")

	pMoon2.PlaceObjectByName("Moon2 Location")
	pMoon2.UpdateNodeOnly()