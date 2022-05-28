# by USS Sovereign

import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):                 
        from Custom.DS9FX.DS9FXObjects import DS9Objects
        DS9Objects.DS9SetObjects()

        from Custom.DS9FX.DS9FXObjects import DS9Stations
        DS9Stations.DS9SetStations()

        from Custom.DS9FX.DS9FXObjects import DS9Ships
        DS9Ships.DS9SetShips()
        
        pSun = App.Sun_Create(3000.0, 3000.0, 3000.0, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "B'hava'el")

        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()
        
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun, 1, 0.35, 0.35)
        SunStreak.Create(pSet, "SunStr", 100000.0, "Yellow", "2")        

        reload(DS9FXSavedConfig)
        if DS9FXSavedConfig.DS9MapPlanetDetail == 3:
                if DS9FXSavedConfig.DS9Planets == 1:
                        pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/HighRes/Bajor1High.nif")
                        pSet.AddObjectToSet(pPlanet, "Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/HighRes/Bajor2High.nif")
                        pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor3High.nif")
                        pSet.AddObjectToSet(pPlanet3, "Bajoran Homeworld")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly() 

                        pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/HighRes/Bajor4High.nif")
                        pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()  

                        pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor5High.nif")
                        pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                        pPlanet5.PlaceObjectByName("Planet5")
                        pPlanet5.UpdateNodeOnly()  

                        pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor6High.nif")
                        pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                        pPlanet6.PlaceObjectByName("Planet6")
                        pPlanet6.UpdateNodeOnly()   

                        pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor7High.nif")
                        pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                        pPlanet7.PlaceObjectByName("Planet7")
                        pPlanet7.UpdateNodeOnly()    

                        pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/HighRes/Bajor8High.nif")
                        pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                        pPlanet8.PlaceObjectByName("Planet8")
                        pPlanet8.UpdateNodeOnly()    

                        pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/HighRes/Bajor11High.nif")
                        pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                        pPlanet9.PlaceObjectByName("Planet9")
                        pPlanet9.UpdateNodeOnly()    

                        pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                        pPlanet10.PlaceObjectByName("Planet10")
                        pPlanet10.UpdateNodeOnly()   

                        pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/HighRes/Bajor10High.nif")
                        pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                        pPlanet11.PlaceObjectByName("Planet11")
                        pPlanet11.UpdateNodeOnly()     

                        pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/HighRes/Bajor12High.nif")
                        pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                        pPlanet12.PlaceObjectByName("Planet12")
                        pPlanet12.UpdateNodeOnly()     

                        pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                        pPlanet13.PlaceObjectByName("Planet13")
                        pPlanet13.UpdateNodeOnly()     

                        pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/HighRes/Bajor13High.nif")
                        pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                        pPlanet14.PlaceObjectByName("Planet14")
                        pPlanet14.UpdateNodeOnly()

                        if DS9FXSavedConfig.DS9NanoFX == 1:
                                try:                            
                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/HighRes/Bajor1High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Bajor2High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Bajor3High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/Bajor4High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/HighRes/Bajor5High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/HighRes/Bajor6High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/HighRes/Bajor7High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/HighRes/Bajor8High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/HighRes/Bajor11High.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/HighRes/Bajor10High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/HighRes/Bajor12High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/HighRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/HighRes/Bajor13High.nif", "Class-K")

                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                        else:
                                pass


                else:
                        return

        elif DS9FXSavedConfig.DS9MapPlanetDetail == 2:
                if DS9FXSavedConfig.DS9Planets == 1:
                        pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/StandardRes/Bajor1High.nif")
                        pSet.AddObjectToSet(pPlanet, "Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/StandardRes/Bajor2High.nif")
                        pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor3High.nif")
                        pSet.AddObjectToSet(pPlanet3, "Bajoran Homeworld")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly() 

                        pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/StandardRes/Bajor4High.nif")
                        pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()  

                        pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor5High.nif")
                        pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                        pPlanet5.PlaceObjectByName("Planet5")
                        pPlanet5.UpdateNodeOnly()  

                        pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor6High.nif")
                        pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                        pPlanet6.PlaceObjectByName("Planet6")
                        pPlanet6.UpdateNodeOnly()   

                        pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor7High.nif")
                        pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                        pPlanet7.PlaceObjectByName("Planet7")
                        pPlanet7.UpdateNodeOnly()    

                        pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/StandardRes/Bajor8High.nif")
                        pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                        pPlanet8.PlaceObjectByName("Planet8")
                        pPlanet8.UpdateNodeOnly()    

                        pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/StandardRes/Bajor11High.nif")
                        pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                        pPlanet9.PlaceObjectByName("Planet9")
                        pPlanet9.UpdateNodeOnly()    

                        pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                        pPlanet10.PlaceObjectByName("Planet10")
                        pPlanet10.UpdateNodeOnly()   

                        pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/StandardRes/Bajor10High.nif")
                        pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                        pPlanet11.PlaceObjectByName("Planet11")
                        pPlanet11.UpdateNodeOnly()     

                        pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/StandardRes/Bajor12High.nif")
                        pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                        pPlanet12.PlaceObjectByName("Planet12")
                        pPlanet12.UpdateNodeOnly()     

                        pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                        pPlanet13.PlaceObjectByName("Planet13")
                        pPlanet13.UpdateNodeOnly()     

                        pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/StandardRes/Bajor13High.nif")
                        pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                        pPlanet14.PlaceObjectByName("Planet14")
                        pPlanet14.UpdateNodeOnly()

                        if DS9FXSavedConfig.DS9NanoFX == 1:
                                try:

                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/StandardRes/Bajor1High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Bajor2High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Bajor3High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/Bajor4High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/StandardRes/Bajor5High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/StandardRes/Bajor6High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/StandardRes/Bajor7High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/StandardRes/Bajor8High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/StandardRes/Bajor11High.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/StandardRes/Bajor10High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/StandardRes/Bajor12High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/StandardRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/StandardRes/Bajor13High.nif", "Class-K")


                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                        else:
                                pass


                else:
                        return


        elif DS9FXSavedConfig.DS9MapPlanetDetail == 1:
                if DS9FXSavedConfig.DS9Planets == 1:
                        pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/LowRes/Bajor1High.nif")
                        pSet.AddObjectToSet(pPlanet, "Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowRes/Bajor2High.nif")
                        pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor3High.nif")
                        pSet.AddObjectToSet(pPlanet3, "Bajoran Homeworld")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly() 

                        pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowRes/Bajor4High.nif")
                        pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()  

                        pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor5High.nif")
                        pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                        pPlanet5.PlaceObjectByName("Planet5")
                        pPlanet5.UpdateNodeOnly()  

                        pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor6High.nif")
                        pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                        pPlanet6.PlaceObjectByName("Planet6")
                        pPlanet6.UpdateNodeOnly()   

                        pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor7High.nif")
                        pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                        pPlanet7.PlaceObjectByName("Planet7")
                        pPlanet7.UpdateNodeOnly()    

                        pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/LowRes/Bajor8High.nif")
                        pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                        pPlanet8.PlaceObjectByName("Planet8")
                        pPlanet8.UpdateNodeOnly()    

                        pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/LowRes/Bajor11High.nif")
                        pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                        pPlanet9.PlaceObjectByName("Planet9")
                        pPlanet9.UpdateNodeOnly()    

                        pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                        pPlanet10.PlaceObjectByName("Planet10")
                        pPlanet10.UpdateNodeOnly()   

                        pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowRes/Bajor10High.nif")
                        pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                        pPlanet11.PlaceObjectByName("Planet11")
                        pPlanet11.UpdateNodeOnly()     

                        pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowRes/Bajor12High.nif")
                        pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                        pPlanet12.PlaceObjectByName("Planet12")
                        pPlanet12.UpdateNodeOnly()     

                        pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                        pPlanet13.PlaceObjectByName("Planet13")
                        pPlanet13.UpdateNodeOnly()     

                        pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowRes/Bajor13High.nif")
                        pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                        pPlanet14.PlaceObjectByName("Planet14")
                        pPlanet14.UpdateNodeOnly()

                        if DS9FXSavedConfig.DS9NanoFX == 1:
                                try:

                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowRes/Bajor1High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Bajor2High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Bajor3High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/Bajor4High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowRes/Bajor5High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/LowRes/Bajor6High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/LowRes/Bajor7High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/LowRes/Bajor8High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/LowRes/Bajor11High.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/LowRes/Bajor10High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/LowRes/Bajor12High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/LowRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/LowRes/Bajor13High.nif", "Class-K")


                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                        else:
                                pass


                else:
                        return


        else:
                if DS9FXSavedConfig.DS9Planets == 1:
                        pPlanet = App.Planet_Create(50.0, "data/Models/Environment/DS9FX/LowestRes/Bajor1High.nif")
                        pSet.AddObjectToSet(pPlanet, "Bajor 1")

                        pPlanet.PlaceObjectByName("Planet1")
                        pPlanet.UpdateNodeOnly()

                        pPlanet2 = App.Planet_Create(55.0, "data/Models/Environment/DS9FX/LowestRes/Bajor2High.nif")
                        pSet.AddObjectToSet(pPlanet2, "Bajor 2")

                        pPlanet2.PlaceObjectByName("Planet2")
                        pPlanet2.UpdateNodeOnly()

                        pPlanet3 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowestRes/Bajor3High.nif")
                        pSet.AddObjectToSet(pPlanet3, "Bajoran Homeworld")

                        pPlanet3.PlaceObjectByName("Planet3")
                        pPlanet3.UpdateNodeOnly() 

                        pPlanet4 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowestRes/Bajor4High.nif")
                        pSet.AddObjectToSet(pPlanet4, "Bajor 4")

                        pPlanet4.PlaceObjectByName("Planet4")
                        pPlanet4.UpdateNodeOnly()  

                        pPlanet5 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowestRes/Bajor5High.nif")
                        pSet.AddObjectToSet(pPlanet5, "Bajor 5")

                        pPlanet5.PlaceObjectByName("Planet5")
                        pPlanet5.UpdateNodeOnly()  

                        pPlanet6 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowestRes/Bajor6High.nif")
                        pSet.AddObjectToSet(pPlanet6, "Bajor 6")

                        pPlanet6.PlaceObjectByName("Planet6")
                        pPlanet6.UpdateNodeOnly()

                        pPlanet7 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowestRes/Bajor7High.nif")
                        pSet.AddObjectToSet(pPlanet7, "Bajor 7")

                        pPlanet7.PlaceObjectByName("Planet7")
                        pPlanet7.UpdateNodeOnly()    

                        pPlanet8 = App.Planet_Create(90.0, "data/Models/Environment/DS9FX/LowestRes/Bajor8High.nif")
                        pSet.AddObjectToSet(pPlanet8, "Bajor 8")

                        pPlanet8.PlaceObjectByName("Planet8")
                        pPlanet8.UpdateNodeOnly()    

                        pPlanet9 = App.Planet_Create(40.0, "data/Models/Environment/DS9FX/LowestRes/Bajor11High.nif")
                        pSet.AddObjectToSet(pPlanet9, "Bajor 9")

                        pPlanet9.PlaceObjectByName("Planet9")
                        pPlanet9.UpdateNodeOnly()    

                        pPlanet10 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowestRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet10, "Bajor 10")

                        pPlanet10.PlaceObjectByName("Planet10")
                        pPlanet10.UpdateNodeOnly()   

                        pPlanet11 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/LowestRes/Bajor10High.nif")
                        pSet.AddObjectToSet(pPlanet11, "Bajor 11")

                        pPlanet11.PlaceObjectByName("Planet11")
                        pPlanet11.UpdateNodeOnly()     

                        pPlanet12 = App.Planet_Create(100.0, "data/Models/Environment/DS9FX/LowestRes/Bajor12High.nif")
                        pSet.AddObjectToSet(pPlanet12, "Bajor 12")

                        pPlanet12.PlaceObjectByName("Planet12")
                        pPlanet12.UpdateNodeOnly()     

                        pPlanet13 = App.Planet_Create(120.0, "data/Models/Environment/DS9FX/LowestRes/Bajor9High.nif")
                        pSet.AddObjectToSet(pPlanet13, "Bajor 13")

                        pPlanet13.PlaceObjectByName("Planet13")
                        pPlanet13.UpdateNodeOnly()     

                        pPlanet14 = App.Planet_Create(60.0, "data/Models/Environment/DS9FX/LowestRes/Bajor13High.nif")
                        pSet.AddObjectToSet(pPlanet14, "Bajor 14")

                        pPlanet14.PlaceObjectByName("Planet14")
                        pPlanet14.UpdateNodeOnly()

                        if DS9FXSavedConfig.DS9NanoFX == 1:
                                try:

                                        import Custom.NanoFXv2.NanoFX_Lib
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/Models/Environment/DS9FX/LowestRes/Bajor1High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Bajor2High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Bajor3High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/Bajor4High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowestRes/Bajor5High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet6, "data/Models/Environment/DS9FX/LowestRes/Bajor6High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet7, "data/Models/Environment/DS9FX/LowestRes/Bajor7High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet8, "data/Models/Environment/DS9FX/LowestRes/Bajor8High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet9, "data/Models/Environment/DS9FX/LowestRes/Bajor11High.nif", "Class-O")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet10, "data/Models/Environment/DS9FX/LowestRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet11, "data/Models/Environment/DS9FX/LowestRes/Bajor10High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet12, "data/Models/Environment/DS9FX/LowestRes/Bajor12High.nif", "Class-K")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet13, "data/Models/Environment/DS9FX/LowestRes/Bajor9High.nif", "Class-M")
                                        Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet14, "data/Models/Environment/DS9FX/LowestRes/Bajor13High.nif", "Class-K")


                                except:
                                        print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"

                        else:
                                pass


                else:
                        return

