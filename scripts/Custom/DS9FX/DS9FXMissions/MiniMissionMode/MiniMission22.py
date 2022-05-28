# Xtended Mission

# by Smbw

import App
import MissionLib
import loadspacehelper
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXMissions import MissionIDs
from Custom.DS9FX.DS9FXLib import DS9FXMenuLib, DS9FXShips, DS9FXMissionLib, DS9FXLifeSupportLib
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXAILib import DS9FXGenericEnemyAI, DS9FXGenericFriendlyFollowAI
from AI.Player import OrbitPlanet

pName = MissionIDs.MM22
sName = "Escort Service"
sObjectives = "-Escort the USS Lexington to New Bajor\n-Defend the Lexington against any attackers!"
sBriefing = "Captain, you are to escort the USS Lexington to New Bajor. The USS Lexington is carrying supplies and relif crew for the colony."
sModule = "Custom.DS9FX.DS9FXMissions.MiniMissionMode.MiniMission22"

ShipIDs = []
LexingtonID = None
iStatus = 0


def Briefing():
        DS9FXMissionLib.Briefing(sName, sObjectives, sBriefing, pName, sModule)

def MissionInitiate():
        global LexingtonID, iStatus, ShipIDs

        iStatus = 0
        ShipIDs = []
        LexingtonID = None

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
        App.g_kEventManager.AddBroadcastPythonFuncHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")        
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pLocation = pPlayer.GetWorldLocation()

        sShip = "USS Lexington"
        pShip = loadspacehelper.CreateShip(DS9FXShips.Nebula, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericFriendlyFollowAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()
        LexingtonID = pShip.GetObjID()

def DisableDS9FXMenuButtons(pObject, pEvent):
        try:
                bHail = DS9FXMenuLib.GetSubMenuButton("Hail DS9", "Helm", "DS9FX", "DS9 Options...")
                bHail.SetDisabled()
        except:
                raise RuntimeError, "DS9FX: Runtime mission error... please consult BCS:TNG..."

def ObjectExploding(pObject, pEvent):
        global ShipIDs, LexingtonID, iStatus

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if pShip != None:
                if pShip == pPlayer:
                        FailedTxt()
                        RemoveHandlers()
                        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

                pShipID = pShip.GetObjID()

                if pShipID in ShipIDs:
                        ShipIDs.remove(pShipID)
                        if ShipIDs == []:
                                if iStatus == 1:
                                        Lexington = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(LexingtonID))
                                        if Lexington:
                                                pSet = Lexington.GetContainingSet()
                                                pObj = pSet.GetObject('New Bajor Colony')
                                                pPlanet = App.Planet_Cast(pObj)
                                                if pPlanet:
                                                        Lexington.SetAI(OrbitPlanet.CreateAI(Lexington, pPlanet))
                                                        pCon = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 250, pPlanet.GetName(), Lexington.GetName())
                                                        MissionLib.CallFunctionWhenConditionChanges(pMission, __name__, "LexingtonInRange", pCon)
                                                        HintTxt()
                                elif iStatus == 2:
                                        GoHomeTxt()
                                        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
                                        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

                elif pShipID == LexingtonID:
                        LexingtonTxt()
                        RemoveHandlers()
                        DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def FailedTxt():
        sText = "Mission Failed!"
        iPos = 6
        iFont = 12
        iDur = 6
        iDelay = 0
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def LexingtonTxt():
        sText = "Mission Failed! The Lexington has been destroyed!"
        iPos = 6
        iFont = 12
        iDur = 6
        iDelay = 0
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def HintTxt():
        sText = "The Lexington is going to beaming down crew and supplies..."
        iPos = 6
        iFont = 12
        iDur = 16
        iDelay = 30
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionHandler(pObject, pEvent):
        global iStatus
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        if (pShip != None):
                if pPlayer.GetObjID() == pShip.GetObjID():

                        pSystemName = pSet.GetName()
                        if pSystemName == "DS9FXNewBajor1" and iStatus == 0:
                                DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
                                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")

                                ObjectiveTxt()
                                CreateShips()
                                iStatus = 1

                        elif pSet.GetName() == "DeepSpace91" and iStatus == 1:
                                ObjectiveTxt3()
                                # Delay the creation, otherwise the AI will grab the dummy player instead of the real player
                                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".Reinforcements", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)
                                iStatus = 2

                        elif pSet.GetName() == "DS9FXTRogoran1" and iStatus == 2:
                                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
                                DS9FXGlobalEvents.Trigger_Force_Mission_Playing(MissionLib.GetPlayer())
                                CreateShips2()

                        else:
                                MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".DisableDS9FXMenuButtons", App.g_kUtopiaModule.GetGameTime() + 10, 0, 0)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def ObjectiveTxt():
        sText = "Sir, we need to secure the System first so the Lexington can safely beam down its crew!"
        iPos = 6
        iFont = 12
        iDur = 10
        iDelay = 6
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def ObjectiveTxt2():
        sText = "Captain, we are to return to DS9 for further instructions..."
        iPos = 6
        iFont = 12
        iDur = 20
        iDelay = 2
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def ObjectiveTxt3():
        sText = "The attack in on New Bajor was a result of the renegade dominion forces. We believe that the renegades try building a base in the TRogoran System. Captain, we want you to attack the renegades. The USS Discovery and the USS Thunderbird will join you.\nGood luck Captain!"
        iPos = 8
        iFont = 12
        iDur = 25
        iDelay = 25
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def CreateShips(pObject = None, pEvent = None):
        global ShipIDs

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pLocation = pPlayer.GetWorldLocation()
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        for i in range(1, 9):
                sShip = "Atacker " + str(i)
                pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")
                DS9FXLifeSupportLib.ClearFromGroup(sShip)
                pMission.GetEnemyGroup().AddName(sShip)
                pShip = MissionLib.GetShip(sShip, pSet) 
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(DS9FXGenericEnemyAI.CreateAI(pShip))
                pX = pLocation.GetX()
                pY = pLocation.GetY()
                pZ = pLocation.GetZ()
                adX = GetRandomNumber(1500, 100)
                adY = GetRandomNumber(1500, 100)
                adZ = GetRandomNumber(1500, 100)
                pX = pX + adX
                pY = pY + adY
                pZ = pZ + adZ
                pShip.SetTranslateXYZ(pX, pY, pZ)
                pShip.UpdateNodeOnly()
                ShipIDs.append(pShip.GetObjID())

        for i in range(9, 14):
                sShip = "Atacker " + str(i)
                pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Dummy Location")
                DS9FXLifeSupportLib.ClearFromGroup(sShip)
                pMission.GetEnemyGroup().AddName(sShip)
                pShip = MissionLib.GetShip(sShip, pSet) 
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(DS9FXGenericEnemyAI.CreateAI(pShip))
                pX = pLocation.GetX()
                pY = pLocation.GetY()
                pZ = pLocation.GetZ()
                adX = GetRandomNumber(1500, 100)
                adY = GetRandomNumber(1500, 100)
                adZ = GetRandomNumber(1500, 100)
                pX = pX + adX
                pY = pY + adY
                pZ = pZ + adZ
                pShip.SetTranslateXYZ(pX, pY, pZ)
                pShip.UpdateNodeOnly()
                ShipIDs.append(pShip.GetObjID())

def CreateShips2(pObject = None, pEvent = None):
        global ShipIDs

        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pLocation = pPlayer.GetWorldLocation()
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        for i in range(1, 6):
                sShip = "Defender " + str(i)
                pShip = loadspacehelper.CreateShip(DS9FXShips.DomBC, pSet, sShip, "Dummy Location")
                DS9FXLifeSupportLib.ClearFromGroup(sShip)
                pMission.GetEnemyGroup().AddName(sShip)
                pShip = MissionLib.GetShip(sShip, pSet) 
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(DS9FXGenericEnemyAI.CreateAI(pShip))
                pX = pLocation.GetX()
                pY = pLocation.GetY()
                pZ = pLocation.GetZ()
                adX = GetRandomNumber(1500, 100)
                adY = GetRandomNumber(1500, 100)
                adZ = GetRandomNumber(1500, 100)
                pX = pX + adX
                pY = pY + adY
                pZ = pZ + adZ
                pShip.SetTranslateXYZ(pX, pY, pZ)
                pShip.UpdateNodeOnly()
                ShipIDs.append(pShip.GetObjID())

        for i in range(6, 13):
                sShip = "Defender " + str(i)
                pShip = loadspacehelper.CreateShip(DS9FXShips.Bugship, pSet, sShip, "Dummy Location")
                DS9FXLifeSupportLib.ClearFromGroup(sShip)
                pMission.GetEnemyGroup().AddName(sShip)
                pShip = MissionLib.GetShip(sShip, pSet) 
                pShip = App.ShipClass_Cast(pShip)
                pShip.SetAI(DS9FXGenericEnemyAI.CreateAI(pShip))
                pX = pLocation.GetX()
                pY = pLocation.GetY()
                pZ = pLocation.GetZ()
                adX = GetRandomNumber(1500, 100)
                adY = GetRandomNumber(1500, 100)
                adZ = GetRandomNumber(1500, 100)
                pX = pX + adX
                pY = pY + adY
                pZ = pZ + adZ
                pShip.SetTranslateXYZ(pX, pY, pZ)
                pShip.UpdateNodeOnly()
                ShipIDs.append(pShip.GetObjID())

        sShip = "Renegade Base"
        pShip = loadspacehelper.CreateShip(DS9FXShips.MissionStation, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetEnemyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericEnemyAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()
        ShipIDs.append(pShip.GetObjID())

def LexingtonInRange(bInRange):
        global LexingtonID
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        MissionLib.StopCallingFunctionWhenConditionChanges(__name__, "LexingtonInRange")

        MissionLib.CreateTimer(DS9FXMenuLib.GetNextEventType(), __name__ + ".TransportDone", App.g_kUtopiaModule.GetGameTime() + 12, 0, 0)
        pSequence.Play()
        return 0

def TransportDone(pObject, pEvent):
        global LexingtonID

        ObjectiveTxt2()

        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
        Lexington = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(LexingtonID))
        if Lexington:                
                Lexington.SetAI(DS9FXGenericFriendlyFollowAI.CreateAI(Lexington))

        LexingtonID = None
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())

def Reinforcements(pObject, pEvent):    
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pLocation = pPlayer.GetWorldLocation()
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()


        sShip = "USS Thunderbird"
        pShip = loadspacehelper.CreateShip(DS9FXShips.Akira, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericFriendlyFollowAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()

        sShip = "USS Discovery"
        pShip = loadspacehelper.CreateShip(DS9FXShips.Galaxy, pSet, sShip, "Dummy Location")
        DS9FXLifeSupportLib.ClearFromGroup(sShip)
        pMission.GetFriendlyGroup().AddName(sShip)
        pShip = MissionLib.GetShip(sShip, pSet) 
        pShip = App.ShipClass_Cast(pShip)
        pShip.SetAI(DS9FXGenericFriendlyFollowAI.CreateAI(pShip))
        pX = pLocation.GetX()
        pY = pLocation.GetY()
        pZ = pLocation.GetZ()
        adX = GetRandomNumber(1500, 100)
        adY = GetRandomNumber(1500, 100)
        adZ = GetRandomNumber(1500, 100)
        pX = pX + adX
        pY = pY + adY
        pZ = pZ + adZ
        pShip.SetTranslateXYZ(pX, pY, pZ)
        pShip.UpdateNodeOnly()

def GetRandomNumber(iNum, iStat):
        return App.g_kSystemWrapper.GetRandomNumber(iNum) + iStat

def GoHomeTxt():
        sText = "We're done here. We should return to DS9."
        iPos = 4
        iFont = 12
        iDur = 12
        iDelay = 15
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def MissionEnd(pObject, pEvent):
        pPlayer = MissionLib.GetPlayer()
        pSet = pPlayer.GetContainingSet()
        pShip = App.ShipClass_Cast(pEvent.GetDestination())


        if pShip != None:
                if pPlayer.GetObjID() == pShip.GetObjID():

                        if pSet.GetName() == "DeepSpace91":
                                CompletedTxt()
                                RemoveHandlers()

                                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(pPlayer, pName)

        if pObject and pEvent:
                pObject.CallNextHandler(pEvent)

def CompletedTxt():
        sText = "Mission Completed!"
        iPos = 6
        iFont = 12
        iDur = 6
        iDelay = 20
        DS9FXMissionLib.PrintText(sText, iPos, iFont, iDur, iDelay)

def RemoveHandlers():
        global ShipIDs, LexingtonID, iStatus

        ShipIDs = []
        LexingtonID = None
        iStatus = 0
        pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()

        try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, pMission, __name__ + ".ObjectExploding")
                App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, pMission, __name__ + ".ObjectExploding")                
        except:
                pass
        try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionEnd")
        except:
                pass
        try:
                App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, pMission, __name__ + ".MissionHandler")
        except:
                pass
        try:
                DS9FXGlobalEvents.Trigger_Stop_Forcing_Mission_Playing(MissionLib.GetPlayer())
        except:
                pass

def CrewLost():
        try:
                FailedTxt()
                RemoveHandlers()
                DS9FXGlobalEvents.Trigger_DS9FX_Mission_End(MissionLib.GetPlayer(), pName)
        except:
                pass
