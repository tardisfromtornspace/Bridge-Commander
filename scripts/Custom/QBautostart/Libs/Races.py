from bcdebug import debug
Races = {}

bLoadedPlugins = 0

def LoadRacesPlugins():
	debug(__name__ + ", LoadRacesPlugins")
	global bLoadedPlugins, Races
	if bLoadedPlugins == 1:
		return
	
	import nt
	import string
	import Foundation
	from Custom.QBautostart.Libs.Races import Races
	from Custom.QBautostart.Libs.Racesclass import RaceInfo

	RacesList = nt.listdir('scripts\Custom\QBautostart\Libs\Racesd')

	lToBeRemoved = ['__init__.py', '__init__.pyc']
	for sRemovee in lToBeRemoved:
		if sRemovee in RacesList:
			RacesList.remove(sRemovee)

	lCreatedRacesPlugins = []

	for sFile in RacesList :
		sFileStrings = string.split(sFile, '.')
		sPlugin = sFileStrings[0]
		sExt = sFileStrings[-1]
		if (sExt == "py" or sExt == "pyc") and (not sPlugin in lCreatedRacesPlugins):
			lCreatedRacesPlugins.append(sPlugin)
			pModule = __import__("Custom.QBautostart.Libs.Racesd." + sPlugin)

			pRaceObj = RaceInfo(pModule.sName)

			if "ALL" in pModule.lEnemies:
				pRaceObj.SetIsEnemyToAll(1)
			for sEnemy in pModule.lEnemies:
				if sEnemy != "ALL":
					pRaceObj.AddEnemy(sEnemy)

			for sFriend in pModule.lFriendlies:
				pRaceObj.AddFriendly(sFriend)

			pRaceObj.SetPeaceValue(pModule.fPeaceValue)

			lShipFiles = []
			FdtnShips = Foundation.shipList
			if FdtnShips:
				for Ship in FdtnShips:
					lShipFiles.append(Ship.shipFile)
					if Ship.menuGroup:
						if not Ship.shipFile in pModule.lDefaultBases and Ship.menuGroup == pModule.sLookInMenu:
							pRaceObj.AddShip(Ship.shipFile)

			for sShipClass in pModule.lDefaultShips:
				if sShipClass in lShipFiles:
					pRaceObj.AddShip(sShipClass)

			lEscortees = pModule.dEscorts.keys()
			for sEscortedShip in lEscortees:
				for sEscort in pModule.dEscorts[sEscortedShip]:
					if sEscort in lShipFiles and sEscortedShip in lShipFiles:
						pRaceObj.AddEscort(sEscortedShip, sEscort)

			if pModule.sInitialShipBuild != "":
				if pModule.sInitialShipBuild in lShipFiles:
					pRaceObj.BuildShip(pModule.sInitialShipBuild)

			for sBaseClass in pModule.lDefaultBases:
				if sBaseClass in lShipFiles:
					pRaceObj.AddBase(sBaseClass)

			lResourcesKeys = pModule.dResources.keys()
			for sReKey in lResourcesKeys:
				pRaceObj.AddResource(sReKey, pModule.dResources[sReKey])

			for sShipName in pModule.lShipNames:
				pRaceObj.AddName(sShipName)

			Races[pModule.sName] = pRaceObj

	bLoadedPlugins = 1
	return

LoadRacesPlugins()
