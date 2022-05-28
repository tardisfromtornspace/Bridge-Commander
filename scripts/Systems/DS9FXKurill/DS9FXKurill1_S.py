# by Sov

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):    
        from Custom.DS9FX.DS9FXObjects import KurrillShips
        KurrillShips.KurrillSetShips()
        
        pSun = App.Sun_Create(2800.0, 2800.0, 2800.0, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
        pSet.AddObjectToSet(pSun, "Kurill Sun")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun, 1, 0.5, 0.5)
        SunStreak.Create(pSet, "SunStr", 110000.0, "Red", "6")        

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.KurrillMapPlanetDetail == 3:
                if DS9FXSavedConfig.KurrillPlanets == 1:
                        pPlanet = App.Planet_Create(92.0, "data/Models/Environment/DS9FX/HighRes/KurrillPrime.nif")
                        pSet.AddObjectToSet(pPlanet, "Kurill Prime")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/HighRes/Planet005.nif")
                        pSet.AddObjectToSet(pPlanet2, "Kurill 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        if DS9FXSavedConfig.KurrillNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/KurrillPrime.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet005.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.KurrillMapPlanetDetail == 2:
                if DS9FXSavedConfig.KurrillPlanets == 1:
                        pPlanet = App.Planet_Create(92.0, "data/Models/Environment/DS9FX/StandardRes/KurrillPrime.nif")
                        pSet.AddObjectToSet(pPlanet, "Kurill Prime")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/StandardRes/Planet005.nif")
                        pSet.AddObjectToSet(pPlanet2, "Kurill 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        if DS9FXSavedConfig.KurrillNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/KurrillPrime.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet005.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        elif DS9FXSavedConfig.KurrillMapPlanetDetail == 1:
                if DS9FXSavedConfig.KurrillPlanets == 1:
                        pPlanet = App.Planet_Create(92.0, "data/Models/Environment/DS9FX/LowRes/KurrillPrime.nif")
                        pSet.AddObjectToSet(pPlanet, "Kurill Prime")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowRes/Planet005.nif")
                        pSet.AddObjectToSet(pPlanet2, "Kurill 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        if DS9FXSavedConfig.KurrillNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/KurrillPrime.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet005.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

        else:
                if DS9FXSavedConfig.KurrillPlanets == 1:
                        pPlanet = App.Planet_Create(92.0, "data/Models/Environment/DS9FX/LowestRes/KurrillPrime.nif")
                        pSet.AddObjectToSet(pPlanet, "Kurill Prime")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowestRes/Planet005.nif")
                        pSet.AddObjectToSet(pPlanet2, "Kurill 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        if DS9FXSavedConfig.KurrillNanoFX == 1:
                                try:
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/KurrillPrime.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet005.nif", "Class-M")
                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
