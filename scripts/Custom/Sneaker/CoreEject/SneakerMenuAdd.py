import App
import Bridge.BridgeUtils
import Bridge.XOMenuHandlers

def SneakerCreateMenus():
#	kDebugObj.Print("Creating XO Menu\n")

	pTopWindow = App.TopWindow_GetTopWindow()
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()

	# Import resolution dependent LCARS module for size/placement variables.
	LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

	###############################################################################
	# XO
	###############################################################################
	#
	#	Commander
	#		Set Alert Level
	#			Green
	#			Yellow
	#			Red
	#		Report
	#		Contact Engineering
	#		Objectives
	#		Contact Starfleet
	#
	###############################################################################

	pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")

	#pXOPane = App.TGPane_Create(LCARS.TACTICAL_MENU_WIDTH, LCARS.TACTICAL_MENU_HEIGHT)
	pXOMenu = App.STTopLevelMenu_CreateW(pDatabase.GetString("Commander"))
	pXOPane = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", pDatabase.GetString("Commander"), 0.0, 0.0)
	pXOPane.AddChild(pXOMenu, 0.0, 0.0, 0)

	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_ST_BUTTON_CLICKED, "Bridge.BridgeMenus.ButtonClicked")

	# Communicate
	import Bridge.BridgeMenus
	pCommunicate = Bridge.BridgeMenus.CreateCommunicateButton("XO", pXOMenu)
	pXOMenu.AddChild(pCommunicate, 0.0, 0.0, 0)

	# Report
	pReport = Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Damage Report"), App.ET_REPORT, 0, pXOMenu)
	pXOMenu.AddChild(pReport, 0.0, 0.0, 0)

	# Alert Levels
	pXOMenu.AddChild(Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Green Alert"),		App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_GREEN, pXOMenu), 0.0, 0.0, 0)
	pXOMenu.AddChild(Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Yellow Alert"),	App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_YELLOW, pXOMenu), 0.0, 0.0, 0)
	pXOMenu.AddChild(Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Red Alert"),		App.ET_SET_ALERT_LEVEL, App.CharacterClass.EST_ALERT_RED, pXOMenu), 0.0, 0.0, 0)

	# Objectives
	pObjectives = App.STCharacterMenu_CreateW(pDatabase.GetString("Objectives"))
	pXOMenu.AddChild(pObjectives, 0.0, 0.0, 0)

	# Mission Log
	pShowLog = Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Show Mission Log"),				App.ET_SHOW_MISSION_LOG, 0, pXOMenu)
	pXOMenu.AddChild(pShowLog, 0.0, 0.0, 0)

	# Contact Starfleet
	pContactStarfleet = Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Contact Starfleet"),		App.ET_CONTACT_STARFLEET, 0, pXOMenu)
	pXOMenu.AddChild(pContactStarfleet, 0.0, 0.0, 0)

	# Contact Engineering
	pContactEngineering = Bridge.BridgeUtils.CreateBridgeMenuButton(pDatabase.GetString("Contact Engineering"),	App.ET_CONTACT_ENGINEERING, 0, pXOMenu)
	pXOMenu.AddChild(pContactEngineering, 0.0, 0.0, 0)
	pContactEngineering.SetDisabled()

	# If in multiplayer, disable all single-player specific buttons	
	if (App.g_kUtopiaModule.IsMultiplayer()):
		pReport.SetDisabled()
		pCommunicate.SetDisabled()
		pObjectives.SetDisabled()
		pShowLog.SetDisabled()
		pContactStarfleet.SetDisabled()
		pContactEngineering.SetDisabled()

	###Unload database
	App.g_kLocalizationManager.Unload(pDatabase)

	pXOPane.SetNotVisible()
	pXOMenu.SetNotVisible()

	# We don't want the "skip parent" behavior in this case, because otherwise
	# menu items would think that the window was their parent.
	pXOMenu.SetNoSkipParent()

	# Add the pane to the Top window, so we can see it in both Tactical
	# and Bridge views
	pTacticalControlWindow.AddChild(pXOPane, 0.0, 0.0, 0)
	pTacticalControlWindow.AddMenuToList(pXOMenu)

	# Add Python function handlers.
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL,		"Bridge.XOMenuHandlers" + ".SetAlertLevel")
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_OBJECTIVES,			"Bridge.XOMenuHandlers" + ".Objectives")
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_CONTACT_ENGINEERING, "Bridge.EngineerCharacterHandlers.ContactEngineering")
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_COMMUNICATE,			"Bridge.Characters.CommonAnimations.NothingToAdd")
	pXOMenu.AddPythonFuncHandlerForInstance(App.ET_SHOW_MISSION_LOG,	"Bridge.XOMenuHandlers" + ".ShowLog")

	###########################sneaker add
	import Custom.Sneaker.CoreEject.SneakerCoreMenuHandlers
	Custom.Sneaker.CoreEject.SneakerCoreMenuHandlers.SneakerCoreCreateMenu(pXOMenu)

	try:
		import Custom.Sneaker.SneakerXOMenuHandlers
		Custom.Sneaker.SneakerXOMenuHandlers.SneakerCreateMenu(pXOMenu)
	except:
		# basically, it failed. Do something so the compiler is happy
		DoNothing = "WhoCares"

	#######################end sneaker add

	return pXOMenu