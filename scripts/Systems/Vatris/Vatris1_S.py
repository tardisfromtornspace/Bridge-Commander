import App
import Tactical.LensFlares

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(5000.0, 5000, 6000, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	pPlanet = App.Planet_Create(185.0, "data/models/environment/TanPlanet2.nif")
	pSet.AddObjectToSet(pPlanet, "Vatris 1")

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/TanPlanet2.NIF", "Class K")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass	
	
	pMoon1 = App.Planet_Create(110.0, "data/models/environment/GrayPlanet.nif")
	pSet.AddObjectToSet(pMoon1, "Vatris 1 Moon 1")
	
	pMoon1.PlaceObjectByName("Moon1 Location")
	pMoon1.UpdateNodeOnly()

	pMoon1 = App.Planet_Create(75.0, "data/models/environment/moon.nif")
	pSet.AddObjectToSet(pMoon1, "Vatris 1 Moon 2")
	
	pMoon1.PlaceObjectByName("Moon2 Location")
	pMoon1.UpdateNodeOnly()

	pMoon1 = App.Planet_Create(140.0, "data/models/environment/PurplePlanet.nif")
	pSet.AddObjectToSet(pMoon1, "Vatris 1 Moon 3")
	
	pMoon1.PlaceObjectByName("Moon3 Location")
	pMoon1.UpdateNodeOnly()
