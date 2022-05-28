import App
import Tactical.LensFlares

def Initialize(pSet):

        # Add a sun, far far away
        pSun = App.Sun_Create(1000.0, 1200, 1450, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")
        
        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.YellowLensFlare(pSet, pSun)

        pAlecrea = App.Planet_Create(70.0, "data/models/environment/MClass1.NIF")
        pSet.AddObjectToSet(pAlecrea, "Alecrea")        

        pAlecrea.PlaceObjectByName("Planet Location")
        pAlecrea.UpdateNodeOnly()
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pAlecrea, "data/models/environment/MClass1.NIF", "Class-M")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass    

        pMoon1 = App.Planet_Create(32.0, "data/models/environment/YClass1.NIF")
        pSet.AddObjectToSet(pMoon1, "Moon 1, Demon")

        pMoon1.PlaceObjectByName("Moon1 Location")
        pMoon1.UpdateNodeOnly()
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMoon1, "data/models/environment/YClass1.NIF", "Y-Class")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass    
        
        pCaulth = App.Planet_Create(79.0, "data/models/environment/MClass3.NIF")
        pSet.AddObjectToSet(pCaulth, "Caulth")

        pCaulth.PlaceObjectByName("Planet2 Location")
        pCaulth.UpdateNodeOnly()
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCaulth, "data/models/environment/MClass3.NIF", "Class-M")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass    
        
        pMoon2 = App.Planet_Create(27.0, "data/models/environment/PClass1.NIF")
        pSet.AddObjectToSet(pMoon2, "Class P Moon")

        pMoon2.PlaceObjectByName("Moon2 Location")
        pMoon2.UpdateNodeOnly()
