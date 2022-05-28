from bcdebug import debug
###############################################################################
#       Filename:       Sol4_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 4 static objects.  Called by Sol4.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
# NanoFx2 effects added: 2/20/04 - Chris Jones
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

        # 228 million km from the sun

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
        # Create the Planet - 6,794 km diameter
        pMars = App.Planet_Create(388.23, "data/models/environment/Mars.nif")
        pSet.AddObjectToSet(pMars, "Mars")

        # Place the object at the specified location.
        pMars.PlaceObjectByName( "Mars" )
        pMars.UpdateNodeOnly()

        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pMars, 8.86e4, 5.94e7, pSun)

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pMars, "data/models/environment/Mars.nif", "Class-K")      

