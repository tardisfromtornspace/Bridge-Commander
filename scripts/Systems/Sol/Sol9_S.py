from bcdebug import debug
###############################################################################
#       Filename:       Sol9_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 5 static objects.  Called by Sol9.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

        # 4.7 billion km from the sun

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        ######
        # Create the Planet - 2,290 km diameter
        pPluto = App.Planet_Create(130.86, "data/models/environment/Pluto.nif")
        pSet.AddObjectToSet(pPluto, "Pluto")

        # Place the object at the specified location.
        pPluto.PlaceObjectByName( "Pluto" )
        pPluto.SetAtmosphereRadius(0.01)
        pPluto.UpdateNodeOnly()

        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pPluto, 7.83e9, 3.74e8, pSun)

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPluto, "data/models/environment/Pluto.nif", "Class-K")    

        pCharon = App.Planet_Create(66.97, "data/models/environment/Charon.nif")
        pSet.AddObjectToSet(pCharon, "Charon")

        # Place the object at the specified location.
        pCharon.PlaceObjectByName( "Charon" )
        pCharon.SetAtmosphereRadius(0.01)
        pCharon.UpdateNodeOnly()

