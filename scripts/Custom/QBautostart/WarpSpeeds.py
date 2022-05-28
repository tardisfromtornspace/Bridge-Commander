from bcdebug import debug
import App
import MissionLib
import Libs.LibEngineering
import Libs.LibWarp
import BridgeHandlers
from Libs.LibWarp import dCurWarpSpeeds, SetCurWarpSpeed, GetMaxWarp, ProcessMessageHandler, DeWarp

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.2",
                "needBridge": 0
            }


sMasterButtonName = "Warp Speed"


def GetMasterButton():
	debug(__name__ + ", GetMasterButton")
	pHelmMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
	pMasterButton = Libs.LibEngineering.GetButton(sMasterButtonName, pHelmMenu)
	if not pMasterButton:
		pMasterButton = App.STCharacterMenu_CreateW(App.TGString(sMasterButtonName))
		pHelmMenu.AddChild(pMasterButton)
	return pMasterButton
	

def SetPlayerWarpSpeed(pObject, pEvent):
	debug(__name__ + ", SetPlayerWarpSpeed")
	pPlayer = MissionLib.GetPlayer()
	iSpeed = pEvent.GetInt()
	pMasterButton = GetMasterButton()
	
	SetCurWarpSpeed(pPlayer, iSpeed)
	pMasterButton.Close()
	

def SetupButtons():
	# replaced by CWP 2.0
	debug(__name__ + ", SetupButtons")
	return
	pMasterButton = GetMasterButton()
	pMasterButton.KillChildren()
	iMaxSpeed = int(GetMaxWarp(MissionLib.GetPlayer()))
	
	for iSpeed in range(iMaxSpeed):
		iSpeed = iMaxSpeed - iSpeed
		Libs.LibEngineering.CreateMenuButton("Warp " + str(iSpeed), "Helm", __name__ + ".SetPlayerWarpSpeed", iSpeed, pMasterButton)


def DeWarp2(pObject, pEvent):
	debug(__name__ + ", DeWarp2")
	pPlayer = MissionLib.GetPlayer()
	
	BridgeHandlers.DropMenusTurnBack()
	Libs.LibWarp.DeWarp(pPlayer)
	

def EnterSet(pObject, pEvent):
	debug(__name__ + ", EnterSet")
	pPlayer = MissionLib.GetPlayer()
	if not pPlayer:
		return
	pSet = pPlayer.GetContainingSet()
	pMenu = Libs.LibEngineering.GetBridgeMenu("Engineer")
	pButton = Libs.LibEngineering.GetButton("deWarp", pMenu)
	
	if pSet and pSet.GetName() == "warp" and not pButton:
		Libs.LibEngineering.CreateMenuButton("deWarp", "Engineer", __name__ + ".DeWarp2")
	elif pButton:
		pMenu.DeleteChild(pButton)
	
	pObject.CallNextHandler(pEvent)
	

def SubsystemStateChanged(pObject, pEvent):
	debug(__name__ + ", SubsystemStateChanged")
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	pSubsystem = pEvent.GetSource()

	if pShip and pSubsystem:
		pWarp = pShip.GetWarpEngineSubsystem()
		
		if pWarp and pWarp.GetWarpState() == App.WarpEngineSubsystem.WES_WARPING and pSubsystem.IsTypeOf(App.CT_IMPULSE_ENGINE_SUBSYSTEM):
			pShip.GetImpulseEngineSubsystem().TurnOff()
	
	pObject.CallNextHandler(pEvent)

	
def init():
	debug(__name__ + ", init")
	SetupButtons()
	dCurWarpSpeeds = {}
	
	if App.g_kUtopiaModule.IsMultiplayer():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_NETWORK_MESSAGE_EVENT, MissionLib.GetMission(), __name__ + ".ProcessMessageHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, MissionLib.GetMission(), __name__ + ".EnterSet")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_POWER_CHANGED, MissionLib.GetMission(), __name__ + ".SubsystemStateChanged")
	
	
def Restart():
	debug(__name__ + ", Restart")
	SetupButtons()
	dCurWarpSpeeds = {}


def NewPlayerShip():
	debug(__name__ + ", NewPlayerShip")
	SetupButtons()
	
