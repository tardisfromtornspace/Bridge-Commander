from bcdebug import debug
###############################################################################
#       Filename:       Sol6_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 5 static objects.  Called by Sol6.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

        # 1.43 billion km from the sun

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        ######
        # Create the Planet - 120,536 km diameter
        # Especially high diameter to compensate for the rings - not sure of this scaling.
        pSaturn = App.Planet_Create(14691.49, "data/models/environment/Saturn.nif")
        pSet.AddObjectToSet(pSaturn, "Saturn")

        # Place the object at the specified location.
        pSaturn.PlaceObjectByName( "Saturn" )
        pSaturn.SetAtmosphereRadius(0.01)
        pSaturn.UpdateNodeOnly()

        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pSaturn, 3.84e4, 9.29e8, pSun)
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pSaturn, "data/models/environment/Saturn.nif", "Class-K")  

        pTethys = App.Planet_Create(60.57, "data/models/environment/Tethys.nif")
        pSet.AddObjectToSet(pTethys, "Tethys")

        # Place the object at the specified location.
        pTethys.PlaceObjectByName( "Tethys" )
        pTethys.SetAtmosphereRadius(0.01)
        pTethys.UpdateNodeOnly()

        pDione = App.Planet_Create(64.00, "data/models/environment/Dione.nif")
        pSet.AddObjectToSet(pDione, "Dione")

        # Place the object at the specified location.
        pDione.PlaceObjectByName( "Dione" )
        pDione.SetAtmosphereRadius(0.01)
        pDione.UpdateNodeOnly()

        pRhea = App.Planet_Create(87.43, "data/models/environment/Rhea.nif")
        pSet.AddObjectToSet(pRhea, "Rhea")

        # Place the object at the specified location.
        pRhea.PlaceObjectByName( "Rhea" )
        pRhea.SetAtmosphereRadius(0.01)
        pRhea.UpdateNodeOnly()

        pTitan = App.Planet_Create(294.29, "data/models/environment/Titan.nif")
        pSet.AddObjectToSet(pTitan, "Titan")

        # Place the object at the specified location.
        pTitan.PlaceObjectByName( "Titan" )
        pTitan.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pTitan, "data/models/environment/Titan.nif", "Class-K")    

