import App
import loadspacehelper
import MissionLib

def Seperation (snkMvamModule, straShipInfo):
	# grab some values, these are used later and throughout
	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pPlayer = pGame.GetPlayer()
	pSet = pPlayer.GetContainingSet()
	pShipOrig = App.ShipClass_GetObject (pSet, straShipInfo[0])

	#is this our proper ship? If it's not, CAN IT LIKE A GROCERY STORE!
	if (pShipOrig.GetScript() != ("ships." + snkMvamModule.ReturnMvamShips()[0])):
		return

	#set the player at tactical alert. why? problems ensue if we dont!
	pShipOrig.SetAlertLevel(App.ShipClass.RED_ALERT)

	# do the prescript def before we do anything major
	pPreScripts = App.TGSequence_Create()
	pPreScripts.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PreScripts", pShipOrig))
	MissionLib.QueueActionToPlay(pPreScripts)

	#first, check to see if the players target is the seperating ship
	intShipTargetted = 0
	if (pPlayer.GetTarget() and pShipOrig.GetName() == pPlayer.GetTarget().GetName()):
		intShipTargetted = 1

	# grab position points and orientation
	pPlayerForward = pShipOrig.GetWorldForwardTG()
	pPlayerUp = pShipOrig.GetWorldUpTG()
	vLocation = pShipOrig.GetWorldLocation()

	#iterate to set the hardpoints
	pLocations = []
	pLocVec = []
	intTempCount = 0

	#grab the hull and property.
	pHull = pShipOrig.GetHull()
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

	# im gonna need this for future reference to transfer hardpoints. also, get the group
	# move the player WAYYY the hell away from everything. just temporarily
	vLocation.SetY(vLocation.GetY() + 500000)
	pShipOrig.SetTranslate(vLocation)
	vLocation.SetY(vLocation.GetY() - 500000)
	pEnemies = pMission.GetEnemyGroup()
	pFriendlies = pMission.GetFriendlyGroup()
	pNeutrals = pMission.GetNeutralGroup()

	#we need to find what group the ship was in... 0 = enemy, 1 = friend. there wont be a neutral
	if (pEnemies.IsNameInGroup(pShipOrig.GetName())):
		pEnemies.RemoveName(pShipOrig.GetName())
		intGroup = 0
	elif (pFriendlies.IsNameInGroup(pShipOrig.GetName())):
		pFriendlies.RemoveName(pShipOrig.GetName())
		intGroup = 1
	else:
		pNeutrals.RemoveName(pShipOrig.GetName())
		intGroup = 2

	# creating the actual ship, then move and orient
	pShip = loadspacehelper.CreateShip(snkMvamModule.ReturnMvamShips()[1], pSet, snkMvamModule.ReturnMvamShips()[1] + straShipInfo[1], "")

	try:
		pShip.SetTranslate(pLocations[0])
	except:
		kPoint = App.TGPoint3()
		kPoint.Set(vLocation)
		kPoint.Add(snkMvamModule.ReturnMvamDistances()[0])
		pShip.SetTranslate(kPoint)
	pShip.AlignToVectors(pPlayerForward, pPlayerUp)

	#if the player's target is the seperating ship, change it to the first of the seperating ships
	if (intShipTargetted == 1):
		pPlayer.SetTarget(pShip.GetName())

	#setting friendly/enemy
	pFriendlies.RemoveName(pShip.GetName())
	if (intGroup == 0):
		pEnemies.AddName(pShip.GetName())
	elif (intGroup == 1):
		pFriendlies.AddName(pShip.GetName())
	else:
		pNeutrals.AddName(pShip.GetName())

	# put em at tac alert
	pShip.SetAlertLevel(App.ShipClass.RED_ALERT)

	pProximityManager = pSet.GetProximityManager()
	if (pProximityManager):
		pProximityManager.UpdateObject (pShip)
	pShip.UpdateNodeOnly()

	## making others ##
	# creating the ships holder
	pMvamShips = []
	#placeholder... we CANT use i
	intCounter = 0
	for i in range (len(snkMvamModule.ReturnMvamShips()) - 1):
		#make sure we're not launching duplicates (ie: what we're setting as player)
		if ("ships." + snkMvamModule.ReturnMvamShips()[i + 1] != pShip.GetScript()):
			pMvamShips.append(loadspacehelper.CreateShip(snkMvamModule.ReturnMvamShips()[i + 1], pSet, snkMvamModule.ReturnMvamShips()[i + 1] + straShipInfo[1], ""))
			pShip.EnableCollisionsWith(pMvamShips[intCounter], 0)
			pMvamShips[intCounter].EnableCollisionsWith(pShip, 0)
			for l in range(intCounter):
				if l != intCounter:
					pMvamShips[intCounter].EnableCollisionsWith(pMvamShips[l], 0)

			# set position: use the player spot, then move em on the Z and Y axis
			pMvamShips[intCounter].SetTranslate(pLocations[i])
			pMvamShips[intCounter].AlignToVectors(pPlayerForward, pPlayerUp)

			pFriendlies.RemoveName(pMvamShips[intCounter].GetName())
			if (intGroup == 0):
				pEnemies.AddName(pMvamShips[intCounter].GetName())
			elif (intGroup == 1):
				pFriendlies.AddName(pMvamShips[intCounter].GetName())
			else:
				pNeutrals.AddName(pMvamShips[intCounter].GetName())

			# set alert level
			pMvamShips[intCounter].SetAlertLevel(App.ShipClass.RED_ALERT)

			# put em all in the proxy manager, so we can AHHH LOOK OUT!
			if (pProximityManager):
				pProximityManager.UpdateObject (pMvamShips[intCounter])
			# update all these purdy changes
			pMvamShips[intCounter].UpdateNodeOnly()

			#alright, counter is now used up. add one to it for next iteration
			intCounter = intCounter + 1

	#transfer damage
	import Custom.Sneaker.Mvam.Hardpoints
	Custom.Sneaker.Mvam.Hardpoints.HardpointsSep(pShipOrig, pShip, pMvamShips)

	#set up the vector of the ai ship
	vVelocity = pLocVec[0]
	vVelocity.Subtract(pLocations[0])
	vVelocity.Unitize() 
	vVelocity.Scale(snkMvamModule.ReturnMvamSpeeds()[0])
	pShip.SetVelocity(vVelocity) 

	intCountShip = 0
	for i in range (len(pMvamShips)):
		if (i != 0):
			vVelocity = pLocVec[i]
			vVelocity.Subtract(pLocations[i])
			vVelocity.Unitize() 
			vVelocity.Scale(snkMvamModule.ReturnMvamSpeeds()[i])
			pMvamShips[intCountShip].SetVelocity(vVelocity)
			intCountShip = intCountShip + 1

	# make a pretty cut scene
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PreSeperate", pShip), 5.0)
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MakeShipAi", snkMvamModule, pShip, pMvamShips, straShipInfo[0]))
	pSeq.AppendAction(App.TGScriptAction_Create(snkMvamModule.ReturnModuleName(), "PostSeperate", pShip))
	MissionLib.QueueActionToPlay(pSeq)

	pKillSeq = App.TGSequence_Create()
	pKillSeq.AppendAction(App.TGScriptAction_Create(__name__, "KillShip", pSet, straShipInfo[0]))
	pKillSeq.Play()

	return 0


def KillShip (pAction, pSet, strShipName):
	#get rid of the original ship, we don't need it anymore
	pSet.RemoveObjectFromSet(strShipName)	
	return 0


def MakeShipAi (pAction, snkMvamModule, pShip, pMvamShips, strShipName):
	# grab some values
	pSet = pShip.GetContainingSet()

	snkMvamAiModule = __import__ (snkMvamModule.ReturnMvamAiName())
	pMvamShips.append(pShip)

	# setting Ai
	for i in range (len(pMvamShips)):
		pMvamShips[i].SetAI(snkMvamAiModule.CreateAI(pMvamShips[i]))

		# re-enable collisions now that all ships are seperated
		pMvamShips[i].EnableCollisionsWith(pShip, 1)
		for j in range (len(pMvamShips)):
			if (j != i):
				pMvamShips[i].EnableCollisionsWith(pMvamShips[j], 1)

	return 0