###############################################################################
#	Filename:	Cardassia2_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 2 static objects.  Called by Cardassia2.py when region is created
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
	pCardassia2 = App.Planet_Create(278.80, "data/models/environment/Io.nif")
	pSet.AddObjectToSet(pCardassia2, "Cardassia 2") # Klasse B

	# Place the object at the specified location.
	pCardassia2.PlaceObjectByName( "Cardassia-2" )
	pCardassia2.SetAtmosphereRadius(0.001)	
	pCardassia2.UpdateNodeOnly()
	
#        try:    
#                import Custom.NanoFXv2.NanoFX_Lib
#                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia2, "data/models/environment/Io.nif", "Class-B")        
#        except ImportError:
#                # Couldn't find NanoFx2.  That's ok.  Do nothing...
#                pass  	
