from bcdebug import debug
###############################################################################
#       Filename:       Sol1_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 1 static objects.  Called by Sol1.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
#  NanoFx2 effects added: 2/20/04 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        # Builds a Red-Orange lens flare, attached to the sun
        Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

        ######
        # Create the Planet - 4,879 km diameter
        pMercury = App.Planet_Create(278.80, "data/models/environment/Mercury.nif")
        pSet.AddObjectToSet(pMercury, "Mercury")

        # Place the object at the specified location.
        pMercury.PlaceObjectByName( "Mercury" )
        pMercury.UpdateNodeOnly()

        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pMercury, 5.07e6, 7.60e6, pSun)

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMercury, "data/models/environment/Mercury.nif", "Class-K")

        

