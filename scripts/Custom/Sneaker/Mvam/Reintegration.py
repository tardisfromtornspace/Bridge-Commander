from bcdebug import debug
import App
import loadspacehelper
import MissionLib

MVAMReintegrationRunning = 0

def Reintegration (snkMvamModule):
	#do the bridge sound before anything, just so it's not delayed
	debug(__name__ + ", Reintegration")
	global MVAMReintegrationRunning
	MVAMReintegrationRunning = 1
	
	BridgeSound(snkMvamModule)

	# grab some values, these are used later and throughout
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pProximityManager = pSet.GetProximityManager()

	#set the player at tactical alert. why? problems ensue if we dont!
	pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

	#grab the set name, we need to know if the camera is on the bridge or outside
	intCameraInOrOut = 0
	if (App.g_kSetManager.GetRenderedSet().GetName() == "bridge"):
		intCameraInOrOut = 1

	# grab position points and orientation
	pPlayerForward = pPlayer.GetWorldForwardTG()
	pPlayerUp = pPlayer.GetWorldUpTG()
	vLocation = pPlayer.GetWorldLocation()

	#iterate to set the hardpoints
	pLocations = []
	pLocVec = []
	intTempCount = 0

	#grab the hull and property. put it in a try just in case there isnt a hull somehow
	pHull = pPlayer.GetHull()
	pHullPosition = pHull.GetPositionTG()
	pHullProperty = App.SubsystemProperty_Cast(pHull.GetProperty())

	#go through the ship positions. put it in a try in case of failure
	for n in range (len(snkMvamModule.ReturnMvamShips()) - 1):
		#set the hull and record
		pHullProperty.SetPosition(snkMvamModule.ReturnMvamReinDistances()[intTempCount].GetX(),
				snkMvamModule.ReturnMvamReinDistances()[intTempCount].GetY(),
				snkMvamModule.ReturnMvamReinDistances()[intTempCount].GetZ())
		pLocations.append(pHull.GetWorldLocation())

		#get the vector it would be heading to and record
		pHullProperty.SetPosition(pHull.GetPositionTG().GetX() + snkMvamModule.ReturnMvamReinDirections()[intTempCount].GetX(),
				pHull.GetPositionTG().GetY() + snkMvamModule.ReturnMvamReinDirections()[intTempCount].GetY(),
				pHull.GetPositionTG().GetZ() + snkMvamModule.ReturnMvamReinDirections()[intTempCount].GetZ())
		pLocVec.append(pHull.GetWorldLocation())

		#reset the hull location
		pHullProperty.SetPosition(pHullPosition.GetX(), pHullPosition.GetY(), pHullPosition.GetZ())

		#iterate the counter for the next ship
		intTempCount = intTempCount + 1

	# place all new ships
	pMvamShips = []
	pMvamTempShips = []
	intCount = 0

	for i in range (len(snkMvamModule.ReturnMvamShips()) - 1):
		#if the ship is already there, lets grab it. if not... create a new one
		if (App.ShipClass_GetObject (pSet, snkMvamModule.ReturnMvamShips()[i + 1])):
			#grab the ship. remove the object. create a new so its stopped
			pMvamShips.append(App.ShipClass_GetObject (pSet, snkMvamModule.ReturnMvamShips()[i + 1]))
			pSet.RemoveObjectFromSet(snkMvamModule.ReturnMvamShips()[i + 1])
			pMvamTempShips.append(loadspacehelper.CreateShip(snkMvamModule.ReturnMvamShips()[i + 1], pSet, snkMvamModule.ReturnMvamShips()[i + 1], ""))

			# positioning it, translate it to pLocations
			pMvamTempShips[intCount].SetTranslate(pLocations[i])
			pMvamTempShips[intCount].AlignToVectors(pPlayerForward, pPlayerUp)
			pMvamTempShips[intCount].SetAlertLevel(App.ShipClass.RED_ALERT)

			# update the ship with all these purdy changes
			pMvamTempShips[intCount].UpdateNodeOnly()
			# put it in the proxy manager, so we can AHHH LOOK OUT!
			if (pProximityManager):
				pProximityManager.UpdateObject (pMvamTempShips[intCount])

			#remember to add to the counter
			intCount = intCount + 1

		#else... its the player ship. create a new one, since we need the old one for reference (i think!)
		else:
			pPlayerJunk = loadspacehelper.CreateShip(snkMvamModule.ReturnMvamShips()[i + 1], pSet, "MvamTemp", "")

			# reposition the temp ship. dont make it collidable, just in case
			kPoint1 = App.TGPoint3()
			kPoint1.Set(vLocation)
			kPoint1.SetY(kPoint1.GetY() - 50000)
			pPlayerJunk.SetTranslate(kPoint1)
			pPlayerJunk.AlignToVectors(pPlayerForward, pPlayerUp)
			pPlayerJunk.SetCollisionsOn(0)

			#transfer temp hardpoints
			import Custom.Sneaker.Mvam.Hardpoints
			Custom.Sneaker.Mvam.Hardpoints.HardpointsTemp(pPlayerJunk, pPlayer)

			# reload the player ship so we know its STOPPED. reintegrate according to the pLocations
			pPlayer = MissionLib.CreatePlayerShip(snkMvamModule.ReturnMvamShips()[i + 1], pSet, "Player", "")
			pPlayer.SetTranslate(pLocations[i])
			pPlayer.AlignToVectors(pPlayerForward, pPlayerUp)
			pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

			# update the ship with all these purdy changes
			pPlayer.UpdateNodeOnly()
			# put it in the proxy manager, so we can AHHH LOOK OUT!
			if (pProximityManager):
				pProximityManager.UpdateObject (pPlayer)

	# okay, we gotta kill collisions
	for j in range (len(pMvamTempShips)):
		pMvamTempShips[j].EnableCollisionsWith(pPlayer, 0)
		for k in range (len(pMvamTempShips)):
			if (k != j):
				pMvamTempShips[j].EnableCollisionsWith(pMvamTempShips[k], 0)

	#set up the ship vectors
	intCountShip = 0
	for i in range (len(snkMvamModule.ReturnMvamShips()) - 1):
		if (App.ShipClass_GetObject (pSet, snkMvamModule.ReturnMvamShips()[i + 1])):
			vVelocity = pLocVec[i]
			vVelocity.Subtract(pLocations[i])
			vVelocity.Unitize() 
			vVelocity.Scale(snkMvamModule.ReturnMvamSpeeds()[i])
			pMvamTempShips[intCountShip].SetVelocity(vVelocity)
			intCountShip = intCountShip + 1
		else:
			vVelocity = pLocVec[i]
			vVelocity.Subtract(pLocations[i])
			vVelocity.Unitize() 
			vVelocity.Scale(snkMvamModule.ReturnMvamSpeeds()[i])
			pPlayer.SetVelocity(vVelocity)

	# purdy cutscene
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PreReintegrate", pPlayer))
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName()))
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName()))
	pSeq.AppendAction(App.TGScriptAction_Create("Custom.Sneaker.Mvam.Mvam_Lib", "SneakerWatchShip", pSet.GetName(), "Player", snkMvamModule))
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "CreateSound", snkMvamModule), snkMvamModule.ReturnCameraReinLength())
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ChangePlayer", snkMvamModule, pPlayerJunk, pMvamShips))
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName()))
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "PostCutscene", intCameraInOrOut))
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	pSeq.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PostReintegrate", pPlayer))
	MissionLib.QueueActionToPlay(pSeq)

	return 0


def BridgeSound (snkMvamModule):
	debug(__name__ + ", BridgeSound")
	if (snkMvamModule.ReturnBridgeReinSoundName() != ""):
		#grab pGame
		pGame = App.Game_GetCurrentGame()

		#set up the sound and play if it exists
		pGame.LoadSound("sfx/" + snkMvamModule.ReturnBridgeReinSoundName() + ".WAV", snkMvamModule.ReturnBridgeReinSoundName(), App.TGSound.LS_3D)
		pSound = App.g_kSoundManager.GetSound(snkMvamModule.ReturnBridgeReinSoundName())
		if (pSound != None):
			pSound.Play()


def CreateSound (pAction, snkMvamModule):
	debug(__name__ + ", CreateSound")
	if (snkMvamModule.ReturnReinSoundName() != ""):
		# grab some values
		pGame = App.Game_GetCurrentGame()
		pPlayer = pGame.GetPlayer()
		pSet = pPlayer.GetContainingSet()

		#set up the sound
		pGame.LoadSound("sfx/Explosions/" + snkMvamModule.ReturnReinSoundName() + ".WAV", snkMvamModule.ReturnReinSoundName(), App.TGSound.LS_3D)

		pSoundSeq = App.TGSequence_Create()
		pSound = App.TGSoundAction_Create(snkMvamModule.ReturnReinSoundName(), 0, pSet.GetName())
		pSound.SetNode(pPlayer.GetNode())
		pSoundSeq.AddAction(pSound)
		pSoundSeq.Play()

	return 0


def PostCutscene (pAction, intCameraInOrOut):
	# grab some values
	debug(__name__ + ", PostCutscene")
	global MVAMReintegrationRunning
	MVAMReintegrationRunning = 0
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	import Actions.CameraScriptActions
	if (intCameraInOrOut == 0):
		Actions.CameraScriptActions.ChangeRenderedSet (pAction, pSet.GetName())
	else:
		Actions.CameraScriptActions.ChangeRenderedSet (pAction, "bridge")

	return 0


def ChangePlayer (pAction, snkMvamModule, pPlayerJunk, pMvamShips):
	# grab some values, these are used later and throughout
	debug(__name__ + ", ChangePlayer")
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	# grab position points and orientation. make sure to jump the location up by 50
	pPlayerForward = pPlayerJunk.GetWorldForwardTG()
	pPlayerUp = pPlayerJunk.GetWorldUpTG()
	vLocation = pPlayerJunk.GetWorldLocation()
	vLocation.SetY(vLocation.GetY() + 50000)

	# get all ships, and remove them
	for c in range (len(pMvamShips)):
		pSet.RemoveObjectFromSet(pMvamShips[c].GetName())

	# changing the player ship
	pPlayer = MissionLib.CreatePlayerShip(snkMvamModule.ReturnMvamShips()[0], pSet, "Player", "")
	pPlayer.SetTranslate(vLocation)
	pPlayer.AlignToVectors(pPlayerForward, pPlayerUp)

	#transfer hardpoints and remove the temp ship. make sure there's a junk ship in there
	try:
		import Custom.Sneaker.Mvam.Hardpoints
		Custom.Sneaker.Mvam.Hardpoints.HardpointsRein(pPlayer, pPlayerJunk, pMvamShips)
		pSet.RemoveObjectFromSet("MvamTemp")
	#it failed... no big deal
	except:
		DoNothing = "Boooring!"

	# setting the alert level and impulse
	pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)
	vImpPoint = App.TGPoint3()
	vImpPoint.SetXYZ(0.0, 1.0, 0.0)
	pPlayer.SetImpulse(0.9, vImpPoint, App.ShipClass.DIRECTION_MODEL_SPACE)

	return 0
