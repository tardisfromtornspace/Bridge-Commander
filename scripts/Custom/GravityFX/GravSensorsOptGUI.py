################################################################
#######  GravSensorsOptGUI Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is the script that handles the Gravity Sensors Menu GUI in-game,
# and relative things
####################################################################
import App
import MissionLib
import Custom.GravityFX.Logger
from GravityFXlib import *
from ListLib import *
GUILIB = __import__('GravityFXguilib')
Astrometrics = __import__('Custom.GravityFX.AstrometricsGUI')

pGUICreator = None
ET_GSO = None
ET_3D_MAP_HANDLER = None
eRefresh = None
WellGlowList = []
Logger = None
CGWplayerID = 0

def CreateGSOGUI():
	global pGUICreator, ET_GSO, eRefresh, Logger
	try:
		pGUICreator = GUILIB.GUICreator()
		pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
		pBridge = App.g_kSetManager.GetSet('bridge')
		pScience = App.CharacterClass_GetObject(pBridge, "Science")
		pScienceMenu = pScience.GetMenu()
		if GetConfigValue("LogGravSensors"):
			Logger = Custom.GravityFX.Logger.LogCreator("Grav Sensors Logger", "scripts\Custom\GravityFX\Logs\GravSensorsLOG.txt")
			Logger.LogString("Initialized Grav Sensors logger")
		else:
			Logger = Custom.GravityFX.Logger.DummyLogger()

		ET_GSO = GUILIB.GetNextEventType()
		App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_GSO, pMission, __name__+".GSOOpenClose")

		pGUICreator.ButtonCreator.CreateButton("Gravity Sensors Options", ET_GSO, None, 1, pScienceMenu)
		
		pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__+".GSOClose")

		eRefresh = RefreshEventHandler(UpdateGUI)
		
		Astrometrics.CreateAstroGUI()

		Logger.LogString("Created GSO GUI")
	except:
		LogError("CreateGSOGUI")

def GSOOpenClose(pObject, pEvent):
	try:
		pGSO = pGUICreator.GetElement("GSO Menu")
		if not pGSO:
			pGUICreator.SetInfoForName("GSO Menu", 0.1, 0.1, 0.3, 0.6, 0)
			pGUICreator.SetInfoForName("GWI Window", 0.4, 0.05, 0.52, 0.7, 0, 1)
			pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
			pGSO = pGUICreator.CreateWindow("GSO Menu", pTCW)
			pGWIW = pGUICreator.CreateWindow("GWI Window", pTCW)
			Logger.LogString("Created GSO Window / Menu")
			pGSO.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
			pGWIW.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
			CreateGSOContents()
		if pGSO.IsVisible():
			Logger.LogString("Showing GSO")
			pGUICreator.CloseElement("GSO Menu")
			pGUICreator.CloseElement("GWI Window")
		else:
			Logger.LogString("Closing GSO")
			pGUICreator.ShowElement("GSO Menu")
			pGUICreator.ShowElement("GWI Window")
	except:
		LogError("GSOOpenClose")

def CreateGSOContents():
	try:
		global CGWplayerID
		pGSO = pGUICreator.GetElement("GSO Menu")

		sName = ["Gravity Sensors Options Menu"]
		pGUICreator.SetInfoForName("GSO Menu Title", 0.07, 0.01)
		pGUICreator.CreateParagraph("GSO Menu Title", sName, pGSO)

		TTCGButtonDict = {'X': 0.0, 'Y': 0.05, 'WIDTH': 0.25, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateYesNoButton("Toggle Thrusters to Counter Gravity", None, __name__+".GSOToggleThrusters", GetConfigValue("ThrusterState"), pGSO, TTCGButtonDict, TTCGButtonDict)

		TMapButtonDict = {'X': 0.0, 'Y': 0.1, 'WIDTH': 0.25, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateButton("Toggle Map", None, __name__+".ToggleMap", 0, pGSO, TMapButtonDict, TMapButtonDict)

		SGW3DMButtonDict = {'X': 0.0, 'Y': 0.15, 'WIDTH': 0.25, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateYesNoButton("Show Gravity Wells on 3D Map", None, None, 0, pGSO, SGW3DMButtonDict, SGW3DMButtonDict)

		SGW3DMButtonDict = {'X': 0.0, 'Y': 0.2, 'WIDTH': 0.25, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateYesNoButton("Enable Astrometrics", None, None, 0, pGSO, SGW3DMButtonDict, SGW3DMButtonDict)

		STGIButtonDict = {'X': 0.0, 'Y': 0.25, 'WIDTH': 0.25, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateYesNoButton("Show Gravity Info on All Ships", None, None, 0, pGSO, STGIButtonDict, STGIButtonDict)

		CloseButtonDict = {'X': 0.0, 'Y': 0.5, 'WIDTH': 0.1, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateButton("Close", None, __name__+".GSOClose", 0, pGSO, CloseButtonDict , CloseButtonDict )

		pGWIW = pGUICreator.GetElement("GWI Window")
		sGWIName = ["Gravity Sensors Output"]
		pGUICreator.SetInfoForName("GWI Window Title", 0.19, 0.01)
		pGUICreator.CreateParagraph("GWI Window Title", sGWIName, pGWIW)

		pGUICreator.SetInfoForName("Gravity Wells Info", 0.0, 0.1)
		Logger.LogString("Created GSO Static Contents")
	except:
		LogError("CreateGSOContents")

def GSOClose(pObject, pEvent):
	try:
		pGUICreator.CloseElement("GSO Menu")  
		pGUICreator.CloseElement("GWI Window") 
		Logger.LogString("Closed GSO")
		pObject.CallNextHandler(pEvent)
	except:
		LogError("GSOClose")

def ToggleMap(pObject, pEvent):
	pTop = App.TopWindow_GetTopWindow()
	pTop.ToggleMapWindow()
	Logger.LogString("Toggled Map")


def GSOToggleThrusters(pObject, pEvent):
	try:
		pButton = pGUICreator.ButtonCreator.GetButtonByName("Toggle Thrusters to Counter Gravity")
		if pButton:
			App.g_kGravityManager.PlayerCounterGravity = pButton.IsChosen()
		Logger.LogString("Toggled Thrusters")
	except:
		LogError("GSOToggleThrusters")

def UpdateGUI(pObject, pEvent):
	try:
		global WellGlowList, MapIDlist, bMapContPurged
		UpdateWellInfoList()
		pMapWindow = Get3DMapWindow()
		pPlayer = MissionLib.GetPlayer()
		pButton = pGUICreator.ButtonCreator.GetButtonByName("Show Gravity Wells on 3D Map")
		if pMapWindow:
			if pMapWindow.IsWindowActive() == 0:
				if WellGlowList:
					for pWell in WellGlowList:
						DeleteObject(pWell)
					WellGlowList = []
			elif pMapWindow.IsWindowActive() == 1:
				if pButton and pButton.IsChosen():
					if not WellGlowList:
						WellGlowList = []
						for GW in App.g_kGravityManager.GravWellList:
							if not GW.CLASS == "Torp Grav Effect":
								pWellGlow = ShowGravityWellGlow(GW.Parent)
								WellGlowList.append(pWellGlow)
	except:
		LogError("UpdateGUI")
	
    
def UpdateWellInfoList():
	try:
		pGWIW = pGUICreator.GetElement("GWI Window")
		if not pGWIW:
			return
		if pGWIW.IsVisible():
			pGWIW.SetScrollViewHeight(25.0)       #  I really don't know if these arent working...
			pGWIW.SetUseScrolling(1)              #  I never tested it for sure.
			pPlayer = MissionLib.GetPlayer()
			if pPlayer == None:
				return
			pSTGIButton = pGUICreator.ButtonCreator.GetButtonByName("Show Gravity Info on All Ships")
			InfoList = App.g_kGravityManager.GetGravInfoOnShip(pPlayer)
			if pSTGIButton:
				if pSTGIButton.IsChosen():
					ShipList = App.g_kGravityManager.GetObjListInSet(1)
					for pShip in ShipList:
						if pShip and not pShip.GetObjID() == pPlayer.GetObjID():
							ShipInfoList = App.g_kGravityManager.GetGravInfoOnShip(pShip)
							InfoList.append(" ")
							for string in ShipInfoList:
								InfoList.append(string)
			pPara = pGUICreator.GetElement("Gravity Wells Info")
			if pPara:
				pGUICreator.UpdateParagraph("Gravity Wells Info", InfoList)		
			else:
				pGUICreator.CreateParagraph("Gravity Wells Info", InfoList, pGWIW)
	except:
		LogError("UpdateWellInfoList")

def MouseHandler(pObject, pEvent):
	try:
		pObject.CallNextHandler(pEvent)
		if pEvent.EventHandled() == 0:
			pEvent.SetHandled()
	except:
		LogError("MouseHandler")

def LogError(strFromFunc):
	import sys
	et = sys.exc_info()
	if strFromFunc == None:
		strFromFunc = "???"
	if Logger:
		Logger.LogException(et, "ERROR at "+strFromFunc)
	else:
		error = str(et[0])+": "+str(et[1])
		print "ERROR at "+strFromFunc+", details -> "+error