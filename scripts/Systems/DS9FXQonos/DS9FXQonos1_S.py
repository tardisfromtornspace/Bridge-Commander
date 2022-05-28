import App
import MissionLib
import Tactical.LensFlares
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
from Custom.DS9FX.DS9FXSunStreak import SunStreak

def Initialize(pSet):        
    from Custom.DS9FX.DS9FXObjects import QonosShips
    QonosShips.QonosSetShips() 
    
    pSun = App.Sun_Create(4500.0, 4500.0, 4500.0, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRedOrange.tga")
    pSet.AddObjectToSet(pSun, "Qo'nos Sun")

    pSun.PlaceObjectByName( "Sun" )
    pSun.UpdateNodeOnly()

    Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun, 1, 0.65, 0.65)
    SunStreak.Create(pSet, "SunStr", 150000.0, "RedOrange", "4")    
    
    reload(DS9FXSavedConfig)
    if DS9FXSavedConfig.QonosMapPlanetDetail == 3:
        if DS9FXSavedConfig.QonosPlanets == 1:                        
                    pPlanet1 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/HighRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet1, "Qo'nos 1")

                    pPlanet1.PlaceObjectByName("Planet1")
                    pPlanet1.UpdateNodeOnly()  
                    
                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/HighRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet2, "Qo'nos 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()  
                    
                    pDS9FXQonos = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/HighRes/Qonos.nif")
                    pSet.AddObjectToSet(pDS9FXQonos, "Qo'nos")
                    
                    pDS9FXQonos.PlaceObjectByName( "Colony" )
                    pDS9FXQonos.UpdateNodeOnly()                       
                    
                    pPlanet3 = App.Planet_Create(150.0, "data/Models/Environment/DS9FX/HighRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet3, "Qo'nos 4")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()  
                    
                    pPlanet4 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Qo'nos 5")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()      
                    
                    pPlanet5 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/HighRes/bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Qo'nos 6")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()                          

                    if DS9FXSavedConfig.QonosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pDS9FXQonos, "data/Models/Environment/DS9FX/HighRes/Qonos.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/HighRes/Planet004.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/HighRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/HighRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/HighRes/Gamma1High.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/HighRes/bajor9High.nif", "Class-H")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
                            
    elif DS9FXSavedConfig.QonosMapPlanetDetail == 2:
        if DS9FXSavedConfig.QonosPlanets == 1:                        
                    pPlanet1 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet1, "Qo'nos 1")

                    pPlanet1.PlaceObjectByName("Planet1")
                    pPlanet1.UpdateNodeOnly()  
                    
                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet2, "Qo'nos 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()  
                    
                    pDS9FXQonos = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/StandardRes/Qonos.nif")
                    pSet.AddObjectToSet(pDS9FXQonos, "Qo'nos")
                    
                    pDS9FXQonos.PlaceObjectByName( "Colony" )
                    pDS9FXQonos.UpdateNodeOnly()                       
                    
                    pPlanet3 = App.Planet_Create(150.0, "data/Models/Environment/DS9FX/StandardRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet3, "Qo'nos 4")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()  
                    
                    pPlanet4 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Qo'nos 5")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()      
                    
                    pPlanet5 = App.Planet_Create(200.0, "data/Models/Environment/DS9FX/StandardRes/bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Qo'nos 6")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()                          

                    if DS9FXSavedConfig.QonosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pDS9FXQonos, "data/Models/Environment/DS9FX/StandardRes/Qonos.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/StandardRes/Planet004.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/StandardRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/StandardRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/StandardRes/Gamma1High.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/StandardRes/bajor9High.nif", "Class-H")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"                       

    elif DS9FXSavedConfig.QonosMapPlanetDetail == 1:
        if DS9FXSavedConfig.QonosPlanets == 1:                        
                    pPlanet1 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet1, "Qo'nos 1")

                    pPlanet1.PlaceObjectByName("Planet1")
                    pPlanet1.UpdateNodeOnly()  
                    
                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet2, "Qo'nos 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()  
                    
                    pDS9FXQonos = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/LowRes/Qonos.nif")
                    pSet.AddObjectToSet(pDS9FXQonos, "Qo'nos")
                    
                    pDS9FXQonos.PlaceObjectByName( "Colony" )
                    pDS9FXQonos.UpdateNodeOnly()                       
                    
                    pPlanet3 = App.Planet_Create(150.0, "data/Models/Environment/DS9FX/LowRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet3, "Qo'nos 4")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()  
                    
                    pPlanet4 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Qo'nos 5")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()      
                    
                    pPlanet5 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/LowRes/bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Qo'nos 6")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()                          

                    if DS9FXSavedConfig.QonosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pDS9FXQonos, "data/Models/Environment/DS9FX/LowRes/Qonos.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/LowRes/Planet004.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowRes/Gamma1High.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowRes/bajor9High.nif", "Class-H")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"
                            
    else:
        if DS9FXSavedConfig.QonosPlanets == 1:                        
                    pPlanet1 = App.Planet_Create(88.0, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif")
                    pSet.AddObjectToSet(pPlanet1, "Qo'nos 1")

                    pPlanet1.PlaceObjectByName("Planet1")
                    pPlanet1.UpdateNodeOnly()  
                    
                    pPlanet2 = App.Planet_Create(70.0, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif")
                    pSet.AddObjectToSet(pPlanet2, "Qo'nos 2")

                    pPlanet2.PlaceObjectByName("Planet2")
                    pPlanet2.UpdateNodeOnly()  
                    
                    pDS9FXQonos = App.Planet_Create(95.0, "data/Models/Environment/DS9FX/LowestRes/Qonos.nif")
                    pSet.AddObjectToSet(pDS9FXQonos, "Qo'nos")
                    
                    pDS9FXQonos.PlaceObjectByName( "Colony" )
                    pDS9FXQonos.UpdateNodeOnly()                       
                    
                    pPlanet3 = App.Planet_Create(150.0, "data/Models/Environment/DS9FX/LowestRes/Planet002.nif")
                    pSet.AddObjectToSet(pPlanet3, "Qo'nos 4")

                    pPlanet3.PlaceObjectByName("Planet3")
                    pPlanet3.UpdateNodeOnly()  
                    
                    pPlanet4 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif")
                    pSet.AddObjectToSet(pPlanet4, "Qo'nos 5")

                    pPlanet4.PlaceObjectByName("Planet4")
                    pPlanet4.UpdateNodeOnly()      
                    
                    pPlanet5 = App.Planet_Create(175.0, "data/Models/Environment/DS9FX/LowestRes/bajor9High.nif")
                    pSet.AddObjectToSet(pPlanet5, "Qo'nos 6")

                    pPlanet5.PlaceObjectByName("Planet5")
                    pPlanet5.UpdateNodeOnly()                          

                    if DS9FXSavedConfig.QonosNanoFX == 1:
                        try:
                            import Custom.NanoFXv2.NanoFX_Lib
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pDS9FXQonos, "data/Models/Environment/DS9FX/LowestRes/Qonos.nif", "Class-M")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet1, "data/Models/Environment/DS9FX/LowestRes/Planet004.nif", "Class-K")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet2, "data/Models/Environment/DS9FX/LowestRes/Planet003.nif", "Class-O")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet3, "data/Models/Environment/DS9FX/LowestRes/Planet002.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet4, "data/Models/Environment/DS9FX/LowestRes/Gamma1High.nif", "Class-H")
                            Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet5, "data/Models/Environment/DS9FX/LowestRes/bajor9High.nif", "Class-H")
                        except:
                            print "DS9FX: No NanoFX 2.0 Beta installed to enhance your atmospheres! Now, you'll just have to deal with crappy stock ones!!!"                           
