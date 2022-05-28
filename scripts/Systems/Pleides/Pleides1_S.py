import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun1
	pSun = App.Sun_Create(500.0, 700, 600, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	# Sun2
	pSun2 = App.Sun_Create(400.0, 600, 700, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 2
	Tactical.LensFlares.BlueLensFlare(pSet, pSun2)

	# Sun3
	pSun3 = App.Sun_Create(700.0, 900, 1100, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun3, "Sun3")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 3
	Tactical.LensFlares.BlueLensFlare(pSet, pSun3)

	# Sun4
	pSun4 = App.Sun_Create(300.0, 500, 600, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun4, "Sun4")
	
	# Place the object at the specified location.
	pSun4.PlaceObjectByName( "Sun4" )
	pSun4.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 4
	Tactical.LensFlares.BlueLensFlare(pSet, pSun4)

	# Sun5
	pSun5 = App.Sun_Create(250.0, 450, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun5, "Sun5")
	
	# Place the object at the specified location.
	pSun5.PlaceObjectByName( "Sun5" )
	pSun5.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 5
	Tactical.LensFlares.BlueLensFlare(pSet, pSun5)

	# Sun6
	pSun6 = App.Sun_Create(750.0, 950, 1200, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun6, "Sun6")
	
	# Place the object at the specified location.
	pSun6.PlaceObjectByName( "Sun6" )
	pSun6.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 6
	Tactical.LensFlares.BlueLensFlare(pSet, pSun6)

	# Sun7
	pSun7 = App.Sun_Create(950.0, 1150, 1100, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun7, "Sun7")
	
	# Place the object at the specified location.
	pSun7.PlaceObjectByName( "Sun7" )
	pSun7.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 7
	Tactical.LensFlares.BlueLensFlare(pSet, pSun7)

        # Sun8
	pSun8 = App.Sun_Create(200.0, 400, 500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun8, "Sun8")
	
	# Place the object at the specified location.
	pSun8.PlaceObjectByName( "Sun8" )
	pSun8.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 8
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun8)

        # Sun9
	pSun9 = App.Sun_Create(800.0, 1000, 1500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun9, "Sun9")
	
	# Place the object at the specified location.
	pSun9.PlaceObjectByName( "Sun9" )
	pSun9.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 9
	Tactical.LensFlares.YellowLensFlare(pSet, pSun9)

        # Sun10
	pSun10 = App.Sun_Create(300.0, 500, 700, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun10, "Sun10")
	
	# Place the object at the specified location.
	pSun10.PlaceObjectByName( "Sun10" )
	pSun10.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 10
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun10)

	# Sun11
	pSun11 = App.Sun_Create(6350.0, 7150, 8000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun11, "Sun11")
	
	# Place the object at the specified location.
	pSun11.PlaceObjectByName( "Sun11" )
	pSun11.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 11
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun11)

        #Planet 1
	pEridian = App.Planet_Create(85.0, "data/models/environment/BlackRookTerraformedMars.NIF")
	pSet.AddObjectToSet(pEridian, "Eridian")

	pEridian.PlaceObjectByName("Planet Location")
	pEridian.UpdateNodeOnly()
        #End Planet 1
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pEridian, "data/models/environment/BlackRookTerraformedMars.NIF", "Class-M")        
        except ImportError:
                # If NanoFx2 is not installed.  That's ok.  Do nothing...
                pass        


        #Nebula
        
	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(0.0 / 160.0, 40.0 / 100.0, 105.0 / 255.0, 14.0, 10.5, "data/Backgrounds/anomaly1.tga", "data/Backgrounds/anomaly1.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(20.0, 50.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (6000.0 in this case)
	pNebula.AddNebulaSphere(24000.0, 12500.0, 3000.0,  6000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
