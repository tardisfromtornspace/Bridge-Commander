from bcdebug import debug
# written by the TG scripter Colin Carley.
#
# current Maintainer: Defiant <mail@defiant.homedns.org>
#
# Self Destruct Countdown


import App
import MissionLib
import QuickBattle.QuickBattle
import Lib.LibEngineering

pBridge = None
g_pSaffi = None
pSaffiMenu = None
g_iCountdown = -1
MySelfDestructCaller = None
SDpPlayer = None
cTime = 10 # standard time
pDatabase = App.g_kLocalizationManager.Load("data/TGL/SelfDestructionCountdown.tgl")
pButtonSD = None
pButtonSDTimer = None

MODINFO = { "Author": "\"Defiant\" mail@defiant.homedns.org",
            "Download": "http://defiant.homedns.org/~erik/STBC/SelfDestruct/",
            "Version": "1.6",
            "License": "GPL",
            "Description": "This is adding a Countdown to the Self Destruction",
            "needBridge": 0
            }
            
# The Button
def init():
        debug(__name__ + ", init")
        global pButtonSD, pButtonSDTimer, cTime, pBridge, g_pSaffi, pSaffiMenu
        
        pBridge = App.g_kSetManager.GetSet('bridge')
        g_pSaffi = App.CharacterClass_GetObject(pBridge, 'XO')
        pSaffiMenu = Lib.LibEngineering.GetBridgeMenu('XO')
	App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(App.ET_INPUT_SELF_DESTRUCT, __name__ + ".MySelfDestructStart")
        
        pMasterButtonSD = App.STMenu_CreateW(App.TGString("Self Destruct menu"))
        
        pButtonSD = Lib.LibEngineering.CreateMenuButton("Self Destruct", "XO", __name__ + ".MySelfDestructStart", 0, pMasterButtonSD)
        
        pButtonSDTimer = Lib.LibEngineering.CreateMenuButton("Time: " + str(cTime), "XO", __name__ + ".SetSDTimer", 0, pMasterButtonSD)
        
        pSaffiMenu.PrependChild(pMasterButtonSD)
        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(App.ET_INPUT_SELF_DESTRUCT, __name__ + ".MySelfDestructStart")


def MySelfDestructStart(pObject, pEvent):
	debug(__name__ + ", MySelfDestructStart")
	global g_iCountdown, MySelfDestructCaller, SDpPlayer

        # fail in MP if Hull <= 10%
        if App.g_kUtopiaModule.IsMultiplayer():
                pPlayer = MissionLib.GetPlayer()
		if not pPlayer:
			return
                if pPlayer.GetHull().GetConditionPercentage() <= 0.1:
                        pSequence = App.TGSequence_Create()
                        pAction = App.TGScriptAction_Create(__name__, "SayString", "Self Destruct System is offline", 1)
                        pSequence.AppendAction(pAction)
                        pSequence.Play()
                        return

	if (g_iCountdown == -1):
		# mySelfDestruct: Start
		
		# This makes sure we kill the right ship (when transporting on another)
		SDpPlayer = MissionLib.GetPlayer()
		if not (SDpPlayer):
			return
			
		MySelfDestruct()
	# Now test what Function is calling us
	elif (str(MySelfDestructCaller) == str(pEvent)):
		if (g_iCountdown != -2):
			# mySelfDestruct: Go on
			MySelfDestruct()
	else:
		if (g_iCountdown == -2):
			# resetting g_iCountdown
			g_iCountdown = -1
		else:
			# mySelfDestruct: Cancel
			CancelSelfDestruct()


def SayString(pAction, pcString, Duration = 5.0):
        debug(__name__ + ", SayString")
        pSequence = App.TGSequence_Create()
        pSubtitleAction = App.SubtitleAction_CreateC(pcString)
        pSubtitleAction.SetDuration(Duration)
        pSequence.AddAction(pSubtitleAction)
        pSequence.Play()
        
        App.STMissionLog_GetMissionLog().AddLine(App.TGString(pcString))
        
        return 0


def MySelfDestruct():
	debug(__name__ + ", MySelfDestruct")
	global g_iCountdown, MySelfDestructCaller, cTime, g_pSaffi, pDatabase
	
	MySelfDestructCaller = None
	
	if (g_iCountdown == -1):
		# We are starting our countdown..
		g_iCountdown = cTime + 6
		# its 14 cause we need more time for auth...
	elif (g_iCountdown == 0):
                # We're dead!
	        FinallyDie()
        	return

	# Create an event - it's a thing that will call this function
	pTimerEvent = App.TGEvent_Create()
	pTimerEvent.SetEventType(App.ET_INPUT_SELF_DESTRUCT)
	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

	SDCounterTime = 1.0
	
	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + SDCounterTime)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)
	MySelfDestructCaller = pTimerEvent
	
	# And finally, call out the line..
	if g_pSaffi:
		# Needed some Custom Values cause Saffi is speaking too slow!
		if ( g_iCountdown == cTime + 6):
			g_pSaffi.SpeakLine(g_pSaffi.GetDatabase(),"SelfDestructStart")
		elif ( g_iCountdown == cTime + 5):
			g_pSaffi.SpeakLine(g_pSaffi.GetDatabase(),"SaffiCommand")
		elif ( g_iCountdown == 10 and cTime > 0):
			g_pSaffi.SpeakLine(g_pSaffi.GetDatabase(),"SelfDestruct10")
		elif ( g_iCountdown < 10 and cTime > 0):
			g_pSaffi.SpeakLine(g_pSaffi.GetDatabase(),"SelfDestruct" + str(g_iCountdown))
                elif (g_iCountdown > 10 and g_iCountdown%10 == 0):
                        pcString = pDatabase.GetString ("SelfDestructTime").GetCString ()
                        pSequence = App.TGSequence_Create()
                        pSequence.AppendAction(App.CharacterAction_Create(g_pSaffi, App.CharacterAction.AT_SAY_LINE, "SelfDestructTime" + str(g_iCountdown), None, 0, pDatabase))
                        pSequence.Play()
        else:
                line = None
                if ( g_iCountdown == cTime + 6):
                        line = "Self Destruct Initiated"
                elif ( g_iCountdown == cTime + 5):
                        line = "and authorized"
                elif ( g_iCountdown == 10 and cTime > 0):
                        line = "10"
                elif ( g_iCountdown < 10 and cTime > 0):
                        line = str(g_iCountdown)
                elif (g_iCountdown > 10 and g_iCountdown%10 == 0):
                        line = str(g_iCountdown)
                if line:
                        pSequence = App.TGSequence_Create()
                        pAction = App.TGScriptAction_Create(__name__, "SayString", line, 1)
                        pSequence.AppendAction(pAction)
                        pSequence.Play()


	g_iCountdown = g_iCountdown - 1
	

def FinallyDie():
	debug(__name__ + ", FinallyDie")
	global g_iCountdown, SDpPlayer
	
	g_iCountdown = -1
	MySelfDestructCaller = None
	
	#print("Now we kill us")
	if hasattr(SDpPlayer, "GetHull"):
		SDpPlayer.DestroySystem(SDpPlayer.GetHull())


def CancelSelfDestruct():
	debug(__name__ + ", CancelSelfDestruct")
	global g_iCountdown, SDpPlayer, g_pSaffi
	
	# set it to -2: lock it so all calls from MySelfDestruct() will land in /dev/null
	g_iCountdown = -2
	SDpPlayer = None
	
	if g_pSaffi:
		g_pSaffi.SpeakLine(g_pSaffi.GetDatabase(),"SelfDestructCancel")
		g_pSaffi.SpeakLine(g_pSaffi.GetDatabase(),"SaffiCommand")


def Restart():
	debug(__name__ + ", Restart")
	global g_iCountdown
	global SDpPlayer
	
	if ( g_iCountdown > -1 ):
		CancelSelfDestruct()
		SDpPlayer = None


def SetSDTimer(pObject, pEvent):
    debug(__name__ + ", SetSDTimer")
    global pButtonSDTimer, cTime, g_iCountdown
    if (g_iCountdown != -1):
        return
    cTime = cTime + 10
    if (cTime == 130):
        cTime = 0
    pButtonSDTimer.SetName(App.TGString("Time: " + str(cTime)))
