from bcdebug import debug
import App
import nt
import MissionLib
import string
import Foundation
import Lib.LibEngineering
from Libs.LibConstruct import SendMPNewMode, SendMPNewModeSet, SendMPAppendToQueue, SendMPRemoveFromQueue, SendMPShipInConstructQueue
pTimerProcess = None
MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de & \"cnotsch\" c.notsch@gmx.at (patch)",
                "Version": "0.3",
                "needBridge": 0
            }


CONSTRUCT_CONF_DIR = "scripts/Custom/QBautostart/conf/Construct/"
MP_CONSTRUCT_MSG = 207
g_dPlugins = {}

NonSerializedObjects = (
"g_dPlugins",
)

def LoopPermissionToStart(pObject, pEvent):
	debug(__name__ + ", LoopPermissionToStart")
	myEvent = Lib.LibEngineering.GetEngineeringNextEventType()
	MissionLib.CreateTimer(myEvent, __name__ + ".LoopPermissionToStart", App.g_kUtopiaModule.GetGameTime() + 0.5, 0, 0)
	if not g_dPlugins:
		return
	first = None
	setnext = None
	done = 0
	ships = 0
	for plugin in g_dPlugins.keys():
		plugincontent = g_dPlugins[plugin].dConstructors
		ships = ships + len(plugincontent)
	if ships == 0:
		return
	for plugin in g_dPlugins.keys():
		plugincontent = g_dPlugins[plugin].dConstructors
		for ship in plugincontent.keys():
			shipconstructor = plugincontent[ship]
			if ships == 1:
				plugincontent[plugincontent.keys()[0]].SetPerMissionToStart(1)
				return
			if first == None:
				first = shipconstructor
			if shipconstructor.GetPerMissionToStart() == 1:
				setnext = shipconstructor
				shipconstructor.SetPerMissionToStart(0)
			#print shipconstructor.pConstructingShip.GetName() , shipconstructor.GetPerMissionToStart()
			if setnext != None and setnext != shipconstructor:
				shipconstructor.SetPerMissionToStart(1)
				setnext = None
				done = 1
	if setnext != None or done != 1:
		if first:
			first.SetPerMissionToStart(1)
		setnext = None
		first = None
		done = 0

def GetConstructInstanceFor(pShip, iSelectedDock = None):        
	debug(__name__ + ", GetConstructInstanceFor")
	if iSelectedDock == None:
		return None
       	sShipType = pShip.GetScript()
        if sShipType and g_dPlugins.has_key(sShipType):
                mod = g_dPlugins[sShipType]
                if mod.dConstructors.has_key(pShip.GetName()):
                        return mod.dConstructors[pShip.GetName()]
		elif mod.dConstructors.has_key(pShip.GetName() + 'Dock' + str(iSelectedDock)):
			return mod.dConstructors[pShip.GetName() + 'Dock' + str(iSelectedDock)]
        return None
def GetNumDocks(pShip):
       	debug(__name__ + ", GetNumDocks")
       	sShipType = pShip.GetScript()
	if sShipType and g_dPlugins.has_key(sShipType):
		mod = g_dPlugins[sShipType]
		i = 1
		while mod.dConstructors.has_key(pShip.GetName() + 'Dock' + str(i)):
			i = i + 1
		return i - 1

def isConstructing(pShip):
        debug(__name__ + ", isConstructing")
        pConstructor = GetConstructInstanceFor(pShip)
        if pConstructor and pConstructor.GetMode() == "Construct":
                return 1
        return 0


def RequestDock(pShip):
        debug(__name__ + ", RequestDock")
        pConstructor = GetConstructInstanceFor(pShip)
        if pConstructor:
                pConstructor.SetMode("Repair")
        

def LoadPluginDir():
	debug(__name__ + ", LoadPluginDir")
	global g_dPlugins
	
	g_dPlugins = {}
	list = nt.listdir(CONSTRUCT_CONF_DIR)
	
        for plugin in list:
                s = string.split(plugin, '.')
                sExtension = s[-1]
                sPluginName = string.join(s[:-1], '.')

		if sPluginName != "__init__" and sExtension == "py":
			sPluginModule = "BCROOT." + string.replace(CONSTRUCT_CONF_DIR, '/', '.') + sPluginName
			sPluginModule = string.replace(sPluginModule, "BCROOT.scripts.", "")
			
			mod = __import__(sPluginModule)
			sShip = mod.CONSTRUCT_SHIP
			g_dPlugins[sShip] = mod
			


def NewShip(pObject, pEvent):
	debug(__name__ + ", NewShip")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())

        if pShip:
                sShipType = pShip.GetScript()
                if sShipType and g_dPlugins.has_key(sShipType):
                        pSeq = App.TGSequence_Create()
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "StartConstruction", sShipType, pShip), 2)
                        pSeq.Play()

	pObject.CallNextHandler(pEvent)	



def StartConstruction(pAction, sShipType, pShip):
	debug(__name__ + ", StartConstruction")
	mod = g_dPlugins[sShipType]
	if pShip and pShip.GetContainingSet():
		mod.StartConstruction(pShip)
	return 0


def ProcessMessageHandler(pObject, pEvent):
	debug(__name__ + ", ProcessMessageHandler")
	pMessage = pEvent.GetMessage()
	if pMessage:
		kStream = pMessage.GetBufferStream()
		cType = kStream.ReadChar()
		cType = ord(cType)
		if cType == MP_CONSTRUCT_MSG:
			iMode = kStream.ReadInt()
			iShipID = kStream.ReadInt()
			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			
			# newMode
			if iMode == 1:
				pcMessage = ""
				iLen = kStream.ReadShort()
				for i in range(iLen):
					pcMessage = pcMessage + kStream.ReadChar()
				if App.g_kUtopiaModule.IsHost():
					SendMPNewMode(iShipID, pcMessage)
				pConstructor = GetConstructInstanceFor(pShip)
				if pConstructor:
					pConstructor.sNewMode = pcMessage
			# newMode set
			elif iMode == 2:
				pcMessage = ""
				iLen = kStream.ReadShort()
				for i in range(iLen):
					pcMessage = pcMessage + kStream.ReadChar()
				if App.g_kUtopiaModule.IsHost():
					SendMPNewModeSet(iShipID, pcMessage)
				pConstructor = GetConstructInstanceFor(pShip)
				if pConstructor:
					pConstructor.sMode = pcMessage
			# Add to queue
			elif iMode == 3:
				pcMessage = ""
				iLen = kStream.ReadShort()
				for i in range(iLen):
					pcMessage = pcMessage + kStream.ReadChar()
				if App.g_kUtopiaModule.IsHost():
					SendMPAppendToQueue(iShipID, pcMessage)
				pConstructor = GetConstructInstanceFor(pShip)
				if pConstructor:
					pConstructor.AddShipToConstructQueue(pcMessage, bSendNoMessage=1)
			# Remove from queue
			elif iMode == 4:
				iPos = kStream.ReadInt()
				if App.g_kUtopiaModule.IsHost():
					SendMPRemoveFromQueue(iShipID, iPos)
				pConstructor = GetConstructInstanceFor(pShip)
				if pConstructor:
					pConstructor.RemoveShipFromQueue(iPos, bSendNoMessage=1)
			# for new players only
			elif iMode == 5:
				pcMessage = ""
				iLen = kStream.ReadShort()
				for i in range(iLen):
					pcMessage = pcMessage + kStream.ReadChar()
				pConstructor = GetConstructInstanceFor(pShip)
				if pConstructor:
					pConstructor.AddShipToConstructQueue(pcMessage, bSendNoMessage=1)
		kStream.Close()


def NewPlayerHandler(pObject, pEvent):
	debug(__name__ + ", NewPlayerHandler")
	pObject.CallNextHandler(pEvent)
	
	lSets = App.g_kSetManager.GetAllSets()
	for pSet in lSets:
		for pShip in pSet.GetClassObjectList(App.CT_SHIP):
			pConstructor = GetConstructInstanceFor(pShip)
			if pConstructor:
				iShipID = pShip.GetObjID()
				SendMPNewMode(iShipID, pConstructor.sNewMode)
				SendMPNewModeSet(iShipID, pConstructor.sMode)
				for sShipType in pConstructor.GetConstructQueue():
					SendMPShipInConstructQueue(iShipID, sShipType)

def init():
        # check our Mutator
        debug(__name__ + ", init")
        if not Lib.LibEngineering.CheckActiveMutator("Construct Mod"):
                return

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return

	pMission = MissionLib.GetMission()
	LoadPluginDir()
	
	if App.g_kUtopiaModule.IsMultiplayer():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, MissionLib.GetMission(), __name__ + ".ProcessMessageHandler")
	
        if App.g_kUtopiaModule.IsMultiplayer():
		if App.g_kUtopiaModule.IsHost():
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NEW_PLAYER_IN_GAME, pMission, __name__ + ".NewPlayerHandler")
		else:
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".NewShip")

	App.g_kEventManager.AddBroadcastPythonFuncHandler(Foundation.TriggerDef.ET_FND_CREATE_SHIP, pMission, __name__ + ".NewShip")
	myEvent = Lib.LibEngineering.GetEngineeringNextEventType()
	MissionLib.CreateTimer(myEvent, __name__ + ".LoopPermissionToStart", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
