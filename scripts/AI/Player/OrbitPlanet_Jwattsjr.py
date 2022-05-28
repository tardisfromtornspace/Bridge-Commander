import App

def StartingOrbit(pShip, pPlanet):
	# Send an event saying that the ship is now orbitting the
	# planet it's around.
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(App.ET_AI_ORBITTING)
	pEvent.SetDestination(pPlanet)
	pEvent.SetSource(pShip)
	App.g_kEventManager.AddEvent(pEvent)


def ResetCamera(pPlanet):
	pPlayer = App.Game_GetCurrentPlayer()
	pJW = pPlanet.GetName()
	pPlayer.SetTarget(str(pJW))


def ChooseNewLocation(vOrigin, vOffset):
	# Add some random amount to vOffset
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * 20.0

	vOffset.SetX( vOffset.GetX() + fUnitRandom )


	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * 20.0

	vOffset.SetY( vOffset.GetY() + fUnitRandom )


	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * 20.0

	vOffset.SetZ( vOffset.GetZ() + fUnitRandom )

	return 0


def CreateAI(pShip, pPlanet):
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	pSetName = pSet.GetName()

	pPlacement = App.PlacementObject_Create("Warpto Exit", pSet.GetName(), None)
	kLocation = pPlanet.GetWorldLocation()
	vDiff = pPlanet.GetWorldLocation()
	vDiff.Unitize()
	#Exit Warp 900 Units away
	vDiff.Scale(900.0)

	# Make sure the ship's location won't overlap any other objects in the world.
	kTestPosition = App.TGPoint3()
	kTestPosition.Set(kLocation)
	kTestPosition.Add(vDiff)
	while pSet.IsLocationEmptyTG(kTestPosition, pPlanet.GetRadius() * 1.5) == 0:
		ChooseNewLocation(kLocation, vDiff)
		kTestPosition.Set(kLocation)
		kTestPosition.Add(vDiff)
	kLocation.Set(kTestPosition)

	# Change the waypoint's orientation so it's facing toward the
	# planet, so the player warps in toward the planet.
	kFwd = pPlanet.GetWorldLocation()
	kFwd.Subtract( kLocation )
	kFwd.Unitize()
	kUp = pPlanet.GetWorldUpTG()
	kUp.GetPerpendicularComponent( kFwd )
	kUp.Unitize()

	pPlacement.SetTranslate(kLocation)
	pPlacement.AlignToVectors( kFwd, kUp )
	pPlacement.UpdateNodeOnly()



	#########################################
	# Creating PlainAI StartingOrbitScript at (241, 52)
	pStartingOrbitScript = App.PlainAI_Create(pShip, "StartingOrbitScript")
	pStartingOrbitScript.SetScriptModule("RunScript")
	pStartingOrbitScript.SetInterruptable(1)
	pScript = pStartingOrbitScript.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StartingOrbit")
	pScript.SetArguments(pShip, pPlanet)
	# Done creating PlainAI StartingOrbitScript
	#########################################
	#########################################
	# Creating PlainAI CirclePlanet at (353, 55)
	pCirclePlanet = App.PlainAI_Create(pShip, "CirclePlanet")
	pCirclePlanet.SetScriptModule("CircleObject")
	pCirclePlanet.SetInterruptable(1)
	pScript = pCirclePlanet.GetScriptInstance()
	pScript.SetFollowObjectName(pPlanet.GetName())
	pScript.SetNearFacingVector(App.TGPoint3_GetModelLeft())
	fOrbitDistance = pPlanet.GetRadius() + pPlanet.GetAtmosphereRadius() + 150
	pScript.SetRoughDistances(fOrbitDistance, fOrbitDistance * 1.2)
	# Done creating PlainAI CirclePlanet
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (201, 111)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (301, 127)
	pSequence.AddAI(pStartingOrbitScript)
	pSequence.AddAI(pCirclePlanet)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating ConditionalAI CloseEnough at (210, 167)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 200.0 + pPlanet.GetRadius(),  pShip.GetName(), pPlanet.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCloseEnough = App.ConditionalAI_Create(pShip, "CloseEnough")
	pCloseEnough.SetInterruptable(1)
	pCloseEnough.SetContainedAI(pSequence)
	pCloseEnough.AddCondition(pInRange)
	pCloseEnough.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseEnough
	#########################################
	#########################################
	# Creating PlainAI SystemWarp at (626, 106)
	pSystemWarp = App.PlainAI_Create(pShip, "SystemWarp")
	pSystemWarp.SetScriptModule("Warp")
	pSystemWarp.SetInterruptable(1)
	pScript = pSystemWarp.GetScriptInstance()
	pScript.SetDestinationSetName("Systems." + str(pSetName)[:-1] + "." + str(pSetName))
	pScript.SetDestinationPlacementName("Warpto Exit")
	# Done creating PlainAI SystemWarp
	#########################################
	#########################################
	# Creating ConditionalAI FarAway at (487, 187)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 8000, pShip.GetName(), pPlanet.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if not bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pFarAway = App.ConditionalAI_Create(pShip, "FarAway")
	pFarAway.SetInterruptable(1)
	pFarAway.SetContainedAI(pSystemWarp)
	pFarAway.AddCondition(pInRange)
	pFarAway.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI FarAway
	#########################################
	#########################################
	# Creating PlainAI FixCamera at (415, 427)
	pFixCamera = App.PlainAI_Create(pShip, "FixCamera")
	pFixCamera.SetScriptModule("RunScript")
	pFixCamera.SetInterruptable(1)
	pScript = pFixCamera.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("ResetCamera")
	pScript.SetArguments(pPlanet)
	# Done creating PlainAI FixCamera
	#########################################
	#########################################
	# Creating PlainAI FlyToPlanet at (618, 430)
	pFlyToPlanet = App.PlainAI_Create(pShip, "FlyToPlanet")
	pFlyToPlanet.SetScriptModule("Intercept")
	pFlyToPlanet.SetInterruptable(1)
	pScript = pFlyToPlanet.GetScriptInstance()
	pScript.SetTargetObjectName(pPlanet.GetName())
	pScript.SetInterceptDistance(0.0)
	pScript.SetAddObjectRadius(1)
	# Done creating PlainAI FlyToPlanet
	#########################################
	#########################################
	# Creating SequenceAI Sequence_2 at (375, 269)
	pSequence_2 = App.SequenceAI_Create(pShip, "Sequence_2")
	pSequence_2.SetInterruptable(1)
	pSequence_2.SetLoopCount(2)
	pSequence_2.SetResetIfInterrupted(1)
	pSequence_2.SetDoubleCheckAllDone(1)
	pSequence_2.SetSkipDormant(1)
	# SeqBlock is at (485, 276)
	pSequence_2.AddAI(pFarAway)
	pSequence_2.AddAI(pFixCamera)
	pSequence_2.AddAI(pFlyToPlanet)
	# Done creating SequenceAI Sequence_2
	#########################################
	#########################################
	# Creating PriorityListAI OrbitPriorityList at (156, 227)
	pOrbitPriorityList = App.PriorityListAI_Create(pShip, "OrbitPriorityList")
	pOrbitPriorityList.SetInterruptable(1)
	# SeqBlock is at (272, 228)
	pOrbitPriorityList.AddAI(pCloseEnough, 1)
	pOrbitPriorityList.AddAI(pSequence_2, 2)
	# Done creating PriorityListAI OrbitPriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI OrbitAvoidObstacles at (128, 289)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pOrbitAvoidObstacles = App.PreprocessingAI_Create(pShip, "OrbitAvoidObstacles")
	pOrbitAvoidObstacles.SetInterruptable(1)
	pOrbitAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pOrbitAvoidObstacles.SetContainedAI(pOrbitPriorityList)
	# Done creating PreprocessingAI OrbitAvoidObstacles
	#########################################
	return pOrbitAvoidObstacles
