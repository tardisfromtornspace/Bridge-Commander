from bcdebug import debug
###############################################################################################################
#   TravelerAI_Override.py                 by Fernando Aluani
############
#  This script contains the overrides for BC's Warp and FollowThroughWarp PlainAIs, to make them use the 
#  GalaxyChart's Traveler travel system, instead of BC's out-dated warp system.
#  Plus it also contains the stuff to make in-system Warp Intercept a reality
###############################################################################################################
import App
import AI.PlainAI.BaseAI
import Traveler
import GalaxyLIB
import MissionLib
import Bridge.HelmMenuHandlers

ET_AI_EXITED_WARP = App.UtopiaModule_GetNextEventType()

##########################
import Custom.GravityFX.Logger
if GalaxyLIB.GetConfigValue("LogTravelerAI") == 1:
	Logger = Custom.GravityFX.Logger.LogCreator("Galaxy WarpAI Logger", "scripts\Custom\GalaxyCharts\Logs\TravelerAI_LOG.txt")
	Logger.LogString("Initialized Galaxy WarpAI logger")
else:
	Logger = Custom.GravityFX.Logger.DummyLogger()
##########################

#
# Warp           PlainAI
#
# Warp immediately.  If a set is specified, warp to the specified set.
# If no set is specified, the ship just warps out and disappears, never
# to be seen again.  The ship will be deleted.
# If the set is invalid (the name doesn't correspond to any existing
# set), this will treat it the same as if no set were specified.
# If a placement is specified, warp in so we land on that placement in
# the new set.
# If no placement is specified, warp in and land on the default warp
# entry placement for that set.
#
#  This AI module had to be modified, as there are some cases that her alone is used.
#  Plus, it didn't gave much problem...
#
class TravelerWarp(AI.PlainAI.BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		debug(__name__ + ", __init__")
		global Logger
		# Base class init, first..
		AI.PlainAI.BaseAI.BaseAI.__init__(self, pCodeAI)
		Logger.LogString("Initializing a TravelerWarp instance")
		# Set default values for parameters that have them.
		self.SetupDefaultParams(
			self.SetDestinationSetName,
			self.SetDestinationPlacementName,
			self.SetWarpDuration,
			self.SetWarpSpeed,
			self.WarpBlindly,
			self.WarpBlindlyNoCollisionsIfImpulseDisabled,
			self.EnableTowingThroughWarp)
		self.SetRequiredParams()
		self.SetExternalFunctions()

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# We need an event handler...
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		self.pEventHandler.AddPythonMethodHandlerForInstance( ET_AI_EXITED_WARP, "WarpDone" )

		# Initialize variables...
		self.bWarping = 0
		self.bCollisionsDisabled = 0
		self.eUpdateReturn = App.ArtificialIntelligence.US_ACTIVE
		self.pWarpSequence = None

		self.vTowPosition = None
		self.idTowObject = App.NULL_ID
		self.idTowTimer = App.NULL_ID

		self.vBetterDirection = None
		self.fDirectionTimeThreshold = 0.2



	# Name of the set we're going to.
	def SetDestinationSetName(self, sSetName = None): #AISetup
		self.sToSetName = sSetName

	def SetDestinationPlacementName(self, sPlacementName = None): #AISetup
		self.sPlacementName = sPlacementName

	def SetWarpDuration(self, fTime = 3.0): #AISetup
		self.fWarpTime = fTime

	def SetWarpSpeed(self, fWarpFactor = None): #AISetup
		self.fWarpFactor = fWarpFactor

	def WarpBlindly(self, bWarpImmediately = 0): #AISetup
		self.bWarpImmediately = bWarpImmediately

	def WarpBlindlyNoCollisionsIfImpulseDisabled(self, bWarpBlindly = 0): #AISetup
		self.bWarpBlindlyIfNoImpulse = bWarpBlindly

	def EnableTowingThroughWarp(self, bTowThroughWarp = 0): # NOT an AISetup function.  Add it by hand.
		self.bEnableTowing = bTowThroughWarp

	# To force Warp to use this WarpSequence, rather than
	# creating its own.  This is not normally accessible to
	# the AI Editor, but it is used by the game.
	def SetSequence(self, pWarpSequence):
		debug(__name__ + ", SetSequence")
		self.pWarpSequence = pWarpSequence

		# Need to add an action to the end of the warp
		# sequence to call our WarpDone member, since
		# this probably won't send the event to the right place.
	#	pWarpDoneAction = App.TGScriptAction_Create(__name__, "WarpDoneAction", self.pCodeAI.GetID())
	#	self.pWarpSequence.AddActionAfterWarp(pWarpDoneAction, 0)




	def Reset(self):
		# Reset any state info
		debug(__name__ + ", Reset")
		self.bWarping = 0

	def LostFocus(self):
		# If we were towing, stop towing.
		#self.StopTowing(self.pCodeAI.GetShip())
		# If we'd disabled collisions for our ship, reenable them.
		debug(__name__ + ", LostFocus")
		if self.bCollisionsDisabled:
			pShip = self.pCodeAI.GetShip()
			if pShip:
				pShip.SetCollisionsOn(1)
			self.bCollisionsDisabled = 0


	def GetStatusInfo(self):
		debug(__name__ + ", GetStatusInfo")
		return "Destination(%s), Placement(%s), Duration(%f), Blind(%d), BlindIfDisabledImpulse(%d)%s" % (
			self.sToSetName,
			self.sPlacementName,
			self.fWarpTime,
			self.bWarpImmediately,
			self.bWarpBlindlyIfNoImpulse,
			("", ", Towing")[self.bEnableTowing])

	def GetNextUpdateTime(self):
		# We want to be updated every 1.0 seconds (+/- 0.2)
		debug(__name__ + ", GetNextUpdateTime")
		fRandomFraction = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
		return 1.0 + (fRandomFraction * 0.2)

	def Update(self):
		debug(__name__ + ", Update")
		"Do our stuff"
		# Default return is Done.
		eRet = App.ArtificialIntelligence.US_DONE

		pShip = self.pCodeAI.GetShip()
		if (pShip == None):
			# ***FIXME: For now, this AI only works on ShipClass
			# and below...
			return App.ArtificialIntelligence.US_DONE

		# Check power of engines.
		pEngines = pShip.GetImpulseEngineSubsystem()
		if pEngines:
			# If no power, then at least give enough to get going.
			if pEngines.GetPowerPercentageWanted() <= 0.0:
				pEngines.SetPowerPercentageWanted(1.0)
				pEngines.TurnOn()

		pWarp = pShip.GetWarpEngineSubsystem()
		if pWarp and (pWarp.GetPowerPercentageWanted() <= 0.0):
			pWarp.SetPowerPercentageWanted(1.0)
			pWarp.TurnOn()
		
		###########
		## USS Frontier addition
		pShipTravel = App.g_kTravelManager.GetTravel(pShip)
		if pShipTravel and pShipTravel.Started == 1:
			Logger.LogString(pShip.GetName()+" is already warping...")
			return App.ArtificialIntelligence.US_DONE
		if Traveler.Travel.TravelIntercept == 0:
			Logger.LogString(pShip.GetName()+" is not capable of warping.")
			return App.ArtificialIntelligence.US_ACTIVE    # this return state may be wrong...
		###########

		# Set our speed to 0.
		pShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)
		
		# Set our turning to 0.
		vZero = App.TGPoint3()
		vZero.SetXYZ(0, 0, 0)
		pShip.SetTargetAngularVelocityDirect( vZero )

		# If we haven't started the warp sequence yet, start it:
		if self.bWarping == 0:
			# Should we warp immediately, or aim for a good
			# direction first?
			bWarpImmediately = self.bWarpImmediately
			if self.bWarpBlindlyIfNoImpulse:
				# Check the state of our ship's impulse engines.  If they're disabled,
				# we want to warp immediately, without searching for a good direction.
				pImpulse = pShip.GetImpulseEngineSubsystem()
				if (not pImpulse)  or  (pImpulse.IsDisabled()):
					bWarpImmediately = 1

					# And disable collisions for this object...
					self.bCollisionsDisabled = 1
					pShip.SetCollisionsOn(0)

			if not bWarpImmediately:
				# Aim for a good direction.
				if not self.AimForGoodDirection(pShip):
					# Not yet facing a good direction.
					Logger.LogString(pShip.GetName()+" is not yet facing a good direction to travel.")
					return App.ArtificialIntelligence.US_ACTIVE

			# Setup the warp sequence.  *USS Frontier - Removed this to put Traveler in good use
			if self.pWarpSequence == None:
				pWarpSeq = App.WarpSequence_Create(pShip, self.sToSetName, self.fWarpTime, self.sPlacementName)
			
				# Set the warp sequence to send us an event when
				# it's done (as long as we still exist).
			#	pEvent = App.TGEvent_Create()
			#	pEvent.SetEventType( ET_AI_EXITED_WARP )
			#	pEvent.SetDestination( self.pEventHandler )
			#	pWarpSeq.AddCompletedEvent(pEvent)
			
			#	pWarpSeq.SetEventDestination( pShip )
			else:
				pWarpSeq = self.pWarpSequence
				self.pWarpSequence = None
				Logger.LogString(str(pShip.GetName())+"  TravelerAI obj had her WarpSequence obj set up from outside.")

			try:
				pThisTravel = pWarpSeq.Travel
			except:
				LogError("TravelerAI Update of ship "+str(pShip.GetName())+" ("+str(pShip.GetObjID())+"): Couldn't acquire Travel obj from WarpSeq")
				pThisTravel = None

			# If we're towing a ship, save the info we need to do that.
			if pThisTravel != None:
				pWarpSeq.Travel.SetEnableTowing( self.bEnableTowing)

			# Before playing the sequence, and thus, warp, set the ship's warp speed.
			if pThisTravel != None:
				if self.fWarpFactor == None:
					self.fWarpFactor = pWarpSeq.Travel.GetActualCruiseSpeed()
				pWarpSeq.Travel.SetSpeed(self.fWarpFactor)

			# Play the sequence. *USS Frontier - Also removed to use Traveler instead
			pWarpSeq.Play()

			########################
			Logger.LogString(str(pShip.GetName())+" is engaging warp to set: "+str(self.sToSetName))
			########################

			# Set the bWarping flag, so we know we're warping now.
			self.bWarping = 1

			# Let the game know we're active.
			eRet = self.eUpdateReturn = App.ArtificialIntelligence.US_DONE
		else:
			# We've already started warping.  Just return
			# whatever our state is..  The event handler for
			# when we come out of warp will set this to Done.
			#debug("Warping, warping...")
			#self.WarpDone(None)
			eRet = self.eUpdateReturn

		return eRet

	def WarpDone(self, pEvent):
		debug(__name__ + ", WarpDone")
		"Our warp sequence has finished."
		# Next time we're updated, we can say we're done.
		Logger.LogString(self.pCodeAI.GetShip().GetName()+" is done warping.")
		self.eUpdateReturn = App.ArtificialIntelligence.US_DONE

	def AimForGoodDirection(self, pShip):
		# Get all the objects along the line that we'll
		# be warping through.
		debug(__name__ + ", AimForGoodDirection")
		fRayLength = 4000.0
		vOrigin = pShip.GetWorldLocation()
		vEnd = pShip.GetWorldForwardTG()
		vEnd.Scale(fRayLength)
		vEnd.Add(vOrigin)

		lsObstacles = self.GrabObstacles(vOrigin, vEnd, pShip)
		# If we have no obstacles in the way, we're good.
		if len(lsObstacles) == 0:
			vZero = App.TGPoint3()
			vZero.SetXYZ(0, 0, 0)
			pShip.SetTargetAngularVelocityDirect(vZero)
			return 1

		# We've got obstacles in the way.
		if not self.vBetterDirection:
			# Cast a few rays
			# and try to find a good direction to go.  If we don't
			# find a good direction, that's ok; we'll try again
			# next frame.
			for iRayCount in range(8):
				vRay = App.TGPoint3_GetRandomUnitVector()

				# Bias it toward our Forward direction.
				vRay.Scale(1.5)
				vRay.Add(pShip.GetWorldForwardTG())

				vRay.Unitize()

				vEnd = App.TGPoint3()
				vEnd.Set(vRay)
				vEnd.Scale(fRayLength)

				vEnd.Add(vOrigin)
				lsObstacles = self.GrabObstacles(vOrigin, vEnd, pShip)
				if not lsObstacles:
					# Found a good direction.
					self.vBetterDirection = vRay
					break

		if self.vBetterDirection:
			#debug("Aiming for better direction.")
			fTime = pShip.TurnTowardDirection(self.vBetterDirection)
			if fTime < self.fDirectionTimeThreshold:
				# We're almost facing it, and still
				# no good.  Toss out this direction
				# so we try again next frame.
				self.vBetterDirection = None
#		else:
#			debug("Can't find a good direction...")
		return 0

	def GrabObstacles(self, vStart, vEnd, pShip):
		debug(__name__ + ", GrabObstacles")
		import MissionLib
		return MissionLib.GrabWarpObstaclesFromSet(vStart, vEnd, pShip.GetContainingSet(), pShip.GetRadius(), 1, pShip.GetObjID())



###################################################################################################3
#
# FollowThroughWarp           PlainAI
#
# Follow a given object between sets.  If at any time the other
# object moves to a different set, our object will warp after it.
# When we warp to a new set, this creates a temporary placement
# near the object we're following, so we warp into a good position.
#
#  This AI however, was mostly overrided for safety purposes.
#  As long as I noticed, the Compound AI with the same name is used mostly to give AIs the follow through warp
#  behavior.
#
class TravelerFollowThroughWarp(TravelerWarp):
	def __init__(self, pCodeAI):
		# Base class init, first..
		debug(__name__ + ", __init__")
		global Logger
		TravelerWarp.__init__(self, pCodeAI)
		Logger.LogString("Initializing a Traveler FollowThroughWarp instance")
		# Set default values for parameters that have them.
		self.SetupDefaultParams()
		self.SetRequiredParams(
			( "sObjectName", "SetFollowObjectName" ) )
		self.SetExternalFunctions(
			( "SetTarget", "SetFollowObjectName" ) )

		# Override the default warp duration.
		self.SetWarpDuration(13.0)

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		self.fWarpInBackDistance = 40.0
		self.fWarpInPerpendicularDistance = 15.0

		# USS Frontier Addition:
		self.sTargetDestinationScript = None

	def SetFollowObjectName(self, sName): #AISetup
		# Set the name of the object we're following...
		self.sObjectName = sName
		pShip = self.pCodeAI.GetShip()
		pTarget =  App.ShipClass_Cast(App.ObjectClass_GetObject(None, self.sObjectName))
		if pShip == None:
			debug(__name__ + ", SetFollowObjectName")
			pChaser = App.g_kTravelManager.GetTravel(pShip)
			if pChaser != None:
				pChaser.SetTarget(pTarget)

	def GetStatusInfo(self):
		debug(__name__ + ", GetStatusInfo")
		return "Target(%s)" % self.sObjectName

	def GetNextUpdateTime(self):
		# We want to be updated every 10.0 seconds (+/- 2.0)
		debug(__name__ + ", GetNextUpdateTime")
		fRandomFraction = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
		return 10.0 + (fRandomFraction * 2.0)

	def WarpDone(self, pEvent):
		debug(__name__ + ", WarpDone")
		"Our warp sequence has finished."
		# Next time we're updated, we can say we're done.
		Logger.LogString(self.pCodeAI.GetShip().GetName()+" is done warping.")
		self.eUpdateReturn = App.ArtificialIntelligence.US_DORMANT  #used to be DONE
		pShip = self.pCodeAI.GetShip()
		if pShip == None:
			pChaser = App.g_kTravelManager.GetTravel(pShip)
			if pChaser != None:
				pChaser.SetTarget(None)

	def Update(self):
		debug(__name__ + ", Update")
		"Do our stuff"
		# Now with the Traveler system and the Chaser class there is no need to keep running Update
		# so we start the Chaser, and return DONE, that's it.

		pShip = self.pCodeAI.GetShip()
		pObject = App.ObjectClass_GetObject(None, self.sObjectName)
		if not pObject:
			return App.ArtificialIntelligence.US_DONE
		pTarget = App.ShipClass_Cast(pObject)
		pObject = None

		if pShip == None or pTarget == None:
			# ***FIXME: For now, this AI only works on ShipClass
			# and below...
			return App.ArtificialIntelligence.US_DONE

		# Are we in the same set as our target?
		bNeedToWarp = 1
		pSet = pShip.GetContainingSet()
		pTargetSet = pTarget.GetContainingSet()
		if pSet != None and pTargetSet != None:
			if pSet.GetRegionModule() == pTargetSet.GetRegionModule():
				# We're in the same set.  We don't need to warp.
				bNeedToWarp = 0

		pChaser = App.g_kTravelManager.CreateChaser(pShip, pTarget)

		pEvent = None
		for pExEvent in pChaser.ArrivedEvents:
			try:
				if pExEvent.GetEventType() == ET_AI_EXITED_WARP:
					pEvent = pExEvent
					break
			except:
				# errors in AI scripts can get REALLY nasty, so it's best to do this operation in a try statement
				pass
		if pEvent == None:
			pEvent = App.TGEvent_Create()
			pEvent.SetEventType( ET_AI_EXITED_WARP )
			pEvent.SetDestination( self.pEventHandler )
			pChaser.AddArrivedEvent(pEvent)

		pChaser.SetTarget(pTarget)

		return App.ArtificialIntelligence.US_DONE

	#############
	# the following methods were still left here because a external script still might want to use them...
	def SetupWarpParameters(self, pShip):
		debug(__name__ + ", SetupWarpParameters")
		pass

	def HandleTravelParametersCheck(self, pShip):
		debug(__name__ + ", HandleTravelParametersCheck")
		pass

	def SafeDirection(self, vPosition, vForward, fRadius):
		debug(__name__ + ", SafeDirection")
		pass


###############################################################################################
##
##        CompoundAI  FollowThroughWarp Override
##
######
##  yes, strange... But this won't use PlainAI with the same name.
##  to avoid some problems with this freaking AI, the Traveler system will handle the follow thru warp behavior
##  this will simply start a Chaser, and pass in the necessary information.
def CreateAI(pShip, sTarget, bWarpBlindly = 0, **dKeywords):
	debug(__name__ + ", CreateAI")
	if dKeywords.has_key("Keywords"):
		dKeywords = dKeywords["Keywords"]

	if not dKeywords.has_key("FollowToSB12"):
		# Default value should be true.
		dKeywords["FollowToSB12"] = 1
	if not dKeywords.has_key("FollowThroughMissions"):
		# Default value should be false.
		dKeywords["FollowThroughMissions"] = 0

	if not dKeywords.has_key("FollowTargetThroughWarp"):
		dKeywords["FollowTargetThroughWarp"] = 1

	pTarget = App.ShipClass_Cast(App.ObjectClass_GetObject(None, sTarget))
	if pShip != None and pTarget != None:
		pChaser = App.g_kTravelManager.CreateChaser(pShip, pTarget)
		pChaser.SetTarget( pTarget )
		pChaser.SetCanChaseTarget( dKeywords["FollowTargetThroughWarp"] )
		pChaser.SetTravelBlindly( bWarpBlindly )

	# check if a ship should follow if target is warping to, or in Starbase 12
	# check if a ship should follow if target is warping to mission

	# we return a simple, kinda usefull AI since she'll have a special condition that won't work as a condition and will
	# instead update our Chaser. 
	# Plus, if we didn't return any AI at all, the BC engine wouldn't like >_<

	#########################################
	# Creating ConditionalAI UpdateChaser at (76, 184)
	## Conditions:
	#### Condition Disabled
	pUpdating = App.ConditionScript_Create(__name__, "ConditionUpdateChaser", pShip.GetName(), sTarget)
	## Evaluation function:
	def EvalFunc(bUpdating):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bUpdating:
			return DORMANT
		return DORMANT
	## The ConditionalAI:
	pUpdateChaser = App.ConditionalAI_Create(pShip, "UpdateChaser")
	pUpdateChaser.SetInterruptable(1)
	# as we here don't have a AI to be contained, comment this line out. Hopefully it won't give problems.
	#pUpdateChaser.SetContainedAI(pStay)    
	pUpdateChaser.AddCondition(pUpdating)
	pUpdateChaser.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI UpdateChaser 
	#########################################
	#########################################
	# Creating SequenceAI FollowThroughWarpSequence at (126, 260)
	pFollowThroughWarpSequence = App.SequenceAI_Create(pShip, "FollowThroughWarpSequence")
	pFollowThroughWarpSequence.SetInterruptable(1)
	pFollowThroughWarpSequence.SetLoopCount(-1)
	pFollowThroughWarpSequence.SetResetIfInterrupted(1)
	pFollowThroughWarpSequence.SetDoubleCheckAllDone(1)
	pFollowThroughWarpSequence.SetSkipDormant(1)
	# SeqBlock is at (236, 267)
	pFollowThroughWarpSequence.AddAI(pUpdateChaser)
	# Done creating SequenceAI FollowThroughWarpSequence
	#########################################
	return pFollowThroughWarpSequence

################################################################################################
##
##        Condition (AI)  ConditionUpdateChaser
##
######
##  also strange i think... but yes, this is a condition used in Conditional AIs.
##  however, this one in particular won't have a purpose to be used in 'correct' AIs, because the only thing she'll do is
##  update the Chaser of her parent ship, and that's it. Nothing else. She won't even bother returning that the condition
##  is true, because trully, there isn't a condition. I merely want to abuse the AI system, since it's the best thing
##  in my opinion (considering the situation) to properly update the Chaser with the new ship's Target. =P
##  And then this will be used in the above CompoundAI FollowThroughWarp.
######
class ConditionUpdateChaser:
	def __init__(self, pCodeCondition, sShipName, sObjectName):
		debug(__name__ + ", __init__")
		self.pCodeCondition = pCodeCondition
		# Set our primary object's name..
		self.sObjectName = sObjectName
		self.sShipName = sShipName

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# Setup our interrupt handlers, for checking of the object
		# enters the set.
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)

		self.pEventHandler.AddPythonMethodHandlerForInstance( App.ET_ENTERED_SET, "EnteredSet" )
		self.SetState()

	def RegisterExternalFunctions(self, pAI):
		debug(__name__ + ", RegisterExternalFunctions")
		pAI.RegisterExternalFunction("SetTarget", { "CodeID" : self.pCodeCondition.GetObjID(), "FunctionName" : "SetTarget" })

	def SetTarget(self, sTarget):
		# Target changed
		debug(__name__ + ", SetTarget")
		self.sObjectName = sTarget
		self.SetState()

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		dState["pEventHandler"].pContainingInstance = self
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)
		del self.pEventHandler.pContainingInstance

	def SetState(self):
		debug(__name__ + ", SetState")
		if self.sShipName != "":
			pObj = App.ObjectClass_GetObject( None, self.sShipName )
		else:
			pObj = None
		pTargObj = App.ObjectClass_GetObject( None, self.sObjectName)

		pShip = None
		pTarget = None
		if pObj != None and pTargObj != None:
			pShip = App.ShipClass_Cast(pObj)
			pTarget = App.ShipClass_Cast(pTargObj)

		if pShip != None and pTarget != None:
			pChaser = App.g_kTravelManager.CreateChaser(pShip, pTarget)
			if pChaser.Target == None:
				pChaser.SetTarget(pTarget)
			elif pChaser.Target.GetObjID() != pTarget.GetObjID():
				pChaser.SetTarget(pTarget)

		bStatus = 0
		self.pCodeCondition.SetStatus(bStatus)

	def EnteredSet(self, pObjEvent):
		# update state
		debug(__name__ + ", EnteredSet")
		self.SetState()
		# Call the next handler for this event...
		self.pEventHandler.CallNextHandler(pObjEvent)


##########################################################################################################
#  The following 3 methods are overrides for the App.ShipClass method of same name
# these are overriden in the LoadGalaxyCharts script
###
def ShipClass_InSystemWarp(self, pTarget, fStopDistance):
	debug(__name__ + ", ShipClass_InSystemWarp")
	pTravel = App.g_kTravelManager.CreateTravel(self)
	if pTravel != None:
		return pTravel.TravelIntercept(pTarget, fStopDistance)
	return 0

def ShipClass_StopInSystemWarp(self):
	debug(__name__ + ", ShipClass_StopInSystemWarp")
	pTravel = App.g_kTravelManager.GetTravel(self)
	if pTravel != None:
		return pTravel.StopIntercept()
	return 0

def ShipClass_IsDoingInSystemWarp(self):
	debug(__name__ + ", ShipClass_IsDoingInSystemWarp")
	pTravel = App.g_kTravelManager.GetTravel(self)	
	if pTravel != None:
		if pTravel.IsIntercepting() != 0:
			return 1
		elif pTravel.InterceptTarget != None:
			return 1
	return self.IsIntercepting()

#########################################
# logger helper
def LogError(strFromFunc):
	debug(__name__ + ", LogError")
	import sys
	et = sys.exc_info()
	if strFromFunc == None:
		strFromFunc = "???"
	if Logger:
		Logger.LogException(et, "ERROR at "+strFromFunc)
	else:
		error = str(et[0])+": "+str(et[1])
		print "ERROR at "+strFromFunc+", details -> "+error