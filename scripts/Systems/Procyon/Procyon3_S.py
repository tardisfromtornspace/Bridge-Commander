import App
import Tactical.LensFlares

def Initialize(pSet):
	pSun = App.Sun_Create(300.0, 400, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Blue Star")

	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	pSun2 = App.Sun_Create(1100.0, 2000, 2500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun2, "Red Star")
	
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a Redorange lens flare for Sun 2
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun2)

