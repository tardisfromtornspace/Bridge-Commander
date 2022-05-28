from bcdebug import debug
########################################################################################################
#  Cartographer.py
#               by Fernando Aluani, aka USS Frontier
########################################################################################################
# This is the script which handles the task of creating/handling BC regions. It contains the Region class, extremely 
# important, the RegionManager, the CreateSystemMenu override, and a few methods which are put in App
#####
# -App.SetClass.GetLocation()
#	- this returns the location of the set in the galaxy, it's a NiPoint2 object, ranging from -100000 to 100000 in both
#	  axis
#	- it returns DEFAULT if the location of set wasn't set.
# -App.SetClass.SetLocation(x, y)
#	- this sets the X and Y location of the set in the galaxy. It can be any value, but it'll be lowered or increased to 
#	  remain in the -50000 to 50000 range.
# -NOTE that these positions are set in lightyears, relative to the galactic core. So (0,0) is the exact galatic core,
#  while something like (50000,0) would be in the border of the galaxy.
# -NOTE to Myself and others: The Milky Way galaxy, ours and Star Trek's galaxy that is, is 100000 light years in diameter
########################################################################################################
import App
import string
import Galaxy
import GalaxyLIB
import GalacticWarSimulator
import Systems.Utils

NonSerializedObjects = (
"RegionManager",
)

# class which contains all the info about a region and it's contained sets.
# can be used alone, but if the plugin info is added there will be a lot more data in it.
# i know i should do something to make the SystemPlugin class and this one be just a single class or one which inherits
# from the other, but i'm not in the mood to try that, plus i can't see a reason why not do it this way.
class Region:
	fStrategicLimit = 1000.0
	fEconomyLimit = 1000.0	
	fDefaultDefenceLimit = 1000.0
	iDefShipLimit = 10

	def __init__(self, sSystemName, sSystemRegion, lSystems, pMenu):
		debug(__name__ + ", __init__")
		self.Name = sSystemName         # Name of the system in the Set Course menu
		if lSystems == None:
			lSystems = []
		lSystems = list(lSystems)
		if not sSystemRegion in lSystems:
			lSystems.append(sSystemRegion)
		self.Region = sSystemRegion     # Name region module that you go to. (System Border, like Belaruz 4, of Belaruz1,2,3,4)
		self.Systems = lSystems         # List of the region modules of this region
		self.Menu = pMenu               # App.SortedRegionMenu object, region menu in Set Course menu.
		self.Location = None            # Location of the region in the galaxy.
		self.CLASS = "Region"
		self.__ID = GalaxyLIB.GetUniqueID(sSystemName+"Region")
		self.ControllingEmpire = "Unknown"
		self.SectorNumber = 0
		self.ImagePath = ""
		self.Type = "Unknown"
		self.OnlyInQB = 0
		self.OnlyMult = 0
		self.IgnoreRDF = 0
		self.RestrictedFor = []
		self.OnlyByRestrictedMethods = 0
		self.SystemsFiles = self.Systems
		self.Description = "no description found..."
		self.BorderSet = None
		self.Sets = []
		self.__nDefensiveShips = 0	
		self.RegionBattle = GalacticWarSimulator.RegionBattle(self)    # Class instance used by the War Simulation.
	def SetLocation(self, x, y):
		debug(__name__ + ", SetLocation")
		vPos = App.NiPoint2(x, y)
		fLen = vPos.Length()
		fGalaxyRadius = 50000.0
		if fLen > fGalaxyRadius:
			vPos.x = vPos.x/(fLen/fGalaxyRadius)
			vPos.y = vPos.y/(fLen/fGalaxyRadius)
		self.Location = vPos
	def GetLocation(self):
		debug(__name__ + ", GetLocation")
		if self.Location == None and (self.Name == "SpaceSet" or self.Name == "TravelSet" or self.Name == "AITravelSet" or self.IsAISpaceSet() == 1):
			return "DEFAULT"
		if self.Location == None:
			SetRandomLocationForRegion(self)
		return App.NiPoint2(self.Location.x, self.Location.y)
	def GetDistanceBetweenSystems(self, sSystemModule1, sSystemModule2):
		# ship is warping in the same set, from one planet to another (example: Belaruz 4 to Belaruz 3)
		# set a static distance then. This distance should make the ship take 3 seconds to reach it at warp 9.99
		# these 3 seconds(at warp 9.99) it should take to go from the 4º set to the 3º set, so going from the 4º to
		# the 2º would actually take 2 times more to go.
		debug(__name__ + ", GetDistanceBetweenSystems")
		n1 = None
		n2 = None
		index = 0
		for eleSys in self.Systems:
			if eleSys == sSystemModule1:
				n1 = index
			if eleSys == sSystemModule2:
				n2 = index
			index = index + 1
		diff = n1-n2
		dist = (9.99*3)*diff
		if dist <0:
			dist = -dist
		return dist
	def GetModuleOfSystem(self, sSystemSetName):
		debug(__name__ + ", GetModuleOfSystem")
		for sSystem in self.Systems:
			sName = string.split(sSystem, ".")[-1]
			if sName == sSystemSetName:
				return sSystem
	def HasSystem(self, sSystemModule):
		#debug(__name__ + ", HasSystem")
		if sSystemModule in self.Systems:
			return 1
		else:
			return 0
	def IsAISpaceSet(self):
		debug(__name__ + ", IsAISpaceSet")
		ls = string.split(self.Region, ".")
		name = ls[-1]
		ls.remove(name)
		path = string.join(ls, ".")
		if path == "Custom.GalaxyCharts.TravelerSystems.AI_SpaceSets":
			return 1
		else:
			return 0
	
	def AddSystemPluginInfo(self, pRegionPlug, lSetsPlugs):
		debug(__name__ + ", AddSystemPluginInfo")
		if pRegionPlug.Name != self.Name:
			return
		self.ControllingEmpire = pRegionPlug.ControllingEmpire 
		self.SectorNumber = pRegionPlug.SectorNumber
		self.ImagePath = pRegionPlug.ImagePath
		self.Type = pRegionPlug.Type
		self.OnlyInQB = pRegionPlug.OnlyInQB
		self.OnlyMult = pRegionPlug.OnlyMult
		self.IgnoreRDF = pRegionPlug.IgnoreRDF
		self.RestrictedFor = pRegionPlug.RestrictedFor
		self.OnlyByRestrictedMethods = pRegionPlug.OnlyByRestrictedMethods
		self.SystemsFiles = pRegionPlug.SystemsFiles
		self.Description = pRegionPlug.Description
		self.BorderSet = None
		self.Sets = []
		self.Location = pRegionPlug.Location
		if GalaxyLIB.GetConfigValue("UseDefaultLocs") == 1:
			if type(self.Location) == type([]):
				lPos = self.Location
				self.SetLocation(lPos[0], lPos[1])
			self.SetLocation(self.Location.x, self.Location.y)
		else:
			SetRandomLocationForRegion(self)
		self.Systems = self.SystemsFiles
		for pSetPlug in lSetsPlugs:
			if pSetPlug.ScriptFile in self.SystemsFiles:
				self.Sets.append(pSetPlug)
				pSetPlug.ParentRegion = self
			if pSetPlug.ScriptFile == self.SystemsFiles[0] and self.BorderSet == None:
				self.BorderSet = pSetPlug
		self.Region = self.BorderSet.GetScriptFile()
		self.AddDefenseShipAmount(self.GetTotalDefaultDefence())
	def GetBorderSet(self):	return self.BorderSet
	def GetAllSets(self):	return self.Sets
	def GetSet(self, sName):
		debug(__name__ + ", GetSet")
		for pSet in self.Sets:
			if pSet.GetName() == sName:
				return pSet
		return None
	def GetSetByModule(self, sSetModule):
		debug(__name__ + ", GetSetByModule")
		for pSet in self.Sets:
			if pSet.GetScriptFile() == sSetModule:
				return pSet
		return None
	def GetAttribute(self, sName):
		debug(__name__ + ", GetAttribute")
		if self.__dict__.has_key(sName):
			return self.__dict__[sName]
		else:
			return None
	def GetTotalEconomy(self):
		debug(__name__ + ", GetTotalEconomy")
		fRet = 0.0
		for pSet in self.Sets:
			fRet = fRet + pSet.GetEconomy()
		if fRet > Region.fEconomyLimit:
			return Region.fEconomyLimit
		return fRet
	def GetTotalStrategicValue(self):
		debug(__name__ + ", GetTotalStrategicValue")
		fRet = 0.0
		for pSet in self.Sets:
			fRet = fRet + pSet.GetStrategicValue()
		if fRet > Region.fStrategicLimit:
			return Region.fStrategicLimit
		return fRet
	def GetTotalDefaultDefence(self):
		debug(__name__ + ", GetTotalDefaultDefence")
		fRet = 0.0
		for pSet in self.Sets:
			fRet = fRet + pSet.GetDefaultDefence()
		if fRet > Region.fEconomyLimit:
			return Region.fDefaultDefenceLimit
		return fRet
	def GetNumDefensiveShips(self):	return self.__nDefensiveShips
	def AddDefenseShipAmount(self, iAmount):
		debug(__name__ + ", AddDefenseShipAmount")
		if iAmount < 0:
			iAmount = 0
		self.__nDefensiveShips = self.__nDefensiveShips + int(iAmount)
		if self.__nDefensiveShips > Region.iDefShipLimit:
			self.__nDefensiveShips = int(Region.iDefShipLimit)
	def DeductDefenseShipAmount(self, iAmount):
		debug(__name__ + ", DeductDefenseShipAmount")
		if iAmount < 0:
			iAmount = 0
		self.__nDefensiveShips = self.__nDefensiveShips - int(iAmount)
		if self.__nDefensiveShips < 0:
			self.__nDefensiveShips = 0
	def GetName(self):	return self.Name
	def GetControllingEmpire(self):	return self.ControllingEmpire
	def GetSectorNumber(self):	return self.SectorNumber
	def GetImagePath(self):	return self.ImagePath
	def GetType(self):	return self.Type
	def GetOnlyInQB(self):	return self.OnlyInQB
	def GetOnlyMult(self):	return self.OnlyMult
	def GetIgnoreRDF(self):	return self.IgnoreRDF
	def GetRestrictedFor(self):	return self.RestrictedFor
	def GetOnlyByRestrictedMethods(self):	return self.OnlyByRestrictedMethods
	def GetSystemsFiles(self):	return self.SystemsFiles
	def GetDescription(self):	return self.Description

	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.__ID+">"


class RegionManagerClass:
	fEconomyPointCost = 8000.0
	fStrategicPointCost = 6000.0
	fDefencePointCost = 4500.0

	def __init__(self):
		debug(__name__ + ", __init__")
		self.Regions = {}
		self.CLASS = "RegionManager"
		self.__ID = GalaxyLIB.GetUniqueID("RegionManager")
	def AddRegion(self, sSystemName, sSystemRegion, lSystems, pMenu):
		debug(__name__ + ", AddRegion")
		import Custom.Systems.PluginUtils
		if self.GetRegionBySystem(sSystemRegion) == None:
			region = Region(sSystemName, sSystemRegion, lSystems, pMenu)
			pSystemPlugin = Custom.Systems.PluginUtils.GetSystemPlugin(sSystemName)
			if pSystemPlugin != None:
				region.AddSystemPluginInfo(pSystemPlugin, pSystemPlugin.GetAllSets())
			self.Regions[sSystemName] = region
		else:
			region = self.GetRegionBySystem(sSystemRegion)
			if pMenu != None and region != None:
				if region.Menu == None:
					region.Menu = pMenu
				elif region.Menu.GetObjID() != pMenu.GetObjID():
					region.Menu = pMenu
		return region
	def AddRegionBySystemPlugin(self, pSystemPlugin):
		debug(__name__ + ", AddRegionBySystemPlugin")
		try:
			sSystemName = pSystemPlugin.GetName()
			if self.GetRegionBySystem(pSystemPlugin.GetBorderSet().GetScriptFile()) == None:
				sSystemRegion = pSystemPlugin.BorderSet.GetScriptFile()
				lSystems = pSystemPlugin.GetSystemsFiles()
				region = Region(sSystemName, sSystemRegion, lSystems, None)
				region.AddSystemPluginInfo(pSystemPlugin, pSystemPlugin.GetAllSets())
				self.Regions[sSystemName] = region
			else:
				region = self.GetRegionBySystem(pSystemPlugin.GetBorderSet().GetScriptFile())
				region.AddSystemPluginInfo(pSystemPlugin, pSystemPlugin.GetAllSets())
			return region
		except:
			Galaxy.LogError("RegionManager_AddRegionBySystemPlugin")
	def DeleteRegion(self, sSystemName):
		debug(__name__ + ", DeleteRegion")
		if self.HasRegion(sSystemName):
			del self.Regions[sSystemName]
	def HasRegion(self, sSystemName):
		debug(__name__ + ", HasRegion")
		if self.Regions.has_key(sSystemName):
			return 1
		else:
			return 0
	def GetRegion(self, sSystemName):
		debug(__name__ + ", GetRegion")
		if self.HasRegion(sSystemName):
			return self.Regions[sSystemName]
	def GetRegionBySystem(self, sSystemModule):
		debug(__name__ + ", GetRegionBySystem")
		lRegions = self.Regions.values()
		for region in lRegions:
			if region.HasSystem(sSystemModule):
				return region
		return None
	def GetAllRegions(self):
		debug(__name__ + ", GetAllRegions")
		return self.Regions.values()
	def DeleteAllRegions(self):
		debug(__name__ + ", DeleteAllRegions")
		self.Regions = {}
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.__ID+">"

RegionManager = RegionManagerClass()
App.g_kRegionManager = RegionManager

def CreateSystemMenu_Override(sSystemName, sSystemRegion, *lSystems):
	# Disable sorting of the menus...
	debug(__name__ + ", CreateSystemMenu_Override")
	bPaused = App.SortedRegionMenu_IsSortingPaused()
	if not bPaused:
		App.SortedRegionMenu_SetPauseSorting(1)

	# Create the menu.
	pMenu = Systems.Utils.CreateSystemMenuInternal(sSystemName, sSystemRegion, lSystems)
	
	#############
	# USS Frontier addition:
	pRegion = RegionManager.AddRegion(sSystemName, sSystemRegion, lSystems, pMenu)
	#############
	# Reenable sorting, if it was enabled before.
	if not bPaused:
		kProfiling2 = App.TGProfilingInfo("Systems.CreateMenus, Unpausing")
		App.SortedRegionMenu_SetPauseSorting(0)

	return pMenu

def SetRandomLocationForRegion(pRegion):
	debug(__name__ + ", SetRandomLocationForRegion")
	x = (App.g_kSystemWrapper.GetRandomNumber(1000)*100) - 50000
	y = (App.g_kSystemWrapper.GetRandomNumber(1000)*100) - 50000
	pRegion.SetLocation(x, y)

def GetLocationOfSet(self, sSystemName):
	debug(__name__ + ", GetLocationOfSet")
	pRegion = RegionManager.GetRegion(sSystemName)
	if pRegion:
		return pRegion.GetLocation()
	else:
		return "NOREGION"

def SetLocationOfSet(self, sSystemName, x, y):
	debug(__name__ + ", SetLocationOfSet")
	pRegion = RegionManager.GetRegion(sSystemName)
	if pRegion:
		pRegion.SetLocation(x, y)
 
###
#App.SetManager.GetLocationOfSet = GetLocationOfSet
#App.SetManager.SetLocationOfSet = SetLocationOfSet
GetLocationOfSet = None
SetLocationOfSet = None
###

def GetFullName_C(self):
	debug(__name__ + ", GetFullName_C")
	pRegion = self.GetRegion()
	if pRegion:
		return pRegion.Name
	else:
		return ""

def GetRegion_C(self):
	debug(__name__ + ", GetRegion_C")
	sScript = self.GetRegionModule()
	pRegion = RegionManager.GetRegionBySystem(sScript)
	return pRegion

App.SetClass.GetFullName = GetFullName_C
App.SetClass.GetRegion = GetRegion_C
GetFullName_C = None
GetRegion_C = None
