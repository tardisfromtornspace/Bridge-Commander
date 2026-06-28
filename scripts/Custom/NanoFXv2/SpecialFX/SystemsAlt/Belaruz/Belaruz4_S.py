import App
import loadspacehelper
import MissionLib
import traceback

def Initialize(pSet):

	import Systems.Belaruz.Belaruz4
	pBelaruz4 = Systems.Belaruz.Belaruz4.GetSet()

	################
	# Create the Planet
	################
#	print ("Putting in the planet.\n")
	pBelaruzPlanet = App.Planet_Create(180.0, "data/Models/Environment/K-Class.nif")
	pSet.AddObjectToSet(pBelaruzPlanet, "Belaruz 4")

	#Place the object at the specified location.
	pBelaruzPlanet.PlaceObjectByName( "Belaruz4" )
	pBelaruzPlanet.UpdateNodeOnly()

	import Custom.NanoFXv2.NanoFX_Lib
	Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereALT(pBelaruzPlanet, "data/Models/Environment/K-Class.nif", "data/Models/Environment/K-Class.nif", "K-Class") # TO-DO the second "K-Class.nif" should be "Y-CloudsHi.nif", but I cannot find that on my install

	pNebula = App.MetaNebula_Create(255.0 / 255.0, 255.0 / 255.0, 255.0  / 255.0, 250.0, 10.5, "data/Backgrounds/High/treknebula0.tga", "data/Backgrounds/High/treknebula0.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(1.0, 5.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(100, 10000, 500.0,  2500.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula Sphere")

	shouldWeSpin = 0
	try:
		from Custom.NanoFXv2.SpecialFX.AtmosphereALT import AddRotatingBody
		AddRotatingBody(pNebula, 0.0005)
		shouldWeSpin = 1
	except:
		shouldWeSpin = 0
		traceback.print_exc()

	#########
	# Create the asteroids and make them rotate randomly

	# pBelaruzRing = App.Planet_Create(360.0, "data/models/environment/planet/TethysGasRings1.nif")
	# pSet.AddObjectToSet(pBelaruzRing, "Ring Planet")

	#Place the object at the specified location.
	# pBelaruzRing.UpdateNodeOnly()
	# pBelaruzPlanet.AttachObject(pBelaruzRing)
	#########

	#Get the asteroid model
#	print ("Putting in the asteroid.\n")
	
	import ships.Asteroid
	ships.Asteroid.LoadModel ()

#	App.g_kModelManager.LoadModel('data/models/misc/Asteroids/asteroid.nif', None)

	# Only create system stuff if not multiplayer or is the host in multiplayer
	if (App.g_kUtopiaModule.IsMultiplayer () == 0 or App.g_kUtopiaModule.IsHost () == 1):
#		print ("Placing asteroids.\n")
		#Create the asteroids for Belaruz4
		for sAsteroidName, sPlacementName in ( 
			("Asteroid 1", "Asteroid1"),
			("Asteroid 2", "Asteroid2"),
			("Asteroid 3", "Asteroid3"),
			("Asteroid 4", "Asteroid4"),
			("Asteroid 5", "Asteroid5"),
			("Asteroid 6", "Asteroid6"),
			("Asteroid 7", "Asteroid7")):
	#		pModel = App.g_kModelManager.CloneModel('data/models/misc/Asteroids/asteroid.nif' )
	#		pModel.SetScale(0.1) 
	#		if (pModel == None):
	#			print("Unable to create asteroid; couldn't load model.")
	#		else:

			pAsteroid = loadspacehelper.CreateShip("Asteroid", pBelaruz4, sAsteroidName, sPlacementName)

			if (pAsteroid):
				pAsteroid.SetHailable(0)
				pAsteroid.SetTargetable(0)
				pAsteroid.SetScannable(0)

				#Rotate the asteroid
				vVelocity = App.TGPoint3_GetModelForward()	# Get the vector to rotate around
				vVelocity.Scale( 10.0 * App.PI / 180.0 )		# Scale it to 10 degrees/second (converted to radians)
				pAsteroid.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
