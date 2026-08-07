from bcdebug import debug

import App
import Lib.LibEngineering

MODINFO = {
    "Author": "ChatGPT",
    "Version": "1.0",
    "needBridge": 0
}


def InitMovie(pAction):
	debug(__name__ + ", InitMovie")
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return 0

	pTopWindow.SetNotVisible()

	pTopWindow.DisableOptionsMenu(1)
	pTopWindow.AllowKeyboardInput(0)
	pTopWindow.AllowMouseInput(0)

	return 0



def ExitMovie(pAction):
	debug(__name__ + ", ExitMovie")
	App.g_kMovieManager.SwitchOutOfMovieMode()

	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return 0

	pTopWindow.SetVisible()

	pTopWindow.DisableOptionsMenu(0)
	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)

	return 0



def PlaySeq(pAction, pEvent):
	debug(__name__ + ", PlaySeq")
	pSequence = App.TGSequence_Create()

	pInitAction = App.TGScriptAction_Create(__name__, "InitMovie")
	pSequence.AddAction(pInitAction)
	pMovie = App.TGMovieAction_Create("data/Movies/Blank.bik", 1, 1)
	pSequence.AddAction(pMovie)
	pExitAction = App.TGScriptAction_Create(__name__, "ExitMovie")
	pSequence.AddAction(pExitAction)

	pSequence.Play()
	return 0



def init():
	debug(__name__ + ", init")

	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return

	Lib.LibEngineering.CreateMenuButton("Clean Memory", "Engineer", __name__ + ".PlaySeq")
