from bcdebug import debug
# Racesclass.py script by Defiant
# Modified by USS Frontier to, and included in Galaxy Charts

try:
	from bcdebug import debug
except ImportError:
	# we do this here because not everybody may have the bcdebug module from KM
	def debug(*args):
		return
import App
from Custom.QBautostart.Libs.Races import Races

class RaceInfo:
	def __init__(self, Race):
		debug(__name__ + ", __init__")
		self.Name = Race
		self.myFriendlys = []
		self.myEnemys = []
		self.isEnemyToAll = 0
        	self.myNames = []
		self.myShips = []
		self.myBases = []
		self.myEscorts = {}
		self.peaceVal = 0.5
		self.PlayerRanks = {}
		self.BuildShips = {}
		self.dResources = {}
		# i'll leave this Systems attribute, but it'll be no longer used. the System Plugins will take care of 
		# assigning a system to an empire.
		self.Systems = []
		self.__createdShipNames = {}   #dict of ship names already used
		self.dWSShips = {}     # dict of WSShip (War Simulation Ship) instances belonging to this race
		# yup, this might seem weird considering the dicts above, but this list stores all WSShip names that passes by this race, since not all of 
		# them might be taken from this race's GetRandomName...
		self.lShipNames = []  
						

	def GetRaceName(self):
		debug(__name__ + ", GetRaceName")
		return self.Name

	def AddName(self, Name):
		debug(__name__ + ", AddName")
		self.myNames.append(Name)
	
	def GetNames(self):
		debug(__name__ + ", GetNames")
		return self.myNames

	def GetRandomName(self):
		debug(__name__ + ", GetRandomName")
		num = len(self.myNames)
		if (num <= 0):
			return None
		rand = App.g_kSystemWrapper.GetRandomNumber(num)
		sName = self.myNames[rand]
		if self.__createdShipNames.has_key(sName):
			sLastChar = self.__createdShipNames[sName]
			if type(sLastChar) == type(""):
				lLetters = ["<FIRST>", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
				iIndex = lLetters.index(sLastChar) + 1
				if iIndex >= len(lLetters):
					sChar = "R1"
					self.__createdShipNames[sName] = 1
				else:
					sChar = lLetters[iIndex]
					self.__createdShipNames[sName] = sChar
				sName = sName + "-" + str(sChar)
			else:
				iDigit = self.__createdShipNames[sName] + 1
				self.__createdShipNames[sName] = iDigit
				sName = sName + "-R" + str(iDigit)
		else:
			self.__createdShipNames[sName] = "<FIRST>"
		return sName
		
    	def GetFriendlys(self):
		debug(__name__ + ", GetFriendlys")
		return self.myFriendlys

	def AddFriendly(self, Friendly):
        	debug(__name__ + ", AddFriendly")
		if not Friendly in self.myFriendlys:
	        	self.myFriendlys.append(Friendly)

	def GetEnemys(self):
		debug(__name__ + ", GetEnemys")
		return self.myEnemys

	def AddEnemy(self, Enemy):
		debug(__name__ + ", AddEnemy")
		if not Enemy in self.myEnemys:
			self.myEnemys.append(Enemy)
        
	def IsFriendlyRace(self, match):
		debug(__name__ + ", IsFriendlyRace")
		if match == self.Name:
			return 1
		if match in self.myFriendlys:
			return 1
		if Races.has_key(match):
			pMatchRace = Races[match]
			if self.Name in pMatchRace.myFriendlys:
				return 1
		return 0
        
	def IsEnemyRace(self, match):
		debug(__name__ + ", IsEnemyRace")
		if match == self.Name:
			return 0
		if self.isEnemyToAll == 1:
			return 1
		if match in self.myEnemys:
			return 1
		if Races.has_key(match):
			pMatchRace = Races[match]
			if self.Name in pMatchRace.myEnemys:
				return 1
		return 0

	def SetIsEnemyToAll(self, bIs):
		debug(__name__ + ", SetIsEnemyToAll")
		self.isEnemyToAll = bIs

	def GetIsEnemyToAll(self, bIs = None):
		debug(__name__ + ", GetIsEnemyToAll")
		return self.isEnemyToAll

	def AddShip(self, Ship):
		debug(__name__ + ", AddShip")
		if not Ship in self.myShips and not Ship in self.myBases:
			self.myShips.append(Ship)
	
	def GetShips(self):
		debug(__name__ + ", GetShips")
		return self.myShips
	
	def AddBase(self, baseScript):
		debug(__name__ + ", AddBase")
		if not baseScript in self.myBases and not baseScript in self.myShips:
			self.myBases.append(baseScript)

	def GetBases(self):
		debug(__name__ + ", GetBases")
		return self.myBases

	def IsOurRace(self, shipScript):
		debug(__name__ + ", IsOurRace")
		for ship in self.myShips:
			if ship == shipScript:
				return 1
		return 0

	def GetAllShipClasses(self):
		debug(__name__ + ", GetAllShipClasses")
		lShips = []
		for sShip in self.GetShips():
			lShips.append(sShip)
		for sBase in self.GetBases():
			lShips.append(sBase)
		return lShips

	def ContainsShip(self, shipScript):
		debug(__name__ + ", ContainsShip")
		for ship in self.myShips:
			if ship == shipScript:
				return 1
		for base in self.myBases:
			if base == shipScript:
				return 1
		return 0

	def AddEscort(self, Name, Escort):
		debug(__name__ + ", AddEscort")
		if not self.myEscorts.has_key(Name):
			self.myEscorts[Name] = []
		self.myEscorts[Name].append(Escort)
		
	def GetEscort(self, Name):
		debug(__name__ + ", GetEscort")
		if not self.myEscorts.has_key(Name):
			return None
		return self.myEscorts[Name]
	
	def GetEscorts(self, name):
		debug(__name__ + ", GetEscorts")
		return self.GetEscort(name)
		
	def SetPeaceValue(self, Num):
		debug(__name__ + ", SetPeaceValue")
		self.peaceVal = Num
        
	def GetPeaceValue(self):
		debug(__name__ + ", GetPeaceValue")
		return self.peaceVal

	def BuildShip(self, sShipType):
		debug(__name__ + ", BuildShip")
		self.BuildShips[sShipType] = self.NumFreeShips(sShipType) + 1
			
	def NumFreeShips(self, sShipType):
		debug(__name__ + ", NumFreeShips")
		iNum = 0
		if self.BuildShips.has_key(sShipType):
			iNum = self.BuildShips[sShipType]
		return iNum

	def SetNumFreeShips(self, sShipType, iNum):	
		debug(__name__ + ", SetNumFreeShips")
		self.BuildShips[sShipType] = iNum

	def BuildShipToPlayerShip(self, sShipType):
		debug(__name__ + ", BuildShipToPlayerShip")
		self.BuildShips[sShipType] = self.NumFreeShips(sShipType) - 1
		if self.NumFreeShips(sShipType) < 0:
			self.BuildShips[sShipType] = 0

	def AddResource(self, sResource, fAmount):
		debug(__name__ + ", AddResource")
		if not self.dResources.has_key(sResource):
			self.dResources[sResource] = fAmount
		else:
			self.dResources[sResource] = self.dResources[sResource] + fAmount

	# return: the amount of resources really removed
	def RemoveResource(self, sResource, fAmount):
		debug(__name__ + ", RemoveResource")
		if not self.dResources.has_key(sResource):
			return 0.0
		
		# we have enough
		if fAmount <= self.dResources[sResource]:
			self.dResources[sResource] = self.dResources[sResource] - fAmount
			return fAmount
		
		# we do not have enough
		fAmount = self.dResources[sResource]
		self.dResources[sResource] = 0.0
		return fAmount

	def AddSystem(self, sSystemName):
		debug(__name__ + ", AddSystem")
		pass

	def RemoveSystem(self, sSystemName):
		debug(__name__ + ", RemoveSystem")
		pass

	def GetSystems(self):
		debug(__name__ + ", GetSystems")
		lAllRegions = App.g_kRegionManager.GetAllRegions()
		lRegions = []
		for pRegion in lAllRegions:
			if pRegion.GetControllingEmpire() == self.Name:
				lRegions.append(pRegion)
		return lRegions

	def GetTotalEconomyProduction(self):
		debug(__name__ + ", GetTotalEconomyProduction")
		lSystems = self.GetSystems()
		fTotal = 0.0
		for pSystem in lSystems:
			fTotal = fTotal + pSystem.GetTotalEconomy()
		return fTotal
	def GetTotalDefenceValue(self):
		debug(__name__ + ", GetTotalDefenceValue")
		lSystems = self.GetSystems()
		fTotal = 0.0
		for pSystem in lSystems:
			fTotal = fTotal + pSystem.GetTotalDefaultDefence()
		return fTotal
	def GetTotalStrategicValue(self):
		debug(__name__ + ", GetTotalStrategicValue")
		lSystems = self.GetSystems()
		fTotal = 0.0
		for pSystem in lSystems:
			fTotal = fTotal + pSystem.GetTotalStrategicValue()
		return fTotal
	def AddFunds(self, fAmount):
		debug(__name__ + ", AddFunds")
		self.AddResource("WarFunds", fAmount)
		try:
			import Custom.GalaxyCharts.GalacticWarSimulator
			WarSim = Custom.GalaxyCharts.GalacticWarSimulator.WarSimulator
			sPlaName = WarSim.sPlayerName
			pWSPla = WarSim.GetWSShipObjForName(sPlaName)
			if pWSPla.Race.GetRaceName() == self.GetRaceName():
				WarSim.dStats["FundsAcquired"] = WarSim.dStats["FundsAcquired"] + fAmount
		except:
			pass
	def DeductFunds(self, fAmount):
		debug(__name__ + ", DeductFunds")
		self.RemoveResource("WarFunds", fAmount)
		try:
			import Custom.GalaxyCharts.GalacticWarSimulator
			WarSim = Custom.GalaxyCharts.GalacticWarSimulator.WarSimulator
			sPlaName = WarSim.sPlayerName
			pWSPla = WarSim.GetWSShipObjForName(sPlaName)
			if pWSPla.Race.GetRaceName() == self.GetRaceName():
				WarSim.dStats["FundsSpent"] = WarSim.dStats["FundsSpent"] + fAmount
		except:
			pass
	def GetTotalFunds(self):
		debug(__name__ + ", GetTotalFunds")
		if self.dResources.has_key("WarFunds"):
			return self.dResources["WarFunds"]
		else:
			return 0.0
	def AddWSShip(self, pWSShip):
		debug(__name__ + ", AddWSShip")
		if pWSShip.Race == None:
			return
		if pWSShip.Race.GetRaceName() != self.GetRaceName():
			return
		sShipName = pWSShip.GetShipName()
		self.dWSShips[sShipName] = pWSShip
		if not sShipName in self.lShipNames:
			self.lShipNames.append(sShipName)
	def DeleteWSShip(self, pWSShip):
		debug(__name__ + ", DeleteWSShip")
		if pWSShip.Race == None:
			return
		if pWSShip.Race.GetRaceName() != self.GetRaceName():
			return
		if self.dWSShips.has_key(pWSShip.GetShipName()) == 1:
			del self.dWSShips[pWSShip.GetShipName()]
