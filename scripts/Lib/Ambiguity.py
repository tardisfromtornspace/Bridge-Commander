import App

g_forms = {}
g_panels = {}
g_events = {}
g_eventhandler = {}

g_oldfocus = None

BAR_WIDTH				= 0.2609625
BAR_HEIGHT				= 0.0291666

# Stations
HELM = 		"Helm"
TACTICAL = 	"Tactical"
XO = 		"XO"
SCIENCE = 	"Science"
ENGINEER =	"Engineer"

# Frame styles
FS_RIGHTBORDER = "RightBorder"
FS_NOMINIMIZE = "NoMinimize"
FS_NORMALSTYLE = "NormalStyle"
FS_LEFTSEPARATOR = "LeftSeparator"
FS_WEAPONSDISPLAY = "WeaponsDisplay"
FS_SOLIDGLASS = "SolidGlass"

def terminate():
    global g_forms    
    try:
        for form in g_forms.keys():
            destroyForm(form)
    except:
        pass
    g_forms = None

    global g_panels        
    try:
        for panel in g_panels:
            panel = None
    except:
        pass
    g_panels = None

    global g_events
    global g_eventhandler
    try:
        for event in g_events:
            if (g_eventhandler.has_key(event)):
                removeEventHandler(g_eventhandler[event]['person'], event, g_eventhandler[event]['function'])
                del g_eventhandler[event]
            event = None
    except:
        pass
    g_events = None


def getForm(name):
	if (g_forms.has_key(name)):
		return g_forms[name]
	else:
		return None

def createForm(name, w, h, visible):
	pPane = App.TGPane_Create (1.0, 1.0)
	
	if (not visible):
		pPane.SetNotVisible()
	
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.AddChild(pPane, 0, 0)
	g_forms[name] = pPane
	
	return pPane    

def destroyForm(name):
	if (g_forms.has_key(name)):
		App.g_kFocusManager.RemoveAllObjectsUnder(getForm(name))
	        pTopWindow = App.TopWindow_GetTopWindow()
	        pTopWindow.DeleteChild(getForm(name))
	        del g_forms[name]

def showFormModal(name):
	pForm = getForm(name)
	pForm.SetVisible()
	pForm.SetEnabled()
	
	pTopWindow = App.TopWindow_GetTopWindow()
	global g_oldfocus
	g_oldfocus = pTopWindow.GetFocus()
	pTopWindow.MoveToFront(pForm)
	pTopWindow.SetFocus(pForm)
	
	pForm.SetAlwaysHandleEvents()

def closeFormModal(name):
	pForm = getForm(name)
	pForm.SetNotVisible()
	pForm.SetNotAlwaysHandleEvents()
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.SetFocus(g_oldfocus)
	
def hideFormModal(name, visible):
	pForm = getForm(name)
	if (not visible):
		pForm.SetNotVisible()
	else:
		pForm.SetVisible()

def createPanel(parent, name, x, y, w, h):
	pPanel = App.TGPane_Create(w, h)
	parent.AddChild (pPanel, x, y)
	g_panels[name] = pPanel
	return pPanel

def getPanel(name):
	return g_panels[name]

def createSubPanel(parent, name, x, y, w, h):
	pSubPanel = App.STSubPane_Create(w, h, 1)
	parent.AddChild(pSubPanel, x, y)
	return pSubPanel

def createFrame(parent, title, x, y, w, h, style, color, scrolling=0):
	pFrame = App.STStylizedWindow_CreateW("StylizedWindow", style, App.TGString(title), x, y, None, 1, w, h, color)
	parent.AddChild(pFrame)
	pFrame.SetTitleBarThickness(BAR_HEIGHT)
	pFrame.SetUseScrolling(scrolling)
	return pFrame

def createIcon(parent, nr, x, y, w, h, color = None):
    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
    pcLCARS = pGraphicsMode.GetLcarsString()
    if (not color is None):
        pIcon = App.TGIcon_Create(pcLCARS, nr)
    else:
        pIcon = App.TGIcon_Create(pcLCARS, nr, color)
    pIcon.Resize(w, h)
    parent.AddChild(pIcon, x, y)
    return pIcon

def createIcon2(parent, name, nr, x, y, w, h, color=None):
    pIcon = App.TGIcon_Create(name, nr, color)
    pIcon.Resize(w, h)
    parent.AddChild(pIcon, x, y)
    return pIcon
    
def createGlassBackground(parent):
    pGlass = createIcon(parent, 120, 0, 0, parent.GetWidth(), parent.GetHeight())
    return pGlass

def createLabel(parent, name, x, y):
	pText = App.TGParagraph_CreateW(App.TGString(name))
	parent.AddChild(pText, x, y)
	return pText

def getEvent(name):
    if (not g_events.has_key(name)):
        event = App.Mission_GetNextEventType()
        g_events[name] = event

    return g_events[name]

def addEventHandler(person, name, function):
    pSet =  App.g_kSetManager.GetSet('bridge')
    pPerson = App.CharacterClass_GetObject(pSet, person)

    if (pPerson is None):
        return 0

    event = getEvent(name)
    pPerson.AddPythonFuncHandlerForInstance(event, function)
    evh = {'person':person, 'function':function}
    g_eventhandler[name] = evh
    return event

def removeEventHandler(person, name, function):
    pSet =  App.g_kSetManager.GetSet('bridge')
    pPerson = App.CharacterClass_GetObject(pSet, person)

    if (pPerson is None):
        return 0

    pPerson.RemoveHandlerForInstance(getEvent(name), function)
    

def createButton(parent, title, event, event_string, receiver, x=-1, y=-1, w=0, h=0):
    pSet =  App.g_kSetManager.GetSet('bridge')
    pPerson = App.CharacterClass_GetObject(pSet, receiver)

    pButton = CreateBridgeMenuButton(App.TGString(title), event, event_string, pPerson, w, h)
    if (not parent is None):
    	if ((x != -1) and (y!=-1)):
        	parent.AddChild(pButton, x, y)
        else:
        	parent.AddChild(pButton)
    return pButton

def createMainMenuButton(parent, title, event, event_string, receiver, x, y, w, h, color=App.g_kMainMenuButtonColor):
    pButton = createButton(parent, title, event, event_string, receiver, x, y, w, h)
    pButton.SetNormalColor(color)
    pButton.SetHighlightedTextColor (App.g_kMainMenuButtonHighlightedColor)
    pButton.SetSelectedColor(App.g_kMainMenuButtonSelectedColor)
    return pButton

def createMenuButton(person, title, event, event_string):
    pSet =  App.g_kSetManager.GetSet('bridge')
    pPerson = App.CharacterClass_GetObject(pSet, person)
    pMenu = pPerson.GetMenu()
    if (not pMenu is None):
        button = pMenu.AddChild(createButton(None, title, event, event_string, person, 0, 0, 0, 0))
        return button

def getEventString(pEvent):
	if (not pEvent is None):
		return (App.TGStringEvent_Cast(pEvent)).GetCString()
	else:
		return ""

def createMenu(parent, title, event, receiver, menudef, x, y, w, h):
	pMenu = App.STSubPane_Create(w, h, 1)

	pStylizedWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString(title))
	pStylizedWindow.SetUseScrolling(1)
	pStylizedWindow.SetFixedSize(w, h)
	pStylizedWindow.SetTitleBarThickness(BAR_HEIGHT)
	pStylizedWindow.AddChild(pMenu)
	parent.AddChild(pStylizedWindow, x, y)
	
	for menuitem in menudef:
		if (len(menuitem)==1):
			button = createButton(pMenu, menuitem[0], event, menuitem[0], receiver)
			button.SetUseUIHeight(0)
		elif (len(menuitem)==2):
			if (type(menuitem[1]) == type("")):
				button = createButton(pMenu, menuitem[0], event, menuitem[1], receiver)
				button.SetUseUIHeight(0)
			else:
				pSubMenu = App.STCharacterMenu_CreateW(App.TGString(menuitem[0]))
				if (len(menuitem[1]) == 1):
					button = createButton(pSubMenu, menuitem[1][0], event, menuitem[1][0], receiver)
				else:
					button = createButton(pSubMenu, menuitem[1][0], event, menuitem[1][1], receiver)
				button.SetUseUIHeight(0)
				pMenu.AddChild(pSubMenu)
	return pMenu
		
def createEditBox(parent, x, y, name, text, width, label_width, maxChars):
	pTextEntry = CreateTextEntry(App.TGString(name), App.TGString(text), width, label_width, maxChars)
	parent.AddChild(pTextEntry, x, y)
	pTextBox = App.TGParagraph_Cast(pTextEntry.GetNthChild(1))
	
	return pTextBox
	
def showMessageBox(title, text):
	pTopWindow = App.TopWindow_GetTopWindow()
	pModalDialogWindow = App.ModalDialogWindow_Cast (pTopWindow.FindMainWindow (App.MWT_MODAL_DIALOG))
	pModalDialogWindow.Run(App.TGString(title), App.TGString(text), App.TGString("OK"), None, None, None)
	
def showModalDialog(title, text, button1_text, button1_event, button2_text, button2_event):
	pTopWindow = App.TopWindow_GetTopWindow()
	pModalDialogWindow = App.ModalDialogWindow_Cast (pTopWindow.FindMainWindow (App.MWT_MODAL_DIALOG))
	pModalDialogWindow.Run(App.TGString(title), App.TGString(text), App.TGString(button1_text), button1_event, App.TGString(button2_text), button2_event)
	

###############################################################################
#	CreateBridgeMenuButton()
#
#	Create a menu button which sends an int event with the passed in event
#	type and int data, to a passed in character.
#
#	Args:	pName		- name of button (string)
#			eType		- event type
#			sSubType	- sub type to be passed in the string of the TGStringEvent
#			pCharacter	- character to which to send the event
#			fWidth		- the width of the button
#			fHeight		- the height of the button
#
#	Return:	none
###############################################################################
def CreateBridgeMenuButton(pName, eType, sSubType, pCharacter, fWidth = 0.0, fHeight = 0.0):
	pEvent = App.TGStringEvent_Create()
	if eType != None:
		pEvent.SetEventType(eType)
	pEvent.SetDestination(pCharacter)
	pEvent.SetString(sSubType)
	if fWidth == 0.0:
		return (App.STButton_CreateW(pName, pEvent))
	else:
		return (App.STRoundedButton_CreateW(pName, pEvent, fWidth, fHeight))

###############################################################################
#	CreateTextEntry(pName, pDefault, fMaxWidth
#	
#	Creates a text entry thingie
#	
#	Args:	pName - the name of the title tag
#			pDefault - the default string of the text entry
#			fMaxWidth - the max width of this thingie
#			fLongestLen - spacing for the name versus the text entry box
#	Return:	the newly-created thingie
###############################################################################
def CreateTextEntry(pName, pDefault, fMaxWidth, fLongestLen, iMaxChars, bBackground = 1, pcIgnoreString = None):
	# First create a pane for this.
	pPane = App.TGPane_Create (fMaxWidth, 1.0)

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	# Create the text tag
	if (pName == None):
		pText = App.TGPane_Create ()
		fWidth = pText.GetWidth ()
		pPane.AddChild (pText, fLongestLen - fWidth, 0)
		
		# Add some space between text tag and text entry box
		fLongestLen = 0

		# Get width for spacing the text entry box.
		fWidth = fLongestLen

		# Create the name entry button
		# Get LCARS string
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pGraphicsMode.GetLcarsString()

		if (pDefault == None):
			pTextEntry = App.TGParagraph_Create ("Default")
		else:
			pTextEntry = App.TGParagraph_CreateW (pDefault)
		pTextEntry.SetMaxChars (iMaxChars)
		pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
		pTextEntry.SetReadOnly (0)
		if (pcIgnoreString == None):
			pTextEntry.SetIgnoreString ("\n\r")
		else:
			pTextEntry.SetIgnoreString(pcIgnoreString + "\n\r");
#		pTextEntry.SetColor (App.g_kSTMenuTextColor)

		pPane.AddChild (pTextEntry, fWidth + 0.005, (LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT - pTextEntry.GetHeight ()) / 2.0)

		# Create a background for the text entry button
		if (bBackground):
			pBackground = App.TGIcon_Create(pcLCARS, 200, App.g_kTextEntryColor)
			pBackground.Resize (fMaxWidth - fWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)
			pPane.AddChild (pBackground, fWidth, 0)

		# Now resize the pane to be the height of text entry
		pPane.Resize (fMaxWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)

		if (pDefault == None):
			# Okay, now I have to blank out the string
			pTextEntry.SetString ("", 0)

	else:
		pText = App.TGParagraph_CreateW (pName)
		fWidth = pText.GetWidth ()
#		pPane.AddChild (pText, fLongestLen - fWidth, 0)
		pPane.AddChild (pText, 0, 0)
		
		# Add some space between text tag and text entry box
		fLongestLen = fLongestLen + 0.008125

		# Get width for spacing the text entry box.
		fWidth = fLongestLen

		# Create the name entry button
		# Get LCARS string
		pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
		pcLCARS = pGraphicsMode.GetLcarsString()

		if (pDefault == None):
			pTextEntry = App.TGParagraph_Create ("Default")
		else:
			pTextEntry = App.TGParagraph_CreateW (pDefault)
		pTextEntry.SetMaxChars (iMaxChars)
		pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight ()+0.007, 0)
		pTextEntry.SetReadOnly (0)
		pTextEntry.SetIgnoreString ("\n\r")
		pPane.AddChild (pTextEntry, fWidth + 0.005, 0)
#		pTextEntry.SetColor (App.g_kSTMenuTextColor)

		# Create a background for the text entry button
		if (bBackground):
			pBackground = App.TGIcon_Create(pcLCARS, 200, App.g_kTextEntryColor)
			pBackground.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
			pPane.AddChild (pBackground, fWidth, 0)

		# Now resize the pane to be the height of text entry
		pPane.Resize (fMaxWidth, pTextEntry.GetHeight (), 0)

		if (pDefault == None):
			# Okay, now I have to blank out the string
			pTextEntry.SetString ("", 0)

	#pPane.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__ + ".TextEntryMouseHandler")

	return pPane
    