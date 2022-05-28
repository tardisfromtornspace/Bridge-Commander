###############################################################################
#	Filename:	TheGalaxy7_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates TheGalaxy7 static objects.  Called by TheGalaxy7.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	09/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(400.0, 800, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Rogue Star")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        pObj = loadspacehelper.CreateShip ("Asteroidh1", pSet, "Unknown Debris", "Asteroid1")
	        if (pObj):
		        # Set objects Genus to Asteroid.
		        pProperty = pObj.GetShipProperty()
		        pProperty.SetGenus(App.GENUS_ASTEROID)

		        pObj.SetScale (9.0)
		        # Rotate object
		        vVelocity = App.TGPoint3_GetModelForward()	# Get the vector to rotate around
		        vVelocity.Scale( 10.0 * App.PI / 180.0 )		# Scale it to 10 degrees/second (converted to radians)
		        pObj.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
		        # The Core objects can't take damage from the nebula.
		        # Override the Environmental Damage handler for these.
		        pObj.AddPythonFuncHandlerForInstance(App.ET_ENVIRONMENT_DAMAGE, "MissionLib.IgnoreEvent")
