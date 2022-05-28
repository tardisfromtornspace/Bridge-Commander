# Determines if you will experience the Mirror Universe surprise or not

# by Sov

import App
import MissionLib
import DS9FXPrintTextLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

bShowMessage = 0
bInMission = 0
bGoBack = 0
bFedSide = 0
bDomSide = 0
bRestore = 0

lShips =  ["Bugship 1", "Bugship 2", "Bugship 3", "Deep_Space_9", "USS Excalibur", "USS Defiant", "USS Oregon", "USS_Lakota", "Verde", "Guadiana", "Lankin", "Maroni", "Kuban", "Paraguay", "Tigris"]
lSets = ["DeepSpace91", "GammaQuadrant1"]

def MissionStart():
        global bShowMessage, bInMission, bGoBack, bFedSide, bDomSide, bRestore
        bShowMessage = 0
        bInMission = 0
        bGoBack = 0
        bFedSide = 0
        bDomSide = 0
        bRestore = 0

def InMission(bState):
        global bInMission
        bInMission = bState

def MirrorUniverse():
        global bShowMessage, bInMission, bGoBack, bDomSide, bFedSide, bRestore

        if bGoBack:
                bShowMessage = 0

                if bInMission:
                        return

                reload(DS9FXSavedConfig)
                if not DS9FXSavedConfig.EasterEggs == 1:
                        return

                from Custom.UnifiedMainMenu.ConfigModules.Options import DS9FXConfig
                DS9FXConfig.SetMirrorUniverse(bFedSide, bDomSide)   
                
                for s in lSets:
                        try:
                                App.g_kSetManager.DeleteSet(s)
                        except:
                                pass
                
                for s in lShips:
                        try:
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pFriend = pMission.GetFriendlyGroup()
                                pEnemy = pMission.GetEnemyGroup()
                                if pFriend.IsNameInGroup(s):
                                        pFriend.RemoveName(s)
                                if pEnemy.IsNameInGroup(s):
                                        pEnemy.RemoveName(s)                                        
                        except:
                                pass                        

        else:
                bShowMessage = 0

                if bInMission:
                        return

                reload(DS9FXSavedConfig)
                if not DS9FXSavedConfig.EasterEggs == 1:
                        return

                pChance = GetRnd(9999, 1)
                if pChance > 500:
                        return

                bShowMessage = 1
                bRestore = 1
                bDomSide = DS9FXSavedConfig.DominionSide
                bFedSide = DS9FXSavedConfig.FederationSide

                from Custom.UnifiedMainMenu.ConfigModules.Options import DS9FXConfig
                DS9FXConfig.SetMirrorUniverse(0, 0)
                
                for s in lSets:
                        try:
                                App.g_kSetManager.DeleteSet(s)
                        except:
                                pass
                
                for s in lShips:
                        try:
                                pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
                                pFriend = pMission.GetFriendlyGroup()
                                pEnemy = pMission.GetEnemyGroup()
                                if pFriend.IsNameInGroup(s):
                                        pFriend.RemoveName(s)
                                if pEnemy.IsNameInGroup(s):
                                        pEnemy.RemoveName(s)                                        
                        except:
                                pass                        
                

def TriggerSurprise():
        global bShowMessage, bInMission, bGoBack

        if bGoBack:
                if bInMission:
                        return

                PrintAllIsNormal()

                bGoBack = 0 

        else:
                if bInMission:
                        return

                if not bShowMessage:
                        return

                DisableButtons()

                PrintTheSurprise()

                bGoBack = 1

def DisableButtons():
        global bShowMessage, bInMission

        reload(DS9FXSavedConfig)
        if not DS9FXSavedConfig.EasterEggs == 1:
                return    
        
        if bInMission:
                return
        
        if not bShowMessage:
                return

        pSequence = App.TGSequence_Create()
        pAction = App.TGScriptAction_Create(__name__, "DisableButtonsDelay")
        pSequence.AddAction(pAction, None, 5)
        pSequence.Play()   

def DisableButtonsDelay(pAction):
        from Custom.DS9FX import DS9FXmain

        try:
                DS9FXmain.bDockToDS9.SetDisabled()
                DS9FXmain.bCloseChannel.SetDisabled()
                DS9FXmain.bHail.SetDisabled()
                DS9FXmain.bMissionStats.SetDisabled()
        except:
                pass

        return 0

def PrintTheSurprise():
        sText = "I don't think we're in Kansas anymore sir... This might be the Mirror Universe.\nYour orders sir?!"
        iPos = 6
        iFont = 12
        iDur = 12
        iDelay = 10
        DS9FXPrintTextLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def PrintAllIsNormal():
        sText = "We seem to be back to our Universe sir. I feel much better already..."
        iPos = 6
        iFont = 12
        iDur = 12
        iDelay = 10
        DS9FXPrintTextLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def RestoreProperSettings():
        global bDomSide, bFedSide, bRestore

        if not bRestore:
                return

        from Custom.UnifiedMainMenu.ConfigModules.Options import DS9FXConfig
        DS9FXConfig.SetMirrorUniverse(bFedSide, bDomSide)

def GetRnd(iRnd, iStatic):
        return App.g_kSystemWrapper.GetRandomNumber(iRnd) + iStatic 