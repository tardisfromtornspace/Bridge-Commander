# Atacks an enemy with an away team - Smbw

# Thank you USS Sovereign for your help!


# To-do:
# - adapt the fight calculations to the difficulty of the target
# + add speech if the target's shields are up


# Imports
import App
import MissionLib
from Custom.DS9FX.DS9FXAILib import DS9FXGenericStaticFriendlyFollowAI, DS9FXGenericStaticStarbaseFriendlyAI
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXLifeSupport import LifeSupport_dict
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents


# Events
ET_CLOSE = App.UtopiaModule_GetNextEventType()
ET_RECALL = App.UtopiaModule_GetNextEventType()
ET_CAPTURE = App.UtopiaModule_GetNextEventType()
ET_UPDATE = App.UtopiaModule_GetNextEventType()


# Vars
pPane = None
pMainPane = None
pSlider = None
sRecallInfoText = "N/A"
pRecallInfoText = None
sTransferInfoText = "N/A"
pTransferInfoText = None
fPercentage = 0
recallcrew = 0
secdelay = 0

captureships = {}


# Functions
def TakeroverEnemy():
    global pPane, fPercentage, pMainPane, pSlider, captureships, secdelay, sRecallInfoText, pRecallInfoText, sTransferInfoText, pTransferInfoText

    transportstat = 0
    recallstat = 0
    recallcrew = 0
    shipcaptureinfo = None
    retcrew = "N/A"
    remcrew = "N/A"
    awayteam = "N/A"
    pllooses = "N/A"
    enlooses = "N/A"
    transport = "Crew to Transport: 0"
    
    if secdelay != 0: # to prevent a bug - too many capture comands in a short time lead to misscaculations (overflow)
        return 0

    if not pPane == None:
        KillGUI(None, None)
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0
    
    if pPlayer.IsCloaked() or pTarget.IsCloaked():
        return 0

    if not Distance(pTarget) < 300:
        return 0

    pEnemy = MissionLib.GetEnemyGroup()
    if not pEnemy:
        return 0
    
    TargetName = pTarget.GetName()
    if not TargetName:
        return 0
    
    if not pEnemy.IsNameInGroup(TargetName):
        return 0

    pPlayerID = pPlayer.GetObjID()
    if not pPlayerID:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pPlayerID) or not LifeSupport_dict.dCrew.has_key(pTargetID):
        return 0

    crewinfolist = crewinfo()
    fPlayerMaxCrew = crewinfolist[0]
    fPlayerCurrCrew = crewinfolist[1]
    PlayerCurTacticalCrew = crewinfolist[2]
    fTargetMaxCrew = crewinfolist[3]
    fTargetCurrCrew = crewinfolist[4]
    TargetCurTacticalCrew = crewinfolist[5]

    if not captureships.has_key(pTargetID) and PlayerCurTacticalCrew <= 0:
        transportstat = 0

    if PlayerCurTacticalCrew > 0:
        transportstat = 1
    
    preplcrew = fPlayerCurrCrew

    if captureships.has_key(pTargetID):
        shipcaptureinfo = captureships[pTargetID]
        
        if shipcaptureinfo[0] <= 0 or shipcaptureinfo[1] <= 0:
            del captureships[pTargetID]
            shipcaptureinfo = None

        else:
            fTargetCurrCrew = shipcaptureinfo[1]
            preplcrew = fTargetCurrCrew
            TargetCurTacticalCrew = int(fTargetCurrCrew - (fTargetMaxCrew / 2.0))
            if TargetCurTacticalCrew < 1:
                TargetCurTacticalCrew = 0
            awayteam = shipcaptureinfo[0]
            pllooses = int(shipcaptureinfo[5] - shipcaptureinfo[0])
            if pllooses < 0:
                pllooses = 0
            enlooses = int(shipcaptureinfo[6] - shipcaptureinfo[1])
            if enlooses < 0:
                enlooses = 0
            retcrew = 0
            remcrew = awayteam
            transport = "Reinforcemments: 0"
            recallstat = 1

            if PlayerCurTacticalCrew > 0:
                transportstat = 2

    if not ShieldCheck(pTargetID) == 1:
        return 0

    fPercentage = 0.0
    
    App.g_kUtopiaModule.Pause(1)

    # Sov fix starts here
    pPane = App.TGPane_Create(1.0, 1.0)
    pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
    pTCW.AddChild(pPane, 0, 0)
    pMainPane = App.TGPane_Create(0.6, 0.7)
    pPane.AddChild(pMainPane, 0.33, 0.04)
    
    pGame = App.Game_GetCurrentGame()
    pEpisode = pGame.GetCurrentEpisode()
    pMission = pEpisode.GetCurrentMission()
    
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_RECALL, pMission, __name__ + ".Recall")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_CAPTURE, pMission, __name__ + ".Capture")
    App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_UPDATE, pMission, __name__ + ".UpdateSlider")

    kColor = App.TGColorA() 
    kColor.SetRGBA(1, 0.81, 0.41, 1.0)

    pMainWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Capture Management"), 0.0, 0.0, None, 1, 0.6, 0.7, kColor)
    pMainPane.AddChild(pMainWindow, 0.0, 0.0)
    pMainPane.MoveToFront(pMainWindow)

    pCaptureWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Capture Target"), 0.0, 0.0, None, 1, 0.19, 0.3, kColor)
    pMainPane.AddChild(pCaptureWindow, 0.03, 0.31)
    if transportstat > 0:
        pMainPane.MoveToFront(pCaptureWindow)
    
    pPlayerInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Player Details:"), 0.0, 0.0, None, 1, 0.16, 0.18, kColor)
    pMainPane.AddChild(pPlayerInfoWindow, 0.03, 0.04)
    pMainPane.MoveToFront(pPlayerInfoWindow)

    pTargetInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Target Details:"), 0.0, 0.0, None, 1, 0.16, 0.18, kColor)
    pMainPane.AddChild(pTargetInfoWindow, 0.38, 0.04)
    pMainPane.MoveToFront(pTargetInfoWindow)
    
    pRecallWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Recall"), 0.0, 0.0, None, 1, 0.19, 0.3, kColor)
    pMainPane.AddChild(pRecallWindow, 0.38, 0.31)
    if recallstat == 1:
        pMainPane.MoveToFront(pRecallWindow)

    pRecallInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Recall Info"), 0.0, 0.0, None, 1, 0.16, 0.14, kColor)
    pMainPane.AddChild(pRecallInfoWindow, 0.39, 0.35)
    if recallstat == 1:
        pMainPane.MoveToFront(pRecallInfoWindow)

    pTransferInfoWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NoMinimize", App.TGString("Transfer Info"), 0.0, 0.0, None, 1, 0.16, 0.14, kColor)
    pMainPane.AddChild(pTransferInfoWindow, 0.04, 0.35)
    if transportstat > 0:
        pMainPane.MoveToFront(pTransferInfoWindow)

    pSlider = DS9FXMenuLib.CreateSliderbar(App.TGString("Crew Selection"), ET_UPDATE, float(fPercentage), 0.0, 1.0, 0.01, 1.0, 0.42, 0.04)
    if transportstat == 0 and recallstat == 0: # I guess this never happens...
        pSlider.SetDisabled()
    pMainWindow.AddChild(pSlider, 0.06, 0.22)
    pMainWindow.MoveToFront(pSlider)

    sPlayerText = "Current Crew: " + str(fPlayerCurrCrew) + "\n" + "Security Officers: " + str(PlayerCurTacticalCrew) + "\n" + "Awayteam Members: " + str(awayteam) + "\n" + "Awayteam Looses: " + str(pllooses)
    pPlayerText = App.TGParagraph_CreateW(App.TGString(str(sPlayerText)), pPlayerInfoWindow.GetMaximumInteriorWidth(), None, '', pPlayerInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pPlayerInfoWindow.AddChild(pPlayerText, 0, 0.01)

    sTargetText = "Operational Max Crew: " + str(fTargetMaxCrew) + "\n" + "Current Crew: " + str(fTargetCurrCrew) + "\n" + "Security Officers: " + str(TargetCurTacticalCrew) + "\n" + "Enemy Looses: " + str(enlooses)
    pTargetText = App.TGParagraph_CreateW(App.TGString(str(sTargetText)), pTargetInfoWindow.GetMaximumInteriorWidth(), None, '', pTargetInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pTargetInfoWindow.AddChild(pTargetText, 0, 0.01)

    sRecallInfoText = "Returning Crew: " + str(retcrew) + "\n" + "Remaining Awayteam: " + str(remcrew) + "\n" + "Player Crew: " + str(preplcrew)
    pRecallInfoText = App.TGParagraph_CreateW(App.TGString(str(sRecallInfoText)), pTargetInfoWindow.GetMaximumInteriorWidth(), None, '', pTargetInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pRecallInfoWindow.AddChild(pRecallInfoText, 0, 0.01)

    sTransferInfoText = str(transport) + "\n" + "Remaining Crew: " + str(fPlayerCurrCrew) + "\n" + "Awayteam Members: " + str(awayteam)
    pTransferInfoText = App.TGParagraph_CreateW(App.TGString(str(sTransferInfoText)), pTargetInfoWindow.GetMaximumInteriorWidth(), None, '', pTargetInfoWindow.GetMaximumInteriorWidth(), App.TGParagraph.TGPF_WORD_WRAP | App.TGParagraph.TGPF_READ_ONLY)
    pTransferInfoWindow.AddChild(pTransferInfoText, 0, 0.01)

    kNormalColor = App.TGColorA() 
    kNormalColor.SetRGBA(0.8, 0.6, 0.8, 1.0)
    kHilightedColor = App.TGColorA() 
    kHilightedColor.SetRGBA(0.92, 0.76, 0.92, 1.0)
    kDisabledColor = App.TGColorA() 
    kDisabledColor.SetRGBA(0.25, 0.25, 0.25, 1.0)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_CAPTURE)
    pEvent.SetString("DS9FXCapture")
    if transportstat == 2:
        pButton = App.STRoundedButton_CreateW(App.TGString("Send Reinforcements"), pEvent, 0.16, 0.035)
    else:
        pButton = App.STRoundedButton_CreateW(App.TGString("Capture"), pEvent, 0.16, 0.035)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    if transportstat == 0:
        pButton.SetDisabled()
    pCaptureWindow.AddChild(pButton, 0.01, 0.2)
    pCaptureWindow.MoveToFront(pButton)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_RECALL)
    pEvent.SetString("DS9FXRecall")
    pButton = App.STRoundedButton_CreateW(App.TGString("Recall"), pEvent, 0.16, 0.035)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    if recallstat == 0:
        pButton.SetDisabled()
    pRecallWindow.AddChild(pButton, 0.01, 0.2)
    pRecallWindow.MoveToFront(pButton)

    pEvent = App.TGStringEvent_Create()
    pEvent.SetEventType(ET_CLOSE)
    pEvent.SetString("DS9FXCaptureClose")
    pButton = App.STRoundedButton_CreateW(App.TGString("Close"), pEvent, 0.36, 0.04)
    pButton.SetNormalColor(kNormalColor)
    pButton.SetHighlightedColor(kHilightedColor)
    pButton.SetSelectedColor(kNormalColor)
    pButton.SetDisabledColor(kDisabledColor)
    pButton.SetColorBasedOnFlags()
    pMainWindow.AddChild(pButton, 0.12, 0.61)
    pMainWindow.MoveToFront(pButton)
    # Sov fix ends here

    pGraphicsMode = App.GraphicsModeInfo_GetCurrentMode() 
    pLCARS = pGraphicsMode.GetLcarsString() 
    pGlass = App.TGIcon_Create(pLCARS, 120) 
    pGlass.Resize(pMainPane.GetWidth(), pMainPane.GetHeight()) 
    pMainPane.AddChild(pGlass, 0, 0)

    pTransferInfoWindow.InteriorChangedSize()
    pTransferInfoWindow.Layout()
    pRecallInfoWindow.InteriorChangedSize()
    pRecallInfoWindow.Layout()
    pRecallWindow.InteriorChangedSize()
    pRecallWindow.Layout()
    pTargetInfoWindow.InteriorChangedSize()
    pTargetInfoWindow.Layout()
    pPlayerInfoWindow.InteriorChangedSize()
    pPlayerInfoWindow.Layout()
    pCaptureWindow.InteriorChangedSize()
    pCaptureWindow.Layout()
    pMainWindow.InteriorChangedSize()
    pMainWindow.Layout()
    pMainPane.Layout()
    pPane.Layout()

    pPane.SetVisible()

def UpdateSlider(pObject, pEvent):
    global pSlider, fPercentage, captureships, sRecallInfoText, pRecallInfoText, sTransferInfoText, pTransferInfoText, maxTransCrew

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0
    
    if hasattr(pEvent, "GetFloat"):
        fPercentage = pEvent.GetFloat()
    else:
        if pObject and pEvent:
            pObject.CallNextHandler(pEvent)
        return 0

    pSlider.SetValue(fPercentage)

    crewinfolist = crewinfo()
    fPlayerMaxCrew = crewinfolist[0]
    fPlayerCurrCrew = crewinfolist[1]
    PlayerCurTacticalCrew = crewinfolist[2]
    fTargetMaxCrew = crewinfolist[3]
    fTargetCurrCrew = crewinfolist[4]
    TargetCurTacticalCrew = crewinfolist[5]

    maxTransCrew = int(fTargetMaxCrew * 1.5)
    if maxTransCrew > PlayerCurTacticalCrew:
        maxTransCrew = PlayerCurTacticalCrew

    iPlayerTransfer = int(maxTransCrew * float(fPercentage))
    if iPlayerTransfer >= PlayerCurTacticalCrew:
        iPlayerTransfer = PlayerCurTacticalCrew


    if not captureships.has_key(pTargetID):
        awayteam = 0
        transport = "Crew to Transport: "
        iPlayerRecall = "N/A"
        remaw = "N/A"
        newplcrew = fPlayerCurrCrew
        
    else:
        shipcaptureinfo = captureships[pTargetID]
        awayteam = shipcaptureinfo[0]
        transport = "Reinforcemments: "
        
        iPlayerRecall = int(awayteam * float(fPercentage))
        if iPlayerRecall >= awayteam:
            iPlayerRecall = awayteam

        remaw = awayteam - iPlayerRecall
        newplcrew = fPlayerCurrCrew + iPlayerRecall

    sRecallInfoText = "Returning Crew: " + str(iPlayerRecall) + "\n" + "Remaining Awayteam: " + str(remaw) + "\n" + "Player Crew: " + str(newplcrew)
    pRecallInfoText.SetString(str(sRecallInfoText))
        
    sTransferInfoText = transport + str(iPlayerTransfer) + "\n" + "Remaining Crew: " + str(fPlayerCurrCrew - iPlayerTransfer) + "\n" + "Awayteam Members: " + str(awayteam + iPlayerTransfer)
    pTransferInfoText.SetString(str(sTransferInfoText))

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def KillGUI(pObject, pEvent):
    Quitting()

    App.g_kUtopiaModule.Pause(0)

    if pObject and pEvent:
        pObject.CallNextHandler(pEvent)

def Quitting():
    global pMainPane, pPane, pSlider, sRecallInfoText, pRecallInfoText, sTransferInfoText, pTransferInfoText

    try:
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_CLOSE, pMission, __name__ + ".KillGUI")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_CAPTURE, pMission, __name__ + ".Capture")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_RECALL, pMission, __name__ + ".Recall")
    except:
        pass
    try:
        App.g_kEventManager.RemoveBroadcastHandler(ET_UPDATE, pMission, __name__ + ".UpdateSlider")
    except:
        pass

    if not pPane is None:
        pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
        try:
            App.g_kFocusManager.RemoveAllObjectsUnder(pPane)
            pTCW.DeleteChild(pPane)
            pPane = None   
            pMainPane = None
        except:
            pass

    pSlider = None
    pTransferInfoText = None
    pRecallInfoText = None
    sTransferInfoText = "N/A"
    sRecallInfoText = "N/A"

def Capture(pObject, pEvent):
    global pPane, fPercentage, recallcrew, captureships, secdelay, maxTransCrew

    if fPercentage <= 0:
        return 0

    Reinforcements = None

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    crewinfolist = crewinfo()
    fPlayerMaxCrew = crewinfolist[0]
    fPlayerCurrCrew = crewinfolist[1]
    PlayerCurTacticalCrew = crewinfolist[2]
    fTargetMaxCrew = crewinfolist[3]
    fTargetCurrCrew = crewinfolist[4]
    TargetCurTacticalCrew = crewinfolist[5]

    if recallcrew == 0:
        fToTransfer = float(maxTransCrew) * float(fPercentage)
        if not fToTransfer > 0:
            return 0

    else:
        fToTransfer = recallcrew * (-1)
        recallcrew = 0
        if not fToTransfer < 0:
            return 0

    # check if we already try to capture the target.
    if captureships.has_key(pTargetID):
        shipcaptureinfo = captureships[pTargetID]

        if (shipcaptureinfo[1] - shipcaptureinfo[3]) < 0:
            return 0
        
        if (shipcaptureinfo[0] - shipcaptureinfo[2]) < 0:
            return 0

        if shipcaptureinfo: # Save the fToTransfer value and add the existing away team for the calculation

            Reinforcements = fToTransfer
            pllooses = int(shipcaptureinfo[5] - shipcaptureinfo[0])
            if pllooses < 0:
                pllooses = 0
            enlooses = int(shipcaptureinfo[6] - shipcaptureinfo[1])
            if enlooses < 0:
                enlooses = 0
            fPlayerCurrCrewSvd = fPlayerCurrCrew
            fTargetCurrCrewSvd = fTargetCurrCrew
            PlayerCurTacticalCrewSvd = PlayerCurTacticalCrew
            TargetCurTacticalCrewSvd = TargetCurTacticalCrew
            
            fToTransfer = fToTransfer + shipcaptureinfo[0]
            if fToTransfer <= 0:
                return 0
            fPlayerCurrCrew = fPlayerCurrCrew + shipcaptureinfo[0]
            fTargetCurrCrew = shipcaptureinfo[1]
            PlayerCurTacticalCrew = PlayerCurTacticalCrew + shipcaptureinfo[0]
            if PlayerCurTacticalCrew < 1:
                PlayerCurTacticalCrew = 0
            TargetCurTacticalCrew = int(fTargetCurrCrew - (fTargetMaxCrew / 2.0))
            if TargetCurTacticalCrew < 1:
                TargetCurTacticalCrew = 0
            
            shipcaptureinfo[4] = 2
            shipcaptureinfo = None

    # Calculate the time:
    fighttime = int((((fToTransfer + fTargetCurrCrew) * 235) / 2000.0) - (235 / 2000.0) + 5)

    if fighttime < 10:
        fighttime = 10

    # Now calculate the fight:

    playervalue = (fToTransfer * 3.0)
    targetvalue = ((TargetCurTacticalCrew * 3.0) + (fTargetCurrCrew - float(TargetCurTacticalCrew))) * 1.1

    if fTargetMaxCrew < fPlayerMaxCrew: # Player has a bigger crew   (+ player)
        targetvalue = targetvalue * 1.1

    else:
        playervalue = playervalue * 1.1 # Target has a bigger crew   (+ target)

    if (fTargetMaxCrew / 100.0) * 45.0 >= fTargetCurrCrew: # Target lost many crewmembers   (- Target)
        targetvalue = targetvalue * 0.7

    if (fPlayerMaxCrew / 100.0) * 45.0 >= fPlayerCurrCrew: # Atacker lost many crewmembers   (+ Player)
        playervalue = playervalue * 1.2

    if (fTargetMaxCrew / 100.0) * 95.0 <= fTargetCurrCrew: # Target still has standard crew or even more   (+ Target)
        if fTargetMaxCrew + ((fTargetMaxCrew / 100.0) * 5.0) <= fTargetCurrCrew:
            targetvalue = targetvalue * 3.0

        else:
            targetvalue = targetvalue * 1.8

    if fToTransfer >= (fTargetMaxCrew / 2): # Atacker beams over too many ppl   (- Player)
        playervalue = playervalue * 0.5

    gvalue = (playervalue / (playervalue + targetvalue)) * 100 # the chance for the player to win.

    if gvalue > 50:
        deadfriends = int(((100 - gvalue) * 1.75) * (fToTransfer / 100.0))
        deadenemies = int((gvalue / 100.0) * fTargetCurrCrew)

    else:
        deadfriends = int((100 - gvalue) * (fToTransfer / 100.0))
        deadenemies = int((gvalue * 1.75) * (fTargetCurrCrew / 100.0))

    RandomNr = App.g_kSystemWrapper.GetRandomNumber(99) + 1 # Sov fix

    if (RandomNr - gvalue) < 7.5 and RandomNr >= gvalue or (gvalue - RandomNr) < 7.5 and RandomNr < gvalue: # Everyone is dying :(
        killfrppl = int(fToTransfer / (fighttime / 5.0))
        killenppl = int(fTargetCurrCrew / (fighttime / 5.0))

    elif float(RandomNr) < gvalue: # Player is winning...
        killfrppl = int(deadfriends / (fighttime / 5.0))
        killenppl = int(fTargetCurrCrew / (fighttime / 5.0))

    else: # Enemy is winning...
        killfrppl = int(fToTransfer / (fighttime / 5.0))
        killenppl = int(deadenemies / (fighttime / 5.0))

    if killenppl < 1: # sadly we need to set a minimum
        killenppl = 1

    if killfrppl < 1: # same here
        killfrppl = 1

    # Now save the important information - so we can recall our crewmen even if we're trying to capture different ships at the same time.
    fToTransfer = int(fToTransfer)
    # current friendly crew, current enemy crew, friendly kill interval, enemy kill interval, status, friendly start crew, enemy start crew
    shipcaptureinfo = [fToTransfer, fTargetCurrCrew, killfrppl, killenppl, 0, fToTransfer, fTargetCurrCrew]

    delay = 0

    if not Reinforcements == None: # Restore the correct information
        shipcaptureinfo[5] = int(fToTransfer + pllooses)
        shipcaptureinfo[6] = int(fTargetCurrCrew + enlooses)
        fToTransfer = int(Reinforcements)
        fPlayerCurrCrew = fPlayerCurrCrewSvd
        fTargetCurrCrew = fTargetCurrCrewSvd
        PlayerCurTacticalCrew = PlayerCurTacticalCrewSvd
        TargetCurTacticalCrew = TargetCurTacticalCrewSvd
        delay = 6

    secdelay = 1
    pSequence = App.TGSequence_Create()
    pAction = App.TGScriptAction_Create(__name__, "Startloop", shipcaptureinfo, pTargetID, fToTransfer)
    pSequence.AddAction(pAction, None, delay)

    pPane.SetNotVisible()
    App.g_kUtopiaModule.Pause(0)
    Quitting()
    
    pSequence.Play()

def Recall(pObject, pEvent):
    global pPane, captureships, fPercentage, recallcrew, secdelay

    recallcrew = 0

    if fPercentage <= 0:
        return 0

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    shipcaptureinfo = captureships[pTargetID]
    if not shipcaptureinfo:
        return 0

    if (shipcaptureinfo[1] - shipcaptureinfo[3]) < 0:
        return 0
        
    if (shipcaptureinfo[0] - shipcaptureinfo[2]) < 0:
        return 0

    if fPercentage >= 1.0:
        secdelay = 1
        shipcaptureinfo[4] = 1

        pPane.SetNotVisible()
        App.g_kUtopiaModule.Pause(0)
        Quitting()
        return 0

    else:
        recallcrew = int(float(fPercentage) * shipcaptureinfo[0])
        Capture(None, None)
        return 0
    
    return 0

def KillCrew(pAction, pShipID):
    global captureships, secdelay

    if not pShipID:
        return 0

    if not captureships.has_key(pShipID):
        return 0
    
    shipcaptureinfo = captureships[pShipID]

    if not shipcaptureinfo:
        return 0

    if shipcaptureinfo[4] > 0 and shipcaptureinfo[4] < 3:
        
#     if ShieldCheck(pShipID) == 1:
        
        if shipcaptureinfo[4] == 1:
            
            pPlayer = MissionLib.GetPlayer()
            if not pPlayer:
                return 0
            
            pPlayerID = pPlayer.GetObjID()
            if not pPlayerID:
                return 0
            
            Transfer(shipcaptureinfo[0])
            secdelay = 0
            
        del captureships[pShipID]
        return 0
        
#     else:
#         shipcaptureinfo[4] = 3

    if shipcaptureinfo[0] > 0 and shipcaptureinfo[1] > 0:
        
        iShipCurrStats = LifeSupport_dict.dCrew[pShipID]
        iShipCurrStatstest = shipcaptureinfo[0] + shipcaptureinfo[1]
        froff = 0
        enoff = 0
        
        if iShipCurrStats != iShipCurrStatstest:
            offset = int(iShipCurrStats - iShipCurrStatstest) # might be negative
            froff = offset / 2
            offset = (offset % 2)
            
            if froff < 0 and offset != 0:
                enoff = froff - offset
            else:
                enoff = froff + offset
        
        iShipCurrStats = iShipCurrStats - (shipcaptureinfo[2] + shipcaptureinfo[3])
        if iShipCurrStats <= 0:
            iShipCurrStats = 0
 
        LifeSupport_dict.dCrew[pShipID] = iShipCurrStats
        
        pShips = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
        if pShips:
            DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShips)

        froff = abs(froff)
        enoff = abs(enoff)
        shipcaptureinfo[2] = shipcaptureinfo[2] + froff
        shipcaptureinfo[3] = shipcaptureinfo[3] + enoff
            
        shipcaptureinfo[0] = shipcaptureinfo[0] - (shipcaptureinfo[2])
        shipcaptureinfo[1] = shipcaptureinfo[1] - (shipcaptureinfo[3])
        if iShipCurrStats <= 0:
            shipcaptureinfo[0] = 0
            shipcaptureinfo[1] = 0

        if shipcaptureinfo[0] > 0 and shipcaptureinfo[1] > 0:
            pSequence = App.TGSequence_Create()
            pAction = App.TGScriptAction_Create(__name__, "KillCrew", pShipID)
            pSequence.AddAction(pAction, None, 5) 
            pSequence.Play()
            return 0

    if shipcaptureinfo[1] > 0 and shipcaptureinfo[0] <= 0:
        LifeSupport_dict.dCrew[pShipID] = int(shipcaptureinfo[1]) # must be positive.
        pShips = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
        if pShips:
            DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShips)
        del captureships[pShipID]
        return 0

    pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
    if not pShip:
        del captureships[pShipID]
        return 0

    ShipName = pShip.GetName()
    if not ShipName:
        del captureships[pShipID]
        return 0
    
    if shipcaptureinfo[0] <= 0 and shipcaptureinfo[1] <= 0:
        LifeSupport_dict.dCrew[pShipID] = 0
        pShips = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
        if pShips:
            DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShips)
        pShip.ClearAI()
        DS9FXLifeSupportLib.GroupCheck(pShip)
        DS9FXLifeSupportLib.PlayerCheck(pShipID)
        DS9FXGlobalEvents.Trigger_Ship_Dead_In_Space(pShip)
        del captureships[pShipID]
        return 0
    
    if shipcaptureinfo[0] > 0 and shipcaptureinfo[1] <= 0:
        LifeSupport_dict.dCrew[pShipID] = int(shipcaptureinfo[0]) # must be positive.
        pShips = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
        if pShips:
            DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pShips)
        DS9FXLifeSupportLib.GroupCheck(pShip)
        DS9FXLifeSupportLib.PlayerCheck(pShipID)           
        del captureships[pShipID]
        Reactivate(None, pShip)
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
            return 0
        DS9FXGlobalEvents.Trigger_Ship_Taken_Over(pPlayer, pShip)
        return 0

    return 0

def Startloop(pAction, shipcaptureinfo, pShipID, fToTransfer):
    global captureships, secdelay
    
#    if not ShieldCheck(pShipID) == 1:
#        return 0

    if captureships.has_key(pShipID):
        if captureships[pShipID][4] == 3:
            captureships[pShipID][4] = 0
            return 0
        return 0

    secdelay = 0
    captureships[pShipID] = shipcaptureinfo
    Transfer(-1 * fToTransfer)
    KillCrew(None, pShipID)
    return 0

def crewinfo():
    crewinfolist = []
    
    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return 0

    pPlayerID = pPlayer.GetObjID()
    if not pPlayerID:
        return 0

    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    if not pTarget:
        return 0

    pTargetID = pTarget.GetObjID()
    if not pTargetID:
        return 0

    if not LifeSupport_dict.dCrew.has_key(pPlayerID) or not LifeSupport_dict.dCrew.has_key(pTargetID):
        return 0

    pPlayerInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pPlayer, pPlayerID) # Sov Edit
    if not pPlayerInfo:
        return 0

    fPlayerMaxCrew = pPlayerInfo["fMax"]
    fPlayerCurrCrew = pPlayerInfo["fMin"]

    PlayerCurTacticalCrew = int(fPlayerCurrCrew - (fPlayerMaxCrew / 2.0)) # available crew to transfer

    pTargetInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pTarget, pTargetID) # Sov Edit
    if not pTargetInfo:
        return 0

    fTargetMaxCrew = pTargetInfo["fMax"]
    fTargetCurrCrew = pTargetInfo["fMin"]

    TargetCurTacticalCrew = int(fTargetCurrCrew - (fTargetMaxCrew / 2.0))

    testcrewinfolist = [fPlayerMaxCrew, fPlayerCurrCrew, PlayerCurTacticalCrew, fTargetMaxCrew, fTargetCurrCrew, TargetCurTacticalCrew]

    for creamount in testcrewinfolist:
        if creamount < 1:
            creamount = 0
        crewinfolist.append(creamount)

    return crewinfolist

def Reset():
    global pPane, pMainPane, pSlider, fPercentage, recallcrew, secdelay, captureships, sRecallInfoText, pRecallInfoText, sTransferInfoText, pTransferInfoText

    Quitting()
#    App.g_kUtopiaModule.Pause(0) # I'm not sure if that is needed here or if it should be removed...
    
    pPane = None
    pMainPane = None
    pSlider = None
    sRecallInfoText = "N/A"
    pRecallInfoText = None
    sTransferInfoText = "N/A"
    pTransferInfoText = None
    fPercentage = 0
    recallcrew = 0
    secdelay = 0
    
    captureships = {}

def ShieldCheck(pShipID):
    pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
    if not pShip:
        return 0

    tarshields = pShip.GetShields()

    if tarshields:
        if tarshields.IsOn() == 1:
            s1 = tarshields.GetSingleShieldPercentage(tarshields.FRONT_SHIELDS)
            s2 = tarshields.GetSingleShieldPercentage(tarshields.REAR_SHIELDS)
            s3 = tarshields.GetSingleShieldPercentage(tarshields.TOP_SHIELDS)
            s4 = tarshields.GetSingleShieldPercentage(tarshields.BOTTOM_SHIELDS)
            s5 = tarshields.GetSingleShieldPercentage(tarshields.LEFT_SHIELDS)
            s6 = tarshields.GetSingleShieldPercentage(tarshields.RIGHT_SHIELDS)
            
            if s1 < 0.175 or s2 < 0.175 or s3 < 0.175 or s4 < 0.175 or s5 < 0.175 or s6 < 0.175:
                return 1
            
            else:
                return 0
        else:
            return 1
    else:
        return 1

def Transfer(fToTransfer):
    pPlayer = MissionLib.GetPlayer()
    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    pPlayerID = pPlayer.GetObjID()
    pTargetID = pTarget.GetObjID()
    
    iToTransfer = int(fToTransfer)

    pTargetInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pTarget, pTargetID) # Sov Edit
    if not pTargetInfo:
        return 0
    
    fTargetCurrCrew = pTargetInfo["fMin"]

    pPlayerInfo = DS9FXLifeSupportLib.GetShipMaxAndMinCrewCount(pPlayer, pPlayerID) # Sov Edit
    if not pPlayerInfo:
        return 0
    
    fPlayerCurrCrew = pPlayerInfo["fMin"]

    if fToTransfer >= 0: # The player gets crew
        if iToTransfer >= fTargetCurrCrew:
            iToTransfer = fTargetCurrCrew

    else:
        if (iToTransfer * -1) >= fPlayerCurrCrew:
            iToTransfer = (fPlayerCurrCrew * -1)

    if pPlayer.GetShields().IsOn() == 1:
        pSequence = App.TGSequence_Create()
        g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
        pSequence.AppendAction(App.CharacterAction_Create(App.CharacterClass_GetObject(App.g_kSetManager.GetSet('bridge'), 'Engineer'), App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase))
        pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, 4))
        pSequence.Play()

    App.g_kSoundManager.PlaySound("DS9FXTransportSound")

    iPlayerCurrStats = LifeSupport_dict.dCrew[pPlayerID]
    iTargetCurrStats = LifeSupport_dict.dCrew[pTargetID]

    iPlayerCurrStats = iPlayerCurrStats + iToTransfer
    iTargetCurrStats = iTargetCurrStats - iToTransfer

    if iPlayerCurrStats <= 0:
        iPlayerCurrStats = 0
        DS9FXLifeSupportLib.GroupCheck(pPlayer)
        DS9FXLifeSupportLib.PlayerCheck(pPlayerID)

    if iTargetCurrStats <= 0:
        iTargetCurrStats = 0
        pTarget.ClearAI()
        DS9FXLifeSupportLib.GroupCheck(pTarget)
        DS9FXLifeSupportLib.PlayerCheck(pTargetID)

    LifeSupport_dict.dCrew[pPlayerID] = iPlayerCurrStats
    LifeSupport_dict.dCrew[pTargetID] = iTargetCurrStats
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pPlayer)
    DS9FXGlobalEvents.Trigger_Combat_Effectiveness(pTarget)

def Reactivate(pAction, pShip):
    pFriendly = MissionLib.GetFriendlyGroup()
    if not pFriendly:
        return 0

    sName = pShip.GetName()
    if not sName:
        return 0
    
    DS9FXLifeSupportLib.ClearFromGroup(sName)
    
    pFriendly.AddName(str(sName))
    
    DS9FXLifeSupportLib.ResetAffiliationColors()

    # Ok - now we need USS Sovereign's AI code.

    if not (pFriendly.IsNameInGroup(pShip.GetName())): # well I guess it's there, it was just added...
        return 0

    NoQBR = None
    import QuickBattle.QuickBattle
    try:
        import Custom.QuickBattleGame.QuickBattle
    except:
        NoQBR = 'NoQBR'

    if QuickBattle.QuickBattle.pFriendlies:
        if (pShip.GetShipProperty().IsStationary() == 1):

            pShip.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pShip))
        else:
            pShip.SetAI(DS9FXGenericStaticFriendlyFollowAI.CreateAI(pShip))


    if not NoQBR == 'NoQBR':
        if Custom.QuickBattleGame.QuickBattle.pFriendlies:
            if (pShip.GetShipProperty().IsStationary() == 1):

                pShip.SetAI(DS9FXGenericStaticStarbaseFriendlyAI.CreateAI(pShip))
            else:
                pShip.SetAI(DS9FXGenericStaticFriendlyFollowAI.CreateAI(pShip))

    return 0

def Distance(pObject):
    pPlayer = App.Game_GetCurrentPlayer()
    vDifference = pObject.GetWorldLocation()
    vDifference.Subtract(pPlayer.GetWorldLocation())

    return vDifference.Length()
