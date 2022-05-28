# by USS Sovereign

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):       
    from Custom.DS9FX.DS9FXObjects import GammaObjects
    GammaObjects.GammsSetObjects()

    from Custom.DS9FX.DS9FXObjects import GammaShips
    GammaShips.GammaSetShips()
    
    pSun = App.Sun_Create(9000.0, 9000.0, 9000.0, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
    pSet.AddObjectToSet(pSun, "Idran A")

    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()

    Tactical.LensFlares.WhiteLensFlare(pSet, pSun, 1, 0.35, 0.35)
    SunStreak.Create(pSet, "SunStr", 125000.0, "White", "4")

    pSun2 = App.Sun_Create(4500.0, 4500.0, 4500.0, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
    pSet.AddObjectToSet(pSun2, "Idran B")

    pSun2.PlaceObjectByName( "Sun2" )
    pSun2.UpdateNodeOnly()

    Tactical.LensFlares.WhiteLensFlare(pSet, pSun2, 1, 0.15, 0.15)
    SunStreak.Create(pSet, "Sun2Str", 60000.0, "White", "4")

    pSun3 = App.Sun_Create(5000.0, 5000.0, 5000.0, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
    pSet.AddObjectToSet(pSun3, "Idran C")

    pSun3.PlaceObjectByName( "Sun3" )
    pSun3.UpdateNodeOnly()

    Tactical.LensFlares.WhiteLensFlare(pSet, pSun3, 1, 0.2, 0.2)
    SunStreak.Create(pSet, "Sun3Str", 70000.0, "White", "4")    

    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.GammaMapPlanetDetail == 3:
            if DS9FXSavedConfig.GammaPlanets == 1:
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.GammaNanoFX == 1:
                            try:
                                    import Custom.NanoFXv2.NanoFX_Lib
                                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif", "Class-M")

                            except:
                                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
            else:
                    return


    elif DS9FXSavedConfig.GammaMapPlanetDetail == 2:
            if DS9FXSavedConfig.GammaPlanets == 1:
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.GammaNanoFX == 1:
                            try:
                                    import Custom.NanoFXv2.NanoFX_Lib
                                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif", "Class-M")

                            except:
                                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
            else:
                    return


    elif DS9FXSavedConfig.GammaMapPlanetDetail == 1:
            if DS9FXSavedConfig.GammaPlanets == 1:
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.GammaNanoFX == 1:
                            try:
                                    import Custom.NanoFXv2.NanoFX_Lib
                                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif", "Class-M")

                            except:
                                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
            else:
                    return


    else:
            if DS9FXSavedConfig.GammaPlanets == 1:
                    pPlanet = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet, "Idran")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.GammaNanoFX == 1:
                            try:
                                    import Custom.NanoFXv2.NanoFX_Lib
                                    Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif", "Class-M")

                            except:
                                    print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
            else:
                    return

