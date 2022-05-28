# by Defiant <mail@defiant.homedns.org>

import App
import MissionLib
import Lib.LibEngineering
pButton = None

MODINFO = {     "Author": "\"Defiant\" mail@defiant.homedns.org",
                "License": "GPL",
                "needBridge": 0
            }


def PhaserSet(pObject, pEvent):
    global pButton
    
    pPlayer = MissionLib.GetPlayer()
    PhaserSystem = pPlayer.GetPhaserSystem()
    
    if not PhaserSystem:
        return
        
    if PhaserSystem.IsSingleFire():
        PhaserSystem.GetProperty().SetSingleFire(0)
    else:
        PhaserSystem.GetProperty().SetSingleFire(1)
    
    if not pButton:
            pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
            pButton = Lib.LibEngineering.GetButton("Single Phaser: " + "0", pMenu)
    if not pButton:
            pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
            pButton = Lib.LibEngineering.GetButton("Single Phaser: " + "1", pMenu)
    pButton.SetName(App.TGString("Single Phaser: " + str(PhaserSystem.IsSingleFire())))


def init():
        global pButton
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer or App.g_kUtopiaModule.IsMultiplayer():
                return
        PhaserSystem = pPlayer.GetPhaserSystem()
        if PhaserSystem:
                if not pButton:
                        pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
                        pButton = Lib.LibEngineering.GetButton("Single Phaser: " + "0", pMenu)
                if not pButton:
                        pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
                        pButton = Lib.LibEngineering.GetButton("Single Phaser: " + "1", pMenu)
                pButton = Lib.LibEngineering.CreateMenuButton("Single Phaser: " + str(PhaserSystem.IsSingleFire()), "Tactical", __name__ + ".PhaserSet")


def Restart():
	global pButton
        
        if App.g_kUtopiaModule.IsMultiplayer():
                return
        
	pPlayer = MissionLib.GetPlayer()
	PhaserSystem = pPlayer.GetPhaserSystem()
	if not pButton:
		pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
		pButton = Lib.LibEngineering.GetButton("Single Phaser: " + "0", pMenu)
	if not pButton:
		pMenu = Lib.LibEngineering.GetBridgeMenu("Tactical")
		pButton = Lib.LibEngineering.GetButton("Single Phaser: " + "1", pMenu)
	if PhaserSystem:
		if pButton:
			pButton.SetName(App.TGString("Single Phaser: " + str(PhaserSystem.IsSingleFire())))
		else:
			pButton = Lib.LibEngineering.CreateMenuButton("Single Phaser: " + str(PhaserSystem.IsSingleFire()), "Tactical", __name__ + ".PhaserSet")
