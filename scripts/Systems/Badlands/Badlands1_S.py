import App
import loadspacehelper
import MissionLib
import SelfDefenseAI

def Initialize(pSet):

	pPlasma1 = App.Planet_Create(200.0, "data/models/environment/PlasmaTornadoG2.NIF")
	pSet.AddObjectToSet(pPlasma1, "Plasma1a")

	pPlasma1.PlaceObjectByName( "Plasma1" )
	pPlasma1.UpdateNodeOnly()

	pPlasma2 = App.Planet_Create(400.0, "data/models/environment/PlasmaTornadoG4.NIF")
	pSet.AddObjectToSet(pPlasma2, "Plasma1b")

	pPlasma2.PlaceObjectByName( "Plasma2" )
	pPlasma2.UpdateNodeOnly()

	pPlasma3 = App.Planet_Create(300.0, "data/models/environment/PlasmaTornadoG2.NIF")
	pSet.AddObjectToSet(pPlasma3, "Plasma1c")

	pPlasma3.PlaceObjectByName( "Plasma3" )
	pPlasma3.UpdateNodeOnly()

	pPlasma4 = App.Planet_Create(200.0, "data/models/environment/PlasmaTornadoG3.NIF")
	pSet.AddObjectToSet(pPlasma4, "Plasma2a")

	pPlasma4.PlaceObjectByName( "Plasma4" )
	pPlasma4.UpdateNodeOnly()

	pPlasma5 = App.Planet_Create(300.0, "data/models/environment/PlasmaTornadoG4.NIF")
	pSet.AddObjectToSet(pPlasma5, "Plasma2b")

	pPlasma5.PlaceObjectByName( "Plasma5" )
	pPlasma5.UpdateNodeOnly()

	pPlasma6 = App.Planet_Create(200.0, "data/models/environment/PlasmaTornadoG2.NIF")
	pSet.AddObjectToSet(pPlasma6, "Plasma2c")

	pPlasma6.PlaceObjectByName( "Plasma6" )
	pPlasma6.UpdateNodeOnly()

	pPlasma7 = App.Planet_Create(400.0, "data/models/environment/PlasmaTornadoG4.NIF")
	pSet.AddObjectToSet(pPlasma7, "Plasma3a")

	pPlasma7.PlaceObjectByName( "Plasma7" )
	pPlasma7.UpdateNodeOnly()

	pPlasma8 = App.Planet_Create(200.0, "data/models/environment/PlasmaTornadoG2.NIF")
	pSet.AddObjectToSet(pPlasma8, "Plasma3b")

	pPlasma8.PlaceObjectByName( "Plasma8" )
	pPlasma8.UpdateNodeOnly()

	pPlasma9 = App.Planet_Create(400.0, "data/models/environment/PlasmaTornadoG4.NIF")
	pSet.AddObjectToSet(pPlasma9, "Plasma3c")

	pPlasma9.PlaceObjectByName( "Plasma9" )
	pPlasma9.UpdateNodeOnly()

	pPlasma10 = App.Planet_Create(200.0, "data/models/environment/PlasmaTornadoG3.NIF")
	pSet.AddObjectToSet(pPlasma10, "Plasma4a")

	pPlasma10.PlaceObjectByName( "Plasma10" )
	pPlasma10.UpdateNodeOnly()

	pPlasma11 = App.Planet_Create(300.0, "data/models/environment/PlasmaTornadoG2.NIF")
	pSet.AddObjectToSet(pPlasma11, "Plasma4b")

	pPlasma11.PlaceObjectByName( "Plasma11" )
	pPlasma11.UpdateNodeOnly()

	pPlasma12 = App.Planet_Create(400.0, "data/models/environment/PlasmaTornadoG3.NIF")
	pSet.AddObjectToSet(pPlasma12, "Plasma4c")

	pPlasma12.PlaceObjectByName( "Plasma12" )
	pPlasma12.UpdateNodeOnly()

	pPlasma13 = App.Planet_Create(200.0, "data/models/environment/PlasmaTornadoG2.NIF")
	pSet.AddObjectToSet(pPlasma13, "Plasma5a")

	pPlasma13.PlaceObjectByName( "Plasma13" )
	pPlasma13.UpdateNodeOnly()

	pPlasma14 = App.Planet_Create(500.0, "data/models/environment/PlasmaTornadoG4.NIF")
	pSet.AddObjectToSet(pPlasma14, "Plasma5b")

	pPlasma14.PlaceObjectByName( "Plasma14" )
	pPlasma14.UpdateNodeOnly()

	pPlasma15 = App.Planet_Create(500.0, "data/models/environment/PlasmaTornadoG3.NIF")
	pSet.AddObjectToSet(pPlasma15, "Plasma5c")

	pPlasma15.PlaceObjectByName( "Plasma15" )
	pPlasma15.UpdateNodeOnly()


	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
   	 # name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(245.0 / 255.0, 90.0 / 255.0, 105.0 / 105.0, 625.0, 10.5, "data/Backgrounds/plasma.tga", "data/Backgrounds/plasma.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(15.0, 20.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (3300.0 in this case)
	pNebula.AddNebulaSphere(0.0, -5000.0, 0.0,  3400.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")

	# Create Ships
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		pKeldonClass		= loadspacehelper.CreateShip("Keldon", pSet, "Keldon Class", "Keldon Locale")
		pKeldonClass.SetAI(SelfDefenseAI.CreateAI(pKeldonClass))
        
		pKeldonClass2		= loadspacehelper.CreateShip("Keldon", pSet, "Another Keldon", "Keldon2 Locale")
		pKeldonClass2.SetAI(SelfDefenseAI.CreateAI(pKeldonClass2))
        
		pHulk1		= loadspacehelper.CreateShip("Galor", pSet, "Cardassian Galor", "wreck")		
		DamageWrecks(pHulk1)


def DamageWrecks(pHulk1):

	# Import our damaged script ship and apply it to the Hulk1
	pHulk1.SetHailable(0)
	import DamGalor
	DamGalor.AddDamage(pHulk1)
	# Turn off the ships repair
	pRepair = pHulk1.GetRepairSubsystem()
	pProp 	= pRepair.GetProperty()
	pProp.SetMaxRepairPoints(0.0)
	# Damage the Hulk1...
	# Turn off the shields
	pAlertEvent = App.TGIntEvent_Create()
	pAlertEvent.SetDestination(pHulk1)
	pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	pAlertEvent.SetInt(pHulk1.GREEN_ALERT)
	App.g_kEventManager.AddEvent(pAlertEvent)
	# Damage the hull - 500 pts left
	pHulk1.DamageSystem(pHulk1.GetHull(), 3500)
	pHulk1.DisableGlowAlphaMaps()
	# Dont allow the user to see the sub-systems
	MissionLib.HideSubsystems(pHulk1)
	# Spin the hulk
	MissionLib.SetRandomRotation(pHulk1, 10)
	# The Core objects can't take damage from the nebula.
	# Override the Environmental Damage handler for these.
	pHulk1.AddPythonFuncHandlerForInstance(App.ET_ENVIRONMENT_DAMAGE, "MissionLib.IgnoreEvent")