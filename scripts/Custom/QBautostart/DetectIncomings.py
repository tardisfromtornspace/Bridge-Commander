import App
import MissionLib
from Libs.Races import Races
from Libs.LibQBautostart import *


MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Download": "http://www.bckobayashimaru.de",
                "needBridge": 0
            }

MAX_DETECT_DISTANCE = 10000 # km

def PrintIncomingMessage(sSetName, sShipName, sRace, iCloaked):
	if iCloaked:
		s = "Warning: unidentified object entering %s" % (sSetName)
	else:
		s = "Warning: %s ship identified as %s is entering %s" % (sRace, sShipName, sSetName)
	Say(s)


def WarnRaceForIncoming(sRace, pIncomingShip, sIncomingRace):
	# only needs todo something if the Player is in sRace
	pPlayer = MissionLib.GetPlayer()
	sPlayerRace = GetRaceFromShip(pPlayer)
	# do not warn if player is in same set
	if sRace == sPlayerRace and pPlayer.GetContainingSet().GetName() != pIncomingShip.GetContainingSet().GetName():
		PrintIncomingMessage(pIncomingShip.GetContainingSet().GetName(), pIncomingShip.GetName(), sIncomingRace, pIncomingShip.IsCloaked())


def EnterSet(pObject, pEvent):
	pObject.CallNextHandler(pEvent)
	
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip:
		pSet = pShip.GetContainingSet()
		if not pSet or pSet.GetName() == "warp":
			return
		
		sIncomingShipRace = GetRaceFromShip(pShip)
		
		lStationaryShipsInSet = GetStationaryShipsIn(pShip.GetContainingSet())
		lRaceWarningDone = []
		for pStation in lStationaryShipsInSet:
			sStationRace = GetRaceFromShip(pStation)
			if sStationRace != sIncomingShipRace and Races.has_key(sStationRace) and not Races[sStationRace].IsFriendlyRace(sIncomingShipRace) and Distance(pStation, pShip) < App.UtopiaModule_ConvertKilometersToGameUnits(MAX_DETECT_DISTANCE) and sStationRace not in lRaceWarningDone:
				WarnRaceForIncoming(sStationRace, pShip, sIncomingShipRace)
				lRaceWarningDone.append(sStationRace)


def init():
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_SET, MissionLib.GetMission(), __name__ + ".EnterSet")
