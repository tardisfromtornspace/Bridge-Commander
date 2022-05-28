from bcdebug import debug
import App
import MissionLib
import string
from Libs.Races import Races
from Libs.LibQBautostart import *

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }


def ObjectCreatedHandler(pObject, pEvent):
	debug(__name__ + ", ObjectCreatedHandler")
	pObject.CallNextHandler(pEvent)
	
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip and pShip.GetShipProperty() and pShip.GetShipProperty().IsStationary():
		sRace = GetRaceFromShip(pShip)
		sSystemName = GetSystemShortName(pShip.GetContainingSet())
		if sRace and sSystemName:
			Races[sRace].AddSystem(sSystemName)
	debug(__name__ + ", ObjectCreatedHandler End")
		

def ObjectKilledHandler(pObject, pEvent):
	debug(__name__ + ", ObjectKilledHandler")
	pObject.CallNextHandler(pEvent)
	
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip and pShip.GetShipProperty().IsStationary():
		sRace = GetRaceFromShip(pShip)
		sSystemName = GetSystemShortName(pShip.GetContainingSet())
		
		lStationaryShipsInSet = GetStationaryShipsIn(pShip.GetContainingSet())
		AnotherStationOfThisRaceInSystem = 0
		for pStation in lStationaryShipsInSet:
			sStationRace = GetRaceFromShip(pStation)

			if sStationRace == sRace and not pStation.IsDead() and not pStation.IsDying():
				AnotherStationOfThisRaceInSystem = 1
				break
				
		if Races.has_key(sRace) and not AnotherStationOfThisRaceInSystem:
			Races[sRace].RemoveSystem(sSystemName)
		

def init():
	debug(__name__ + ", init")
	pMission = MissionLib.GetMission()
	
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED, pMission, __name__ + ".ObjectCreatedHandler")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_EXPLODING, pMission, __name__ + ".ObjectKilledHandler")
