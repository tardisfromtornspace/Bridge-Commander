import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

	# This script was a pain in the patooty but worth it I think.
	# Some way of being able to look at all this in 3D to map it out would be nice.
	# The Placement Editor in the Console is a bit on the weak side but helpful, some.
	# Febuary 15-18, 2003 Zorg/Morpheus

        # Sun1
	pSun = App.Sun_Create(19500.0, 20000, 22500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.DimBlueFlares(pSet, pSun)

	pPlanet = App.Planet_Create(275.0, "data/models/environment/AquaPlanet.NIF")
	pSet.AddObjectToSet(pPlanet, "Hakares 1, (Class O)")

	pPlanet.PlaceObjectByName("Planet1")
	pPlanet.UpdateNodeOnly()

	pMoon1 = App.Planet_Create(75.0, "data/models/environment/BrownPlanet.NIF")
	pSet.AddObjectToSet(pMoon1, "Hakares, Moon 1 (Class D)")

	pMoon1.PlaceObjectByName("Moon1")
	pMoon1.UpdateNodeOnly()

	pMoon2 = App.Planet_Create(55.0, "data/models/environment/SlimeGreenPlanet.NIF")
	pSet.AddObjectToSet(pMoon2, "Hakares, Moon 2 (Class N)")

	pMoon2.PlaceObjectByName("Moon2")
	pMoon2.UpdateNodeOnly()

#Nebula info reads (R,G,B, Vision-distance, Sensor interference, "neblua texture", "nebula external texture")

	# First Set (Middle)
	# Left1
	pNebula = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 180.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula.SetupDamage(5.0, 10.0)

	pNebula.AddNebulaSphere(2200.0, 0.0, 0.0, 1200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")

	# Right1
        pNebula2 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 200.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula2.SetupDamage(5.0, 10.0)

	pNebula2.AddNebulaSphere(-2200.0, 0.0, 0.0, 1200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")

	# Top1
        pNebula3 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 200.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula3.SetupDamage(5.0, 10.0)

	pNebula3.AddNebulaSphere(0.0, 0.0, 2200.0, 1200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")

	# Bottom1
        pNebula4 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 180.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula4.SetupDamage(5.0, 10.0)

	pNebula4.AddNebulaSphere(0.0, 0.0, -2200.0, 1200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula4, "Nebula4")

	# Second Set (End)
	# Left2
	pNebula5 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 250.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula5.SetupDamage(5.0, 10.0)

	pNebula5.AddNebulaSphere(1400.0, 1500.0, 0.0, 1600.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula5, "Nebula5")

	# Right2
        pNebula6 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 180.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula6.SetupDamage(5.0, 10.0)

	pNebula6.AddNebulaSphere(-1400.0, 1500.0, 0.0, 1600.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula6, "Nebula6")

	# Top2
        pNebula7 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 255.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula7.SetupDamage(5.0, 10.0)

	pNebula7.AddNebulaSphere(0.0, 2000.0, 1400.0, 1700.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula7, "Nebula7")

	# Bottom2
        pNebula8 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 200.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula8.SetupDamage(5.0, 10.0)

	pNebula8.AddNebulaSphere(0.0, 2000.0, -1400.0, 1700.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula8, "Nebula8")

	# Third Set (End)
	# Left3
	pNebula9 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 250.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula9.SetupDamage(5.0, 10.0)

	pNebula9.AddNebulaSphere(1200.0, -1500.0, 0.0, 1600.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula9, "Nebula9")

	# Right3
        pNebula10 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 200.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula10.SetupDamage(5.0, 10.0)

	pNebula10.AddNebulaSphere(-1200.0, -1500.0, 0.0, 1600.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula10, "Nebula10")

	# Top3
        pNebula11 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 255.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula11.SetupDamage(5.0, 10.0)

	pNebula11.AddNebulaSphere(0.0, -1500.0, 1200.0, 1700.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula11, "Nebula11")

	# Bottom3
        pNebula12 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 180.0, 5.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula12.SetupDamage(5.0, 10.0)

	pNebula12.AddNebulaSphere(0.0, -1500.0, -1200.0, 1700.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula12, "Nebula12")

	# End1
	pNebula13 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 250.0, 2.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula13.SetupDamage(5.0, 10.0)

	pNebula13.AddNebulaSphere(0.0, 2000.0, 0.0, 1000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula13, "Nebula13")

	# End2
	pNebula14 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 245.0, 2.5, "data/Backgrounds/nebulaoverlay.tga", "data/Backgrounds/nebulaexternal.tga")
	pNebula14.SetupDamage(5.0, 10.0)

	pNebula14.AddNebulaSphere(0.0, -2000.0, 0.0, 1000.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula14, "Nebula14")

        # Subspace Rift
	pNebula15 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 200.0, 10.5, "data/Backgrounds/rift.tga", "data/Backgrounds/rift.tga")
	pNebula15.SetupDamage(450.0, 2500.0)

	pNebula15.AddNebulaSphere(1500.0, 650.0, 950.0, 350.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula15, "Nebula15")

        # Distortion Field
	pNebula16 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 200.0, 10.5, "data/Backgrounds/anomaly1a.tga", "data/Backgrounds/anomaly1a.tga")
	pNebula16.SetupDamage(250.0, 1500.0)

	pNebula16.AddNebulaSphere(-1800.0, -250.0, -1250.0, 850.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula16, "Nebula16")

        # Hidden1 You don't wanna hit this by mistake, ouch!
	pNebula17 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 10.0, 14.5, "data/Backgrounds/anomaly1a.tga", "data/Backgrounds/anomaly1a.tga")
	pNebula17.SetupDamage(500.0, 3000.0)

	pNebula17.AddNebulaSphere(200.0, -850.0, 200.0, 200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula17, "Nebula17")

        # Hidden2 Nebulas!  How bout some more Nebulas!  I loooovvvee Nebulas!  Approaching too many though!
	pNebula18 = App.MetaNebula_Create(100.0 / 255.0, 99.0 / 255.0, 146.0 / 255.0, 10.0, 14.5, "data/Backgrounds/anomaly1a.tga", "data/Backgrounds/anomaly1a.tga")
	pNebula18.SetupDamage(500.0, 3000.0)

	pNebula18.AddNebulaSphere(-500.0, -800.0, -225.0, 200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula18, "Nebula18")


