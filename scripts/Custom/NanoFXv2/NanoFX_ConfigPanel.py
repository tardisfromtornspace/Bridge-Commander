#########################################
#					#
# NanoFX Configuration Panel - In Game!	#
# By: MLeoDaalder			#
#					#
#########################################

import App
import MainMenu.mainmenu

import Custom.NanoFXv2.NanoFX_Config

# Nano FX tab
ET_NANOFX_TAB = App.UtopiaModule_GetNextEventType()

NanoFXButton1 = None
NanoFXButton2 = None

MainConfigure = None

# globals
ET_BRIDGEFX = App.UtopiaModule_GetNextEventType()
ET_WARPFX = App.UtopiaModule_GetNextEventType()
ET_EXPFX = App.UtopiaModule_GetNextEventType()
ET_SPECIALFX = App.UtopiaModule_GetNextEventType()
ET_CAMERAFX = App.UtopiaModule_GetNextEventType()
ET_DEFAULT = App.UtopiaModule_GetNextEventType()

ET_USEBRIDGEFX = App.UtopiaModule_GetNextEventType()
ET_USEEXPFX = App.UtopiaModule_GetNextEventType()
ET_USEWARPFX = App.UtopiaModule_GetNextEventType()
ET_USECAMERAFX = App.UtopiaModule_GetNextEventType()
ET_USESPECIALFX = App.UtopiaModule_GetNextEventType()
ET_USEDEFAULT = App.UtopiaModule_GetNextEventType()
ET_SAVECONFIG = App.UtopiaModule_GetNextEventType()

## lennie update: i really deplore all these globals! :(
	## Sorry... It looked good when I started...

BridgeFX = None
CameraFX = None
ExpFX = None
WarpFX = None
SpecialFX = None
Default = None
SaveConfig = None

ConfigPath = "scripts\\Custom\\NanoFXv2\\NanoFX_Config.py"

# store name of last menu invoked: if we don't save which pane is 
# presently active, we'll write erroneous results to file when we 
# invoke the TG string database for the menu buttons, because we're 
# clearing and reinitializing them (and the event handles) each and 
# every time (this is bad) a new dialogue is opened
sActivePane = None

# Bridge stuff
bFXDamageSparkDurationText = None
bFXParticleControlText = None
ET_BRDFX_EXPSPK_LEVEL = App.UtopiaModule_GetNextEventType()
ET_BRDFX_DAMSPK_LEVEL = App.UtopiaModule_GetNextEventType()

# Camera stuff
cFXViewScreenDefaultText = None
cFXViewScreenMaxText = None
cFXAwayDistanceText = None
cFXAwayForwardText = None

# Explosion stuff
eFXDamageSparkDurationText = None
eFXParticleControlText = None
eFXDebrisFXDurationText = None
eFXSplashRadiusText = None
ET_EXPFX_SPK_LEVEL = App.UtopiaModule_GetNextEventType()
ET_EXPFX_DAM_SPK_LEVEL = App.UtopiaModule_GetNextEventType()
ET_EXPFX_DEBRIS_LEVEL = App.UtopiaModule_GetNextEventType()

# Warp text var
wFXMaxRandomDistanceText = None

ET_EXPLIGHTFLICKER = App.UtopiaModule_GetNextEventType()
ET_FIXBRIGHTGLOWS = App.UtopiaModule_GetNextEventType()
ET_ROTATION = App.UtopiaModule_GetNextEventType()

# Special Stuff
ET_ATMOS = App.UtopiaModule_GetNextEventType()
ET_PLASMAFX = App.UtopiaModule_GetNextEventType()

# Warp Stuff
wFXMaxRandomDistance = App.UtopiaModule_GetNextEventType()


def SetNanoFXConfigHandler():
	global ET_NANOFX_TAB

	pOptionsWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS)

	# NanoFX Configurations Panel
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_NANOFX_TAB, __name__ + ".HandleNanoFX")

	# Now to make sure graphics don't go through each other
	pOptionsWindow.AddPythonFuncHandlerForInstance(MainMenu.mainmenu.ET_CONFIGURE_GENERAL_TAB, __name__ + ".MoveUp")
	pOptionsWindow.AddPythonFuncHandlerForInstance(MainMenu.mainmenu.ET_CONFIGURE_SOUND_TAB, __name__ + ".MoveUp")
	pOptionsWindow.AddPythonFuncHandlerForInstance(MainMenu.mainmenu.ET_CONFIGURE_GRAPHICS_TAB, __name__ + ".MoveUp")
	pOptionsWindow.AddPythonFuncHandlerForInstance(MainMenu.mainmenu.ET_CONFIGURE_SAVE, __name__ + ".MoveUp")
	pOptionsWindow.AddPythonFuncHandlerForInstance(MainMenu.mainmenu.ET_CONFIGURE_KEYBOARD, __name__ + ".MoveDown")


def CreateConfigEntry(pTabPane, x, y, pConfigurePane, pContentPane, pOptionsPane):
	global NanoFXButton1, NanoFXButton2
	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

 	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetSource(pConfigurePane)
	pEvent.SetDestination(pContentPane)
	pEvent.SetEventType(ET_NANOFX_TAB)
	pEvent.SetObjPtr(pOptionsPane)
	NanoFXButton1 = App.STRoundedButton_CreateW (App.TGString("NanoFX Config"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, 
				   LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	NanoFXButton2 = App.STRoundedButton_CreateW (App.TGString("NanoFX Config"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, 
				   LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	NanoFXButton2.SetNotVisible()

	NanoFXButton1.SetNormalColor(App.g_kMainMenuButton1Color)
	NanoFXButton1.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	NanoFXButton1.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	NanoFXButton1.SetDisabledColor(App.g_kSTMenu1Disabled)
	NanoFXButton1.SetColorBasedOnFlags()

	NanoFXButton2.SetNormalColor(App.g_kMainMenuButton1Color)
	NanoFXButton2.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	NanoFXButton2.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	NanoFXButton2.SetDisabledColor(App.g_kSTMenu1Disabled)
	NanoFXButton2.SetColorBasedOnFlags()

	if App.Game_GetCurrentGame():
		NanoFXButton1.SetDisabled (1)
		NanoFXButton2.SetDisabled (1)

	pTabPane.AddChild(NanoFXButton1, x, 0.0, 0)
	pTabPane.AddChild(NanoFXButton2, 0.0, y, 0)

def HandleNanoFX(pContentPane, pEvent):
	#global g_pcConfigurePaneName
	#g_pcConfigurePaneName = "nanofxconfig"
	MainMenu.mainmenu.g_pcConfigurePaneName = "NanoFXConfig"

	pConfigurePane = App.TGPane_Cast (pEvent.GetSource ())
	pSubTab = pConfigurePane.GetNthChild (1)
	if (pSubTab):
		pConfigurePane.DeleteChild (pSubTab)

	pOptionsPane = App.TGPane_Cast(pEvent.GetObjPtr())
	BuildConfigureNanoFXTab(pOptionsPane, pContentPane)

	pContentPane.CallNextHandler(pEvent)

	if (pContentPane):
		pContentPane.CallNextHandler(pEvent)
	

def BuildConfigureNanoFXTab(pOptionsPane, pContentPane, bGameEnded = 0):

	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return
	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pOptionsPane.KillChildren()
	pOptionsPane.SetNotExclusive()
	fMenuWidth = pOptionsPane.GetWidth()
	
	global MainConfigure
	MainConfigure = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("NanoFX Configuration"), 0, 0, None, 1, LCARS.MAIN_MENU_MIDDLE_CONTENT_WIDTH * 0.48, LCARS.MAIN_MENU_MIDDLE_CONTENT_HEIGHT * 0.96)
	MainConfigure.SetUseScrolling(1)

	MakeStanButtons()
	pOptionsPane.AddChild(MainConfigure, 0.0, 0.0, 0)

	pOptionsPane.SetFocus (pOptionsPane.GetFirstChild ())
	
	pOptionsPane.Layout ()

	if (MainMenu.mainmenu.g_iMovieMode != 3):
		MainMenu.mainmenu.g_iMovieMode = 3
		MainMenu.mainmenu.PlayBackgroundMovie (1)



def MakeStanButtons():
	global MainConfigure

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	pEvent = App.TGObjPtrEvent_Create()

	global BridgeFX

	BridgeFX = App.STRoundedButton_CreateW (App.TGString("BridgeFX"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	pEvent.SetSource(BridgeFX)
	pEvent.SetDestination(MainConfigure)
	pEvent.SetEventType(ET_BRIDGEFX)

	BridgeFX.SetNormalColor(App.g_kMainMenuButton1Color)
	BridgeFX.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	BridgeFX.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	BridgeFX.SetDisabledColor(App.g_kSTMenu1Disabled)
	BridgeFX.SetColorBasedOnFlags()
	BridgeFX.SetVisible()

	MainConfigure.RemoveHandlerForInstance(ET_BRIDGEFX, __name__ + ".HandleBridgeFX")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_BRIDGEFX, __name__ + ".HandleBridgeFX")

	pEvent2 = App.TGObjPtrEvent_Create()
	global ExpFX

	ExpFX = App.STRoundedButton_CreateW (App.TGString("ExplosionFX"), pEvent2, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	pEvent2.SetSource(ExpFX)
	pEvent2.SetDestination(MainConfigure)
	pEvent2.SetEventType(ET_EXPFX)


	ExpFX.SetNormalColor(App.g_kMainMenuButton1Color)
	ExpFX.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	ExpFX.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	ExpFX.SetDisabledColor(App.g_kSTMenu1Disabled)
	ExpFX.SetColorBasedOnFlags()
	ExpFX.SetVisible()

	MainConfigure.RemoveHandlerForInstance(ET_EXPFX, __name__ + ".HandleExplosionFX")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_EXPFX, __name__ + ".HandleExplosionFX")


	pEvent = App.TGObjPtrEvent_Create()
	global WarpFX

	WarpFX = App.STRoundedButton_CreateW (App.TGString("WarpFX"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	pEvent.SetSource(WarpFX)
	pEvent.SetDestination(MainConfigure)
	pEvent.SetEventType(ET_WARPFX)


	WarpFX.SetNormalColor(App.g_kMainMenuButton1Color)
	WarpFX.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	WarpFX.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	WarpFX.SetDisabledColor(App.g_kSTMenu1Disabled)
	WarpFX.SetColorBasedOnFlags()
	WarpFX.SetVisible()

	MainConfigure.RemoveHandlerForInstance(ET_WARPFX, __name__ + ".HandleWarpFX")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_WARPFX, __name__ + ".HandleWarpFX")

	pEvent = App.TGObjPtrEvent_Create()
	global SpecialFX

	SpecialFX = App.STRoundedButton_CreateW (App.TGString("SpecialFX"), pEvent, BridgeFX.GetWidth(), BridgeFX.GetHeight())
	pEvent.SetSource(SpecialFX)
	pEvent.SetDestination(MainConfigure)
	pEvent.SetEventType(ET_SPECIALFX)

	SpecialFX.SetNormalColor(App.g_kMainMenuButton1Color)
	SpecialFX.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	SpecialFX.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	SpecialFX.SetDisabledColor(App.g_kSTMenu1Disabled)
	SpecialFX.SetColorBasedOnFlags()
	SpecialFX.SetVisible()

	MainConfigure.RemoveHandlerForInstance(ET_SPECIALFX, __name__ + ".HandleSpecialFX")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_SPECIALFX, __name__ + ".HandleSpecialFX")

	pEvent = App.TGObjPtrEvent_Create()
	global CameraFX

	CameraFX = App.STRoundedButton_CreateW (App.TGString("CameraFX"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	pEvent.SetSource(CameraFX)
	pEvent.SetDestination(MainConfigure)
	pEvent.SetEventType(ET_CAMERAFX)


	CameraFX.SetNormalColor(App.g_kMainMenuButton1Color)
	CameraFX.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	CameraFX.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	CameraFX.SetDisabledColor(App.g_kSTMenu1Disabled)
	CameraFX.SetColorBasedOnFlags()
	CameraFX.SetVisible()

	MainConfigure.RemoveHandlerForInstance(ET_CAMERAFX, __name__ + ".HandleCameraFX")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_CAMERAFX, __name__ + ".HandleCameraFX")

	pEvent = App.TGObjPtrEvent_Create()
	global Default

	Default = App.STRoundedButton_CreateW (App.TGString("Restore Default"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	pEvent.SetSource(Default)
	pEvent.SetDestination(MainConfigure)
	pEvent.SetEventType(ET_DEFAULT)

	
	Default.SetNormalColor(App.g_kMainMenuButton1Color)
	Default.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	Default.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	Default.SetDisabledColor(App.g_kSTMenu1Disabled)
	Default.SetColorBasedOnFlags()
	Default.SetVisible()

	MainConfigure.RemoveHandlerForInstance(ET_DEFAULT, __name__ + ".HandleDefault")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_DEFAULT, __name__ + ".HandleDefault")

	pEvent = App.TGObjPtrEvent_Create()
	global SaveConfig

	SaveConfig = App.STRoundedButton_CreateW(App.TGString("Save Config"), pEvent, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT)
	pEvent.SetSource(SaveConfig)
	pEvent.SetDestination(MainConfigure)
	pEvent.SetEventType(ET_SAVECONFIG)


	SaveConfig.SetNormalColor(App.g_kMainMenuButton1Color)
	SaveConfig.SetHighlightedColor(App.g_kMainMenuButton1HighlightedColor)
	SaveConfig.SetSelectedColor(App.g_kMainMenuButton1SelectedColor)
	SaveConfig.SetDisabledColor(App.g_kSTMenu1Disabled)
	SaveConfig.SetColorBasedOnFlags()
	SaveConfig.SetVisible()


	MainConfigure.RemoveHandlerForInstance(ET_SAVECONFIG, __name__ + ".HandleSave")
	MainConfigure.AddPythonFuncHandlerForInstance(ET_SAVECONFIG, __name__ + ".HandleSave")

	x = BridgeFX.GetWidth() + 0.05
	MainConfigure.AddChild(BridgeFX, 0.0, 0.0, 0)
	MainConfigure.AddChild(CameraFX, x, 0.0, 0)
	y = BridgeFX.GetHeight() + 0.002
	MainConfigure.AddChild(SpecialFX, 0.0, y, 0)
	MainConfigure.AddChild(WarpFX, x, y, 0)
	y = y + BridgeFX.GetHeight() + 0.002
	MainConfigure.AddChild(ExpFX, 0.0, y, 0)
	MainConfigure.AddChild(Default, x, y, 0)
	BridgeFX.SetVisible()
	ExpFX.SetVisible()
	WarpFX.SetVisible()
	CameraFX.SetVisible()
	Default.SetVisible()
	SpecialFX.SetVisible()

	y = y + MainConfigure.GetHeight() - (4.6 * BridgeFX.GetHeight()+ 0.002)
	MainConfigure.AddChild(SaveConfig, 0.0,y,0)  #((MainConfigure.GetWidth() / 5) / 2) - (SaveConfig.GetWidth() / 2), MainConfigure.GetHeight() - SaveConfig.GetHeight(), 0)
	SaveConfig.SetVisible()

	## lennie update:
	## once again, i don't know of a better way here, since we're destroying
	## and reinit'ing the GUI every time!

	BridgeFX.SetSelectedFlag(0)
	ExpFX.SetSelectedFlag(0)
	WarpFX.SetSelectedFlag(0)
	CameraFX.SetSelectedFlag(0)
	Default.SetSelectedFlag(0)
	SpecialFX.SetSelectedFlag(0)
	SaveConfig.SetSelectedFlag(0)

	## darken the button to indicate what we're modifying
	if sActivePane == "BridgeFX":
		BridgeFX.SetSelectedFlag(1)

	elif sActivePane == "ExplosionFX":
		ExpFX.SetSelectedFlag(1)

	elif sActivePane == "WarpFX":
		WarpFX.SetSelectedFlag(1)

	elif sActivePane == "CameraFX":
		CameraFX.SetSelectedFlag(1)

	elif sActivePane == "SpecialFX":
		SpecialFX.SetSelectedFlag(1)
	

def HandleSave(pObject, pEvent):
	global MainConfigure, sActivePane

	WriteConfig()

	MainConfigure.KillChildren()
	MakeStanButtons()
	
	pObject = None
	pEvent  = None 

	## manually call the handler to redraw the active pane
	if sActivePane == "BridgeFX":
		HandleBridgeFX(pObject, pEvent)	
	elif sActivePane == "ExplosionFX":
		HandleExplosionFX(pObject, pEvent)	
	elif sActivePane == "CameraFX":
		HandleCameraFX(pObject, pEvent)	
	elif sActivePane == "WarpFX":
		HandleWarpFX(pObject, pEvent)	
	elif sActivePane == "SpecialFX":
		HandleSpecialFX(pObject, pEvent)	

def HandleBridgeFX(pObject, pEvent):
	global MainConfigure, BridgeFX, ET_USEBRIDGEFX, sActivePane
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	sActivePane = "BridgeFX"

	MainConfigure.KillChildren()
	MakeStanButtons()	

	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_USEBRIDGEFX)
	pEvent.SetDestination(MainConfigure)
	UseBridgeFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Bridge Effects"), ET_USEBRIDGEFX, Custom.NanoFXv2.NanoFX_Config.bFX_Enabled, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseBridgeFX)

	global ET_BRDFX_EXPSPK_LEVEL
	pOptionsWindow.RemoveHandlerForInstance(ET_USEBRIDGEFX, __name__ + ".HandleUseBridgeFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_USEBRIDGEFX, __name__ + ".HandleUseBridgeFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_BRDFX_EXPSPK_LEVEL, __name__ + ".HandleBrdFX_EXP_SPK")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_BRDFX_DAMSPK_LEVEL, __name__ + ".HandleBrdFX_DAM_SPK")
	MainConfigure.AddChild(UseBridgeFX, 0.0, (BridgeFX.GetHeight() * 4), 0)

	UseBridgeFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.bFX_Enabled)


	# Explosion Spark Level

	kStates = (	(App.TGString("Low"), ET_BRDFX_EXPSPK_LEVEL, 1),
			(App.TGString("Med"), ET_BRDFX_EXPSPK_LEVEL, 2),
			(App.TGString("High"), ET_BRDFX_EXPSPK_LEVEL, 3))
	pButton = CreateMenuToggleButton(App.TGString("Explosion Spark Level: "), kStates, Custom.NanoFXv2.NanoFX_Config.bFX_ExpSparkFXLevel - 1, MainConfigure.GetWidth())
	pButton.SetVisible()
	MainConfigure.AddChild(pButton, 0.0, (BridgeFX.GetHeight() * 4) + UseBridgeFX.GetHeight() + 0.01, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	# Damage Spark Level

	kStates = (	(App.TGString("Low"), ET_BRDFX_DAMSPK_LEVEL, 1),
			(App.TGString("Med"), ET_BRDFX_DAMSPK_LEVEL, 2),
			(App.TGString("High"), ET_BRDFX_DAMSPK_LEVEL, 3))
	pButton = CreateMenuToggleButton(App.TGString("Damage Spark Level: "), kStates, Custom.NanoFXv2.NanoFX_Config.bFX_DamageSparkFXLevel - 1, MainConfigure.GetWidth())
	pButton.SetVisible()
	MainConfigure.AddChild(pButton, 0.0, (BridgeFX.GetHeight() * 4) + (UseBridgeFX.GetHeight() * 2) + 0.015, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	# Damage Spark Duration
	global bFXDamageSparkDurationText

	pButton = App.STRoundedButton_CreateW (App.TGString("Damage Spark Duration:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (BridgeFX.GetHeight() * 4) + (UseBridgeFX.GetHeight() * 3) + 0.02, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	#if bFXDamageSparkDurationText == None:
	bFXDamageSparkDurationPreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.bFX_DamageSparkFXDuration)), UseBridgeFX.GetWidth(), "bFX_DamageSparkFXDuration")
	bFXDamageSparkDurationText = App.TGParagraph_Cast(bFXDamageSparkDurationPreText.GetNthChild(1))

	MainConfigure.AddChild(bFXDamageSparkDurationText, fWidth + 0.003, (BridgeFX.GetHeight() * 4) + (UseBridgeFX.GetHeight() * 3) + 0.02, 0)
	bFXDamageSparkDurationText.SetVisible()



	# Particle Control
	global bFXParticleControlText
		
	pButton = App.STRoundedButton_CreateW(App.TGString("Maximum particles:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (BridgeFX.GetHeight() * 4) + (UseBridgeFX.GetHeight() * 4) + 0.025, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	#if bFXParticleControlText == None:
	bFXParticleControlTextPre = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.bFX_ParticleControl)), UseBridgeFX.GetWidth(), "bFX_ParticleControl")
	bFXParticleControlText = App.TGParagraph_Cast(bFXParticleControlTextPre.GetNthChild(1))

	MainConfigure.AddChild(bFXParticleControlText, fWidth + 0.003, (BridgeFX.GetHeight() * 4) + (UseBridgeFX.GetHeight() * 4) + 0.025, 0)
	bFXParticleControlText.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)


def HandleUseBridgeFX(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.bFX_Enabled = App.STButton_Cast(pEvent.GetSource()).IsChosen ()
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleBrdFX_EXP_SPK(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.bFX_ExpSparkFXLevel = pEvent.GetInt()
	WriteConfig()

	if(pObject):
		pObject.CallNextHandler(pEvent)

def HandleBrdFX_DAM_SPK(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.bFX_DamageSparkFXLevel = pEvent.GetInt()
	WriteConfig()

	if(pObject):
		pObject.CallNextHandler(pEvent)

def HandleExplosionFX(pObject, pEvent):
	global MainConfigure, ExpFX, ET_USEEXPFX, ET_EXPLIGHTFLICKER, ET_FIXBRIGHTGLOWS, sActivePane
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	sActivePane = "ExplosionFX"

	MainConfigure.KillChildren()
	MakeStanButtons()

	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_USEEXPFX)
	pEvent.SetDestination(MainConfigure)
	UseExpFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enhance Explosion Sequences"), ET_USEEXPFX, Custom.NanoFXv2.NanoFX_Config.eFX_Enabled, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseExpFX)

	global ET_EXPFX_SPK_LEVEL, ET_EXPFX_DAM_SPK_LEVEL, ET_EXPFX_DEBRIS_LEVEL
	pOptionsWindow.RemoveHandlerForInstance(ET_USEEXPFX, __name__ + ".HandleUseExpFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_USEEXPFX, __name__ + ".HandleUseExpFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_EXPFX_SPK_LEVEL, __name__ + ".HandleExpFX_EXP_SPK")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_EXPFX_DAM_SPK_LEVEL, __name__ + ".HandleExpFX_DAM_SPK")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_EXPFX_DEBRIS_LEVEL, __name__ + ".HandleExpFX_DEBRIS")
	MainConfigure.AddChild(UseExpFX, 0.0, (ExpFX.GetHeight()) * 4, 0)
	UseExpFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.eFX_Enabled)


	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_EXPLIGHTFLICKER)
	pEvent.SetDestination(MainConfigure)
	LightFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Light Flicker"), ET_EXPLIGHTFLICKER, 0, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(LightFX)

	pOptionsWindow.RemoveHandlerForInstance(ET_EXPLIGHTFLICKER, __name__ + ".HandleExpLightFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_EXPLIGHTFLICKER, __name__ + ".HandleExpLightFX")
	MainConfigure.AddChild(LightFX, 0.0, (ExpFX.GetHeight() * 4) + UseExpFX.GetHeight() + 0.01, 0)

	if Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX == "On":
		LightFX.SetChosen(1)
	else:
		LightFX.SetChosen(0)

	LightFX.SetVisible()


	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_FIXBRIGHTGLOWS)
	pEvent.SetDestination(MainConfigure)
	LightFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Fix Bright Glow Bug"), ET_FIXBRIGHTGLOWS, 0, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(LightFX)

	pOptionsWindow.RemoveHandlerForInstance(ET_FIXBRIGHTGLOWS, __name__ + ".HandleFixBright")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_FIXBRIGHTGLOWS, __name__ + ".HandleFixBright")
	MainConfigure.AddChild(LightFX, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 2) + 0.015, 0)

	if Custom.NanoFXv2.NanoFX_Config.eFX_FixBrightGlows == "On":
		LightFX.SetChosen(1)
	else:
		LightFX.SetChosen(0)

	LightFX.SetVisible()


	# Explosion Spark Level
	
	kStates = (	(App.TGString("Low"), ET_EXPFX_SPK_LEVEL, 1),
			(App.TGString("Med"), ET_EXPFX_SPK_LEVEL, 2),
			(App.TGString("High"), ET_EXPFX_SPK_LEVEL, 3))
	pButton = CreateMenuToggleButton(App.TGString("Explosion Spark Level: "), kStates, Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel - 1, MainConfigure.GetWidth())
	pButton.SetVisible()
	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 3) + 0.02, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	# Damage Spark Level

	kStates = (	(App.TGString("Low"), ET_EXPFX_DAM_SPK_LEVEL, 1),
			(App.TGString("Med"), ET_EXPFX_DAM_SPK_LEVEL, 2),
			(App.TGString("High"), ET_EXPFX_DAM_SPK_LEVEL, 3))
	pButton = CreateMenuToggleButton(App.TGString("Damage Spark Level: "), kStates, Custom.NanoFXv2.NanoFX_Config.eFX_DamageSparkFXLevel - 1, MainConfigure.GetWidth())
	pButton.SetVisible()
	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 4) + 0.025, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	# Damage Spark Duration
	global eFXDamageSparkDurationText

	pButton = App.STRoundedButton_CreateW (App.TGString("Damage Spark Duration:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	#pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 5) + 0.03, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	#if eFXDamageSparkDurationText == None:
	eFXDamageSparkDurationPreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.eFX_DamageSparkFXDuration)), UseExpFX.GetWidth())
	eFXDamageSparkDurationText = App.TGParagraph_Cast(eFXDamageSparkDurationPreText.GetNthChild(1))

	MainConfigure.AddChild(eFXDamageSparkDurationText, fWidth + 0.003, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 5) + 0.03, 0)
	eFXDamageSparkDurationText.SetVisible()


	# Debris FX Level

	kStates = (	(App.TGString("Low"), ET_EXPFX_DEBRIS_LEVEL, 1),
			(App.TGString("Med"), ET_EXPFX_DEBRIS_LEVEL, 2),
			(App.TGString("High"), ET_EXPFX_DEBRIS_LEVEL, 3))
	pButton = CreateMenuToggleButton(App.TGString("Debris Level: "), kStates, Custom.NanoFXv2.NanoFX_Config.eFX_DebrisFXLevel - 1, MainConfigure.GetWidth())
	pButton.SetVisible()
	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 6) + 0.035, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()



	# Debris FX Duration
	global eFXDebrisFXDurationText

	pButton = App.STRoundedButton_CreateW (App.TGString("Debris Duration:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	#pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 7) + 0.04, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	#if eFXDebrisFXDurationText == None:
	eFXDebrisFXDurationPreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.eFX_DebrisFXDuration)), UseExpFX.GetWidth())
	eFXDebrisFXDurationText = App.TGParagraph_Cast(eFXDebrisFXDurationPreText.GetNthChild(1))

	MainConfigure.AddChild(eFXDebrisFXDurationText, fWidth + 0.003, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 7) + 0.04, 0)
	eFXDebrisFXDurationText.SetVisible()




	# Particle Control
	global eFXParticleControlText

	pButton = App.STRoundedButton_CreateW(App.TGString("Maximum particles:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	#pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 8) + 0.045, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	#if eFXParticleControlText == None:
	eFXParticleControlTextPre = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.eFX_ParticleControl)), UseExpFX.GetWidth())
	eFXParticleControlText = App.TGParagraph_Cast(eFXParticleControlTextPre.GetNthChild(1))

	MainConfigure.AddChild(eFXParticleControlText, fWidth + 0.003, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 8) + 0.045, 0)
	eFXParticleControlText.SetVisible()

	# Rotation FX
	global ET_ROTATION
	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_ROTATION)
	pEvent.SetDestination(MainConfigure)
	LightFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Critical Hit Rotations"), ET_ROTATION, 0, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(LightFX)

	pOptionsWindow.RemoveHandlerForInstance(ET_ROTATION, __name__ + ".HandleRotation")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_ROTATION, __name__ + ".HandleRotation")
	MainConfigure.AddChild(LightFX, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 9) + 0.05, 0)

	if Custom.NanoFXv2.NanoFX_Config.eFX_RotationFX == "On":
		LightFX.SetChosen(1)
	else:
		LightFX.SetChosen(0)

	LightFX.SetVisible()


	# Splash Radius
	global eFXSplashRadiusText

	pButton = App.STRoundedButton_CreateW(App.TGString("Damage Splash Radius:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	#pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 10) + 0.055, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	eFXSplashRadiusTextPre = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.eFX_SplashRadius)), UseExpFX.GetWidth())
	eFXSplashRadiusText = App.TGParagraph_Cast(eFXSplashRadiusTextPre.GetNthChild(1))
	#eFXSplashRadiusText.SetVisible()

	MainConfigure.AddChild(eFXSplashRadiusText, fWidth + 0.003, (ExpFX.GetHeight() * 4) + (UseExpFX.GetHeight() * 10) + 0.055, 0)
	eFXSplashRadiusText.SetVisible()


	if (pObject):
		pObject.CallNextHandler(pEvent)
	
def HandleUseExpFX(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.eFX_Enabled = App.STButton_Cast(pEvent.GetSource()).IsChosen()
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleExpLightFX(pObject, pEvent):
	pButton = App.STButton_Cast(pEvent.GetSource())
	bOn = pButton.IsChosen()
	if bOn == 1:
		Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX = "On"
	else:
		Custom.NanoFXv2.NanoFX_Config.eFX_LightFlickerFX = "Off"
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleFixBright(pObject, pEvent):
	pButton = App.STButton_Cast(pEvent.GetSource())
	bOn = pButton.IsChosen()
	if bOn == 1:
		Custom.NanoFXv2.NanoFX_Config.eFX_FixBrightGlows = "On"
	else:
		Custom.NanoFXv2.NanoFX_Config.eFX_FixBrightGlows = "Off"
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleExpFX_EXP_SPK(pObject, pEvent):
	pButton = App.STButton_Cast(pEvent.GetSource())
	Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel = pEvent.GetInt()

	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleExpFX_DAM_SPK(pObject, pEvent):
	pButton = App.STButton_Cast(pEvent.GetSource())
	Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel = pEvent.GetInt()

	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleRotation(pObject, pEvent):
	pButton = App.STButton_Cast(pEvent.GetSource())
	bOn = pButton.IsChosen()
	if bOn == 1:
		Custom.NanoFXv2.NanoFX_Config.eFX_Rotation = "On"
	else:
		Custom.NanoFXv2.NanoFX_Config.eFX_Rotation = "Off"
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleExpFX_DEBRIS(pObject, pEvent):
	pButton = App.STButton_Cast(pEvent.GetSource())
	Custom.NanoFXv2.NanoFX_Config.eFX_ExpSparkFXLevel = pEvent.GetInt()

	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleWarpFX(pObject, pEvent):
	global MainConfigure, WarpFX, ET_USEWARPFX, sActivePane
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	sActivePane = "WarpFX"

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	MainConfigure.KillChildren()
	MakeStanButtons()

	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_USEWARPFX)
	pEvent.SetDestination(MainConfigure)
	UseWarpFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enhance Warp Sequences"), ET_USEWARPFX, Custom.NanoFXv2.NanoFX_Config.wFX_Enabled, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseWarpFX)


	pOptionsWindow.RemoveHandlerForInstance(ET_USEWARPFX, "Custom.NanoFXv2.NanoFX_ConfigPanel.HandleUseWarpFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_USEWARPFX, "Custom.NanoFXv2.NanoFX_ConfigPanel.HandleUseWarpFX")
	MainConfigure.AddChild(UseWarpFX, 0.0, (WarpFX.GetHeight()) * 4, 0)
	UseWarpFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.wFX_Enabled)


	# Max Random Distance
	global wFXMaxRandomDistanceText

	pButton = App.STRoundedButton_CreateW(App.TGString("Maximum Travel Duration"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (WarpFX.GetHeight() * 4) + (UseWarpFX.GetHeight()) + 0.005, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()

	wFXMaxRandomDistanceTextPre = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.wFX_MaxRandomDistance)), UseWarpFX.GetWidth())
	wFXMaxRandomDistanceText = App.TGParagraph_Cast(wFXMaxRandomDistanceTextPre.GetNthChild(1))
	wFXMaxRandomDistanceText.SetVisible()

	MainConfigure.AddChild(wFXMaxRandomDistanceText, fWidth + 0.003, (WarpFX.GetHeight() * 4) + (UseWarpFX.GetHeight()) + 0.005, 0)
	wFXMaxRandomDistanceText.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)


def HandleUseWarpFX(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.wFX_Enabled = App.STButton_Cast(pEvent.GetSource()).IsChosen ()
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleCameraFX(pObject, pEvent):
	global MainConfigure, CameraFX, ET_USECAMERAFX, sActivePane
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	sActivePane = "CameraFX"

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	MainConfigure.KillChildren()
	MakeStanButtons()

	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_USECAMERAFX)
	pEvent.SetDestination(MainConfigure)
	UseCameraFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Camera Effects"), ET_USECAMERAFX, Custom.NanoFXv2.NanoFX_Config.cFX_Enabled, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseCameraFX)


	pOptionsWindow.RemoveHandlerForInstance(ET_USECAMERAFX, "Custom.NanoFXv2.NanoFX_ConfigPanel.HandleUseCameraFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_USECAMERAFX, "Custom.NanoFXv2.NanoFX_ConfigPanel.HandleUseCameraFX")
	MainConfigure.AddChild(UseCameraFX, 0.0, (CameraFX.GetHeight()) * 4, 0)
	UseCameraFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.cFX_Enabled)
	UseCameraFX.SetVisible()

	# View Screen Default
	global cFXViewScreenDefaultText

	pButton = App.STRoundedButton_CreateW (App.TGString("Viewscreen Default Zoom:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (CameraFX.GetHeight() * 4) + UseCameraFX.GetHeight() + 0.01, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	cFXViewScreenDefaultPreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.cFX_ViewScreenDefault)), UseCameraFX.GetWidth())
	cFXViewScreenDefaultText = App.TGParagraph_Cast(cFXViewScreenDefaultPreText.GetNthChild(1))
	cFXViewScreenDefaultText.SetVisible()

	MainConfigure.AddChild(cFXViewScreenDefaultText, fWidth + 0.003, (CameraFX.GetHeight() * 4) + UseCameraFX.GetHeight() + 0.01, 0)
	cFXViewScreenDefaultText.SetVisible()



	# View Screen Max
	global cFXViewScreenMaxText

	pButton = App.STRoundedButton_CreateW(App.TGString("Viewscreen Maximal Zoom:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (CameraFX.GetHeight() * 4) + (UseCameraFX.GetHeight() * 2) + 0.015, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	cFXViewScreenMaxPreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.cFX_ViewScreenMax)), UseCameraFX.GetWidth())
	cFXViewScreenMaxText = App.TGParagraph_Cast(cFXViewScreenMaxPreText.GetNthChild(1))
	cFXViewScreenMaxText.SetVisible()

	MainConfigure.AddChild(cFXViewScreenMaxText, fWidth + 0.003, (CameraFX.GetHeight() * 4) + (UseCameraFX.GetHeight() * 2) + 0.015, 0)
	cFXViewScreenMaxText.SetVisible()



	# View Screen Max
	global cFXAwayDistanceText

	pButton = App.STRoundedButton_CreateW(App.TGString("Flyby Side Offset:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (CameraFX.GetHeight() * 4) + (UseCameraFX.GetHeight() * 3) + 0.02, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	cFXAwayDistancePreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.cFX_AwayDistance)), UseCameraFX.GetWidth())
	cFXAwayDistanceText = App.TGParagraph_Cast(cFXAwayDistancePreText.GetNthChild(1))
	cFXAwayDistanceText.SetVisible()

	MainConfigure.AddChild(cFXAwayDistanceText, fWidth + 0.003, (CameraFX.GetHeight() * 4) + (UseCameraFX.GetHeight() * 3) + 0.02, 0)
	cFXAwayDistanceText.SetVisible()


	# View Screen Max
	global cFXAwayForwardText

	pButton = App.STRoundedButton_CreateW(App.TGString("Flyby Forward Offset:"), None, LCARS.MAIN_MENU_TOP_BUTTON_WIDTH * 1.5, MainMenu.mainmenu.CLIENT_START_BUTTON_HEIGHT / 1.9, 1)
	pButton.SetDisabledColor(App.g_kMainMenuBorderMainColor)
	pButton.SetDisabled (0)
	pButton.SetColorBasedOnFlags()
	pButton.SetVisible()

	MainConfigure.AddChild(pButton, 0.0, (CameraFX.GetHeight() * 4) + (UseCameraFX.GetHeight() * 4) + 0.025, 0)
	pButton.SetVisible()
	fWidth = pButton.GetWidth ()


	cFXAwayForwardPreText = CreateTextEntry(App.TGString(str(Custom.NanoFXv2.NanoFX_Config.cFX_ForwardDistance)), UseCameraFX.GetWidth())
	cFXAwayForwardText = App.TGParagraph_Cast(cFXAwayForwardPreText.GetNthChild(1))
	cFXAwayForwardText.SetVisible()

	MainConfigure.AddChild(cFXAwayForwardText, fWidth + 0.003, (CameraFX.GetHeight() * 4) + (UseCameraFX.GetHeight() * 4) + 0.025, 0)
	cFXAwayForwardText.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleUseCameraFX(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.cFX_Enabled = App.STButton_Cast(pEvent.GetSource()).IsChosen ()
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleSpecialFX(pObject, pEvent):
	global MainConfigure, SpecialFX, ET_USESPECIALFX, sActivePane
	pTopWindow = App.TopWindow_GetTopWindow()
	if (pTopWindow == None):
		return
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	sActivePane = "SpecialFX"

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	MainConfigure.KillChildren()
	MakeStanButtons()

	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_USESPECIALFX)
	pEvent.SetDestination(MainConfigure)
	UseSpecialFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Special Effects"), ET_USESPECIALFX, Custom.NanoFXv2.NanoFX_Config.sFX_Enabled, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseSpecialFX)

	pOptionsWindow.RemoveHandlerForInstance(ET_USESPECIALFX, __name__ + ".HandleUseSpecialFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_USESPECIALFX, __name__ + ".HandleUseSpecialFX")
	MainConfigure.AddChild(UseSpecialFX, 0.0, (SpecialFX.GetHeight()) * 4, 0)
	UseSpecialFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.sFX_Enabled)
	UseSpecialFX.SetVisible()

	fHeigth = UseSpecialFX.GetHeight() + 0.005

	# Atmosphere Glow FX
	global ET_ATMOS
	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_ATMOS)
	pEvent.SetDestination(MainConfigure)
	UseSpecialFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Planet Atmospheres"), ET_ATMOS, 0, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseSpecialFX)

	pOptionsWindow.RemoveHandlerForInstance(ET_ATMOS, __name__ + ".HandleUseAtmosFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_ATMOS, __name__ + ".HandleUseAtmosFX")
	MainConfigure.AddChild(UseSpecialFX, 0.0, (SpecialFX.GetHeight() * 4) + fHeigth, 0)
	UseSpecialFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.sFX_Enabled)
	UseSpecialFX.SetVisible()

	fHeigth = fHeigth + UseSpecialFX.GetHeight() + 0.005

	if Custom.NanoFXv2.NanoFX_Config.sFX_AtmosphereGlowFX== "On":
		UseSpecialFX.SetChosen(1)
	else:
		UseSpecialFX.SetChosen(0)

	# Plasma FX
	global ET_PLASMAFX
	pEvent = App.TGObjPtrEvent_Create()
	pEvent.SetEventType(ET_PLASMAFX)
	pEvent.SetDestination(MainConfigure)
	UseSpecialFX = MainMenu.mainmenu.CreateMenuYesNoButton(App.TGString("Enable Nacelle Venting"), ET_PLASMAFX, 0, MainConfigure.GetWidth() / 5)
	pEvent.SetSource(UseSpecialFX)


	if Custom.NanoFXv2.NanoFX_Config.sFX_PlasmaFX== "On":
		UseSpecialFX.SetChosen(1)
	else:
		UseSpecialFX.SetChosen(0)

	pOptionsWindow.RemoveHandlerForInstance(ET_ATMOS, __name__ + ".HandlePlasmaFX")
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_ATMOS, __name__ + ".HandlePlasmaFX")
	MainConfigure.AddChild(UseSpecialFX, 0.0, (SpecialFX.GetHeight() * 4) + fHeigth, 0)
	UseSpecialFX.SetChosen(Custom.NanoFXv2.NanoFX_Config.sFX_Enabled)
	UseSpecialFX.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleUseSpecialFX(pObject, pEvent):
	Custom.NanoFXv2.NanoFX_Config.sFX_Enabled = App.STButton_Cast(pEvent.GetSource()).IsChosen ()
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleUseAtmosFX(pObject, pEvent):
	if App.STButton_Cast(pEvent.GetSource()).IsChosen() == 1:
		Custom.NanoFXv2.NanoFX_Config.sFX_AtmosphereGlowFX = "On"
	else:
		Custom.NanoFXv2.NanoFX_Config.sFX_AtmosphereGlowFX = "Off"
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandlePlasmaFX(pObject, pEvent):
	if App.STButton_Cast(pEvent.GetSource()).IsChosen() == 1:
		Custom.NanoFXv2.NanoFX_Config.sFX_PlasmaFX = "On"
	else:
		Custom.NanoFXv2.NanoFX_Config.sFX_PlasmaFX = "Off"
	WriteConfig()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def HandleDefault(pObject, pEvent):
	global MainConfigure, sActivePane
	#MainConfigure.KillChildren()
	#MakeStanButtons()

	#sActivePane = "Default"

	m = __import__("Custom.NanoFXv2.NanoFX_Config")

	TRUE = 1
	FALSE = 0	

	## to vars in memory
	m.bFX_Enabled = FALSE
	m.bFX_ExpSparkFXLevel = 3
	m.bFX_DamageSparkFXLevel = 3
	m.bFX_DamageSparkFXDuration = 60.0
	m.bFX_ParticleControl = 200

	m.cFX_Enabled = TRUE
	m.cFX_ViewScreenDefault = 8.0
	m.cFX_ViewScreenMax = 128.0
	m.cFX_AwayDistance = 8.0 
	m.cFX_ForwardDistance = 8.0

	m.eFX_Enabled = TRUE
	m.eFX_LightFlickerFX = "On"
	m.eFX_FixBrightGlows = "On"
	m.eFX_ExpSparkFXLevel = "On"

	m.eFX_ExpSparkFXLevel = 3
	m.eFX_DamageSparkFXLevel = 3
	m.eFX_DamageSparkFXDuration = 60.0
	m.eFX_DebrisFXLevel = 3
	m.eFX_DebrisFXDuration = 30.0
	m.eFX_RotationFX = "On"
	m.eFX_ParticleControl = 300
	m.eFX_SplashRadius = 25.0

	m.wFX_Enabled = TRUE
	m.wFX_MaxRandomDistance = 30

	m.sFX_Enabled = TRUE
	m.sFX_AtmosphereGlowFX = "On"
	m.sFX_PlasmaFX = "On"

	global MainConfigure, sActivePane

	MainConfigure.KillChildren()
	MakeStanButtons()
	
	pObject = None
	pEvent  = None 

	## manually call the handler to redraw the active pane
	if sActivePane == "BridgeFX":
		HandleBridgeFX(pObject, pEvent)	
	elif sActivePane == "ExplosionFX":
		HandleExplosionFX(pObject, pEvent)	
	elif sActivePane == "CameraFX":
		HandleCameraFX(pObject, pEvent)	
	elif sActivePane == "WarpFX":
		HandleWarpFX(pObject, pEvent)	
	elif sActivePane == "SpecialFX":
		HandleSpecialFX(pObject, pEvent)


	import nt
	Out = "TRUE = 1\n"
	Out = Out + "FALSE = 0\n"
	Out = Out + "###[BridgeFX Settings]###\n"
	Out = Out + "bFX_Enabled = FALSE\n"
	Out = Out + "###\nbFX_ExpSparkFXLevel = 3\n"
	Out = Out + "bFX_DamageSparkFXLevel = 3\n"
	Out = Out + "bFX_DamageSparkFXDuration = 60.0\n"
	Out = Out + "bFX_ParticleControl = 200\n"
	Out = Out + "###\n"
	Out = Out + "###[CameraFX Settings]###\n"
	Out = Out + "cFX_Enabled = TRUE\n"
	Out = Out + "###\n"
	Out = Out + "cFX_ViewScreenDefault = 8.0\n"
	Out = Out + "cFX_ViewScreenMax = 128.0\n"
	Out = Out + "cFX_AwayDistance = 8.0\n"
	Out = Out + "cFX_ForwardDistance = 8.0\n"
	Out = Out + "###\n"
	Out = Out + "###[ExplosionFX Settings]###\n"
	Out = Out + "eFX_Enabled = TRUE\n"
	Out = Out + "###\n"
	Out = Out + "eFX_LightFlickerFX = \"On\"\n"
	Out = Out + "eFX_FixBrightGlows = \"On\"\n"
	Out = Out + "eFX_ExpSparkFXLevel = 3\n"
	Out = Out + "eFX_DamageSparkFXLevel = 3\n"
	Out = Out + "eFX_DamageSparkFXDuration = 60.0\n"
	Out = Out + "eFX_DebrisFXLevel = 3\n"
	Out = Out + "eFX_DebrisFXDuration = 30.0\n"
	Out = Out + "eFX_ParticleControl = 300\n"
	Out = Out + "eFX_RotationFX = \"On\"\n"
	Out = Out + "eFX_SplashRadius = 25.0\n"
	Out = Out + "###\n"
	Out = Out + "###[SpecialFX Settings]###\n"
	Out = Out + "sFX_Enabled = TRUE\n"
	Out = Out + "###\n"
	Out = Out + "sFX_AtmosphereGlowFX = \"On\"\n"
	Out = Out + "sFX_PlasmaFX = \"On\"\n"
	Out = Out + "###\n"
	Out = Out + "###[WarpFX Settings]###\n"
	Out = Out + "wFX_Enabled = TRUE\n"
	Out = Out + "###\n"
	Out = Out + "wFX_MaxRandomDistance = 30\n"
	Out = Out + "###\n"

	global ConfigPath
	ConFile = nt.open(ConfigPath, nt.O_WRONLY|nt.O_TRUNC|nt.O_CREAT)
	nt.write(ConFile, Out)
	nt.close(ConFile)

	reload(m)
	if (pObject):
		pObject.CallNextHandler(pEvent)

def WriteConfig(pObject = None, pEvent = None):
	global ConfigPath
	m = __import__("Custom.NanoFXv2.NanoFX_Config")

	global bFXDamageSparkDurationText
	global bFXbParticleControlText, cFXViewScreenDefaultText, cFXViewScreenMaxText
	global cFXAwayDistanceText, cFXAwayForwardText
	global eFXDamageSparkDurationText, eFXbParticleControlText
	global eFXDebrisFXDurationText, eFXSplashRadiusText, wFXMaxRandomDistanceText
	global eFXExpSparkLevelText, sActivePane

	import nt
	n = "\n"
	Out = "TRUE = 1" + n
	Out = Out + "FALSE = 0" + n
	Out = Out + "###[BridgeFX Settings]###" + n
	
	TRUE = 1
	FALSE = 0

	if m.bFX_Enabled == 0:
		Out = Out + "bFX_Enabled = FALSE" + n
		m.bFX_Enabled = FALSE

	else:
		Out = Out + "bFX_Enabled = TRUE" + n
		m.bFX_Enabled = TRUE

	Out = Out + "###" + n

	#### lennie update:
	#
	# these vars are only initialized if the respective handler has been called; otherwise
	# they're null and we'll just use the vals directly from NanoFX_Config.

	#### MLeoDaalder ReUpdate:
	#
	# I'm no longer using text boxes for the levels.
	if sActivePane == "BridgeFX":
		
		Out = Out + "bFX_ExpSparkFXLevel = " + str(m.bFX_ExpSparkFXLevel) + n
		Out = Out + "bFX_DamageSparkFXLevel = " +  str(m.bFX_DamageSparkFXLevel)  + n
		Out = Out + "bFX_DamageSparkFXDuration = " + bFXDamageSparkDurationText.GetCString() + n
		Out = Out + "bFX_ParticleControl = " + bFXParticleControlText.GetCString() + n

	else:
		Out = Out + "bFX_ExpSparkFXLevel = " + str(m.bFX_ExpSparkFXLevel) + n
		Out = Out + "bFX_DamageSparkFXLevel = " + str(m.bFX_DamageSparkFXLevel) + n
		Out = Out + "bFX_DamageSparkFXDuration = " + str(m.bFX_DamageSparkFXDuration) + n
		Out = Out + "bFX_ParticleControl = " + str(m.bFX_ParticleControl) + n


	Out = Out + "###" + n
	Out = Out + "###[CameraFX Settings]###" + n

	if m.cFX_Enabled == 0:
		Out = Out + "cFX_Enabled = FALSE" + n
		m.cFX_Enabled = FALSE
	else:
		Out = Out + "cFX_Enabled = TRUE" + n
		m.cFX_Enabled = TRUE

	Out = Out + "###" + n

	if sActivePane == "CameraFX":
		Out = Out + "cFX_ViewScreenDefault = " + cFXViewScreenDefaultText.GetCString() + n
		Out = Out + "cFX_ViewScreenMax = " + cFXViewScreenMaxText.GetCString() + n
		Out = Out + "cFX_AwayDistance = " + cFXAwayDistanceText.GetCString() + n
		Out = Out + "cFX_ForwardDistance = " + cFXAwayForwardText.GetCString() + n

		## updates to vars in memory:
		m.cFX_ViewScreenDefault = float(cFXViewScreenDefaultText.GetCString())
		m.cFX_ViewScreenMax = float(cFXViewScreenMaxText.GetCString())
		m.cFX_AwayDistance = float(cFXAwayDistanceText.GetCString())
		m.cFX_ForwardDistance = float(cFXAwayForwardText.GetCString())
	else:
		Out = Out + "cFX_ViewScreenDefault = " + str(m.cFX_ViewScreenDefault) + n
		Out = Out + "cFX_ViewScreenMax = " + str(m.cFX_ViewScreenMax) + n
		Out = Out + "cFX_AwayDistance = " + str(m.cFX_AwayDistance) + n
		Out = Out + "cFX_ForwardDistance = " + str(m.cFX_ForwardDistance) + n

	Out = Out + "###" + n
	Out = Out + "###[ExplosionFX Settings]###" + n

	if m.eFX_Enabled == 0:
		Out = Out + "eFX_Enabled = FALSE" + n
		m.eFX_Enabled = FALSE
	else:
		Out = Out + "eFX_Enabled = TRUE" + n
		m.eFX_Enabled = TRUE

	Out = Out + "###" + n

	Out = Out + "eFX_LightFlickerFX = \"" + m.eFX_LightFlickerFX + "\"" + n

	Out = Out + "eFX_FixBrightGlows = \"" + m.eFX_FixBrightGlows + "\"" + n

	if sActivePane == "ExplosionFX":

		Out = Out + "eFX_ExpSparkFXLevel = " + str(m.eFX_ExpSparkFXLevel) + n
		Out = Out + "eFX_DamageSparkFXLevel = " + str(m.eFX_DamageSparkFXLevel) + n
		Out = Out + "eFX_DamageSparkFXDuration = " + eFXDamageSparkDurationText.GetCString()  + n
		Out = Out + "eFX_DebrisFXLevel = " + str(m.eFX_DebrisFXLevel) + n
		Out = Out + "eFX_DebrisFXDuration = " + eFXDebrisFXDurationText.GetCString() + n
		Out = Out + "eFX_ParticleControl = " + eFXParticleControlText.GetCString() + n

	else:
		Out = Out + "eFX_ExpSparkFXLevel = " + str(m.eFX_ExpSparkFXLevel) + n
		Out = Out + "eFX_DamageSparkFXLevel = " + str(m.eFX_DamageSparkFXLevel) + n
		Out = Out + "eFX_DamageSparkFXDuration = " + str(m.eFX_DamageSparkFXDuration)  + n
		Out = Out + "eFX_DebrisFXLevel = " + str(m.eFX_DebrisFXLevel) + n
		Out = Out + "eFX_DebrisFXDuration = " + str(m.eFX_DebrisFXDuration) + n
		Out = Out + "eFX_ParticleControl = " + str(m.eFX_ParticleControl) + n


	Out = Out + "eFX_RotationFX = \"" + m.eFX_RotationFX + "\"" + n

	if sActivePane == "ExplosionFX":
		Out = Out + "eFX_SplashRadius = " + eFXSplashRadiusText.GetCString() + n
		m.eFX_SplashRadius = float(eFXSplashRadiusText.GetCString())

	else:
		Out = Out + "eFX_SplashRadius = " + str(m.eFX_SplashRadius) + n

	Out = Out + "###" + n
	Out = Out + "###[SpecialFX Settings]###" + n

	if m.sFX_Enabled == 0:
		Out = Out + "sFX_Enabled = FALSE" + n
		m.sFX_Enabled = FALSE

	else:
		Out = Out + "sFX_Enabled = TRUE" + n
		m.sFX_Enabled = TRUE

	Out = Out + "###" + n

	Out = Out + "sFX_AtmosphereGlowFX = \"" + m.sFX_AtmosphereGlowFX + "\"" + n
	Out = Out + "sFX_PlasmaFX = \"" + m.sFX_PlasmaFX + "\"" + n


	Out = Out + "###" + n
	Out = Out + "###[WarpFX Settings]###" + n

	if m.wFX_Enabled == 1:
		Out = Out + "wFX_Enabled = TRUE" + n
		m.wFX_Enabled = TRUE

	else:
		Out = Out + "wFX_Enabled = FALSE" + n
		m.wFX_Enabled = FALSE

	Out = Out + "###" + n

	if sActivePane == "WarpFX":
		Out = Out + "wFX_MaxRandomDistance = " + wFXMaxRandomDistanceText.GetCString() + n
		
		m.wFX_MaxRandomDistance = int(wFXMaxRandomDistanceText.GetCString())
	else:
		Out = Out + "wFX_MaxRandomDistance = " + str(m.wFX_MaxRandomDistance) + n

	Out = Out + "###" + n
	ConFile = nt.open(ConfigPath, nt.O_WRONLY|nt.O_TRUNC|nt.O_CREAT)
	nt.write(ConFile, Out)

	if (pObject):
		pObject.CallNextHandler(pEvent)

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
def CreateTextEntry(pDefault, fMaxWidth, sIndex = "Name: "):
	# First create a pane for this.
	pPane = App.TGPane_Create (fMaxWidth, 1.0)

	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	# Create the text tag

	pText = App.TGParagraph_CreateW(App.TGString(sIndex)) #App.TGPane_Create() #Paragraph_CreateW(App.TGString("Name: "))
	fWidth = pText.GetWidth ()
	pPane.AddChild (pText, fWidth, 0)
		
	# Create the name entry button
	# Get LCARS string
	pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode()
	pcLCARS = pGraphicsMode.GetLcarsString()

	if (pDefault == None):
		pTextEntry = App.TGParagraph_Create ("Default")
	else:
		pTextEntry = App.TGParagraph_CreateW (pDefault)

	pTextEntry.Resize (fMaxWidth - fWidth, pTextEntry.GetHeight (), 0)
	pTextEntry.SetReadOnly (0)

	pPane.AddChild (pTextEntry, fWidth + 0.005, (LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT - pTextEntry.GetHeight ()) / 2.0)

	pBackground = App.TGIcon_Create(pcLCARS, 200, App.g_kTextEntryColor)
	pBackground.Resize (fMaxWidth - fWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)
	pPane.AddChild (pBackground, fWidth, 0)


	# Now resize the pane to be the height of text entry
	pPane.Resize (fMaxWidth, LCARS.MAIN_MENU_TOP_BUTTON_HEIGHT, 0)

	return pPane
	
def CreateMenuYesNoButton(pName, eType, iState):
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pOptionsWindow)

	pMenuButton = App.STButton_CreateW(pName, pEvent)
	pEvent.SetSource (pMenuButton)

	pMenuButton.SetChoosable (1)
	pMenuButton.SetAutoChoose (1)
	pMenuButton.SetChosen (iState)

	return pMenuButton

def MoveNanoDown(pObject, pEvent):
	global NanoFXButton1, NanoFXButton2
	NanoFXButton1.SetNotVisible()
	NanoFXButton2.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def MoveNanoUp(pObject, pEvent):
	global NanoFXButton1, NanoFXButton2
	NanoFXButton2.SetNotVisible()
	NanoFXButton1.SetVisible()

	if (pObject):
		pObject.CallNextHandler(pEvent)

def CreateMenuToggleButton(pName, kStates, iDefault, fWidth):
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

	kArgs = [pName, iDefault]

	for kStateName, eEventType, iEventValue in kStates:
		pEvent = App.TGIntEvent_Create()
		pEvent.SetEventType(eEventType)
		pEvent.SetDestination(pOptionsWindow)
		pEvent.SetInt(iEventValue)

		kArgs.append(kStateName)
		kArgs.append(pEvent)

	kMenuButton = apply(App.STToggle_CreateW, kArgs)

	return kMenuButton

