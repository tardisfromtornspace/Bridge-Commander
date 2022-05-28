# Fix for exit mission related errors

# by Sov

from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def FixExiting():
    reload(DS9FXSavedConfig)
    if not DS9FXSavedConfig.ExitGameFix == 1:
        return
    
    try:
        import MainMenu.mainmenu
	MainMenu.mainmenu.BuildInterface()
	MainMenu.mainmenu.SwitchMiddlePane("New Game")
	MainMenu.mainmenu.HandleSwitchIconGroups(None, None)        
        print "DS9FX: Fixing Exit Game releated errors, switching to New Game pane..."
    except:
        pass
    