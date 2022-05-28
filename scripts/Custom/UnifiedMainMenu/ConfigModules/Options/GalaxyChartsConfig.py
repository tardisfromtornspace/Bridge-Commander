from bcdebug import debug
###############################################################################
## GalaxyCharts Config plugin for UMM			by USS Frontier
#######
# UMM plugin for Galaxy Charts mod.
# To allow easy customizability by users of key aspects of the mod.
################################################################################
import App
import Foundation
import string
import nt
from Custom.GravityFX.GravityFXguilib import *
import Custom.GalaxyCharts.Galaxy
import Custom.GalaxyCharts.LibStarstreaks
from Custom.GalaxyCharts.GalaxyMapGUI import GetTimeStrings

pModule = __import__("SavedConfigs.GalaxyChartsConfigValues")
pBar = None
pGUICreator = None
ET_BAR_SAVE = App.UtopiaModule_GetNextEventType()
pWin = None
pUDL = None
pSB = None
pLC1 = None
pLC2 = None
pLC3 = None
pLC4 = None
pLC5 = None
pLC6 = None
pSSO1 = None
pSSO2 = None
pSSO3 = None
pSSO4 = None
pSSO5 = None
pRDF1 = None
pRDF2 = None
pRDF3 = None
pRDF4 = None
pRDF5 = None
pRDF6 = None
pRDF7 = None
pRDF8 = None
pRDF9 = None
pRDF10 = None
pRDF11 = None
pRDF12 = None
pRDF13 = None
pRDF14 = None
pRDF15 = None
pRDF16 = None
pRDF17 = None
pRDF18 = None
pRDF19 = None
pWS1 = None
pWS2 = None
pWS3 = None
pWS4 = None
pWS5 = None
pWS6 = None

#####################################################
## Required Functions for UMM
#############################################
def GetName():
	debug(__name__ + ", GetName")
	return "Galaxy Charts Config"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	debug(__name__ + ", CreateMenu")
	global pGUICreator
	pGUICreator = GUICreator()
	CreateGalaChartsConfigMenu(pOptionsPane, pContentPanel)

	return App.TGPane_Create(0,0)
##########################################################


#####################################################
## Helper Functions
#############################################
def CreateGalaChartsConfigMenu(pOptionsPane, pContentPanel):
	debug(__name__ + ", CreateGalaChartsConfigMenu")
	global ET_BAR_SAVE, pBar, pWin, pUDL, pSB, pLC1, pLC2, pLC3, pLC4, pLC5, pLC6, pSSO1, pSSO2, pSSO3, pSSO4, pSSO5
	global pRDF1, pRDF2, pRDF3, pRDF4, pRDF5, pRDF6, pRDF7, pRDF8, pRDF9, pRDF10, pRDF11, pRDF12
	global pRDF13, pRDF14, pRDF15, pRDF16, pRDF17, pRDF18, pRDF19
	global pWS1, pWS2, pWS3, pWS4, pWS5, pWS6

	# Create Window for set User Time Factor
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
	pGUICreator.SetInfoForName("Galaxy Charts Config", 0.0, 0.0, 0.33, 0.35, 1)
	pWin = pGUICreator.CreateWindow("Galaxy Charts Config", pContentPanel)
	pWin.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
	pWin.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
	CreateWindowContent()

	# Create Yes/No button to set use default locations
	fValue = pModule.SetDefaultLocs
	UDLButtonDict = {'X': 0.0, 'Y': 0.35, 'WIDTH': 0.33, 'HEIGTH': 0.03}
	pUDL = pGUICreator.ButtonCreator.CreateYesNoButton("Use Default Locations?", ET_BAR_SAVE, None, fValue, pContentPanel, UDLButtonDict, UDLButtonDict)	

	fValue = pModule.ShowBanners
	SBButtonDict = {'X': 0.0, 'Y': 0.38, 'WIDTH': 0.33, 'HEIGTH': 0.03}
	pSB = pGUICreator.ButtonCreator.CreateYesNoButton("Show Text Banners?", ET_BAR_SAVE, None, fValue, pContentPanel, SBButtonDict, SBButtonDict)	


	###############
	# Create Menu/button to choose starstreaks option
	pSSMenu = CreateCharMenu("Star Streaks Options", pContentPanel)

	fValue = pModule.Starstreaks.MaxPulseUpdate
	SSButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pSSO1 = pGUICreator.ButtonCreator.CreateBar("Pulse Update Delay", ET_BAR_SAVE, None, fValue, [1.0, 10.0], 4.0, 0, pSSMenu, SSButtonDict, SSButtonDict)
	pSSO1.SetKeyInterval(1.0)

	fValue = pModule.Starstreaks.StreaksPerPulse
	SSButtonDict = {'X': 0.0, 'Y': 0.032, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pSSO2 = pGUICreator.ButtonCreator.CreateBar("How Many Streaks Per Pulse", ET_BAR_SAVE, None, fValue, [10.0, 500.0], 50.0, 0, pSSMenu, SSButtonDict, SSButtonDict)
	pSSO2.SetKeyInterval(1.0)

	fValue = pModule.Starstreaks.StreakDuration
	SSButtonDict = {'X': 0.0, 'Y': 0.064, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pSSO3 = pGUICreator.ButtonCreator.CreateBar("Duration of a Streak", ET_BAR_SAVE, None, fValue, [5.0, 60.0], 13.0, 0, pSSMenu, SSButtonDict, SSButtonDict)
	pSSO3.SetKeyInterval(1.0)

	fValue = pModule.Starstreaks.ForwardProject
	SSButtonDict = {'X': 0.0, 'Y': 0.096, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pSSO4 = pGUICreator.ButtonCreator.CreateBar("Front Projection Distance", ET_BAR_SAVE, None, fValue, [10.0, 600.0], 50.0, 0, pSSMenu, SSButtonDict, SSButtonDict)
	pSSO4.SetKeyInterval(1.0)

	fValue = pModule.Starstreaks.SizeMultiplier
	SSButtonDict = {'X': 0.0, 'Y': 0.128, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pSSO5 = pGUICreator.ButtonCreator.CreateBar("Streaks Proximity To Ship", ET_BAR_SAVE, None, fValue, [1.0, 30.0], 3.0, 0, pSSMenu, SSButtonDict, SSButtonDict)
	pSSO5.SetKeyInterval(1.0)

	###############
	# Create Menu/button to choose random defence force option
	pRDFMenu = CreateCharMenu("Random Defence Force Options", pContentPanel)

	fValue = pModule.RandomDefenceForce.UseRDF
	RDFButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF1 = pGUICreator.ButtonCreator.CreateYesNoButton("Enable RDF", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.AffectAI
	RDFButtonDict = {'X': 0.0, 'Y': 0.032, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF2 = pGUICreator.ButtonCreator.CreateYesNoButton("Affect AI Ships", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.DetectionChance
	RDFButtonDict = {'X': 0.0, 'Y': 0.064, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF3 = pGUICreator.ButtonCreator.CreateBar("Chance Of Detection", ET_BAR_SAVE, None, fValue, [0.0, 100.0], 100.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF3.SetKeyInterval(0.1)

	fValue = pModule.RandomDefenceForce.UsePeace
	RDFButtonDict = {'X': 0.0, 'Y': 0.096, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF4 = pGUICreator.ButtonCreator.CreateYesNoButton("Peace Value affects Chance?", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.UseStrategic
	RDFButtonDict = {'X': 0.0, 'Y': 0.128, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF5 = pGUICreator.ButtonCreator.CreateYesNoButton("Strategic Value affects Chance?", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.UseEconomic
	RDFButtonDict = {'X': 0.0, 'Y': 0.16, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF6 = pGUICreator.ButtonCreator.CreateYesNoButton("Economic Value  affects Chance?", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.CloakCounts
	RDFButtonDict = {'X': 0.0, 'Y': 0.192, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF7 = pGUICreator.ButtonCreator.CreateYesNoButton("Cloaking affects Chance?", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.UseDefence
	RDFButtonDict = {'X': 0.0, 'Y': 0.224, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF8 = pGUICreator.ButtonCreator.CreateYesNoButton("Use Default Defence of a Set", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.MinNumShips
	RDFButtonDict = {'X': 0.0, 'Y': 0.256, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF9 = pGUICreator.ButtonCreator.CreateBar("Minimum Number of Ships", ET_BAR_SAVE, None, fValue, [1.0, 10.0], 2.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF9.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MaxNumShips
	RDFButtonDict = {'X': 0.0, 'Y': 0.288, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF10 = pGUICreator.ButtonCreator.CreateBar("Maximum Number of Ships", ET_BAR_SAVE, None, fValue, [1.0, 20.0], 4.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF10.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MinReinShips
	RDFButtonDict = {'X': 0.0, 'Y': 0.32, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF11 = pGUICreator.ButtonCreator.CreateBar("Min Reinforcements Ships", ET_BAR_SAVE, None, fValue, [1.0, 10.0], 2.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF11.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MaxReinShips
	RDFButtonDict = {'X': 0.0, 'Y': 0.352, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF12 = pGUICreator.ButtonCreator.CreateBar("Max Reinforcements Ships", ET_BAR_SAVE, None, fValue, [1.0, 20.0], 4.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF12.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.NumOfReins
	RDFButtonDict = {'X': 0.0, 'Y': 0.384, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF13 = pGUICreator.ButtonCreator.CreateBar("Num of Reinforcements Waves", ET_BAR_SAVE, None, fValue, [0.0, 15.0], 3.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF13.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MinTimeToEnter
	RDFButtonDict = {'X': 0.0, 'Y': 0.416, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF14 = pGUICreator.ButtonCreator.CreateBar("Min Initial Time To Enter", ET_BAR_SAVE, None, fValue, [1.0, 60.0], 10.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF14.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MaxTimeToEnter
	RDFButtonDict = {'X': 0.0, 'Y': 0.448, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF15 = pGUICreator.ButtonCreator.CreateBar("Max Initial Time To Enter", ET_BAR_SAVE, None, fValue, [1.0, 120.0], 30.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF15.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MinTimeToRein
	RDFButtonDict = {'X': 0.0, 'Y': 0.48, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF16 = pGUICreator.ButtonCreator.CreateBar("Min Reinforcement Time Delay", ET_BAR_SAVE, None, fValue, [1.0, 60.0], 20.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF16.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.MaxTimeToRein
	RDFButtonDict = {'X': 0.0, 'Y': 0.512, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF17 = pGUICreator.ButtonCreator.CreateBar("Max Reinforcement Time Delay", ET_BAR_SAVE, None, fValue, [1.0, 180.0], 40.0, 0, pRDFMenu, RDFButtonDict, RDFButtonDict)
	pRDF17.SetKeyInterval(1.0)

	fValue = pModule.RandomDefenceForce.IncludeGodShips
	RDFButtonDict = {'X': 0.0, 'Y': 0.544, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF18 = pGUICreator.ButtonCreator.CreateYesNoButton("Include God Ships?", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	fValue = pModule.RandomDefenceForce.IncludeEscorts
	RDFButtonDict = {'X': 0.0, 'Y': 0.576, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pRDF19 = pGUICreator.ButtonCreator.CreateYesNoButton("Include Escorts?", ET_BAR_SAVE, None, fValue, pRDFMenu, RDFButtonDict, RDFButtonDict)

	############
	# Create Menu/button to choose logger selection
	pWSMenu = CreateCharMenu("War Simulator Options", pContentPanel)

	fValue = pModule.WarSimulator.UseWarSim
	WSButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pWS1 = pGUICreator.ButtonCreator.CreateYesNoButton("Use War Simulator?", ET_BAR_SAVE, None, fValue, pWSMenu, WSButtonDict, WSButtonDict)

	fValue = pModule.WarSimulator.PlayerHasRaceCommand
	WSButtonDict = {'X': 0.0, 'Y': 0.032, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pWS2 = pGUICreator.ButtonCreator.CreateYesNoButton("Player Has Race Command?", ET_BAR_SAVE, None, fValue, pWSMenu, WSButtonDict, WSButtonDict)

	fValue = pModule.WarSimulator.EconomicModifier
	WSButtonDict = {'X': 0.0, 'Y': 0.064, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pWS3 = pGUICreator.ButtonCreator.CreateBar("Economic Income Modifier", ET_BAR_SAVE, None, fValue, [0.01, 10.0], 1.0, 0, pWSMenu, WSButtonDict, WSButtonDict)
	pWS3.SetKeyInterval(0.1)

	fValue = pModule.WarSimulator.RAFModifier
	WSButtonDict = {'X': 0.0, 'Y': 0.096, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pWS4 = pGUICreator.ButtonCreator.CreateBar("RAF Chance Modifier", ET_BAR_SAVE, None, fValue, [0.0, 200.0], 100.0, 0, pWSMenu, WSButtonDict, WSButtonDict)
	pWS4.SetKeyInterval(1.0)

	fValue = pModule.WarSimulator.MaxInitShips
	WSButtonDict = {'X': 0.0, 'Y': 0.128, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pWS5 = pGUICreator.ButtonCreator.CreateBar("Max Init Ships", ET_BAR_SAVE, None, fValue, [0.0, 20.0], 10.0, 0, pWSMenu, WSButtonDict, WSButtonDict)
	pWS5.SetKeyInterval(1.0)

	fValue = pModule.WarSimulator.MaxReinShips
	WSButtonDict = {'X': 0.0, 'Y': 0.16, 'WIDTH': 0.3, 'HEIGTH': 0.032}
	pWS6 = pGUICreator.ButtonCreator.CreateBar("Max Rein Ships", ET_BAR_SAVE, None, fValue, [0.0, 30.0], 15.0, 0, pWSMenu, WSButtonDict, WSButtonDict)
	pWS6.SetKeyInterval(1.0)


	############
	# Create Menu/button to choose logger selection
	pGCLSMenu = CreateCharMenu("Galaxy Charts Logger Support", pContentPanel)

	fValue = pModule.LoggerConfig.LogChaser
	LCButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pLC1 = pGUICreator.ButtonCreator.CreateYesNoButton("Log Chaser Class", ET_BAR_SAVE, None, fValue, pGCLSMenu, LCButtonDict, LCButtonDict)
	fValue = pModule.LoggerConfig.LogTravel
	LCButtonDict = {'X': 0.0, 'Y': 0.03, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pLC2 = pGUICreator.ButtonCreator.CreateYesNoButton("Log Travel Class", ET_BAR_SAVE, None, fValue, pGCLSMenu, LCButtonDict, LCButtonDict)
	fValue = pModule.LoggerConfig.LogGalaxy
	LCButtonDict = {'X': 0.0, 'Y': 0.06, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pLC3 = pGUICreator.ButtonCreator.CreateYesNoButton("Log Galaxy Script", ET_BAR_SAVE, None, fValue, pGCLSMenu, LCButtonDict, LCButtonDict)
	fValue = pModule.LoggerConfig.LogTravelerAI
	LCButtonDict = {'X': 0.0, 'Y': 0.09, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pLC4 = pGUICreator.ButtonCreator.CreateYesNoButton("Log TravelerAI Script", ET_BAR_SAVE, None, fValue, pGCLSMenu, LCButtonDict, LCButtonDict)
	fValue = pModule.LoggerConfig.LogTWS
	LCButtonDict = {'X': 0.0, 'Y': 0.12, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pLC5 = pGUICreator.ButtonCreator.CreateYesNoButton("Log TravelerWarpSequence Class", ET_BAR_SAVE, None, fValue, pGCLSMenu, LCButtonDict, LCButtonDict)
	fValue = pModule.LoggerConfig.LogRDF
	LCButtonDict = {'X': 0.0, 'Y': 0.15, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pLC6 = pGUICreator.ButtonCreator.CreateYesNoButton("Log Random Defence Force", ET_BAR_SAVE, None, fValue, pGCLSMenu, LCButtonDict, LCButtonDict)

	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_BAR_SAVE, App.TopWindow_GetTopWindow(), __name__+".StarstreakOptionChange")

	##  create the set default values button.
	RDCButtonDict = {'X': 0.0, 'Y': 0.35, 'WIDTH': 0.33, 'HEIGTH': 0.03}
	pGUICreator.ButtonCreator.CreateButton("Reset Default Configuration", None, __name__ + ".ResetDefaults", 1, pContentPanel, None, RDCButtonDict)	

	return pContentPanel

def OpenCloseWindow(pObject, pEvent):
	debug(__name__ + ", OpenCloseWindow")
	pWin = pGUICreator.GetElement("Galaxy Charts Config")
	if pWin.IsVisible():
		pGUICreator.CloseElement("Galaxy Charts Config")
	else:
		pGUICreator.ShowElement("Galaxy Charts Config")

def CloseWindow(pObject, pEvent):
	debug(__name__ + ", CloseWindow")
	pGUICreator.CloseElement("Galaxy Charts Config")

def CreateWindowContent():
	debug(__name__ + ", CreateWindowContent")
	global pBar, pWin
	fMax = Custom.GalaxyCharts.Galaxy.GetTimeToWarp(100000.0, App.g_kTravelManager.ConvertTravelTypeSpeedIntoCs("Warp", 9.99))
	nValue = pModule.UserTimeFactor

	pGUICreator.SetInfoForName("TextInput Title", 0.0, 0.0)
	pGUICreator.CreateParagraph("TextInput Title", ["Time Factor:"], pWin)
	
	pGUICreator.SetInfoForName("Time Para", 0.0, 0.1)
	sList = GetTimeStrings(nValue)
	sList[0] = "Time to travel 100000 lightyears at \nwarp 9.99 :"
	pGUICreator.CreateParagraph("Time Para", sList, pWin)

	if nValue == fMax:
		pDefault = App.TGString("MAXIMUM")
	elif nValue == 1.0:
		pDefault = App.TGString("MINIMUM")
	else:
		pDefault = App.TGString(str(nValue))
	iMaxCharNum = 30
	pBar = pGUICreator.ButtonCreator.CreateTextInput("", pWin, pDefault, 0.3, 0.0, "Time Factor T", iMaxCharNum, Coords = {'X': 0.0, 'Y': 0.035})
	pBar[0].AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".BarUpdate")

# this actually shouldn't be called "BarUpdate" anymore, because it's the function which is called when there is text input
# in the text input box, but whatever lol
def BarUpdate(pObject, pEvent):
	debug(__name__ + ", BarUpdate")
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)
	pModule.UserTimeFactor = GetTimeFactor()
	sList = GetTimeStrings(pModule.UserTimeFactor)
	sList[0] = "Time to travel 100000 lightyears at \nwarp 9.99 :"
	pGUICreator.UpdateParagraph("Time Para", sList)
	SaveGalaChartsConfig(None, None)


def GetTimeFactor():
	debug(__name__ + ", GetTimeFactor")
	global pBar
	fMax = Custom.GalaxyCharts.Galaxy.GetTimeToWarp(100000.0, App.g_kTravelManager.ConvertTravelTypeSpeedIntoCs("Warp", 9.99))
	sText = pBar[1].GetCString()
	try:
		fValue = float(sText)
		if fValue < 1.0:
			fValue = 1.0
		if fValue > fMax:
			fValue = fMax
	except:
		if sText == "MAXIMUM" or sText == "maximum":
			fValue = fMax
		elif sText == "MINIMUM" or sText == "minimum":
			fValue = 1.0
		else:
			fValue = 60.0
	return fValue

def MouseHandler(pObject, pEvent):
	debug(__name__ + ", MouseHandler")
	pObject.CallNextHandler(pEvent)


def KeyHandler(pObject, pEvent):
	debug(__name__ + ", KeyHandler")
	pObject.CallNextHandler(pEvent)


iTimerID = None
ET_TIMER_SAVE = App.UtopiaModule_GetNextEventType()
bCreatedHandler = 0
def StarstreakOptionChange(pObject, pEvent):
	debug(__name__ + ", StarstreakOptionChange")
	global ET_TIMER_SAVE, iTimerID, bCreatedHandler
	if iTimerID == None:
		pTopWindow = App.TopWindow_GetTopWindow()
		pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
		if bCreatedHandler == 0:
			pOptionsWindow.AddPythonFuncHandlerForInstance(ET_TIMER_SAVE, __name__+".SSOsaveNow")
			bCreatedHandler = 1
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(ET_TIMER_SAVE )
		pEvent.SetDestination(pOptionsWindow)
		pTimer = App.TGTimer_Create()
		pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + 1.0)
		pTimer.SetDelay(0.0)
		pTimer.SetDuration(0.0)
		pTimer.SetEvent(pEvent)
		App.g_kTimerManager.AddTimer(pTimer)
		iTimerID = pTimer.GetObjID()
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def SSOsaveNow(pObject, pEvent):
	debug(__name__ + ", SSOsaveNow")
	global iTimerID
	App.g_kTimerManager.DeleteTimer(iTimerID)
	iTimerID = None
	SaveGalaChartsConfig(None, None)
	Custom.GalaxyCharts.LibStarstreaks.UpdateConstants()
	#print "update lib starstreaks"
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def ResetDefaults(pObject, pEvent):
	# get our nice little big family of globals, might even not be needed, but at this point, it's already personal lol
	debug(__name__ + ", ResetDefaults")
	global pBar, pUDL, pSB, pLC1, pLC2, pLC3, pLC4, pLC5, pLC6, pSSO1, pSSO2, pSSO3, pSSO4, pSSO5
	global pRDF1, pRDF2, pRDF3, pRDF4, pRDF5, pRDF6, pRDF7, pRDF8, pRDF9, pRDF10, pRDF11
	global pRDF12, pRDF13, pRDF14, pRDF15, pRDF16, pRDF17, pRDF18, pRDF19
	global pWS1, pWS2, pWS3, pWS4, pWS5, pWS6

	# start setting the default values manually. 
	pBar[1].SetString("300.0")   # user time factor
	pUDL.SetChosen(1)    # use default locations
	pSB.SetChosen(1)    # show text banners

	pLC1.SetChosen(0)   # log chaser
	pLC2.SetChosen(0)   # log travel
	pLC3.SetChosen(0)   # log galaxy
	pLC4.SetChosen(0)   # log TravelerAI
	pLC5.SetChosen(0)   # log traveler warp sequence
	pLC6.SetChosen(0)   # log RDF

	pSSO1.SetValue(4.0)   # pulse update delay
	pSSO2.SetValue(50.0)   # how many streaks per pulse
	pSSO3.SetValue(13.0)   # duration of a streak
	pSSO4.SetValue(50.0)   # front projection dist
	pSSO5.SetValue(3.0)   # streaks proximity to the ship

	pRDF1.SetChosen(1)  # use RDF
	pRDF2.SetChosen(0)   # affect AI
	pRDF3.SetValue(100.0)   # chance
	pRDF4.SetChosen(1)   # use peace value
	pRDF5.SetChosen(1)   # use strategic
	pRDF6.SetChosen(1)   # use economic
	pRDF7.SetChosen(1)   # count cloak
	pRDF8.SetChosen(1)   # use default defence
	pRDF9.SetValue(2.0)   # min ships
	pRDF10.SetValue(4.0)  # max ships
	pRDF11.SetValue(2.0)  # min rein ships
	pRDF12.SetValue(4.0)  # max rein ships
	pRDF13.SetValue(3.0)  # rein waves
	pRDF14.SetValue(10.0)    # min time to enter
	pRDF15.SetValue(30.0)    # max time to enter
	pRDF16.SetValue(20.0)    # mix rein time
	pRDF17.SetValue(40.0)    # max rein time
	pRDF18.SetChosen(0)    # include god ships
	pRDF19.SetChosen(1)    # include escorts

	pWS1.SetChosen(1)   # use war sim
	pWS2.SetChosen(1)   # player has race command
	pWS3.SetValue(1.0)   # economic modifier
	pWS4.SetValue(100.0)   # RAF chance modifier
	pWS5.SetValue(10.0)   # Max initial ships
	pWS6.SetValue(15.0)   # max reinforcent ships
	
	# now we make a list of the numeric bars, to update their gauges so that after changing their value they'll
	# show their new given value too
	lBarsList = [pSSO1,pSSO2,pSSO3,pSSO4,pSSO5,pRDF3,pRDF9,pRDF10,pRDF11,pRDF12,pRDF13,pRDF14,pRDF15,pRDF16,pRDF17,pWS3,pWS4,pWS5,pWS6]
	for pBarProp in lBarsList:
		pBarProp.UpdateGauge()

	# finally, save the default values
	SaveGalaChartsConfig(None, None)
	# no need to call next handler here, we are the only (and should) be the only handler for this event


def SaveGalaChartsConfig(pObject, pEvent):
	debug(__name__ + ", SaveGalaChartsConfig")
	global pUDL, pSB, pLC1, pLC2, pLC3, pLC4, pLC5, pLC6, pSSO1, pSSO2, pSSO3, pSSO4, pSSO5
	global pRDF1, pRDF2, pRDF3, pRDF4, pRDF5, pRDF6, pRDF7, pRDF8, pRDF9, pRDF10, pRDF11
	global pRDF12, pRDF13, pRDF14, pRDF15, pRDF16, pRDF17, pRDF18, pRDF19
	global pWS1, pWS2, pWS3, pWS4, pWS5, pWS6
	ConfigPath  = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\GalaxyChartsConfigValues.py"
	file = nt.open(ConfigPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
	nt.write(file, "# Saved Configuration File for Galaxy Charts,   by USS Frontier" + "\n")
	nt.write(file, "UserTimeFactor = " + str(GetTimeFactor()) + "\n")
	nt.write(file, "SetDefaultLocs = " + str(pUDL.IsChosen()) + "\n")
	nt.write(file, "ShowBanners = " + str(pSB.IsChosen()) + "\n")
	nt.write(file, "class LoggerConfig:" + "\n")
	nt.write(file, "\tLogChaser = " + str(pLC1.IsChosen()) + "\n")
	nt.write(file, "\tLogTravel = " + str(pLC2.IsChosen()) + "\n")
	nt.write(file, "\tLogGalaxy = " + str(pLC3.IsChosen()) + "\n")
	nt.write(file, "\tLogTravelerAI = " + str(pLC4.IsChosen()) + "\n")
	nt.write(file, "\tLogTWS = " + str(pLC5.IsChosen()) + "\n")
	nt.write(file, "\tLogRDF = " + str(pLC6.IsChosen()) + "\n")
	nt.write(file, "class Starstreaks:" + "\n")
	nt.write(file, "\tMaxPulseUpdate = " + str(pSSO1.GetValue()) + "\n")
	nt.write(file, "\tStreaksPerPulse = " + str(pSSO2.GetValue()) + "\n")
	nt.write(file, "\tStreakDuration = " + str(pSSO3.GetValue()) + "\n")
	nt.write(file, "\tForwardProject = " + str(pSSO4.GetValue()) + "\n")
	nt.write(file, "\tSizeMultiplier = " + str(pSSO5.GetValue()) + "\n")
	nt.write(file, "class RandomDefenceForce:" + "\n")
	nt.write(file, "\tUseRDF = " +str(pRDF1.IsChosen()) + "\n")
	nt.write(file, "\tAffectAI = " +str(pRDF2.IsChosen()) + "\n")
	nt.write(file, "\tDetectionChance = " +str(pRDF3.GetValue()) + "\n")
	nt.write(file, "\tUsePeace = " +str(pRDF4.IsChosen()) + "\n")
	nt.write(file, "\tUseStrategic = " +str(pRDF5.IsChosen()) + "\n")
	nt.write(file, "\tUseEconomic = " +str(pRDF6.IsChosen()) + "\n")
	nt.write(file, "\tCloakCounts = " +str(pRDF7.IsChosen()) + "\n")
	nt.write(file, "\tUseDefence = " +str(pRDF8.IsChosen()) + "\n")
	nt.write(file, "\tMinNumShips = " +str(pRDF9.GetValue()) + "\n")
	nt.write(file, "\tMaxNumShips = " +str(pRDF10.GetValue()) + "\n")
	nt.write(file, "\tMinReinShips = " +str(pRDF11.GetValue()) + "\n")
	nt.write(file, "\tMaxReinShips = " +str(pRDF12.GetValue()) + "\n")
	nt.write(file, "\tNumOfReins = " +str(pRDF13.GetValue()) + "\n")
	nt.write(file, "\tMinTimeToEnter = " +str(pRDF14.GetValue()) + "\n")
	nt.write(file, "\tMaxTimeToEnter = " +str(pRDF15.GetValue()) + "\n")
	nt.write(file, "\tMinTimeToRein = " +str(pRDF16.GetValue()) + "\n")
	nt.write(file, "\tMaxTimeToRein = " +str(pRDF17.GetValue()) + "\n")
	nt.write(file, "\tIncludeGodShips = " +str(pRDF18.IsChosen()) + "\n")
	nt.write(file, "\tIncludeEscorts = " +str(pRDF19.IsChosen()) + "\n")
	nt.write(file, "class WarSimulator:" + "\n")
	nt.write(file, "\tUseWarSim = " +str(pWS1.IsChosen()) + "\n")
	nt.write(file, "\tPlayerHasRaceCommand = " +str(pWS2.IsChosen()) + "\n")
	nt.write(file, "\tEconomicModifier = " +str(pWS3.GetValue()) + "\n")
	nt.write(file, "\tRAFModifier = " +str(pWS4.GetValue()) + "\n")
	nt.write(file, "\tMaxInitShips = " +str(pWS5.GetValue()) + "\n")
	nt.write(file, "\tMaxReinShips = " +str(pWS6.GetValue()) + "\n")
	nt.close(file)


	pModule.UserTimeFactor = GetTimeFactor()
	pModule.SetDefaultLocs = pUDL.IsChosen()
	pModule.ShowBanners = pSB.IsChosen()
	pModule.LoggerConfig.LogChaser = pLC1.IsChosen()
	pModule.LoggerConfig.LogTravel = pLC2.IsChosen()
	pModule.LoggerConfig.LogGalaxy = pLC3.IsChosen()
	pModule.LoggerConfig.LogTravelerAI = pLC4.IsChosen()
	pModule.LoggerConfig.LogTWS = pLC5.IsChosen()
	pModule.LoggerConfig.LogRDF = pLC6.IsChosen()
	pModule.Starstreaks.MaxPulseUpdate = pSSO1.GetValue()
	pModule.Starstreaks.StreaksPerPulse = pSSO2.GetValue()
	pModule.Starstreaks.StreakDuration = pSSO3.GetValue()
	pModule.Starstreaks.ForwardProject = pSSO4.GetValue()
	pModule.Starstreaks.SizeMultiplier = pSSO5.GetValue()
	pModule.RandomDefenceForce.UseRDF = pRDF1.IsChosen()
	pModule.RandomDefenceForce.AffectAI = pRDF2.IsChosen()
	pModule.RandomDefenceForce.DetectionChance = pRDF3.GetValue()
	pModule.RandomDefenceForce.UsePeace = pRDF4.IsChosen()
	pModule.RandomDefenceForce.UseStrategic = pRDF5.IsChosen()
	pModule.RandomDefenceForce.UseEconomic = pRDF6.IsChosen()
	pModule.RandomDefenceForce.CloakCounts = pRDF7.IsChosen()
	pModule.RandomDefenceForce.UseDefence = pRDF8.IsChosen()
	pModule.RandomDefenceForce.MinNumShips = pRDF9.GetValue()
	pModule.RandomDefenceForce.MaxNumShips = pRDF10.GetValue()
	pModule.RandomDefenceForce.MinReinShips = pRDF11.GetValue()
	pModule.RandomDefenceForce.MaxReinShips = pRDF12.GetValue()
	pModule.RandomDefenceForce.NumOfReins = pRDF13.GetValue()
	pModule.RandomDefenceForce.MinTimeToEnter = pRDF14.GetValue()
	pModule.RandomDefenceForce.MaxTimeToEnter = pRDF15.GetValue()
	pModule.RandomDefenceForce.MinTimeToRein = pRDF16.GetValue()
	pModule.RandomDefenceForce.MaxTimeToRein = pRDF17.GetValue()
	pModule.RandomDefenceForce.IncludeGodShips = pRDF18.IsChosen()
	pModule.RandomDefenceForce.IncludeEscorts = pRDF19.IsChosen()
	pModule.WarSimulator.UseWarSim = pWS1.IsChosen()
	pModule.WarSimulator.PlayerHasRaceCommand = pWS2.IsChosen()
	pModule.WarSimulator.EconomicModifier = pWS3.GetValue()
	pModule.WarSimulator.RAFModifier = pWS4.GetValue()
	pModule.WarSimulator.MaxInitShips = pWS5.GetValue()
	pModule.WarSimulator.MaxReinShips = pWS6.GetValue()

	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)