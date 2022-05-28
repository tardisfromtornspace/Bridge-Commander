###############################################################################
#	Filename:	Cardassia7_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 7 static objects.  Called by Cardassia7.py when region is created
#	
#	Created:	10/04/01 - Tony Evans (Added Header)
#	Modified:	08/11/04 - Klaus Kann
###############################################################################
import App
import Tactical.LensFlares

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(240000.0, 45000.0, 500, "data/Textures/SunRedOrange.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

	######
	# Create the Planet
	pCardassia7 = App.Planet_Create(388.23, "data/models/environment/Mercury.nif")
	pSet.AddObjectToSet(pCardassia7, "Cardassia 7") # Klasse Q

	# Place the object at the specified location.
	pCardassia7.PlaceObjectByName( "Cardassia-7" )
	pCardassia7.UpdateNodeOnly()
