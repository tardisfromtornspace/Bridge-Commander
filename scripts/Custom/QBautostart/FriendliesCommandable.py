import App
import MissionLib
import Lib.LibEngineering

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 1
            }


GROUP_CHECK_TIMER = Lib.LibEngineering.GetEngineeringNextEventType()

def GroupChanged(pObject, pEvent):
	pPlayer = MissionLib.GetPlayer()
	MissionLib.CreateTimer(GROUP_CHECK_TIMER, __name__ + ".GroupChanged", App.g_kUtopiaModule.GetGameTime() + 10.0, 0, 0)
	
	if not pPlayer:
		return
	
	pSet = pPlayer.GetContainingSet()
	pFriendlyGroup = MissionLib.GetFriendlyGroup()
	
	if not pSet:
		return
	
	lpFriendlies = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)

	MissionLib.RemoveAllCommandableShips()
	for pFriendly in lpFriendlies:
		if pFriendly.GetName() != pPlayer.GetName():
			MissionLib.AddCommandableShip(pFriendly.GetName())


def init():
	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	
	MissionLib.CreateTimer(GROUP_CHECK_TIMER, __name__ + ".GroupChanged", App.g_kUtopiaModule.GetGameTime() + 10.0, 0, 0)
