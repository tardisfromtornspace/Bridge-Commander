"""
I bet that you expected to see something more, but the problem is that when you exit BC there are some leftover handlers.
So we clean them before exiting with this small piece of code.

by USS Sovereign
"""

import App
from Custom.DS9FX.DS9FXLib import LogConsole
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

def FixMe():
    pTopWindow = App.TopWindow_GetTopWindow()
    pWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
    App.g_kEventManager.RemoveAllBroadcastHandlersForObject(pWindow)

    # Incase this is turned on, then we must do it manually
    reload (DS9FXSavedConfig)        
    if DS9FXSavedConfig.ExitGameDebugMode == 1:
        LogConsole.Output()
    
