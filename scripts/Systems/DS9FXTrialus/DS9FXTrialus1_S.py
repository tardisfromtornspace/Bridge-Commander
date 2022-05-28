# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):       
    pSun = App.Sun_Create(5760.0, 5760.0, 5760.0, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
    pSet.AddObjectToSet(pSun, "Trialus Sun")
    
    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()
    
    Tactical.LensFlares.WhiteLensFlare(pSet, pSun)
    SunStreak.Create(pSet, "SunStr", 85000.0, "White", "6")    
    
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.TrialusMapPlanetDetail == 3:
        if DS9FXSavedConfig.TrialusPlanets == 1:    
                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/HighRes/Meridian.nif")
                    pSet.AddObjectToSet(pPlanet, "Meridian")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.TrialusNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Meridian.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.TrialusMapPlanetDetail == 2:
        if DS9FXSavedConfig.TrialusPlanets == 1:    
                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/StandardRes/Meridian.nif")
                    pSet.AddObjectToSet(pPlanet, "Meridian")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.TrialusNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Meridian.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    elif DS9FXSavedConfig.TrialusMapPlanetDetail == 1:
        if DS9FXSavedConfig.TrialusPlanets == 1:    
                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/LowRes/Meridian.nif")
                    pSet.AddObjectToSet(pPlanet, "Meridian")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.TrialusNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Meridian.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

    else:
        if DS9FXSavedConfig.TrialusPlanets == 1:    
                    pPlanet = App.Planet_Create(65.0, "data/Models/Environment/DS9FX/LowestRes/Meridian.nif")
                    pSet.AddObjectToSet(pPlanet, "Meridian")

                    pPlanet.PlaceObjectByName("Planet1")
                    pPlanet.UpdateNodeOnly()

                    if DS9FXSavedConfig.TrialusNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Meridian.nif", "Class-M")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
