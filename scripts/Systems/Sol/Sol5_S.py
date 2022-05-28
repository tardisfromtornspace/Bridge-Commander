from bcdebug import debug
###############################################################################
#       Filename:       Sol5_S.py
#
#       Confidential and Proprietary, Copyright 2001 by Totally Games
#
#       Creates Sol 5 static objects.  Called by Sol5.py when region is created
#
#       Created:        10/04/01 - Tony Evans (Added Header)
#       Modified:       10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares
import Systems.FoundationUtils

def Initialize(pSet):

        # 778 million km from the sun

        # Add a sun, far far away
        debug(__name__ + ", Initialize")
        pSun = App.Sun_Create(79428.57, 14000.0, 500, "data/Textures/SunBase.tga", "data/Textures/Effects/SunFlaresYellow.tga")
        pSet.AddObjectToSet(pSun, "Sun")

        # Place the object at the specified location.
        pSun.PlaceObjectByName( "Sun" )
        pSun.UpdateNodeOnly()

        ######
        # Create the Planet - 142,984 km diameter
        pJupiter = App.Planet_Create(8170.51, "data/models/environment/Jupiter.nif")
        pSet.AddObjectToSet(pJupiter, "Jupiter")

        # Place the object at the specified location.
        # pJupiter.ReplaceTexture("data/models/environment/Jupiter.tga", "Generic")
        # pJupiter.SetCollisionFlags(0)
        pJupiter.SetAtmosphereRadius(0.01)
        pJupiter.PlaceObjectByName( "Jupiter" )
        pJupiter.UpdateNodeOnly()

        import Custom.QBautostart.Libs.LibPlanet
        global pPlanetRotation
        pPlanetRotation = Custom.QBautostart.Libs.LibPlanet.Rotate(pJupiter, 3.57e4, 3.74e8, pSun)

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pJupiter, "data/models/environment/Jupiter.nif", "Class-K")        


        # coord = Systems.FoundationUtils.Sol_JupiterCoord

        # # MetaNebula_Create params are:
        # # r, g, b : (floats [0.0 , 1.0])
        # # visibility distance inside the nebula (float in world units)
        # # sensor density of nebula(value to scale sensor range by)
    # # name of internal texture (needs alpha)
        # # name of external texture (no need for alpha)

        # pNebula = App.MetaNebula_Create(0.82, 0.41, 0.3, 40.0, 10.5, "data/Backgrounds/nebulaoverlay.tga", "data/models/environment/Jupiter.tga")
        # # Set nebula damage/sec to Hull/Shields.
        # pNebula.SetupDamage(200.0, 100.0)
        # # Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
        # pNebula.AddNebulaSphere(coord[0], coord[1], coord[2], 8150.0)
        # # Puts the nebula in the set
        # pSet.AddObjectToSet(pNebula, "Nebula1")


        ######
        # Create the Planet - 3,630 km diameter
        pIo = App.Planet_Create(207.43, "data/models/environment/Io.nif")
        pSet.AddObjectToSet(pIo, "Io")

        # Place the object at the specified location.
        pIo.PlaceObjectByName( "Io" )
        pIo.UpdateNodeOnly()
        pIo.SetAtmosphereRadius(0.01)

        ######
        # Create the Planet - 3,183 km diameter
        pEuropa = App.Planet_Create(179.31, "data/models/environment/Europa.nif")
        pSet.AddObjectToSet(pEuropa, "Europa")

        # Place the object at the specified location.
        pEuropa.PlaceObjectByName( "Europa" )
        pEuropa.UpdateNodeOnly()
        pEuropa.SetAtmosphereRadius(0.01)

        ######
        # Create the Planet - 5,262 km diameter
        pGanymede = App.Planet_Create(300.69, "data/models/environment/Ganymede.nif")
        pSet.AddObjectToSet(pGanymede, "Ganymede")

        # Place the object at the specified location.
        pGanymede.PlaceObjectByName( "Ganymede" )
        pGanymede.UpdateNodeOnly()
        pGanymede.SetAtmosphereRadius(0.01)

        try:    
                import Custom.NanoFXv2.NanoFX_Lib                 
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
               pass
        else:
               Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pGanymede, "data/models/environment/Ganymede.nif", "Class-K")      

        ######
        # Create the Planet - 4,800 km diameter
        pCallisto = App.Planet_Create(274.29, "data/models/environment/Callisto.nif")
        pSet.AddObjectToSet(pCallisto, "Callisto")

        # Place the object at the specified location.
        pCallisto.PlaceObjectByName( "Callisto" )
        pCallisto.UpdateNodeOnly()
        pCallisto.SetAtmosphereRadius(0.01)

