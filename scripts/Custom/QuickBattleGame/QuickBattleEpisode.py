import App

###############################################################################
#	PreLoadAssets()
#	
#	This is called once, at the beginning of the mission before Initialize()
#	to allow us to add models to be pre loaded
#	
#	Args:	pMission	- the Mission object
#	
#	Return:	none
###############################################################################
def PreLoadAssets(pMission):
	return 0

def Initialize(pEpisode):
    'Called Initialize and activate an Episode'
    pMissionStartEvent = App.TGEvent_Create()
    pMissionStartEvent.SetEventType(App.ET_MISSION_START)
    pMissionStartEvent.SetDestination(pEpisode)
    pEpisode.LoadMission('Custom.QuickBattleGame.QuickBattle', pMissionStartEvent)


def Terminate(pEpisode):
    'Called Terminate and de-activate an Episode'
    pass

