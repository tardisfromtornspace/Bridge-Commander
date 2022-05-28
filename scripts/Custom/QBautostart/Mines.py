from bcdebug import debug
#!/usr/bin/python-1.5
# Mines.py - just..lay mines ;) <mail@defiant.homedns.org>

# TODO:
# Keine Schilde!

# Settings
fRangeValue = 100 # Range to Activate in Gameunits, 1km = 5.71428 game units (default: 100)
SetNeutral = 1 # Set to one if the the Mine Should be Neutral and not friendly (default: 0)
MineModel = "Mine" # Mine Model to use as in scripts/ships/, use in brackets (default: "Mine")
initTime = 10 # Time before the mine get ready (default: 10)
prepareMineTime = 40 # the Time Brex needs to prepare the mine (default: 40)

# Please do not edit below this line - except you know what you are doing
# ================================================================================

# Header
import App 
import MissionLib 
import Lib.LibEngineering
import ftb.FTB_MissionLib
MINE_COUNTER = None
pInitTimeButton = None
pPrepareButton = None
numprepare = 0
g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Mines.tgl")
        
MODINFO = {     "Author": "\"Defiant\" mail@defiant.homedns.org",
                "Download": "http://defiant.homedns.org/~erik/STBC/Mine/",
                "Version": "0.4",
                "License": "GPL",
                "Description": "Mines...",
                "needBridge": 0
            }
            
# Create Button
def init():
        debug(__name__ + ", init")
        global initTime, pInitTimeButton, pBrexMenu, pPrepareButton, MINE_COUNTER
        pBrexMenu = Lib.LibEngineering.GetBridgeMenu("Engineer")
        pMasterButton = App.STMenu_CreateW(App.TGString("Mine control"))
    
        pPrepareButton = Lib.LibEngineering.CreateMenuButton("prepare", "Engineer", __name__ + ".Minesdef", 0, pMasterButton)
        pInitTimeButton = Lib.LibEngineering.CreateMenuButton("init Time: " + str(initTime), "Engineer", __name__ + ".SetInitTime", 0, pMasterButton)
        pBrexMenu.AddChild(pMasterButton)
        
        # Event Handler for the Timer:
        MINE_COUNTER = Lib.LibEngineering.GetEngineeringNextEventType()
        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(MINE_COUNTER, __name__ + ".Addmine")


def SetInitTime(pObject, pEvent):
    debug(__name__ + ", SetInitTime")
    global initTime, pInitTimeButton
    initTime = initTime + 10
    if (initTime == 130):
        initTime = 0
    pInitTimeButton.SetName(App.TGString("init Time: " + str(initTime)))


# Start the add Timer
def Minesdef(pObject, pEvent):
        debug(__name__ + ", Minesdef")
        global MINE_COUNTER, prepareMineTime, g_pDatabase, pPrepareButton, numprepare
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pBrex = App.CharacterClass_GetObject(pBridge, "Engineer")
        
        # Yes, thats the timer from the Self Destruct Mod.
        # Create an event - it's a thing that will call this function
        pTimerEvent = App.TGEvent_Create()
        pTimerEvent.SetEventType(MINE_COUNTER)
        pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

	CounterTime = prepareMineTime
	
	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + CounterTime)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)

        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "MinePrepare", None, 0, g_pDatabase)) # Brex
        pSequence.Play()
        
        numprepare = numprepare + 1
	if pPrepareButton:
		pPrepareButton.SetName(App.TGString("prepare " + str(numprepare)))


# Add the Mine
def Addmine(pObject, pEvent):
        # Do not execute if this is a Bool Event
        debug(__name__ + ", Addmine")
        if hasattr(pEvent, "GetBool"):
                pObject.CallNextHandler(pEvent)
                return
        
        global MineModel, g_pDatabase, pPrepareButton, numprepare
        pBridge = App.g_kSetManager.GetSet("bridge")
        g_pBrex = App.CharacterClass_GetObject(pBridge, "Engineer")

        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "MineReady", None, 0, g_pDatabase)) # Brex
        pSequence.Play()
        
        pShip = App.Game_GetCurrentPlayer()
        
        # From scripts.ReturnShuttles.IncreaseShuttleCount()
        LauncherManager = __import__("ftb.LauncherManager")
        launcher = LauncherManager.GetLauncher(ftb.FTB_MissionLib.GetFirstShuttleBayName(), pShip)
        if not launcher:
		print("Mine Error: No working Carrier file for this ship.")
		return
	if SetNeutral and not App.g_kUtopiaModule.IsMultiplayer():
		launcher.AddLaunchable(MineModel, "Custom.QBautostart.Mines", ftb.FTB_MissionLib.ShuttlesInBayOfThisType(MineModel) + 1, side="neutral")
	else:
        	launcher.AddLaunchable(MineModel, "Custom.QBautostart.Mines", ftb.FTB_MissionLib.ShuttlesInBayOfThisType(MineModel) + 1)
        
        numprepare = numprepare - 1
        if numprepare > 0:
                pPrepareButton.SetName(App.TGString("prepare " + str(numprepare)))
        else:
                pPrepareButton.SetName(App.TGString("prepare"))


def Restart():
        debug(__name__ + ", Restart")
        global numprepare
        numprepare = 0


# Set AI
def CreateAI(pShip, pEnemies=MissionLib.GetEnemyGroup()):
        debug(__name__ + ", CreateAI")
        global SetNeutral, initTime
        if initTime == 0:
                import AI.Player.Stay
                pAttack = AI.Player.Stay.CreateAI(pShip)
        else:
	        pAttack = CreateAI2(pShip, pEnemies)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (80, 77)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", initTime, 0)
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
	pWait.SetContainedAI(pAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait


def CreateAI2(pShip, *lsTargets):
	# Make a group for all the targets...
	pAllTargetsGroup = App.ObjectGroup_ForceToGroup(lsTargets)
	sInitialTarget = None
	if pAllTargetsGroup.GetNameTuple():
		sInitialTarget = pAllTargetsGroup.GetNameTuple()[0]

        debug(__name__ + ", CreateAI2")
        global fRangeValue
	#########################################
	# Creating PlainAI SelfDestruct_2 at (117, 91)
	pSelfDestruct_2 = App.PlainAI_Create(pShip, "SelfDestruct_2")
	pSelfDestruct_2.SetScriptModule("SelfDestruct")
	pSelfDestruct_2.SetInterruptable(1)
	# Done creating PlainAI SelfDestruct_2
	#########################################
	#########################################
	# Creating ConditionalAI SensorsDead at (76, 184)
	## Conditions:
	#### Condition Disabled
	pDisabled = App.ConditionScript_Create("Conditions.ConditionSystemDisabled", "ConditionSystemDisabled", pShip.GetName(), App.CT_SENSOR_SUBSYSTEM, 1)
	## Evaluation function:
	def EvalFunc(bDisabled):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bDisabled:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pSensorsDead = App.ConditionalAI_Create(pShip, "SensorsDead")
	pSensorsDead.SetInterruptable(1)
	pSensorsDead.SetContainedAI(pSelfDestruct_2)
	pSensorsDead.AddCondition(pDisabled)
	pSensorsDead.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI SensorsDead
	#########################################
	#########################################
	# Creating PlainAI SelfDestruct at (286, 61)
	pSelfDestruct = App.PlainAI_Create(pShip, "SelfDestruct")
	pSelfDestruct.SetScriptModule("SelfDestruct")
	pSelfDestruct.SetInterruptable(1)
	# Done creating PlainAI SelfDestruct
	#########################################
	#########################################
	# Creating ConditionalAI ConditionInRange at (245, 127)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", fRangeValue, sInitialTarget, pShip.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pConditionInRange = App.ConditionalAI_Create(pShip, "ConditionInRange")
	pConditionInRange.SetInterruptable(1)
	pConditionInRange.SetContainedAI(pSelfDestruct)
	pConditionInRange.AddCondition(pInRange)
	pConditionInRange.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI ConditionInRange
	#########################################
	#########################################
	# Creating ConditionalAI TargetsInSet at (184, 184)
	## Conditions:
	#### Condition SameSet
	pSameSet = App.ConditionScript_Create("Conditions.ConditionAnyInSameSet", "ConditionAnyInSameSet", pShip.GetName(), lsTargets)
	## Evaluation function:
	def EvalFunc(bSameSet):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bSameSet:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pTargetsInSet = App.ConditionalAI_Create(pShip, "TargetsInSet")
	pTargetsInSet.SetInterruptable(1)
	pTargetsInSet.SetContainedAI(pConditionInRange)
	pTargetsInSet.AddCondition(pSameSet)
	pTargetsInSet.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI TargetsInSet
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (42, 243)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (146, 250)
	pPriorityList.AddAI(pSensorsDead, 1)
	pPriorityList.AddAI(pTargetsInSet, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	return pPriorityList
