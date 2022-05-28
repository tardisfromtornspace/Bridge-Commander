from bcdebug import debug
###############################################################################
#       Filename:       Sol7_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 5 static objects.  Called by Sol7.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

        # 2.9 billion km from the sun

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        ######
        # Create the Planet - 51,118 km diameter
        pUranus = App.Planet_Create(2921.03, "data/models/environment/Uranus.nif")
        pSet.AddObjectToSet(pUranus, "Uranus")

        # Place the object at the specified location.
        pUranus.PlaceObjectByName( "Uranus" )
        pUranus.SetAtmosphereRadius(0.01)
        pUranus.UpdateNodeOnly()

        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pUranus, 6.21e4, 2.64e9, pSun)

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pUranus, "data/models/environment/Uranus.nif", "Class-K")  

        pAriel = App.Planet_Create(66.16, "data/models/environment/Ariel.nif")
        pSet.AddObjectToSet(pAriel, "Ariel")

        # Place the object at the specified location.
        pAriel.PlaceObjectByName( "Ariel" )
        pAriel.SetAtmosphereRadius(0.01)
        pAriel.UpdateNodeOnly()

        pUmbriel = App.Planet_Create(66.82, "data/models/environment/Umbriel.nif")
        pSet.AddObjectToSet(pUmbriel, "Umbriel")

        # Place the object at the specified location.
        pUmbriel.PlaceObjectByName( "Umbriel" )
        pUmbriel.SetAtmosphereRadius(0.01)
        pUmbriel.UpdateNodeOnly()

        pTitania = App.Planet_Create(90.17, "data/models/environment/Titania.nif")
        pSet.AddObjectToSet(pTitania, "Titania")

        # Place the object at the specified location.
        pTitania.PlaceObjectByName( "Titania" )
        pTitania.SetAtmosphereRadius(0.01)
        pTitania.UpdateNodeOnly()

        pOberon = App.Planet_Create(87.02, "data/models/environment/Oberon.nif")
        pSet.AddObjectToSet(pOberon, "Oberon")

        # Place the object at the specified location.
        pOberon.PlaceObjectByName( "Oberon" )
        pOberon.SetAtmosphereRadius(0.01)
        pOberon.UpdateNodeOnly()

