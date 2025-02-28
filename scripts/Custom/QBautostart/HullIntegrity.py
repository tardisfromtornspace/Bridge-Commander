# Hull integrity

# by Sov
# Slightly tweaked by Alex SL Gato

# Modify, redistribute to your liking. Just remember to give credit where due.
sPath = "Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.AccessibilityConfigVals"
sCPath = "Custom.UnifiedMainMenu.ConfigModules.Options.AccessibilityConfig"

pModule = __import__(sPath)
pConfigModule = __import__(sCPath)

import App
import MissionLib
import string
import traceback

pText = None
pHealth = None
pTimer = None
pMission = None
pOriginalWidth = 1
pOriginalHeight = 1
firstTime = 1

globalVarList = {
	"ShowPercent" : 0,
	"ShowBar" : 1,
	"ShowFraction" : 0,
	"NumberDecimals" : 0,
	"RadixNotation" : ".",
	"sFont" : "Crillee",
	"FontSize": 5,
}

def CheckAndRefreshModule(variableList, pMyModule, theWay, issue=0): # Used when for example you had an incomplete BC Accesibility Config values
	if not pMyModule:
		pMyModule = __import__(theWay)
	elif pMyModule or issue > 0:
		global pModule
		reload (pModule)
		pMyModule = __import__(theWay)
		pModule = pMyModule

	global globalVarList
	if pMyModule != None and issue == 0:	
		for variable in globalVarList.keys():
			if hasattr(pMyModule, variable):
				globalVarList[variable] = getattr(pMyModule, variable)
			else:
				print theWay, " on cache has no ", variable, " attribute."
				issue = issue + 1

def ShipCheck(pObject, pEvent):
	print "Called reinit"
	global firstTime
	firstTime = 1

class ShipSwapCheckClass:
	def __init__(self, name):
		self.name = name
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		#self.AddHandler()

	def ShipCheck(self, pEvent): # Somehow I cannot call this function...
		print "Called reinit"
		global firstTime
		firstTime = 1
		return 0

	def AddHandler(self):
		self.RemoveHandler()
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, self.pEventHandler, __name__ + ".ShipCheck")

	def RemoveHandler(self):
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, self.pEventHandler, __name__ + ".ShipCheck")


shipSwapChecker = ShipSwapCheckClass("Ship Swap checker")

CheckAndRefreshModule(globalVarList, pModule, sPath, 0)

def init():
	CheckAndRefreshModule(globalVarList, pModule, sPath, 0)

	if pModule == None:
		return

	# Grab health gauge
	pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
	if not pTCW:
		return
	pDisplay = pTCW.GetShipDisplay()
	if not pDisplay:
		return

	global pHealth, firstTime
	pHealth = pDisplay.GetHealthGauge()
	if not pHealth:
		return

	firstTime = 1
	# This line hides the health gauge which is replaced by the percentage text
	if globalVarList["ShowBar"] == 0:
		pHealth.SetNotVisible(0)

	global pOriginalWidth, pOriginalHeight
	pOriginalWidth = pDisplay.GetWidth()
	pOriginalHeight = pDisplay.GetHeight()

	# Create the text
	global pText
	if globalVarList["ShowPercent"]:
		pText = App.TGParagraph_Create("Hull :          100%", 1.0, None, globalVarList["sFont"], globalVarList["FontSize"])
	elif globalVarList["ShowFraction"]:
		pText = App.TGParagraph_Create("Hull :          100/100", 1.0, None, globalVarList["sFont"], globalVarList["FontSize"])	
	
	if not pText:
		return

	print(pHealth.GetPosition) # Sov had this

	if globalVarList["ShowFraction"]:
		howRight = 0
	else:
		howRight = pHealth.GetRight() * 0.8 - pText.GetWidth()

	pDisplay.AddChild(pText, howRight, pHealth.GetBottom())

	# Decided to do the size change on the Active Watcher as the first time, so init only gathers data and appends these
	#newWidth = pOriginalWidth
	#if (1.05 * pText.GetWidth()) > newWidth:
	#	newWidth = pText.GetWidth() * 1.05 #pOriginalWidth + pText.GetWidth()/2.0
	#pDisplay.SetFixedSize(newWidth, (pOriginalHeight + pText.GetHeight()))
	#pHealth.Resize(pDisplay.GetMaximumInteriorWidth(), pHealth.GetHeight(), 0)
	pDisplay.InteriorChangedSize()	

        # When you change a player ship then initiate the script
	shipSwapChecker.AddHandler()

	global pTimer
	if not pTimer:
		pTimer = Watcher()

def exit():
	global pText, pHealth, pTimer
	pText = None
	pHealth = None
	pTimer = None
	shipSwapChecker.RemoveHandler()

class Watcher:
	def __init__(self):
		self.pTimer = None
		self.StartTiming()
	def StartTiming(self):
		if self.pTimer:
			return
		if not globalVarList["ShowPercent"] and not globalVarList["ShowFraction"]:
			return
		self.pTimer = App.PythonMethodProcess()
		self.pTimer.SetInstance(self)
		self.pTimer.SetFunction("Update")
		self.pTimer.SetDelay(1)
		self.pTimer.SetPriority(App.TimeSliceProcess.LOW)
	def Update(self, fTime):
		# TEST AREA - WHY? BECAUSE OF TELEPORTERS, THAT'S WHY
		# Grab health gauge
		#pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		#if not pTCW:
		#	return
		#pDisplay = pTCW.GetShipDisplay()
		#if not pDisplay:
		#	return
		# END OF TEST AREA

		pPlayer = MissionLib.GetPlayer()
		if not pPlayer:
			return

		global pText
		if not pText: # I'm sure this would need to change
			return

		pHull = pPlayer.GetHull()

		if not pHull or not hasattr(pHull, "GetMaxCondition"):
			return

		self.fHullCurr = pHull.GetCondition()
		self.fHullMax = pHull.GetMaxCondition()
		if not self.fHullCurr or not self.fHullMax or self.fHullMax == 0.0:
			return

		self.iExact = self.fHullCurr/self.fHullMax
		self.iCon = int(self.iExact * 100)
		
		infoString = ""
		
		if globalVarList["ShowPercent"]:
			auxPercString = ""
			if globalVarList["NumberDecimals"] > 0:
				self.iDec = string.zfill(int(self.iExact * 100 * (10**globalVarList["NumberDecimals"])) - int(self.iCon * (10**globalVarList["NumberDecimals"])), globalVarList["NumberDecimals"])
				auxPercString = auxPercString + str(globalVarList["RadixNotation"]) + str(self.iDec) 
			infoString = infoString + str(self.iCon) + auxPercString + "%"
			if not globalVarList["ShowFraction"]:
				infoString = "          " + infoString
			else:
				infoString = " " + infoString
		if globalVarList["ShowFraction"]:
			if self.fHullMax <= 1.0:
				signifDec = 6
			else:
				signifDec = globalVarList["NumberDecimals"]

			currHullAprox = int(self.fHullCurr) 
			maxHullAprox = int(self.fHullMax) 

			if signifDec >= 1:
				try:
					currHullDecAprox = string.zfill(int(self.fHullCurr * (10**signifDec))  - (currHullAprox * (10**signifDec)), signifDec)
				except:
					currHullDecAprox = ">=2^64"
				try:
					maxHullDecAprox = string.zfill(int(self.fHullMax * (10**signifDec))  - (maxHullAprox * (10**signifDec)), signifDec)
				except:
					maxHullDecAprox = ">=2^64"

				sCurrHull = str(currHullAprox) + str(globalVarList["RadixNotation"]) + str(currHullDecAprox)
				sMaxHull = str(maxHullAprox) + str(globalVarList["RadixNotation"]) + str(maxHullDecAprox)
			else:
				sCurrHull = str(currHullAprox)
				sMaxHull = str(maxHullAprox)


			auxString = str(sCurrHull) + "/" + str(sMaxHull)
			if globalVarList["ShowPercent"]:
				auxString = "(" + auxString + ")"
			infoString = infoString + " " + auxString
		
		pText.SetString("Hull :" + infoString)

		global pHealth
		#pHealth = pDisplay.GetHealthGauge()
		if not pHealth:
			return
		if pHealth.IsVisible() and globalVarList["ShowBar"] == 0:
			pHealth.SetNotVisible(0)

		global firstTime
		if firstTime > 0:
			print "called re-size"
			pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
			if not pTCW:
				return
			pDisplay = pTCW.GetShipDisplay()
			if not pDisplay:
				return
			print "re-size commencing..."
			firstTime = 0
			newWidth = pOriginalWidth
			if (1.05 * pText.GetWidth()) > newWidth:
				newWidth = pText.GetWidth() * 1.05 #pOriginalWidth + pText.GetWidth()/2.0
			pDisplay.SetFixedSize(newWidth, (pOriginalHeight + pText.GetHeight()))
			pHealth.Resize(pDisplay.GetMaximumInteriorWidth(), pHealth.GetHeight(), 0)
			pDisplay.InteriorChangedSize()	