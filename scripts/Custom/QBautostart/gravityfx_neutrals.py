from bcdebug import debug
import App
import MissionLib
import AI.Player.Stay

NonSerializedObjects = (
"g_NoTargetsGroup",
)

g_NoTargetsGroup = None

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Download": "http://www.bckobayashimaru.de",
                "needBridge": 0
            }

def SetAIAction(pAction, pShip):
	debug(__name__ + ", SetAIAction")
	if not pShip.IsDead() and not pShip.IsDying() and not pShip.GetAI() and pShip.GetName() != MissionLib.GetPlayer().GetName() and (App.g_kUtopiaModule.IsMultiplayer() and pShip.GetNetPlayerID() < 0):
		#pShip.SetAI(AI.Player.Stay.CreateAI(pShip))
		g_NoTargetsGroup = App.ObjectGroup()
		pShip.SetAI(CreateAI(pShip, g_NoTargetsGroup))
	return 0


def EnterSet(pObject, pEvent):
	debug(__name__ + ", EnterSet")
	pObject.CallNextHandler(pEvent)
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip:
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "SetAIAction", pShip), 1.0)
		pSeq.Play()


def init():
	debug(__name__ + ", init")
	# don't do anything in MP
	pMission = MissionLib.GetMission()
	import string
	if pMission and string.find(pMission.GetScript(), "Multiplayer") != -1:
		return
	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	
	global g_NoTargetsGroup
	g_NoTargetsGroup = App.ObjectGroup()
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, MissionLib.GetMission(), __name__ + ".EnterSet")



def CreateAI(pShip, pFriendlies):
        debug(__name__ + ", CreateEnemyAI")
        if not pFriendlies.GetNameTuple():
            pFriendlies.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import AI.Compound.BasicAttack
	pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pFriendlies, Difficulty = 1, FollowTargetThroughWarp = 1, UseCloaking = 1)
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
	# Creating PreprocessingAI AvoidObstacles at (29, 285)
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
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 12, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

