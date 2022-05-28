import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):    
    pSun = App.Sun_Create(3500.0, 3500.0, 3500.0, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
    pSet.AddObjectToSet(pSun, "Chin'toka Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.YellowLensFlare(pSet, pSun, 1, 0.5, 0.5)
    SunStreak.Create(pSet, "SunStr", 75000.0, "Yellow", "6")

    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.ChintokaMapPlanetDetail == 3:
        if DS9FXSavedConfig.ChintokaPlanets == 1:
            pPlanet1 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Chintoka1.nif")
            pSet.AddObjectToSet(pPlanet1, "Chin'toka 1")

            pPlanet1.PlaceObjectByName("Planet1")
            pPlanet1.UpdateNodeOnly()  

            pPlanet2 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/HighRes/Chintoka2.nif")
            pSet.AddObjectToSet(pPlanet2, "Chin'toka 2")

            pPlanet2.PlaceObjectByName("Planet2")
            pPlanet2.UpdateNodeOnly()  

            pPlanet3 = App.Planet_Create(115.0, "data/Models/Environment/DS9FX/HighRes/Chintoka3.nif")
            pSet.AddObjectToSet(pPlanet3, "Chin'toka 3")

            pPlanet3.PlaceObjectByName("Planet3")
            pPlanet3.UpdateNodeOnly()  

            pPlanet4 = App.Planet_Create(85.0, "data/Models/Environment/DS9FX/HighRes/Chintoka4.nif")
            pSet.AddObjectToSet(pPlanet4, "Chin'toka 4")

            pPlanet4.PlaceObjectByName("Planet4")
            pPlanet4.UpdateNodeOnly()      

            pPlanet5 = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/HighRes/Chintoka5.nif")
            pSet.AddObjectToSet(pPlanet5, "AR 558")

            pPlanet5.PlaceObjectByName("Planet5")
            pPlanet5.UpdateNodeOnly()                          

            if DS9FXSavedConfig.ChintokaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/HighRes/Chintoka1.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Chintoka2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Chintoka3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/Chintoka4.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/HighRes/Chintoka5.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.ChintokaMapPlanetDetail == 2:
        if DS9FXSavedConfig.ChintokaPlanets == 1:
            pPlanet1 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Chintoka1.nif")
            pSet.AddObjectToSet(pPlanet1, "Chin'toka 1")

            pPlanet1.PlaceObjectByName("Planet1")
            pPlanet1.UpdateNodeOnly()  

            pPlanet2 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/StandardRes/Chintoka2.nif")
            pSet.AddObjectToSet(pPlanet2, "Chin'toka 2")

            pPlanet2.PlaceObjectByName("Planet2")
            pPlanet2.UpdateNodeOnly()  

            pPlanet3 = App.Planet_Create(115.0, "data/Models/Environment/DS9FX/StandardRes/Chintoka3.nif")
            pSet.AddObjectToSet(pPlanet3, "Chin'toka 3")

            pPlanet3.PlaceObjectByName("Planet3")
            pPlanet3.UpdateNodeOnly()  

            pPlanet4 = App.Planet_Create(85.0, "data/Models/Environment/DS9FX/StandardRes/Chintoka4.nif")
            pSet.AddObjectToSet(pPlanet4, "Chin'toka 4")

            pPlanet4.PlaceObjectByName("Planet4")
            pPlanet4.UpdateNodeOnly()      

            pPlanet5 = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/StandardRes/Chintoka5.nif")
            pSet.AddObjectToSet(pPlanet5, "AR 558")

            pPlanet5.PlaceObjectByName("Planet5")
            pPlanet5.UpdateNodeOnly()                          

            if DS9FXSavedConfig.ChintokaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/StandardRes/Chintoka1.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Chintoka2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Chintoka3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/Chintoka4.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/StandardRes/Chintoka5.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"                   

    elif DS9FXSavedConfig.ChintokaMapPlanetDetail == 1:
        if DS9FXSavedConfig.ChintokaPlanets == 1:            
            pPlanet1 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Chintoka1.nif")
            pSet.AddObjectToSet(pPlanet1, "Chin'toka 1")

            pPlanet1.PlaceObjectByName("Planet1")
            pPlanet1.UpdateNodeOnly()  

            pPlanet2 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/LowRes/Chintoka2.nif")
            pSet.AddObjectToSet(pPlanet2, "Chin'toka 2")

            pPlanet2.PlaceObjectByName("Planet2")
            pPlanet2.UpdateNodeOnly()  

            pPlanet3 = App.Planet_Create(115.0, "data/Models/Environment/DS9FX/LowRes/Chintoka3.nif")
            pSet.AddObjectToSet(pPlanet3, "Chin'toka 3")

            pPlanet3.PlaceObjectByName("Planet3")
            pPlanet3.UpdateNodeOnly()  

            pPlanet4 = App.Planet_Create(85.0, "data/Models/Environment/DS9FX/LowRes/Chintoka4.nif")
            pSet.AddObjectToSet(pPlanet4, "Chin'toka 4")

            pPlanet4.PlaceObjectByName("Planet4")
            pPlanet4.UpdateNodeOnly()      

            pPlanet5 = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/LowRes/Chintoka5.nif")
            pSet.AddObjectToSet(pPlanet5, "AR 558")

            pPlanet5.PlaceObjectByName("Planet5")
            pPlanet5.UpdateNodeOnly()                          

            if DS9FXSavedConfig.ChintokaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/LowRes/Chintoka1.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Chintoka2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Chintoka3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/Chintoka4.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowRes/Chintoka5.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.ChintokaPlanets == 1:
            pPlanet1 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowestRes/Chintoka1.nif")
            pSet.AddObjectToSet(pPlanet1, "Chin'toka 1")

            pPlanet1.PlaceObjectByName("Planet1")
            pPlanet1.UpdateNodeOnly()  

            pPlanet2 = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/LowestRes/Chintoka2.nif")
            pSet.AddObjectToSet(pPlanet2, "Chin'toka 2")

            pPlanet2.PlaceObjectByName("Planet2")
            pPlanet2.UpdateNodeOnly()  

            pPlanet3 = App.Planet_Create(115.0, "data/Models/Environment/DS9FX/LowestRes/Chintoka3.nif")
            pSet.AddObjectToSet(pPlanet3, "Chin'toka 3")

            pPlanet3.PlaceObjectByName("Planet3")
            pPlanet3.UpdateNodeOnly()  

            pPlanet4 = App.Planet_Create(85.0, "data/Models/Environment/DS9FX/LowestRes/Chintoka4.nif")
            pSet.AddObjectToSet(pPlanet4, "Chin'toka 4")

            pPlanet4.PlaceObjectByName("Planet4")
            pPlanet4.UpdateNodeOnly()      

            pPlanet5 = App.Planet_Create(35.0, "data/Models/Environment/DS9FX/LowestRes/Chintoka5.nif")
            pSet.AddObjectToSet(pPlanet5, "AR 558")

            pPlanet5.PlaceObjectByName("Planet5")
            pPlanet5.UpdateNodeOnly()                          

            if DS9FXSavedConfig.ChintokaNanoFX == 1:
                try:
                    import Custom.NanoFXv2.NanoFX_Lib
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/LowestRes/Chintoka1.nif", "Class-H")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Chintoka2.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Chintoka3.nif", "Class-M")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/Chintoka4.nif", "Class-K")
                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowestRes/Chintoka5.nif", "Class-O")
                except:
                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!" 