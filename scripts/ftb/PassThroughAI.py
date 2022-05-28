from bcdebug import debug
import App
import MissionLib


def FixCollisionsAction(pAction, pShip1ID, pShip2ID):
	debug(__name__ + ", FixCollisionsAction")
	
	pShip1 = App.ShipClass_GetObjectByID(None, pShip1ID)
	pShip2 = App.ShipClass_GetObjectByID(None, pShip2ID)

	# the following line stops the game in MP for unknown reason
	if pShip1 and pShip2 and not App.g_kUtopiaModule.IsMultiplayer():
		pShip1.EnableCollisionsWith(pShip2, 1)
	debug(__name__ + ", FixCollisionsAction Done")
	return 0


def FixCollisions(pShip, pLauncherShipName):
	debug(__name__ + ", FixCollisions")
	pLauncherShip = MissionLib.GetShip(pLauncherShipName)
	if pShip and pLauncherShip:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "FixCollisionsAction", pShip.GetObjID(), pLauncherShip.GetObjID()), 1)
		pSeq.Play()
	
		
def MoveIt(pShip):
	debug(__name__ + ", MoveIt")
	pEngines = pShip.GetImpulseEngineSubsystem()
        if pEngines:
            pProp = pEngines.GetProperty()
            maxSpeed = pProp.GetMaxSpeed()
            pShip.SetImpulse( maxSpeed, App.TGPoint3_GetModelForward(), App.ShipClass.DIRECTION_MODEL_SPACE )
	

def CreateAI(pShip, pDoneAI, pRadius, pLauncherShipName):
	debug(__name__ + ", CreateAI")
	pMission = MissionLib.GetMission ()
	pEnemies = pMission.GetEnemyGroup ()
	if not pEnemies.IsNameInGroup("DUMMYNAME"):
		pEnemies.AddName("DUMMYNAME")


	#########################################
	# Creating PlainAI Move at (147, 475)
	pMove = App.PlainAI_Create(pShip, "Move")
	pMove.SetScriptModule("RunScript")
	pMove.SetInterruptable(1)
	pScript = pMove.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("MoveIt")
	pScript.SetArguments(pShip)
	# Done creating PlainAI Move
	#########################################
	#########################################
	# Creating PlainAI ReEanbleCollisions at (310, 539)
	pReEanbleCollisions = App.PlainAI_Create(pShip, "ReEanbleCollisions")
	pReEanbleCollisions.SetScriptModule("RunScript")
	pReEanbleCollisions.SetInterruptable(1)
	pScript = pReEanbleCollisions.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("FixCollisions")
	pScript.SetArguments(pShip, pLauncherShipName)
	# Done creating PlainAI ReEanbleCollisions
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (269, 490)
	## Conditions:
	#### Condition DistanceFromLauncher
	pDistanceFromLauncher = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", pRadius, pLauncherShipName, pShip.GetName())
	## Evaluation function:
	def EvalFunc(bDistanceFromLauncher):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bDistanceFromLauncher:
			return DORMANT
		return ACTIVE
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pReEanbleCollisions)
	pWait.AddCondition(pDistanceFromLauncher)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################


	#########################################
	# Creating CompoundAI Attack at (108, 133)
	NewAI = __import__ ( pDoneAI)
	pAttack =  NewAI.CreateAI(pShip)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn at (237, 47)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (353, 55)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (429, 103)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (448, 147)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (198, 181)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (309, 185)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI RepeatForever at (195, 224)
	pRepeatForever = App.SequenceAI_Create(pShip, "RepeatForever")
	pRepeatForever.SetInterruptable(1)
	pRepeatForever.SetLoopCount(-1)
	pRepeatForever.SetResetIfInterrupted(1)
	pRepeatForever.SetDoubleCheckAllDone(1)
	pRepeatForever.SetSkipDormant(0)
	# SeqBlock is at (295, 228)
	pRepeatForever.AddAI(pFlyPointlessly)
	# Done creating SequenceAI RepeatForever
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (30, 228)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 235)
	pPriorityList.AddAI(pAttack, 1)
	pPriorityList.AddAI(pRepeatForever, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (269, 331)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (125, 380)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(1)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (244, 387)
	pSequence.AddAI(pMove)
	pSequence.AddAI(pWait)
	pSequence.AddAI(pAvoidObstacles)
	# Done creating SequenceAI Sequence
	#########################################
	return pSequence
