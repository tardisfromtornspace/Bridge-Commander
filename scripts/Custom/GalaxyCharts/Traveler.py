from bcdebug import debug
######################################################################################################################
#######         Traveler  Script             #########################################################################
######################################################################################################################
#################        by Fernando Aluani aka USS Frontier
######################################################################################################################
#         <<   The  Traveler System          >>
#  This is the script that contains the Traveler system code, and strictly related functions.
#  The Traveler system is the travelling system that replaces the stock BC's warp method, and does so a lot more 
#  functionality (and possibly extensibility).
#  Contains the TravelManager, Travel, Chaser and EngineStatus classes, plus various helper functions used around here.
######################################################################################################################

import App
import time
import nt
import string
import MissionLib
import BridgeHandlers
import Galaxy
import GalaxyMapGUI
import HelmAddonGUI
import SystemAnalysisGUI
import WarpSequence_Override
from GalaxyLIB import *
import TravelerSystems.AISpaceSet
import LibStarstreaks
import Custom.GravityFX.Logger
import Bridge.HelmMenuHandlers
from GalacticWarSimulator import WarSimulator, FleetManager, WSShip

################
# Global Variables
#####
ET_RDF_TRIGGER = App.UtopiaModule_GetNextEventType()

################
# Variables Names Remarks
#####
# sDestination is the region script of the destination set


class TravelManager:
	def __init__(self):
		debug(__name__ + ", __init__")
		global g_dTowingToToweeMatches
		self.CLASS = "Travel Manager"
		self.__ID = GetUniqueID("TravelManager")
		self.ToweeIDList = []
		self.bFiredPlaFixTimer = 0
		self.TravelProps = {}
		self.IsGamePaused = 0
		self.TimePaused = 0
		self.dTravelTypes = {}
		self.bLoadedPlugins = 0
		self.LoadTravelTypes()
	def LoadTravelTypes(self):
		debug(__name__ + ", LoadTravelTypes")
		if self.bLoadedPlugins == 1:
			return

		TTList = nt.listdir('scripts/Custom/TravellingMethods')

		lToBeRemoved = ['__init__.py', '__init__.pyc']
		for sRemovee in lToBeRemoved:
			if sRemovee in TTList:
				TTList.remove(sRemovee)

		lLoadedPlugins = []
		sPathToPlugins = "Custom.TravellingMethods."
		lAttrsToCheckFor = ['sName', 'bIsShipBased', 'bCanTowShips', 'sDegradationSoundFile', 'bUseStarstreaks', 'bCanDropOut',
					 'bCanChangeCourse', 'sGoingTo', 'sDropOut', 'CanTravel', 'CanContinueTravelling', 'PreEngageStuff', 'PreExitStuff', 
					 'SetupSequence', 'GetStartTravelEvents', 'GetExitedTravelEvents', 'GetTravelSetToUse', 'IsShipEquipped', 'bCanTriggerRDF',
					 'ConvertSpeedAmount', 'GetMaxSpeed', 'GetCruiseSpeed', 'GetActualMaxSpeed', 'GetActualCruiseSpeed', 'fMinimumSpeed',
					 'fMaximumSpeed', 'GetDegradationSystems', 'bCanChangeSpeed', 'GetLaunchCoordinatesList', 'fLaunchRadius', 
					 'iRestrictionFlag', 'GetEngageDirection']

		for sFile in TTList:
			sFileStrings = string.split(sFile, '.')
			sPlugin = sFileStrings[0]
			sExt = sFileStrings[-1]
			if (sExt == "py" or sExt == "pyc") and (not sPlugin in lLoadedPlugins):
				lLoadedPlugins.append(sPlugin)
				pModule = __import__(sPathToPlugins + sPlugin)
				bIsOK = 1
				for sAttr in lAttrsToCheckFor:
					if pModule.__dict__.has_key(sAttr) == 0:
						print "TravellingMethod ERROR:", pModule.__name__, "plugin does not have the attribute:", sAttr
						bIsOK = 0
						break
				if bIsOK == 1:
					self.dTravelTypes[pModule.sName] = pModule
		self.bLoadedPlugins = 1
	def GetAllTravelTypes(self):
		debug(__name__ + ", GetAllTravelTypes")
		return self.dTravelTypes.keys()
	def HasTravelType(self, sTravelType):
		debug(__name__ + ", HasTravelType")
		if self.dTravelTypes.has_key(sTravelType):
			return 1
		else:
			return 0
	def GetTravelTypeAttr(self, sTravelType, sAttrName):
		debug(__name__ + ", GetTravelTypeAttr")
		if sTravelType == "" or sTravelType == "None":
			return None
		if self.dTravelTypes.has_key(sTravelType):
			pTravelModule = self.dTravelTypes[sTravelType]
			if pTravelModule.__dict__.has_key(sAttrName):
				return pTravelModule.__dict__[sAttrName]
			else:
				Galaxy.Logger.LogString("TravelerManager: couldn't find atribute named "+str(sAttrName)+" in Travel Type Plugin "+str(sTravelType))
				return None
		else:
			Galaxy.Logger.LogString("TravelerManager: couldn't find Travel Type named "+str(sTravelType))
			return None
	def IsShipEquippedWithTravelType(self, pShip, sTravelType):
		debug(__name__ + ", IsShipEquippedWithTravelType")
		try:
			if self.IsTravelTypeShipBased(sTravelType) == 0:
				return 0
			if sTravelType == "" or sTravelType == "None":
				return 0
			pFunc = self.GetTravelTypeAttr(sTravelType, "IsShipEquipped")
			oRet = pFunc(pShip)
			if type(oRet) == type(1):
				return oRet
			else:
				Galaxy.Logger.LogError("TravelManager: Travel Type "+sTravelType+" IsShipEquipped method returns a "+str(type(oRet))+", not a bool (integer).")
				return 0
		except:
			Galaxy.LogError("TravelManager_IsShipEquippedWithTravelType")
	# IsShipInLaunchPosFor
	# returns None if ship can't use given non-ship-based travelling method
	# return a world coord if the ship is in good position.
	def IsShipInLaunchPosFor(self, pShip, sTravelType):
		debug(__name__ + ", IsShipInLaunchPosFor")
		if self.IsTravelTypeShipBased(sTravelType) == 1:
			return None
		if sTravelType == "" or sTravelType == "None":
			return None
		fLaunchRadius = self.GetTravelTypeAttr(sTravelType, "fLaunchRadius")
		if type(fLaunchRadius) != type(1.0):
			Galaxy.Logger.LogError("TravelManager: Travel Type "+sTravelType+" fLaunchRadius attribute returns a "+str(type(fLaunchRadius))+", not a float.")
			return None
		pSet = pShip.GetContainingSet()
		if pSet == None:
			return None
		lList = self.GetLaunchCoordinatesForTT(sTravelType, pSet)
		for vPos in lList:
			if DistanceOfPoints(pShip.GetWorldLocation(), vPos) <= ConvertKMtoGU(fLaunchRadius):
				return vPos
		return None
	def IsTravelTypeShipBased(self, sTravelType):
		debug(__name__ + ", IsTravelTypeShipBased")
		try:
			oRet = self.GetTravelTypeAttr(sTravelType, "bIsShipBased")
			if sTravelType == "" or sTravelType == "None":
				return 0
			if type(oRet) == type(1):
				return oRet
			else:
				Galaxy.Logger.LogError("TravelManager: Travel Type "+sTravelType+" bIsShipBased attribute returns a "+str(type(oRet))+", not a bool (integer).")
				return 1
		except:
			Galaxy.LogError("TravelManager_IsTravelTypeShipBased")
	# this only returns travel types equipped on the ship
	def GetAllTravelTypesInShip(self, pShip):
		debug(__name__ + ", GetAllTravelTypesInShip")
		lList = []
		for sTravelType in self.dTravelTypes.keys():
			if self.IsShipEquippedWithTravelType(pShip, sTravelType) == 1:
				lList.append(sTravelType)
		lList.sort()
		return lList
	# this returns travel types equipped on the ship and non-ship-based travel methods which the ship can currently activate
	#                                                      (she's on a launch coordinate)
	def GetAllTTAvailableForShip(self, pShip):
		debug(__name__ + ", GetAllTTAvailableForShip")
		lList = []
		for sTravelType in self.dTravelTypes.keys():
			if self.IsShipEquippedWithTravelType(pShip, sTravelType) == 1:
				lList.append(sTravelType)
			elif self.IsTravelTypeShipBased(sTravelType) == 0:
				if self.IsShipInLaunchPosFor(pShip, sTravelType) != None:
					lList.append(sTravelType)
		lList.sort()
		return lList
	def CanTravelTypeTriggerRDF(self, sTravelType):
		debug(__name__ + ", CanTravelTypeTriggerRDF")
		try:
			if sTravelType == "" or sTravelType == "None":
				return 0
			oRet = self.GetTravelTypeAttr(sTravelType, "bCanTriggerRDF")
			if type(oRet) == type(1):
				return oRet
			else:
				Galaxy.Logger.LogError("TravelManager: Travel Type "+sTravelType+" bCanTriggerRDF attribute returns a "+str(type(oRet))+", not a bool (integer).")
				return 1
		except:
			Galaxy.LogError("TravelManager_CanTravelTypeTriggerRDF")
	def ConvertTravelTypeSpeedIntoCs(self, sTravelType, fSpeed):
		debug(__name__ + ", ConvertTravelTypeSpeedIntoCs")
		try:
			if sTravelType == "" or sTravelType == "None":
				return 0.0
			pFunc = self.GetTravelTypeAttr(sTravelType, "ConvertSpeedAmount")
			oRet = pFunc(fSpeed)
			if type(oRet) == type(1.0):
				return oRet
			else:
				Galaxy.Logger.LogError("TravelManager: Travel Type "+sTravelType+" ConvertSpeedAmount method returns a "+str(type(oRet))+", not a float.")
				return 1079252848.8   # = 1 time speed-of-light
		except:
			Galaxy.LogError("TravelManager_ConvertTravelTypeSpeedIntoCs")
	def GetLaunchCoordinatesForTT(self, sTravelType, pSet):
		debug(__name__ + ", GetLaunchCoordinatesForTT")
		try:
			if sTravelType == "" or sTravelType == "None":
				return 0.0
			pFunc = self.GetTravelTypeAttr(sTravelType, "GetLaunchCoordinatesList")
			oRet = pFunc(pSet)
			if type(oRet) == type([]):
				return oRet
			else:
				Galaxy.Logger.LogError("TravelManager: Travel Type "+sTravelType+" GetLaunchCoordinatesList method returns a "+str(type(oRet))+", not a list.")
				return []
		except:
			Galaxy.LogError("TravelManager_GetLaunchCoordinatesForTT")
	def CreateTravel(self, ship, sDestination = ""):
		debug(__name__ + ", CreateTravel")
		travel = self.GetTravel(ship)
		if travel == None:
			travel = Travel(ship, sDestination)
			self.TravelProps[ship.GetObjID()] = travel
			pTWS = WarpSequence_Override.TravelerWarpSequence(travel)
			travel.TravelerSequence = pTWS
		return travel
	def CreateChaser(self, ship, target, sDestination = ""):
		debug(__name__ + ", CreateChaser")
		chaser = self.GetTravel(ship)
		if chaser == None:
			chaser = Chaser(ship, target, sDestination)
			self.TravelProps[ship.GetObjID()] = chaser
			pTWS = WarpSequence_Override.TravelerWarpSequence(chaser)
			chaser.TravelerSequence = pTWS
		else:
			if chaser.CLASS == "Ship Travel":
				self.DeleteTravel(ship)
				chaser = self.CreateChaser(ship, target, sDestination)
		return chaser
	def EngageTravelToOfShip(self, ship, sDestination, sTravelType = ""):
		debug(__name__ + ", EngageTravelToOfShip")
		travel = self.CreateTravel(ship)
		return travel.TravelTo(sDestination, sTravelType)
	def ChangeDestinationOfShip(self, ship, sNewDestination):
		debug(__name__ + ", ChangeDestinationOfShip")
		travel = self.GetTravel(ship)
		if travel != None:
			travel.SetDestination(sNewDestination)
	def MakeShipDropOutOfTravel(self, ship):
		debug(__name__ + ", MakeShipDropOutOfTravel")
		travel = self.GetTravel(ship)
		if travel != None:
			travel.DropOutOfTravel()
	def IsShipTravelling(self, ship):
		debug(__name__ + ", IsShipTravelling")
		travel = self.GetTravel(ship)
		if travel != None:
			return travel.IsTravelling()
		else:
			return 0
	def IsAnyShipTravelling(self):
		debug(__name__ + ", IsAnyShipTravelling")
		for travel in self.TravelProps.values():
			if travel.IsTravelling() == 1:
				return 1
		return 0
	def GetTravel(self, ship):
		debug(__name__ + ", GetTravel")
		if ship == None:
			return None
		if self.TravelProps.has_key(ship.GetObjID()):
			return self.TravelProps[ship.GetObjID()]
		else:
			return None
	def GetTravelByID(self, id):
		debug(__name__ + ", GetTravelByID")
		if id == None:
			return None
		if self.TravelProps.has_key(id):
			return self.TravelProps[id]
		else:
			return None
	def GetAllTravels(self):
		debug(__name__ + ", GetAllTravels")
		return self.TravelProps.values()
	def SetToweeShip(self, ship, bStat):
		debug(__name__ + ", SetToweeShip")
		if ship == None:	return
		if bStat not in [0, 1, None]:
			return
		ID = ship.GetObjID()
		if ID not in self.ToweeIDList and bStat == 1:
			self.ToweeIDList.append(ID)
		elif ID in self.ToweeIDList and bStat in [0, None]:
			self.ToweeIDList.remove(ID)
	def IsShipBeingTowed(self, ship):
		debug(__name__ + ", IsShipBeingTowed")
		if ship == None:	return
		id = ship.GetObjID()
		if id in self.ToweeIDList:
			return 1
		else:
			return 0
	def TravelerPauseCheck(self, bIsPaused):
		debug(__name__ + ", TravelerPauseCheck")
		if self.IsGamePaused == 0 and bIsPaused == 1:
			# game is pausing... store values
			self.TimePaused = time.clock()
			self.IsGamePaused = 1
		elif self.IsGamePaused == 1 and bIsPaused == 0:
			# game is unpausing, update the entire Traveler system
			fClock = time.clock()
			fTimeInPause = fClock - self.TimePaused
			for pTravel in self.TravelProps.values():
				if pTravel.Started == 1:
					pTravel.PausedTimeUpdateCheck = fTimeInPause
			self.TimePaused = 0			
			self.IsGamePaused = 0
		return
	def DeleteTravel(self, ship):
		debug(__name__ + ", DeleteTravel")
		travel = self.GetTravel(ship)
		if travel != None:
			pPlayer = App.Game_GetCurrentPlayer()
			if travel.Started == 1:
				if pPlayer != None and pPlayer.GetObjID() == ship.GetObjID() and self.bFiredPlaFixTimer == 0:
					# Player was destroyed in-warp... Move him to his initial set then, otherwise he might end up
					# being re-created in the travel set, which is a bad thing.
					MissionLib.CreateTimer(GetNextEventType(), __name__ + ".PlayerDeleteTravellingFix", App.g_kUtopiaModule.GetGameTime() + 10.0, 0, 0)
					self.bFiredPlaFixTimer = 1
					return
				if pPlayer != None and pPlayer.GetObjID() == ship.GetObjID() and self.bFiredPlaFixTimer == 1:
					pOldSet = ship.GetContainingSet()
					pOldSet.RemoveObjectFromSet(ship.GetName())
					travel.InitialShipSet.AddObjectToSet(ship, ship.GetName())
					self.bFiredPlaFixTimer = 0
			if travel.Refresher != None:
				if travel.Refresher._Refresher != None:
					travel.Logger.LogString("Stopping Refresh Handler")
					travel.Refresher.StopRefreshHandler()
					#del travel.Refresher
			travel.Logger.LogString("Deleting...")
			del travel
			del self.TravelProps[ship.GetObjID()]

App.g_kTravelManager = TravelManager()

class Travel:
	pAITravelSet = None   # Traveler system sets
	pTravelSet = None
	pSpaceSet = None
	pNebSet = None
	
	NOT_ENGAGING = 0   # enumeration used to check the status of the travelling procedure (both normal warp and 
	ENGAGING = 1       # in-system warp (intercept) )
	ENGAGED = 2
	EXITING = 3

	def __init__(self, pShip, sDestination):
		# now we initialize the class instance attributes.
		debug(__name__ + ", __init__")
		self.Ship = pShip
		self.CLASS = "Ship Travel"
		self.__ID = GetUniqueID(pShip.GetName()+"("+str(pShip.GetObjID())+") Travel")
		if GetConfigValue("LogTravel") == 1:
			self.Logger = Custom.GravityFX.Logger.LogCreator(pShip.GetName()+" Travel Logger", "scripts\Custom\GalaxyCharts\Logs\Travel_"+pShip.GetName()+"_LOG.txt")
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
		self.Logger.AddStaticStringToDTS("Updating Travelling Procedures...")
		self.Logger.AddStaticStringToDTS(" -Update Loop MARK START")
		self.Logger.AddVariableStringToDTS(" -Time left:")
		self.Logger.AddStaticStringToDTS(" -Update Loop MARK COMPLETED")
		self.Logger.LogDynamicTS()
		self.Logger.LogString("Initialized "+pShip.GetName()+" Travel logger")
		self.Logger.LogString("SELF = "+self.__repr__())
		# most of these variables are updated in the UpdateVariables method.
		self.CheckedMVAM = 0
		self.CheckedCoreEject = 0
		self.CheckedAddShips = 0
		self.CheckedLaunchShuttles = 0
		self.CheckedAbandonShip = 0
		self.CheckedAbandonShipMenu = 0
		self.CheckedTransporter = 0
		self.CheckedSetCourse = 0
		self.IsPlayer = 0
		self.IsAIinPlayerRoute = 0
		self.fInitialClock = 0
		self.fLastClock = 0
		self.PausedTimeUpdateCheck = 0
		self.DegradationAlert = None
		# this will be properly updated in the UpdateVariables method
		self.InitialShipSet = None
		self.DestinationScript = ""
		self.DestSet = None
		self.AlreadyStoppedIntercept = 0
		self.InterceptTarget = None
		self.InterceptStopDist = ConvertKMtoGU(900.0)
		self.InterceptStatus = self.NOT_ENGAGING
		self.TravelValues = {}
		self.TimeToReach = 0   # this is the total time needed to travel                # both times in secs
		self.TimeLeft = 0      # this is the time there's left to reach the destination #
		self.Refresher = None
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		self.TravelerSequence = None
		self.ImpulseStatus = EngineStatus(self)
		self.TravelBlindly = 0
		self.Started = 0
		self.StartWarpEvents = []
		self.ArrivedEvents = []
		self.SeqStat = self.NOT_ENGAGING
		self.DegradeSoundCheck = 0
		self.DegradationAlert = None
		self.AIwarpPower = 1.0
		self.IsTurning = 0
		self.EnableTowing = 1      ##
		self.Towee = None          ##   For Tractoring a ship thru travel
		self.bTractorStat = 0      ##
		self.vTowPosition = None   ##
		self.StreaksNode = None
		self.LTVUPOS = None        ##   Last Travel Values Update position
		self.dSysRestrictionF2 = {}
		self.bStrangeNebula = 0
		lPTT = App.g_kTravelManager.GetAllTravelTypesInShip(self.Ship)
		if "Warp" in lPTT:
			self.__travelType = "Warp"
		elif len(lPTT) >= 1:
			self.__travelType = lPTT[0]
		else:
			self.__travelType = "None"
		self.Logger.LogString("Initial Travel Type: "+self.__travelType)
		self.__speedAmount = -1.0
		self.__launchPos = None
		self.SetSpeed(self.GetActualCruiseSpeed())
		self.UpdateVariables()
		self.SetDestination(sDestination)
		self.SetExitPlacementName(None)
		self.SetExitLocationVector(None)
	def UpdateVariables(self):
		debug(__name__ + ", UpdateVariables")
		try:
			self.Logger.LogString("Updating Variables...")
			# check to see if ship exists...
			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString(" -Ship is dead or dying")
				return
			# first of all we create these 2 sets we may use, if they aren't.
			if Travel.pAITravelSet == None:
				import TravelerSystems.AITravelSet
				Travel.pAITravelSet = TravelerSystems.AITravelSet.Initialize()
				self.Logger.LogString(" -Initialized AI Travel Set")
			if Travel.pTravelSet == None:
				import TravelerSystems.TravelSet
				Travel.pTravelSet = TravelerSystems.TravelSet.Initialize()
				self.Logger.LogString(" -Initialized Travel Set")
			if Travel.pSpaceSet == None:
				import TravelerSystems.SpaceSet
				Travel.pSpaceSet = TravelerSystems.SpaceSet.Initialize()
				self.Logger.LogString(" -Initialized Space Set")
			self.CheckedMVAM = 0
			self.CheckedCoreEject = 0
			self.CheckedAddShips = 0
			self.CheckedLaunchShuttles = 0
			self.CheckedAbandonShip = 0
			self.CheckedAbandonShipMenu = 0
			self.CheckedTransporter = 0
			self.CheckedSetCourse = 0
			pPlayer = App.Game_GetCurrentPlayer()
			self.IsPlayer = 0
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipEnteredSet")
			if pPlayer != None and self.Ship.GetObjID() == pPlayer.GetObjID():
				self.IsPlayer = 1
				self.Logger.LogString(" -Is Player - Checked")
				App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipEnteredSet")
			self.InitialShipSet = self.Ship.GetContainingSet()
			self.IsAIinPlayerRoute = 0
			if pPlayer and self.IsPlayer == 0:
				pPlaTravel = App.g_kTravelManager.GetTravel(pPlayer)
				if pPlaTravel != None:
					self.Logger.LogString(" -Is AI in Player in route CHECKING: Player Travel OK")
					if pPlaTravel.DestSet != None:
						self.Logger.LogString(" -Is AI in Player in route CHECKING: Player Travel Destination OK")
				if self.DestSet != None:
					self.Logger.LogString(" -Is AI in Player in route CHECKING: self Destination OK")
				if pPlaTravel != None and pPlaTravel.DestSet != None and pPlaTravel.InitialShipSet != None and self.DestSet != None and self.InitialShipSet != None:
					sPlaSetName = pPlaTravel.InitialShipSet.GetName()
					sPlaDestName = pPlaTravel.DestSet.GetName()
					sSelfSetName = self.InitialShipSet.GetName()
					sSelfDestName = self.DestSet.GetName()
					self.Logger.LogString(" -Is AI in Player in route CHECKING: Player Set = "+sPlaSetName+" // self Set = "+sSelfSetName)
					self.Logger.LogString(" -Is AI in Player in route CHECKING: Player Dest Set = "+sPlaDestName+" // self Dest Set = "+sSelfDestName)
					if sPlaSetName == sSelfSetName and sPlaDestName == sSelfDestName:
						self.IsAIinPlayerRoute = 1
						self.Logger.LogString(" -Is AI in Player Route - Checked")
			self.fInitialClock = time.clock()
			# set the last clock for now, it'll be reset in FinishTravel
			self.fLastClock = self.fInitialClock 
			self.PausedTimeUpdateCheck = 0
			if self.IsPlayer == 1 and self.GetDegradationSoundFileName() != "" and self.GetDegradationSoundFileName() != "None":
				sSoundFile = self.GetDegradationSoundFileName()
				self.DegradationAlert = App.TGSound_Create(sSoundFile, "Traveler_DegradationAlert", 0)
				self.DegradationAlert.SetSFX(1)
				self.DegradationAlert.SetInterface(0)
			else:
				self.DegradationAlert = None
		except:
			self._LogError("UpdateVariables")
	def TravelIntercept(self, pTarget, fStopDistance):
		debug(__name__ + ", TravelIntercept")
		try:
			if self.InterceptStatus != self.NOT_ENGAGING:
				# is already intercepting, so should update the intercept procedures
				#self.Logger.LogString(" -Directing to update, ship is already travel intercepting...")
				# also, if it's a different target, we should update our target.
				if pTarget != None and self.InterceptTarget != None:
					if pTarget.GetObjID() != self.InterceptTarget.GetObjID():
						self.InterceptTarget = pTarget
						self.Logger.LogString("TravelIntercept: updated target to "+pTarget.GetName()+" ("+str(pTarget.GetObjID())+")")
						#self.StopIntercept()
						#return 1
				return self.InterceptUpdate()
			elif self.InterceptTarget != None:
				# this case normally means the ship initiated the intercept procedure, but it still didn't started
				# most likely possibly because the ship is still turning to face her target, so we just return 1
				#self.Logger.LogString("TravelIntercept:  our target isnt none")
				return 1

			if pTarget == None:
				self.Logger.LogString(" -Cancelling TravelIntercept, target ship is none...")
				return 0

			vLoc = pTarget.GetWorldLocation()
			if DistanceOfPoints(self.Ship.GetWorldLocation(), vLoc) < fStopDistance:
				self.Logger.LogString(" -Cancelling, too close to target to warp intercept...")
				return 0

			self.Logger.LogString("Travelling INTERCEPT procedures initiated...")

			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString(" -Ship is dead or dying")
				return 0
			if App.g_kTravelManager.IsShipBeingTowed(self.Ship) == 1:
				self.Logger.LogString(" -Cancelling, ship is being towed")
				return 0

			self.UpdateVariables()

			oCanShipWarp = "no value acquired"
			try:
				pFunc = App.g_kTravelManager.GetTravelTypeAttr("Warp", "CanTravel")
				oRet = pFunc(self)
				if type(oRet) == type(1) or type(oRet) == type(""):
					oCanShipWarp = oRet
				else:
					self.Logger.LogError("Travel Type "+self.__travelType+" CanTravel method returns a "+str(type(oRet))+", not a bool or a string.")
					oCanShipWarp = "erroneous travel type CanTravel return value"
			except:
				self._LogError("TravelIntercept_TryCanWarp")

			if self.Ship.IsDocked() == 1:
				return "Can't travel travel intercept while docked."
			if oCanShipWarp != 1:
				self.Logger.LogString(" -Cancelling, ship can't warp. ("+str(oCanShipWarp)+")")
				return 0
			if self.InitialShipSet == None:
				self.Logger.LogString(" -Cancelling, no initial set...")
				return 0
			if self.IsTravelling() == 1:
				self.Logger.LogString(" -Cancelling, already started...")
				return 0
			if self.IsTurning == 1:
				self.Logger.LogString(" -Cancelling, ship is turning...")
				return 0
			
			uAimValue = self.GetEngageDirection()
			if uAimValue != None:
				self.Logger.LogString(" -cancelling, bad direction...")
				return 0
			self.Logger.LogString(" -Checked: Ship can warp, travel procedures started.")
	
			self.Ship.StopIntercept()
			self.Logger.LogString(" -Stopped Intercept speed, incase the ship was intercepting.")

			#self.SetSpeed(9.99) # mainly, to affect the streaks for the player.

			#use the following to get accurate speed: Galaxy.GetTimeToWarp(1, fInSystemWarpFactor, 1)['Speed']
			#however, that might be too much lol
			fSpeed = 500.0
			vVelocity = GetVectorFromToByPoints(vLoc, self.Ship.GetWorldLocation(), unitize = 1)

			if self.IsPlayer == 1:
				self.Logger.LogString(" -Doing Player only stuff")
				if self.StreaksNode == None:
					self.StreaksNode = LibStarstreaks.WarpSetv2_Create(self.Ship, self.GetSpeed())
				#	self.Logger.LogString(" -created star streaks")
					LibStarstreaks.OverrideForwardProject(300.0)

			fTimeToStart = self.Ship.TurnTowardLocation(vLoc)

			pSeq = App.TGSequence_Create()
			sRace = GetShipRace(self.Ship)
			sActionsPath = "Custom.GalaxyCharts.WarpSequence_Override"
			pWarpSoundAction1 = App.TGScriptAction_Create(sActionsPath, "PlayWarpSound", self.TravelerSequence, "Enter Warp", sRace)
			pSeq.AddAction(pWarpSoundAction1, None, fTimeToStart)
	
			pBoostAction = App.TGScriptAction_Create(sActionsPath, "BoostShipSpeed", self.Ship.GetObjID(), 1, fSpeed, vVelocity)
			pSeq.AddAction(pBoostAction, pWarpSoundAction1, 1.0)

			pFlash = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", self.Ship.GetObjID())
			pSeq.AddAction(pFlash, pBoostAction, 1.0)

			try:
				import Custom.NanoFXv2.WarpFX.WarpFX
				pNacelleFlash = Custom.NanoFXv2.WarpFX.WarpFX.CreateNacelleFlashSeq(self.Ship, self.Ship.GetRadius())
				pSeq.AddAction(pNacelleFlash, pWarpSoundAction1)
			except:
				pass

			pFinish = App.TGScriptAction_Create(__name__, "FinishTravelInterceptAction", self)
			pSeq.AddAction(pFinish, pBoostAction, 0.5)

			pSeq.Play()
			self.Logger.LogString(" -Target is "+pTarget.GetName()+" ("+str(pTarget.GetObjID())+")")
			self.Logger.LogString("Playing travel intercept sequence...")

			self.InterceptTarget = pTarget
			self.InterceptStopDist = fStopDistance
			self.InterceptStatus = self.ENGAGING
			return 1
		except:
			self._LogError("TravelIntercept")
	def FinishTravelIntercept(self):
		debug(__name__ + ", FinishTravelIntercept")
		try:
			self.Logger.LogString("Travel INTERCEPT sequence ended...")
			if self.InterceptStatus != self.ENGAGING:
				# this is being called when it shouldn't...
				self.Logger.LogString(" -cancelling, being called when it shouldnt")
				vVelocity = App.TGPoint3()
				vVelocity.SetXYZ(0,0,0)
				self.Ship.SetVelocity(vVelocity)
				return 0
			if self.InterceptTarget == None:
				self.InterceptStatus = self.ENGAGED  # we need to set this here so that Stop Intercept works.
				self.Logger.LogString(" -cancelling, target is none")
				self.StopIntercept()
				return 0
			if self.IsPlayer == 1:
				self.Logger.LogString(" -Doing Player only stuff")
				ShowTextBanner("Engaging In-System Warp", 0.5, 0.4, 3.0, 16, 1, 0)
			#	self.Logger.LogString(" -played engaging banner")
			self.Logger.LogString("Travelling Intercept procedures finished...")
			self.AlreadyStoppedIntercept = 0
			self.InterceptStatus = self.ENGAGED
			#self.InterceptUpdate()
			return 1
		except:
			self._LogError("FinishTravelIntercept")
	def InterceptUpdate(self):
		debug(__name__ + ", InterceptUpdate")
		try:
			#self.Logger.LogString("InterceptUpdate:  Status = "+str(self.InterceptStatus))
			if self.InterceptStatus == self.ENGAGED:
				if self.Ship.IsDying() or self.Ship.IsDead():
					self.Logger.LogString("Ship is dead or dying (at InterceptUpdate)")
					return 0
				if self.InterceptTarget == None:
					self.Logger.LogString("Cancelling Intercept update, our target is none...")
					self.StopIntercept()
					return 1
				if self.IsTravelling() == 1:
					self.Logger.LogString("Cancelling Intercept update, our ship is warping...")
					self.StopIntercept()
					return 1
				vLoc = self.InterceptTarget.GetWorldLocation()
				if DistanceOfPoints(self.Ship.GetWorldLocation(), vLoc) < self.InterceptStopDist:
					self.Logger.LogString("Cancelling Intercept update, we are within distance...")
					self.StopIntercept()
					return 1
				self.Ship.TurnTowardLocation(vLoc)
				sActionsPath = "Custom.GalaxyCharts.WarpSequence_Override"
				fSpeed = 500.0
				vVelocity = GetVectorFromToByPoints(vLoc, self.Ship.GetWorldLocation(), unitize = 1)
				pSeq = App.TGSequence_Create()  # sequence to play a few update actions
				pBoostAction = App.TGScriptAction_Create(sActionsPath, "BoostShipSpeed", self.Ship.GetObjID(), 2, fSpeed, vVelocity)
				pSeq.AddAction(pBoostAction, None)
				pUpdateAction = App.TGScriptAction_Create(__name__, "InterceptUpdateAction", self)
				pSeq.AddAction(pUpdateAction, pBoostAction, 0.3)
				pSeq.Play()
			#	self.Logger.LogString("Intercept Update finished...")
				return 1
			elif self.InterceptStatus == self.ENGAGING or self.InterceptStatus == self.EXITING:
			#	self.Logger.LogString("Intercept Update is going on 1")
				return 1
			return 0
		except:
			self._LogError("InterceptUpdate")
	def StopIntercept(self):
		debug(__name__ + ", StopIntercept")
		try:
			#self.Logger.LogString("StopIntercept:  Status = "+str(self.InterceptStatus))
			if self.InterceptStatus == self.ENGAGED or self.InterceptStatus == self.ENGAGING:
				self.Logger.LogString("Stopping warp intercept")
				sActionsPath = "Custom.GalaxyCharts.WarpSequence_Override"
				pSeq = App.TGSequence_Create()
				pFlash = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", self.Ship.GetObjID())
				pSeq.AddAction(pFlash, None)

				pUnBoostAction = App.TGScriptAction_Create(sActionsPath, "BoostShipSpeed", self.Ship.GetObjID(), 0, 1.0)
				pSeq.AddAction(pUnBoostAction, pFlash)

				sRace = GetShipRace(self.Ship)
				pWarpSoundAction1 = App.TGScriptAction_Create(sActionsPath, "PlayWarpSound", self.TravelerSequence, "Exit Warp", sRace)
				pSeq.AddAction(pWarpSoundAction1, pUnBoostAction)

				pEndAction = App.TGScriptAction_Create(__name__, "FinishStopInterceptAction", self)
				pSeq.AddAction(pEndAction, pWarpSoundAction1, 2.0)

				if self.IsPlayer == 1:
					ShowTextBanner("Disengaging In-System Warp...", 0.5, 0.45, 3.0, 16, 1, 0)
			#		self.Logger.LogString(" -played disengaging banner")
				if self.StreaksNode != None:
					LibStarstreaks.OverrideForwardProject(-300.0)
					LibStarstreaks.WarpSetv2_KillByNode(self.StreaksNode)
			#		self.Logger.LogString(" -deleted star streaks")
					self.StreaksNode = None
				#self.SetSpeed(self.GetActualCruiseWarpSpeed())
				self.AlreadyStoppedIntercept = 1
				self.InterceptTarget = None
			#	self.Logger.LogString(" -our target has been reset")
				# finally update the status and play the sequence.
				self.InterceptStatus = self.EXITING
				pSeq.Play()
				self.Logger.LogString("Stopped Warp Intercept...")

				return 1
			elif self.InterceptStatus == self.EXITING:
				return 1
			return 0
		except:
			self._LogError("StopIntercept")
	def FinishStopIntercept(self):
		debug(__name__ + ", FinishStopIntercept")
		try:
		#	self.Logger.LogString("FinishStopIntercept:  Status = "+str(self.InterceptStatus))
			if self.InterceptStatus == self.EXITING:
				# just to be sure the ship is stopped, without caring for original speed.
				sActionsPath = "Custom.GalaxyCharts.WarpSequence_Override"
				pAllStopAction = App.TGScriptAction_Create(sActionsPath, "BoostShipSpeed", self.Ship.GetObjID(), -1, 1.0)
				pAllStopAction.Play()
				# finally update the status
				self.InterceptStatus = self.NOT_ENGAGING
				self.Logger.LogString("Finished  FinishStopIntercept")
		except:
			self._LogError("FinishStopIntercept")
	def _StopInterceptDirect(self):
		# this function will stop normal intercept speed and directly stop the in-system warp, so no exiting sound, etc
		# It meant to be used internally by the Travel class, to make a ship stop before warping.
		debug(__name__ + ", _StopInterceptDirect")
		try:
			#self.Logger.LogString("StopInterceptDirect:  Status = "+str(self.InterceptStatus))
			self.Ship.StopIntercept()
			if self.InterceptStatus == self.ENGAGED or self.InterceptStatus == self.ENGAGING:
				self.Logger.LogString("Stopping warp intercept, by Direct")

				sActionsPath = "Custom.GalaxyCharts.WarpSequence_Override"
				pUnBoostAction = App.TGScriptAction_Create(sActionsPath, "BoostShipSpeed", self.Ship.GetObjID(), -1, 1.0)
				pUnBoostAction.Play()

				if self.StreaksNode != None:
					LibStarstreaks.OverrideForwardProject(-300.0)
					LibStarstreaks.WarpSetv2_KillByNode(self.StreaksNode)
					self.StreaksNode = None
				#self.SetSpeed(self.GetActualCruiseWarpSpeed())
				self.AlreadyStoppedIntercept = 1
				self.InterceptTarget = None

				# finally update the status and play the sequence.
				self.InterceptStatus = self.NOT_ENGAGING

				if self.IsPlayer == 1:
					self.Ship.ClearAI()
				self.Logger.LogString("Stopped Warp Intercept Directly...")
		except:
			self._LogError("StopInterceptDirect")
	def IsIntercepting(self):
		debug(__name__ + ", IsIntercepting")
		return self.InterceptStatus
	def _TurnTimerTravel(self, pMethodTimerEvent = None):
		# called by the timers that wait for a ship to turn to a good direction
		# this is a little function just to check/update the self.IsTurning attribute, before calling Travel() again
		debug(__name__ + ", _TurnTimerTravel")
		try:
			if self.IsTurning == 1:
				self.IsTurning = 0
				self.Travel()
		except:
			self._LogError("TurnTimerTravel")
	def GetTravelType(self):
		debug(__name__ + ", GetTravelType")
		return self.__travelType
	def SetTravelType(self, sTravelType):
		debug(__name__ + ", SetTravelType")
		if self.IsTravelling() == 1:
			self.Logger.LogString("Tried to set Travel Type ("+sTravelType+") while ship was travelling.")
			return
		if sTravelType != "" and type(sTravelType) == type(""):
			if App.g_kTravelManager.HasTravelType(sTravelType) == 1:
				self.__travelType = sTravelType
				self.Logger.LogString(" -Travel Type Set: "+sTravelType)
			else:
				self.Logger.LogString(" -Tried to set to a non-existant travel type: "+sTravelType)
	def Travel(self, sTravelType = ""):
		debug(__name__ + ", Travel")
		try:
			self.Logger.LogString("Travelling procedures initiated...")
			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString(" -Ship is dead or dying")
				return "Ship is dead or dying."
			#####
			self.SetTravelType(sTravelType)
			if self.__travelType == "" or self.__travelType == "None":
				self.Logger.LogString(" -Cancelling, travel type is None")
				return "Cancelling, travel type is None."
			if App.g_kTravelManager.IsTravelTypeShipBased(self.GetTravelType()) == 1:
				if App.g_kTravelManager.IsShipEquippedWithTravelType(self.Ship, self.GetTravelType()) == 0:
					self.Logger.LogString(" -Cancelling, ship is not equipped with travelling type "+self.GetTravelType())
					return "Cancelling, ship is not equipped with travelling type "+self.GetTravelType()
			else:
				vPos = App.g_kTravelManager.IsShipInLaunchPosFor(self.Ship, self.GetTravelType())
				if vPos == None:
					self.Logger.LogString(" -Cancelling, ship is not in launch coord for travelling type "+self.GetTravelType())
					return "Cancelling, ship is not in launch coord for travelling type "+self.GetTravelType()
				self.__launchPos = [vPos.x, vPos.y, vPos.z]
				self.Logger.LogString(" -Launch Coordinates: X="+str(vPos.x)+"   Y="+str(vPos.y)+"   Z="+str(vPos.z))
			#####
			if self.IsTurning == 1:
				self.Logger.LogString(" -Ship is turning to face a good direction")
				return "Ship is turning to face a good direction"
			if App.g_kTravelManager.IsShipBeingTowed(self.Ship) == 1:
				self.Logger.LogString(" -Cancelling, ship is being towed")
				return "Cancelling, ship is being towed"

			self.UpdateVariables()

			if self.InitialShipSet == None:
				self.Logger.LogString(" -Cancelling, no initial set.")
				return " Cancelling, no initial set."
			if self.Started == 0 and self.IsPlayer == 0 and self.DestSet == None:
				self.Logger.LogString(" -Extra path: AI ship warping to None")
				bGoingToNONE = 1
			else:
				bGoingToNONE = 0
				if self.Started == 1 or self.DestSet == None or self.DestinationScript == "":
					self.Logger.LogString(" -Cancelling, already started or no destination.")
					return "Cancelling, already started or no destination."
				self.Logger.LogString(" -Attribute: Initial Set = "+self.InitialShipSet.GetName())
				self.Logger.LogString(" -Attribute: Destination Set = "+self.DestSet.GetName())
				if self.InitialShipSet.GetRegion() == None or self.DestSet.GetRegion() == None:
					self.Logger.LogString(" -Cancelling, initial set or destination set doesn't have the Region set.")
					return "Cancelling, initial set or destination set doesn't have the Region set."
				if self.InitialShipSet.GetRegionModule() == self.DestinationScript:
					self.Logger.LogString(" -Cancelling, initial and destination sets are the same.")
					return "Cancelling, initial and destination sets are the same."
				else:
					if self.InitialShipSet.GetRegion().GetLocation() == "DEFAULT" or self.DestSet.GetRegion().GetLocation() == "DEFAULT":
						self.Logger.LogString(" -Cancelling, initial or destination regions have the location set as DEFAUT")
						return "Cancelling, initial or destination regions have the location set as DEFAUT."

			oCanShipTravel = self.CanTravel()
			if oCanShipTravel != 1:
				self.Logger.LogString(" -Cancelling, ship can't warp. ("+str(oCanShipTravel)+")")
				return "Cancelling, ship can't warp. Reason: "+str(oCanShipTravel)

			pTopWin = App.TopWindow_GetTopWindow()
			if self.TravelBlindly == 0:
				uAimValue = self.GetEngageDirection()
			else:
				uAimValue = None
				self.Logger.LogString(" -Travelling blindly...")		

			# call this to directly stop intercepting
			self._StopInterceptDirect()

			if type(uAimValue) == type([]) and len(uAimValue) >= 2:
				fTime = self.Ship.TurnTowardOrientation(uAimValue[0], uAimValue[1])
				if pTopWin != None:
					pTopWin.ForceTacticalVisible()
				self.Logger.LogString(" -Going to wait "+str(fTime)+" secs to try again, while ship is turning to a good orientation")
				self.IsTurning = 1
				CreateMethodTimer(self.pEventHandler, "_TurnTimerTravel", App.g_kUtopiaModule.GetGameTime() + fTime)
				return "Going to wait "+str(fTime)+" secs to try again, while ship is turning to a good orientation."
			elif uAimValue != None:
				fTime = self.Ship.TurnTowardDirection(uAimValue)
				if pTopWin != None:
					pTopWin.ForceTacticalVisible()
				self.Logger.LogString(" -Going to wait "+str(fTime)+" secs to try again, while ship is turning to a good direction")
				self.IsTurning = 1
				CreateMethodTimer(self.pEventHandler, "_TurnTimerTravel", App.g_kUtopiaModule.GetGameTime() + fTime)
				return "Going to wait "+str(fTime)+" secs to try again, while ship is turning to a good direction."

			self.Logger.LogString(" -Checked: Ship can warp, travel procedures started.")
			self.Logger.LogString(" -Speed Check:")
			self.Logger.LogString("     -Current:  "+str(self.GetSpeed()))
			self.Logger.LogString("     -Real Speed:  "+str(self.GetRealSpeed()))
			self.Logger.LogString("     -Cruise:  "+str(self.GetCruiseSpeed()))
			self.Logger.LogString("     -Max:  "+str(self.GetMaxSpeed()))
			self.Logger.LogString("     -Actual Cruise:  "+str(self.GetActualCruiseSpeed()))
			self.Logger.LogString("     -Actual Max:  "+str(self.GetActualMaxSpeed()))
			self.StopIntercept()
			self.Ship.StopIntercept()
			if bGoingToNONE == 0:
				self.SetupTowing()
			iRF = self.GetRestrictionFlag()
			if bGoingToNONE == 0:
				pRegion = self.InitialShipSet.GetRegion()
				pDestRegion = self.DestSet.GetRegion()
				ISA = [pRegion.GetOnlyByRestrictedMethods(), int(self.__travelType in pRegion.GetRestrictedFor())]
				DSA = [pDestRegion.GetOnlyByRestrictedMethods(), int(self.__travelType in pDestRegion.GetRestrictedFor())]
				if ISA == [0,0] and DSA[1] == 1 and iRF == 2:
					#mark the system we're exiting for restriction purposes.
					self.dSysRestrictionF2[self.__travelType] = pRegion.GetName()
			self.DoPreEngageStuff()
			self.TravelerSequence.SetupSequence()
			####################
			# first send travel type specific start travel events
			for pEvent in self.GetStartTravelEvents():
				App.g_kEventManager.AddEvent(pEvent)
			# then send our customly set start travel events
			for pStartWarpEvent in self.StartWarpEvents:
				App.g_kEventManager.AddEvent(pStartWarpEvent)
			##########
			if bGoingToNONE == 0:
				self.Logger.LogString(" -GFX Sequence Set up DONE")
				self.SetEnginesState(App.WarpEngineSubsystem.WES_WARP_INITIATED)
				self.TravelValues = Galaxy.CalculateTimeToTravel(self.InitialShipSet, self.DestSet, self.GetRealSpeed(), 1)
				self.TimeToReach = self.TravelValues['Time']
				self.TimeLeft = self.TimeToReach
				self.LTVUPOS = self.InitialShipSet.GetRegion().GetLocation()
				self.Logger.LogString(" -Travel Values calculated:")
				self.Logger.LogString("   -Time To Reach: "+str(self.TimeToReach)+" seconds")
				if self.IsPlayer == 1:
					self.Logger.LogString(" -Doing Player only stuff:")
					# Clear the player's target when they go into warp if they aren't tractoring.
					if self.bTractorStat != 1:
						import TacticalInterfaceHandlers
						TacticalInterfaceHandlers.ClearTarget(None, None)
					BridgeHandlers.DropMenusTurnBack()
					if pTopWin != None:
						pTopWin.ForceTacticalVisible()
						self.Logger.LogString("   -Tactical view forced visible")
					ShowTextBanner(self.GetTravellingToString()+" "+self.DestSet.GetName(), 0.5, 0.4, 3.0, 16, 1, 0)
					sEmpire = self.DestSet.GetRegion().GetControllingEmpire()      
					if sEmpire != "Unknown" and sEmpire != "None":
						if IsShipEnemyOfRace(self.Ship, sEmpire) == 1:
							ShowTextBanner("Warning: Going to Hostile Space", 0.5, 0.45, 3.0, 15, 1, 0)
					pHelm = App.CharacterClass_GetObject(App.g_kSetManager.GetSet("bridge"), "Helm")
					if pHelm != None:
						pHelm.SetActive(1)
						App.CharacterAction_Create(pHelm, App.CharacterAction.AT_SAY_LINE, pHelm.GetCharacterName() + "Yes" + str(App.g_kSystemWrapper.GetRandomNumber(4)+1), None, 1).Play()
						self.Logger.LogString("   -Played Helm Yes Line")
			self.SetEnginesState(App.WarpEngineSubsystem.WES_WARP_BEGINNING)
			######## GFX EFFECT - ENTERING WARP - HERE ##################################
			self.TravelerSequence.PlayEngagingWarpSeq()    ###########
			########################################################
			#
			if WarSimulator.IsInitialized() == 1:
				if self.DestSet != None:
					WarSimulator.AddNewsItem("Travel", self.Ship.GetName()+" is travelling to "+str(self.DestSet.GetName()))
					if self.IsPlayer == 1:
						WarSimulator.dStats["TimesTraveled"] = WarSimulator.dStats["TimesTraveled"] + 1
				else:
					WarSimulator.AddNewsItem("Travel", self.Ship.GetName()+" is travelling somewhere...")
			self.Logger.LogString(" -Started playing engaging sequence.")
			self.SeqStat = self.ENGAGING
			return 1
		except:
			self._LogError("Travel")
			return "ERROR! Something bad has happened..."
	def IsTravelling(self):
		debug(__name__ + ", IsTravelling")
		if self.Started == 1 or self.SeqStat == self.ENGAGING:
			return 1
		else:
			return 0
	def FinishTravel(self):
		debug(__name__ + ", FinishTravel")
		try:
			if self.Started == 0 and self.SeqStat == self.ENGAGING:
				self.Logger.LogString(" -Finishing travelling procedures...")
				if self.IsPlayer == 0 and self.DestSet == None:
					self.InitialShipSet.RemoveObjectFromSet(self.Ship.GetName())
					self.SeqStat = self.NOT_ENGAGING
					self.Logger.LogString(" -Finished. AI Ship travelling to None.")
					#App.g_kTravelManager.DeleteTravel(self.Ship)
					return 1
				if self.Refresher == None:
					self.Refresher = RefreshEventHandler(self.Update, 0.1)
				else:
					self.Refresher.StartRefreshHandler('NORMAL')
				self.Logger.LogString(" -Started Refresher Loop")
				pSetToUse = self.GetTravelSetToUse()
				self.Logger.LogString(" -Travel Set being used: "+pSetToUse.GetName())
				# the following line disables the "Arriving at..." text banner =)
				# very easy. thanks Sovvie by the inspiration xD
				if self.IsPlayer == 1:
					Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0
				ChangeShipSet(self, pSetToUse)
				if self.bTractorStat == 1 and self.Towee != None:
					ChangeToweeSet(self, pSetToUse)
				self.Logger.LogString(" -Just changed ship set.")
				if self.IsPlayer == 1:
					self.Logger.LogString(" -Doing more player only stuff:")
					vRegPos = self.InitialShipSet.GetRegion().GetLocation()
					Travel.pTravelSet.GetRegion().SetLocation(vRegPos.x, vRegPos.y)
					if self.bTractorStat != 1:
						self.Ship.SetTarget(None)
						self.Logger.LogString("   -Cleared target")
						pTargetMenu = App.STTargetMenu_GetTargetMenu()
						if pTargetMenu != None:
							pTargetMenu.ClearPersistentTarget()
							self.Logger.LogString("   -Cleared Target Menu persistent target")
				self.Started = 1
				self.SeqStat = self.ENGAGED
				self.ImpulseStatus.SetAsWarping()
				if self.IsPlayer == 1:
					if self.CanDropOut() == 1:
						HelmAddonGUI.pDropOutButton.SetEnabled()
						if WarSimulator.IsInitialized() == 1 and WarSimulator.dStats["SystemsConquered"] >= 10 and WarSimulator.dStats["NebulasDestroyed"] >= 10:
							if self.GetTravelType() == "Warp" and Travel.pNebSet == None:
								if App.g_kSystemWrapper.GetRandomNumber(100) <= 50 and self.TimeToReach >= 10.0:
									ShowTextBanner("We're getting some strange Nebula readings ahead, captain.", 0.5, 0.45, 4.0, 15, 1, 1)
									self.bStrangeNebula = 1
					HelmAddonGUI.pMenu.SetDisabled()
					GalaxyMapGUI.UpdateSelectSpeedButtons(self.CanChangeSpeed())
					if self.StreaksNode == None and self.UseStarstreaks() == 1:
						self.StreaksNode = LibStarstreaks.WarpSetv2_Create(self.Ship, self.GetSpeed())
					# now disable some menus, to avoid possible bugs while warping, only if it is the player
					pSetCmenu = GetSTMenu("Set Course", "Helm")
					if pSetCmenu != None:
						if pSetCmenu.IsEnabled() == 1:
							pSetCmenu.SetDisabled()
							self.CheckedSetCourse = 1
					pMVAMmenu = GetSTMenu("MVAM Menu")
					if pMVAMmenu != None:
						if pMVAMmenu.IsEnabled() == 1:
							pMVAMmenu.SetDisabled()
							self.CheckedMVAM = 1
					pCoreMenu = GetSTMenu("Core Ejection")
					if pCoreMenu != None:
						if pCoreMenu.IsEnabled() == 1:
							pCoreMenu.SetDisabled()
							self.CheckedCoreEject = 1
					pAbandonMenu = GetSTMenu("Abandon Ship")
					if pAbandonMenu != None:
						if pAbandonMenu.IsEnabled() == 1:
							pAbandonMenu.SetDisabled()
							self.CheckedAbandonShipMenu = 1
					pAddShipsButt = GetSTButton("Add ships")
					if pAddShipsButt != None:
						if pAddShipsButt.IsEnabled() == 1:
							pAddShipsButt.SetDisabled()
							self.CheckedAddShips = 1
					pTransButt = GetSTButton("Transporter", "Engineer")
					if pTransButt != None:
						if pTransButt.IsEnabled() == 1:
							pTransButt.SetDisabled()
							self.CheckedTransporter = 1
					lLaunchButtons = GetLaunchShuttleButtons()
					if lLaunchButtons != []:
						for pLaunchButton in lLaunchButtons:
							if pLaunchButton.IsEnabled() == 1:
								pLaunchButton.SetDisabled()
								self.CheckedLaunchShuttles = 1
						if self.CheckedLaunchShuttles == 1:
							pMission = MissionLib.GetMission()
							try:
								import ftb.LaunchShipHandlers
								pMission.AddPythonFuncHandlerForInstance(ftb.LaunchShipHandlers.ET_TOGGLE_LAUNCH_TYPE, __name__+".DisableLaunchShuttleButtons")
							except:
								self._LogError("FinishTravel - couldn't add ET_TOGGLE_LAUNCH_TYPE handler")
				try:
					pAbandonShipScript = __import__('Custom.QBautostart.Abandon Ship')
					if not self.Ship.GetObjID() in pAbandonShipScript.lAbandonDone:
						pAbandonShipScript.lAbandonDone.append(self.Ship.GetObjID())
						self.CheckedAbandonShip = 1
				except:
					self.Logger.LogString(" -Couldn't disable Abandon Ship for this ship - most likely user do not have Abandon Ships")
				self.fInitialClock = time.clock()
				self.fLastClock = self.fInitialClock
				self.Logger.LogString(" -Travelling procedures ended, ship is already travelling.")
				return 1
			else:
				return 0
		except:
			self._LogError("FinishTravel")
	def TravelTo(self, sDestination, sTravelType = ""):
		debug(__name__ + ", TravelTo")
		if self.Started == 1:
			return 0
		self.SetDestination(sDestination)
		iResult = self.Travel(sTravelType)
		return iResult
	def Update(self, pObject, pEvent):
		debug(__name__ + ", Update")
		try:
			bCanUpdate = 1
			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString("Ship is dead or dying (at Update)")
				bCanUpdate = 0
			if self.Started == 1 and bCanUpdate == 1:
				self.Logger.LogString("Updating Travelling Procedures...")
				bCanTravelStatus = self.CanContinueTravelling()
				if bCanTravelStatus == 0:
					self.Logger.LogString(" -Ship can't travel anymore, dropping out.")
					self.DropOutOfTravel()
				else:
					self.Logger.LogString(" -Update Loop MARK START")
					if self.IsPlayer == 1:
						self.Ship.GetContainingSet().GetRegion().Location = self.GetShipLocationInGalaxy()
						#####################################
						# update the Galaxy Map GUI, the player may be using it, so we need to update it in
						# real time
						GalaxyMapGUI.UpdateGUI()
						SystemAnalysisGUI.UpdateSystemAnalysis()
						#####################################
					self.ImpulseStatus.MaintainWarping()
					bDegradeAlertCheck = self.DegradationCheck()
					if bDegradeAlertCheck == 1 and self.DegradationAlert != None:
						self.DegradationAlert.Play()
					self.SetEnginesState(App.WarpEngineSubsystem.WES_WARPING)
					fCurrentClock = time.clock()
					fTimePassed =  fCurrentClock - self.fLastClock  ##self.Refresher.Delay  
					if self.PausedTimeUpdateCheck != 0:
						fTimePassed = fTimePassed - self.PausedTimeUpdateCheck
						self.PausedTimeUpdateCheck = 0
					self.fLastClock = fCurrentClock
					self.TimeLeft = self.TimeLeft - fTimePassed
					self.Logger.LogString(" -Time left: "+str(self.TimeLeft)+" seconds")
					if self.bTractorStat == 1:
						pSeq = App.TGSequence_Create()
						fCount = 0.0
						while fCount < fTimePassed:
							pMaintainTowingAction = App.TGScriptAction_Create(__name__, "MaintainTowingAction", self)
							pSeq.AddAction(pMaintainTowingAction, None, fCount)
							fCount = fCount + 0.01
							if fCount >= fTimePassed:
								break
						pSeq.Play()
					######## GFX EFFECT - ENTERING WARP - HERE ##################################
					self.TravelerSequence.PlayDuringWarpSeq()    ###########
					########################################################
					if self.IsPlayer == 1:
						ShowTextBanner("Destination: "+self.DestSet.GetName(), 0.35, 0.0, 0.1, 14, 0, 0)
						ShowTextBanner(self.__travelType+" Speed: "+str(self.GetSpeed()), 0.35, 0.05, 0.1, 14, 1, 0)
						ShowTextBanner("ETA: "+GetStrFromFloat(self.TimeLeft, 1)+" seconds", 0.35, 0.1, fTimePassed/3.0, 14, 0, 0)
					if self.TimeLeft <= self.TimeToReach/5:
						self.SetEnginesState(App.WarpEngineSubsystem.WES_WARP_ENDING)
					else:
						self.SetEnginesState(App.WarpEngineSubsystem.WES_WARPING)
					if self.TimeLeft <= 0:
						# arrived at destination
						self.Logger.LogString(" -Update Loop MARK COMPLETED, arrived at destination.")
						self.DropOutOfTravel()
					else:
						self.Logger.LogString(" -Update Loop MARK COMPLETED")
		except:
			self._LogError("Update (Travel)")
	def __setupNebulaSystem(self):
		debug(__name__ + ", __setupNebulaSystem")
		import TravelerSystems.SpaceSet
		if Travel.pNebSet != None:
			return
		TravelerSystems.SpaceSet.SET_NAME = "Nebula System"
		Travel.pNebSet = TravelerSystems.SpaceSet.Initialize()
		###
		if WarSimulator.dShips.has_key("Nebula"):
			# ops, problem here. Ship already exists...
			# for now, do nothing else...
			return
		WarSimulator.dShips["Nebula"] = WSShip("Nebula", "Nebula System", 0)
		pNebDef = GetShipDefByScript( "Nebula" )
		pNebula = CreateShip(pNebDef, Travel.pNebSet, "Nebula", "None")
		pNebula.SetInvincible(1)
		pNebula.SetHurtable(0)
		pNebula.SetTargetable(1)
		pNebula.SetScale(2.5)
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			pSensors = pPlayer.GetSensorSubsystem()
			if pSensors:
				pSensors.ForceObjectIdentified(pNebula)
		###
		self.Logger.LogString(" -Initialized Nebula Set")
		TravelerSystems.SpaceSet.SET_NAME = "SpaceSet"
	def DropOutOfTravel(self):
		debug(__name__ + ", DropOutOfTravel")
		try:
			if self.Ship.IsDying() or self.Ship.IsDead():
				return
			if self.Started == 1:
				bIsDroppingOut = 0
				if self.TimeLeft <= 0:
					bIsDroppingOut = 0
				else:
					bIsDroppingOut = 1
					if self.CanDropOut() == 0 and self.CanContinueTravelling() == 1:
						self.Logger.LogString("Tried to drop out of travel. Cancelled by Travel Type - cant drop out")
						return
					if self.IsPlayer == 0:
						vPos = self.GetShipLocationInGalaxy()
						pAISpaceSet = TravelerSystems.AISpaceSet.GetSetForPos(vPos)
						if pAISpaceSet == None:
							# for some strangely bizarre reason, the function didn't returned a set...
							# so cancel this for now. chances are it'll try again next update.
							return
						pAISpaceSet.GetRegion().SetLocation(vPos.x, vPos.y)
				self.Logger.LogString("Drop Out Of Travel Procedures Started:")
				self.SeqStat = self.EXITING
				self.Logger.LogString(" -Is Dropping out: "+str(bIsDroppingOut))
				self.SetEnginesState(App.WarpEngineSubsystem.WES_DEWARP_INITIATED)
				if self.IsPlayer == 1:
					if bIsDroppingOut == 1 and self.bStrangeNebula == 1 and Travel.pNebSet == None:
						self.__setupNebulaSystem()
						Travel.pNebSet.GetRegion().Location = self.GetShipLocationInGalaxy()
					elif bIsDroppingOut == 1:
						Travel.pSpaceSet.GetRegion().Location = self.GetShipLocationInGalaxy()
					self.Ship.GetContainingSet().GetRegion().Location = None
				self.Logger.LogString(" -Traveler Systems Location Set")
				self.TravelValues = {}
				self.TimeToReach = 0
				self.TimeLeft = 0
				self.LTVUPOS = None
				self.Logger.LogString(" -Travel Values are zero")
				if self.CLASS == "Ship Travel":
					# With this IF, Chaser instances won't stop their refresh handler, which is really important
					# to make them work properly
					self.Refresher.StopRefreshHandler()
				self.Logger.LogString(" -Stopped Refresher...")
				self.SetEnginesState(App.WarpEngineSubsystem.WES_DEWARP_BEGINNING)
				self.ImpulseStatus.SetAsNormal()
				if self.StreaksNode != None:
					LibStarstreaks.WarpSetv2_KillByNode(self.StreaksNode)
					self.StreaksNode = None
				self.Logger.LogString(" -Impulse Engines status reset")
				if bIsDroppingOut == 1:
					if self.IsPlayer == 1:
						if self.bStrangeNebula == 1:
							pSetToDrop = Travel.pNebSet
							self.bStrangeNebula = 0
						else:
							pSetToDrop = Travel.pSpaceSet
					else:
						pSetToDrop = pAISpaceSet
				else:
					pSetToDrop = self.DestSet
				self.ShipGoingToExit(pSetToDrop)
				self.DoPreExitStuff()
				if (GetConfigValue("ShowBanners") == 0 or bIsDroppingOut == 1) and self.IsPlayer == 1:
					Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0
				ChangeShipSet(self, pSetToDrop)
				self.Logger.LogString(" -Changed ship set to destination: "+str(pSetToDrop.GetName()))
				if self.bTractorStat == 1 and self.Towee != None:
					ChangeToweeSet(self, pSetToDrop)
				############
				# send out travel type specific exited travel events
				for pEvent in self.GetExitedTravelEvents():
					App.g_kEventManager.AddEvent(pEvent)
				# then send our customly/manually set exited travel events
				for pArrivedEvent in self.ArrivedEvents:
					App.g_kEventManager.AddEvent(pArrivedEvent)
				# and finally the RDF_TRIGGER event, which will trigger the RDF check.
				#print "CanTriggerRDF:", App.g_kTravelManager.CanTravelTypeTriggerRDF(self.__travelType)
				#print "IgnoreRDF:", pSetToDrop.GetRegion().GetIgnoreRDF()
				if App.g_kTravelManager.CanTravelTypeTriggerRDF(self.__travelType) == 1 and pSetToDrop.GetRegion().GetIgnoreRDF() == 0:
					pRDFEvent = App.TGStringEvent_Create()
					pRDFEvent.SetEventType(ET_RDF_TRIGGER)
					pRDFEvent.SetDestination(self.Ship)
					pRDFEvent.SetString(self.__travelType)
					App.g_kEventManager.AddEvent(pRDFEvent)
				###########
				self.Logger.LogString(" -Sent Arrived Events")
				self.SetEnginesState(App.WarpEngineSubsystem.WES_DEWARP_ENDING)
				if self.IsPlayer == 1:
					self.Logger.LogString(" -Doing player only stuff...")
					HelmAddonGUI.pDropOutButton.SetDisabled()
					HelmAddonGUI.pMenu.SetEnabled()
					GalaxyMapGUI.UpdateSelectSpeedButtons(1)
					BridgeHandlers.DropMenusTurnBack()
					self.Logger.LogString("   -At bridge: dropped menus turn back")
					pTopWin = App.TopWindow_GetTopWindow()
					if pTopWin != None:
						pTopWin.ForceTacticalVisible()
						self.Logger.LogString("   -Tactical view forced visible")
					if bIsDroppingOut == 1:
						ShowTextBanner(self.GetDroppedOutString(), 0.5, 0.3, 2.0, 16, 1, 0)
				##### GFX EFFECT - WARPING OUT - HERE #######################################
				self.TravelerSequence.PlayExitWarpSeq()    #############
				########################################################
				self.Logger.LogString(" -Exiting warp Seq played")
				if WarSimulator.IsInitialized() == 1:
					if bIsDroppingOut == 0:
						WarSimulator.AddNewsItem("Travel", self.Ship.GetName()+" has arrived in "+str(self.DestSet.GetName()))
					else:
						WarSimulator.AddNewsItem("Travel", self.Ship.GetName()+" is dropping out of travel.")
				if bIsDroppingOut == 0:
					fCurClock = time.clock()
					fTravelClock = fCurClock - self.fInitialClock
					self.Logger.LogString(" -Clocked Real Time taken to Travel: "+str(fTravelClock)+" seconds")
				self.SetEnginesState(App.WarpEngineSubsystem.WES_NOT_WARPING)
				## Stopping the towing procedure is done on the exit's sequence last action
				self.Started = 0
				self.__launchPos = None
				self.AIwarpPower = 1.0
				self.SeqStat = self.EXITING
				# restore the "possible bug causers" menus... As they would only be disabled if it was the player
				# there is no need in checking if it is player again
				if self.CheckedSetCourse == 1:
					pSetCmenu = GetSTMenu("Set Course", "Helm")
					if pSetCmenu != None:
						pSetCmenu.SetEnabled()
				if self.CheckedMVAM == 1:
					pMVAMmenu = GetSTMenu("MVAM Menu")
					if pMVAMmenu != None:
							pMVAMmenu.SetEnabled()
				if self.CheckedCoreEject == 1:
					pCoreMenu = GetSTMenu("Core Ejection")
					if pCoreMenu != None:
							pCoreMenu.SetEnabled()
				if self.CheckedAddShips == 1:
					pAddShipsButt = GetSTButton("Add ships")
					if pAddShipsButt != None:
						pAddShipsButt.SetEnabled()
				if self.CheckedTransporter == 1:
					pTransButt = GetSTButton("Transporter", "Engineer")
					if pTransButt != None:
						pTransButt.SetEnabled()
				if self.CheckedLaunchShuttles == 1:
					lLaunchButtons = GetLaunchShuttleButtons()
					if lLaunchButtons != []:
						for pLaunchButton in lLaunchButtons:
							pLaunchButton.SetEnabled()
					pMission = MissionLib.GetMission()
					try:
						import ftb.LaunchShipHandlers
						pMission.RemoveHandlerForInstance(ftb.LaunchShipHandlers.ET_TOGGLE_LAUNCH_TYPE, __name__+".DisableLaunchShuttleButtons")
					except:
						self._LogError("DropOutOfTravel - couldn't remove ET_TOGGLE_LAUNCH_TYPE handler")
				if self.CheckedAbandonShipMenu == 1:
					pAbandonMenu = GetSTMenu("Abandon Ship")
					if pAbandonMenu != None:
						pAbandonMenu.SetEnabled()
				try:
					if self.CheckedAbandonShip == 1:
						pAbandonShipScript = __import__('Custom.QBautostart.Abandon Ship')
						pAbandonShipScript.lAbandonDone.remove(self.Ship.GetObjID())
				except:
					self.Logger.LogString(" -Couldn't re-enable Abandon Ship for this ship - most likely user do not have Abandon Ships")
				self.Logger.LogString("Finished procedures to Drop Out Of Travel.")
		except:
			self._LogError("DropOutOfTravel")
	def SetDestination(self, sDestination):
		debug(__name__ + ", SetDestination")
		try:
			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString("Ship is dead or dying (at SetDestination)")
				return
			if self.DestSet != None:
				if self.DestSet.GetRegionModule() == sDestination:
					self.Logger.LogString("Tried to set the same destination...")
					return
			if sDestination != None and sDestination != "":
				if self.Started == 1 and self.CanChangeCourse() == 0:
					self.Logger.LogString("Tried to change destination. Cancelled by Travel Type.")
					return
				self.Logger.LogString("Setting Destination...")
				self.DestinationScript = sDestination
				self.Logger.LogString(" -Destination: "+sDestination)
				if sDestination == "Custom.GalaxyCharts.TravelerSystems.Nebula System" and Travel.pNebSet != None:
					self.DestSet = Travel.pNebSet
				else:
					pDestModule = __import__(sDestination)
					if pDestModule.GetSet() == None:
						pDestModule.Initialize()
						self.Logger.LogString(" -Initialized destination set")
					self.DestSet = pDestModule.GetSet()
				if self.Started == 1:
					# update time to reach/time left based on new warp values calculation.
					self.Logger.LogString(" -Updating travel values (ship changed course)")
					vShipLoc = self.GetShipLocationInGalaxy()
					self.LTVUPOS = vShipLoc
					if self.IsPlayer == 1:
						Travel.pTravelSet.GetRegion().Location = vShipLoc
						self.Logger.LogString(" -Set travel set location")
					vGoingTo = self.DestSet.GetRegion().GetLocation()
					vDist = App.NiPoint2(vGoingTo.x - vShipLoc.x, vGoingTo.y - vShipLoc.y)
					self.TravelValues = Galaxy.GetWarpValues(vDist.Length(), self.GetRealSpeed())
					self.TravelValues['DistanceVector'] = vDist
					self.TimeToReach = self.TravelValues['Time']
					self.Logger.LogString(" -New time to reach: "+str(self.TimeToReach)+" seconds")
					self.TimeLeft = self.TimeToReach
					if self.IsPlayer == 1:
						ShowTextBanner("Destination has changed", 0.5, 0.35, 2.0, 16, 1, 0)
					self.Logger.LogString(" -Finished updating travel values")
			elif self.Started == 0:
				self.DestinationScript = ""
				self.DestSet = None
				self.Logger.LogString("Destination set as None")
		except:
			self._LogError("SetDestination")
	def GetDestination(self):
		debug(__name__ + ", GetDestination")
		return self.DestinationScript
	# The Player Travel will check for ENTERED_SET event to play a warp flash for the ships.
	def ShipEnteredSet(self, pEvent):
		debug(__name__ + ", ShipEnteredSet")
		try:
			if self.IsPlayer == 0:
				return
			if self.Started == 0:
				return
			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			if pShip == None:
				return
			if pShip.GetObjID() == self.Ship.GetObjID():
				return
			if self.Towee != None and pShip.GetObjID() == self.Towee.GetObjID():
				# showing the warp flash for the ship we're towing isn't needed
				### remember, to update this so that towee of AI ship aren't "flashed" as well...
				return
			pSet = pShip.GetContainingSet()
			if pSet == None:
				return
			if pSet.GetName() == "TravelSet":
				pFlash = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
				pFlash.Play()
				self.Logger.LogString("Played Warp Flash for ship "+pShip.GetName())
		except:
			self._LogError("ShipEnteredSet")
	# However, all non-player ships will play their own warp flash before exiting.
	# Because in theory this way it seems more plausible to work on the first try, because when the EXITED_SET event
	# triggers, it's possible that the ship is already out of the TravelSet, which could possibly make the warp flash 
	# useless.
	# Plus, this function, called just before changing the ship sets to the destination, will also set up the exit point
	# and exit placement if there isn't any, and check the warp in path for obstacles.
	def ShipGoingToExit(self, pSet):
		debug(__name__ + ", ShipGoingToExit")
		try:
			bPlayFlash = 1
			if self.IsPlayer == 1:
				bPlayFlash = 0
			if self.IsAIinPlayerRoute == 0:
				bPlayFlash = 0
			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer == None:
				bPlayFlash = 0
			pTravel = App.g_kTravelManager.GetTravel(pPlayer)
			if pTravel != None:
				if pTravel.Started == 1 and bPlayFlash == 1:
					pFlash = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", self.Ship.GetObjID())
					pFlash.Play()
					self.Logger.LogString("Played Warp Flash of self exiting travel.")
			###
			self.Logger.LogString("Checking Exit Point/Placement and exiting path...")
			vLocation = self.GetExitLocationVector()
			if vLocation == None:
				vLocation = GetRandomNewLocation(self.Ship, 0)
			fRadius = self.Ship.GetRadius() * 2.0
			while pSet.IsLocationEmptyTG(vLocation, fRadius, 1) == 0:
				vLocation = GetRandomNewLocation(self.Ship, 0, vLocation)

			pPlacement = self.GetExitPlacement()
			if pPlacement == None:
				iIndex = 1
				while 1:
					sPlacement = "TravelerWarpPlacement"+str(iIndex)
					if not App.PlacementObject_GetObject(pSet, sPlacement):
						break
					iIndex = iIndex + 1
				vEnd = App.TGPoint3_GetRandomUnitVector()
				vEnd.Scale(1000.0)
				vEnd.Add(vLocation)
				vPlaDir = App.TGPoint3()
				vPlaDir.SetXYZ(1.0, 0.0, 0.0)
				vPlaDir.Unitize()
				vPlaUp = App.TGPoint3()
				vPlaUp.SetXYZ(0.0, 1.0, 0.0)
				vPlaUp.Unitize()
				pPlacement = App.PlacementObject_Create(sPlacement, pSet.GetName(), None)
				pPlacement.SetTranslate(vEnd)
				pPlacement.AlignToVectors(vPlaDir, vPlaUp)
				pPlacement.UpdateNodeOnly()
				self.SetExitPlacementName(sPlacement)
			self.SetExitLocationVector(vLocation)

			pPathCheck = App.TGScriptAction_Create("Custom.GalaxyCharts.WarpSequence_Override", "CheckWarpInPath", self.TravelerSequence, self.Ship.GetObjID())
			pPathCheck.Play()
		except:
			self._LogError("ShipGoingToExit")
	# it's possible to make a ship tractor and tow another ship while targetting other obj, but make sure to update it
	# cuz if the ship changes target the tractor will disengage.
	def SetupTowing(self):
		debug(__name__ + ", SetupTowing")
		try:
			if self.IsTowingEnabled() != 1:
				return
			# Figure out if we're towing a ship right now.
			pTractor = self.Ship.GetTractorBeamSystem()
			if (not pTractor)  or  (not pTractor.IsOn())  or  (pTractor.IsDisabled()):
				return

			# Tractor beam mode needs to be set to Tow, and must be firing.
			if (pTractor.GetMode() != App.TractorBeamSystem.TBS_TOW)  or  (not pTractor.IsFiring()):
				return

			# ***FIXME: We're assuming that, just because we're firing, we're
			# hitting the right target.
			#I didn't found this "GetTargetList" method on App, but somehow it works...
			try:
				pTarget = pTractor.GetTargetList()[0]
				if not pTarget:
					return
			except IndexError:
				# probably for some reason the tractor didn't had a target, return
				return

			self.vTowPosition = pTarget.GetWorldLocation()
			self.vTowPosition.Subtract( self.Ship.GetWorldLocation() )
			self.vTowPosition.MultMatrixLeft( self.Ship.GetWorldRotation().Transpose() )

			self.Towee = pTarget
			App.g_kTravelManager.SetToweeShip(self.Towee, 1)
			self.bTractorStat = 1
			self.Logger.LogString(" Towing was set up. Towee: "+self.Towee.GetName()+" ("+str(self.Towee.GetObjID())+")")
		except:
			self._LogError("SetupTowing")
	def MaintainTowing(self):
		debug(__name__ + ", MaintainTowing")
		try:
			if (self.Started == 1 or self.SeqStat == self.ENGAGING or self.SeqStat == self.EXITING) and self.bTractorStat == 1:
				pTractor = self.Ship.GetTractorBeamSystem()
				if pTractor == None:
					# self has no tractor beam... what the fuck?!?
					return
				elif pTractor.IsDisabled() == 1:
					### self tractors are disabled... for now, better bail out...
					return
				if pTractor.IsOn() == 0:
					pTractor.TurnOn()
					if pTractor.IsOn() == 0:
						### couldn't set the tractors on for some reason... for now, better bail out...
						return
				if pTractor.GetMode() != App.TractorBeamSystem.TBS_TOW:
					# the tractor beam system mode was changed, so set it back to tow to make sure that
					# no problems will occur, and the process of towing a ship thru travel goes smoothly
					pTractor.SetMode(App.TractorBeamSystem.TBS_TOW)

				# Update/Maintain the towee's position and speed with the tower.
				vPosition = App.TGPoint3()
				vPosition.Set( self.vTowPosition )
				vPosition.MultMatrixLeft( self.Ship.GetWorldRotation() )
				vPosition.Add( self.Ship.GetWorldLocation() )
				self.Towee.SetTranslate(vPosition)
				# Set it to match velocities.
				self.Towee.SetVelocity( self.Ship.GetVelocityTG() )
				self.Towee.UpdateNodeOnly()

				vOffset = App.TGPoint3()
				vOffset.SetXYZ(0, 0, 0)
				if pTractor.IsFiring():
					try:
						pTarget = pTractor.GetTargetList()[0]
					except IndexError:
						return

					if pTarget == None:
						# self is tractoring target None, so resume tractoring on the Towee
						pTractor.StartFiring(self.Towee, vOffset)
					else:
						if pTarget.GetObjID() != self.Towee.GetObjID():
							# self is tractoring another ship...
							### for now, it's better to resume towing the Towee, we'll think what we can do
							### when this happens later.
							pTractor.StartFiring(self.Towee, vOffset)
				else:
					# self isn't tractoring anymore, so resume tractoring on the Towee
					pTractor.StartFiring(self.Towee, vOffset)
		except:
			self._LogError("MaintainTowing")
	def DegradationCheck(self):
		debug(__name__ + ", DegradationCheck")
		try:
			if self.Started == 1:
				lSystemsToDegrade = self.GetDegradationSystems()
				if lSystemsToDegrade == []:
					return
				fCurrentSpeed = self.GetSpeed()
				fRealCruiseSpeed = self.GetCruiseSpeed()
				fRealMaxSpeed = self.GetMaxSpeed()
				fCruiseSpeed = self.GetActualCruiseSpeed()
				fMaxSpeed = self.GetActualMaxSpeed()
				if fCurrentSpeed > fMaxSpeed and fRealMaxSpeed != fRealCruiseSpeed:
					# Ship is travelling faster than max, really bizarre, anyway still degrade engines.
					fSpeedDiff = fCurrentSpeed - fCruiseSpeed
					MaxDmg = fSpeedDiff * 250
					MinDmg = fSpeedDiff * 50
					for pSystem in lSystemsToDegrade:
						DamageSystem(pSystem, MinDmg, MaxDmg)
					self.DegradeSoundCheck = self.DegradeSoundCheck + 2
				elif fCurrentSpeed > fCruiseSpeed:
					# Ship is travelling faster than cruise, degrade engines.
					fSpeedDiff = fCurrentSpeed - fCruiseSpeed
					MaxDmg = fSpeedDiff * 30
					MinDmg = fSpeedDiff * 5
					for pSystem in lSystemsToDegrade:
						DamageSystem(pSystem, MinDmg, MaxDmg)
					self.DegradeSoundCheck = self.DegradeSoundCheck + 1
				else:
					self.DegradeSoundCheck = 0
				
				# After 3 update loops play the degradation alert if it is the player.
				if self.IsPlayer == 1:
					if self.DegradeSoundCheck >= 12:
						self.DegradeSoundCheck = 0
						# returning 1 (bool) here will make the Travel.Update method, which continously calls this method,
						# to play the degradation alert sound.
						return 1
				else:
					self.DegradeSoundCheck = 0
		except:
			self._LogError("DegradationCheck")
	def StopTowing(self):
		debug(__name__ + ", StopTowing")
		try:
			if self.bTractorStat == 0:
				return
			self.MaintainTowing()
			App.g_kTravelManager.SetToweeShip(self.Towee, 0)
			self.Towee = None
			self.bTractorStat = 0
			self.Logger.LogString(" Stopped Towing...")
		except:
			self._LogError("StopTowing")
	def SetEnableTowing(self, bEnable):
		debug(__name__ + ", SetEnableTowing")
		if bEnable == self.EnableTowing:
			return
		self.EnableTowing = bEnable
		self.Logger.LogString("Enable Towing: "+str(bEnable))
	def IsTowingEnabled(self):
		debug(__name__ + ", IsTowingEnabled")
		if self.CanTowShips() == 1 and self.EnableTowing == 1:
			return 1
		else:
			return 0
	def SetTravelBlindly(self, bTravelBlindly):
		debug(__name__ + ", SetTravelBlindly")
		if self.TravelBlindly == bTravelBlindly:
			return
		self.TravelBlindly = bTravelBlindly
		self.Logger.LogString("Travel Blindly: "+str(bTravelBlindly))
	def IsTravelBlindly(self):
		debug(__name__ + ", IsTravelBlindly")
		return self.TravelBlindly
	def GetShip(self):
		debug(__name__ + ", GetShip")
		return self.Ship
	def AddArrivedEvent(self, event):
		debug(__name__ + ", AddArrivedEvent")
		try:
			if event != None:
				self.ArrivedEvents.append(event)
				self.Logger.LogString("Arrived Events:  added event "+str(event))
		except:
			self._LogError("AddArrivedEvent")
	def AddStartWarpEvent(self, event):
		debug(__name__ + ", AddStartWarpEvent")
		try:
			if event != None:
				self.StartWarpEvents.append(event)
				self.Logger.LogString("StartWarp Events:  added event "+str(event))
		except:
			self._LogError("AddStartWarpEvent")
	def GetArrivedEvents(self):	return self.ArrivedEvents
	def SetExitPlacementName(self, sPlacementName):
		debug(__name__ + ", SetExitPlacementName")
		try:
			self.ExitPlacementName = sPlacementName
			self.Logger.LogString("Set Exit Placement Name as "+str(sPlacementName))
		except:
			self._LogError("SetExitPlacementName")
	def GetExitPlacementName(self):	return self.ExitPlacementName
	def GetExitLocationVector(self):
		debug(__name__ + ", GetExitLocationVector")
		return self.ExitPoint
	def SetExitLocationVector(self, vec):
		debug(__name__ + ", SetExitLocationVector")
		if vec != None:
			if self.ExitPoint != None and self.ExitPoint.x == vec.x and self.ExitPoint.y == vec.y and self.ExitPoint.z == vec.z:
				return
			else:
				self.ExitPoint = vec
				self.Logger.LogString("Set Exit Point to "+str(vec)+" // components: X = "+str(vec.x)+",  Y = "+str(vec.y)+",  Z = "+str(vec.z))
		else:
			self.ExitPoint = None
			self.Logger.LogString("Set Exit Point to None")
	def GetExitPlacement(self):
		debug(__name__ + ", GetExitPlacement")
		try:
			if self.DestSet == None or self.ExitPlacementName == None:
				return None
			pPlacement = App.PlacementObject_GetObject(self.DestSet, self.ExitPlacementName)
			return pPlacement
		except:
			self._LogError("GetExitPlacement")	
	def GetLaunchCoordinates(self):
		debug(__name__ + ", GetLaunchCoordinates")
		if self.__launchPos == None:
			return None
		else:
			vPos = App.TGPoint3()
			vPos.SetXYZ(self.__launchPos[0], self.__launchPos[1], self.__launchPos[2])
			return vPos
	def SetSpeed(self, fSpeed):
		debug(__name__ + ", SetSpeed")
		if fSpeed == self.GetSpeed() or type(fSpeed) != type(1.0) or (self.CanChangeSpeed() == 0 and self.IsTravelling() == 1):
			return
		else:
			if fSpeed > self.GetMaxAllowedSpeed():
				fSpeed = self.GetMaxAllowedSpeed()
			if fSpeed < self.GetMinAllowedSpeed():
				fSpeed = self.GetMinAllowedSpeed()
			self.__speedAmount = fSpeed
		if self.__travelType == "Warp":
			self.Ship.SetWarpSpeed(fSpeed)
		if self.Started == 1:
			if self.StreaksNode != None:
				self.StreaksNode.SetWarpFactor(fSpeed)
			# update time to reach/time left based on new warp values calculation.
			self.Logger.LogString("Updating travel values (ship changed speed)")
			self.Logger.LogString(" -New Speed: "+str(fSpeed))
			vShipLoc = self.GetShipLocationInGalaxy()
			self.LTVUPOS = vShipLoc
			if self.IsPlayer == 1:
				Travel.pTravelSet.GetRegion().Location = vShipLoc
				self.Logger.LogString(" -Set travel set location")
			vGoingTo = self.DestSet.GetRegion().GetLocation()
			vDist = App.NiPoint2(vGoingTo.x - vShipLoc.x, vGoingTo.y - vShipLoc.y)
			self.TravelValues = Galaxy.GetWarpValues(vDist.Length(), self.GetRealSpeed())
			self.TravelValues['DistanceVector'] = vDist
			self.TimeToReach = self.TravelValues['Time']
			self.Logger.LogString(" -New time to reach: "+str(self.TimeToReach)+" seconds")
			self.TimeLeft = self.TimeToReach
			if self.IsPlayer == 1:
				ShowTextBanner(self.__travelType+" Speed has changed.", 0.5, 0.35, 2.0, 16, 1, 0)
			self.Logger.LogString(" -Finished updating travel values")
	def GetSpeed(self):
		debug(__name__ + ", GetSpeed")
		return self.__speedAmount
	def GetRealSpeed(self):
		debug(__name__ + ", GetRealSpeed")
		return App.g_kTravelManager.ConvertTravelTypeSpeedIntoCs(self.__travelType, self.GetSpeed())
	def GetMaxSpeed(self):
		debug(__name__ + ", GetMaxSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0.0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetMaxSpeed")
			oRet = pFunc(self)
			if type(oRet) == type(1.0):
				if oRet > self.GetMaxAllowedSpeed():
					return self.GetMaxAllowedSpeed()
				if oRet < self.GetMinAllowedSpeed():
					return self.GetMinAllowedSpeed()
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetMaxSpeed method returns a "+str(type(oRet))+", not a float.")
				return self.GetMaxAllowedSpeed()
		except:
			self._LogError("GetMaxSpeed")
	def GetActualMaxSpeed(self):
		debug(__name__ + ", GetActualMaxSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0.0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetActualMaxSpeed")
			oRet = pFunc(self)
			if type(oRet) == type(1.0):
				if oRet > self.GetMaxAllowedSpeed():
					return self.GetMaxAllowedSpeed()
				if oRet < self.GetMinAllowedSpeed():
					return self.GetMinAllowedSpeed()
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetActualMaxSpeed method returns a "+str(type(oRet))+", not a float.")
				return self.GetMaxAllowedSpeed()
		except:
			self._LogError("GetActualMaxSpeed")
	def GetCruiseSpeed(self):
		debug(__name__ + ", GetCruiseSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0.0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetCruiseSpeed")
			oRet = pFunc(self)
			if type(oRet) == type(1.0):
				if oRet > self.GetMaxAllowedSpeed():
					return self.GetMaxAllowedSpeed()
				if oRet < self.GetMinAllowedSpeed():
					return self.GetMinAllowedSpeed()
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetCruiseSpeed method returns a "+str(type(oRet))+", not a float.")
				return self.GetMaxAllowedSpeed()/2
		except:
			self._LogError("GetCruiseSpeed")
	def GetActualCruiseSpeed(self):
		debug(__name__ + ", GetActualCruiseSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0.0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetActualCruiseSpeed")
			oRet = pFunc(self)
			if type(oRet) == type(1.0):
				if oRet > self.GetMaxAllowedSpeed():
					return self.GetMaxAllowedSpeed()
				if oRet < self.GetMinAllowedSpeed():
					return self.GetMinAllowedSpeed()
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetActualCruiseSpeed method returns a "+str(type(oRet))+", not a float.")
				return self.GetMaxAllowedSpeed()/2
		except:
			self._LogError("GetActualCruiseSpeed")
	def GetDegradationSoundFileName(self):
		debug(__name__ + ", GetDegradationSoundFileName")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return ""
			oSoundFile = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "sDegradationSoundFile")
			if type(oSoundFile) == type(""):
				return oSoundFile
			else:
				# return default GC degradation sound file, and log the occured.
				self.Logger.LogError("Travel Type "+self.__travelType+" Degradation Sound File attribute is a "+str(type(oSoundFile))+", not string.")
				return "scripts\\Custom\\GalaxyCharts\\Sounds\\DegradationAlert.wav"
		except:
			self._LogError("GetDegradationSoundFileName")
	def GetTravelSetToUse(self):
		debug(__name__ + ", GetTravelSetToUse")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return None
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetTravelSetToUse")
			return pFunc(self)
		except:
			self._LogError("GetTravelSetToUse")
	# this function returns travelling method type specifically setup events
	def GetStartTravelEvents(self):
		debug(__name__ + ", GetStartTravelEvents")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return []
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetStartTravelEvents")
			oRet = pFunc(self)
			if type(oRet) == type([]):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetStartTravelEvents method returns a "+str(type(oRet))+", not a list.")
				return []
		except:
			self._LogError("GetStartTravelEvents")
	# this function returns travelling method type specifically setup events
	def GetExitedTravelEvents(self):
		debug(__name__ + ", GetExitedTravelEvents")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return []
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetExitedTravelEvents")
			oRet = pFunc(self)
			if type(oRet) == type([]):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetExitedTravelEvents method returns a "+str(type(oRet))+", not a list.")
				return []
		except:
			self._LogError("GetExitedTravelEvents")
	def CanTravel(self):
		debug(__name__ + ", CanTravel")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return "no travel type set..."
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "CanTravel")
			oRet = pFunc(self)
			if type(oRet) == type(1):
				# check if ship is docked. The WarAI DockingAI uses this, dunno what else uses these functions from App.ShipClass
				if self.Ship.IsDocked() == 1:
					return "Can't travel while docked."

				iRF = self.GetRestrictionFlag()
				if self.DestSet == None:
					return 1
				pRegion = self.Ship.GetContainingSet().GetRegion()
				pDestRegion = self.DestSet.GetRegion()
				ISA = [pRegion.GetOnlyByRestrictedMethods(), int(self.__travelType in pRegion.GetRestrictedFor())]
				DSA = [pDestRegion.GetOnlyByRestrictedMethods(), int(self.__travelType in pDestRegion.GetRestrictedFor())]
				
				if ISA == [1,0]:
					return "Restricted. This travelling method doesn't work here."
				elif DSA == [1,0]:
					return "Restricted. This travelling method can't go to selected destination."
				elif iRF == 0: #no restriction
					return 1
				elif iRF == 1: #can only be used between RSs  (when in a RS to travel to another RS)
					if ISA[1] == 1 and DSA[1] == 1:
						return 1
					else:
						return "Restricted. This travelling method can only be used between systems restricted for it."
				elif iRF == 2: #travel from anywhere to a RS, but can only return to the system where ship came from
					if DSA[1] == 1:
						return 1
					elif ISA[1] == 1 and DSA == [0,0]:
						#check if is the initial non-RS system
						if pDestRegion.GetName() == self.dSysRestrictionF2[self.__travelType]:
							return 1
						else:
							return "Restricted. Can only return to non-RS system from where we first left to enter a RS system."
					else:
						return "Restricted. This method can only be used to reach a RS from a non-RS, between RSs, and back to the initial non-RS."
				elif iRF == 3: #travel from anywhere to a RS, and can return to any system
					if ISA[1] == 1 or DSA[1] == 1:
						return 1
					else:
						return "Restricted. This travelling method can only be used to reach a RS from anywhere, between RSs, and from a RS to anywhere."
			elif type(oRet) == type(""):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" CanTravel method returns a "+str(type(oRet))+", not a bool or a string.")
				return "erroneous travel type CanTravel return value"
		except:
			self._LogError("CanTravel")
	def CanContinueTravelling(self):
		debug(__name__ + ", CanContinueTravelling")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "CanContinueTravelling")
			oRet = pFunc(self)
			if type(oRet) == type(1):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" CanContinueTravelling method returns a "+str(type(oRet))+", not a bool (integer).")
				return 0
		except:
			self._LogError("CanContinueTravelling")

	def GetEngageDirection(self):
		debug(__name__ + ", GetEngageDirection")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetEngageDirection")
			oRet = pFunc(self)
			if oRet == None or type(oRet) == type(App.TGPoint3()) or type(oRet) == type([]):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetEngageDirection method returns a "+str(type(oRet))+", not None, a TGPoint3, or a list of TGPoint3s...")
				return None
		except:
			self._LogError("GetEngageDirection")

	def DoPreEngageStuff(self):
		debug(__name__ + ", DoPreEngageStuff")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "PreEngageStuff")
			oRet = pFunc(self)
			return oRet
		except:
			self._LogError("PreEngageStuff")
	def DoPreExitStuff(self):
		debug(__name__ + ", DoPreExitStuff")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "PreExitStuff")
			oRet = pFunc(self)
			return oRet
		except:
			self._LogError("PreExitStuff")
	def GetTravellingToString(self):
		debug(__name__ + ", GetTravellingToString")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return "no travel type set..."
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "sGoingTo")
			if type(oRet) == type(""):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" sGoingTo attribute is  a "+str(type(oRet))+", not a string.")
				return "Travelling to"
		except:
			self._LogError("GetTravellingToString")
	def GetDroppedOutString(self):
		debug(__name__ + ", GetDroppedOutString")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return "no travel type set..."
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "sDropOut")
			if type(oRet) == type(""):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" sDropOut attribute is  a "+str(type(oRet))+", not a string.")
				return "Dropped out of travel..."
		except:
			self._LogError("GetDroppedOutString")
	def UseStarstreaks(self):
		debug(__name__ + ", UseStarstreaks")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "bUseStarstreaks")
			if type(oRet) == type(1):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" bUseStarstreaks attribute is a "+str(type(oRet))+", not a bool (integer).")
				return 1
		except:
			self._LogError("UseStarstreaks")
	def CanDropOut(self):
		debug(__name__ + ", CanDropOut")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "bCanDropOut")
			if type(oRet) == type(1):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" bCanDropOut attribute is a "+str(type(oRet))+", not a bool (integer).")
				return 1
		except:
			self._LogError("CanDropOut")
	def CanChangeCourse(self):
		debug(__name__ + ", CanChangeCourse")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "bCanChangeCourse")
			if type(oRet) == type(1):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" bCanChangeCourse attribute is a "+str(type(oRet))+", not a bool (integer).")
				return 1
		except:
			self._LogError("CanChangeCourse")
	def CanChangeSpeed(self):
		debug(__name__ + ", CanChangeSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "bCanChangeSpeed")
			if type(oRet) == type(1):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" bCanChangeSpeed attribute is a "+str(type(oRet))+", not a bool (integer).")
				return 1
		except:
			self._LogError("CanChangeSpeed")
	def CanTowShips(self):
		debug(__name__ + ", CanTowShips")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "bCanTowShips")
			if type(oRet) == type(1):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" bCanTowShips attribute is a "+str(type(oRet))+", not a bool (integer).")
				return 0
		except:
			self._LogError("CanTowShips")

	def GetRestrictionFlag(self):
		debug(__name__ + ", GetRestrictionFlag")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "iRestrictionFlag")
			if type(oRet) == type(1) and oRet in [0, 1, 2, 3]:
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" iRestrictionFlag attribute is a "+str(type(oRet))+", not a integer (0, 1, 2 or 3).")
				return 0
		except:
			self._LogError("GetRestrictionFlag")

	def GetDegradationSystems(self):
		debug(__name__ + ", GetDegradationSystems")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return []
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "GetDegradationSystems")
			oRet = pFunc(self)
			if type(oRet) == type([]):
				lList = []
				for pSystem in oRet:
					if pSystem != None:
						lList.append(pSystem)
				return lList
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" GetDegradationSystems method returns a "+str(type(oRet))+", not a list.")
				return []
		except:
			self._LogError("GetDegradationSystems")
	def GetMinAllowedSpeed(self):
		debug(__name__ + ", GetMinAllowedSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0.0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "fMinimumSpeed")
			if type(oRet) == type(1.0):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" fMinimumSpeed attribute is a "+str(type(oRet))+", not a float.")
				return 0.0
		except:
			self._LogError("GetMinAllowedSpeed")
	def GetMaxAllowedSpeed(self):
		debug(__name__ + ", GetMaxAllowedSpeed")
		try:
			if self.__travelType == "" or self.__travelType == "None":
				return 0.0
			oRet = App.g_kTravelManager.GetTravelTypeAttr(self.__travelType, "fMaximumSpeed")
			if type(oRet) == type(1.0):
				return oRet
			else:
				self.Logger.LogError("Travel Type "+self.__travelType+" fMaximumSpeed attribute is a "+str(type(oRet))+", not a float.")
				return 0.0
		except:
			self._LogError("GetMaxAllowedSpeed")
	def SetEnginesState(self, state):
		debug(__name__ + ", SetEnginesState")
		try:
			# pass this for code debugging...
			pass
		#	pWarpEngines = self.Ship.GetWarpEngineSubsystem()
		#	if pWarpEngines and pWarpEngines.GetWarpState() != state:
		#		# Turns out that setting the warp engine state is for those warp effects, like really fast and 
		#		# stretched ships... So just disable that for now.
		#		return
		#		#pWarpEngines.SetWarpState(state)
		#		#pWarpEngines.TransitionToState(state)
		#		self.Logger.LogString("Engine State Set: "+str(state))
		except:
			self._LogError("SetEnginesState")
	def GetWarpObstacles(self, vStart, vEnd):
		debug(__name__ + ", GetWarpObstacles")
		try:
			return MissionLib.GrabWarpObstaclesFromSet(vStart, vEnd, self.Ship.GetContainingSet(), self.Ship.GetRadius(), 1, self.Ship.GetObjID())
		except:
			self._LogError("GrabWarpObstacles")
	def __setupNebulaSystem(self):
		debug(__name__ + ", __setupNebulaSystem")
		import TravelerSystems.SpaceSet
		if Travel.pNebSet != None:
			return
		TravelerSystems.SpaceSet.SET_NAME = "Nebula System"
		Travel.pNebSet = TravelerSystems.SpaceSet.Initialize()
		###
		if WarSimulator.dShips.has_key("Nebula"):
			# ops, problem here. Ship already exists...
			# for now, do nothing else...
			return
		WarSimulator.dShips["Nebula"] = WSShip("Nebula", "Nebula System", 0)
		pNebDef = GetShipDefByScript( "Nebula" )
		pNebula = CreateShip(pNebDef, Travel.pNebSet, "Nebula", "None")
		pNebula.GetShipProperty().SetStationary(1)
		pNebula.SetInvincible(1)
		pNebula.SetHurtable(0)
		pNebula.SetTargetable(1)
		pNebula.SetScale(2.5)
		pNebula.SetTranslateXYZ(0,0,0)
		pNebula.UpdateNodeOnly()
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			pSensors = pPlayer.GetSensorSubsystem()
			if pSensors:
				pSensors.ForceObjectIdentified(pNebula)
		###
		self.Logger.LogString(" -Initialized Nebula Set")
		TravelerSystems.SpaceSet.SET_NAME = "SpaceSet"
	def GetShipLocationInGalaxy(self):
		debug(__name__ + ", GetShipLocationInGalaxy")
		try:
			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString("Ship is dead or dying (at GetShipLocationInGalaxy)")
				return
			if self.Started == 0:
				return None
			vRealDist = self.TravelValues['DistanceVector']
			vDist = App.NiPoint2(vRealDist.x, vRealDist.y)
			fDist = vDist.Length()
			if self.TimeLeft <= 0:
				fDistTraveled = fDist
			else:
				fDistTraveled = fDist - (fDist/(self.TimeToReach/self.TimeLeft))
			if fDistTraveled <= 0:
				vDist.x = 0.0
				vDist.y = 0.0
			elif fDist > fDistTraveled:
				vDist.x = vDist.x/(fDist/fDistTraveled)
				vDist.y = vDist.y/(fDist/fDistTraveled)
			#vWasIn = self.InitialShipSet.GetRegion().GetLocation()
			#vWasIn = self.Ship.GetContainingSet().GetRegion().GetLocation()
			vWasIn = App.NiPoint2(self.LTVUPOS.x, self.LTVUPOS.y)
			vShipLoc = App.NiPoint2(vWasIn.x + vDist.x, vWasIn.y + vDist.y)
			return vShipLoc
		except:
			self._LogError("GetShipLocationInGalaxy")
	def GetShipID(self):
		debug(__name__ + ", GetShipID")
		return self.Ship.GetObjID()
	def _LogError(self, strFromFunc = None):
		debug(__name__ + ", _LogError")
		import sys
		et = sys.exc_info()
		if strFromFunc == None:
			strFromFunc = "???"
		if self.Logger:
			self.Logger.LogException(et, "ERROR at "+strFromFunc)
		else:
			error = str(et[0])+": "+str(et[1])
			print "ERROR at "+strFromFunc+", details -> "+error
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+str(self.__ID)+">"

class Chaser(Travel):
	def __init__(self, pShip, pTarget, sDestination):
		debug(__name__ + ", __init__")
		Travel.__init__(self, pShip, sDestination)
		self.CLASS = "Ship Chaser"
		if GetConfigValue("LogChaser") == 1 and GetConfigValue("LogTravel") == 0:
			self.Logger = Custom.GravityFX.Logger.LogCreator(pShip.GetName()+" Travel Logger", "scripts\Custom\GalaxyCharts\Logs\Travel_"+pShip.GetName()+"_LOG.txt")
			self.Logger.LogString("Initialized "+pShip.GetName()+" Travel logger")
			self.Logger.LogString("SELF = "+self.__repr__())
		self.Logger.LogString("Chaser base class initialization complete.")
		self.Target = pTarget
		self.CanChaseTarget = 1
		if pTarget != None:
			self.TargTravel = App.g_kTravelManager.GetTravel(pTarget)
			self.Logger.LogString("Target Ship = "+str(pTarget.GetName()))
		else:
			self.TargTravel = None
			self.Logger.LogString("Target Ship = NONE")
		if self.Refresher == None:
			self.Refresher = RefreshEventHandler(self.Update, 0.1)
		else:
			self.Refresher.StartRefreshHandler('NORMAL')
		self.Logger.LogString("Chaser pre-emptive Refresher Initialization")
	def Update(self, pObject = None, pEvent = None):
		debug(__name__ + ", Update")
		try:
			# Do the check to see if the ship is dead or dying.
			# BUT don't do a return statement if it is, just use a bool to update the instance or not.
			# Making a 'return' in the RefreshEventHandler loop can cause it to stop, and that may cause bugs.
			# I remember something like this happening sometime, but i didn't tested it again to have sure.
			# And I don't want to test it now... So we just do it the bool way...
			bCanUpdate = self.CanChaseTarget
			if self.Ship.IsDying() or self.Ship.IsDead():
				self.Logger.LogString("Ship is dead or dying (at Chaser Update)")
				bCanUpdate = -1

			# Now we check for War Sim and Fleet status. If war sim is on, fleet manager is on. If both are on, then ships shall be probably using
			# our War AI. So we override the CanChaseTarget/CanUpdate variables depending on fleet situation.
			pFleet = FleetManager.GetFleetOfShip(self.Ship)
			if WarSimulator.IsInitialized() == 1 and pFleet != None:
				pLeadShip = pFleet.GetLeadShipObj()
				if self.Ship.GetObjID() == pLeadShip.GetObjID():
					# we're leading. We can go anywhere we want. BUT WE CANT CHASE ENEMY SHIPS >_<
					bCanUpdate = 0
				else:
					# we're following. Only chase if we're chasing the lead ship.
					bCanUpdate = 0
					if self.Target != None:
						if self.Target.GetObjID() == pLeadShip.GetObjID():
							bCanUpdate = 1

			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer != None and pPlayer.GetObjID() == self.Ship.GetObjID():
				# we had to do this "is player check" separately here, instead of using the normal Travel.IsPlayer
				# attribute, because that value might not be properly updated at this point, and it wouldn't be
				# very cool if we kept calling UpdateVariables() here, as we don't need to do all those checks.
				HelmAddonGUI.CreateTravelTypeButtons()
				if pObject != None or pEvent != None:
					Travel.Update(self, pObject, pEvent)
			elif bCanUpdate == 0:
				if pObject != None or pEvent != None:
					self.Logger.LogString("Ship can't chase, directing to Travel update...")
					Travel.Update(self, pObject, pEvent)
			elif bCanUpdate == 1:
				# try to re-acquire the Target Travel instance, in case we do not have it already.
				# it is needed to the update process of this class.
				if self.TargTravel == None and self.Target != None:
					pTargTravel = App.g_kTravelManager.GetTravel(self.Target)
					if pTargTravel != None:
						self.TargTravel = pTargTravel
						self.Logger.LogString("Reacquired Travel of target ship.")

				# Just check if we and our target are in the same set. Store in a bool, we'll use this a lot.
				bIsInSameSet = -1
				pSet, pTargSet = None, None
				if self.Target != None:
					pSet = self.Ship.GetContainingSet()
					pTargSet = self.Target.GetContainingSet()
					# Dunno why but it gave a error one time because pSet or pTargSet was None... Makes no sense but anyways
					# do the check then to have sure about it...
					if pSet != None and pTargSet != None:
						if pSet.GetRegionModule() == pTargSet.GetRegionModule():
							bIsInSameSet = 1
						else:
							bIsInSameSet = 0

				# And now update, if we have the target Travel...
				if self.TargTravel != None and self.Target != None and pSet != None and pTargSet != None:
					# Start with the destination/start update check
					if self.TargTravel.Started == 1:
						# so the target is travelling, lets travel as well and chase that bastard!
						if self.Started == 0:
							if self.TargTravel.DestinationScript != None and self.TargTravel.DestinationScript != pSet.GetRegionModule() and bIsInSameSet == 0 and self.SeqStat == self.NOT_ENGAGING and App.g_kTravelManager.IsShipBeingTowed(self.Ship) == 0:
								self.Logger.LogString("Beginning to chase target...")
								self.SetDestination(self.TargTravel.DestinationScript)
								sTravelType = self.__setBestChaseTT()
								if sTravelType == self.TargTravel.GetTravelType():
									self.SetSpeed(self.TargTravel.GetSpeed())
								else:
									self.SetSpeed(self.GetActualCruiseSpeed())
								self.Travel(sTravelType)
						else:
							# We're already travelling, so update our destination if our target changed his
							if self.TargTravel.DestinationScript != None and self.TargTravel.DestinationScript != self.DestinationScript:
								self.Logger.LogString("Updating destination to chase target...")
								self.SetDestination(self.TargTravel.DestinationScript)
					else:
						# the target isn't travelling, or just dropped out... update accordingly
						if self.Started == 0:
							if bIsInSameSet == 0 and self.SeqStat == self.NOT_ENGAGING and App.g_kTravelManager.IsShipBeingTowed(self.Ship) == 0:
								self.Logger.LogString("Beginning to chase target... better late than never...")
								self.SetDestination(pTargSet.GetRegionModule())
								sTravelType = self.__setBestChaseTT()
								self.SetSpeed(self.GetActualCruiseSpeed())
								self.Travel(sTravelType)
						else:
							# We're already travelling, so update our destination if our target changed his
							if pTargSet.GetRegionModule() != self.DestinationScript and bIsInSameSet == 0:
								self.Logger.LogString("Updating destination to reach targets set...")
								self.SetDestination(pTargSet.GetRegionModule())
					# then do the warp speed update check
					if self.Started == 1:
						#self.AIwarpPower 
						fCurrentSpeed = self.GetSpeed()
						fCruiseSpeed = self.GetActualCruiseSpeed()
						if self.TargTravel.Started == 1:
							fTargSpeed = self.TargTravel.GetSpeed()
							if fCurrentSpeed != fTargSpeed:
								fSpeed = fTargSpeed
								if fSpeed > fCruiseSpeed:
									self.AIwarpPower = 1.25
									fBoostedCruiseSpeed = self.GetActualCruiseSpeed()
									if fSpeed > fBoostedCruiseSpeed:
										fSpeed = fBoostedCruiseSpeed
								self.SetSpeed(fSpeed)
						elif bIsInSameSet == 0 and self.AIwarpPower != 1.25:
							self.AIwarpPower = 1.25
							fBoostedCruiseSpeed = self.GetActualCruiseSpeed()
							self.SetSpeed(fBoostedCruiseSpeed)

				if pObject != None or pEvent != None:
					# This is being called as a event call. Sooo we update our base class, otherwise
					# our travel wouldn't end =P
					Travel.Update(self, pObject, pEvent)

				# Lastly, we update our target attribute, according to our ship's target.
				# doing this lastly will make sure next update is clean, and that this update was clean too,
				# because when a ship leaves the set, the other ships that are targetting her will erase their
				# target
				#NOPE, don't do this. Can't remember why now. I'm writing this WAY after commenting this out.
				#pTarget = App.ShipClass_Cast( self.Ship.GetTarget() )
				#self.SetTarget(pTarget)
		except:
			self._LogError("Update (Chaser)")
	def __setBestChaseTT(self):
		debug(__name__ + ", __setBestChaseTT")
		if self.IsTravelling() == 1:
			return
		if self.TargTravel != None:
			lTTs = App.g_kTravelManager.GetAllTTAvailableForShip(self.Ship)
			if self.TargTravel.Started == 1:
				if self.TargTravel.GetTravelType() in lTTs:
					self.SetTravelType(self.TargTravel.GetTravelType())
					return self.TargTravel.GetTravelType()
			if len(lTTs) == 0:
				return ""
			if len(lTTs) == 1:
				return lTTs[0]
			sOldType = self.GetTravelType()
			sBestType = lTTs[0]
			self.__dict__["_Travel__travelType"] = sBestType
			#self.__travelType = sBestType
			fBestSpeed = self.GetRealSpeed()			
			del lTTs[0]
			for sTravelType in lTTs:
				self.__dict__["_Travel__travelType"] = sTravelType
				if self.CanTravel() == 1:
					fSpeed = self.GetRealSpeed()
					fFactor = App.g_kSystemWrapper.GetRandomNumber(100)
					fChance = 5.0
					if fSpeed > fBestSpeed:
						fChance = fChance + 32.5
					if self.CanDropOut() == 1:
						fChance = fChance + 17.5
					if self.CanChangeCourse() == 1:
						fChance = fChance + 22.5
					if self.CanChangeSpeed() == 1:
						fChance = fChance + 17.5
					if fFactor <= fChance:
						fBestSpeed = fSpeed
						sBestType = sTravelType
			self.__dict__["_Travel__travelType"] = sOldType
			self.SetTravelType(sBestType)
			return sBestType
	# if bReturnTTSTuple == 1, instead of simply returning the name (string) of the fastest travel type available, this method will return a tuple
	# with 2 variables:  (travel type name (string), cruise speed value(float, unit: C's))
	def GetFastestTTAvailable(self, bReturnTTSTuple = 0):
		debug(__name__ + ", GetFastestTTAvailable")
		lTTs = App.g_kTravelManager.GetAllTTAvailableForShip(self.Ship)
		if len(lTTs) == 0:
			return ""
		if len(lTTs) == 1:
			return lTTs[0]
		sOldType = self.GetTravelType()
		fOldSpeed = self.GetSpeed()
		sBestType = lTTs[0]
		self.__dict__["_Travel__travelType"] = sBestType
		#self.__travelType = sBestType
		self.SetSpeed( self.GetActualCruiseSpeed() )
		fBestSpeed = self.GetRealSpeed()			
		del lTTs[0]
		for sTravelType in lTTs:
			self.__dict__["_Travel__travelType"] = sTravelType
			self.SetSpeed( self.GetActualCruiseSpeed() )
			if self.CanTravel() == 1:
				fSpeed = self.GetRealSpeed()
				if fSpeed > fBestSpeed:
					fBestSpeed = fSpeed
					sBestType = sTravelType
		self.__dict__["_Travel__travelType"] = sOldType
		self.SetSpeed(fOldSpeed)
		if bReturnTTSTuple == 1:
			return (sBestType, fBestSpeed)
		else:
			return sBestType
	def GetTarget(self):
		debug(__name__ + ", GetTarget")
		return self.Target
	def SetTarget(self, pTarget):
		debug(__name__ + ", SetTarget")
		try:
			if pTarget == None and self.Target != None:
				self.Target = None
				self.TargTravel = None
				self.Logger.LogString("Updated Target Ship to NONE")
			elif pTarget != None:
				if self.Target != None:
					if pTarget.GetObjID() == self.Target.GetObjID():
						return
				self.Target = pTarget
				self.TargTravel = App.g_kTravelManager.GetTravel(pTarget)
				self.Logger.LogString("Updated Target Ship = "+str(pTarget.GetName()))
		except:
			self._LogError("SetTarget")
	def SetCanChaseTarget(self, bEnable):
		debug(__name__ + ", SetCanChaseTarget")
		if bEnable == self.CanChaseTarget:
			return
		self.CanChaseTarget = bEnable
		self.Logger.LogString("Can Chase Target = "+str(bEnable))

# This class handles the status of the impulse engines of a ship while warping.
# Yes, i know i should probably made her handle the warp engine status (degradation and so) too, but that is already 
# scripted in the Travel class so i'll leave it there =P
class EngineStatus:
	NORMAL = 0
	WARPING = 1
	def __init__(self, travel):
		debug(__name__ + ", __init__")
		self.Travel = travel
		self.Ship = travel.Ship
		self.Impulse = self.Ship.GetImpulseEngineSubsystem()
		self.MaxSpeed = 0
		self.MaxAccel = 0
		self.MaxAngVel = 0
		self.MaxAngAccel = 0
		self.Status = self.NORMAL
	def SetAsWarping(self):
		debug(__name__ + ", SetAsWarping")
		if self.Impulse == None:
			self.Impulse = self.Ship.GetImpulseEngineSubsystem()
		if self.Impulse != None and self.Status == self.NORMAL:
			# first, store the ship's impulse properties
			pImpProp = self.Impulse.GetProperty()
			self.MaxSpeed = pImpProp.GetMaxSpeed()
			self.MaxAccel = pImpProp.GetMaxAccel()
			self.MaxAngVel = pImpProp.GetMaxAngularVelocity()
			self.MaxAngAccel = pImpProp.GetMaxAngularAccel()
			# seconds, nullify the ship's impulse
			pImpProp.SetMaxSpeed(0.0)
			pImpProp.SetMaxAccel(0.0)
			pImpProp.SetMaxAngularVelocity(0.0)
			pImpProp.SetMaxAngularAccel(0.0)
			# now create a vector based on the warpspeed, and another vector which is all zeros
			fSpeed = self.Travel.GetSpeed()
			vVec = self.Ship.GetWorldForwardTG()
			vVec.Scale(fSpeed)
			vZero = App.TGPoint3()
			vZero.SetXYZ(0.0, 0.0, 0.0)
			# set the ship's velocity as the warpspeed based vector
			self.Ship.SetVelocity(vVec)
			# and the rest of it's movement related vector as the zero one
			self.Ship.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
			self.Ship.SetAcceleration(vZero)
			self.Ship.SetAngularAcceleration(vZero)
			# finnally, update our status.
			self.Status = self.WARPING
			# And that's how you make a ship go where you want, with no AI or user telling otherwise =)
	def MaintainWarping(self):
		# As some things like gravity or projectile weapon hit can slow down or even make the target spin
		# This method here, will be called in the Travel update, and maintain the speed and rotation we want.
		debug(__name__ + ", MaintainWarping")
		if self.Impulse != None and self.Status == self.WARPING:
			vDir = App.TGPoint3()
			vDir.SetXYZ(1.0, 0.0, 0.0)
			vDir.Unitize()
			vForward = self.Ship.GetWorldForwardTG()
			if AreVectorsDifferent(vForward, vDir) == 1:
				vUp = App.TGPoint3()
				vUp.SetXYZ(0.0, 1.0, 0.0)
				vUp.Unitize()
				self.Ship.AlignToVectors(vDir, vUp)
				self.Ship.UpdateNodeOnly()

			fSpeed = self.Travel.GetSpeed()
			vDir.Scale(fSpeed)
			vZero = App.TGPoint3()
			vZero.SetXYZ(0.0, 0.0, 0.0)
			self.Ship.SetVelocity(vDir)
			self.Ship.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
			self.Ship.SetAcceleration(vZero)
			self.Ship.SetAngularAcceleration(vZero)			
	def SetAsNormal(self):
		debug(__name__ + ", SetAsNormal")
		if self.Impulse == None:
			self.Impulse = self.Ship.GetImpulseEngineSubsystem()
		if self.Impulse != None and self.Status == self.WARPING:
			pImpProp = self.Impulse.GetProperty()
			pImpProp.SetMaxSpeed(self.MaxSpeed)
			pImpProp.SetMaxAccel(self.MaxAccel)
			pImpProp.SetMaxAngularVelocity(self.MaxAngVel)
			pImpProp.SetMaxAngularAccel(self.MaxAngAccel)
			self.Ship.SetSpeed(9, self.Ship.GetWorldForwardTG(), App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
			self.Status = self.NORMAL

##########################
# Helper Functions
##########################
def ChangeShipSet(pTravel, pNewSet):
	debug(__name__ + ", ChangeShipSet")
	pShip = pTravel.Ship
	pOldSet = pShip.GetContainingSet()
	pOldSet.RemoveObjectFromSet(pShip.GetName())
	pNewSet.AddObjectToSet(pShip, pShip.GetName())

	bIsForTravel = 0
	if pTravel.IsTravelling() == 1:
		bIsForTravel = 1
		pPlacement = None

	# Set ship new location
	vLocation = pTravel.GetExitLocationVector()
	if vLocation == None or bIsForTravel == 1:
		vLocation = GetRandomNewLocation(pShip, bIsForTravel)

	fRadius = pShip.GetRadius() * 1.8
	while pNewSet.IsLocationEmptyTG(vLocation, fRadius, 1) == 0:
		vLocation = GetRandomNewLocation(pShip, bIsForTravel, vLocation)
	pShip.SetTranslate(vLocation)

	if bIsForTravel == 0:
		pPlacement = pTravel.GetExitPlacement()
		if pPlacement == None:
			iIndex = 1
			while 1:
				sPlacement = "TravelerWarpPlacement"+str(iIndex)
				if not App.PlacementObject_GetObject(pNewSet, sPlacement):
					break
				iIndex = iIndex + 1
			vEnd = App.TGPoint3_GetRandomUnitVector()
			vEnd.Scale(1000.0)
			vEnd.Add(vLocation)
			vPlaDir = App.TGPoint3()
			vPlaDir.SetXYZ(1.0, 0.0, 0.0)
			vPlaDir.Unitize()
			vPlaUp = App.TGPoint3()
			vPlaUp.SetXYZ(0.0, 1.0, 0.0)
			vPlaUp.Unitize()
			pPlacement = App.PlacementObject_Create(sPlacement, pNewSet.GetName(), None)
			pPlacement.SetTranslate(vEnd)
			pPlacement.AlignToVectors(vPlaDir, vPlaUp)
			pPlacement.UpdateNodeOnly()
			pTravel.SetExitPlacementName(sPlacement)
		pTravel.SetExitLocationVector(vLocation)

	vDir = None
	vUp = None
	if pPlacement != None:
		vDir = GetVectorFromToByPoints(pPlacement.GetWorldLocation(), vLocation)
		vRight = vDir.Cross( pShip.GetWorldUpTG() )
		vUp = vRight.UnitCross(vDir)
	elif bIsForTravel == 1:
		vDir = App.TGPoint3()
		vDir.SetXYZ(1.0, 0.0, 0.0)
		vDir.Unitize()
		vUp = App.TGPoint3()
		vUp.SetXYZ(0.0, 1.0, 0.0)
		vUp.Unitize()
	if vDir != None and vUp != None:
		pShip.AlignToVectors(vDir, vUp)

	# Update the ship with its new positional information...
	pShip.UpdateNodeOnly()

	# update the proximity manager with this object's new position.
	pProxManager = pNewSet.GetProximityManager()
	if pProxManager:
		pProxManager.UpdateObject(pShip)

def ChangeToweeSet(pTravel, pNewSet):
	debug(__name__ + ", ChangeToweeSet")
	if pTravel.bTractorStat != 1 or pTravel.Towee == None:
		return
	pShip = pTravel.Towee
	pOldSet = pShip.GetContainingSet()
	pOldSet.RemoveObjectFromSet(pShip.GetName())
	pNewSet.AddObjectToSet(pShip, pShip.GetName())

	# Set ship new location
	vLocation = pTravel.Ship.GetWorldLocation()
	vPlus = pTravel.Ship.GetWorldBackwardTG()
	vPlus.Scale(1.5)
	vLocation.Add(vPlus)

	fRadius = pShip.GetRadius() * 2.0
	while pNewSet.IsLocationEmptyTG(vLocation, fRadius, 1) == 0:
		vLocation = GetRandomNewLocation(pShip, 0, vLocation)
	pShip.SetTranslate(vLocation)

	# Update the ship with its new positional information...
	pShip.UpdateNodeOnly()

	# update the proximity manager with this object's new position.
	pProxManager = pNewSet.GetProximityManager()
	if pProxManager:
		pProxManager.UpdateObject(pShip)

def GetRandomNewLocation(pShip, bIsForTravelSet, vBaseLoc = None):
	debug(__name__ + ", GetRandomNewLocation")
	if vBaseLoc == None:
		vOrigin = pShip.GetWorldLocation()
	else:
		vOrigin = vBaseLoc
	vOffset = pShip.GetWorldForwardTG()
	
	# Add some random amount to vOffset
	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber(30) + 1)
	vOffset.SetX(vOffset.GetX() + fUnitRandom)

	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber(30) + 1)
	vOffset.SetY(vOffset.GetY() + fUnitRandom)

	fUnitRandom = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
	fUnitRandom = fUnitRandom * (App.g_kSystemWrapper.GetRandomNumber(30) + 1)
	vOffset.SetZ(vOffset.GetZ() + fUnitRandom)
	
	vOrigin.Add(vOffset)
	if bIsForTravelSet == 1:
		# Okay so we're getting a random location to put a ship in one of the Travel Sets...
		# So we want that all ships start in a wall like pattern in the travel set, because they all will be heading
		# forward, so we set the location's X component to the following, which is 1000 kilometers behind the 
		# 0 mark in the coord grid of the set.
		vOrigin.SetX(-5714.28564453)
	return vOrigin

def AreVectorsDifferent(vVec1, vVec2):
	debug(__name__ + ", AreVectorsDifferent")
	if vVec1.x != vVec2.x or vVec1.y != vVec2.y or vVec1.z != vVec2.z:
		return 1
	return 0



def MaintainTowingAction(pAction, pTravel):
	debug(__name__ + ", MaintainTowingAction")
	if pTravel.bTractorStat == 1 and pTravel.Towee != None:
		pTravel.MaintainTowing()
	return 0

def PlayerDeleteTravellingFix(pObject, pEvent):
	debug(__name__ + ", PlayerDeleteTravellingFix")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer != None:
		App.g_kTravelManager.DeleteTravel(pPlayer)

def DisableLaunchShuttleButtons(pObject, pEvent):
	debug(__name__ + ", DisableLaunchShuttleButtons")
	lLaunchButtons = GetLaunchShuttleButtons()
	if lLaunchButtons != []:
		for pLaunchButton in lLaunchButtons:
			if pLaunchButton.IsEnabled() == 1:
				pLaunchButton.SetDisabled()

def FinishTravelInterceptAction(pAction, pTravel):
	debug(__name__ + ", FinishTravelInterceptAction")
	pTravel.FinishTravelIntercept()
	return 0

def InterceptUpdateAction(pAction, pTravel):
	debug(__name__ + ", InterceptUpdateAction")
	pTravel.InterceptUpdate()
	return 0

def FinishStopInterceptAction(pAction, pTravel):
	debug(__name__ + ", FinishStopInterceptAction")
	pTravel.FinishStopIntercept()
	return 0