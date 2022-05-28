# If you lose the original ship, the mission is over

# by Sov

import App
import MissionLib
from Custom.DS9FX.DS9FXMissions import MissionIDs

sMission = ""

def MissionName(pObject, pEvent):
    global sMission

    try:
        s = pEvent.GetCString()
    except:
        return

    sMission = s

def ResetMission():
    global sMission
    sMission = ""

def MissionFailureCheck(pObject, pEvent):
    global sMission

    if sMission == "":
        return

    pPlayer = MissionLib.GetPlayer()
    if not pPlayer:
        return

    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if not pShip:
        return

    if not pPlayer.GetObjID() == pShip.GetObjID():
        return

    if sMission == MissionIDs.BSM1:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission1
        Mission1.CrewLost()

    elif sMission == MissionIDs.BSM2:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission2
        Mission2.CrewLost()

    elif sMission == MissionIDs.BSM3:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission3
        Mission3.CrewLost()

    elif sMission == MissionIDs.BSM4:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission4
        Mission4.CrewLost()

    elif sMission == MissionIDs.BSM5:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.BorderSkirmish import Mission5
        Mission5.CrewLost()

    elif sMission == MissionIDs.HM1:
        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission1
        HistoricMission1.CrewLost()

    elif sMission == MissionIDs.HM2:
        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission2
        HistoricMission2.CrewLost()

    elif sMission == MissionIDs.HM3:
        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission3
        HistoricMission3.CrewLost()

    elif sMission == MissionIDs.HM4:
        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission4
        HistoricMission4.CrewLost()

    elif sMission == MissionIDs.HM5:
        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission5
        HistoricMission5.CrewLost()

    elif sMission == MissionIDs.HM6:
        from Custom.DS9FX.DS9FXMissions.HistoricMode import HistoricMission6
        HistoricMission6.CrewLost()

    elif sMission == MissionIDs.MM1:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission1
        MiniMission1.CrewLost()

    elif sMission == MissionIDs.MM2:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission2
        MiniMission2.CrewLost()

    elif sMission == MissionIDs.MM3:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission3
        MiniMission3.CrewLost()

    elif sMission == MissionIDs.MM4:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission4
        MiniMission4.CrewLost()

    elif sMission == MissionIDs.MM5:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission5
        MiniMission5.CrewLost()

    elif sMission == MissionIDs.MM6:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission6
        MiniMission6.CrewLost()

    elif sMission == MissionIDs.MM7:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission7
        MiniMission7.CrewLost()

    elif sMission == MissionIDs.MM8:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission8
        MiniMission8.CrewLost()

    elif sMission == MissionIDs.MM9:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission9
        MiniMission9.CrewLost()

    elif sMission == MissionIDs.MM10:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission10
        MiniMission10.CrewLost()

    elif sMission == MissionIDs.MM11:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission11
        MiniMission11.CrewLost()

    elif sMission == MissionIDs.MM12:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission12
        MiniMission12.CrewLost()

    elif sMission == MissionIDs.MM13:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission13
        MiniMission13.CrewLost()

    elif sMission == MissionIDs.MM14:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission14
        MiniMission14.CrewLost()

    elif sMission == MissionIDs.MM15:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission15
        MiniMission15.CrewLost()

    elif sMission == MissionIDs.MM16:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission16
        MiniMission16.CrewLost()

    elif sMission == MissionIDs.MM17:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission17
        MiniMission17.CrewLost()

    elif sMission == MissionIDs.MM18:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission18
        MiniMission18.CrewLost()

    elif sMission == MissionIDs.MM19:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission19
        MiniMission19.CrewLost()

    elif sMission == MissionIDs.MM20:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission20
        MiniMission20.CrewLost()

    elif sMission == MissionIDs.MM21:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission21
        MiniMission21.CrewLost()

    elif sMission == MissionIDs.MM22:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import MiniMission22
        MiniMission22.CrewLost()
        
    elif sMission == MissionIDs.RM1:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import RandomMission1
        RandomMission1.CrewLost()        

    elif sMission == MissionIDs.RM2:
        from Custom.DS9FX.DS9FXMissions.MiniMissionMode import RandomMission2
        RandomMission2.CrewLost()   

    elif sMission == MissionIDs.ORM1:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission1
        Mission1.CrewLost()

    elif sMission == MissionIDs.ORM2:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission2
        Mission2.CrewLost()

    elif sMission == MissionIDs.ORM3:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission3
        Mission3.CrewLost()

    elif sMission == MissionIDs.ORM4:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission4
        Mission4.CrewLost()
        
    elif sMission == MissionIDs.ORM5:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission5
        Mission5.CrewLost()      
        
    elif sMission == MissionIDs.ORM6:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission6
        Mission6.CrewLost()

    elif sMission == MissionIDs.ORM7:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission7
        Mission7.CrewLost()

    elif sMission == MissionIDs.ORM8:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission8
        Mission8.CrewLost()  

    elif sMission == MissionIDs.ORM9:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission9
        Mission9.CrewLost()  
        
    elif sMission == MissionIDs.ORM10:
        from Custom.DS9FX.DS9FXMissions.CampaignMode.OldRivals import Mission10
        Mission10.CrewLost()         
