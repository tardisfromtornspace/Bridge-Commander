# Setup function - does whatever needed to be in LoadBridge.py
# This shouldn't need anything more...
import App
import Bridge.BridgeUtils

def GetBridgeMenu(Person):
        pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        pMenu = pTacticalControlWindow.FindMenu(pDatabase.GetString(Person))
        App.g_kLocalizationManager.Unload(pDatabase)
        return pMenu

def LoadGroupMenu():
        global g_RunOnce, g_SpecialMenu

        try:
            if (g_RunOnce == 1):
                return
            else:
                g_RunOnce = 1
        except:
            g_RunOnce = 1
    
  	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet('bridge') 
	#BridgeType = App.BridgeSet_Cast(pBridge).GetConfig() 
	g_pFelix = App.CharacterClass_GetObject(pBridge, "Tactical") 
	pTacticalMenu = GetBridgeMenu("Tactical") 
	pDatabaseBlank = App.g_kLocalizationManager.Load("data/TGL/TechnologyExpansion.tgl")
	pSpecialName = pDatabaseBlank.GetString("CloakedFiring")
	pSpecialName.SetString("Technologies")
	g_SpecialMenu = App.STCharacterMenu_CreateW(pSpecialName)
	pTacticalMenu.AddChild(g_SpecialMenu)
