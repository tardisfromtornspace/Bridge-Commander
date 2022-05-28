import App
import MissionLib

g_pAction = None
g_pMission = None

DETAILPANEL_X=0.225
DETAILPANEL_Y=0.075
DETAILPANEL_W=0.65
DETAILPANEL_H=0.825

g_pTitle = None
g_pLines = []

def Initialize(pMission):
	global g_pMission
	g_pMission = pMission
	#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_START_WARP_NOTIFY, g_pMission, __name__ + ".StartWarpHandler")
	# The GUI must be created only once.
	createGUI()
	# Start the cutscene
	start()

def Restart():
	# We want the Briefing to be played every time the mission is restarted
	start()
	
def Terminate():
	#App.g_kEventManager.RemoveBroadcastHandler(App.ET_START_WARP_NOTIFY, g_pMission, __name__ + ".StartWarpHandler")
	pass
		
def Version():
	return "Briefing 1.0 by Banbury"
		
def createGUI():
	import Custom.QuickBattleGame.plugin
	
	# a pointer to the QBR main menu
	pMenu = Custom.QuickBattleGame.plugin.getMainMenu()
	
	# the text of the briefing
	lines = Custom.QuickBattleGame.plugin.getProperty("gBriefing")
	
	import Lib.Ambiguity
	
	# this adds a button to the main menu
	Lib.Ambiguity.addEventHandler("XO", "ET_BRIEFING_BUTTON", __name__ + ".showGUI")
	button = Lib.Ambiguity.createButton(pMenu, 'Briefing', Lib.Ambiguity.getEvent("ET_BRIEFING_BUTTON"), 'Briefing', 'XO')
	button.SetUseUIHeight(0)

	import Custom.QuickBattleGame.plugin
	# pointer to the main panel of the QBR GUI
	pMainPanel = Custom.QuickBattleGame.plugin.getMainPanel()

	# now the detail panel is created and hidden
	pPanel = Lib.Ambiguity.createPanel(pMainPanel, "BriefingPanel", DETAILPANEL_X, DETAILPANEL_Y, DETAILPANEL_W, DETAILPANEL_H)
	pPanel.SetNotVisible()
	pMainPanel.MoveToFront(pPanel)
	
	if lines == None:
		lines = ["", "", "", "", "", "", "", "", "", "", ""]
	
	# the following creates the text fields and populates them with the briefing texts
	global g_pTitle
	g_pTitle = Lib.Ambiguity.createEditBox(pPanel, 0.02, 0.06, "Title", lines[0], 0.45, 0.05, 256)
	pPanel.MoveToFront(g_pTitle)
	
	for n in range(1, 11):
		s = ""
		if (len(lines)>n):
			s = lines[n]
		pLine = Lib.Ambiguity.createEditBox(pPanel, 0.02, 0.06 + 0.04*n, "Line " + repr(n), s, 0.45, 0.05, 256)
		g_pLines.append(pLine)
		pPanel.MoveToFront(pLine)

	# the 'Update' button
	Lib.Ambiguity.addEventHandler("XO", "ET_UPDATE_BRIEFING", __name__ + ".updateBriefing")
	Lib.Ambiguity.createMainMenuButton(pPanel, "Update", Lib.Ambiguity.getEvent("ET_UPDATE_BRIEFING"), "Update", "XO", 0.5, 0.06, 0.125, 0.041)

	# and a frame with title. This should be created last or it will obstruct the other controls
	pFrame = Lib.Ambiguity.createFrame(pPanel, "Briefing", 0.0, 0.0, DETAILPANEL_W, DETAILPANEL_H, "NoMinimize", App.g_kMainMenuBorderMainColor)
	pFrame.SetUseScrolling(0)
	
def start():	
	import Custom.QuickBattleGame.plugin
	lines = Custom.QuickBattleGame.plugin.getProperty("gBriefing")
	
	# The briefing will be played only if there is text saved with the setup
	if (lines != None):
		playBriefing(lines)

def playBriefing(lines):
	# plays a cutscene with a view of the player ship and the briefing text as subtitles
	if (len(lines) > 0):
		pPlayer = MissionLib.GetPlayer()
		pSet = pPlayer.GetContainingSet()
	
		pSequence = App.TGSequence_Create()
		
		pSequence.AppendAction(App.TGScriptAction_Create(__name__, "addSkipHandler"))
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.MissionScriptActions", "ChangeToBridge"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "StartCutscene"))
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraBegin", pSet.GetName()), 2)
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", pSet.GetName()))
	
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", pSet.GetName(), pPlayer.GetName()))
		
		pSequence.AppendAction(App.TGScriptAction_Create(__name__, "TitleSequenceAction", lines))
		
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "CutsceneCameraEnd", pSet.GetName()), 6)
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))
		pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "EndCutscene"))
		pSequence.AppendAction(App.TGScriptAction_Create(__name__, "removeSkipHandler"))
		
		pSequence.Play()

def TitleSequenceAction(pAction, lines):
	# this sequence actually shows the briefing text
	# it's in a separate action to allow skipping
	global g_pAction
	g_pAction = pAction
	pSequence = App.TGSequence_Create()
	pSequence.AppendAction(App.TGScriptAction_Create(__name__, "EpisodeTitleAction", lines[0]))
	for line in lines[1:]:
		pSubtitleAction = App.SubtitleAction_CreateC(line)
		pSubtitleAction.SetDuration (5.0)
		pSequence.AppendAction(pSubtitleAction);
	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetDestination(App.g_kTGActionManager)
	pEvent.SetEventType(App.ET_ACTION_COMPLETED)
	pEvent.SetObjPtr(pAction)
	pSequence.AddCompletedEvent(pEvent)
	pSequence.Play()
	App.TGActionManager_RegisterAction(pSequence, "Briefing")
	return 1

def EpisodeTitleAction(pAction, pcTitle):
	# prints a text as a TGCredit
	pSeq = App.TGSequence_Create()

	pTop = App.TopWindow_GetTopWindow()
	pSubtitle = pTop.FindMainWindow(App.MWT_SUBTITLE)
	pSubtitle.SetVisible()

	App.TGCreditAction_SetDefaultColor(0.65, 0.65, 1.00, 1.00)
	pSeq.AddAction(App.TGCreditAction_CreateSTR(pcTitle, pSubtitle, 0.5, 0.025, 5, 0.25, 0.5, 12))

	pSeq.Play()

	return 0	

def SkipSequence(TGObject, pEvent):
	# This function is called when a key is pressed
	
	# See if the key that was pressed matches the "SkipKey" string.
	iUnicode = pEvent.GetUnicode()
	kDisplayString = App.g_kInputManager.GetDisplayStringFromUnicode(iUnicode)
	
	kSkipKey = 's'
	
	if (kDisplayString.GetCString() == kSkipKey):
		# stop the TitleSequence
		App.TGActionManager_KillActions("Briefing")
		
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

def showGUI(pObject, pEvent):
	# this is called when the 'Briefing' button in the main menu is pressed
	import Custom.QuickBattleGame.plugin
	# hide the active panel in the GUI
	pActivePanel = Custom.QuickBattleGame.plugin.getActivePanel()
	pActivePanel.SetNotVisible()
	import Lib.Ambiguity
	# show our own panel
	pActivePanel = Lib.Ambiguity.getPanel("BriefingPanel")
	Custom.QuickBattleGame.plugin.setActivePanel(pActivePanel)
	pActivePanel.SetVisible()	

	if (pObject):
		pObject.CallNextHandler(pEvent)

def updateBriefing(pObject, pEvent):
	# this is called when the 'Update' button is pressed
	
	# retrieve the text from the edit fields
	lines = []
	lines.append(g_pTitle.GetCString())

	for pLine in g_pLines:
		lines.append(pLine.GetCString())
		
	# delete any empty lines from the end of list
	for n in range(0, len(lines)):
		if (lines[-1] == ""):
			lines.pop()
		else:
			break

	import Custom.QuickBattleGame.plugin
	# save the briefing text
	# the next time the user hits the 'Save' button this will be saved to the active setup file
	lines = Custom.QuickBattleGame.plugin.setProperty("gBriefing", lines)

	if (pObject):
		pObject.CallNextHandler(pEvent)

def StartWarpHandler (pObject, pEvent):
	pShip = App.ShipClass_Cast(pEvent.GetDestination ())
	if (not pShip):
		return 0
	
	pSet = pShip.GetContainingSet()
	print pSet.GetName()

	pWarp = pShip.GetWarpEngineSubsystem()
	
	# I wanted to add code here, to stop ships from warping during the briefing.
	# If you know a solution to this problem, contact me.
	
	return 0

