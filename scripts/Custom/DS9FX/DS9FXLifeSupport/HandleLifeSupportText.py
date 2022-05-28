# This script will show current crew stats

# by Sov

# Imports
import App
import MissionLib
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict, AIBoarding, CaptureShip
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Vars
pCrewLabel = None
Timer = None
bTimerOverflow = 0

# Functions
def CreateLabel():
    global pCrewLabel

    if pCrewLabel:
        return 0

    pCrewLabel = DS9FXLifeSupportLib.CreateCrewLabels()

def RemoveLabel():
    global pCrewLabel

    if not pCrewLabel:
        return 0

    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    if not pTCW:
        return 0

    if not pCrewLabel == None:
        try:
            App.g_kFocusManager.RemoveAllObjectsUnder(pCrewLabel["Label"])
            pTCW.DeleteChild(pCrewLabel["Label"])
            pCrewLabel = None
        except:
            pass

def StartUpTimingProcess():
    global Timer, bTimerOverflow

    if not bTimerOverflow:
        Timer = LifeSupportTextTimer()
    else:
        return

class LifeSupportTextTimer:
    def __init__(self):
        global bTimerOverflow
        bTimerOverflow = 1
        self.pTimer = None
        self.__countdown__()

    def __countdown__(self):
        if not self.pTimer:
            self.pTimer = App.PythonMethodProcess()
            self.pTimer.SetInstance(self)
            self.pTimer.SetFunction("__update__text__")
            self.pTimer.SetDelay(0.01)
            self.pTimer.SetPriority(App.TimeSliceProcess.LOW)

    def __update__text__(self, fTime):
        global pCrewLabel

        if not pCrewLabel:
            return 0

        reload(DS9FXSavedConfig)
        if not DS9FXSavedConfig.LifeSupport == 1 and not DS9FXSavedConfig.LifeSupportCrewLabels == 1:
            return 0

        try:
            pPlayer = MissionLib.GetPlayer()
            pPlayerID = pPlayer.GetObjID()
            if LifeSupport_dict.dCrew.has_key(pPlayerID):
                pPlayerText = LifeSupport_dict.dCrew[pPlayerID]
            else:
                pPlayerText = "N/A"
            iAttackers = 0
            iDefenders = 0
            if CaptureShip.captureships.has_key(pPlayerID):
                lInfo = CaptureShip.captureships[pPlayerID]
                iDefenders = lInfo[1]
                iAttackers = lInfo[0]
            if AIBoarding.dCombat.has_key(pPlayerID):
                dData = AIBoarding.dCombat[pPlayerID]
                iDefenders = iDefenders + dData["Defender"]
                iAttackers = iAttackers + dData["Attacker"]
            if iAttackers <= 0 or iDefenders <= 0 or pPlayerText == "N/A":
                pass
            else:
                pPlayerText = str(pPlayerText) + " " + "(" + str(iDefenders) + "/" + str(iAttackers) + ")"
        except:
            pPlayerText = "N/A"

        try:
            pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
            pTargetID = pTarget.GetObjID()
            if LifeSupport_dict.dCrew.has_key(pTargetID):
                pTargetText = LifeSupport_dict.dCrew[pTargetID]
            else:
                pTargetText = "N/A"
            iAttackers = 0
            iDefenders = 0                
            if CaptureShip.captureships.has_key(pTargetID):
                lInfo = CaptureShip.captureships[pTargetID]
                iDefenders = lInfo[1]
                iAttackers = lInfo[0]
            if AIBoarding.dCombat.has_key(pTargetID):
                dData = AIBoarding.dCombat[pTargetID]
                iDefenders = iDefenders + dData["Defender"]
                iAttackers = iAttackers + dData["Attacker"]
            if iAttackers <= 0 or iDefenders <= 0 or pTargetText == "N/A":
                pass
            else:
                pTargetText = str(pTargetText) + " " + "(" + str(iDefenders) + "/" + str(iAttackers) + ")"                
        except:
            pTargetText = "N/A"

        pText = "Player Crew: " + str(pPlayerText) + "\n" + "Target Crew: " + str(pTargetText)
        try:
            pCrewLabel["Text"].SetString(str(pText))
            pCrewLabel["Text"].Layout()
        except:
            pass
        try:
            pCrewLabel["Label"].Resize(pCrewLabel["Text"].GetWidth() + pCrewLabel["Text"].GetWidth() / 8.0, pCrewLabel["Text"].GetHeight() + pCrewLabel["Text"].GetHeight() / 8.0)
        except:
            pass
        try:
            pCrewLabel["Background"].Resize(pCrewLabel["Label"].GetWidth(), pCrewLabel["Label"].GetHeight())
        except:
            pass

        pTop = App.TopWindow_GetTopWindow()
        if not pTop:
            return 0

        if pTop.IsBridgeVisible():
            pTacticalWindow = App.TacticalControlWindow_GetTacticalControlWindow()
            if not pTacticalWindow:
                pCrewLabel["Label"].SetNotVisible()
                return 0

            pTacticalMenu = pTacticalWindow.GetTacticalMenu()
            if not pTacticalMenu:
                pCrewLabel["Label"].SetNotVisible()
                return 0

            if pTacticalMenu.IsVisible():
                pCrewLabel["Label"].SetVisible()
            else:
                pCrewLabel["Label"].SetNotVisible()
        elif pTop.IsTacticalVisible():
            pCrewLabel["Label"].SetVisible()
        else:
            pCrewLabel["Label"].SetNotVisible()
