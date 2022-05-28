# DS9FXMenuLib

# Designed by USS Sovereign & Wowbagger

# Imports
import App
import Foundation
import MainMenu.mainmenu
import MissionLib

# Timer lists
pTimers = []

# Functions
def GetButton(sButtonName, sMenuName):
        pMenu   = GetBridgeMenu(sMenuName)
        pButton = pMenu.GetButton(sButtonName)
        if not pButton:
                return None
        
        return pButton

def GetMenuButton(sButtonName, sMenuName, sSubMenuName):
        pMenu   = GetBridgeMenu(sMenuName)
        if not pMenu:
                return None
        pSubMenu = pMenu.GetSubmenu(sSubMenuName)
        if not pSubMenu:
                return None
        pButton = pSubMenu.GetButton(sButtonName)
        if not pButton:
                return None   
        
        return pButton
        
def GetSubMenuButton(sButtonName, sMenuName, sSubMenuName, sSubSubMenuName):
        pMenu   = GetBridgeMenu(sMenuName)
        if not pMenu:
                return None
        pSubMenu = pMenu.GetSubmenu(sSubMenuName)
        if not pSubMenu:
                return None
        pSubSubMenu = pSubMenu.GetSubmenu(sSubSubMenuName)
        if not pSubSubMenu:
                return None
        pButton = pSubSubMenu.GetButton(sButtonName)
        if not pButton:
                return None
        
        return pButton

def CreateBridgeMenuButton(sButtonName, sMenuName, sFunction, mToButton = None, iEventInt = 0):        
        pMenu = GetBridgeMenu(sMenuName)

        ET_EVENT = App.UtopiaModule_GetNextEventType()

        pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, sFunction)

        pEvent = App.TGIntEvent_Create()
        pEvent.SetEventType(ET_EVENT)
        pEvent.SetDestination(pMenu)
        pEvent.SetInt(iEventInt)
        pButton = App.STButton_CreateW(App.TGString(sButtonName), pEvent)

        if not mToButton:
                pMenu.PrependChild(pButton)
        else:
                mToButton.PrependChild(pButton)
                
        return pButton

def DeleteButton(sButtonName, sMenuName, sSubMenuName = None, sSubSubMenuName = None):
        pMenu = GetBridgeMenu(sMenuName)
        pButton = GetButton(sButtonName, sMenuName)
        if sSubMenuName:
                pButton = GetMenuButton(sButtonName, sMenuName, sSubMenuName)
        if sSubSubMenuName:
                pButton = GetSubMenuButton(sButtonName, sMenuName, sSubMenuName, sSubSubMenuName)
        if pButton:
                pMenu.DeleteChild(pButton)

def CreateSliderbar (pName, eType, fValue = 0.0, fRangeMin = 0.0, fRangeMax = 1.0, fKeyInterval = 0.01, fMarkerValue = 1.0, fWidth = 0.25, fHeight = 0.04):
        pTopWindow = App.TopWindow_GetTopWindow()
        pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

        pBar = App.STNumericBar_Create()

        pBar.SetRange(fRangeMin, fRangeMax)
        pBar.SetKeyInterval(fKeyInterval)
        pBar.SetMarkerValue(fMarkerValue)
        pBar.SetValue(fValue)
        pBar.SetUseMarker(0)
        pBar.SetUseAlternateColor(0)
        pBar.SetUseButtons(0)

        kNormalColor = App.TGColorA() 
        kNormalColor.SetRGBA(0.4, 0.4, 0.8, 1.0)
        kEmptyColor = App.TGColorA() 
        kEmptyColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

        pBar.SetNormalColor(kNormalColor)
        pBar.SetEmptyColor(kEmptyColor)
        pText = pBar.GetText()
        pText.SetStringW(pName)

        pBar.Resize (fWidth, fHeight, 0)

        pEvent = App.TGFloatEvent_Create ()
        pEvent.SetDestination(pOptionsWindow)
        pEvent.SetFloat (fValue)
        pEvent.SetEventType(eType)

        pBar.SetUpdateEvent(pEvent)

        return pBar        

def CreateMenu(sNewMenuName, sBridgeMenuName, iAdditional = 0, iPosition = 0):
        pMenu = GetBridgeMenu(sBridgeMenuName)
        pNewMenu = App.STMenu_CreateW(App.TGString(sNewMenuName))

        if iAdditional == 1:
                pMenu.AddChild(pNewMenu)
        elif iAdditional == 2:
                pMenu.InsertChild(iPosition, pNewMenu)
        else:
                pMenu.PrependChild(pNewMenu)

        return pNewMenu

def CreateSubMenu(pToAdd, sSubMenu, iAdditional = 0, iPosition = 0):
        pMenu = App.STMenu_CreateW(App.TGString(sSubMenu))
        
        if iAdditional == 1:
                pToAdd.AddChild(pMenu)
        elif iAdditional == 2:
                pToAdd.InsertChild(iPosition, pMenu)
        else:
                pToAdd.PrependChild(pMenu)

        return pMenu

def CreateEngineerMenu(sNewMenuName, sBridgeMenuName):
        pMenu = GetBridgeMenu(sBridgeMenuName)
        pDropDownMenu = App.STMenu_CreateW(App.TGString(sNewMenuName))
        pMenu.AddChild(pDropDownMenu)

        pLowest = FindLowestChild(pMenu)
        pDropDownMenu.SetPosition(pLowest.GetLeft(), pLowest.GetBottom(), 0)

        pMenu.AddChild(None)

        return pDropDownMenu

def FindLowestChild(pPane):
        iIndex = pPane.GetTrueNumChildren() - 1
        iBottom = 0
        iLowestChild = None
        iCurrent = None
        while iIndex >= 0:
                iCurrent = pPane.GetTrueNthChild(iIndex)
                iCurrentBottom = iCurrent.GetBottom()
                if(iCurrentBottom > iBottom):
                        iBottom = iCurrentBottom
                        iLowestChild = iCurrent
                iIndex = iIndex - 1

        return iLowestChild

def GetBridgeMenu(sMenuName):
        pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
        if(pDatabase is None):
                return
        App.g_kLocalizationManager.Unload(pDatabase)

        return pTactCtrlWindow.FindMenu(pDatabase.GetString(sMenuName))

def GetNextEventType():
        return App.UtopiaModule_GetNextEventType()

def CreateTimer(eEvent, sFunctionHandler, fStart):
        pGame = App.Game_GetCurrentGame()
        if (pGame == None):
                return None
        pEpisode = pGame.GetCurrentEpisode()
        if (pEpisode == None):
                return None
        pMission = pEpisode.GetCurrentMission()
        if (pMission == None):
                return None

        pMission.AddPythonFuncHandlerForInstance(eEvent, sFunctionHandler)

        pEvent = App.TGEvent_Create()
        pEvent.SetEventType(eEvent)
        pEvent.SetDestination(pMission)
        pTimer = App.TGTimer_Create()
        pTimer.SetTimerStart(fStart)
        pTimer.SetDelay(0)
        pTimer.SetDuration(0)
        pTimer.SetEvent(pEvent)

        App.g_kTimerManager.AddTimer(pTimer)

        global pTimers
        pTimers.append(pTimer.GetObjID())

        return pTimer

def DeleteAllTimers():
        global pTimers
        for idTimer in pTimers:
                App.g_kTimerManager.DeleteTimer(idTimer)
                App.g_kRealtimeTimerManager.DeleteTimer(idTimer)
        pTimers = []

def DeleteTimer(pTimer):
        try:
                App.g_kTimerManager.DeleteTimer(pTimer.GetObjID())
                App.g_kRealtimeTimerManager.DeleteTimer(pTimer.GetObjID())
        except AttributeError:
                pass

def AddKeyBind(sKeyName, sFunction, iEventInt = 0, sGroup = "General", eType = App.KeyboardBinding.GET_INT_EVENT):
        if not hasattr(Foundation, "g_kKeyBucket"):
                return
        import Custom.Autoload.zzz_DS9FX
        mode = Custom.Autoload.zzz_DS9FX.mode
        pMission = MissionLib.GetMission()
        ET_KEY_EVENT = GetNextEventType()
        App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_KEY_EVENT, pMission, sFunction)
        Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig(sKeyName, sKeyName, ET_KEY_EVENT, eType, iEventInt, sGroup, dict = {"modes": [mode]}))

def CheckActiveMutator(sMutatorName):
        Foundation.LoadConfig()
        for i in Foundation.mutatorList._arrayList:
                fdtnMode = Foundation.mutatorList._keyList[i]
                if fdtnMode.IsEnabled() and (fdtnMode.name == sMutatorName):
                        return 1
        return 0

def CheckModInstallation(sInput):
        if sInput is None:
                return 0

        sInput = str(sInput)

        Foundation.LoadConfig()
        for i in Foundation.mutatorList._arrayList:
                fdtnMode = Foundation.mutatorList._keyList[i]
                if fdtnMode.IsEnabled() and SeekPartially(fdtnMode.name, sInput):
                        return 1

        return 0

def SeekPartially(sMutator, sToProbe):
        if sMutator == None or sToProbe == None:
                return 0

        sMutator = str(sMutator)
        sToProbe = str(sToProbe)

        import string

        sMutator = string.lower(sMutator)
        sToProbe = string.lower(sToProbe)

        lToProbe = []
        for strToProbe in string.split(sToProbe):
                lToProbe.append(strToProbe)

        iWords = len(lToProbe)

        lMutator = []
        for strMutator in string.split(sMutator):
                lMutator.append(strMutator)

        iMatches = 0

        for s in lToProbe:
                try:
                        lMutator.remove(s)
                        iMatches = iMatches + 1
                except:
                        pass

        if iWords == iMatches:
                return 1

        return 0

def ColorizeButton(pButton, kNormR=0.8, kNormG=0.6, kNormB=0.8, kNormA=1.0, kHighR=0.92, kHighG=0.76, kHighB=0.92, kHighA=1.0, kDisR=0.25, kDisB=0.25, kDisG=0.25, kDisA=1.0):
        kNorm = App.TGColorA()
        kHigh = App.TGColorA()
        kDis = App.TGColorA()
        kNorm.SetRGBA(kNormR, kNormG, kNormB, kNormA)
        kHigh.SetRGBA(kHighR, kHighG, kHighB, kHighA)
        kDis.SetRGBA(kDisR, kDisG, kDisB, kDisA)
        pButton.SetUseUIHeight(0)
        pButton.SetNormalColor(kNorm)
        pButton.SetHighlightedColor(kHigh)
        pButton.SetSelectedColor(kNorm)
        pButton.SetDisabledColor(kDis)
        pButton.SetColorBasedOnFlags()

        return pButton