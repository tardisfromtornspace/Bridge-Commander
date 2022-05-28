from bcdebug import debug
# Unified Main Main V1.0
# by MLeo Daalder
#
# This project aims to solve the diffrent versions of MainMenu.py problem by
# providing an interface for scripters to add their own items.
#
# Licence:
#  Third party scripters are allowed to redistribute the original package in their mods,
#  although it is advised that they link to the latest version just to be sure.
#  If you, as third party scripter, decide to include this mod, then I would find it very nice
#  to see my name in the credits.
#
#  No special permission is needed to redistribute the original, unmodified package (and all files there in).
#  However, if you do have made modifications to this mod, or any files in the package, then you _MUST_ run it
#  by me as I'd like to test it for problems.
#
# Creating Main Menu Mods:
#  There are several types of mods, though all are the same setup (save for the startup mods)
#  These types are (behind the name is the place to put the file):
#  StartUp (StartupModules)
#  Configurations (ConfigModules)
#  Configurations::Options (ConfigModules/Options)
#  Configurations::Options::General (ConfigModules/Options/General)
#  Configurations::Options::Sound (ConfigModules/Options/Sound)
#  Configurations::Options::Graphics (ConfigModules/Options/Graphics)
#
#  All locations are relative to your BC path and the following path:
#  scripts/Custom/UnifiedMainMenu/
#
#  As for the basic structure of your plugin, you need atleast 2 functions.
#   GetName - this must return the name of your mod
#     It has no arguments
#   CreateMenu - this must return your configuration screen, if there isn't one, then return None
#     It has the following arguments:
#      pOptionsPane - pOptionsPane is the right hand side of the options window, can be entered as None (in the stock scripts it isn't really used, except for the keyboard configuration)
#      pContentPanel - this is the direct "parent" your UI will be added to.
#      bGameEnded - wether or not the game ended, must defaults to 0
#
#  There is an exception, namely in the StartUp modules. These mods have an extra function:
#   StartUp - this doesn't return anything, and it will have to contain all the code you need for your mod to be "hooked" into BC
#     It has no arguments


import App

dMenus = {}

# This is the startup function
#
# Scripts loading function based on Foundation
def StartUp():
    debug(__name__ + ", StartUp")
    if not App.g_kConfigMapping.LoadConfigFile("options.cfg"):
        App.g_kConfigMapping.SaveConfigFile("options.cfg")
    if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", "Master Switch"):
        App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", "Master Switch", 0)
        App.g_kConfigMapping.SaveConfigFile("options.cfg")

    global dMenus
    # Load all the plugins...
    
    # Startup
    LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\StartupModules", "StartUp")
    
    # Keyboard
    #LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\KeyboardModules", "Keyboard")
    
    # Configuration
    LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules", "Config")
    
    # Config::Options
    LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options", "Config::Options")
    
    # Config::Options::General
    LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\General", "Config::Options::General")
    # Config::Options::Sound
    LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\Sound", "Config::Options::Sound")
    # Config::Options::Graphics
    LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\Graphics", "Config::Options::Graphics")
    
    #LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\LoadGame", "Config::LoadGame")
    # Config::Missions
    #LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Missions", "Config::Missions")
    # Config::LoadGame
    #LoadPlugins("scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\NewGame", "Config::NewGame")

    if App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", "Master Switch"):
        for plugin in dMenus["StartUp"]:
            if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", plugin[1]):
                App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", plugin[1], 0)
                continue
            elif App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", plugin[1]):
                __import__(plugin[0]).StartUp()

def BuildExtraStuff(pOptionsPane, pContentPane, ToAddTo, type, bGameEnded = 0):
    debug(__name__ + ", BuildExtraStuff")
    global dMenus, pConfigPanel
    if App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", "Master Switch"):
        for plugin in dMenus[type]:
            if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", plugin[1]):
                App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", plugin[1], 0)
                continue
            elif App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", plugin[1]):
                pModMenu = App.STCharacterMenu_Create(__import__(plugin[0]).GetName())
                ToAddTo.AddChild(pModMenu)
                pUI = __import__(plugin[0]).CreateMenu(pOptionsPane, pModMenu, bGameEnded)
                if pUI:
                    pModMenu.AddChild(pUI)
                    pModMenu.ForceUpdate(0)
                else:
                    ToAddTo.DeleteChild(pModMenu)

    return None

pConfigPanel = None
def BuildCustomizeTab(pOptionsPane, pContentPane, bGameEnded = 0):
    debug(__name__ + ", BuildCustomizeTab")
    global dMenus, pConfigPanel

    pOptionsPane.KillChildren()
    pOptionsPane.SetNotExclusive()

    LCARS = __import__(App.GraphicsModeInfo_GetCurrentMode().GetLcarsModule())

    pConfigPanel = App.STStylizedWindow_Create("StylizedWindow", "NoMinimize", "", 0.0, 0.0, App.STSubPane_Create(LCARS.MAIN_MENU_MIDDLE_CONTENT_WIDTH, LCARS.MAIN_MENU_MIDDLE_CONTENT_HEIGHT))
    pConfigPanel.SetFixedSize(LCARS.MAIN_MENU_MIDDLE_CONTENT_WIDTH * 0.48, LCARS.MAIN_MENU_MIDDLE_CONTENT_HEIGHT * 0.9)
    #pConfigPanel.SetFixedSize(LCARS.MAIN_MENU_MIDDLE_CONTENT_WIDTH * 0.46, LCARS.MAIN_MENU_MIDDLE_CONTENT_HEIGHT * 0.9)

    pConfigPanel.Resize(pConfigPanel.GetMaximumWidth(), pConfigPanel.GetMaximumHeight())
    
    pConfigPanel.SetUseScrolling(1)

    App.g_kConfigMapping.LoadConfigFile("options.cfg")

    if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", "Master Switch"):
        App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", "Master Switch", 0)

    # Time to load plugins. This mod will provide the "contentPane" (for the Javaliterate among us) on which the scripter can put things on.
    # This plugin also allows you to activate mods
    # So add a configuration panel for that
    pConfigMenu = App.STCharacterMenu_Create("Configurations")
    CreateConfigPanel(pConfigMenu)
    pConfigPanel.AddChild(pConfigMenu)
    
    # Start up menu...
    CreateControlMenu(dMenus["StartUp"], "Start Up", pConfigPanel, pOptionsPane, bGameEnded)
    #CreateControlMenu(dMenus["Config::Options"], "Customize", pOptionsPane, pOptionsPane, bGameEnded)
    if App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration","Master Switch"):
        for plugin in dMenus["Config::Options"]:
            if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", plugin[1]):
                App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", plugin[1], 0)
                continue
            elif App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", plugin[1]):
                #try:
                pModMenu = App.STCharacterMenu_Create(__import__(plugin[0]).GetName())
                pUI = __import__(plugin[0]).CreateMenu(pOptionsPane, pModMenu, bGameEnded)
                if pUI:
                    pModMenu.AddChild(pUI)
                    pModMenu.ForceUpdate(0)
                    pConfigPanel.AddChild(pModMenu)
                #except:
                #    print plugin[1], "failed to create menu"

    App.g_kConfigMapping.SaveConfigFile("options.cfg")
    pOptionsPane.AddChild(pConfigPanel, 0.0, 0.0, 0)

    pOptionsPane.SetFocus (pOptionsPane.GetFirstChild ())
    pOptionsPane.Layout ()

# Helper function for creating the config panel, in case we need to add this at other places as well.
ET_MASTERSWITCH = App.UtopiaModule_GetNextEventType()
def CreateConfigPanel(pConfigMenu):
    debug(__name__ + ", CreateConfigPanel")
    global ET_MASTERSWITCH
    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_MASTERSWITCH)
    pEvent.SetDestination(pConfigMenu)

    pMasterSwitch = App.STButton_Create("Master Switch", pEvent)

    pEvent.SetSource(pMasterSwitch)
    pEvent.SetString("Master Switch")

    pMasterSwitch.SetChoosable(1)
    pMasterSwitch.SetAutoChoose(1)
    pMasterSwitch.SetChosen(App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration","Master Switch"))
    pConfigMenu.AddChild(pMasterSwitch)

    pConfigMenu.AddPythonFuncHandlerForInstance(ET_MASTERSWITCH, __name__ + ".ToggleControl")

    # Insert seperator here?
    #   Depends if I can find one...
    #   Found in UIHelpers.CreateBracket
    #   Hmm... It doesn't appear to be visible...
    pSeperator = App.TGIcon_Create(App.GraphicsModeInfo_GetCurrentMode().GetLcarsString(), 200, App.g_kMainMenuBorderMainColor)
    pSeperator.Resize (pConfigMenu.GetClientArea().GetWidth()-0.02, 0.001, 0)

    pConfigMenu.AddChild(pSeperator)

    # The rest of the plugins...
    CreatePluginActiveMenu(dMenus["StartUp"], "Start Up Options", pConfigMenu)
    #CreatePluginActiveMenu(dMenus["Keyboard"],"Keyboard Options", pConfigMenu)
    pConfigurationsMenu = CreatePluginActiveMenu(dMenus["Config"], "Custom Options", pConfigMenu)

    # The next 4 in reverse order because we are prepending them to be above the "usual" options
    """pMenu = CreatePluginActiveMenu(dMenus["Config::NewGame"], "New Game", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pConfigurationsMenu.PrependChild(pMenu)

    pMenu = CreatePluginActiveMenu(dMenus["Config::LoadGame"], "Load Game", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pConfigurationsMenu.PrependChild(pMenu)

    pMenu = CreatePluginActiveMenu(dMenus["Config::Missions"], "Missions", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pConfigurationsMenu.PrependChild(pMenu)"""

    pMenu = CreatePluginActiveMenu(dMenus["Config::Options"], "Options", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pConfigurationsMenu.PrependChild(pMenu)

    pOptionsMenu = pMenu
    pMenu = CreatePluginActiveMenu(dMenus["Config::Options::Graphics"], "Graphics", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pOptionsMenu.PrependChild(pMenu)

    pMenu = CreatePluginActiveMenu(dMenus["Config::Options::Sound"], "Sound", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pOptionsMenu.PrependChild(pMenu)

    pMenu = CreatePluginActiveMenu(dMenus["Config::Options::General"], "General", pConfigMenu)
    pConfigMenu.RemoveChild(pMenu)
    pOptionsMenu.PrependChild(pMenu)

    pConfigurationsMenu.Layout()

    pConfigMenu.Layout()
    
def ToggleControl(pObject, pEvent):
    debug(__name__ + ", ToggleControl")
    App.g_kConfigMapping.LoadConfigFile("options.cfg")
    pButton = App.STButton_Cast(pEvent.GetSource())
    App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration",pEvent.GetCString(), pButton.IsChosen())
    App.g_kConfigMapping.SaveConfigFile("options.cfg")
    pObject.CallNextHandler(pEvent)

def CreatePluginActiveMenu(lList, name, pConfigMenu):
    debug(__name__ + ", CreatePluginActiveMenu")
    pMenu = App.STMenu_Create(name)
    global ET_MASTERSWITCH

    for plugin in lList:
        #print plugin
        if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", plugin[1]):
            App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", plugin[1], 0)
            App.g_kConfigMapping.SaveConfigFile("Options.cfg")

        pEvent = App.TGStringEvent_Create()
        pEvent.SetEventType(ET_MASTERSWITCH)
        pEvent.SetDestination(pConfigMenu)
        pEvent.SetString(plugin[1])
        pButton = App.STButton_Create(__import__(plugin[0]).GetName(), pEvent)
        pEvent.SetSource(pButton)
        pButton.SetChoosable(1)
        pButton.SetAutoChoose(1)
        pButton.SetChosen(App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration",plugin[1]))
        pMenu.AddChild(pButton)
    pMenu.Layout()
    pConfigMenu.AddChild(pMenu)
    return pMenu

def CreateControlMenu(lList, sName, pParentMenu, pOptionsPane, bGameEnded = 0):
    debug(__name__ + ", CreateControlMenu")
    if App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", "Master Switch"):
        pMenu = App.STMenu_Create(sName)
        for plugin in lList:
            if not App.g_kConfigMapping.HasValue("Unified MainMenu Mod Configuration", plugin[1]):
                App.g_kConfigMapping.SetIntValue("Unified MainMenu Mod Configuration", plugin[1], 0)
                continue
            elif App.g_kConfigMapping.GetIntValue("Unified MainMenu Mod Configuration", plugin[1]):
                #try:
                pModMenu = App.STCharacterMenu_Create(__import__(plugin[0]).GetName())
                pUI = __import__(plugin[0]).CreateMenu(pOptionsPane, pModMenu, bGameEnded)
                if pUI:
                    pModMenu.AddChild(pUI)
                    pModMenu.ForceUpdate(0)
                    pMenu.AddChild(pModMenu)
                    pModMenu.ResizeToContents()
                    pModMenu.Layout()
                #except:
                #    print plugin[1], "failed to create menu"
        pMenu.Layout()
        pMenu.ResizeToContents()
        pParentMenu.AddChild(pMenu)
        return pMenu
    return None

# Function based on Foundation which is based on the one of RedBeards in QBR
def LoadPlugins(dir, type):
    debug(__name__ + ", LoadPlugins")
    import nt
    import string
    list = nt.listdir(dir)
    list.sort()

    dotPrefix = string.join(string.split(dir, '\\')[1:], '.') + '.'

    global dMenus
    dMenus[type] = []

    lLoaded = ["__init__"]

    for plugin in list:
        s = string.split(plugin, '.')
        if len(s) <= 1:
            continue
        # Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
        extension = s[-1]
        fileName = string.join(s[:-1], '.')

        if (extension == 'pyc' or extension == 'py') and not fileName in lLoaded:
            lLoaded.append(fileName)
            pModule = __import__(dotPrefix + fileName)
            dMenus[type].append([dotPrefix + fileName, fileName])
