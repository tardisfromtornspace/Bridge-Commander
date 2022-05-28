from bcdebug import debug
import App
import loadspacehelper
import MissionLib
import string
import imp

#im not happy, but i gotta make the core name global. its just the rules
g_CoreName = ""

#this is for chucking the core straight outta the ship. fwoomp!
def DumpIt():
	# grab some values, these are used later and throughout
	debug(__name__ + ", DumpIt")
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	# grab position points
	pPlayerForward = pPlayer.GetWorldForwardTG()
	pPlayerUp = pPlayer.GetWorldUpTG()
	# take the world location of the core, man! THE CORE!!!
	vLocation = pPlayer.GetPowerSubsystem().GetWorldLocation()

	#grab the future name of the core
	pShipName = string.split(pPlayer.GetScript(), ".")
	pCoreName = pShipName[-1] + " Core"
	global g_CoreName
	g_CoreName = pCoreName

	# okay, check to see what core we should use!
	# galaxy core
	if (pPlayer.GetScript() == "ships.MvamGalaxy" or pPlayer.GetScript() == "ships.Galaxy" or pPlayer.GetScript() == "ships.MvamGalaxyStardrive"):
		pCore = loadspacehelper.CreateShip("Galaxycore", pSet, pCoreName, "")
		pCoreHp = "Galaxycore"
	# intrepid core
	elif (pPlayer.GetScript() == "ships.Intrepid"):
		pCore = loadspacehelper.CreateShip("Intcore", pSet, pCoreName, "")
		pCoreHp = "Intcore"
	# small sov core
	elif (pPlayer.GetRadius() <= 1.0):
		pCore = loadspacehelper.CreateShip("Smallcore", pSet, pCoreName, "")
		pCoreHp = "Smallcore"
	#misc (sovvy) core
	else:
		pCore = loadspacehelper.CreateShip("Warpcore", pSet, pCoreName, "")
		pCoreHp = "Warpcore"

	# grab the position of the core
	kPoint1 = App.TGPoint3()
	kPoint1.Set(vLocation)
	pCore.SetTranslate(kPoint1)
	pCore.AlignToVectors(pPlayerForward, pPlayerUp)

	#add the core to the friendly group and uhh... thats all. oh yeah, disable collisions. nah, forget the group
	pCore.EnableCollisionsWith(pPlayer, 0)

	# set up impulse speed
	vImpPoint = App.TGPoint3()
	vImpPoint.SetXYZ(0.0, 0.0, -1.0)
	pCore.SetImpulse(0.9, vImpPoint, App.ShipClass.DIRECTION_MODEL_SPACE)

	############## Load hardpoints....this is messed up argh
	# grab the player power system
	pPlayerPower = pPlayer.GetPowerSubsystem()

	#get player and core hardpoint names
	pPlayerHp = App.Game_GetPlayerHardpointFileName()
	try:
		mod = __import__("ships.Hardpoints." + pPlayerHp)
		modCore = __import__("ships.Hardpoints." + pCoreHp)
	except ImportError:
		return

	# get the property sets... im not sure if the rest is relevant
	pShipSet = pPlayer.GetPropertySet()
	pCoreSet = pPlayer.GetPropertySet()
	reload (mod)
	reload (modCore)

	# Grab all subsystems
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pCoreList = pCoreSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	# lets go through all the core items till we find that hardpoint
	pCoreList.TGBeginIteration()
	for i in range(pCoreList.TGGetNumItems()):
		pCoreProperty = App.SubsystemProperty_Cast(pCoreList.TGGetNext().GetProperty())
		pSubsystem = pCore.GetSubsystemByProperty(pCoreProperty)

		if (pSubsystem != None):
			# okay, lets do a couple if's to see if we have the power core
			if (pSubsystem.GetName() == "HullStore"):
				pCoreProperty.SetMaxCondition(pPlayerPower.GetMaxCondition())
				pSubsystem.SetCondition(pPlayerPower.GetCondition())

	#lets go through all the player items till we find the core
	pShipList.TGBeginIteration()
	for i in range(pShipList.TGGetNumItems()):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

		if (pSubsystem != None):
			# okay, lets do a couple if's to see if we have the power core
			if (pSubsystem.GetName() == "Warp Core"):
				pShipProperty.SetCritical(0)
				pShipProperty.SetTargetable(0)
				pSubsystem.SetCondition(0)
			# find the nacelles and disable them so we cant warp without a core
			if (pSubsystem.IsTypeOf(App.CT_WARP_ENGINE_SUBSYSTEM)):
				pShipProperty.SetDisabledPercentage(100)

	pShipList.TGDoneIterating()
	pShipList.TGDestroy()
	pCoreList.TGDoneIterating()
	pCoreList.TGDestroy()
	######### end loading hardpoints

	#lets flicker those ship lights!
	try:
		import Custom.NanoFX.NanoFX_Lib
		pSequence = App.TGSequence_Create()
		pSequence.AddAction(Custom.NanoFX.NanoFX_Lib.CreateFlickerSeq(pPlayer, 3.0, sStatus = "Off"))
		pSequence.Play()
	except:
		#it failed. dont worry about it, it means the user doesnt have nanofx 2.0
		novalue = "crap"

	# put em all in the proxy manager, so we can AHHH LOOK OUT!
	pProximityManager = pSet.GetProximityManager()
	if (pProximityManager):
		pProximityManager.UpdateObject (pCore)
	# update all ships with all these purdy changes
	pCore.UpdateNodeOnly()

	# we need this for use in a timer. the core is going real fast right now so i gotta stop it in a second
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "CreateSound"))
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ChangeImpulse", pCore), 3.0)
	MissionLib.QueueActionToPlay(pSeq)

	# okayyy, its time to set up the event handlers for core retrieval
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_BEAM_STARTED_HITTING, pMission, __name__ + ".TractorCore")

	return


def CreateSound (pAction):
	# grab some values
	debug(__name__ + ", CreateSound")
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	# play a sound sequence
	pSoundSeq = App.TGSequence_Create()
	pSound = App.TGSoundAction_Create("Death Explosion 1", 0, pSet.GetName())
	pSound.SetNode(pPlayer.GetNode())
	pSoundSeq.AddAction(pSound)
	pSoundSeq.Play()
	#play another
	pSoundSeq2 = App.TGSequence_Create()
	pSound2 = App.TGSoundAction_Create("CoreEject", 0, pSet.GetName())
	pSound2.SetNode(pPlayer.GetNode())
	pSoundSeq2.AddAction(pSound2)
	pSoundSeq2.Play()

	return 0



def ChangeImpulse (pAction, pCore):
	# grab some values
	debug(__name__ + ", ChangeImpulse")
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	# set up impulse speed
	vImpPoint = App.TGPoint3()
	vImpPoint.SetXYZ(0.0, 0.0, -1.0)
	pCore.SetImpulse(0.1, vImpPoint, App.ShipClass.DIRECTION_MODEL_SPACE)

	# allow the core to be able to hit the player
	pCore.EnableCollisionsWith(pPlayer, 1)

	return 0


# plays when the tractor beam is fired
def TractorCore(TGObject, pEvent):
	# grab some values
	debug(__name__ + ", TractorCore")
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	#grab the core name
	global g_CoreName

	# Get the event destination (the thing hit by tractor beam)
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if ((pShip == None) or (pShip.GetName() != g_CoreName)):
		TGObject.CallNextHandler(pEvent)
		return
	pCoreName = pShip.GetName()
		
	# Get the tractor beam system that fired so we can set it's behavior.
	pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
	pTractorSystem = App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
	
	# Get the name of the ship that fired
	pShip = pTractorSystem.GetParentShip()
	if ((pShip == None) or (pShip.GetName() != pPlayer.GetName())):
		TGObject.CallNextHandler(pEvent)
		return

	############## Load hardpoints....this is messed up argh
	#get player and core hardpoint names
	pPlayerHp = App.Game_GetPlayerHardpointFileName()
	try:
		mod = __import__("ships.Hardpoints." + pPlayerHp)
	except ImportError:
		TGObject.CallNextHandler(pEvent)
		return

	# get the property sets... im not sure if the rest is relevant
	pShipSet = pPlayer.GetPropertySet()
	reload (mod)

	# Grab all subsystems
	pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

	#lets go through all the player items till we find the core
	pShipList.TGBeginIteration()
	for i in range(pShipList.TGGetNumItems()):
		pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
		pSubsystem = pPlayer.GetSubsystemByProperty(pShipProperty)

		if (pSubsystem != None):
			# okay, lets do a couple if's to see if we have the power core
			if (pSubsystem.GetName() == "Warp Core"):
				pShipProperty.SetCritical(1)
				pShipProperty.SetTargetable(1)
				#screw it. make the damn core full health when u recover it. its not worth the trouble
				pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
			# find the nacelles and disable them so we cant warp without a core
			if (pSubsystem.IsTypeOf(App.CT_WARP_ENGINE_SUBSYSTEM)):
				pShipProperty.SetDisabledPercentage(50)

	pShipList.TGDoneIterating()
	pShipList.TGDestroy()
	######### end loading hardpoints

	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveCore", pCoreName), 3.0)
	MissionLib.QueueActionToPlay(pSeq)

	# All done here, pass the event onto it's next handler
	TGObject.CallNextHandler(pEvent)


# i have to put this in a seperate def so i can delay it
def RemoveCore(pAction, pCoreName):
	# grab some values
	debug(__name__ + ", RemoveCore")
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	# this means that the core is in a tractor hold by the player ship. Lets kill the core.
	pSet.RemoveObjectFromSet(pCoreName)

	#lets flicker those ship lights!
	try:
		import Custom.NanoFX.NanoFX_Lib
		pSequence = App.TGSequence_Create()
		pSequence.AddAction(Custom.NanoFX.NanoFX_Lib.CreateFlickerSeq(pPlayer, 3.0, sStatus = "On"))
		pSequence.Play()
	except:
		#it failed. dont worry about it, it means the user doesnt have nanofx 2.0
		novalue = "crap"

	return 0