import App
import Foundation
import string
import nt
import traceback

# TO-DO REMOVE THE extra prints
# TO-DO REMOVE DRIED LAVA
LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

pModule = __import__("SavedConfigs.AccessibilityConfigVals")
configPath = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\AccessibilityConfigVals.py"

ET_SAVED_CONFIG = App.UtopiaModule_GetNextEventType() # You may wonder, ¿why? Because it is actually possible to play a mission and have access to the Customize configurations on the fly as long as the last Configure Window you opened was Customize
ET_SELECT_BUTTON = App.UtopiaModule_GetNextEventType()

issues = 0 # To prevent another case like Galaxy Charts wrong configuration values breaking an entire install - yes, like KCS' case.
def SafeConfigStatement(variable, pMyModule, default, issue=0):
	myVariable = default
	try:
		if pMyModule != None and hasattr(pMyModule, variable):
			myVariable = getattr(pMyModule, variable)
		else:
			print configPath, " has no ", variable, " attribute. This will be addressed"
			myVariable = default
			issue = issue + 1
	except:
		traceback.print_exc()
		myVariable = default
		issue = issue + 1

	return myVariable, issue

dConfig = {}
dConfig["ShowPercent"], issues = SafeConfigStatement("ShowPercent", pModule, 0, issues)
dConfig["ShowBar"], issues = SafeConfigStatement("ShowBar", pModule, 1, issues)
dConfig["ShowFraction"], issues = SafeConfigStatement("ShowFraction", pModule, 0, issues)

dRadixNotation = {
	"," : "Comma (,)",
	"." : "Lower point (.)",
	"·" : "Middle point (·)",
	"’" : "Apostrophe (’)",
}
dConfig["NumberDecimals"], issues = SafeConfigStatement("NumberDecimals", pModule, 0, issues)
dConfig["RadixNotation"], issues = SafeConfigStatement("RadixNotation", pModule, ".", issues) # TO-DO add button

dFont = {
	"Crillee": [5, 6, 9, 12, 15],
	"LCARSText": [5, 6, 9, 12, 15],
	"Tahoma": [8, 14], "Arial": [8],
	"Serpentine": [12],
} # TO-DO make this an import
dConfig["sFont"], issues = SafeConfigStatement("sFont", pModule, "Crillee", issues) # TO-DO Make this something like dFont.keys()[0]
dConfig["FontSize"], issues = SafeConfigStatement("FontSize", pModule, 5, issues) # TO-DO Make this something like dFont[dFont.keys()[0]]

pFontSubMenu = None
sBaseFMenu = "Font Selection: "
sSeparator = ", size "

# sColor = {"Default": [], } # TO-DO DIFFERENT HEALTH BAR COLORS? ALSO TGParagraph.SetColor

def SaveConfig(pObject, pEvent):
	file = nt.open(configPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
	nt.write(file, "ShowPercent = " + str(dConfig["ShowPercent"]))
	nt.write(file, "\nShowBar = " + str(dConfig["ShowBar"]))
	nt.write(file, "\nShowFraction = " + str(dConfig["ShowFraction"]))
	nt.write(file, "\nNumberDecimals = " + str(dConfig["NumberDecimals"]))
	nt.write(file, "\nRadixNotation = \"" + str(dConfig["RadixNotation"])+ "\"")
	nt.write(file, "\nsFont = \"" + str(dConfig["sFont"]) + "\"")
	nt.write(file, "\nFontSize = " + str(dConfig["FontSize"]))
	nt.close(file)

	"""
	# Because of shenanigans with menu being available during QB... What do you think, Sovereign? Should we add support for that?
	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(ET_SAVED_CONFIG)
	#pEvent.SetDestination(None)
	pEvent.SetString("SAVED BC ACCESIBILITY")
	App.g_kEventManager.AddEvent(pEvent)
	"""
	
if issues > 0:
	print "Re-applying a safe save Accesibility Config"
	try:
		SaveConfig(None, None)
	except:
		traceback.print_exc()

def GetName():
	return "BC Accessibility"


# Builds our menu.  Remember to add the "return App.TGPane_Create(0,0)" command!
def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	CreateButton("Show Health Bar", pContentPanel, pOptionsPane, pContentPanel, __name__ + ".BarToggle", isChosen=dConfig["ShowBar"], isToggle=1)
	CreateButton("Show Health Percent", pContentPanel, pOptionsPane, pContentPanel, __name__ + ".PercentToggle", isChosen=dConfig["ShowPercent"], isToggle=1)
	CreateButton("Show Health Fraction", pContentPanel, pOptionsPane, pContentPanel, __name__ + ".FractionToggle", isChosen=dConfig["ShowFraction"], isToggle=1)

	CreateTextEntryButton("Number of decimals: ", pContentPanel, pOptionsPane, pContentPanel, "NumberDecimals", __name__ + ".HandleKeyboardGoBetween")
	CreateFontMenu(sBaseFMenu + str(dConfig["sFont"]) + str(sSeparator)+str(dConfig["FontSize"]) , pContentPanel, pOptionsPane, pContentPanel)
	# TO-DO CreateMultipleChoiceButton("Radix Notation:", pContentPanel, pOptionsPane, pContentPanel, __name__ + ".PercentToggle", variable, isChosen=dConfig["ShowPercent"], isToggle=1)

	CreateButton("Save Config", pContentPanel, pOptionsPane, pContentPanel, __name__ + ".SaveConfig")
	return App.TGPane_Create(0,0)

def BarToggle(object, event):
	#global ShowBar
	global dConfig
	dConfig["ShowBar"] = not dConfig["ShowBar"]
	App.STButton_Cast(event.GetSource()).SetChosen(dConfig["ShowBar"]) # Found method to get the button from BridgePlugin.py

def PercentToggle(object, event):
	#global ShowPercent
	global dConfig
	dConfig["ShowPercent"] = not dConfig["ShowPercent"]
	App.STButton_Cast(event.GetSource()).SetChosen(dConfig["ShowPercent"])

def FractionToggle(object, event):
	#global ShowFraction
	global dConfig
	dConfig["ShowFraction"] = not dConfig["ShowFraction"]
	App.STButton_Cast(event.GetSource()).SetChosen(dConfig["ShowFraction"])

def HandleKeyboardGoBetween(pObject, pEvent):
	pPara = App.TGParagraph_Cast(pEvent.GetDestination())
	pParent = App.TGPane_Cast(pPara.GetParent())
	pSubPara = App.TGParagraph_Cast(pParent.GetNthChild(2))
	pString = App.TGString()
	pSubPara.GetString(pString)
	pNewVal = App.TGString()
	pPara.GetString(pNewVal)
	sNewVal = pNewVal.GetCString()	
	if string.count(sNewVal, ".") > 1:
		lList = string.split(sNewVal, ".")
		sNewVal = lList[0] + "." + string.join(lList[1:-1], "")
		pPara.SetString(sNewVal)

	if pNewVal.GetCString() != None and pNewVal.GetCString() != "":
		dConfig[pString.GetCString()] = int(pNewVal.GetCString())
		if pString.GetCString() == "sFont" or pString.GetCString() == "FontSize":
			UpdateFontSubMenu(0)

	pObject.CallNextHandler(pEvent)

def CreateTextEntryButton(sButtonName, pMenu, pOptionPane, pContentPanel, sVar, sFunction, isChosen = 0, isToggle = 0, EventInt = 0, ET_EVENT = None):
	pTextField  = CreateTextField(App.TGString(sButtonName), sVar, sFunction)
	pMenu.AddChild(pTextField)

# From Custom\UnifiedMainMenu\ConfigModules\Options\Graphics\NanoFX by MLeoDaalder
def CreateTextField(pName, sVar, sFunction):
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
	LCARS = __import__(pGraphicsMode.GetLcarsModule())
	fMaxWidth = LCARS.MAIN_MENU_CONFIGURE_CONTENT_WIDTH - 0.02
	pPane = App.TGPane_Create (fMaxWidth, 1.0)

	# Create the text tag
	pText = App.TGParagraph_CreateW(pName)
	fWidth = pText.GetWidth ()+0.01
	pTText = App.STButton_CreateW(pName, None)
	del pText

	pPane.AddChild(pTText,0,0)
	pTText.SetUseEndCaps(0)
	pTText.SetJustification(App.STButton.LEFT)
	pTText.SetDisabled(1)
	pTText.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pTText.SetColorBasedOnFlags()
	pTText.SetVisible()

	pcLCARS = pGraphicsMode.GetLcarsString()

	pTextEntry = App.TGParagraph_Create (str(dConfig[sVar]))
	pTextEntry.SetIgnoreString("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*?\t\\/,<>\"|:;\'\n-+()&^%$#@!`~\n\r")

	pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
	pTextEntry.SetReadOnly(0)
	pTextEntry.SetColor(App.NiColorA(0,0,0,1))

	pTextEntry.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__ + ".HandleKeyboardGoBetween")

	pSubEntry = App.TGParagraph_Create(str(sVar))
	pSubEntry.SetNotVisible(1)

	pPane.AddChild (pTextEntry, fWidth + 0.02, 0.002)
	pPane.AddChild(pSubEntry)

	pPane.Resize (fMaxWidth, pTText.GetHeight(), 0)

	return pPane


"""
def CreateMultipleChoiceButton(sButtonName, pOptionsPane, pContentPanel, sFunction, variable, isChosen= 0, isToggle = 0, EventInt = 0, bGameEnded = 0):
	CreateButton(sButtonName, pContentPanel, pOptionsPane, pContentPanel, __name__ + ".PercentToggle", isChosen=ShowPercent, isToggle=1)
"""

def CreateButton(sButtonName, pMenu, pOptionPane, pContentPanel, sFunction, isChosen = 0, isToggle = 0, EventInt = 0, ET_EVENT = None):
	if ET_EVENT == None:		
		ET_EVENT = App.UtopiaModule_GetNextEventType()

	pOptionPane.AddPythonFuncHandlerForInstance(ET_EVENT, sFunction)

	pEvent = App.TGStringEvent_Create()
	pEvent.SetEventType(ET_EVENT)
	pEvent.SetDestination(pOptionPane)
	pEvent.SetString(sButtonName)

	pButton = App.STButton_Create(sButtonName, pEvent)
	pButton.SetChoosable(isToggle)
	pButton.SetChosen(isChosen)

	pEvent.SetSource(pButton)
	pMenu.AddChild(pButton)

	return pButton


def CreateFontMenu(sMenuName, pMenu, pOptionsPane, pContentPanel):
	pSubMenu = App.STMenu_Create(sMenuName)
	pSubMenu.AddPythonFuncHandlerForInstance(ET_SELECT_BUTTON, __name__ + ".HandleSelectButton")

	for font in dFont.keys():
		for i in range(len(dFont[font])):
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(ET_SELECT_BUTTON)
			pEvent.SetDestination(pSubMenu)
			s = "%s%s%d" % (font, sSeparator, dFont[font][i])
			print (s)
			pEvent.SetString(str(s))
			pButton = App.STButton_Create(s, pEvent)
			pSubMenu.AddChild(pButton)

	CreateTextEntryButton("Custom size (may cause font issues): ", pSubMenu, pOptionsPane, pSubMenu, "FontSize", __name__ + ".HandleKeyboardGoBetween")
	pMenu.AddChild(pSubMenu)

	global pFontSubMenu
	pFontSubMenu = pSubMenu
	return

def HandleSelectButton(pObject, pEvent):
	pObject.CallNextHandler(pEvent)
	i = pEvent.GetCString()

	print i

	s = string.split(i, sSeparator)
	if len(s) >= 2 and s[0] != None and s[0] != "" and s[1] != None and s[1] != "":
		global dConfig
		print "valid config"
		dConfig["sFont"] = s[0]
		dConfig["FontSize"] = s[1]
		UpdateFontSubMenu(1)

def UpdateFontSubMenu(close=0): 
	global pFontSubMenu
	pFontSubMenu.SetName(App.TGString(sBaseFMenu + str(dConfig["sFont"]) + str(sSeparator)+str(dConfig["FontSize"])))
	if close:
		pFontSubMenu.Close()


