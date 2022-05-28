from bcdebug import debug
##############################################################################################################
# PluginUtils.py 
#                    by USS Frontier
##############################################################################################################
# Handles loading the regions plugins and the set plugins, creating a database of the values, thus creating
# what I like to call a system plugin.
#  This will most likely be used by Galaxy Charts and New Frontier
##############################################################################################################
import App
import nt
import string
from Custom.GalaxyCharts.GalaxyLIB import *
import Custom.GalaxyCharts.Cartographer


NonSerializedObjects = (
"dSystemPlugins",
"bLoadedPlugins",
)

dSystemPlugins = {}
bLoadedPlugins = 0

def LoadSystemPlugins():
	debug(__name__ + ", LoadSystemPlugins")
	global dSystemPlugins, bLoadedPlugins
	if bLoadedPlugins == 1:
		return

	RegionList = nt.listdir('scripts/Custom/Systems/Regions')
	SetsList = nt.listdir('scripts/Custom/Systems/Sets')

	lToBeRemoved = ['__init__.py', '__init__.pyc']
	for sRemovee in lToBeRemoved:
		if sRemovee in RegionList:
			RegionList.remove(sRemovee)
		if sRemovee in SetsList:
			SetsList.remove(sRemovee)

	lCreatedRegPlugins = []
	lCreatedSetPlugins = []
	dSets = {}

	for sFile in SetsList:
		sFileStrings = string.split(sFile, '.')
		sPlugin = sFileStrings[0]
		sExt = sFileStrings[-1]
		if (sExt == "py" or sExt == "pyc") and (not sPlugin in lCreatedSetPlugins):
			lCreatedSetPlugins.append(sPlugin)
			pModule = __import__("Custom.Systems.Sets." + sPlugin)
			pSet = SetPlugin(pModule)
			dSets[pSet.GetScriptFile()] = pSet

	for sFile in RegionList:
		sFileStrings = string.split(sFile, '.')
		sPlugin = sFileStrings[0]
		sExt = sFileStrings[-1]
		if (sExt == "py" or sExt == "pyc") and (not sPlugin in lCreatedRegPlugins):
			lCreatedRegPlugins.append(sPlugin)
			pModule = __import__("Custom.Systems.Regions." + sPlugin)
			lSystemFiles = pModule.SystemsFiles
			lSets = []
			for sSystemFile in lSystemFiles:
				if dSets.has_key(sSystemFile):
					lSets.append(dSets[sSystemFile])
			pSystem = SystemPlugin(pModule, lSets)
			#####
			# now check if the border set exists. If it doesn't, do not continue with the loading of this system plugin.
			bIsOK = 1
			if pSystem.BorderSet != None:
				sBorderScript = pSystem.BorderSet.GetScriptFile()
				try:
					pBSS = __import__(sBorderScript)
				except:
					pBSS = None
				if pBSS == None:
					bIsOK = 0
			else:
				bIsOK = 0
			#####
			if bIsOK == 1:
				dSystemPlugins[pSystem.GetName()] = pSystem
				if hasattr(App, "g_kRegionManager"):
					pRegion = App.g_kRegionManager.GetRegion(pSystem.GetName())
					if pRegion == None:
						App.g_kRegionManager.AddRegionBySystemPlugin(pSystem)
					else:
						pRegion.AddSystemPluginInfo(pSystem, pSystem.GetAllSets())
				else:
					print "System PluginUtils: Couldn't find the Region Manager..."

	bLoadedPlugins = 1
	return

def IsLoaded():	return bLoadedPlugins

def GetSystemPlugin(sName):
	debug(__name__ + ", GetSystemPlugin")
	if dSystemPlugins.has_key(sName):
		return dSystemPlugins[sName]
	else:
		return None

def GetAllSystemPlugins():
	debug(__name__ + ", GetAllSystemPlugins")
	return dSystemPlugins.values()


# A little more complex than the SetPlugin class, to hold a Region plugin's info, and her SetPlugins as well.
# use SystemPlugin.Get*   to get any of the region plugin's values.
#   with * being the name of any of the region plugin's attributes names.
class SystemPlugin:
	def __init__(self, pRegionPlug, lSetsPlugs):
		debug(__name__ + ", __init__")
		self.__dict__ = pRegionPlug.__dict__
		if not self.__dict__.has_key("IgnoreRDF"):
			self.IgnoreRDF = 0
		if not self.__dict__.has_key("RestrictedFor"):
			self.RestrictedFor = []
		if not self.__dict__.has_key("OnlyByRestrictedMethods"):
			self.OnlyByRestrictedMethods = 0
		lPos = self.Location
		self.Location = App.NiPoint2(lPos[0], lPos[1])
		self.CLASS = "System Plugin Class"
		self.__ID = GetUniqueID(pRegionPlug.Name+"_SystemPlugin")
		self.Sets = []
		self.BorderSet = None
		for pSetPlug in lSetsPlugs:
			if pSetPlug.ScriptFile in self.SystemsFiles:
				self.Sets.append(pSetPlug)
				pSetPlug.ParentRegion = self
			if pSetPlug.ScriptFile == self.SystemsFiles[0] and self.BorderSet == None:
				self.BorderSet = pSetPlug

	##### non-region plugin related methods  #####
	def __repr__(self):	return "<"+self.__ID+">"
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
	def GetRegionObj(self):
		debug(__name__ + ", GetRegionObj")
		try:
			return App.g_kRegionManager.GetRegion(self.GetName())
		except:
			return None
	def GetAttribute(self, sName):
		debug(__name__ + ", GetAttribute")
		if self.__dict__.has_key(sName):
			return self.__dict__[sName]
		else:
			return None

	##### region plugin related methods  #####

	# General Region Plugin Info  get functions
	def GetName(self):	return self.Name
	def GetControllingEmpire(self):	return self.ControllingEmpire
	def GetSectorNumber(self):	return self.SectorNumber
	def GetImagePath(self):	return self.ImagePath
	def GetType(self):	return self.Type
	def GetLocation(self):	return self.Location
	def GetOnlyInQB(self):	return self.OnlyInQB
	def GetOnlyMult(self):	return self.OnlyMult
	def GetIgnoreRDF(self):	return self.IgnoreRDF
	def GetRestrictedFor(self):	return self.RestrictedFor
	def GetOnlyByRestrictedMethods(self):	return self.OnlyByRestrictedMethods
	def GetSystemsFiles(self):	return self.SystemsFiles
	def GetDescription(self):	return self.Description

# This class represents a Set Plugin.
# use SetPlugin.Get*   to get any of the set plugin's values.
#   with * being the name of any of the set plugin's attributes names.
class SetPlugin:
	debug(__name__ + ", GetDescription")
	def __init__(self, pSetPlugin):
		debug(__name__ + ", __init__")
		self.__dict__ = pSetPlugin.__dict__
		self.CLASS = "Set Plugin Class"
		self.__ID = GetUniqueID(pSetPlugin.Name+"_SetPlugin")
		self.ParentRegion = None
		self.warsimSetStarbase = ""
		if not self.__dict__.has_key("NativeShipNames"):
			self.NativeShipNames = []

	##### non-set plugin file related methods #####
	def GetParentRegion(self):	return self.ParentRegion
	def __repr__(self):	return "<"+self.__ID+">"
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def GetSetObj(self, bInitialize = 0):
		debug(__name__ + ", GetSetObj")
		try:
			pSetScript = __import__(self.GetScriptFile())
			pSet = pSetScript.GetSet()
			if bInitialize == 1 and pSet == None:
				pSetScript.Initialize()
				pSet = pSetScript.GetSet()
			return pSet
		except:
			return None
	def GetAttribute(self, sName):
		debug(__name__ + ", GetAttribute")
		if self.__dict__.has_key(sName):
			return self.__dict__[sName]
		else:
			return None
	def GetStarbaseName(self):
		debug(__name__ + ", GetStarbaseName")
		return self.warsimSetStarbase
	def SetStarbaseName(self, name):
		# do safety checks: see if this set already has a base
		debug(__name__ + ", SetStarbaseName")
		if self.warsimSetStarbase != "" and self.GetStarbaseObj() != None:
			print "Warning: tried to set the starbase name of set", self.GetName(), "without properly deleting the previous starbase from this set."
		self.warsimSetStarbase = name
	def RemoveStarbaseName(self):
		#probably gonna need more stuff here
		debug(__name__ + ", RemoveStarbaseName")
		self.warsimSetStarbase = ""
	def GetStarbaseObj(self):
		#debug(__name__ + ", GetStarbaseObj")
		debug(__name__ + ", GetStarbaseObj")
		pStarbase = None
		if self.warsimSetStarbase != "" and self.GetSetObj() != None:
			pStarbase = App.ShipClass_Cast(App.ObjectClass_GetObject(self.GetSetObj(), self.warsimSetStarbase))
		return pStarbase

	def GetEconomy(self):
		#debug(__name__ + ", GetEconomy")
		debug(__name__ + ", GetEconomy")
		fValue = self.Economy
		pBase = self.GetStarbaseObj()
		if pBase != None:
			fBaseCost = GetShipClassFundCost( GetShipType(pBase) )
			fValue = fValue + ( fBaseCost/App.g_kRegionManager.fEconomyPointCost )
		return fValue
	def GetStrategicValue(self):
		debug(__name__ + ", GetStrategicValue")
		fValue = self.StrategicValue
		pBase = self.GetStarbaseObj()
		if pBase != None:
			fBaseCost = GetShipClassFundCost( GetShipType(pBase) )
			fValue = fValue + ( fBaseCost/App.g_kRegionManager.fStrategicPointCost )
		return fValue
	def GetDefaultDefence(self):
		debug(__name__ + ", GetDefaultDefence")
		fValue = self.DefaultDefence
		pBase = self.GetStarbaseObj()
		if pBase != None:
			fBaseCost = GetShipClassFundCost( GetShipType(pBase) )
			fValue = fValue + ( fBaseCost/App.g_kRegionManager.fDefencePointCost )
		return fValue

	##### set plugin file related methods #####

	# General Set Plugin Info   get functions
	def GetName(self):	return self.Name
	def GetAlternateName(self):	return self.AltName
	def GetAltName(self):	return self.AltName
	def GetScriptFile(self):	return self.ScriptFile
	def GetDescription(self):	return self.Description
	def GetBiographical(self):	return self.Biographical
	def GetNativeShipNamesList(self):	return self.NativeShipNames

	# Radiation Set Plugin info   get functions
	def GetChronitonRadiation(self):	return self.ChronitonRadiation
	def GetCosmicRadiation(self):	return self.CosmicRadiation
	def GetDeltaRadiation(self):	return self.DeltaRadiation
	def GetEMRadiation(self):	return self.EMRadiation
	def GetGammaRadiation(self):	return self.GammaRadiation
	def GetHyperonicRadiation(self):	return self.HyperonicRadiation
	def GetKinoplasmicRadiation(self):	return self.KinoplasmicRadiation
	def GetThalaronRadiation(self):	return self.ThalaronRadiation
	def GetThetaRadiation(self):	return self.ThetaRadiation
	def GetMetaphasicRadiation(self):	return self.MetaphasicRadiation
	def GetOmicronRadiation(self):	return self.OmicronRadiation
	def GetPlasmaRadiation(self):	return self.PlasmaRadiation
	def GetPolaricRadiation(self):	return self.PolaricRadiation
	def GetSubnucleonicRadiation(self):	return self.SubnucleonicRadiation
	def GetSubspaceRadiation(self):	return self.SubspaceRadiation
	def GetTemporalRadiation(self):	return self.TemporalRadiation
	def GetThermionicRadiation(self):	return self.ThermionicRadiation
	def GetThoronRadiation(self):	return self.ThoronRadiation

	# Particles Set Plugin info   get functions
	def GetAntiProtons(self):	return self.AntiProtons
	def GetAntiNeutrinos(self):	return self.AntiNeutrinos
	def GetAntiGravitons(self):	return self.AntiGravitons
	def GetDarkMatter(self):	return self.DarkMatter
	def GetDuderons(self):	return self.Duderons
	def GetMetreons(self):	return self.Metreons
	def GetGravitons(self):	return self.Gravitons
	def GetOmega(self):	return self.Omega
	def GetPolarons(self):	return self.Polarons
	def GetPositrons(self):	return self.Positrons
	def GetTetryons(self):	return self.Tetryons
	def GetVerterons(self):	return self.Verterons
	def GetMesons(self):	return self.Mesons
	def GetNeutrinos(self):	return self.Neutrinos

	# Sole General Particle/Radiation  get function
	## parameter: GetRadiationValue: radiation name (possibly without the "Radiation" at the end of the name
	##            GetParticleValue: particle name
	## NOTE: the radiation/particle name should be the same name as it is in the plugin files.
	def GetParticleValue(self, sParticleName):
		debug(__name__ + ", GetParticleValue")
		if self.__dict__.has_key(sParticleName):
			return self.__dict__[sParticleName]
		else:
			return None
	def GetRadiationValue(self, sRadiationName):
		debug(__name__ + ", GetRadiationValue")
		if self.__dict__.has_key(sRadiationName):
			return self.__dict__[sRadiationName]
		else:
			sRadName = sRadiationName + "Radiation"
			if self.__dict__.has_key(sRadName):
				return self.__dict__[sRadName]
			else:
				return None
	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		return self.__dict__
	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		#self.__dict__ == dict

#########
#  finally, call LoadSystemPlugins() ...  That way this script will automaticaly load the plugins when imported
#  thus, we have no need in having another script call the LoadSystemPlugins function
#LoadSystemPlugins()
