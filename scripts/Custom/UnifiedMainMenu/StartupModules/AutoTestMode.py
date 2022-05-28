# Auto Test Mode
# By MLeo Daalder
#
# Created as: example for my Unified Main Menu "mod"
#             and to have something for the "noobs" under us who can't seem to get into test mode...

import App

def GetName():
    return "Automatic Test Mode"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
    return None

def StartUp():
    App.UtopiaApp_GetApp().SetTestMenuState(2)