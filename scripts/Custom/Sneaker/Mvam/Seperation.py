from bcdebug import debug
import App
import loadspacehelper
import MissionLib

def Seperation (snkMvamModule, strShip):
	#do the bridge sound before ANYTHING. this prevents delays
	debug(__name__ + ", Seperation")
	BridgeSound(snkMvamModule)

	# grab some values, these are used later and throughout
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	#set the player at tactical alert. why? problems ensue if we dont!
	pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

	#grab the set name, we need to know if the camera is on the bridge or outside
	intCameraInOrOut = 0
	if (App.g_kSetManager.GetRenderedSet().GetName() == "bridge"):
		intCameraInOrOut = 1

	# do the prescript def before we do anything major
	pPreScripts = App.TGSequence_Create()
	pPreScripts.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PreScripts", pPlayer))
	MissionLib.QueueActionToPlay(pPreScripts)	

	# grab position points and orientation
	pPlayerForward = pPlayer.GetWorldForwardTG()
	pPlayerUp = pPlayer.GetWorldUpTG()
	vLocation = pPlayer.GetWorldLocation()

	#iterate to set the hardpoints
	pLocations = []
	pLocVec = []
	intTempCount = 0

	#grab the hull and property
	pHull = pPlayer.GetHull()
	pHullPosition = pHull.GetPositionTG()
	pHullProperty = App.SubsystemProperty_Cast(pHull.GetProperty())

	#go through the ship positions. put it in a try in case of failure
	for n in range (len(snkMvamModule.ReturnMvamShips()) - 1):
		#set the hull and record
		pHullProperty.SetPosition(snkMvamModule.ReturnMvamDistances()[intTempCount].GetX(),
				snkMvamModule.ReturnMvamDistances()[intTempCount].GetY(),
				snkMvamModule.ReturnMvamDistances()[intTempCount].GetZ())
		pLocations.append(pHull.GetWorldLocation())

		#get the vector it would be heading to and record
		pHullProperty.SetPosition(pHull.GetPositionTG().GetX() + snkMvamModule.ReturnMvamDirections()[intTempCount].GetX(),
				pHull.GetPositionTG().GetY() + snkMvamModule.ReturnMvamDirections()[intTempCount].GetY(),
				pHull.GetPositionTG().GetZ() + snkMvamModule.ReturnMvamDirections()[intTempCount].GetZ())
		pLocVec.append(pHull.GetWorldLocation())

		#reset the hull location
		pHullProperty.SetPosition(pHullPosition.GetX(), pHullPosition.GetY(), pHullPosition.GetZ())

		#iterate the counter for the next ship
		intTempCount = intTempCount + 1

	# im gonna need this for future reference to transfer hardpoints
	pPlayerOriginal = pPlayer

	# creating the actual ship, then move and orient
	pPlayer = MissionLib.CreatePlayerShip(strShip, pSet, "Player", "")

	# put em at tac alert
	pPlayer.SetAlertLevel(App.ShipClass.RED_ALERT)

	# find out which ship the player is. subtract one because the combined ship isnt included
	for z in range (len(snkMvamModule.ReturnMvamShips())):
		if (snkMvamModule.ReturnMvamShips()[z] == strShip):
			intShipNum = z - 1

	# set the player location. do the impulse later! do it in a try... if it doesnt work, do it the standard way
	pPlayer.SetTranslate(pLocations[intShipNum])
	pPlayer.AlignToVectors(pPlayerForward, pPlayerUp)

	pProximityManager = pSet.GetProximityManager()
	if (pProximityManager):
		pProximityManager.UpdateObject (pPlayer)
	pPlayer.UpdateNodeOnly()

	## making others ##
	# creating the ships holder
	pMvamShips = []
	#placeholder... we CANT use i
	intCounter = 0
	for i in range (len(snkMvamModule.ReturnMvamShips()) - 1):
		#make sure we're not launching duplicates (ie: what we're setting as player)
		if (snkMvamModule.ReturnMvamShips()[i + 1] != strShip):
			#create the ship
			pMvamShips.append(loadspacehelper.CreateShip(snkMvamModule.ReturnMvamShips()[i + 1], pSet, snkMvamModule.ReturnMvamShips()[i + 1], ""))
			pPlayer.EnableCollisionsWith(pMvamShips[intCounter], 0)
			for l in range(intCounter):
				if l != intCounter:
					pMvamShips[intCounter].EnableCollisionsWith(pMvamShips[l], 0)

			# set position: use the player spot, then move em on the Z and Y axis. do a try, like above
			pMvamShips[intCounter].SetTranslate(pLocations[i])
			pMvamShips[intCounter].AlignToVectors(pPlayerForward, pPlayerUp)

			# add to friendlies group, set alert level, and disable collisions with player/ai ship
			pMission.GetFriendlyGroup().AddName(snkMvamModule.ReturnMvamShips()[i + 1])
			pMvamShips[intCounter].SetAlertLevel(App.ShipClass.RED_ALERT)
			pMvamShips[intCounter].EnableCollisionsWith(pPlayer, 0)

			# put em all in the proxy manager, so we can AHHH LOOK OUT!
			if (pProximityManager):
				pProximityManager.UpdateObject (pMvamShips[intCounter])
			#update all these purdy changes
			pMvamShips[intCounter].UpdateNodeOnly()

			#alright, counter is now used up. add one to it for next iteration
			intCounter = intCounter + 1

	#transfer damage
	import Custom.Sneaker.Mvam.Hardpoints
	Custom.Sneaker.Mvam.Hardpoints.HardpointsSep(pPlayerOriginal, pPlayer, pMvamShips)

	# set up a nice lil musical piece!!
	import DynamicMusic
	snkMvamModule.LoadDynamicMusic()
	DynamicMusic.PlayFanfare(snkMvamModule.ReturnMusicName())

	#set up the vectors
	vVelocity = pLocVec[intShipNum]
	vVelocity.Subtract(pLocations[intShipNum])
	vVelocity.Unitize() 
	vVelocity.Scale(snkMvamModule.ReturnMvamSpeeds()[intShipNum])
	pPlayer.SetVelocity(vVelocity) 

	intCountShip = 0
	for i in range (len(pMvamShips)):
		if (i != intShipNum):
			vVelocity = pLocVec[i]
			vVelocity.Subtract(pLocations[i])
			vVelocity.Unitize() 
			vVelocity.Scale(snkMvamModule.ReturnMvamSpeeds()[i])
			pMvamShips[intCountShip].SetVelocity(vVelocity)
			intCountShip = intCountShip + 1

	# make a pretty cut scene
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PreSeperate", pPlayer))
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName()))
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName()))
	pSeq.AppendAction(App.TGScriptAction_Create("Custom.Sneaker.Mvam.Mvam_Lib", "SneakerWatchShip", pSet.GetName(), "Player", snkMvamModule))
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "CreateSound", snkMvamModule))
	pSeq.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName()), snkMvamModule.ReturnCameraSepLength())
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "PostCutscene", intCameraInOrOut))
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MakeShipAi", snkMvamModule, pMvamShips))
	pSeq.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	pSeq.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PostSeperate", pPlayer))
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "DelayedCollisions", snkMvamModule, pMvamShips))
	MissionLib.QueueActionToPlay(pSeq)
	
	return 0


def BridgeSound (snkMvamModule):
	debug(__name__ + ", BridgeSound")
	if (snkMvamModule.ReturnBridgeSoundName() != ""):
		#grab pGame
		pGame = App.Game_GetCurrentGame()

		#set up the sound and play if it exists
		pGame.LoadSound("sfx/" + snkMvamModule.ReturnBridgeSoundName() + ".WAV", snkMvamModule.ReturnBridgeSoundName(), App.TGSound.LS_3D)
		pSound = App.g_kSoundManager.GetSound(snkMvamModule.ReturnBridgeSoundName())
		if (pSound != None):
			pSound.Play()


def CreateSound (pAction, snkMvamModule):
	debug(__name__ + ", CreateSound")
	if (snkMvamModule.ReturnSoundName() != ""):
		# grab some values
		pGame = App.Game_GetCurrentGame()
		pPlayer = pGame.GetPlayer()
		pSet = pPlayer.GetContainingSet()

		#set up the sound
		pGame.LoadSound("sfx/Explosions/" + snkMvamModule.ReturnSoundName() + ".WAV", snkMvamModule.ReturnSoundName(), App.TGSound.LS_3D)

		pSoundSeq = App.TGSequence_Create()
		pSound = App.TGSoundAction_Create(snkMvamModule.ReturnSoundName(), 0, pSet.GetName())
		pSound.SetNode(pPlayer.GetNode())
		pSoundSeq.AddAction(pSound)
		pSoundSeq.Play()

	return 0


def PostCutscene (pAction, intCameraInOrOut):
	# grab some values
	debug(__name__ + ", PostCutscene")
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()

	import Actions.CameraScriptActions
	if (intCameraInOrOut == 0):
		Actions.CameraScriptActions.ChangeRenderedSet (pAction, pSet.GetName())
	else:
		Actions.CameraScriptActions.ChangeRenderedSet (pAction, "bridge")

	return 0


def MakeShipAi (pAction, snkMvamModule, pMvamShips):
	# grab some values
	debug(__name__ + ", MakeShipAi")
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	snkMvamAiModule = __import__ (snkMvamModule.ReturnMvamAiName())

	# setting Ai
	for i in range (len(pMvamShips)):
		if (pMvamShips[i].GetName() != "Player"):
			pMvamShips[i].SetAI(snkMvamAiModule.CreateAI(pMvamShips[i]))

	#set player impulse
	vImpPoint = App.TGPoint3()
	vImpPoint.SetXYZ(0.0, 1.0, 0.0)
	pPlayer.SetImpulse(0.9, vImpPoint, App.ShipClass.DIRECTION_MODEL_SPACE)

	return 0


def DelayedCollisions (pAction, snkMvamModule, pMvamShips):
	# grab some values
	debug(__name__ + ", DelayedCollisions")
	pGame = App.Game_GetCurrentGame()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	snkMvamAiModule = __import__ (snkMvamModule.ReturnMvamAiName())

	# setting collisions. put it in a try JUST IN CASE the ships die in this length of time
	try:
		for i in range (len(pMvamShips)):
			if (pMvamShips[i].GetName() != "Player"):
				# re-enable collisions now that all ships are seperated and well apart
				pMvamShips[i].EnableCollisionsWith(pPlayer, 1)
				pPlayer.EnableCollisionsWith(pMvamShips[i], 1)
				for j in range (len(pMvamShips)):
					if (j != i):
						pMvamShips[i].EnableCollisionsWith(pMvamShips[j], 1)
	except:
		#well, now the ships cant run into each other. no big deal
		DoNothing = "Nothing At All"

	return 0