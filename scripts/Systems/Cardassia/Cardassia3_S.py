###############################################################################
#	Filename:	Cardassia3_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 3 static objects.  Called by Cardassia3.py when region is created
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
	pCardassia3 = App.Planet_Create(388.23, "data/models/environment/FClass1.nif")
	pSet.AddObjectToSet(pCardassia3, "Cardassia 3") # Klasse M

	# Place the object at the specified location.
	pCardassia3.PlaceObjectByName( "Cardassia-3" )
	pCardassia3.SetAtmosphereRadius(0.01)
	pCardassia3.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia3, "data/models/environment/FClass1.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass 