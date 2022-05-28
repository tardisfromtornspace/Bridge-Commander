###############################################################################
#	Filename:	Comet1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Comet 1 static objects.  Called by Comet1.py when region is created
#	
#	Created:	09/17/00 
#	Modified:	10/04/01 - Tony Evans
#	Modified:	03/15/02 - Ben Howard
###############################################################################
import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(800.0, 1200, 100, "data/Textures/SunDrkBlue.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Regula")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Red-Orange lens flare, attached to the sun
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                loadspacehelper.CreateShip("CardStarbase", pSet, "Observatory", "Station")
	
	        pObj = loadspacehelper.CreateShip ("Asteroid3", pSet, "Comet", "Sun")
	        if (pObj):
		        # Set objects Genus to Asteroid.
		        pProperty = pObj.GetShipProperty()
		        pProperty.SetGenus(App.GENUS_ASTEROID)

		        pObj.SetScale (9.0)
		        # Rotate object
		        vVelocity = App.TGPoint3_GetModelForward()	# Get the vector to rotate around
		        vVelocity.Scale( 15.0 * App.PI / 180.0 )		# Scale it to 10 degrees/second (converted to radians)
		        pObj.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
		        # The Core objects can't take damage from the nebula.
		        # Override the Environmental Damage handler for these.
		        pObj.AddPythonFuncHandlerForInstance(App.ET_ENVIRONMENT_DAMAGE, "MissionLib.IgnoreEvent")

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
        # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 50.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(10.0, 250.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(250.0, 2650.0, 300.0, 60.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 60.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(10.0, 150.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(190.0, 2700.0, 325.0, 75.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")

	pNebula3 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 70.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula3.SetupDamage(10.0, 90.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula3.AddNebulaSphere(120.0, 2775.0, 375.0, 100.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")

	pNebula4 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 80.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula4.SetupDamage(10.0, 60.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula4.AddNebulaSphere(40.0, 2875.0, 450.0, 130.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula4, "Nebula4")

	pNebula5 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 90.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula5.SetupDamage(10.0, 40.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula5.AddNebulaSphere(-50.0, 3000.0, 550.0, 160.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula5, "Nebula5")

	pNebula6 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 100.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula6.SetupDamage(10.0, 25.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula6.AddNebulaSphere(-150.0, 3150.0, 675.0, 180.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula6, "Nebula6")

	pNebula7 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 200.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula7.SetupDamage(10.0, 15.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula7.AddNebulaSphere(-260.0, 3325.0, 825.0, 200.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula7, "Nebula7")

	pNebula8 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 200.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula8.SetupDamage(10.0, 10.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula8.AddNebulaSphere(-380.0, 3525.0, 1000.0, 230.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula8, "Nebula8")

	pNebula9 = App.MetaNebula_Create(30.0 / 255.0, 40.0 / 255.0, 145.0  / 255.0, 200.0, 1.5, "data/Backgrounds/nebulaoverlayblue.tga", "data/Backgrounds/nebulaexternalblue.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula9.SetupDamage(10.0, 10.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula9.AddNebulaSphere(-510.0, 3750.0, 1200.0, 260.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula9, "Nebula9")
