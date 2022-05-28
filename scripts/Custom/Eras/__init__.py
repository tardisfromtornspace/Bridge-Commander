from bcdebug import debug
##############################################################################################################
# ERA  PLUGIN  SYSTEM 
#                    by USS Frontier
##############################################################################################################
# This is the __init__ script of the Eras folder, which contains each Era plugin script.
# This handles loading up all of the era plugins, while the actual selection of era will happen with UMM
##############################################################################################################
import App
import nt
import string
import MissionLib

import Custom.Systems.PluginUtils
from Custom.GalaxyCharts.GalaxyLIB import *
import Custom.GalaxyCharts.Cartographer


dEraPlugins = {}
bLoadedPlugins = 0
pSelectedEra = None

def LoadEraPlugins():
	debug(__name__ + ", LoadEraPlugins")
	global dEraPlugins, bLoadedPlugins, pSelectedEra
	if bLoadedPlugins == 1:
		return

	EraList = nt.listdir('scripts/Custom/Eras')

	lToBeRemoved = ['__init__.py', '__init__.pyc']
	for sRemovee in lToBeRemoved:
		if sRemovee in EraList:
			EraList.remove(sRemovee)

	lCreatedEraPlugins = []

	for sFile in EraList:
		sFileStrings = string.split(sFile, '.')
		sPlugin = sFileStrings[0]
		sExt = sFileStrings[-1]
		if (sExt == "py" or sExt == "pyc") and (not sPlugin in lCreatedEraPlugins):
			lCreatedEraPlugins.append(sPlugin)
			pModule = __import__("Custom.Eras." + sPlugin)
			pEra = EraPlugin(pModule)
			dEraPlugins[pEra.GetName()] = pEra

	bLoadedPlugins = 1
	return

def IsLoaded():	return bLoadedPlugins

def GetEraPlugin(sName):
	debug(__name__ + ", GetEraPlugin")
	if dEraPlugins.has_key(sName):
		return dEraPlugins[sName]
	else:
		return None

def GetAllEraPlugins():
	debug(__name__ + ", GetAllEraPlugins")
	return dEraPlugins.values()

def GetSelectedEraPlugin():
	debug(__name__ + ", GetSelectedEraPlugin")
	global pSelectedEra
	return pSelectedEra

def GetDefaultEraPlugin():
	debug(__name__ + ", GetDefaultEraPlugin")
	return GetEraPlugin(GetDefaultEraName())

def GetDefaultEraName():
	debug(__name__ + ", GetDefaultEraName")
	return "Late Dominion Wars"

def SetSelectedEraPlugin(sName):
	debug(__name__ + ", SetSelectedEraPlugin")
	global pSelectedEra
	pEra = GetEraPlugin(sName)
	if pEra == None:
		print "Era Plugin System Error: tried to set non-existant era", sName, " as selected era..."
		return
	if pSelectedEra != None:
		if pSelectedEra.GetName() == sName:
			# trying to set the same era again...
			return
		pSelectedEra.RestoreOriginalValues()
	pEra.ApplyEraValues()
	pSelectedEra = pEra
	

# Little class to hold the info of a Era plugin.
class EraPlugin:
	def __init__(self, pEraPlug):
		debug(__name__ + ", __init__")
		self.CLASS = "Era Plugin Class"
		self.ID = GetUniqueID(pEraPlug.Name+"_EraPlugin")
		#self.__dict__ = pRegionPlug.__dict__
		self.Name = pEraPlug.Name
		self.Description = pEraPlug.Description
		self.InitialStardate = pEraPlug.StardateRange[0]
		self.EndingStardate = pEraPlug.StardateRange[1]
		self.RaceChanges = pEraPlug.RaceInfo
		self.SystemChanges = pEraPlug.SystemInfo
		self.__acquiredBackup = 0
		self.backRaceChanges = {}
		self.backSystemChanges = {}
		self.AcquireBackup()

	def GetName(self):	return self.Name
	def __repr__(self):	return "<"+self.ID+">"
	def GetDescriptionLines(self):
		debug(__name__ + ", GetDescriptionLines")
		return self.Description
	def GetDescriptionString(self):
		debug(__name__ + ", GetDescriptionString")
		ret = ""
		for s in self.Description:
			ret = ret + s + "\n"
		ret = ret[0:len(ret)-1]
		return ret
	def GetInitialStardate(self): return self.InitialStardate
	def GetEndingStardate(self):	return self.EndingStardate

	def AcquireBackup(self):
		# acquire and store the original values for the attributes this era will overwrite.
		## yeah well, this is pretty fucking nasty right now  >_<
		debug(__name__ + ", AcquireBackup")
		if self.__acquiredBackup == 0:
			##### acquire race values #####
			# start by looping thru each race
			lRaceKeys = self.RaceChanges.keys()
			for sRace in lRaceKeys:
				pRaceObj = GetRaceClassObj(sRace)
				if pRaceObj != None:
					# now that we got the race, loop thru each attribute we'll change.
					lAttrKeys = self.RaceChanges[sRace].keys()
					if len(lAttrKeys) >= 1:
						self.backRaceChanges[sRace] = {}
						for sAttr in lAttrKeys:
							try:
								self.backRaceChanges[sRace][sAttr] = pRaceObj.__dict__[sAttr]
							except:
								print "Era Plugin "+self.Name+" Error: Couldn't acquire attribute", sAttr, " for race", sRace
					else:
						print "Era Plugin "+self.Name+" Error: not trying to overwrite any attribute of race", sRace 
				else:
					print "Era Plugin "+self.Name+" Error: race", sRace, " does not exist..."
			
			##### acquire system values #####
			# also start by looping thru each region we'll change
			lSystemKeys = self.SystemChanges.keys()
			for sRegion in lSystemKeys:
				pRegion = App.g_kRegionManager.GetRegion(sRegion)
				if pRegion != None:
					# now that we got the region, loop thru each attribute we'll change.
					lAttrKeys = self.SystemChanges[sRegion].keys()
					if len(lAttrKeys) >= 1:
						self.backSystemChanges[sRegion] = {}
						for sAttr in lAttrKeys:
							if sAttr == "Sets":
								# okay this era changes some sets of this region as well.
								# loop thru each one
								lSetsKeys = self.SystemChanges[sRegion]["Sets"].keys()
								if len(lSetsKeys) >= 1:
									self.backSystemChanges[sRegion]["Sets"] = {}
									for sSet in lSetsKeys:
										pSetObj = pRegion.GetSet(sSet)
										if pSetObj != None:
											# and now finally loop thru each attribute of this set that
											# we'll change
											lSetAttrKeys = self.SystemChanges[sRegion]["Sets"][sSet].keys()
											if len(lSetAttrKeys) >= 1:
												self.backSystemChanges[sRegion]["Sets"][sSet] = {}
												for sSetAttr in lSetAttrKeys:
													try:
														self.backSystemChanges[sRegion]["Sets"][sSet][sSetAttr] = pSetObj.__dict__[sSetAttr]
													except:
														print "Era Plugin "+self.Name+" Error: Couldn't acquire attribute", sSetAttr, " for set", sSet
											else:
												print "Era Plugin "+self.Name+" Error: trying to overwrite 0 attributes of set", sSet, " of system", sRegion
										else:
											print "Era Plugin "+self.Name+" Error: set", sSet, " in system", sRegion, " does not exist..."
								else:
									print "Era Plugin "+self.Name+" Error: trying to overwrite 0 sets of system", sRegion
							else:
								try:
									self.backSystemChanges[sRegion][sAttr] = pRegion.__dict__[sAttr]
								except:
									print "Era Plugin "+self.Name+" Error: Couldn't acquire attribute", sAttr, " for region", sRegion
					else:
						print "Era Plugin "+self.Name+" Error: not trying to overwrite any attribute of system", sRegion
				else:
					print "Era Plugin "+self.Name+" Error: system", sRegion, " does not exist..."

			self.__acquiredBackup = 1

	def ApplyEraValues(self):
		debug(__name__ + ", ApplyEraValues")
		self.__applyValues(self.RaceChanges, self.SystemChanges)
	def RestoreOriginalValues(self):
		debug(__name__ + ", RestoreOriginalValues")
		self.__applyValues(self.backRaceChanges, self.backSystemChanges)
	def __applyValues(self, raceValues, systemValues):
		# this method will apply the given race/system values to the game, overwriting the race/system plugins.
		debug(__name__ + ", __applyValues")
		if self.__acquiredBackup == 1:
			##### apply race values #####
			# start by looping thru each race
			lRaceKeys = raceValues.keys()
			for sRace in lRaceKeys:
				pRaceObj = GetRaceClassObj(sRace)
				if pRaceObj != None:
					# now that we got the race, loop thru each attribute we'll change.
					lAttrKeys = raceValues[sRace].keys()
					if len(lAttrKeys) >= 1:
						for sAttr in lAttrKeys:
							try:
								pRaceObj.__dict__[sAttr] = raceValues[sRace][sAttr]
							except:
								print "Era Plugin "+self.Name+" Error (Applying): Couldn't apply attribute", sAttr, " for race", sRace
					else:
						print "Era Plugin "+self.Name+" Error (Applying): not trying to overwrite any attribute of race", sRace 
				else:
					print "Era Plugin "+self.Name+" Error (Applying): race", sRace, " does not exist..."
			
			##### apply system values #####
			# also start by looping thru each region we'll change
			lSystemKeys = systemValues.keys()
			for sRegion in lSystemKeys:
				pRegion = App.g_kRegionManager.GetRegion(sRegion)
				if pRegion != None:
					# now that we got the region, loop thru each attribute we'll change.
					lAttrKeys = systemValues[sRegion].keys()
					if len(lAttrKeys) >= 1:
						for sAttr in lAttrKeys:
							if sAttr == "Sets":
								# okay this era changes some sets of this region as well.
								# loop thru each one
								lSetsKeys = systemValues[sRegion]["Sets"].keys()
								if len(lSetsKeys) >= 1:
									for sSet in lSetsKeys:
										pSetObj = pRegion.GetSet(sSet)
										if pSetObj != None:
											# and now finally loop thru each attribute of this set that
											# we'll change
											lSetAttrKeys = systemValues[sRegion]["Sets"][sSet].keys()
											if len(lSetAttrKeys) >= 1:
												for sSetAttr in lSetAttrKeys:
													try:
														pSetObj.__dict__[sSetAttr] = systemValues[sRegion]["Sets"][sSet][sSetAttr]
													except:
														print "Era Plugin "+self.Name+" Error (Applying): Couldn't apply attribute", sSetAttr, " for set", sSet
											else:
												print "Era Plugin "+self.Name+" Error (Applying): trying to overwrite 0 attributes of set", sSet, " of system", sRegion
										else:
											print "Era Plugin "+self.Name+" Error (Applying): set", sSet, " in system", sRegion, " does not exist..."
								else:
									print "Era Plugin "+self.Name+" Error (Applying): trying to overwrite 0 sets of system", sRegion
							else:
								try:
									pRegion.__dict__[sAttr] = systemValues[sRegion][sAttr]
								except:
									print "Era Plugin "+self.Name+" Error (Applying): Couldn't apply attribute", sAttr, " for region", sRegion
					else:
						print "Era Plugin "+self.Name+" Error (Applying): not trying to overwrite any attribute of system", sRegion
				else:
					print "Era Plugin "+self.Name+" Error (Applying): system", sRegion, " does not exist..."
	#############################################################################################


#########
#  finally, call LoadEraPlugins() ...  That way this script will automaticaly load the plugins when imported
#  thus, we have no need in having another script call the LoadEraPlugins function
LoadEraPlugins()
