# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL LICENSE AS WELL
# HullIntegrity.py
# 7th March 2025, by USS Sovereign, and tweaked by Noat and Alex SL Gato (CharaToLoki)
#         Inspired by the Shield Percentages mod by Defiant. It was originally made pre-2010 with the goal of showing lots of accessibility options, such as for colorblind people.
#
# Modify, redistribute to your liking. Just remember to give credit where due.
#################################################################################################################
#
MODINFO = { "Author": "\"USS Sovereign\" (mario0085), Noat (noatblok),\"Alex SL Gato\" (andromedavirgoa@gmail.com)",
	    "Version": "0.54",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

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
	"SeparateFraction": 0,
	"NumberDecimals" : 0,
	"RadixNotation" : ".",
	"sFont" : "Crillee",
	"FontSize": 5,
}

def CheckAndRefreshModule(variableList, pMyModule, theWay, issue=0): # Used when for example you had an incomplete BC Accessibility Config values
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

def RefreshConfig(pObject, pEvent):
	print "Saved mid-game, refreshing configuration..."
	CheckAndRefreshModule(globalVarList, pModule, sPath, 0)
	global pText, firstTime

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
	
	if not pHealth:
		pHealth = pDisplay.GetHealthGauge()

	if not pHealth:
		return

	# Commented, it may accidentally affect ablativeArmours...
	#kFillColor = App.TGColorA()
	#kFillColor.SetRGBA(App.g_kSubsystemFillColor.r, App.g_kSubsystemFillColor.g, App.g_kSubsystemFillColor.b, App.g_kSubsystemFillColor.a)
	#kEmptyColor = App.TGColorA()
	#kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r, App.g_kSubsystemEmptyColor.g, App.g_kSubsystemEmptyColor.b, App.g_kSubsystemEmptyColor.a)

	#pHealth.SetFillColor(kFillColor)
	#pHealth.SetEmptyColor(kEmptyColor)

	firstTime = 1
	# This line hides the health gauge which is replaced by the percentage text
	if globalVarList["ShowBar"] == 0:
		pHealth.SetNotVisible(0)
	else:
		pHealth.SetVisible(0)


	#kTFillColor = App.TGColorA()
	#kTFillColor.SetRGBA(App.g_kSTMenuTextColor.r, App.g_kSTMenuTextColor.g, App.g_kSTMenuTextColor.b, App.g_kSTMenuTextColor.a)

	if globalVarList["ShowPercent"] or globalVarList["ShowFraction"]:
		wasNone = 0
		if pText == None:
			pText = App.TGParagraph_Create("Hull :          100%", 1.0, None, globalVarList["sFont"], globalVarList["FontSize"])
			wasNone = 1
		else:
			pText.SetFontGroup(App.g_kFontManager.GetFontGroup(globalVarList["sFont"], globalVarList["FontSize"]))
			#pText.SetColor(kTFillColor)

		if globalVarList["ShowFraction"]:
			howRight = 0
		else:
			howRight = pHealth.GetRight() * 0.8 - pText.GetWidth()

		if wasNone != 0:
			pDisplay.AddChild(pText, howRight, pHealth.GetBottom())

	else:
		if pText != None: # "Hiding" in a way...
			#pText.SetColor(kTFillColor)
			pText.SetString("")
		pDisplay.SetFixedSize(pOriginalWidth, pOriginalHeight)
		pHealth.Resize(pDisplay.GetMaximumInteriorWidth(), pHealth.GetHeight(), 0)


	pDisplay.InteriorChangedSize()
	#pDisplay.Layout()
	pObject.AddHandler() #shipSwapChecker.AddHandler()

	global pTimer
	if not pTimer:
		pTimer = Watcher()



def ShipCheck(pObject, pEvent):
	global firstTime
	firstTime = 1
	#pObject.CallNextHandler(pEvent)

class ShipSwapCheckClass:
	def __init__(self, name):
		self.name = name
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		self.AddSHandler()

	def ShipCheck(self, pEvent): # Somehow I cannot call this function... but the global one I pretty much can...
		global firstTime
		firstTime = 1

	def AddHandler(self):
		self.RemoveHandler()
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_PLAYER, self.pEventHandler, __name__ + ".ShipCheck")

	def RemoveHandler(self):
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, self.pEventHandler, __name__ + ".ShipCheck")

	def AddSHandler(self):
		if pConfigModule != None and hasattr(pConfigModule, "ET_SAVED_CONFIG") and pConfigModule.ET_SAVED_CONFIG != None:
			App.g_kEventManager.RemoveBroadcastHandler(pConfigModule.ET_SAVED_CONFIG, self.pEventHandler, __name__ + ".RefreshConfig")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(pConfigModule.ET_SAVED_CONFIG, self.pEventHandler, __name__ + ".RefreshConfig")

	def RemoveSHandler(self):
		if pConfigModule != None and hasattr(pConfigModule, "ET_SAVED_CONFIG") and pConfigModule.ET_SAVED_CONFIG != None:
			App.g_kEventManager.RemoveBroadcastHandler(pConfigModule.ET_SAVED_CONFIG, self.pEventHandler, __name__ + ".RefreshConfig")
		

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


	# Commented, it may accidentally affect ablativeArmours...
	#kFillColor = App.TGColorA()
	#kFillColor.SetRGBA(App.g_kSubsystemFillColor.r, App.g_kSubsystemFillColor.g, App.g_kSubsystemFillColor.b, App.g_kSubsystemFillColor.a)
	#kEmptyColor = App.TGColorA()
	#kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r, App.g_kSubsystemEmptyColor.g, App.g_kSubsystemEmptyColor.b, App.g_kSubsystemEmptyColor.a)

	#pHealth.SetFillColor(kFillColor)
	#pHealth.SetEmptyColor(kEmptyColor)	

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

	#kTFillColor = App.TGColorA()
	#kTFillColor.SetRGBA(App.g_kSTMenuTextColor.r, App.g_kSTMenuTextColor.g, App.g_kSTMenuTextColor.b, App.g_kSTMenuTextColor.a)
	#pText.SetColor(kTFillColor)

	#print(pHealth.GetPosition) # Sov had this

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

	shipSwapChecker.RemoveSHandler()
	shipSwapChecker.RemoveHandler()

	pText = None
	pHealth = None
	pTimer = None

def convertToString(iExact, numDec, radNot):
	pExactPart = ""
	auxPercString = ""
	iDec = "0"
	ipExact = str(repr(iExact))
	iHugeOrMicro = 0
	
	if "e" in ipExact:
		iHugeOrMicro = 1

	if iHugeOrMicro:
		pLittlePart = string.split(str(repr(iExact)), "e")
		pExactPart = string.split(str(pLittlePart[0]), ".")
		pFullDec = string.join(pExactPart[:], "")
		auxPercString = "0"
		iPowerReverse = int(pLittlePart[1])
		if iPowerReverse < 0:
			iDec = string.zfill(string.zfill(pFullDec, len(pFullDec)+abs(iPowerReverse)-1), numDec+1)[:(numDec+1)]

		else:
			currRelA = string.ljust(pFullDec, abs(iPowerReverse)+1)
			currRelB = string.replace(currRelA, " ", "0")
			auxPercString = currRelB[:(iPowerReverse+1)]
			iDec = string.replace(string.ljust(currRelB[(iPowerReverse+1):], numDec)[:(numDec)], " ", "0")
			
	else:
		pExactPart = string.split(str(iExact), ".")
		auxPercString = pExactPart[0]
		if len (pExactPart) >= 2:
			currHullRelA = string.ljust(str(pExactPart[1]), numDec)[:(numDec)]
			iDec = string.replace(currHullRelA, " ", "0")
		else:
			iDec = string.zfill(iDec, numDec)
	if numDec > 0:
		auxPercString = auxPercString + str(radNot) + str(iDec)

	return auxPercString

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

		pPlayer = MissionLib.GetPlayer()
		if not pPlayer:
			return

		if pPlayer.IsDead() or pPlayer.IsDying():
			return

		global pText
		if pText != None:
			pHull = pPlayer.GetHull()

			if not pHull or not hasattr(pHull, "GetMaxCondition"):
				return

			self.fHullCurr = pHull.GetCondition()
			self.fHullMax = pHull.GetMaxCondition()
			if not self.fHullCurr or not self.fHullMax or self.fHullMax == 0.0:
				pText.SetString("Hull : N/A")
				return

			self.iExact = self.fHullCurr/self.fHullMax * 100
		
			infoString = ""
		
			if globalVarList["ShowPercent"]:
				auxPercString = ""
				if globalVarList["NumberDecimals"] > 0:
					auxPercString = convertToString(self.iExact, globalVarList["NumberDecimals"], str(globalVarList["RadixNotation"]))

				infoString = infoString + auxPercString + "% "
				if not globalVarList["ShowFraction"]:
					infoString = ":          " + infoString
				else:
					if globalVarList["SeparateFraction"] > 0:
						infoString = "Integrity : " + infoString
					else:
						infoString = ": " + infoString

			if globalVarList["ShowFraction"]:
				if self.fHullMax <= 1.0 and globalVarList["NumberDecimals"] < 6:
					signifDec = 6
				else:
					signifDec = globalVarList["NumberDecimals"]

				sCurrHull = convertToString(self.fHullCurr, signifDec, str(globalVarList["RadixNotation"]))
				sMaxHull = convertToString(self.fHullMax, signifDec, str(globalVarList["RadixNotation"]))

				auxString = str(sCurrHull) + "/" + str(sMaxHull)
				if globalVarList["ShowPercent"]:
					if globalVarList["SeparateFraction"] > 0:
						auxString = "\nHull Strength : " + auxString + " "
					else:
						auxString = " (" + auxString + ")"
				else:
					auxString = ": " + auxString + " "
				infoString = infoString + "" + auxString

			if globalVarList["ShowFraction"] or globalVarList["ShowPercent"]:			
				pText.SetString("Hull " + infoString)

			"""
			if globalVarList["ShowPercent"]:
				auxPercString = ""
				if globalVarList["NumberDecimals"] > 0:
					auxPercString = convertToString(self.iExact, globalVarList["NumberDecimals"], str(globalVarList["RadixNotation"]))

				infoString = infoString + auxPercString + "%"
				if not globalVarList["ShowFraction"]:
					infoString = "          " + infoString
				else:
					infoString = " " + infoString
			if globalVarList["ShowFraction"]:
				if self.fHullMax <= 1.0 and globalVarList["NumberDecimals"] < 6:
					signifDec = 6
				else:
					signifDec = globalVarList["NumberDecimals"]

				sCurrHull = convertToString(self.fHullCurr, signifDec, str(globalVarList["RadixNotation"]))
				sMaxHull = convertToString(self.fHullMax, signifDec, str(globalVarList["RadixNotation"]))

				auxString = str(sCurrHull) + "/" + str(sMaxHull)
				if globalVarList["ShowPercent"]:
					auxString = "(" + auxString + ")"
				infoString = infoString + " " + auxString

			if globalVarList["ShowFraction"] or globalVarList["ShowPercent"]:			
				pText.SetString("Hull :" + infoString)
			"""

		global pHealth

		if not pHealth:
			pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
			if not pTCW:
				return
			pDisplay = pTCW.GetShipDisplay()
			if not pDisplay:
				return

			pHealth = pDisplay.GetHealthGauge()

		if not pHealth:
			return

		if pHealth.IsVisible() and globalVarList["ShowBar"] == 0:
			pHealth.SetNotVisible(0)
		elif not pHealth.IsVisible() and globalVarList["ShowBar"] == 1:
			pHealth.SetVisible(0)

		global firstTime

		if firstTime > 0:
			pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
			if not pTCW:
				return

			pDisplay = pTCW.GetShipDisplay()
			if not pDisplay:
				return

			firstTime = 0

			# Commented, it may accidentally affect ablativeArmours...
			#kFillColor = App.TGColorA()
			#kFillColor.SetRGBA(App.g_kSubsystemFillColor.r, App.g_kSubsystemFillColor.g, App.g_kSubsystemFillColor.b, App.g_kSubsystemFillColor.a)
			#kEmptyColor = App.TGColorA()
			#kEmptyColor.SetRGBA(App.g_kSubsystemEmptyColor.r, App.g_kSubsystemEmptyColor.g, App.g_kSubsystemEmptyColor.b, App.g_kSubsystemEmptyColor.a)

			#pHealth.SetFillColor(kFillColor)
			#pHealth.SetEmptyColor(kEmptyColor)

			#if pText != None:
			#	kTFillColor = App.TGColorA()
			#	kTFillColor.SetRGBA(App.g_kSTMenuTextColor.r, App.g_kSTMenuTextColor.g, App.g_kSTMenuTextColor.b, App.g_kSTMenuTextColor.a)
			#	pText.SetColor(kTFillColor)

			newWidth = pOriginalWidth
			extraHeight = 0
			if (globalVarList["ShowFraction"] or globalVarList["ShowPercent"]) and pText != None:
				if (1.05 * pText.GetWidth()) > newWidth:
					newWidth = pText.GetWidth() * 1.05
				extraHeight = pText.GetHeight()

			itsMin = pDisplay.IsMinimized()

			beforeX = 0
			beforeY = 0

			if itsMin:
				pDisplay.SetNotMinimized(1)
				
			pDisplay.SetFixedSize(newWidth, (pOriginalHeight + extraHeight))
			pHealth.Resize(pDisplay.GetMaximumInteriorWidth(), pHealth.GetHeight(), 0)

			pDisplay.InteriorChangedSize()

			pDisplay.Layout()

			pWepCon = pTCW.GetWeaponsControl()
			if pWepCon:
				if itsMin:
					pDisplay.SetMinimized(1)
				pDisplay.AlignTo(pWepCon, App.TGUIObject.ALIGN_BL, App.TGUIObject.ALIGN_BR)
			elif itsMin:
				pDisplay.SetMinimized(1)		