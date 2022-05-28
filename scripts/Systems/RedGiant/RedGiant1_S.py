import App
import Tactical.LensFlares

def Initialize(pSet):

	# Sun1
	pSun = App.Sun_Create(6500.0, 8000, 8500, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a White lens flare for this sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	# Sun2
	pSun2 = App.Sun_Create(120.0, 150, 500, "data/Textures/SunWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun2, "Sun2")
	
	# Place the object at the specified location.
	pSun2.PlaceObjectByName( "Sun2" )
	pSun2.UpdateNodeOnly()

	# Builds a White lens flare for this sun
	Tactical.LensFlares.WhiteLensFlare(pSet, pSun2)

	# Sun3
	pSun3 = App.Sun_Create(90.0, 120, 200, "data/Textures/SunBlack.tga", "data/Textures/Effects/SunFlaresBlack.tga")
	pSet.AddObjectToSet(pSun3, "Sun3")
	
	# Place the object at the specified location.
	pSun3.PlaceObjectByName( "Sun3" )
	pSun3.UpdateNodeOnly()

	# Builds a Black lens flare for Sun 3
	Tactical.LensFlares.BlackFlares(pSet, pSun3)