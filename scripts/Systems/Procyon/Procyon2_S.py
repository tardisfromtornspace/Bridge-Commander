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

	pPR2 = App.Planet_Create(100.0, "data/models/environment/BlueGasPlanet.NIF")
	pSet.AddObjectToSet(pPR2, "Procyon 2")

	pPR2.PlaceObjectByName("Planet Location")
	pPR2.UpdateNodeOnly()
	
	try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPR2, "data/models/environment/BlueGasPlanet.NIF", "Blue Gas")        
	except ImportError:
		# Couldn't find NanoFx2.  That's ok.  Do nothing...
	        pass 	
	
	pMoon1 = App.Planet_Create(25.0, "data/models/environment/Io.nif")
	pSet.AddObjectToSet(pMoon1, "Moon 1")

	pMoon1.PlaceObjectByName("Moon1 Location")
	pMoon1.UpdateNodeOnly()
	
	pMoon2 = App.Planet_Create(35.0, "data/models/environment/SulphuricPlanetZM1.NIF")
	pSet.AddObjectToSet(pMoon2, "Moon 2")

	pMoon2.PlaceObjectByName("Moon2 Location")
	pMoon2.UpdateNodeOnly()
	
	pMoon3 = App.Planet_Create(20.0, "data/models/environment/Dione.NIF")
	pSet.AddObjectToSet(pMoon3, "Moon 3")

	pMoon3.PlaceObjectByName("Moon3 Location")
	pMoon3.UpdateNodeOnly()
	
	pMoon4 = App.Planet_Create(35.0, "data/models/environment/Callisto.NIF")
	pSet.AddObjectToSet(pMoon4, "Moon 4")

	pMoon4.PlaceObjectByName("Moon4 Location")
	pMoon4.UpdateNodeOnly()
	
	pMoon5 = App.Planet_Create(65.0, "data/models/environment/RedPlanet.NIF")
	pSet.AddObjectToSet(pMoon5, "Moon 5")

	pMoon5.PlaceObjectByName("Moon5 Location")
	pMoon5.UpdateNodeOnly()
	
	pMoon6 = App.Planet_Create(10.0, "data/models/environment/Mercury.NIF")
	pSet.AddObjectToSet(pMoon6, "Moon 6")

	pMoon6.PlaceObjectByName("Moon6 Location")
	pMoon6.UpdateNodeOnly()
