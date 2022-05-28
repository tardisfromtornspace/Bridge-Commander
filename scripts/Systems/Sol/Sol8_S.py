from bcdebug import debug
###############################################################################
#       Filename:       Sol8_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 5 static objects.  Called by Sol8.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

        # 4.5 billion km from the sun

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        ######
        # Create the Planet - 49,528 km diameter
        pNeptune = App.Planet_Create(2830.17, "data/models/environment/Neptune.nif")
        pSet.AddObjectToSet(pNeptune, "Neptune")

        # Place the object at the specified location.
        pNeptune.PlaceObjectByName( "Neptune" )
        pNeptune.SetAtmosphereRadius(0.01)
        pNeptune.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pNeptune, "data/models/environment/Neptune.nif", "Class-K")        


        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pNeptune, 5.80e4, 5.17e9, pSun)

        pTriton = App.Planet_Create(154.29, "data/models/environment/Triton.nif")
        pSet.AddObjectToSet(pTriton, "Triton")

        # Place the object at the specified location.
        pTriton.PlaceObjectByName( "Triton" )
        pTriton.SetAtmosphereRadius(0.01)
        pTriton.UpdateNodeOnly()

