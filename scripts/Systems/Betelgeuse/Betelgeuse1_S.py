import App
import loadspacehelper
import MissionLib
import Tactical.LensFlares

def Initialize(pSet):

	# Sun1
	pSun = App.Sun_Create(6350.0, 9150, 10000, "data/Textures/SunRed.tga", "data/Textures/Effects/SunFlaresRed.tga")
	pSet.AddObjectToSet(pSun, "Sun")
	
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Blue lens flare for Sun 1
	Tactical.LensFlares.RedOrangeLensFlare(pSet, pSun)

        #Planet 1
	pPlanet = App.Planet_Create(545.0, "data/models/environment/Venus.NIF")
	pSet.AddObjectToSet(pPlanet, "Betelgeuse 1")

	pPlanet.PlaceObjectByName("Planet Location")
	pPlanet.SetAtmosphereRadius(1.0)
	pPlanet.UpdateNodeOnly()
        #End Planet 1
        
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/Venus.NIF", "Class-N")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass         

        #Syrna, Inhabited
 	pMoon1 = App.Planet_Create(70.0, "data/models/environment/SFCIIRomulus.NIF")
	pSet.AddObjectToSet(pMoon1, "Syrna")
	
	pMoon1.PlaceObjectByName("Moon1 Location")
	pMoon1.UpdateNodeOnly()
	#End Syrna
	
        try:    
                import Custom.NanoFXv2.NanoFX_Lib
                Custom.NanoFXv2.NanoFX_Lib.CreateAtmosphereFX(pPlanet, "data/models/environment/SFCIIRomulus.NIF", "Class-M")        
        except ImportError:
                # Couldn't find NanoFx2.  That's ok.  Do nothing...
                pass  	

        #Asteroid Moon
 	pMoon2 = App.Planet_Create(10.0, "data/models/environment/asteroidh2.NIF")
	pSet.AddObjectToSet(pMoon2, "Asteroid Moon")
	
	pMoon2.PlaceObjectByName("Moon2 Location")
	pMoon2.UpdateNodeOnly()
	#End Asteroid Moon

        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
	        pHulk1		= loadspacehelper.CreateShip("Junk", pSet, "Alien Wreckage", "wreck")		
	        DamageWrecks(pHulk1)

def DamageWrecks(pHulk1):

	# Import our damaged script ship and apply it to the Hulk1
	pHulk1.SetHailable(0)
	import SpaceJunk
	SpaceJunk.AddDamage(pHulk1)
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