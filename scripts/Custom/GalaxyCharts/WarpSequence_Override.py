from bcdebug import debug
###############################################################################################################
#   WarpSequence_Override.py                 by Fernando Aluani
############
# This script contains the overrides for BC's WarpSequence class, and some related method of other classes and App itself.
# This is where the warp sequence (entering and exiting sequences) are set up, and this script also holds some function
# actions used in the warp sequence itself and in the Traveler script.
###############################################################################################################
import App
import Custom.GravityFX.Logger
import Custom.GravityFX.GravityFXlib
import Appc
import string
import WarpSequence
import GalaxyLIB
import MissionLib
import GalacticWarSimulator

def GetPlacement(self):
	debug(__name__ + ", GetPlacement")
	pWarpSeq = self.GetWarpSequence()
	if pWarpSeq:
		return pWarpSeq.Travel.GetExitPlacement()
def GetWarpExitLocation(self):
	debug(__name__ + ", GetWarpExitLocation")
	pWarpSeq = self.GetWarpSequence()
	if pWarpSeq:
		return pWarpSeq.GetExitPoint()
def GetWarpExitRotation(self):
	# for now ships doesn't have a rotation when coming out of warp
	# So we need a matrix with all components zero. Hopefully this will do it. =P
	debug(__name__ + ", GetWarpExitRotation")
	pMatrix = App.TGMatrix3()
	pMatrix.MakeZero()
	return pMatrix
def GetWarpSequence(self):
	debug(__name__ + ", GetWarpSequence")
	pTravel = App.g_kTravelManager.GetTravel(self.GetParentShip())
	if pTravel:
		return pTravel.TravelerSequence
def Warp(self):
	debug(__name__ + ", Warp")
	pWarpSeq = self.GetWarpSequence()
	if pWarpSeq:
		pWarpSeq.Play()
def SetPlacement(self, pPlacement):
	debug(__name__ + ", SetPlacement")
	pWarpSeq = self.GetWarpSequence()
	if pWarpSeq:
		return pWarpSeq.SetPlacement(pPlacement.GetName())
def SetExitPoint(self, vPos):
	debug(__name__ + ", SetExitPoint")
	pWarpSeq = self.GetWarpSequence()
	if pWarpSeq:
		return pWarpSeq.SetExitPoint(vPos)

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
def WarpSequence_Create(pShip, sToSetName, fWarpTime, sPlacementName = None):  #(*args, **kwargs):
	#val = apply(Appc.WarpSequence_Create,args,kwargs)
	#if val: val = WarpSequencePtr(val)
	debug(__name__ + ", WarpSequence_Create")
	if pShip == None:
		return None
	print "Creating WarpSequence:  Ship =", pShip.GetName(), " // To Set =", sToSetName, " // Placement Name =", sPlacementName
	pTravel = App.g_kTravelManager.CreateTravel(pShip)
	pTravel.SetDestination(sToSetName)
	pTravel.SetExitPlacementName(sPlacementName)
	pTWS = pTravel.TravelerSequence
	return pTWS

def WarpSequence_Cast(pCastObj):
	#val = apply(Appc.WarpSequence_Cast,args,kwargs)
	#if val: val = WarpSequencePtr(val)
	debug(__name__ + ", WarpSequence_Cast")
	try:
		if pCastObj.CLASS == "Traveler Warp Sequence":
			return pCastObj
		return None
	except:
		return None

def WarpSequence_GetWarpSet():
	#val = apply(Appc.WarpSequence_GetWarpSet,args,kwargs)
	#if val: val = SetClassPtr(val)
	debug(__name__ + ", WarpSequence_GetWarpSet")
	pTravelSet = App.g_kSetManager.GetSet("TravelSet")
	if not pTravelSet:
		pTravelSet = App.g_kSetManager.GetSet("AITravelSet")
	return pTravelSet

##########################################################################################################################
class TravelerWarpSequence:
	PRE_WARP_SEQUENCE = Appc.WarpSequence_PRE_WARP_SEQUENCE
	DURING_WARP_SEQUENCE = Appc.WarpSequence_DURING_WARP_SEQUENCE
	POST_DURING_WARP_SEQUENCE = Appc.WarpSequence_POST_DURING_WARP_SEQUENCE
	POST_WARP_SEQUENCE = Appc.WarpSequence_POST_WARP_SEQUENCE
	WARP_BEGIN_ACTION = Appc.WarpSequence_WARP_BEGIN_ACTION
	WARP_END_ACTION = Appc.WarpSequence_WARP_END_ACTION
	DEWARP_BEGIN_ACTION = Appc.WarpSequence_DEWARP_BEGIN_ACTION
	DEWARP_END_ACTION = Appc.WarpSequence_DEWARP_END_ACTION
	WARP_ENTER_ACTION = Appc.WarpSequence_WARP_ENTER_ACTION
	DEWARP_FINISH_ACTION = Appc.WarpSequence_DEWARP_FINISH_ACTION
	MOVE_ACTION_1 = Appc.WarpSequence_MOVE_ACTION_1
	MOVE_ACTION_2 = Appc.WarpSequence_MOVE_ACTION_2

	def __init__(self, pTravel):
		debug(__name__ + ", __init__")
		self.Travel = pTravel
		self.EngageWarpSeq = None
		self.DuringWarpSeq = None
		self.ExitWarpSeq = None
		self.CLASS = "Traveler Warp Sequence"
		self.__ID = Custom.GravityFX.GravityFXlib.GetUniqueID("")
		if GalaxyLIB.GetConfigValue("LogTWS") == 1:
			self.Logger = Custom.GravityFX.Logger.LogCreator("TravelerWarpSequence of Ship "+self.Travel.Ship.GetName(), "scripts\Custom\GalaxyCharts\Logs\TWS_"+self.Travel.Ship.GetName()+"_LOG.txt")
			self.Logger.LogString("Initialized TravelerWarpSequence of ship "+self.Travel.Ship.GetName()+" logger")
			self.Logger.LogString("SELF = "+self.__repr__())
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
	
	def __repr__(self):
		debug(__name__ + ", __repr__")
		if hasattr(self, "this"):
			self.Logger.LogString("self has attribute this = "+str(self.this))
			return "<C WarpSequence instance at %s>" % (self.this,)
		else:
			return "<C WarpSequence instance at %s>" % (self.__ID,)

	# TGObject's methods:
	def GetObjType(self):
		debug(__name__ + ", GetObjType")
		self.Logger.LogString("GetObjType called")
		return App.CT_WARP_SEQUENCE
	def IsTypeOf(self, iType):
		debug(__name__ + ", IsTypeOf")
		if iType == self.GetObjType():
			self.Logger.LogString("IsTypeOf called (true)")
			return 1
		self.Logger.LogString("IsTypeOf called (false)")
		return 0
	def GetObjID(*args):
		debug(__name__ + ", GetObjID")
		args[0].Logger.LogString("GetObjID called, ARGS = "+str(args))
	def Destroy(self):
		debug(__name__ + ", Destroy")
		self.Logger.LogString("Destroy called")
		del self
	def Print(*args):
		debug(__name__ + ", Print")
		args[0].Logger.LogString("Print called, ARGS = "+str(args))

	# TGAction's methods:
	def GetSequence(*args):
		#val = apply(Appc.TGAction_GetSequence,args)
		#if val: val = TGSequencePtr(val) 
		#return val
		debug(__name__ + ", GetSequence")
		args[0].Logger.LogString("GetSequence called, ARGS = "+str(args))
	def IsPlaying(self):
		debug(__name__ + ", IsPlaying")
		self.Logger.LogString("IsPlaying called ("+str(self.Travel.Started)+")")
		return self.Travel.Started
	def ConstructDescription(*args):
		debug(__name__ + ", ConstructDescription")
		args[0].Logger.LogString("ConstructDescription called, ARGS = "+str(args))
	def SetupEditControls(*args):
		debug(__name__ + ", SetupEditControls")
		args[0].Logger.LogString("SetupEditControls called, ARGS = "+str(args))
	def ExtractControlValues(*args):
		debug(__name__ + ", ExtractControlValues")
		args[0].Logger.LogString("ExtractControlValues called, ARGS = "+str(args))
	def Restart(*args):
		debug(__name__ + ", Restart")
		args[0].Logger.LogString("Restart called, ARGS = "+str(args))
	def Abort(*args):
		debug(__name__ + ", Abort")
		args[0].Logger.LogString("Abort called, ARGS = "+str(args))
	def IsSkippable(*args):
		debug(__name__ + ", IsSkippable")
		args[0].Logger.LogString("IsSkippable called, ARGS = "+str(args))
	def SetSkippable(*args):
		debug(__name__ + ", SetSkippable")
		args[0].Logger.LogString("SetSkippable called, ARGS = "+str(args))
	def AddCompletedEvent(self, pEvent):
		debug(__name__ + ", AddCompletedEvent")
		self.Logger.LogString("AddCompletedEvent called, EVENT = "+str(pEvent))
		self.Travel.AddArrivedEvent(pEvent)
	def IsPartOfSequence(*args):
		debug(__name__ + ", IsPartOfSequence")
		args[0].Logger.LogString("IsPartOfSequence called, ARGS = "+str(args))
	def Completed(*args):
		debug(__name__ + ", Completed")
		args[0].Logger.LogString("Completed called, ARGS = "+str(args))
	def SetUseRealTime(*args):
		debug(__name__ + ", SetUseRealTime")
		args[0].Logger.LogString("SetUseRealTime called, ARGS = "+str(args))
	def IsUseRealTime(*args):
		debug(__name__ + ", IsUseRealTime")
		args[0].Logger.LogString("IsUseRealTime called, ARGS = "+str(args))
	def SetSurviveGlobalAbort(*args):
		debug(__name__ + ", SetSurviveGlobalAbort")
		args[0].Logger.LogString("SetSurviveGlobalAbort called, ARGS = "+str(args))
	def IsGlobalAbortSurvivor(*args):
		debug(__name__ + ", IsGlobalAbortSurvivor")
		args[0].Logger.LogString("IsGlobalAbortSurvivor called, ARGS = "+str(args))

	# TGSequence's methods:
	def GetAction(*args):
		#val = apply(Appc.TGSequence_GetAction,args)
		#if val: val = TGActionPtr(val) 
		#return val
		debug(__name__ + ", GetAction")
		args[0].Logger.LogString("GetAction called, ARGS = "+str(args))
	def AddAction(*args):
		debug(__name__ + ", AddAction")
		args[0].Logger.LogString("AddAction called, ARGS = "+str(args))
	def AppendAction(*args):
		debug(__name__ + ", AppendAction")
		args[0].Logger.LogString("AppendActions called, ARGS = "+str(args))
	def Play(self, sTravelType = ""):
		# sTravelType argument was added by me
		# ENGAGE TRAVEL
		debug(__name__ + ", Play")
		self.Logger.LogString("Play called")
		iRet = self.Travel.Travel(sTravelType)
		return iRet
	def GetNumActions(*args):
		debug(__name__ + ", GetNumActions")
		args[0].Logger.LogString("GetNumActions called, ARGS = "+str(args))

	# WarpSequence's methods:

	#def __del__(self):
	#	if self.thisown == 1 :
	#		Appc.delete_WarpSequence(self)
	def GetShip(self):
		debug(__name__ + ", GetShip")
		return self.Travel.Ship
	def GetOrigin(self):
		debug(__name__ + ", GetOrigin")
		return self.Travel.InitialShipSet
	def GetDestinationSet(self):
		debug(__name__ + ", GetDestinationSet")
		return self.Travel.DestSet
	def GetExitPoint(self):
		debug(__name__ + ", GetExitPoint")
		return self.Travel.GetExitLocationVector()
	def GetWarpSequencePiece(*args):
		#val = apply(Appc.WarpSequence_GetWarpSequencePiece,args)
		#if val: val = TGActionPtr(val) 
		#return val
		debug(__name__ + ", GetWarpSequencePiece")
		self.Logger.LogString("GetWarpSequencePiece called, ARGS = "+str(args))
	def Skip(*args):
		debug(__name__ + ", Skip")
		args[0].Logger.LogString("Skip called, ARGS = "+str(args))
	def AddActionBeforeWarp(*args):
		debug(__name__ + ", AddActionBeforeWarp")
		args[0].Logger.LogString("AddActionBeforeWarp called, ARGS = "+str(args))
	def AddActionDuringWarp(*args):
		debug(__name__ + ", AddActionDuringWarp")
		args[0].Logger.LogString("AddActionDuringWarp called, ARGS = "+str(args))
	def AddActionPostDuringWarp(*args):
		debug(__name__ + ", AddActionPostDuringWarp")
		args[0].Logger.LogString("AddActionPostDuringWarp called, ARGS = "+str(args))
	def AddActionAfterWarp(*args):
		debug(__name__ + ", AddActionAfterWarp")
		args[0].Logger.LogString("AddActionAfterWarp called, ARGS = "+str(args))
	def GetDestination(self):
		debug(__name__ + ", GetDestination")
		self.Logger.LogString("GetDestination called")
		return self.Travel.DestinationScript
	def GetTimeToWarp(self):
		debug(__name__ + ", GetTimeToWarp")
		self.Logger.LogString("GetTimeToWarp called")
		return self.Travel.TimeLeft
	def GetPlacementName(self):
		debug(__name__ + ", GetPlacementName")
		self.Logger.LogString("GetPlacementName called")
		return self.Travel.GetExitPlacementName()
	def GetDestinationMission(*args):
		debug(__name__ + ", GetDestinationMission")
		args[0].Logger.LogString("GetDestinationMission called, ARGS = "+str(args))
	def GetDestinationEpisode(*args):
		debug(__name__ + ", GetDestinationEpisode")
		args[0].Logger.LogString("GetDestinationEpisode called, ARGS = "+str(args))
	def SetExitPoint(self, vPos):
		debug(__name__ + ", SetExitPoint")
		self.Logger.LogString("SetExitPoint called, vPOS = "+str(vPos)+" // X = "+str(vPos.x)+" | Y = "+str(vPos.y)+" | Z = "+str(vPos.z))
		self.Travel.SetExitLocationVector(vPos)
	def SetPlacement(self, sPlacement):
		debug(__name__ + ", SetPlacement")
		self.Logger.LogString("SetPlacement called, PLACEMENT = "+str(sPlacement))
		self.Travel.SetExitPlacementName(sPlacement)
	def SetEventDestination(self, pDest):
		debug(__name__ + ", SetEventDestination")
		self.Logger.LogString("SetEventDestination called, DEST = "+str(pDest.GetName()))
		for pEvent in self.Travel.ArrivedEvents:
			pEvent.SetDestination(pDest)

	# additional methods by me.
	def PlayEngagingWarpSeq(self):
		debug(__name__ + ", PlayEngagingWarpSeq")
		if self.EngageWarpSeq != None:
			self.EngageWarpSeq.Play()
	def PlayDuringWarpSeq(self):
		debug(__name__ + ", PlayDuringWarpSeq")
		if self.DuringWarpSeq != None:
			self.DuringWarpSeq.Play()
	def PlayExitWarpSeq(self):
		debug(__name__ + ", PlayExitWarpSeq")
		if self.ExitWarpSeq != None:
			self.ExitWarpSeq.Play()
	def SetupSequence(self):
		debug(__name__ + ", SetupSequence")
		self.Logger.LogString("Setting sequence up...")
		# Nullify the sequences, if they exist... *beware, this might be wrong*
		self.EngageWarpSeq = None
		self.DuringWarpSeq = None
		self.ExitWarpSeq = None
		
		# and setup them (possibly again)
		lSeqList = [None, None, None]
		try:
			pFunc = App.g_kTravelManager.GetTravelTypeAttr(self.Travel.GetTravelType(), "SetupSequence")
			oRet = pFunc(self.Travel)
			if type(oRet) == type([]):
				if len(oRet) == 3:
					lSeqList = oRet
				else:
					self.Logger.LogError("Travel Type "+self.Travel.GetTravelType()+" SetupSequence method doesn't return 3-element list.")
			else:
				self.Logger.LogError("Travel Type "+self.Travel.GetTravelType()+" SetupSequence method returns a "+str(type(oRet))+", not a list.")
		except:
			self._LogError("SetupSequence")

		self.EngageWarpSeq = lSeqList[0]
		if self.EngageWarpSeq == None:
			self.EngageWarpSeq = App.TGSequence_Create()
		pEnWarpSeqEND = App.TGScriptAction_Create(__name__, "SequenceEnd", self)
		self.EngageWarpSeq.AppendAction(pEnWarpSeqEND)

		self.DuringWarpSeq = lSeqList[1]

		self.ExitWarpSeq = lSeqList[2]
		if self.ExitWarpSeq == None:
			self.ExitWarpSeq = App.TGSequence_Create()
		pExitWarpSeqEND = App.TGScriptAction_Create(__name__, "ExitSequenceEnd", self)
		self.ExitWarpSeq.AppendAction(pExitWarpSeqEND)

		self.Logger.LogString("Sequence was set up.")

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

##############################################################################################################
###########################################
# Custom Sequence Actions
###########################################
dBoostedShips = {}
def SequenceEnd(pAction, pWS):
	debug(__name__ + ", SequenceEnd")
	pTop = App.TopWindow_GetTopWindow()

	if pTop == None:
		return 0
	
	pShip = pWS.GetShip()
	
	# Finish travel...
	pWS.Travel.FinishTravel()

	# Un Hide the ship
	# Take care, if this is the ending for an AI ship travelling to None, i don't know if this unhide will work nicely
	pUnHideShip = App.TGScriptAction_Create(__name__, "HideShip", pShip.GetObjID(), 0)
	pUnHideShip.Play()

	pFinalCheckTowing = App.TGScriptAction_Create(__name__, "EngageSeqFinalTractorCheck", pWS)
	pFinalCheckTowing.Play()


	if pWS.Travel.IsPlayer == 1:
		# Drop out of cinematic view...
		pCinematicStop = App.TGScriptAction_Create("Actions.CameraScriptActions", "StopCinematicMode")
		pCinematicStop.Play()

		# Ensure that we're in interactive mode.
		pCinematic = App.CinematicWindow_Cast(pTop.FindMainWindow(App.MWT_CINEMATIC))
		if pCinematic != None:
			pCinematic.SetInteractive(1)

		pAllowInput = App.TGScriptAction_Create("MissionLib", "ReturnControl")
		pAllowInput.Play()

	return 0

def ExitSequenceEnd(pAction, pWS):
	debug(__name__ + ", ExitSequenceEnd")
	pTop = App.TopWindow_GetTopWindow()

	if pTop == None:
		return 0

	pWS.Travel.SeqStat = pWS.Travel.NOT_ENGAGING
	pWS.Travel.StopTowing()

	if pWS.Travel.IsPlayer == 1:
		# Drop out of cinematic view...
		pCinematicStop = App.TGScriptAction_Create("Actions.CameraScriptActions", "StopCinematicMode")
		pCinematicStop.Play()

		# Ensure that we're in interactive mode.
		pCinematic = App.CinematicWindow_Cast(pTop.FindMainWindow(App.MWT_CINEMATIC))
		if pCinematic != None:
			pCinematic.SetInteractive(1)

		pAllowInput = App.TGScriptAction_Create("MissionLib", "ReturnControl")
		pAllowInput.Play()
	else:
		# so a AI ship just finished her exiting warp sequence. we should reset her AI then
		# this will fix a freakking bug in the follow target thru warp AI...
		# That frikkin AI bug or didn't let a ship battle while warping or made her completely stop after warping...
		pShip = pWS.GetShip()
		if GalacticWarSimulator.WarSimulator.IsInitialized() == 1 and GalacticWarSimulator.FleetManager.GetFleetOfShip(pShip) != None:
			GalaxyLIB.ResetShipAI(pShip)
		elif pShip.GetAI() != None:
			pShip.GetAI().Reset()
	return 0


# bBoost 1 is to start boost
# bBoost 2 is to maintain boosting
# bBoost 0 is to end boost and revert back to original speed
# bBoost -1 is to directly stop the ship, ending boost.  This will not revert back to original speed.
def BoostShipSpeed(pAction, ShipID, bBoost, fBoostScale = 100.0, vDirection = None):
	debug(__name__ + ", BoostShipSpeed")
	global dBoostedShips
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), ShipID)
	if pShip:
		if bBoost == 1:
			vOldVelocity = pShip.GetVelocityTG()
			dBoostedShips[ShipID] = vOldVelocity
			if vDirection == None:
				vVelocity = pShip.GetWorldForwardTG()
			else:
				vVelocity = App.TGPoint3()
				vVelocity.Set(vDirection)
			vVelocity.Scale(fBoostScale)
			pShip.SetVelocity(vVelocity)
		elif bBoost == 2:
			if dBoostedShips.has_key(ShipID):
				if vDirection == None:
					vVelocity = pShip.GetWorldForwardTG()
				else:
					vVelocity = App.TGPoint3()
					vVelocity.Set(vDirection)
				vVelocity.Scale(fBoostScale)
				pShip.SetVelocity(vVelocity)
		elif bBoost == 0:
			if dBoostedShips.has_key(ShipID):
				vVelocity = dBoostedShips[ShipID]
				pShip.SetVelocity(vVelocity)
				#del dBoostedShips[ShipID]
		elif bBoost == -1:
			if dBoostedShips.has_key(ShipID):
				vVelocity = App.TGPoint3()
				vVelocity.SetXYZ(0,0,0)
				pShip.SetVelocity(vVelocity)
				del dBoostedShips[ShipID]
	return 0

def HideShip(pAction, ShipID, bHide):
	debug(__name__ + ", HideShip")
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), ShipID)
	if pShip:
		pShip.SetHidden(bHide)
	return 0

def PlayWarpSound(pAction, pWS, sType, sRace):
	debug(__name__ + ", PlayWarpSound")
	pShip = pWS.GetShip()
	pPlayer = App.Game_GetCurrentPlayer()
	if pShip == None or pPlayer == None:
		return 0

	pSet = pShip.GetContainingSet()
	pPlaSet = pPlayer.GetContainingSet()
	if pSet == None or pPlaSet == None:
		return 0

	if pSet.GetRegionModule() == pPlaSet.GetRegionModule():
		try:
			import Custom.NanoFXv2.WarpFX.WarpFX
			if sRace == "":
				sRace = "Default"
			if sType == "Enter Warp":
				sType = "EnterWarp"
			elif sType == "Exit Warp":
				sType = "ExitWarp"
			else:
				sType = ""
			if sType != "":
				sFile = "scripts\\Custom\\NanoFXv2\\WarpFX\\Sfx\\"+sRace+"\\"+sRace+sType+".wav"
				Custom.GravityFX.GravityFXlib.PlaySound(sFile, sRace+" "+sType+" Sound")
		except:
			if sType == "Enter Warp":
				Custom.GravityFX.GravityFXlib.PlaySound("sfx\\enter warp.wav", "Default Enter Warp Sound")
			elif sType == "Exit Warp":
				Custom.GravityFX.GravityFXlib.PlaySound("sfx\\exit warp.wav", "Default Exit Warp Sound")
	return 0

def EngageSeqTractorCheck(pAction, pWS):
	debug(__name__ + ", EngageSeqTractorCheck")
	if pWS.Travel.bTractorStat == 1 and pWS.Travel.Towee != None:
		# hide the towee
		pHideTowee = App.TGScriptAction_Create(__name__, "HideShip", pWS.Travel.Towee.GetObjID(), 1)
		pHideTowee.Play()
		# and then shut down the tractors. you don't wanna see a tractor beam going out of nowhere grabbing a ship
		pTractors = pWS.Travel.Ship.GetTractorBeamSystem()
		# I know that for this part to happen the ship that is travelling has to have an tractor beam system,
		# still, knowing BC like I do, it's best to do this check again, to be sure and prevent any problems.
		if pTractors != None:
			pTractors.StopFiring()
		vZero = App.TGPoint3()
		vZero.SetXYZ(0,0,0)
		pWS.Travel.Towee.SetVelocity(vZero)
		pWS.Travel.Towee.SetAcceleration(vZero)
		pWS.Travel.Towee.UpdateNodeOnly()
	return 0

def EngageSeqFinalTractorCheck(pAction, pWS):
	debug(__name__ + ", EngageSeqFinalTractorCheck")
	if pWS.Travel.bTractorStat == 1 and pWS.Travel.Towee != None:
		# Un hide the towee
		pUnHideTowee = App.TGScriptAction_Create(__name__, "HideShip", pWS.Travel.Towee.GetObjID(), 0)
		pUnHideTowee.Play()
		# and then turn the tractor on again. the Travel class can do that for us.
		pWS.Travel.MaintainTowing()
	return 0

def MaintainTowingAction(pAction, pWS):
	debug(__name__ + ", MaintainTowingAction")
	if pWS.Travel.bTractorStat == 1 and pWS.Travel.Towee != None:
		pWS.Travel.MaintainTowing()
	return 0

def NoAction(pAction):
	debug(__name__ + ", NoAction")
	return 0

###############################################################################
#	CheckWarpInPath     (taken and modified from WarpSequence)
#	
#	Check the path that this ship is going to be warping in along.
#	If it's not clear of obstacles, change it.
#	
#	Args:	pAction			- The TGScriptAction calling us.
#			pWarpSequence	- The warp sequence controlling the script action
#							  (and controlling the ship)
#			idShip			- The ship that's warping.
#	
#	Return:	0
###############################################################################
def CheckWarpInPath(pAction, pWarpSequence, idShip):
	# The original function "didn't worry about multiplayer".... So we'll just do the same...
	debug(__name__ + ", CheckWarpInPath")
	if App.g_kUtopiaModule.IsMultiplayer():
		return 0

	# Get various things we'll need...
	try:
		pShip = App.ShipClass_GetObjectByID(None, idShip)
		pSet = pShip.GetContainingSet()     #pWarpSequence.GetDestinationSet()
		if not pSet:
			return 0
		pWarpEngines = pShip.GetWarpEngineSubsystem()

		vStart = App.TGPoint3()
		vStart.Set(pWarpEngines.GetWarpExitLocation())
		pEndPlacement = App.PlacementObject_GetObject(pSet, pWarpSequence.GetPlacementName())
		vEnd = pEndPlacement.GetWorldLocation()
		fShipRadius = pShip.GetRadius()
	except AttributeError:
		return 0

	# Search through all ships warping in the set right now...
	lpShips = []
	for pSetShip in pSet.GetClassObjectList( App.CT_SHIP ):
		pWarpSystem = None
		try:
			pWarpSys = pSetShip.GetWarpEngineSubsystem()
			pShipTravel = App.g_kTravelManager.GetTravel(pSetShip)
			if pShipTravel.SeqStat != pShipTravel.NOT_ENGAGING:
				# Make sure this is the set it's arriving at, not the set it's departing.
				pWS = App.WarpSequence_Cast( pWarpSys.GetWarpSequence() )
				pDestinationSet = pWS.GetDestinationSet()
				if pDestinationSet and pDestinationSet.GetObjID() == pSet.GetObjID():
					# This ship is warping into this set.  Add it's warp system as well...
					pWarpSystem = pWarpSys
		except AttributeError:
			# No warp engine subsystem.  That's ok.
			pass
		lpShips.append((pSetShip, pWarpSystem))

	# Check the path that that these ships are warping in along...
	iIndex = 0
	fRandomMax = 15.0
	bChanged = 0
	while iIndex < len(lpShips):
		pWarpingShip, pWarpingSubsystem = lpShips[iIndex]
		iIndex = iIndex + 1

		bCalculateWarpEnd = 0
		pWarpingTravel = App.g_kTravelManager.GetTravel(pWarpingShip)
		if pWarpingTravel != None:
			vWarpStart = App.TGPoint3()
			vWarpStart.Set(pWarpingTravel.GetExitLocationVector())
			pEndPlacement = pWarpingTravel.GetExitPlacement()

			if pEndPlacement:
				vWarpEnd = pEndPlacement.GetWorldLocation()
			else:
				bCalculateWarpEnd = 1
		else:
			# If the ship's not warping, we still don't want to warp in near it.
			vWarpStart = pWarpingShip.GetWorldLocation()
			bCalculateWarpEnd = 1
		if bCalculateWarpEnd == 1:
			vWarpEnd = App.TGPoint3()	
			vWarpEnd.Set(vWarpStart)
			vEndPlus = pWarpingShip.GetVelocityTG()
			if vEndPlus.x == 0 and vEndPlus.y == 0 and vEndPlus.z == 0:
				vEndPlus = pWarpingShip.GetWorldForwardTG()
			vEndPlus.Scale(3.0)
			vWarpEnd.Add(vEndPlus)

		# If our line is ever too close to their line, adjust our line.
		# Find the distance between the two line segments...
		vClosestStart, vClosestEnd = WarpSequence.FindSegmentBetweenSegments( vStart, vEnd, vWarpStart, vWarpEnd )
		vDiff = App.TGPoint3()
		vDiff.Set(vClosestEnd)
		vDiff.Subtract( vClosestStart )
		fDistance = vDiff.Unitize()

		# Just in case...
		if fDistance == 0:
			vDiff.SetXYZ(1.0, 0, 0)

		# Got the distance.  Are we too close?
		if fDistance < (fShipRadius * 4.0):
			# Yeah, it's probably too close.  Push our line away.  Far away...
			bChanged = 1
			vDiff.Scale( fShipRadius * (App.g_kSystemWrapper.GetRandomNumber(fRandomMax) + 2.0) )
			vStart.Add(vDiff)
			vEnd.Add(vDiff)
			# And reset our checks, so we check from the beginning again.
			iIndex = 0
			# And bump up the random max, in case we keep looping...  We'll eventually break out.
			fRandomMax = fRandomMax + 8.0

	if bChanged:
		# Our warp-in point has changed.  We need to make a new placement to warp into,
		# at the new location.
		iAttempt = 0
		while 1:
			sPlacement = "WarpAdjusted %d" % iAttempt
			if not App.PlacementObject_GetObject(pSet, sPlacement):
				break
			iAttempt = iAttempt + 1

		pPlacement = App.PlacementObject_Create(sPlacement, pSet.GetName(), None)

		pPlacement.SetTranslate(vEnd)
		pPlacement.UpdateNodeOnly()

		pWarpSequence.SetExitPoint(vStart)
		pWarpSequence.SetPlacement(sPlacement)
	return 0
