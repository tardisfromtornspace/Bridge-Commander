import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
    from Custom.DS9FX.DS9FXObjects import CardassiaShips
    CardassiaShips.CardassiaSetShips()

    pSun = App.Sun_Create(4500.0, 4500.0, 4500.0, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
    pSet.AddObjectToSet(pSun, "Cardassia Sun")

    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()

    Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun, 1, 0.55, 0.55)
    SunStreak.Create(pSet, "SunStr", 50000.0, "RedOrange", "8")

    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.CardassiaMapPlanetDetail == 3:
        if DS9FXSavedConfig.CardassiaPlanets == 1:
            pCardassia1 = App.Planet_Create(60.0, "data/models/environment/DS9FX/HighRes/Cardassia1.nif")
            pSet.AddObjectToSet(pCardassia1, "Cardassia 1")

            pCardassia1.PlaceObjectByName( "Cardassia 1" )
            pCardassia1.UpdateNodeOnly()

            pCardassia2 = App.Planet_Create(100.0, "data/models/environment/DS9FX/HighRes/Cardassia2.nif")
            pSet.AddObjectToSet(pCardassia2, "Cardassia 2")

            pCardassia2.PlaceObjectByName( "Cardassia 2" )
            pCardassia2.UpdateNodeOnly()

            pCardassia3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/HighRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia3, "Cardassia 3")

            pCardassia3.PlaceObjectByName( "Cardassia 3" )
            pCardassia3.UpdateNodeOnly()

            pCardassia4 = App.Planet_Create(100.0, "data/models/environment/DS9FX/HighRes/Cardassia6.nif")
            pSet.AddObjectToSet(pCardassia4, "Cardassia 4")

            pCardassia4.PlaceObjectByName( "Cardassia 4" )
            pCardassia4.UpdateNodeOnly()

            pCardassia5 = App.Planet_Create(110.0, "data/models/environment/DS9FX/HighRes/Cardassia5.nif")
            pSet.AddObjectToSet(pCardassia5, "Cardassia 5")

            pCardassia5.PlaceObjectByName( "Cardassia 5" )
            pCardassia5.UpdateNodeOnly()

            pCardassia6 = App.Planet_Create(75.0, "data/models/environment/DS9FX/HighRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia6, "Cardassia Prime")

            pCardassia6.PlaceObjectByName( "Cardassia 6" )
            pCardassia6.UpdateNodeOnly()

            pCardassia7 = App.Planet_Create(95.0, "data/models/environment/DS9FX/HighRes/Cardassia7.nif")
            pSet.AddObjectToSet(pCardassia7, "Cardassia 7")

            pCardassia7.PlaceObjectByName( "Cardassia 7" )
            pCardassia7.UpdateNodeOnly()

            pCardassia8 = App.Planet_Create(200.0, "data/models/environment/DS9FX/HighRes/Cardassia8.nif")
            pSet.AddObjectToSet(pCardassia8, "Cardassia 8")

            pCardassia8.PlaceObjectByName( "Cardassia 8" )
            pCardassia8.UpdateNodeOnly()

            if DS9FXSavedConfig.CardassiaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia1, "data/Models/Environment/DS9FX/HighRes/Cardassia1.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia2, "data/Models/Environment/DS9FX/HighRes/Cardassia2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia3, "data/Models/Environment/DS9FX/HighRes/Cardassia6.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia4, "data/Models/Environment/DS9FX/HighRes/Cardassia4.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia5, "data/Models/Environment/DS9FX/HighRes/Cardassia5.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia6, "data/Models/Environment/DS9FX/HighRes/Cardassia3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia7, "data/Models/Environment/DS9FX/HighRes/Cardassia7.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia8, "data/Models/Environment/DS9FX/HighRes/Cardassia8.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"        

    elif DS9FXSavedConfig.CardassiaMapPlanetDetail == 2:
        if DS9FXSavedConfig.CardassiaPlanets == 1:
            pCardassia1 = App.Planet_Create(60.0, "data/models/environment/DS9FX/StandardRes/Cardassia1.nif")
            pSet.AddObjectToSet(pCardassia1, "Cardassia 1")

            pCardassia1.PlaceObjectByName( "Cardassia 1" )
            pCardassia1.UpdateNodeOnly()

            pCardassia2 = App.Planet_Create(100.0, "data/models/environment/DS9FX/StandardRes/Cardassia2.nif")
            pSet.AddObjectToSet(pCardassia2, "Cardassia 2")

            pCardassia2.PlaceObjectByName( "Cardassia 2" )
            pCardassia2.UpdateNodeOnly()

            pCardassia3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/StandardRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia3, "Cardassia 3")

            pCardassia3.PlaceObjectByName( "Cardassia 3" )
            pCardassia3.UpdateNodeOnly()

            pCardassia4 = App.Planet_Create(100.0, "data/models/environment/DS9FX/StandardRes/Cardassia6.nif")
            pSet.AddObjectToSet(pCardassia4, "Cardassia 4")

            pCardassia4.PlaceObjectByName( "Cardassia 4" )
            pCardassia4.UpdateNodeOnly()

            pCardassia5 = App.Planet_Create(110.0, "data/models/environment/DS9FX/StandardRes/Cardassia5.nif")
            pSet.AddObjectToSet(pCardassia5, "Cardassia 5")

            pCardassia5.PlaceObjectByName( "Cardassia 5" )
            pCardassia5.UpdateNodeOnly()

            pCardassia6 = App.Planet_Create(75.0, "data/models/environment/DS9FX/StandardRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia6, "Cardassia Prime")

            pCardassia6.PlaceObjectByName( "Cardassia 6" )
            pCardassia6.UpdateNodeOnly()

            pCardassia7 = App.Planet_Create(95.0, "data/models/environment/DS9FX/StandardRes/Cardassia7.nif")
            pSet.AddObjectToSet(pCardassia7, "Cardassia 7")

            pCardassia7.PlaceObjectByName( "Cardassia 7" )
            pCardassia7.UpdateNodeOnly()

            pCardassia8 = App.Planet_Create(200.0, "data/models/environment/DS9FX/StandardRes/Cardassia8.nif")
            pSet.AddObjectToSet(pCardassia8, "Cardassia 8")

            pCardassia8.PlaceObjectByName( "Cardassia 8" )
            pCardassia8.UpdateNodeOnly()

            if DS9FXSavedConfig.CardassiaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia1, "data/Models/Environment/DS9FX/StandardRes/Cardassia1.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia2, "data/Models/Environment/DS9FX/StandardRes/Cardassia2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia3, "data/Models/Environment/DS9FX/StandardRes/Cardassia6.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia4, "data/Models/Environment/DS9FX/StandardRes/Cardassia4.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia5, "data/Models/Environment/DS9FX/StandardRes/Cardassia5.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia6, "data/Models/Environment/DS9FX/StandardRes/Cardassia3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia7, "data/Models/Environment/DS9FX/StandardRes/Cardassia7.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia8, "data/Models/Environment/DS9FX/StandardRes/Cardassia8.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 
                    
    elif DS9FXSavedConfig.CardassiaMapPlanetDetail == 1:
        if DS9FXSavedConfig.CardassiaPlanets == 1:
            pCardassia1 = App.Planet_Create(60.0, "data/models/environment/DS9FX/StandardRes/Cardassia1.nif")
            pSet.AddObjectToSet(pCardassia1, "Cardassia 1")

            pCardassia1.PlaceObjectByName( "Cardassia 1" )
            pCardassia1.UpdateNodeOnly()

            pCardassia2 = App.Planet_Create(100.0, "data/models/environment/DS9FX/StandardRes/Cardassia2.nif")
            pSet.AddObjectToSet(pCardassia2, "Cardassia 2")

            pCardassia2.PlaceObjectByName( "Cardassia 2" )
            pCardassia2.UpdateNodeOnly()

            pCardassia3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/StandardRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia3, "Cardassia 3")

            pCardassia3.PlaceObjectByName( "Cardassia 3" )
            pCardassia3.UpdateNodeOnly()

            pCardassia4 = App.Planet_Create(100.0, "data/models/environment/DS9FX/StandardRes/Cardassia6.nif")
            pSet.AddObjectToSet(pCardassia4, "Cardassia 4")

            pCardassia4.PlaceObjectByName( "Cardassia 4" )
            pCardassia4.UpdateNodeOnly()

            pCardassia5 = App.Planet_Create(110.0, "data/models/environment/DS9FX/StandardRes/Cardassia5.nif")
            pSet.AddObjectToSet(pCardassia5, "Cardassia 5")

            pCardassia5.PlaceObjectByName( "Cardassia 5" )
            pCardassia5.UpdateNodeOnly()

            pCardassia6 = App.Planet_Create(75.0, "data/models/environment/DS9FX/StandardRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia6, "Cardassia Prime")

            pCardassia6.PlaceObjectByName( "Cardassia 6" )
            pCardassia6.UpdateNodeOnly()

            pCardassia7 = App.Planet_Create(95.0, "data/models/environment/DS9FX/StandardRes/Cardassia7.nif")
            pSet.AddObjectToSet(pCardassia7, "Cardassia 7")

            pCardassia7.PlaceObjectByName( "Cardassia 7" )
            pCardassia7.UpdateNodeOnly()

            pCardassia8 = App.Planet_Create(200.0, "data/models/environment/DS9FX/StandardRes/Cardassia8.nif")
            pSet.AddObjectToSet(pCardassia8, "Cardassia 8")

            pCardassia8.PlaceObjectByName( "Cardassia 8" )
            pCardassia8.UpdateNodeOnly()

            if DS9FXSavedConfig.CardassiaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia1, "data/Models/Environment/DS9FX/StandardRes/Cardassia1.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia2, "data/Models/Environment/DS9FX/StandardRes/Cardassia2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia3, "data/Models/Environment/DS9FX/StandardRes/Cardassia6.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia4, "data/Models/Environment/DS9FX/StandardRes/Cardassia4.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia5, "data/Models/Environment/DS9FX/StandardRes/Cardassia5.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia6, "data/Models/Environment/DS9FX/StandardRes/Cardassia3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia7, "data/Models/Environment/DS9FX/StandardRes/Cardassia7.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia8, "data/Models/Environment/DS9FX/StandardRes/Cardassia8.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 
                    
    else:
        if DS9FXSavedConfig.CardassiaPlanets == 1:
            pCardassia1 = App.Planet_Create(60.0, "data/models/environment/DS9FX/StandardRes/Cardassia1.nif")
            pSet.AddObjectToSet(pCardassia1, "Cardassia 1")

            pCardassia1.PlaceObjectByName( "Cardassia 1" )
            pCardassia1.UpdateNodeOnly()

            pCardassia2 = App.Planet_Create(100.0, "data/models/environment/DS9FX/StandardRes/Cardassia2.nif")
            pSet.AddObjectToSet(pCardassia2, "Cardassia 2")

            pCardassia2.PlaceObjectByName( "Cardassia 2" )
            pCardassia2.UpdateNodeOnly()

            pCardassia3 = App.Planet_Create(120.0, "data/models/environment/DS9FX/StandardRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia3, "Cardassia 3")

            pCardassia3.PlaceObjectByName( "Cardassia 3" )
            pCardassia3.UpdateNodeOnly()

            pCardassia4 = App.Planet_Create(100.0, "data/models/environment/DS9FX/StandardRes/Cardassia6.nif")
            pSet.AddObjectToSet(pCardassia4, "Cardassia 4")

            pCardassia4.PlaceObjectByName( "Cardassia 4" )
            pCardassia4.UpdateNodeOnly()

            pCardassia5 = App.Planet_Create(110.0, "data/models/environment/DS9FX/StandardRes/Cardassia5.nif")
            pSet.AddObjectToSet(pCardassia5, "Cardassia 5")

            pCardassia5.PlaceObjectByName( "Cardassia 5" )
            pCardassia5.UpdateNodeOnly()

            pCardassia6 = App.Planet_Create(75.0, "data/models/environment/DS9FX/StandardRes/Cardassia3.nif")
            pSet.AddObjectToSet(pCardassia6, "Cardassia Prime")

            pCardassia6.PlaceObjectByName( "Cardassia 6" )
            pCardassia6.UpdateNodeOnly()

            pCardassia7 = App.Planet_Create(95.0, "data/models/environment/DS9FX/StandardRes/Cardassia7.nif")
            pSet.AddObjectToSet(pCardassia7, "Cardassia 7")

            pCardassia7.PlaceObjectByName( "Cardassia 7" )
            pCardassia7.UpdateNodeOnly()

            pCardassia8 = App.Planet_Create(200.0, "data/models/environment/DS9FX/StandardRes/Cardassia8.nif")
            pSet.AddObjectToSet(pCardassia8, "Cardassia 8")

            pCardassia8.PlaceObjectByName( "Cardassia 8" )
            pCardassia8.UpdateNodeOnly()

            if DS9FXSavedConfig.CardassiaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia1, "data/Models/Environment/DS9FX/StandardRes/Cardassia1.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia2, "data/Models/Environment/DS9FX/StandardRes/Cardassia2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia3, "data/Models/Environment/DS9FX/StandardRes/Cardassia6.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia4, "data/Models/Environment/DS9FX/StandardRes/Cardassia4.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia5, "data/Models/Environment/DS9FX/StandardRes/Cardassia5.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia6, "data/Models/Environment/DS9FX/StandardRes/Cardassia3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia7, "data/Models/Environment/DS9FX/StandardRes/Cardassia7.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia8, "data/Models/Environment/DS9FX/StandardRes/Cardassia8.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 
