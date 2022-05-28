import App
import loadspacehelper
import MissionLib

g_pEnemyList = None
g_pFriendlyList = None
g_pNeutralList = None

g_pAction = None

def loadSystem(system_module, system_name, episode="", mission=""):
	pModule = __import__(system_module)
	if (hasattr(pModule, "CreateMenus")):
		pMenu = pModule.CreateMenus()
	else:
		import Systems.Utils
		Systems.Utils.CreateSystemMenu(system_name, system_module)

	if (episode != ""):
		pMenu.SetEpisodeName(episode)
		
	if (mission != ""):
		pMenu.SetMissionName(mission)
		
def CreatePlayerShip(sShipClass, sSetName, pcName, sWaypoint, bUnloadShip = 0):
	pSet = App.g_kSetManager.GetSet(sSetName)
	pPlayer	= MissionLib.CreatePlayerShip(sShipClass, pSet, pcName, sWaypoint, bUnloadShip)

def addFriendly(pMission, name):
	if (g_pFriendlyList == None):
		global g_pFriendlyList
		g_pFriendlyList = pMission.GetFriendlyGroup()
		
	g_pFriendlyList.AddName(name)

def addEnemy(pMission, name):
	if (g_pEnemyList == None):
		global g_pEnemyList
		g_pEnemyList = pMission.GetEnemyGroup()
		
	g_pEnemyList.AddName(name)

def addNeutral(pMission, name):
	if (g_pNeutralList == None):
		global g_pNeutralList
		g_pNeutralList = pMission.GetNeutralGroup()
		
	g_pNeutralList.AddName(name)

def translateShip(pShip, x, y, z, pTarget=None):
	p = App.TGPoint3()
	p.SetX(x)
	p.SetY(y)
	p.SetZ(z)
	pShip.SetTranslate(p)
	
	if (pTarget != None):
		MissionLib.OrientObjectTowardObject(pShip, pTarget)
 
def createCutscene(sModule, sFunc, duration, bFadeOut=0):
	pSequence = App.TGSequence_Create()
	
	#pPlayer = MissionLib.GetPlayer()
	#pSet = pPlayer.GetContainingSet()
	pSet = App.g_kSetManager.GetSet("bridge")

	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "addSkipHandler"))
	if (bFadeOut == 1):
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "FadeOut", 0))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.MissionScriptActions", "ChangeToBridge"))
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName()), 2)
	
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "SkipWrapper", sModule, sFunc))
	
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName()), duration)
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "removeSkipHandler"))
	
	return pSequence

def SkipWrapper(pAction, sModule, sFunc):
	global g_pAction
	g_pAction = pAction
	pSequence = App.TGSequence_Create()

	pSequence.AppendAction(App.TGScriptAction_Create(sModule, sFunc))

	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetDestination(App.g_kTGActionManager)
	pEvent.SetEventType(App.ET_ACTION_COMPLETED)
	pEvent.SetObjPtr(pAction)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.Play()
	App.TGActionManager_RegisterAction(pSequence, "cutscene")
	return 1
 	

def SkipSequence(TGObject, pEvent):
	# This function is called when a key is pressed
	
	# See if the key that was pressed matches the "SkipKey" string.
	iUnicode = pEvent.GetUnicode()
	kDisplayString = App.g_kInputManager.GetDisplayStringFromUnicode(iUnicode)
	
	kSkipKey = 's'
	
	if (kDisplayString.GetCString() == kSkipKey):
		# stop the TitleSequence
		App.TGActionManager_KillActions("cutscene")
		
		# this tells the main sequence to continue playing
		# without this the player would be stuck in cinematic mode
		pSequence = App.TGSequence_Create()
		pEvent = App.TGObjPtrEvent_Create()
		pEvent.SetDestination(App.g_kTGActionManager)
		pEvent.SetEventType(App.ET_ACTION_COMPLETED)
		pEvent.SetObjPtr(g_pAction)
		pSequence.AddCompletedEvent(pEvent)
		pSequence.Play()
		
	# All Done, pass on the event
	TGObject.CallNextHandler(pEvent)

def addSkipHandler(pAction):
	# adds a keyboard handler
	App.g_kRootWindow.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".SkipSequence")
	return 0

def removeSkipHandler(pAction):
	# removes the keyboard handler
	App.g_kRootWindow.RemoveHandlerForInstance(App.ET_KEYBOARD, __name__ + ".SkipSequence")
	return 0
 