from bcdebug import debug
# 2006 by Defiant erik@bckobayashimaru.de
#
# This file is part of the Kobayashi Maru Project: http://www.bckobayashimaru.de
#
# GPL http://www.gnu.org/copyleft
#

import App
import MissionLib
import Lib.LibEngineering

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.1",
                "needBridge": 0
            }

def InitMovie(pAction):
	debug(__name__ + ", InitMovie")
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return None

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
                return None

	pTopWindow.SetVisible()

	pTopWindow.DisableOptionsMenu(0)
	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)

	return 0


def PlaySeq(pAction, pEvent):
        #print "Playing Sequence"
    
        debug(__name__ + ", PlaySeq")
        pSequence = App.TGSequence_Create()
        
        pAction = App.TGScriptAction_Create(__name__, "InitMovie")
        pSequence.AddAction(pAction)
        pMovie = App.TGMovieAction_Create("data/Movies/Blank.bik", 1, 1)
        pSequence.AddAction(pMovie)
        pAction = App.TGScriptAction_Create(__name__, "ExitMovie")
        pSequence.AddAction(pAction)
        
        pSequence.Play()
        
        init()


class DeleteTimer:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.pTimerProcess = None
		self.SetupTimer()
	
	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		if self.pTimerProcess:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(300) # 5 minutes
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)

	def Update(self, dTimeAvailable):
		debug(__name__ + ", Update")
		lSets = App.g_kSetManager.GetAllSets()
		
		print "Trying to clean memory"
		for pSet in lSets:
			for kShip in pSet.GetClassObjectList(App.CT_DAMAGEABLE_OBJECT):
				if kShip.IsDead() and not kShip.IsDying():
					kShip.SetDeleteMe(1)

		# dump the unused models
		#App.g_kLODModelManager.Purge()
		#App.g_kModelManager.FreeAllModels()
		#App.g_kModelManager.Purge()


def init():
	debug(__name__ + ", init")
	
	# Do not start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
		
	global g_pDeleteTimer
	g_pDeleteTimer = DeleteTimer()
	
	# only start if we are Multiplayer dedicated host - we will crash everything else faster
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsClient():
		MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".PlaySeq", App.g_kUtopiaModule.GetGameTime() + 600, 0, 0)
