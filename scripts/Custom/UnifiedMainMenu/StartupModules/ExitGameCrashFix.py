"""
This small piece of code fixes most of the crashes which occur when you Exit BC

by USS Sovereign
"""

import App
from Custom.DS9FX.DS9FXLib import GameCrashFix

def GetName():    
    return "DS9FX: Game Crash Fix"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    return None

def StartUp():
    pWindow = App.TopWindow_GetTopWindow().FindMainWindow(App.MWT_OPTIONS)
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXIT_PROGRAM, pWindow, __name__ + ".RedirectMe")
    print 'DS9FX: Game Crash Fix Active...'

def RedirectMe(pObject, pEvent):
    GameCrashFix.FixMe()
    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

