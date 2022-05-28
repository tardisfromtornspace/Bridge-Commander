import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun 1
	pSun = App.Sun_Create(8000.00, 8150.0, 8200.0, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")

	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	# Sun2
	pSun2 = App.Sun_Create(2400.0, 2450, 2500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	pArc4 = App.Planet_Create(44675.0, "data/models/environment/SClass1.NIF")
	pSet.AddObjectToSet(pArc4, "Arcturus 4")

	pArc4.PlaceObjectByName("Planet Location")
	pArc4.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pArc4, "data/models/environment/SClass1.NIF", "Class-S")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass    
