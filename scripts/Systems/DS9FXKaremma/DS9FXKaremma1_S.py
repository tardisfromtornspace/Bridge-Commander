# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):
        from Custom.DS9FX.DS9FXObjects import KaremmaShips
        KaremmaShips.KaremmaSetShips()
        
        pSun = App.Sun_Create(3775.0, 3775.0, 3775.0, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Karemman Sun")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.YellowLensFlare(pSet, pSun)
        SunStreak.Create(pSet, "SunStr", 80000.0, "Yellow", "8")        

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.KaremmaMapPlanetDetail == 3:
                if DS9FXSavedConfig.KaremmaPlanets == 1:
                        pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet2, "Karemma 1")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/HighRes/Karemma.nif")
                        pSet.AddObjectToSet(pPlanet, "Karemman Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.KaremmaNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Karemma.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.KaremmaMapPlanetDetail == 2:
                if DS9FXSavedConfig.KaremmaPlanets == 1:
                        pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet2, "Karemma 1")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/StandardRes/Karemma.nif")
                        pSet.AddObjectToSet(pPlanet, "Karemman Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.KaremmaNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Karemma.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.KaremmaMapPlanetDetail == 1:
                if DS9FXSavedConfig.KaremmaPlanets == 1:
                        pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet2, "Karemma 1")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/LowRes/Karemma.nif")
                        pSet.AddObjectToSet(pPlanet, "Karemman Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.KaremmaNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Karemma.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        else:
                if DS9FXSavedConfig.KaremmaPlanets == 1:
                        pPlanet2 = App.Planet_Create(105.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                        pSet.AddObjectToSet(pPlanet2, "Karemma 1")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet = App.Planet_Create(75.0, "data/Models/Environment/DS9FX/LowestRes/Karemma.nif")
                        pSet.AddObjectToSet(pPlanet, "Karemman Homeworld")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        if DS9FXSavedConfig.KaremmaNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Karemma.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-H")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
