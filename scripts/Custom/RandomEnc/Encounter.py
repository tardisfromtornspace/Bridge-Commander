from bcdebug import debug
import App
import MissionLib

import Foundation

from Fleets import FleetList

def createRandomPlayerShip():
	debug(__name__ + ", createRandomPlayerShip")
	races = FleetList.keys()
	n = 0
	if races:
		n = App.g_kSystemWrapper.GetRandomNumber(len(races))
	player_race = FleetList[races[n]]
	m = 0
	if player_race:
		m = App.g_kSystemWrapper.GetRandomNumber(len(player_race))
	return (races[n], player_race[m])
	
def createPlayerFleet(race):
	debug(__name__ + ", createPlayerFleet")
	race_ships = FleetList[race]
	n = App.g_kSystemWrapper.GetRandomNumber(2)
	
	ships = []
	for i in range(0, n+1):
		m = 0
		if race_ships:
			m = App.g_kSystemWrapper.GetRandomNumber(len(race_ships))
		ships.append(race_ships[m])
	return ships
		
def createEnemyFleet(race, num):
	debug(__name__ + ", createEnemyFleet")
	races = FleetList.copy()
	del races[race]
	
	irandval = 0
	if races:
		irandval = App.g_kSystemWrapper.GetRandomNumber(len(races))
	race_ships = races.values()[irandval]
	
	n = 0
	if num > 0:
		n = App.g_kSystemWrapper.GetRandomNumber(num) + 2

	ships = []
	for i in range(0, n+1):
		m = 0
		if race_ships:
			m = App.g_kSystemWrapper.GetRandomNumber(len(race_ships))
		ships.append(race_ships[m])
	return ships
