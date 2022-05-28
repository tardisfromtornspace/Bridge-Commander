from bcdebug import debug
# by Defiant <mail@defiant.homedns.org>

import App
import MissionLib
import Bridge.BridgeUtils
import Lib.LibEngineering
import QuickBattle.QuickBattle

MODINFO = { "Author": "\"Defiant\" mail@defiant.homedns.org",
            "License": "GPL",
            }

def EnemyFriendly(pObject, pEvent):
        debug(__name__ + ", EnemyFriendly")
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pFriendlies = pMission.GetFriendlyGroup()
        pEnemies = pMission.GetEnemyGroup()
	pPlayer	= MissionLib.GetPlayer()
	pTarget	= pPlayer.GetTarget()

	if not pTarget:
		print("No target")
		return

	if (pEvent.GetInt() == 0):
		if pEnemies.IsNameInGroup(pTarget.GetName()):
			pEnemies.RemoveName(pTarget.GetName())
		pFriendlies.AddName(pTarget.GetName())
		if not pEnemies.GetNameTuple():
			pEnemies.AddName("nothing")
		SetAI(pTarget, "Friendly")	
	elif (pEvent.GetInt() == 1):
		if pFriendlies.IsNameInGroup(pTarget.GetName()):
			pFriendlies.RemoveName(pTarget.GetName())
		pEnemies.AddName(pTarget.GetName())
		SetAI(pTarget, "Enemy")
	else:
		print("Unknown request")


def SetAI(pShip, Side="Friendly"):
	debug(__name__ + ", SetAI")
	g_pAIShip = App.ShipClass_Cast(pShip)

        if (Side == "Enemy"):
                if (g_pAIShip.GetShipProperty().IsStationary() == 1):
                        g_pAIShip.SetAI(Lib.LibEngineering.CreateStarbaseEnemyAI(g_pAIShip))
                else:
                        g_pAIShip.SetAI(Lib.LibEngineering.CreateEnemyAI(g_pAIShip))
        else:
                if (g_pAIShip.GetShipProperty().IsStationary() == 1):
                        g_pAIShip.SetAI(Lib.LibEngineering.CreateStarbaseFriendlyAI(g_pAIShip))
                else:
                        g_pAIShip.SetAI(Lib.LibEngineering.CreateFriendlyAI(g_pAIShip))


def init():
    debug(__name__ + ", init")
    
    if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
	    return
    
    pBridge = App.g_kSetManager.GetSet('bridge')
    g_pSaffi = App.CharacterClass_GetObject(pBridge, "XO") 
    pSaffiMenu = Bridge.BridgeUtils.GetBridgeMenu("XO") 
    pMasterButtonSite = App.STMenu_CreateW(App.TGString("Switch Side"))
    pSaffiMenu.PrependChild(pMasterButtonSite)

    ENEMY_FRIENDLY = Lib.LibEngineering.GetEngineeringNextEventType()
    g_pSaffi.AddPythonFuncHandlerForInstance(ENEMY_FRIENDLY, __name__ + ".EnemyFriendly")
    pButtonEtF = QuickBattle.QuickBattle.CreateBridgeMenuButton(App.TGString('To Friendly'), ENEMY_FRIENDLY, 0, g_pSaffi)
    pButtonFtE = QuickBattle.QuickBattle.CreateBridgeMenuButton(App.TGString('To Enemy'), ENEMY_FRIENDLY, 1, g_pSaffi)
    pMasterButtonSite.PrependChild(pButtonEtF)
    pMasterButtonSite.PrependChild(pButtonFtE)
