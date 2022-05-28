from bcdebug import debug
import App
import Lib.LibEngineering
import conf.ServerPass
import rexec
import MissionLib

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.1",
                "needBridge": 0
            }

MP_REMOTE_CONTROL_MSG = 198
g_lsCommand = []
g_iPlayersBlocked = []

NonSerializedObjects = (
"g_lsCommand",
"g_iPlayersBlocked",
)


def run(lsCommand):
	debug(__name__ + ", run")
	r_env = rexec.RExec()
	for sCommand in lsCommand:
		r_env.r_exec(sCommand)


def ProcessMessageHandler(pObject, pEvent):
	debug(__name__ + ", ProcessMessageHandler")
	global g_lsCommand, g_iPlayersBlocked
	
	pMessage = pEvent.GetMessage()
	if not App.IsNull(pMessage):
		kStream = pMessage.GetBufferStream();
		cType = kStream.ReadChar();
		cType = ord(cType)

		if cType == MP_REMOTE_CONTROL_MSG:
			sPass = ""
			sCommand = ""
			
			# read the password
			iLen = kStream.ReadShort()
			for i in range(iLen):
				sPass = sPass + kStream.ReadChar()
			
			# now check the password
			if sPass == conf.ServerPass.ServerPass:
				# if pass ok, read command line
				iLen = kStream.ReadShort()
				for i in range(iLen):
					sCommand = sCommand + kStream.ReadChar()
				g_lsCommand.append(sCommand)
				
				# read mode
				iMode = kStream.ReadInt()
				# if mode 1 execute now
				if iMode == 1:
					run(g_lsCommand)
					g_lsCommand = []
			# password not ok, block the sender for 60 seconds
			else:
				iSender = pMessage.GetFromID()
				g_iPlayersBlocked.append(iSender)
				
				# unblock
				pSequence = App.TGSequence_Create()
				pAction = App.TGScriptAction_Create(__name__, "UnBlock", iSender)
				pSequence.AppendAction(pAction, 60)
				pSequence.Play()
			
	kStream.Close()


def UnBlock(pAction, iSender):
	debug(__name__ + ", UnBlock")
	global g_iPlayersBlocked
	if iSender in g_iPlayersBlocked:
		g_iPlayersBlocked.remove(iSender)
	return 0


def init():
	debug(__name__ + ", init")
	global g_lsCommand, g_iPlayersBlocked
	g_lsCommand = []
	g_iPlayersBlocked = []
	
	if App.g_kUtopiaModule.IsMultiplayer() and App.g_kUtopiaModule.IsHost() and conf.ServerPass.ServerPass:
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, MissionLib.GetMission(), __name__ + ".ProcessMessageHandler")
