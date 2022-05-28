import App

def Initialize(pEpisode):
    'Called Initialize and activate an Episode'
    pMissionStartEvent = App.TGEvent_Create()
    pMissionStartEvent.SetEventType(App.ET_MISSION_START)
    pMissionStartEvent.SetDestination(pEpisode)
    pEpisode.LoadMission('Custom.RandomEnc.RandomEncMission', pMissionStartEvent)


def Terminate(pEpisode):
    'Called Terminate and de-activate an Episode'
    pass

