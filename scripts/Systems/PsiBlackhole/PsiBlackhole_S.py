from bcdebug import debug
###############################################################################
#	Filename:	Blackhole_S.py
#	
#	Confidential and Proprietary, Copyright 2007 by Fernando Aluani
#	
#	Creates Blackhole static objects.  Called by Blackhole.py when region is created
#	
#	Created:	10/02/01 - Tony Evans (Added Header)
#	Modified:	10/04/01 - Tony Evans
###############################################################################
import App
import Tactical.LensFlares
import loadspacehelper
import PsiBlackhole

def Initialize(pSet):
#	To create a colored sun:
#	pSun = App.Sun_Create(fRadius, fAtmosphereThickness, fDamagePerSec, fBaseTexture , fFlareTexture)
#
#	for fBaseTexture you can use:
#		data/Textures/SunBase.tga 
#		data/Textures/SunRed.tga
#		data/Textures/SunRedOrange.tga
#	for fFlareTexture you can use:
#		data/Textures/Effects/SunFlaresOrange.tga
#		data/Textures/Effects/SunFlaresRed.tga
#		data/Textures/Effects/SunFlaresRedOrange.tga

	# Create the sun
	debug(__name__ + ", Initialize")
	pSun = App.Sun_Create(1000.0, 1300, 450, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresWhite.tga")
	pSet.AddObjectToSet(pSun, "Psi Sun")
	
	# Place it at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()
	pSun.SetDensity(120.0)

	# Build a Blue lens flare, attached to the sun
	Tactical.LensFlares.BlueLensFlare(pSet, pSun)

	######
	# Create the Planet
	pPlanet = App.Planet_Create(180.0, "data/models/environment/BrownBluePlanet.nif")
	pSet.AddObjectToSet(pPlanet, "Psi Colony VIII")
	
	# Place the object at the specified location.
	pPlanet.PlaceObjectByName( "Planet Location" )
	pPlanet.UpdateNodeOnly()
	pPlanet.SetDensity(5.4)

	##########
	# try to create NanoFXv2 Atmospheres to the planet.
	try:
		import Custom.NanoFXv2.NanoFX_Lib
		Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/BrownBluePlanet.nif", "Class-M")
	except:
		pass

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create the blackhole
		pBlackhole = loadspacehelper.CreateShip("blackhole", pSet, "Psi\'s Blackhole", "Blackhole Start")
		# Set some of his attributes
		pBlackhole.SetInvincible(1)
		pBlackhole.SetHurtable(0)
		pBlackhole.SetTargetable(1)
		pBlackhole.SetScale(30.0)
		# Now set the Blackhole's rotation
		fSpeed = 360.0/3.5                           # Rotation speed, in degrees per seconds
		vVelocity = App.TGPoint3()
		vVelocity.SetXYZ(0.0, 1.0, 0.0)              # Rotation direction
		vVelocity.Unitize()
		vVelocity.Scale(fSpeed*App.HALF_PI/180.0)    # Convert fSpeed from degrees to radians (game works with)
		pBlackhole.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
		# Now if it's possible, make the player's sensors identify the blackhole. 
		# After all, all this map is about is the blackhole, so it's best to let the player know where it is right away
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			pSensors = pPlayer.GetSensorSubsystem()
			if pSensors:
				pSensors.ForceObjectIdentified(pBlackhole)
