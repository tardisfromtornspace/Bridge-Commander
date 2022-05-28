###############################################################################
#	Filename:	Void1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates TheGalaxy 3 static objects.  Called by Void1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	09/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper

def Initialize(pSet):
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        pObj = loadspacehelper.CreateShip ("Asteroidh1", pSet, "Debris", "Asteroid1")
	        if (pObj):
		        # Set objects Genus to Asteroid.
		        pProperty = pObj.GetShipProperty()
		        pProperty.SetGenus(App.GENUS_ASTEROID)

		        pObj.SetScale (9.0)
		        # Rotate object
		        vVelocity = App.TGPoint3_GetModelForward()	# Get the vector to rotate around
		        vVelocity.Scale( 10.0 * App.PI / 180.0 )		# Scale it to 10 degrees/second (converted to radians)
		        pObj.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
