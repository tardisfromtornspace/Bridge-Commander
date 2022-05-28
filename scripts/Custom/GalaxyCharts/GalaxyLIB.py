from bcdebug import debug
#############################################################################################################
##
##       GalaxyLIB
##                          by Fernando Aluani  (USS Frontier)
####
## This is the library script for Galaxy Charts. Besides some new stuff, it uses much of GravityFXs lib script as well.
#############################################################################################################
import App
import Foundation
import string
import time
import MissionLib
import loadspacehelper

# Much of our functions are taken by this import
from Custom.GravityFX.GravityFXlib import *


##############################################################################
#   MethodOverrideDef  (class, inherits from Foundation.OverrideDef)
###
#  The OverrideDef from Foundation caused errors if you tried to use it to override a method of a class.
#  So I created this to allow it.
###
# name* -> the name of the override
# sModule -> the path of the module which has the class you want to overwrite
# sClass -> the name of the class you want to overwrite
# sMethod -> the name of the method of the class that you want to overwrite
# sNewItem* -> the path to your function(plus it's name) that will overwrite the given method of the given class.
# dict* -> used to pass in the MutatorDefs
###
# OBS: parameters described with an * are the same than of the Foundation.OverrideDef
###############################################################################
class MethodOverrideDef(Foundation.OverrideDef):
	def __init__(self, name, sModule, sClass, sMethod, sNewItem, dict = {}):
		debug(__name__ + ", __init__")
		sItem = sModule+"."+sClass+"."+sMethod
		self.sModule = sModule
		self.sClass = sClass
		self.sMethod = sMethod
		Foundation.OverrideDef.__init__(self, name, sItem, sNewItem, dict)

	def _SwapInModules(self, pre, post):
		debug(__name__ + ", _SwapInModules")
		pPreModule = __import__(self.sModule)

		pPostModule = __import__(string.join(post[:-1], '.'))

		self.original = pPreModule.__dict__[self.sClass].__dict__[self.sMethod]
		pPreModule.__dict__[self.sClass].__dict__[self.sMethod] = pPostModule.__dict__[post[-1]]


	def _SwapOutModules(self, pre, post):
		debug(__name__ + ", _SwapOutModules")
		pPreModule = __import__(self.sModule)
		pPreModule.__dict__[self.sClass].__dict__[self.sMethod] = self.original

		self.original = None

###############################################################################
#	CreateMethodTimer(eType, sFunctionHandler, fStart, fDelay, fDuration, bEpisode)
#	
#	Does just what the CreateTimer from MissionLib does, except that this calls a method
#     of a given obj.
#	
#	Args:	pObj				- the object to call the method from
#			sMethodHandler	- method to call
#			fStart				- when this starts firing
#			fDelay				- delay between firings
#			fDuration			- how long this fires for
#			bEpisode			- does this go in the mission or episode list?
#
#	Return:	pTimer
###############################################################################
def CreateMethodTimer(pObj, sMethodHandler, fStart, fDelay = 0, fDuration = 0, bEpisode = 0, bRealTime = 0):
	# Setup the handler function.
	debug(__name__ + ", CreateMethodTimer")
	pGame = App.Game_GetCurrentGame()
	if (pGame == None):
		return None
	pEpisode = pGame.GetCurrentEpisode()
	if (pEpisode == None):
		return None
	pMission = pEpisode.GetCurrentMission()
	if (pMission == None):
		return None

	eType = GetNextEventType()

	#pMission.AddPythonFuncHandlerForInstance( eType, sMethodHandler )
	App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, pObj, sMethodHandler)

	# Create the event and the event timer.
	pEvent = App.TGEvent_Create()
	pEvent.SetEventType(eType)
	pEvent.SetDestination(pMission)
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(fStart)
	pTimer.SetDelay(fDelay)
	pTimer.SetDuration(fDuration)
	pTimer.SetEvent(pEvent)
	if (bRealTime):
		App.g_kRealtimeTimerManager.AddTimer(pTimer)
	else:
		App.g_kTimerManager.AddTimer(pTimer)

	return pTimer

def GetNextEventType():
	debug(__name__ + ", GetNextEventType")
	return App.Mission_GetNextEventType()# + 333

############################################################################################################
##class##     RefreshEventHandler
######################################
# This class purpose is to create a refresh event, that will continuate to call the determined function, with the 
# determined delay time between calls.
# Modified from the one in GravityFX v1.0, this one corrects a bug that caused game crash when you stopped the refresh
# handler. 
# This will also overwrite the GravityFX version of this class for this newer one.
###############################################################################################
#@@@@@@ initializing/creating the RefreshEventHandler
######
# 	- initialize: RefreshEventHandler(sFunc, nDelay = 0.1, sMode = 'NORMAL') 
#		- sFunc: is your function that will be called, her 2 initial args must be pObject, pEvent
#			   Also, the function must NOT have any return statements, or it will cause the Refresher to stop (i think)
#			 NOTE: it is really a function, not a string.
#		- nDelay: it is the delay between calls, defaults to 0.1
#		- sMode: the priority of the event, it can be: 'UNSTOPPABLE', 'CRITICAL', 'NORMAL' and 'LOW',
#		         defaults to 'NORMAL'
###############################################################################################
#@@@@@@ The IconCreator atributes
######
#	- RefreshEventHandler.CLASS -> a string representing the object class.
#	- RefreshEventHandler -> the IconCreator object, it comes with her own unique ID
###############################################################################################
#@@@@@@ The function to edit a value of the event    and to delete the event
######
#	-EditHandler(sType, nValue)
#		- sType: the type of value to be used, it can be:
#			-"Delay": to change the delay of the event
#			-"Priority": to change the priority of the event
#			-"Function": to change the function that is called.
#		- nValue: the value to be set, according to the type selected.
#			-For Delay, use a float.
#			-For Priority, use one of the above mentioned priority strings.
#			-For Function, use a function  duh...
######################################################################################################################
class RefreshEventHandler:
	RUNNING = 1
	STOPPED = 0
	def __init__(self, sFunc, nDelay = 0.1, sMode = 'NORMAL', nLifetime = 0, sFinalFunc = None):
		debug(__name__ + ", __init__")
		self.ModeDict = {'UNSTOPPABLE': App.TimeSliceProcess.UNSTOPPABLE, 'CRITICAL': App.TimeSliceProcess.CRITICAL, 'NORMAL': App.TimeSliceProcess.NORMAL, 'LOW': App.TimeSliceProcess.LOW}
		self.ID = GetUniqueID("RefreshEventHandler")
		self.CLASS = 'Refresh Event Handler'
		self.Function = sFunc
		self.Status = self.RUNNING
          	self.Delay = nDelay
		self.Age = 0
		self.Lifetime = nLifetime
		self.FinalFunction = sFinalFunc
		self._Refresher = None
		self.StartRefreshHandler(sMode)
	
	def Refresh(self, pObject = None, pEvent = None):
		debug(__name__ + ", Refresh")
		if self.Function != None and self.Status == self.RUNNING:
			if self.Lifetime != 0:
				if self.Age < self.Lifetime:
					self.Function(pObject, pEvent)
					self.Age = self.Age + self.Delay
				else:
					if self.FinalFunction != None:
						self.FinalFunction(pObject, pEvent)
						self.StopRefreshHandler()
			else:
				self.Function(pObject, pEvent)			

	def EditHandler(self, sType, nValue):
		debug(__name__ + ", EditHandler")
		if sType == "Delay":
			self.Delay = nValue
			if self.Status == self.RUNNING:
				self._Refresher.SetDelay(self.Delay)
		elif sType == "Priority":
			if nValue == 'UNSTOPPABLE' or nValue == 'CRITICAL' or nValue == 'NORMAL' or nValue == 'LOW':
				self._Refresher.SetPriority(self.ModeDict[nValue])
			else:
				print "Value", nValue, " given to RefreshEventHandler", self.ID, " EditHandler(", sType, ") is invalid."
		elif sType == "Function":
			self.Function = nValue
		elif sType == "FinalFunction":
			self.FinalFunction = nValue
		elif sType == "Age":
			self.Age = nValue
		elif sType == "Lifetime":
			self.Lifetime = nValue
		else:
			print "Type", sType, " given to RefreshEventHandler", self.ID, " EditHandler(", sType, ") is invalid."

	def StartRefreshHandler(self, sMode):
		debug(__name__ + ", StartRefreshHandler")
		if self._Refresher == None:
			self._Refresher = App.PythonMethodProcess()
			self._Refresher.SetInstance(self)
			self._Refresher.SetFunction("Refresh")
			self._Refresher.SetDelay(self.Delay)
			self._Refresher.SetPriority(self.ModeDict[sMode])
			self.Status = self.RUNNING
		elif self.Status == self.STOPPED:
			self.Status = self.RUNNING
			self._Refresher.SetDelay(self.Delay)

	def StopRefreshHandler(self):
		debug(__name__ + ", StopRefreshHandler")
		if self._Refresher and self.Status == self.RUNNING:
			## Disabling the __del__() call because it's probably she that is causing the crashes...
			#self._Refresher.__del__()
			#self._Refresher = None
			self.Status = self.STOPPED
			self._Refresher.SetDelay(10000.0)

	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+self.ID+">"

try:
	import Custom.GravityFX.GravityFXlib
	Custom.GravityFX.GravityFXlib.RefreshEventHandler = RefreshEventHandler
except:
	print "Galaxy Charts couldn't overwrite GravityFX RefreshEventHandler class"

##########################################################################################################################
#  Methods added to ShipClass 
#####
#  Get/Set WarpSpeed
#  Get Cruise/Max WarpSpeed
#####
# 2 methods which are added to the App.ShipClass, thus giving the ability to each ship in the game have her own warp speed
# gotten and set by her ShipClass instance.
#####
# - pShip.GetWarpSpeed has no arguments, only returns the warp speed
# - pShip.GetCruiseWarpSpeed has no arguments, only returns the ship's cruise warp speed
# - pShip.GetMaxWarpSpeed has no arguments, only returns the ship's max warp speed
###
# - pShip.SetWarpSpeed has 1 argument: the warp speed.
#  bear in mind that normal warp speed values range from 1 to 9.99, normally anything bigger than 9.99 is something rare 
#  and really special that travels very fast, things like splistream, transwarp, etc.
##########################################################################################################################
dShipWarpSpeeds = {}

def ShipClass_SetWarpSpeed(self, fWarpSpeed):
	# for now, lets limit the possible warp speeds to the range of 1 to 9.99
	debug(__name__ + ", ShipClass_SetWarpSpeed")
	if fWarpSpeed > 9.99:
		fWarpSpeed = 9.99
	if fWarpSpeed < 1.0:
		fWarpSpeed = 1.0
	dShipWarpSpeeds[self.GetObjID()] = fWarpSpeed
	return fWarpSpeed

def ShipClass_GetWarpSpeed(self):
	debug(__name__ + ", ShipClass_GetWarpSpeed")
	if dShipWarpSpeeds.has_key(self.GetObjID()) == 1:
		return dShipWarpSpeeds[self.GetObjID()]
	else:
		return self.SetWarpSpeed(self.GetCruiseWarpSpeed())

def ShipClass_GetMaxWarp(self):
	debug(__name__ + ", ShipClass_GetMaxWarp")
	pShip = GetShipType(self)

	if Foundation.shipList.has_key(pShip):
		pFoundationShip = Foundation.shipList[pShip]
		if pFoundationShip and hasattr(pFoundationShip, "fMaxWarp"):
			pScale = pFoundationShip.fMaxWarp / 10
			if pScale > 1.0:
				pScale = 1.0
		else:
			pScale = 1.0
	else:
		pScale = 1.0
	maxWarp = pScale
	MaximumWarp = maxWarp * 10
	MaximumWarp = float(str(MaximumWarp)[0:3+1])
	if MaximumWarp > 9.99:
		MaximumWarp = 9.99
	return MaximumWarp 

def ShipClass_GetCruiseWarp(self):
	debug(__name__ + ", ShipClass_GetCruiseWarp")
	pShip = GetShipType(self)

	fBackupScale = self.GetMaxWarpSpeed() / 10
	if Foundation.shipList.has_key(pShip):
		pFoundationShip = Foundation.shipList[pShip]
		if pFoundationShip and hasattr(pFoundationShip, "fCruiseWarp"):
			pScale = pFoundationShip.fCruiseWarp / 10
			if pScale > 1.0:
				pScale = 1.0
		else:
			pScale = fBackupScale 
	else:
		pScale = fBackupScale 
	cruiseWarp = pScale
	CruisingWarp = cruiseWarp * 10
	CruisingWarp = float(str(CruisingWarp)[0:3+1])
	if CruisingWarp > 9.99:
		CruisingWarp = 9.99
	return CruisingWarp

##########################################################################################################################
#  GetShipType
#####
# This function returns the type of the given ship, that is, the name of the ship's script.
#####
# single argument:  an App.ShipClass instance
# return: check description
##########################################################################################################################
def GetShipType(pShip):
	#debug(__name__ + ", GetShipType")
	if pShip.GetScript():
		return string.split(pShip.GetScript(), '.')[-1]
	return None

##########################################################################################################################
#  GetConfigValue
#####
# This function returns the value of the given UMM configuration value.
#####
# single argument:  an App.ShipClass instance
# return: * (value differs for different config values)
##########################################################################################################################
def GetConfigValue(value):
	debug(__name__ + ", GetConfigValue")
	if value == "SelectedSaveGame":
		pConfigScript = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.SelectedSaveGame")
		return pConfigScript.Name
	pConfigScript = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.GalaxyChartsConfigValues")
	if value == "UseDefaultLocs":
		return pConfigScript.SetDefaultLocs
	elif value == "ShowBanners":
		return pConfigScript.ShowBanners
	elif value == "LogChaser":
		return pConfigScript.LoggerConfig.LogChaser
	elif value == "LogTravel":
		return pConfigScript.LoggerConfig.LogTravel
	elif value == "LogGalaxy":
		return pConfigScript.LoggerConfig.LogGalaxy
	elif value == "LogTravelerAI":
		return pConfigScript.LoggerConfig.LogTravelerAI
	elif value == "LogTWS":
		return pConfigScript.LoggerConfig.LogTWS
	elif value == "LogRDF":
		return pConfigScript.LoggerConfig.LogRDF
	elif value == "GetRDFConfig":
		return pConfigScript.RandomDefenceForce
	elif value == "UseWarSim":
		return pConfigScript.WarSimulator.UseWarSim
	elif value == "GetWarSimConfig":
		return pConfigScript.WarSimulator
	else:
		#incorrect value
		raise KeyError, "Incorrect Value for GetConfigValue. Check  with the author"
		return None

def GetSelectedEraName():
	debug(__name__ + ", GetSelectedEraName")
	pConfigScript = __import__("Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.SelectedEra")
	return pConfigScript.Name
##########################################################################################################################
#  GetSTMenu
#####
# This returns a App.STMenu object, with the given name, in the menu of the given character.
#####
# args:
# -  sMenuName: the name of the menu to find
# -  sCharName(default to "XO"): the name of the position of the character to look into, XO, Engineering, Science, etc
# return: the App.STMenu object, if found
##########################################################################################################################
def GetSTMenu(sMenuName, sCharName = "XO"):
	debug(__name__ + ", GetSTMenu")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pXO = App.CharacterClass_GetObject(pBridge, sCharName)
	pXOMenu = pXO.GetMenu()
	pChild = pXOMenu.GetFirstChild()
	while pChild :
		pMenu = App.STMenu_Cast(pChild )
		if pMenu:
			sString = App.TGString()
			pMenu.GetName(sString)
			if (sString.GetCString() == sMenuName):
				return pMenu
		pChild = pXOMenu.GetNextChild(pChild )

##########################################################################################################################
#  GetSTButton
#####
# This returns a App.STButton object, with the given name, in the menu of the given character.
#####
# args:
# -  sButtonName: the name of the button to find
# -  sCharName(default to "XO"): the name of the position of the character to look into, XO, Engineer, Science, etc
# return: the App.STButton object, if found
##########################################################################################################################
def GetSTButton(sButtonName, sCharName = "XO"):
	debug(__name__ + ", GetSTButton")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pXO = App.CharacterClass_GetObject(pBridge, sCharName)
	pXOMenu = pXO.GetMenu()
	pChild = pXOMenu.GetFirstChild()
	while pChild :
		pMenu = App.STButton_Cast(pChild )
		if pMenu:
			sString = App.TGString()
			pMenu.GetName(sString)
			if (sString.GetCString() == sButtonName):
				return pMenu
		pChild = pXOMenu.GetNextChild(pChild )

# This is like the above function, but specially made to get the "Launch ..." buttons that the Shuttle Launching Framework
# creates.
def GetLaunchShuttleButtons():
	debug(__name__ + ", GetLaunchShuttleButtons")
	pBridge = App.g_kSetManager.GetSet("bridge")
	pXO = App.CharacterClass_GetObject(pBridge, "Science")
	pXOMenu = pXO.GetMenu()
	sList = []
	pChild = pXOMenu.GetFirstChild()
	while pChild :
		pMenu = App.STButton_Cast(pChild )
		if pMenu != None:
			sString = App.TGString()
			pMenu.GetName(sString)
			if string.count(sString.GetCString(), "Launch") == 1:
				sList.append(pMenu)
		pChild = pXOMenu.GetNextChild(pChild )
	return sList

##########################################################################################################################
#  GetDictObjsInSet
#####
# This returns a dict with the data  [App.CT_*class type*] = list of objs of this class in the given set
#####
# args:
# -  pSet: the set to get the objects dict from
# return: a dict
##########################################################################################################################
def GetDictObjsInSet(pSet):
	debug(__name__ + ", GetDictObjsInSet")
	dDict = {}
	if pSet == None:
		return dDict 
	dDict[App.CT_SHIP] = []
	dDict[App.CT_ASTEROID_FIELD] = []
	dDict[App.CT_NEBULA] = []
	dDict[App.CT_SUN] = []
	dDict[App.CT_PLANET] = []

	for pShip in pSet.GetClassObjectList(App.CT_SHIP):
		dDict[App.CT_SHIP].append(pShip)

	for pAsField in pSet.GetClassObjectList(App.CT_ASTEROID_FIELD):
		dDict[App.CT_ASTEROID_FIELD].append(pAsField)

	for pNebula in pSet.GetClassObjectList(App.CT_NEBULA):
		dDict[App.CT_NEBULA].append(pNebula)

	lSunIDs = []
	for pSun in pSet.GetClassObjectList(App.CT_SUN):
		try:
			if pSun.IsAtmosphereObj() == None:
				dDict[App.CT_SUN].append(pSun)
		except:
			dDict[App.CT_SUN].append(pSun)
		lSunIDs.append(pSun.GetObjID())

	for pPlanet in pSet.GetClassObjectList(App.CT_PLANET):
		if not pPlanet.GetObjID() in lSunIDs:
			pSunObj = App.Sun_Cast(pPlanet)
			if pSunObj != None:
				if pSunObj.IsAtmosphereObj() == None:
					dDict[App.CT_SUN].append(pSunObj)
					lSunIDs.append(pSunObj.GetObjID())
			else:
				try:
					if pPlanet.IsAtmosphereObj() == None:
						dDict[App.CT_PLANET].append(pPlanet)
				except:
					dDict[App.CT_PLANET].append(pPlanet)

	return dDict 
	
##########################################################################################################################
#  GetShipRace
#####
# This returns the race string of the given ship
#####
# args:
# -  pShip: the ship to get the race from
# return: the race string  ("Default" is it can't get the race)
##########################################################################################################################
def GetShipRace(pShip):
	#debug(__name__ + ", GetShipRace")
	sRace = GetShipDefRace(GetShipDef(pShip))
	return sRace

def GetShipDefRace(pShipDef):
	debug(__name__ + ", GetShipDefRace")
	if pShipDef == None:
		return "Default"
	try:
		sRace = pShipDef.race.name
	except:
		# the ship def has no race... So we try to get it by the Races plugins
		try:
			sRace = "yetunknown"
			import Custom.QBautostart.Libs.Races
			lRaceObjs = Custom.QBautostart.Libs.Races.Races.values()
			for pRaceObj in lRaceObjs:
				if pRaceObj.ContainsShip(pShipDef.shipFile) == 1 and pRaceObj.GetRaceName() != "GodShips":
					sRace = pRaceObj.GetRaceName()
		except:
			import Galaxy
			Galaxy.LogError("LIB_GetShipDefRace")
			sRace = "Default"
	return sRace

# little workaround: since we may have sometimes ships in the war sim of race A fighting for race B, even if both races are enemies (ship was taken, etc)
# instead of various scripts using GetShipRace(pShip) to get a ship's race, which could lead to problems (they would 'detect' the ship isn't allied),
# they use this instead because this will return the race of the ship as the War Sim sees it.
def GetShipRaceByWarSim(pShip):
	debug(__name__ + ", GetShipRaceByWarSim")
	import GalacticWarSimulator
	if GalacticWarSimulator.WarSimulator.IsInitialized() == 1:
		pWSShip = GalacticWarSimulator.WarSimulator.GetWSShipObjForShip(pShip)
		if pWSShip != None:
			if pWSShip.Race != None:
				return pWSShip.Race.GetRaceName()
			else:
				return None
		else:
			return GetShipRace(pShip)
	else:
		return GetShipRace(pShip)

def GetShipDef(pShip):
	#debug(__name__ + ", GetShipDef")
	return GetShipDefByScript(pShip.GetScript())

def GetShipDefByScript(sShipScript):
	#debug(__name__ + ", GetShipDefByScript")
	try:
		lShipScript = string.split(sShipScript, ".")
		sShipScript = lShipScript[-1]
		for pShipDef in Foundation.shipList:
			if pShipDef.shipFile == sShipScript:
				return pShipDef
		return None
	except:
		return None

##########################################################################################################################
#  GetShipsOfRace
#####
# This returns the Foundation.ShipDef of the given race
#####
# args:
# -  sRace: the race to get the shipDefs from
# -  bIncludeGodShips: a bool value indicating if god ships should be included or no.
# return: a list of shipdefs
##########################################################################################################################
# this dict stores a subship file name, and it's parent ship file name, so that these subships aren't acquired as a race's
# ships by the GetShipsOfRace function
dSubShips = {"MvamPrometheusSaucer": "MvamPrometheus",
"MvamPrometheusDorsal": "MvamPrometheus",
"MvamPrometheusVentral": "MvamPrometheus",
"MvamGalaxySaucer": "MvamGalaxy",
"MvamGalaxyStardrive": "MvamGalaxy",
"GalaxySaucer": "Galaxy",
"GalaxyStardrive": "Galaxy",
"FedConstOpen": "FedConst"}

def GetShipsOfRace(sRace, bIncludeGodShips = 1):
	debug(__name__ + ", GetShipsOfRace")
	lShipDefs = []
	try:
		global dSubShips
		lShipDefs = []
		pRaceObj = GetRaceClassObj(sRace)
		pGodsObj = GetRaceClassObj("GodShips")
		if pRaceObj != None:
			for pShipDef in Foundation.shipList:
				if pShipDef.shipFile in pRaceObj.myShips and not pShipDef.shipFile in dSubShips.keys():
					if bIncludeGodShips == 0 and pGodsObj != None:
						if not pShipDef.shipFile in pGodsObj.myShips:
							lShipDefs.append(pShipDef)
					else:
						lShipDefs.append(pShipDef)
	except:
		lShipDefs = []
	return lShipDefs

def GetBasesOfSet(pSet):
	debug(__name__ + ", GetBasesOfSet")
	if pSet == None:
		return []
	pRegion = pSet.GetRegion()
	if pRegion == None:
		return []
	sEmpire = pRegion.GetControllingEmpire()
	pRaceObj = GetRaceClassObj(sEmpire)
	if pRaceObj == None:
		return []
	lBases = []
	for pShip in pSet.GetClassObjectList(App.CT_SHIP):
		sShipRace = GetShipRaceByWarSim(pShip)
		if sShipRace == sEmpire or AreRacesAllied(sShipRace, sEmpire) == 1:
			sShipClass = GetShipType(pShip)
			pShipRaceObj = GetRaceClassObj(sShipRace)
			lBaseClasses = pShipRaceObj.GetBases()
			if sShipClass in lBaseClasses:
				lBases.append(pShip)
			elif pShip.GetShipProperty().IsStationary() == 1:
				lBases.append(pShip)
	return lBases

def IsStarbaseDockable(pStarbase):
	debug(__name__ + ", IsStarbaseDockable")
	bCanDock = 0
	vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, "Docking Entry Start")
	if vPos != None and vFwd != None and vUp != None:
		try:
			import Custom.QBautostart.Construct
			Custom.QBautostart.Construct.RequestDock(pStarbase)
			if not Custom.QBautostart.Construct.isConstructing(pStarbase):
				bCanDock = 1
		except:
			bCanDock = 1
	return bCanDock

def GetDockableBasesOfSet(pSet):
	debug(__name__ + ", GetDockableBasesOfSet")
	lPossibleBases = GetBasesOfSet(pSet)
	lBases = []
	for pStarbase in lPossibleBases:
		if IsStarbaseDockable(pStarbase) == 1:
			lBases.append(pStarbase)
	return lBases

# (not so) simple (anymore) class to handle a random defence force wave, and possible reinforcements
# now modified to have a more complex and racional behavior if this is a RDF for the War Sim
# and also updated to produce a random attack force, depending on situation for the War Sim.
lRDFs = []
class RandomDefenceForce:
	def __init__(self, sEmpire, iNumInitialShips, iNumReinforcementsShips, iNumOfReinforcements, pEnterInSet, fTimeToEnter, fTimeToReinforce, bIncludeGodShips, bIncludeEscorts):
		debug(__name__ + ", __init__")
		self.Empire = sEmpire
		self.bIncludeGodShips = bIncludeGodShips
		self.__ID = GetUniqueID(str(sEmpire) + "_" + str(pEnterInSet.GetRegion().GetName()) + "_" + "RDF")
		self.lShips = []
		self.lShipDefs = []
		self.DoneInitialWave = 0
		self.IncludeEscorts = bIncludeEscorts
		self.pSet = pEnterInSet
		self.iNumIniShips = iNumInitialShips
		self.iNumReinShips = iNumReinforcementsShips
		self.iNumOfReins = iNumOfReinforcements
		self.__reinWaves = self.iNumOfReins
		self.fTimeToEnter = fTimeToEnter
		self.fTimeToReinforce = fTimeToReinforce
		self.__isForWarSim = 0
		self.__initFunds = 0.0
		self.__reinFunds = 0.0
		self.__addAlliedShips = 0
		self.__isRAF = 0
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		if sEmpire != "None":
			self.__timer = CreateMethodTimer(self.pEventHandler, "CreateShips", App.g_kUtopiaModule.GetGameTime() + fTimeToEnter)
		#print "RandomDefenceForce Created:", sEmpire, ", in set:", self.pSet.GetName()
		global lRDFs
		lRDFs.append(self)
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def GetTimeLeftForTimer(self):
		debug(__name__ + ", GetTimeLeftForTimer")
		if self.__timer != None:
			fCurrentTime = time.clock()
			fStart = self.__timer.GetTimerStart()
			return fStart - fCurrentTime
		return 0.0
	def SetAsWarSimRDF(self, fInitShipFunds, fReinShipFunds, bAddAlliedShips):
		debug(__name__ + ", SetAsWarSimRDF")
		self.__isForWarSim = 1
		self.__initFunds = fInitShipFunds
		self.__reinFunds = fReinShipFunds
		self.__addAlliedShips = bAddAlliedShips
		if self.pSet.GetRegion() != None:
			if AreRacesEnemies(  self.Empire, self.pSet.GetRegion().GetControllingEmpire()  ) == 1:
				self.__isRAF = 1
	def CreateShips(self, pMethodTimerEvent = None):
		#print "RandomDefenceForce CreateShips called (", self.Empire, ", in set:", self.pSet.GetName(), ")"
		debug(__name__ + ", CreateShips")
		if self.DoneInitialWave == 0:
			self.SetShipDefsByNum(self.iNumIniShips)
		lShips = []
		sAllegiance = "Enemy"
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			pPlayerSet = pPlayer.GetContainingSet()
			if pPlayerSet != None:
				if pPlayerSet.GetObjID() == self.pSet.GetObjID():
					if self.DoneInitialWave == 0:
						if self.__isRAF == 1:
							ShowTextBanner(self.Empire+" Attack Force Arrived", 0.5, 0.45, 3, 14, 1, 0)
						else:
							ShowTextBanner(self.Empire+" Defense Force Arrived", 0.5, 0.5, 3, 14, 1, 0)
					elif self.DoneInitialWave == 1:
						if self.__isRAF == 1:
							ShowTextBanner(self.Empire+" Reinforcements Arrived", 0.5, 0.55, 3, 14, 1, 0)
						else:
							ShowTextBanner(self.Empire+" Reinforcements Arrived", 0.5, 0.6, 3, 14, 1, 0)
			if IsShipFriendlyOfRace(pPlayer, self.Empire) == 1 or GetShipRaceByWarSim(pPlayer) == self.Empire:
				sAllegiance = "Friendly"
		import GalacticWarSimulator
		for pShipDef in self.lShipDefs:
			pWSShip = GalacticWarSimulator.WarSimulator.GetFirstIdleShipClassOfRace(pShipDef.shipFile, GetShipDefRace(pShipDef) )
			pShip = None
			if pWSShip != None:
				if pWSShip.Ship != None:
					if pWSShip.Ship.IsDying() == 0 and pWSShip.Ship.IsDead() == 0:
						if pWSShip.Ship.GetContainingSet() != None:
							if pWSShip.Ship.GetContainingSet().GetRegion() != None:
								# if the acquired idle ship still exists, obj in space wise, transport her or warp her to 
								# the destination set
								pTravel = App.g_kTravelManager.GetTravel(pShip)
								if pTravel != None and pTravel.IsTravelling() == 0:
									pTravel.SetTarget(None)
									pTravel.TravelTo(self.pSet.GetRegionModule())
									pShip = pWSShip.Ship
				if pShip == None:
					pShip = CreateShip(pShipDef, self.pSet, pWSShip.GetShipName(), sAllegiance, self.IncludeEscorts)
			else:
				pShip = CreateShip(pShipDef, self.pSet, "", sAllegiance, self.IncludeEscorts)
			if pShip != None:
				lShips.append(pShip)
		self.lShips = lShips
		self.DoneInitialWave = 1
		if self.iNumOfReins >= 1:
			self.SetShipDefsByNum(self.iNumReinShips)
			fTimeToReinforce = self.fTimeToReinforce
			self.__timer = CreateMethodTimer(self.pEventHandler, "CreateShips", App.g_kUtopiaModule.GetGameTime() +fTimeToReinforce)
			#print "RandomDefenceForce Reinforcement Wave Timer created (", self.Empire, ", in set:", self.pSet.GetName(), ")"
			self.iNumOfReins = self.iNumOfReins - 1
		else:
			# delete itself
			global lRDFs
			if self in lRDFs:
				lRDFs.remove(self)
	def SetShipDefsByNum(self, iNumOfShips):
		debug(__name__ + ", SetShipDefsByNum")
		if iNumOfShips <= 0:
			return
		pRaceObj = GetRaceClassObj(self.Empire)
		lShipDefs = []
		if self.__isForWarSim == 1 and pRaceObj != None:
			if self.DoneInitialWave == 0:
				fPossibleFunds = self.__initFunds
			else:
				fPossibleFunds = self.__reinFunds / self.__reinWaves   # max cost
			if pRaceObj.GetTotalFunds() != 0.0:
				fAlliedFundPercentage = (-100.0 * (pRaceObj.GetTotalFunds() - (self.__initFunds + self.__reinFunds))) / pRaceObj.GetTotalFunds()
			else:
				fAlliedFundPercentage = 100.0
			fPossibleAlliedFunds = (fPossibleFunds * fAlliedFundPercentage) / 100.0   # max cost for allies
			if fPossibleFunds > pRaceObj.GetTotalFunds():
				fPossibleFunds = pRaceObj.GetTotalFunds()
			lPossibleDefs = []
			lAlliedShipClasses = []
			iMinShipCostFac = iNumOfShips - 1
			while len(lPossibleDefs) <= 0 and iMinShipCostFac < (iNumOfShips + 25):
				iMinShipCostFac = iMinShipCostFac + 1
				fFundForShip = (fPossibleFunds / iMinShipCostFac) - 1000.0    # min cost
				if fFundForShip < 100.0:
					fFundForShip = 100.0
				lPossibleDefs = GetShipsOfRace(self.Empire, self.bIncludeGodShips)
				lPossibleDefs = ModifyShipListByCost(lPossibleDefs, fFundForShip, fPossibleFunds)
				if self.__addAlliedShips == 1:
					for sFriendlyRace in GetAlliedRacesOf(self.Empire):
						pAlliedRaceObj = GetRaceClassObj(sFriendlyRace)
						if pAlliedRaceObj != None:
							lAlliedShipDefs = GetShipsOfRace(sFriendlyRace, self.bIncludeGodShips)
							if fPossibleAlliedFunds > pAlliedRaceObj.GetTotalFunds():
								fPossibleAlliedFunds = pAlliedRaceObj.GetTotalFunds()
							fFundForAlliedShip = (fPossibleAlliedFunds / iMinShipCostFac) - 1000.0    # min cost
							if fFundForAlliedShip < 100.0:
								fFundForAlliedShip = 100.0
							lAlliedShipDefs = ModifyShipListByCost(lAlliedShipDefs, fFundForAlliedShip, fPossibleAlliedFunds)
							for pAlliedShipDef in lAlliedShipDefs:
								lPossibleDefs.append(pAlliedShipDef)
								lAlliedShipClasses.append(pAlliedShipDef.shipFile)

			if len(lAlliedShipClasses) <= 0:
				fPossibleAlliedFunds = -1.0

			import Galaxy
			Galaxy.Logger.LogString("RDF: Mark start")
			fMinShipCost = GetMinShipCostInList(lPossibleDefs)
			if len(lPossibleDefs) >= 1:
				Galaxy.Logger.LogString("RDF: Mark ok  (MSC:"+str(fMinShipCost)+")" )
				Galaxy.Logger.LogString("RDF: Mark ok  (ASC:"+str(lAlliedShipClasses)+")" )
				#for i in range(iNumOfShips):
				while iNumOfShips >= 1 and len(lPossibleDefs) >= 1 and (fPossibleFunds > fMinShipCost or (fPossibleAlliedFunds > fMinShipCost and self.__addAlliedShips == 1)):
					Galaxy.Logger.LogString("RDF: Mark 1")
					index = App.g_kSystemWrapper.GetRandomNumber( len(lPossibleDefs) )
					pShipDef = lPossibleDefs[index]
					sShipClass = pShipDef.shipFile
					fShipCost = GetShipClassFundCost(sShipClass)
					if sShipClass in lAlliedShipClasses:
						Galaxy.Logger.LogString("RDF: Mark 2  (PF:"+str(fPossibleFunds)+" ||PAF:"+str(fPossibleAlliedFunds)+" ||SC:"+str(fShipCost)+")" )
						# is an allied ship class, so we proceed by it.
						if fPossibleAlliedFunds >= fShipCost:
							Galaxy.Logger.LogString("RDF: Mark 2  OK (SClass:"+str(sShipClass)+")" )
							lShipDefs.append(pShipDef)
							fPossibleAlliedFunds = fPossibleAlliedFunds - fShipCost
							iNumOfShips = iNumOfShips - 1
						if fShipCost > fPossibleAlliedFunds:
							#we won't be able to create this ship any longer, so take it out from the PossibleDefs list.
							Galaxy.Logger.LogString("RDF: Mark 2  REMOVE (SClass:"+str(sShipClass)+")" )
							del lPossibleDefs[index]
					else:
						Galaxy.Logger.LogString("RDF: Mark 3  (PF:"+str(fPossibleFunds)+" ||PAF:"+str(fPossibleAlliedFunds)+" ||SC:"+str(fShipCost)+")" )
						if fPossibleFunds >= fShipCost:
							Galaxy.Logger.LogString("RDF: Mark 3  OK (SClass:"+str(sShipClass)+")")
							lShipDefs.append(pShipDef)
							fPossibleFunds = fPossibleFunds - fShipCost
							iNumOfShips = iNumOfShips - 1
						if fShipCost > fPossibleFunds:
							#we won't be able to create this ship any longer, so take it out from the PossibleDefs list.
							Galaxy.Logger.LogString("RDF: Mark 3  REMOVE (SClass:"+str(sShipClass)+")" )
							del lPossibleDefs[index]
		else:
			lPossibleDefs = GetShipsOfRace(self.Empire, self.bIncludeGodShips)
			if len(lPossibleDefs) >= 1:
				for i in range(iNumOfShips):
					index = App.g_kSystemWrapper.GetRandomNumber( len(lPossibleDefs) )
					lShipDefs.append(lPossibleDefs[index])
		self.lShipDefs = lShipDefs
	def CancelRDF(self):
		debug(__name__ + ", CancelRDF")
		if self.__timer != None:
			App.g_kTimerManager.DeleteTimer(self.__timer.GetObjID())
			self.__timer = None
			global lRDFs
			if self in lRDFs:
				lRDFs.remove(self)

def GetRaceClassObj(sRaceName):
	#debug(__name__ + ", GetRaceClassObj")
	try:
		import Custom.QBautostart.Libs.Races
		if Custom.QBautostart.Libs.Races.Races.has_key(sRaceName):
			return Custom.QBautostart.Libs.Races.Races[sRaceName]
		else:
			return None
	except:
		return None

def GetRandomNameForShip(pShipDef):
	debug(__name__ + ", GetRandomNameForShip")
	try:
		pRaceObj = GetRaceClassObj(GetShipDefRace(pShipDef))
		if pRaceObj != None:
			return pRaceObj.GetRandomName()
		else:
			return None

	except:
		return None

def GetEnemyRacesOf(sRace):
	debug(__name__ + ", GetEnemyRacesOf")
	lEnemies = []
	import Custom.QBautostart.Libs.Races
	for sRaceName in Custom.QBautostart.Libs.Races.Races.keys():
		if AreRacesEnemies(sRace, sRaceName) == 1:
			lEnemies.append(sRaceName)
	return lEnemies

def GetAlliedRacesOf(sRace):
	debug(__name__ + ", GetAlliedRacesOf")
	lFriendlies = []
	import Custom.QBautostart.Libs.Races
	for sRaceName in Custom.QBautostart.Libs.Races.Races.keys():
		if AreRacesAllied(sRace, sRaceName) == 1:
			lFriendlies.append(sRaceName)
	return lFriendlies

def AreRacesEnemies(sRace1, sRace2):
	debug(__name__ + ", AreRacesEnemies")
	if sRace1 == sRace2:
		return 0
	try:
		pRaceObj = GetRaceClassObj(sRace2)
		if pRaceObj != None:
			bRaceEnemy = pRaceObj.IsEnemyRace(sRace1)
			if bRaceEnemy == 0:
				pRaceObj2 = GetRaceClassObj(sRace1)
				if pRaceObj2 != None:
					bRaceEnemy = pRaceObj2.IsEnemyRace(sRace2)
			return bRaceEnemy
		else:
			return 1
	except:
		return 1

def AreRacesAllied(sRace1, sRace2):
	debug(__name__ + ", AreRacesAllied")
	if sRace1 == sRace2:
		return 0
	try:
		pRaceObj = GetRaceClassObj(sRace2)
		if pRaceObj != None:
			bRaceEnemy = pRaceObj.IsFriendlyRace(sRace1)
			if bRaceEnemy == 0:
				pRaceObj2 = GetRaceClassObj(sRace1)
				if pRaceObj2 != None:
					bRaceEnemy = pRaceObj2.IsFriendlyRace(sRace2)
			return bRaceEnemy
		else:
			return 0
	except:
		return 0

def IsShipEnemyOfRace(pShip, sRace):
	debug(__name__ + ", IsShipEnemyOfRace")
	sShipRace = GetShipRaceByWarSim(pShip)
	if sShipRace == "Default":
		return 1
	return AreRacesEnemies(sShipRace, sRace)

def IsShipFriendlyOfRace(pShip, sRace):
	debug(__name__ + ", IsShipFriendlyOfRace")
	sShipRace = GetShipRaceByWarSim(pShip)
	if sShipRace == "Default":
		return 0
	return AreRacesAllied(sShipRace, sRace)

def GetRacePeaceValue(sRace):
	debug(__name__ + ", GetRacePeaceValue")
	try:
		pRaceObj = GetRaceClassObj(sRace)
		if pRaceObj != None:
			return pRaceObj.GetPeaceValue()
		else:
			return 0.5
	except:
		return 0.5

iRDFshipCreated = 1
def CreateShip(pShipDef, pSet, sShipName, sAllegiance, bIncludeEscorts = 0):
	debug(__name__ + ", CreateShip")
	global iRDFshipCreated
	pPlayer = MissionLib.GetPlayer()
	if pPlayer == None or pShipDef == None:
		return

	sShipType = pShipDef.shipFile

	sShipRace = GetShipDefRace(pShipDef)
	pRaceObj = GetRaceClassObj(sShipRace)
	if pRaceObj != None and bIncludeEscorts == 1:
		lEscorts = pRaceObj.GetEscorts(sShipType)
		if lEscorts != None:
			for sEscort in lEscorts:
				pEscortDef = GetShipDefByScript(sEscort)
				if pEscortDef != None:
					CreateShip(pEscortDef, pSet, "", sAllegiance, 0)

	if sShipName == "" or sShipName == "None":
		sShipName = GetRandomNameForShip(pShipDef)
		if sShipName == None:
			sShipName = pShipDef.shipFile + " RDF " + str(iRDFshipCreated)
			iRDFshipCreated = iRDFshipCreated +1

	pFriendlies = MissionLib.GetFriendlyGroup()
	pEnemies = MissionLib.GetEnemyGroup()
		
	pShip = loadspacehelper.CreateShip(sShipType, pSet, sShipName, "", 1)
	if not pShip:
		# really strange... ship wasn't created...
		return

	iRandomValue = 500
	kLocation = App.TGPoint3()
	X = GetRandomInRange(-iRandomValue, iRandomValue)
	Y = GetRandomInRange(-iRandomValue, iRandomValue)
	Z = GetRandomInRange(-iRandomValue, iRandomValue)
	kLocation.SetXYZ(X, Y, Z)
	
	i = 0
	while ( pSet.IsLocationEmptyTG(kLocation, pShip.GetRadius()*2, 1) == 0):
		X = GetRandomInRange(-iRandomValue, iRandomValue)
		Y = GetRandomInRange(-iRandomValue, iRandomValue)
		Z = GetRandomInRange(-iRandomValue, iRandomValue)
		kLocation.SetXYZ(X, Y, Z)
		i = i + 1
		if i == 10:
			i = 0
			iRandomValue = iRandomValue + 500
	pShip.SetTranslate(kLocation)
	pShip.UpdateNodeOnly()
	
	pProxManager = pSet.GetProximityManager()
	if pProxManager:
		pProxManager.UpdateObject(pShip)

	if sAllegiance == "Enemy":
		pEnemies.AddName(pShip.GetName())
	elif sAllegiance == "Friendly":
		pFriendlies.AddName(pShip.GetName())
	elif sAllegiance == "None":
		return pShip

	ResetShipAI(pShip)

	return pShip

##########################################################################################################################
#  CreateShipAI
#####
# Creates a AI for the given ship, with the given object group of enemies.
#####
# args:
# -  pShip:  the Ship to create the AI to.
# -  pShipEnemiesGroup:  the object group of the ships that are enemies to the given ship. (like MissionLib.GetEnemyGroup()
#     			 gets the Enemy ship group, they are enemies to the Friendly ship group, which the player belongs 
#				 to.
# return: the AI object.
##########################################################################################################################
def CreateShipAI(pShip, pShipEnemiesGroup):
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	debug(__name__ + ", CreateShipAI")
	import AI.Compound.BasicAttack
	if pShipEnemiesGroup != None:
		pAttack = AI.Compound.BasicAttack.CreateAI(pShip, pShipEnemiesGroup, Difficulty = 1, FollowTargetThroughWarp = 1, MaxFiringRange = 1000.0, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, DisableBeforeDestroy = 0, InaccurateTorps = 1, SmartShields = 1, UseRearTorps = 1, UseCloaking = 1)
	else:
		pAttack = AI.Compound.BasicAttack.CreateAI(pShip, Difficulty = 1, FollowTargetThroughWarp = 1, MaxFiringRange = 1000.0, AggressivePulseWeapons = 1, ChooseSubsystemTargets = 1, DisableBeforeDestroy = 0, InaccurateTorps = 1, SmartShields = 1, UseRearTorps = 1, UseCloaking = 1)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PlainAI Turn at (237, 47)
	pTurn = App.PlainAI_Create(pShip, "Turn")
	pTurn.SetScriptModule("ManeuverLoop")
	pTurn.SetInterruptable(1)
	pScript = pTurn.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelLeft())
	# Done creating PlainAI Turn
	#########################################
	#########################################
	# Creating PlainAI Turn_2 at (353, 55)
	pTurn_2 = App.PlainAI_Create(pShip, "Turn_2")
	pTurn_2.SetScriptModule("ManeuverLoop")
	pTurn_2.SetInterruptable(1)
	pScript = pTurn_2.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelRight())
	# Done creating PlainAI Turn_2
	#########################################
	#########################################
	# Creating PlainAI Turn_3 at (429, 103)
	pTurn_3 = App.PlainAI_Create(pShip, "Turn_3")
	pTurn_3.SetScriptModule("ManeuverLoop")
	pTurn_3.SetInterruptable(1)
	pScript = pTurn_3.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelUp())
	# Done creating PlainAI Turn_3
	#########################################
	#########################################
	# Creating PlainAI Turn_4 at (448, 147)
	pTurn_4 = App.PlainAI_Create(pShip, "Turn_4")
	pTurn_4.SetScriptModule("ManeuverLoop")
	pTurn_4.SetInterruptable(1)
	pScript = pTurn_4.GetScriptInstance()
	pScript.SetLoopFraction(0.25)
	pScript.SetTurnAxis(App.TGPoint3_GetModelDown())
	# Done creating PlainAI Turn_4
	#########################################
	#########################################
	# Creating RandomAI FlyPointlessly at (198, 181)
	pFlyPointlessly = App.RandomAI_Create(pShip, "FlyPointlessly")
	pFlyPointlessly.SetInterruptable(1)
	# SeqBlock is at (309, 185)
	pFlyPointlessly.AddAI(pTurn)
	pFlyPointlessly.AddAI(pTurn_2)
	pFlyPointlessly.AddAI(pTurn_3)
	pFlyPointlessly.AddAI(pTurn_4)
	# Done creating RandomAI FlyPointlessly
	#########################################
	#########################################
	# Creating SequenceAI RepeatForever at (195, 224)
	pRepeatForever = App.SequenceAI_Create(pShip, "RepeatForever")
	pRepeatForever.SetInterruptable(1)
	pRepeatForever.SetLoopCount(-1)
	pRepeatForever.SetResetIfInterrupted(1)
	pRepeatForever.SetDoubleCheckAllDone(1)
	pRepeatForever.SetSkipDormant(0)
	# SeqBlock is at (295, 228)
	pRepeatForever.AddAI(pFlyPointlessly)
	# Done creating SequenceAI RepeatForever
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (30, 228)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (149, 235)
	pPriorityList.AddAI(pAttack, 1)
	pPriorityList.AddAI(pRepeatForever, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (29, 285)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pPriorityList)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 3, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

def CreateStarbaseAI(pShip, pShipEnemiesGroup):
	#if not pShipEnemiesGroup.GetNameTuple():
	#	pShipEnemiesGroup.AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateStarbaseAI")
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pShipEnemiesGroup)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 5, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait

##########################################################################################################################
#  ResetShipAI
#####
# Resets a ship's AI.
# It checks for the allegiance of the ship, to create enemy/friendly AI accordingly.
# Also, it will try to use the normal AI module that the ship uses.
# NOTE: it will probably not work right with stations/starbases...
#####
# args:
# -  pShip:  the ship to reset the AI
# return: None
##########################################################################################################################
def ResetShipAI(pShip):
	debug(__name__ + ", ResetShipAI")
	if pShip != None:
		import GalacticWarSimulator
		pFleet = GalacticWarSimulator.FleetManager.GetFleetOfShip(pShip)
		sCleared = ""
		if pShip.GetAI() != None:
			pShip.ClearAI()
			sCleared = "(cleared old AI)"
		pShipDef = GetShipDef(pShip)
		pFriendlies = MissionLib.GetFriendlyGroup()
		pEnemies = MissionLib.GetEnemyGroup()
		pNeutrals = MissionLib.GetNeutralGroup()
		#print "Resetting ship ", pShip.GetName(), " AI", sCleared
		if GalacticWarSimulator.WarSimulator.IsInitialized() == 1 and pFleet != None:
			# Use our War AI for this ship.
			if pEnemies.IsNameInGroup(pShip.GetName()) or pFriendlies.IsNameInGroup(pShip.GetName()):
				# checking if ship is in our friendly or enemy group may prevent some problems   =/
				import WarAI
				pShip.SetAI(WarAI.CreateWarAI(pShip))
				#print "Reseted as a War AI"
		else:		
			if pEnemies.IsNameInGroup(pShip.GetName()):
				pAIenemyGroup = pFriendlies
				sAI = pShipDef.StrEnemyAI()
				sAItoCheckTo = "QuickBattleAI"
				sStarbaseAItoCheckTo = "StarbaseAI"
			elif pFriendlies.IsNameInGroup(pShip.GetName()):
				pAIenemyGroup = pEnemies
				sAI = pShipDef.StrFriendlyAI()
				sAItoCheckTo = "QuickBattleFriendlyAI"
				sStarbaseAItoCheckTo = "StarbaseFriendlyAI"
			else:   #elif pNeutrals.IsNameInGroup(pShip.GetName()):   #ship is neutral
				# forget resetting AI for a neutral ship
				#print "Cancelled resetting, neutral ship."
				return 0

			if sAI == sAItoCheckTo:
				pShip.SetAI(CreateShipAI(pShip, pAIenemyGroup))
			elif sAI == sStarbaseAItoCheckTo:
				pAIenemyGroup.AddName(pShip.GetName())
				pShip.SetAI(CreateStarbaseAI(pShip, pAIenemyGroup))
				pAIenemyGroup.RemoveName(pShip.GetName())
			else:
				try:
					pAIModule = __import__("QuickBattle." + sAI)
					try:
						pShip.SetAI(pAIModule.CreateAI(pShip, pAIenemyGroup))
					except:
						pShip.SetAI(pAIModule.CreateAI(pShip))
				except:
					pShip.SetAI(CreateShipAI(pShip, pAIenemyGroup))
			#print "Reseted as a Regular AI"
	return

# little helper to check if a ship is using the War AI
def IsShipUsingWarAI(pShip):
	debug(__name__ + ", IsShipUsingWarAI")
	if pShip == None:
		return 0
	pAI = pShip.GetAI()
	if pAI != None:
		if len(pAI.GetFocusAIs()) >= 1:
			if pAI.GetFocusAIs()[0].GetName() == "WarAIStartTimer":
				return 1
	return 0

##########################################################################################################################
#  UpdateShipsAllegiance
#####
# Changes the allegiance (friendly/enemy/neutral setting) of ships of given race to given allegiance
#####
# args:
# -  sRace:  race of name to update ships allegiance
# -  sNewAllegiance: new allegiance of the ships of the given race. (must be: 'Friendly', 'Neutral' or 'Enemy')
# return: non-important
##########################################################################################################################
def UpdateShipsAllegiance(sRace, sNewAllegiance):
	debug(__name__ + ", UpdateShipsAllegiance")
	pRaceObj = GetRaceClassObj(sRace)
	if pRaceObj == None:
		return
	pFriendlies = MissionLib.GetFriendlyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	pEnemies = MissionLib.GetEnemyGroup()
	for pWSShip in pRaceObj.dWSShips.values():
		pShip = pWSShip.Ship
		if GetShipRaceByWarSim(pShip) == sRace:
			bResetAI = 0
			if pEnemies.IsNameInGroup(pShip.GetName()):  #ship is enemy
				if sNewAllegiance == "Friendly":
					pEnemies.RemoveName(pShip.GetName())
					pFriendlies.AddName(pShip.GetName())
					bResetAI = 1
				elif sNewAllegiance == "Neutral":
					pEnemies.RemoveName(pShip.GetName())
					pNeutrals.AddName(pShip.GetName())
					bResetAI = 1
			if pFriendlies.IsNameInGroup(pShip.GetName()):  #ship is friendly
				if sNewAllegiance == "Enemy":
					pFriendlies.RemoveName(pShip.GetName())
					pEnemies.AddName(pShip.GetName())
					bResetAI = 1
				elif sNewAllegiance == "Neutral":
					pFriendlies.RemoveName(pShip.GetName())
					pNeutrals.AddName(pShip.GetName())
					bResetAI = 1
			if pNeutrals.IsNameInGroup(pShip.GetName()):   #ship is neutral
				if sNewAllegiance == "Friendly":
					pNeutrals.RemoveName(pShip.GetName())
					pFriendlies.AddName(pShip.GetName())
					bResetAI = 1
				elif sNewAllegiance == "Enemy":
					pNeutrals.RemoveName(pShip.GetName())
					pEnemies.AddName(pShip.GetName())
					bResetAI = 1
			if bResetAI == 1:
				ResetShipAI(pShip)
	return 1

##########################################################################################################################
#  ShowTextBanner
#####
# shows a text banner, like the "Arriving At..." when you warp somewhere
# however, it only shows a banner if the option ShowBanners of the Galaxy Charts UMM menu is selected on.
#####
# args:
# -  text:  the text of the banner
# -  X and Y:  X and Y location in screen coordinates
# -  fDuration:  the time in seconds the banner will last
# -  iSize:   the size of the font
# -  bHCentered: 1 if it should be centered horizontally
# -  bVCentered: 1 if it should be centered vertically
# return: None
##########################################################################################################################
def ShowTextBanner(text, X, Y, fDuration, iSize, bHCentered, bVCentered):
	debug(__name__ + ", ShowTextBanner")
	if GetConfigValue("ShowBanners") == 1:
		MissionLib.TextBanner(None, App.TGString(text), X, Y, fDuration, iSize, bHCentered, bVCentered)

##########################################################################################################################
#  CheckIfShipIsBeingPursued
#####
# Checks if a ship is being pursued by enemy ships, either if they are going to the same set or if they are truly 
# following the ship thru warp.
#####
# args:
# -  pShip: the ship to check
# return: 1 is the ship is being followed, 0 if not.
##########################################################################################################################
def CheckIfShipIsBeingPursued(pShip):
	debug(__name__ + ", CheckIfShipIsBeingPursued")
	pSet = pShip.GetContainingSet()
	pEnemies = MissionLib.GetEnemyGroup()
	if pSet != None and pEnemies != None and pShip != None:
		lTravels = App.g_kTravelManager.GetAllTravels()
		#print "CISIBP:", lTravels
		for pTravel in lTravels:
			if pEnemies.IsNameInGroup(pTravel.Ship.GetName()) == 1:
				if pTravel.GetDestination() == pSet.GetRegionModule():
					return 1
				if pTravel.Target != None:
					if pTravel.Target.GetObjID() == pShip.GetObjID():
						return 1
	else:
		return 0

####################################################################################
### DamageSystem    (Update on GravityFXlib's version)
#########
# Helper function for DamageShip  
# This damages the given system (and all his child systems) with a random damage between the
# given Minimum and maximun.
# damages. Beware, it can destroy the system if he suffers to much damage, running out of 'health'.
###
# pSystem --> the system to damage
# MinDmg --> the minimum damage, remember it is damage points, and not percentage!	Check the torpedoes
#		 modules and their damages to get an idea.
# MaxDmg --> the maximum damage, remember it is damage points, and not percentage!
# returns --> the damage that was done.
####################################################################################
def Updated_DamageSystem(pSystem, MinDmg, MaxDmg):
	debug(__name__ + ", Updated_DamageSystem")
	Dmg = GetRandomInRange(MinDmg, MaxDmg)
	pParentShip = pSystem.GetParentShip()
	iNumChilds = pSystem.GetNumChildSubsystems()
	if iNumChilds >= 1:
		for i in range(iNumChilds):
			pChild = pSystem.GetChildSubsystem(i)
			if (pChild != None):
				pChild.SetCondition(pChild.GetCondition() - Dmg)
				if pParentShip and pChild.GetCondition() <= 0:
					pParentShip.DestroySystem(pChild)
	else:
		pSystem.SetCondition(pSystem.GetCondition() - Dmg)
		if pParentShip and pSystem.GetCondition() <= 0:
			pParentShip.DestroySystem(pSystem)		
	return Dmg

try:
	import Custom.GravityFX.GravityFXlib
	Custom.GravityFX.GravityFXlib.DamageSystem = Updated_DamageSystem
except:
	print "Galaxy Charts couldn't overwrite GravityFX DamageSystem function"
DamageSystem = Updated_DamageSystem

####################################################################################
### IsStation    (Update on GravityFXlib's version)
#########
# Checks if a ship is a station.
###
# pShip --> App.ShipClass obj to check
# returns --> 1 if ship is a station, 0 if not.
####################################################################################
def Updated_IsStation(pShip):
	debug(__name__ + ", Updated_IsStation")
	if pShip == None:
		return 0
	pRaceObj = GetRaceClassObj( GetShipRace(pShip) )
	sShipClass = GetShipType(pShip)
	if pRaceObj and sShipClass in pRaceObj.GetBases():
		return 1
	elif pShip.GetShipProperty().IsStationary() == 1:
		return 1
	return 0

try:
	import Custom.GravityFX.GravityFXlib
	Custom.GravityFX.GravityFXlib.IsStation = Updated_IsStation
except:
	print "Galaxy Charts couldn't overwrite GravityFX IsStation function"
IsStation = Updated_IsStation

####################################################################################
### ConvertDegreesToRadians and ConvertRadiansToDegrees
#########
# functions to convert a angle measurement in radians to degrees and vice-versa
###
# argument to pass to them is the angle value
####################################################################################
def ConvertDegreesToRadians(fDegrees):
	debug(__name__ + ", ConvertDegreesToRadians")
	return fDegrees * (math.pi / 180.0)

def ConvertRadiansToDegrees(fRadians):
	debug(__name__ + ", ConvertRadiansToDegrees")
	return fRadians * (180.0 / math.pi)

# convinient function names to the 2 above funcions
DegsToRads = ConvertDegreesToRadians
RadsToDegs = ConvertRadiansToDegrees

####################################################################################
### GetShipFundCost
#########
# This checks the amount of funds a ship (either a ShipClass obj or a ship script file path) 
# costs. Used by the War Simulator. 
# The fund cost is very variable, depending on pratically all aspects of the ship: hull/shields strength/size,
# weapons amount/power, has cloak, has tractor, etc. And even some techs.
###
# oShip --> either a App.ShipClass obj, or a string representing the name of the ship script.
# returns --> a float representing the fund cost amount.
#####
# NOTE: this function is a mess. plain and simple lol. A lot of strange (and relatively simple) math go around in it,
#	  in various shapes and sizes lol. But it works.
#	  If I missed something or didn't make all the possible checks to calculate the "cost" of the ship? Probably.
#	  But I know for sure that at least the most important stuff, and some other not-so-much-important things are being taken into consideration
#	  in the calculation of the ship's cost.
####################################################################################
def GetShipClassFundCost(sShipClass):
	debug(__name__ + ", GetShipClassFundCost")
	import GalacticWarSimulator
	return GalacticWarSimulator.WarSimulator.GetShipClassCost(sShipClass)

#  the '##>##' notation when commenting a line means: CHECK IT! there's still something missing to do here.

def GetShipFundCost(oShip, bIncludeEscorts = 1):
	debug(__name__ + ", GetShipFundCost")
	import Galaxy
	try:
		# start by getting the property set of the ship
		if type(oShip) == type(""):
			# oShip is a string
			# access the ship script file to get the hardpoint file name
			try:
				pShipScript = __import__("ships." + oShip)
			except ImportError:
				return 100.0
			sHardpointFile = pShipScript.GetShipStats()["HardpointFile"]

			# now try to import the hardpoint file
			try:
				pHardpoint = __import__("ships.Hardpoints." + sHardpointFile)
			except ImportError:
				return 100.0
			pPropertySet = App.TGModelPropertySet()
			App.g_kModelPropertyManager.ClearLocalTemplates()
			reload(pHardpoint)
			pHardpoint.LoadPropertySet(pPropertySet)
			pShipDef = GetShipDefByScript(oShip)
		else:
			# oShip is something else. Let's assume it's a ShipClass obj.
			pPropertySet = oShip.GetPropertySet()
			pShipDef = GetShipDef(oShip)
	
		# then get the property list from the property set, and start iterating thru the subsystem properties
		pPropertyList = pPropertySet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
		pPropertyList.TGBeginIteration()

		fTotalFunds = 0.0
		fPowerUsed = 0.0
		fCloakPower = 0.0
		pPowerProp = None
		for i in range(pPropertyList.TGGetNumItems()):
			# now we check the fund cost variation that this property gives to the ship.
			pShipProperty = App.SubsystemProperty_Cast(pPropertyList.TGGetNext().GetProperty())
		
			if pShipProperty != None:
				fMaxHP = pShipProperty.GetMaxCondition()
				bIsCritical = pShipProperty.IsCritical()
				bIsTargetable = pShipProperty.IsTargetable()
				bIsPrimary = pShipProperty.IsPrimary()
				fRepairComp = pShipProperty.GetRepairComplexity()
				fDisabledPerc = pShipProperty.GetDisabledPercentage()
				fRadius = pShipProperty.GetRadius()
				fSFF = 4.0    # System Fund Factor
				iFormulaType = 2

				if App.HullProperty_Cast(pShipProperty) != None:
					if bIsPrimary == 1:
						# ship hull
						fSFF = 2.0
						iFormulaType = 1
						#if bIsTargetable == 0:
						#	##>## primary hull not targetable?!? O_o
						#	pass
					else:
						# extra hull systems
						fSFF = 4.0
						iFormulaType = 2
						##>## check for grav generator, hiperdrive and slipstream.
						##>## for hiperdrive/slipstream: add a fixed, probably high, amount to fund cost.
				elif App.PowerProperty_Cast(pShipProperty) != None:
					pPower = App.PowerProperty_Cast(pShipProperty)
					pPowerProp = pPower
				elif App.CloakingSubsystemProperty_Cast(pShipProperty) != None:
					pCloakSys = App.CloakingSubsystemProperty_Cast(pShipProperty)
					fSFF = 4.0
					iFormulaType = 2
					if pCloakSys.GetCloakStrength() <= 0.0:
						fTotalFunds = fTotalFunds + 100.0
					else:
						fTotalFunds = fTotalFunds + (pCloakSys.GetCloakStrength() * 10.0)
					fCloakPower = pCloakSys.GetNormalPowerPerSecond()
				elif App.PoweredSubsystemProperty_Cast(pShipProperty) != None:
					pPoweredSys = App.PoweredSubsystemProperty_Cast(pShipProperty)
					if App.ImpulseEngineProperty_Cast(pPoweredSys) != None:
						pImpSys = App.ImpulseEngineProperty_Cast(pPoweredSys)
						iFormulaType = 3
						fTotalFunds = fTotalFunds + 200.0
						fMaxAccel = pImpSys.GetMaxAccel()
						fMaxAngularAccel = pImpSys.GetMaxAngularAccel()
						fTotalFunds = fTotalFunds + (10.0 * fMaxAccel * fMaxAngularAccel * pImpSys.GetMaxAngularVelocity() * pImpSys.GetMaxSpeed())
					elif App.WarpEngineProperty_Cast(pPoweredSys) != None:
						iFormulaType = 3
						fTotalFunds = fTotalFunds + 500.0
						##>## modify warp engine system cost value based on cruise/max warp speed.
					elif App.RepairSubsystemProperty_Cast(pPoweredSys) != None:
						pRepairSys = App.RepairSubsystemProperty_Cast(pPoweredSys)
						fSFF = 4.0
						iFormulaType = 2
						fTotalFunds = fTotalFunds + (pRepairSys.GetMaxRepairPoints() * pRepairSys.GetNumRepairTeams())
					elif App.SensorProperty_Cast(pPoweredSys) != None:
						pSensorSys = App.SensorProperty_Cast(pPoweredSys)
						fSFF = 4.0
						iFormulaType = 2
						fTotalFunds = fTotalFunds + ((pSensorSys.GetMaxProbes() * 45.0) + (pSensorSys.GetBaseSensorRange() / 20.0))
					elif App.ShieldProperty_Cast(pPoweredSys) != None:
						pShieldSys = App.ShieldProperty_Cast(pPoweredSys)
						fSFF = 4.0
						iFormulaType = 2
						FRONT_MaxShields = pShieldSys.GetMaxShields(pShieldSys.FRONT_SHIELDS)
						REAR_MaxShields = pShieldSys.GetMaxShields(pShieldSys.REAR_SHIELDS)
						TOP_MaxShields = pShieldSys.GetMaxShields(pShieldSys.TOP_SHIELDS)
						BOTTOM_MaxShields = pShieldSys.GetMaxShields(pShieldSys.BOTTOM_SHIELDS)
						LEFT_MaxShields = pShieldSys.GetMaxShields(pShieldSys.LEFT_SHIELDS)
						RIGHT_MaxShields = pShieldSys.GetMaxShields(pShieldSys.RIGHT_SHIELDS)
						FRONT_ShieldCharge = pShieldSys.GetShieldChargePerSecond(pShieldSys.FRONT_SHIELDS)
						REAR_ShieldCharge = pShieldSys.GetShieldChargePerSecond(pShieldSys.REAR_SHIELDS)
						TOP_ShieldCharge = pShieldSys.GetShieldChargePerSecond(pShieldSys.TOP_SHIELDS)
						BOTTOM_ShieldCharge = pShieldSys.GetShieldChargePerSecond(pShieldSys.BOTTOM_SHIELDS)
						LEFT_ShieldCharge = pShieldSys.GetShieldChargePerSecond(pShieldSys.LEFT_SHIELDS)
						RIGHT_ShieldCharge = pShieldSys.GetShieldChargePerSecond(pShieldSys.RIGHT_SHIELDS)
						fTotalFunds = fTotalFunds + ((FRONT_MaxShields + REAR_MaxShields + TOP_MaxShields + BOTTOM_MaxShields + LEFT_MaxShields + RIGHT_MaxShields) / 60.0)
						fTotalFunds = fTotalFunds + (FRONT_ShieldCharge + REAR_ShieldCharge  + TOP_ShieldCharge + BOTTOM_ShieldCharge + LEFT_ShieldCharge + RIGHT_ShieldCharge)
					elif App.WeaponSystemProperty_Cast(pPoweredSys) != None:
						pWeaponSys = App.WeaponSystemProperty_Cast(pPoweredSys)
						if pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_TRACTOR:
							fTotalFunds = fTotalFunds + 300.0
						elif pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_TORPEDO:
							fTotalFunds = fTotalFunds + 120.0
							pTorpSys = App.TorpedoSystemProperty_Cast(pPoweredSys)
							if pTorpSys != None:
								for index in range(pTorpSys.GetNumAmmoTypes()):
									sTorpScript = pTorpSys.GetTorpedoScript(index)
									iTorpAmmo = pTorpSys.GetMaxTorpedoes(index)
									try:
										pTorp = __import__(sTorpScript)
										fDmg = pTorp.GetDamage()
										torpcost = (fDmg+(pTorp.GetLaunchSpeed()*pTorp.GetGuidanceLifetime()*pTorp.GetMaxAngularAccel()*fDmg))/10000.0
									except:
										Galaxy.LogError("LIB_GetShipFundCost: couldn't acquire torpedo: "+str(sTorpScript))
										torpcost = 0.0
									##>## add torpedo tech cost value amunt here to the torpcost variable.
									##>## besides checking by FTech, check for torpedo gravity effect.
									fTotalFunds = fTotalFunds + (torpcost * iTorpAmmo)
						elif pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_PULSE:
							fTotalFunds = fTotalFunds + 200.0
						elif pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_PHASER:
							fTotalFunds = fTotalFunds + 250.0
						iFormulaType = 3
					fPowerUsed = fPowerUsed + pPoweredSys.GetNormalPowerPerSecond()
				elif App.EngineProperty_Cast(pShipProperty) != None:
					pEngine = App.EngineProperty_Cast(pShipProperty)
					fSFF = 4.0
					iFormulaType = 2
					if pEngine.GetEngineType() == pEngine.EP_WARP:
						fSFF = 2.0
				elif App.WeaponProperty_Cast(pShipProperty) != None:
					pWeapon = App.WeaponProperty_Cast(pShipProperty)
					fSFF = 5.0
					iFormulaType = 2
					if App.TorpedoTubeProperty_Cast(pWeapon) != None:
						pTube = App.TorpedoTubeProperty_Cast(pWeapon)
						fImmediateDelay = pTube.GetImmediateDelay()
						fMaxReady = pTube.GetMaxReady()
						if fMaxReady != 0.0:
							secondstofireonetorp = ((((fMaxReady * fImmediateDelay) - fImmediateDelay) + pTube.GetReloadDelay()) / fMaxReady)
						else:
							secondstofireonetorp = 0
						if secondstofireonetorp != 0.0:
							torpsfiredpersecond = 1.0 / secondstofireonetorp
						else:
							torpsfiredpersecond = 0.1
						fTotalFunds = fTotalFunds + (torpsfiredpersecond * 200.0)
					elif App.TractorBeamProperty_Cast(pWeapon) != None:
						pTractor = App.TractorBeamProperty_Cast(pWeapon)
						fSFF = 4.0
						fTotalFunds = fTotalFunds + ((pTractor.GetMaxDamage() + pTractor.GetMaxDamageDistance()) / 2.0)
					elif App.PulseWeaponProperty_Cast(pWeapon) != None:
						pPulseWeapon = App.PulseWeaponProperty_Cast(pWeapon)
						try:
							pPulse = __import__(pPulseWeapon.GetModuleName())
							fDmg = pPulse.GetDamage()
							if hasattr(pPulse, "GetLifetime") == 1:
								fLifetime = pPulse.GetLifetime()
							else:
								fLifetime = 0.1
							pulsecost = (fDmg + (pPulse.GetLaunchSpeed() * pPulse.GetMaxAngularAccel() * fLifetime * fDmg)) / 10.0
						except:
							Galaxy.LogError("LIB_GetShipFundCost: couldn't acquire pulse: "+str(pPulseWeapon.GetModuleName()))
							pulsecost = 0.0
						##>## maybe try to check if the pulse has some special tech (by Foundation Tech). If there isn't a way to calculate a approximate
						##>## cost value for the tech, which will probably happen, multiply the pulsecost by 5.0
						##>## besides checking by FTech, check for torpedo gravity effect.
						fMaxCharge = pPulseWeapon.GetMaxCharge()
						if pPulseWeapon.GetNormalDischargeRate() != 0.0 and pPulseWeapon.GetMinFiringCharge() != 0.0:
							ShotsFactor = ((fMaxCharge / pPulseWeapon.GetNormalDischargeRate()) / pPulseWeapon.GetMinFiringCharge())
						else:
							ShotsFactor = 0.0
						if ShotsFactor != 0.0 and pPulseWeapon.GetRechargeRate() != 0.0:
							secsforoneshot = ( ((ShotsFactor*pPulseWeapon.GetCooldownTime())+(fMaxCharge/pPulseWeapon.GetRechargeRate()))/ShotsFactor )
						else:
							secsforoneshot = 0.0
						if secsforoneshot != 0.0:
							shotspersec = 1.0/ secsforoneshot
						else:
							shotspersec = 0.01
						fTotalFunds = fTotalFunds + (pulsecost * shotspersec)
					elif App.PhaserProperty_Cast(pWeapon) != None:
						pBeam = App.PhaserProperty_Cast(pWeapon)
						fMaxCharge = pBeam.GetMaxCharge()
						beamcost = (fMaxCharge + pBeam.GetMaxDamageDistance() + (fMaxCharge * pBeam.GetDamageRadiusFactor())) / 2.0
						fTotalFunds = fTotalFunds + beamcost
				if iFormulaType == 1:
					fTotalFunds = fTotalFunds + ((fMaxHP + ((bIsCritical-1) * -0.8 * fMaxHP) + (fRepairComp * (fMaxHP/50.0)))/fSFF)
				elif iFormulaType == 2:
					fTotalFunds = fTotalFunds + ((fMaxHP + (bIsCritical* -0.8 * fMaxHP) + (fRepairComp * (fMaxHP/75.0)))/fSFF)
				elif iFormulaType == 3:
					pass

		# finish iterating...
		pPropertyList.TGDoneIterating()
		pPropertyList.TGDestroy()

		# before continuing, and after going thru all subsystems, we check the power property we stored because she should be checked in the end.
		if pPowerProp != None:
			fMaxHP = pShipProperty.GetMaxCondition()
			bIsCritical = pShipProperty.IsCritical()
			fRepairComp = pShipProperty.GetRepairComplexity()
			fTotalFunds = fTotalFunds + ((fMaxHP + ((bIsCritical-1) * -0.8 * fMaxHP) + (fRepairComp * (fMaxHP/50.0)))/2.0)
			fTotalFunds = fTotalFunds + ((pPowerProp.GetMainConduitCapacity() - pPowerProp.GetPowerOutput()) + pPowerProp.GetBackupConduitCapacity())
			fTotalFunds = fTotalFunds + ((pPowerProp.GetPowerOutput() - fPowerUsed)*2)
			if fCloakPower > 0.0:
				fTotalFunds = fTotalFunds + ((pPowerProp.GetBackupBatteryLimit() / fCloakPower) * 10.0)

		# now acquire and iterate thru the object emmiter properties. Since we need to check them, and they aren't classed as subsystems.
		pOEPList = pPropertySet.GetPropertiesByType(App.CT_OBJECT_EMITTER_PROPERTY)
		pOEPList.TGBeginIteration()

		for i in range(pOEPList.TGGetNumItems()):
			# now we check the fund cost variation that this property gives to the ship.
			pOEP = App.ObjectEmitterProperty_Cast(pOEPList.TGGetNext().GetProperty())
			if pOEP != None:
				if pOEP.GetEmittedObjectType() == pOEP.OEP_SHUTTLE:
					fTotalFunds = fTotalFunds + 1000.0
					##>## also, if possible, get the ship types that the ship can launch, and their amount, and add their cost to this ship's 
					##>## cost. maybe make it UMM selectable.
				elif pOEP.GetEmittedObjectType() == pOEP.OEP_PROBE:
					fTotalFunds = fTotalFunds + 100.0		

		# finish iterating...
		pOEPList.TGDoneIterating()
		pOEPList.TGDestroy()

		# now check for ship based FoundationTech techs this ship has.
		if hasattr(pShipDef, "dTechs") == 1:
			for sTechName in pShipDef.dTechs.keys():
				if sTechName == "Ablative Armour":
					oAblative = pShipDef.dTechs[sTechName]
					if type(oAblative) == type([]):
						fAblativeCost = oAblative[0] * 2
					else:
						fAblativeCost = oAblative * 2
					fTotalFunds = fTotalFunds + fAblativeCost
				elif sTechName == "Regenerative Shields":
					oRegShields = pShipDef.dTechs[sTechName]
					if oRegShields != 0.0:
						fTotalFunds = fTotalFunds + (7000.0 / oRegShields)
				elif sTechName == "Multivectral Shields":
					oMultShields = pShipDef.dTechs[sTechName]
					if oMultShields != 0.0:
						fTotalFunds = fTotalFunds + (6000.0 / (100.0 / oMultShields))
				elif sTechName == "Reflector Shields":
					oReflecShields = pShipDef.dTechs[sTechName]
					if oReflecShields != 0.0:
						fTotalFunds = fTotalFunds + (10000.0 / (100.0 / oReflecShields))
				elif sTechName == "Phase Cloak":
					oPhaseCloak = pShipDef.dTechs[sTechName]
					fTotalFunds = fTotalFunds + 10000.0
				elif sTechName == "Breen Drainer Immune":
					oBDI = pShipDef.dTechs[sTechName]
					fTotalFunds = fTotalFunds + 3000.0
				elif sTechName == "Fed Ablative Armor":
					oFedArmor = pShipDef.dTechs[sTechName]
					lPlateList = oFedArmor['Plates']
					fTotalFunds = fTotalFunds + (2500.0 * len(lPlateList))
				elif sTechName == "AdvancedHull":
					oAdvHull = pShipDef.dTechs[sTechName]
					for sSubsystem in oAdvHull.keys():
						fChance = oAdvHull[sSubsystem][0]
						fDmgPerc = oAdvHull[sSubsystem][1]
						fTotalFunds = fTotalFunds + (2000.0 - (20.0 * fChance)) + (2000.0 - (20.0 * fDmgPerc))
				elif sTechName == "AutoTargeting":
					oAutoTarget = pShipDef.dTechs[sTechName]
					for sWeaponType in oAutoTarget.keys():	
						if sWeaponType in ["Pulse", "Phaser", "Torpedo"]:
							iMaxSecTargets = oAutoTarget[sWeaponType][0]
							iMaxSysTargets = oAutoTarget[sWeaponType][1]
							fTotalFunds = fTotalFunds + (100.0 * (iMaxSecTargets + iMaxSysTargets))
				else:
					fTotalFunds = fTotalFunds + 5000.0

		# now check for escorts, and add their price for this ship.
		if bIncludeEscorts == 1:
			sShipRace = GetShipDefRace(pShipDef)
			pRaceObj = GetRaceClassObj(sShipRace)
			if pRaceObj != None:
				lEscorts = pRaceObj.GetEscorts(pShipDef.shipFile)
				if lEscorts != None:
					for sEscort in lEscorts:
						# now get the escort ship price, BUT SRYLY, DON'T TRY TO GET the price of the escorts of the escort ship.
						# or that may create an infinite web of escorts, and thus an infinite loop here that will kill BC...
						fTotalFunds = fTotalFunds + GetShipFundCost(sEscort, 0)

		pGodRace = GetRaceClassObj("GodShips")
		if pShipDef != None and pGodRace != None:
			if pShipDef.shipFile in pGodRace.myShips:
				#ship is a god ship, slightly increase it's cost :P
				fTotalFunds = fTotalFunds + 150000.0

		#apply ShipDef value modifier
		if hasattr(pShipDef, "fShipCostModifier"):
			fValueToAdd = pShipDef.fShipCostModifier
			if (fTotalFunds + fValueToAdd) >= 100.0:
				fTotalFunds = fTotalFunds + fValueToAdd

		# and finally return the cost.
		return fTotalFunds
	except:
		Galaxy.LogError("LIB_GetShipFundCost: couldn't calculate ship cost")
		return 100.0


def ModifyShipListByCost(lShipDefs, fMinCost, fMaxCost):
	debug(__name__ + ", ModifyShipListByCost")
	lRetShipDefs = []
	for pShipDef in lShipDefs:
		sShipClass = pShipDef.shipFile
		fCost = GetShipClassFundCost(sShipClass)
		if fMinCost <= fCost <= fMaxCost:
			lRetShipDefs.append(pShipDef)
	return lRetShipDefs

def GetMinShipCostInList(lShipDefs):
	debug(__name__ + ", GetMinShipCostInList")
	fCost = -1
	for pShipDef in lShipDefs:
		sShipClass = pShipDef.shipFile
		fShipCost = GetShipClassFundCost(sShipClass)
		if fCost == -1 or fShipCost < fCost:
			fCost = fShipCost
	return fCost
