# Force mission playing

import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib

def KillWormholeEntry():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    if not pSet.GetName() == "DeepSpace91":
        return
    pButton = GetEnterButton()
    if not pButton:
        return
    pButton.SetDisabled()

def AllowWormholeEntry():
    pPlayer = MissionLib.GetPlayer()
    pSet = pPlayer.GetContainingSet()
    if not pSet.GetName() == "DeepSpace91":
        return
    pButton = GetEnterButton()
    if not pButton:
        return
    pButton.SetEnabled()

def GetEnterButton():
    try:
        btnEnter = DS9FXMenuLib.GetSubMenuButton("Enter Wormhole", "Helm", "DS9FX", "Wormhole Options...")
        return btnEnter
    except:
        return None
