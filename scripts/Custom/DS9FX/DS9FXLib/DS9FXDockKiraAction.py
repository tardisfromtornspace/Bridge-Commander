# Custom docking action

# by Sov

# Imports
import App
import MissionLib

# Docking Action
def DockAction(pAction, pDockingAction = None, bNoRepair = 0, bFadeEnd = 1):
	# Get Player
	pPlayer = MissionLib.GetPlayer()
	if pPlayer is None:
		return 0

	# Take down Helm menu and turn character back.
	pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
	pHelm = App.CharacterClass_GetObject (pBridgeSet, "Helm")
	if pHelm is None:
		return 0
	pHelm.MenuDown()
	pHelm.TurnBack()

	pSequence = App.TGSequence_Create()

	# Make sure the rendered set is the Bridge.
	sOldSet = App.g_kSetManager.GetRenderedSet().GetName()
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))

	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "KiraSet", "Kira", 200))

	if pDockingAction is None:
		pSequence.AppendAction(App.TGScriptAction_Create(__name__, "WelcomeLine"))
	else:
		pSequence.AppendAction(pDockingAction)

	# Automatically reload & repair the player's ship.
	if not bNoRepair:
		pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "RepairShipFully", pPlayer.GetObjID()))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "ReloadShip", pPlayer.GetObjID()))
	
	# Fade out...  Something else will fade us back in later.
	if bFadeEnd:
		pSequence.AppendAction( App.TGScriptAction_Create("MissionLib", "FadeOut") )

	# Turn off the viewscreen.
	pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "ViewscreenOff"))

	# Change the rendered set back to whatever it used to be.
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", sOldSet), 0.5)

	# pAction is done when pSequence is done.
	pDoneEvent = App.TGObjPtrEvent_Create()
	pDoneEvent.SetEventType(App.ET_ACTION_COMPLETED)
	pDoneEvent.SetDestination(App.g_kTGActionManager)
	pDoneEvent.SetObjPtr(pAction)
	pSequence.AddCompletedEvent(pDoneEvent)

	pSequence.Play()

	return 1

# Line to say
def WelcomeLine(pAction):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        Database = pMission.SetDatabase("data/TGL/DS9FXDialogueDatabase.tgl")
        pSequence = App.TGSequence_Create()
        pKiraSet = App.g_kSetManager.GetSet("KiraSet")
        pKira = App.CharacterClass_GetObject (pKiraSet, "Kira")
        pKira.SetCharacterName("Kira")
        pSequence.AppendAction(App.CharacterAction_Create(pKira, App.CharacterAction.AT_SAY_LINE, "welcome", None, 0, Database))
        pSequence.Play()
        
        return 0
