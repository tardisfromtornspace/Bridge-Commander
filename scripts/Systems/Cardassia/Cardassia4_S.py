###############################################################################
#	Filename:	Cardassia4_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games
#	
#	Creates Cardassia 4 static objects.  Called by Cardassia4.py when region is created
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
	pCardassia4 = App.Planet_Create(728.91, "data/models/environment/YClass1.nif")
	pSet.AddObjectToSet(pCardassia4, "Cardassia 4 / Hutel") # Klasse M

	# Place the object at the specified location.
	pCardassia4.PlaceObjectByName( "Cardassia-4" )
	pCardassia4.SetAtmosphereRadius(0.01)
	pCardassia4.UpdateNodeOnly()

        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pCardassia4, "data/models/environment/YClass1.nif", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	