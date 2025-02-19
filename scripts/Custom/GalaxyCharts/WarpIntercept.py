from bcdebug import debug
#
# WarpIntercept
#
# In-System Warp, to reach a far target.  Once we're close, go in normal intercept.
#
# I made this in a separeted script from TravelerAI_Overrides, so that it doesn't get too crowded lol
#
import App
import AI.PlainAI.BaseAI
import math

from Custom.GalaxyCharts.TravelerAI_Override import Logger

class WarpIntercept(AI.PlainAI.BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		# Parent class init first.
		debug(__name__ + ", __init__")
		AI.PlainAI.BaseAI.BaseAI.__init__(self, pCodeAI)
		Logger.LogString("WarpIntercept class initialization")
		# Set default values for parameters that have them.
		self.SetupDefaultParams(
			self.SetMaximumSpeed,
			self.SetInterceptDistance,
			self.SetAddObjectRadius,
			self.SetMoveInFront,
			self.SetInSystemWarpDistance)
		self.SetRequiredParams(
			( "sTargetName", "SetTargetObjectName" ) )
		self.SetExternalFunctions(
			( "SetTarget", "SetTargetObjectName" ) )

		self.bDecelerated = 0
	#	print "CODE AI: ", pCodeAI
		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)
		

	# The name of our target.
	def SetTargetObjectName(self, sName): #AISetup
		self.sTargetName = sName

	def SetInterceptDistance(self, fDistance = None): #AISetup
		if fDistance == None:
			debug(__name__ + ", SetInterceptDistance")
			fDistance = App.UtopiaModule_ConvertKilometersToGameUnits(50.0)
		self.fInterceptDistance = fDistance

	def SetMaximumSpeed(self, fSpeed = 1.0e20): #AISetup
		self.fMaximumSpeed = fSpeed

	def SetAddObjectRadius(self, bUseRadius = 1): #AISetup
		self.bUseRadius = bUseRadius

	def SetMoveInFront(self, bMoveInFront = 0): #AISetup
		self.bMoveInFront = bMoveInFront

	# Default InSystemWarpDistance value used to be 575.
	def SetInSystemWarpDistance(self, fDistance = None): #AISetup
		if fDistance == None:
			debug(__name__ + ", SetInSystemWarpDistance")
			fDistance = App.UtopiaModule_ConvertKilometersToGameUnits(900.0)
		self.fInSystemWarpDistance = fDistance


	fTowardAngle	= 15.0 * App.PI / 180.0
	fNearAngle	= 30.0 * App.PI / 180.0
	fFarAngle	= 45.0 * App.PI / 180.0

	fTowardSpeed	= 1.0
	fNearSpeed	= 0.9
	fFarSpeed	= 0.7

	fMaxPredictionDistance	= 100.0

	def LostFocus(self):
		# Make sure we're no longer doing an in-system warp,
		# if we were before.
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			Logger.LogString("WIU: lost focus - stop in system warp")
			pShip.StopInSystemWarp()
			pShip.StopIntercept()

	def GetStatusInfo(self):
		debug(__name__ + ", GetStatusInfo")
		return "Target(%s), MaxSpeed(%f), Distance(%f), AddRadius(%d), WarpDist(%f)" % (
			self.sTargetName, self.fMaximumSpeed, self.fInterceptDistance, self.bUseRadius,
			self.fInSystemWarpDistance)

	def GetNextUpdateTime(self):
		# We want to be updated every 0.3 seconds (+/- 0.2)
		debug(__name__ + ", GetNextUpdateTime")
		fRandomFraction = (App.g_kSystemWrapper.GetRandomNumber(10001) - 5000.0) / 5000.0
		return 0.3 + (fRandomFraction * 0.2)

	def Update(self):
		debug(__name__ + ", Update")
		"Do our stuff"
		eRet = App.ArtificialIntelligence.US_DONE
	#	Logger.LogString("WIU: start")
	#	print "wiu: mark 1"
		pShip = self.pCodeAI.GetShip()
		if (pShip == None):
			# ***FIXME: For now, this AI only works on ShipClass
			# and below...
			return App.ArtificialIntelligence.US_DONE
	#	Logger.LogString("WIU: after getting pShip")

		# Get the set we're in, if any.
		pSet = pShip.GetContainingSet()
		if (pSet == None):
#			debug("Intercept update done: no set")
			return eRet
	#	Logger.LogString("WIU: got containing set")
	#	print "wiu: mark 2"
		# Get our target object.
		pObject = App.ObjectClass_GetObject(pSet, self.sTargetName)
		if not pObject:
			# Couldn't find it.  Maybe it's a waypoint?
			pObject = App.PlacementObject_GetObject(pSet, self.sTargetName)
	#	Logger.LogString("WIU: got target object")
	#	print "wiu: mark 3"
		if (pObject != None):
			eRet = App.ArtificialIntelligence.US_ACTIVE

			# Determine the anticipated position of the target,
			# if we fly at them at maximum acceleration right now.
			vOrigDirection = pObject.GetWorldLocation()
			vOrigDirection.Subtract(pShip.GetWorldLocation())
			fObjectDistance = vOrigDirection.Unitize()
	#		Logger.LogString("WIU: mark 1")
	#		print "wiu: mark 4"
			if not pShip.GetImpulseEngineSubsystem():
	#			Logger.LogString("WIU: no impulse engines - returning")
				return eRet
			fMaxSpeed = pShip.GetImpulseEngineSubsystem().GetMaxSpeed()
			if fMaxSpeed > 0:
				# Not particularly accurate (but not horribly
				# bad):
				fTime = fObjectDistance / fMaxSpeed
	#			Logger.LogString("WIU: calculated fTime")
	#			print "wiu: mark 5"
				# Predict the target's location in that
				# amount of time.
				pPhysicsObject = App.PhysicsObjectClass_Cast( pObject )
				if (pPhysicsObject == None):
					# It's not a physics object.  Predicted
					# position is just its current position.
					vDestination = pObject.GetWorldLocation()
				else:
					vDestination = pPhysicsObject.GetPredictedPosition( pPhysicsObject.GetWorldLocation(), pPhysicsObject.GetVelocityTG(), pPhysicsObject.GetAccelerationTG(), fTime )
	#			Logger.LogString("WIU: got predicted position")
	#			print "wiu: mark 6"
				# If the predicted destination is too far
				# from the current position, shorten it.
				# Realistically, there's no way anyone's
				# going to anticpate that far away (and
				# it ends up being pretty useless to do
				# so, anyways).
				vPredictedDiff = App.TGPoint3()
				vPredictedDiff.Set(vDestination)
				vPredictedDiff.Subtract( pObject.GetWorldLocation() )
				if vPredictedDiff.SqrLength() > (self.fMaxPredictionDistance * self.fMaxPredictionDistance):
					# Too long.
	#				print "wiu: mark 6.b"
					vPredictedDiff.Unitize()
					vPredictedDiff.Scale(self.fMaxPredictionDistance)
					vPredictedDiff.Add( pObject.GetWorldLocation() )
					vDestination.Set( vPredictedDiff )
	#			Logger.LogString("WIU: done additional position prediction check")
	#			print "wiu: mark 7"
				if self.bMoveInFront:
					# Our actual destination is some distance in
					# front of this predicted location, so add
					# a scaled Forward vector to it..
					vOffset = pObject.GetWorldForwardTG()
					fForwardDist = self.fInterceptDistance
					if self.bUseRadius:
						fForwardDist = fForwardDist + pObject.GetRadius()
					vOffset.Scale(fForwardDist)
					vDestination.Add(vOffset)
	#				print "wiu: mark 8.a"
	#				Logger.LogString("WIU: done MoveInFront stuff")
				else:
					# Our destination is on the near side of the target's predicted
					# location.
					vOffset = pShip.GetWorldLocation()
					vOffset.Subtract( vDestination )
					vOffset.Unitize()
					fDist = self.fInterceptDistance
					if self.bUseRadius:
						fDist = fDist + pObject.GetRadius()
					vOffset.Scale( fDist )
	#				print "wiu: mark 8.b"
					vDestination.Add( vOffset )
	#				Logger.LogString("WIU: got our destination vec")

				# Check our destination and adjust it for planets and things...
				# Pull the destination in a little before this adjustment.
				vAdjustedDestination = App.TGPoint3()
				vAdjustedDestination.Set(vDestination)
				vOffset = pShip.GetWorldLocation()
				vOffset.Subtract(vDestination)
	#			print "wiu: mark 9"
				vOffset.Unitize()
				vOffset.Scale(pObject.GetRadius())
	#			Logger.LogString("WIU: check our destination")
				if self.AdjustDestinationForLargeObstacles(pShip, vAdjustedDestination):
					vDestination = vAdjustedDestination
	#				print "wiu: mark 9.b"
					pSet = pShip.GetContainingSet()
					if pSet:
						sPlacement = "%s_Intercept_Adjust" % pShip.GetName()
						pAdjustedPlacement = App.PlacementObject_GetObject(pSet, sPlacement)
						if not pAdjustedPlacement:
							pAdjustedPlacement = App.PlacementObject_Create(sPlacement, pSet.GetName(), None)
						pAdjustedPlacement.SetTranslate(vDestination)
						pAdjustedPlacement.UpdateNodeOnly()
	#					print "wiu: mark 9.c"
						pObject = pAdjustedPlacement
						Logger.LogString("WIU: changed target object")

				# Turn toward the destination..
				fTurnTime = pShip.TurnTowardLocation( vDestination )
	#			Logger.LogString("WIU: turn toward location")
	#			print "wiu: mark 10"
				vDifference, fDistance, vDirection, fAngle = pShip.GetRelativePositionInfo( vDestination )

				# If fDistance is less than our ship's radius,
				# we're done.
				if fDistance < pShip.GetRadius():
					Logger.LogString("WIU: returning - fDistance is less that ship radius")
					return App.ArtificialIntelligence.US_DONE
	#			print "wiu: mark 11"
				# Or if we're not moving in front and we're within fInterceptDistance
				# of the object, we're done.
				
				if (not self.bMoveInFront)  and  (fObjectDistance < self.fInterceptDistance):
					Logger.LogString("WIU: returning - were within intercept distance and not moving to front")
					return App.ArtificialIntelligence.US_DONE
	#			print "wiu: mark 12"
	#			Logger.LogString("WIU: mark 2")

				# If we're extremely far away, override the normal
				# speed limitations and do an in-set warp.
				bWarping = 0
				if (self.fMaximumSpeed == 1.0e20):
					bWarping = pShip.InSystemWarp(pObject, self.fInSystemWarpDistance)
				
				if bWarping == 1:
					if self.pCodeAI.IsInterruptable() == 1:
						self.pCodeAI.SetInterruptable(0)
				else:
					if self.pCodeAI.IsInterruptable() == 0:
						self.pCodeAI.SetInterruptable(1)
					# now we do the following, in-case the ship is real warping, don't intercept
					pTravel = App.g_kTravelManager.GetTravel(pShip)
					if pTravel != None:
						bWarping = pTravel.IsTravelling()
							
				if bWarping != 1:
					# not doing an in-system warp. So use the normal intercept speed now.
					# this was actually the original in-system warp :P
					bIntercepting = pShip.Intercept(pObject, App.UtopiaModule_ConvertKilometersToGameUnits(50.0) )

					if bIntercepting != 1:
						# Not doing an in-system intercept.  Our speed should be the
						# maximum speed that will allow us to stop at the specified
						# location.
	#					print "too close, normal speed"
						fMaxSpeed = pShip.GetImpulseEngineSubsystem().GetMaxSpeed()
						fMaxAccel = pShip.GetImpulseEngineSubsystem().GetMaxAccel()

						fSpeed = fMaxSpeed
						fStopDist = 0
						if fMaxAccel > 0:
							fStopDist = fMaxSpeed * fMaxSpeed / (fMaxAccel * 2.0)

						# The ship needs to be able to stop within the
						# calculated distance.  If we're within the distance
						# we need to start stopping.
						if fDistance < fStopDist:
							# We need to stop.  Make sure our velocity
							# is low enough that we can stop in time.
							#fMaxVel = math.sqrt(2 * fMaxAccel * fStopDist)
							fMaxVel = math.sqrt(fMaxSpeed * fMaxSpeed - (2 * fMaxAccel * fDistance))

							# If our current moving speed is greater than fMaxVel, try to slow to 0.  If it's
							# less, set it to fMaxVel.  This should ensure that we stop close to the right spot.
							fCurrentSpeed = pShip.GetVelocityTG().Length()
							if fCurrentSpeed < fMaxVel:
								fSpeed = fMaxVel
							else:
								fSpeed = 0.0

						# Cap the speed to our maximum speed.
						fSpeed = min(fSpeed, self.fMaximumSpeed)

						pShip.SetSpeed( fSpeed, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE )

	#			print "wiu: mark 13"
	#			Logger.LogString("WIU: mark finale")
		return eRet

	# Check our destination and adjust it for planets and things...
	def AdjustDestinationForLargeObstacles(self, pShip, vDestination):
		# Find any obstacles in the way...
		debug(__name__ + ", AdjustDestinationForLargeObstacles")
		pSet = pShip.GetContainingSet()
		if not pSet:
			return 0

		pProx = pSet.GetProximityManager()
		if not pProx:
			return 0

		lAvoidObjects = []

		fShipSize = pShip.GetRadius() * 4.0
		vStart = pShip.GetWorldLocation()
		vDiff = App.TGPoint3()
		vDiff.Set(vDestination)
		vDiff.Subtract(vStart)
		pIter = pProx.GetLineIntersectObjects(vStart, vDestination, fShipSize, 1)
		pObject = pProx.GetNextObject(pIter)
		while pObject:
			# Check to see if the object is actually in front of us.
			vObstacleDiff = pObject.GetWorldLocation()
			vObstacleDiff.Subtract(vStart)
			if vObstacleDiff.Dot( vDiff ) > 0.0:
				# Check to see if the object is on the near side of our destination, too...
				vObDestDiff = pObject.GetWorldLocation()
				vObDestDiff.Subtract(vDestination)
				if vObDestDiff.Dot( vDiff ) < 0.0:
					# If this is a planet, we need to avoid it.
					pPlanet = App.Planet_Cast(pObject)
					if pPlanet:
						fRadius = pPlanet.GetRadius() + min(125.0, pPlanet.GetAtmosphereRadius())
						#debug("May avoid planet %s." % pPlanet.GetName())
						lAvoidObjects.append( (pPlanet.GetWorldLocation(), fRadius) )
					elif App.ShipClass_Cast(pObject)  and  pObject.GetRadius() > 150.0:
						# If this is a very large ship, avoid it.
						#debug("May avoid %s." % pObject.GetName())
						lAvoidObjects.append( (pObject.GetWorldLocation(), pObject.GetRadius()) )

			pObject = pProx.GetNextObject(pIter)
		pProx.EndObjectIteration(pIter)

		# If there's nothing to avoid, we're done.
		if not lAvoidObjects:
			return 0

		# Check which objects we're inside...  We need to
		# avoid these ones first.
		lInsideObjects = []
		for vLocation, fRadius in lAvoidObjects:
			vObstacleDiff = App.TGPoint3()
			vObstacleDiff.Set(vLocation)
			vObstacleDiff.Subtract(vStart)
			if vObstacleDiff.Length() < (fShipSize + fRadius):
				# We're inside this object..
				lInsideObjects.append( (vLocation, fRadius) )

		if lInsideObjects:
			if self.AdjustDestinationAvoidingObjects(lInsideObjects, vStart, fShipSize, vDestination):
				return 1

		return self.AdjustDestinationAvoidingObjects(lAvoidObjects, vStart, fShipSize, vDestination)

	def AdjustDestinationAvoidingObjects(self, lAvoidObjects, vStart, fShipSize, vDestination):
		# Gotta avoid stuff.  Find the nearest one that needs avoiding.
		debug(__name__ + ", AdjustDestinationAvoidingObjects")
		fNearest = None
		lNearest = None

		vRay = App.TGPoint3()
		vRay.Set(vDestination)
		vRay.Subtract(vStart)
		for lInfo in lAvoidObjects:
			vNearPoint = App.TGPoint3()
			vFarPoint = App.TGPoint3()
			if App.TGGeomUtils_LineSphereIntersection(vStart, vRay, lInfo[0], lInfo[1], vNearPoint, vFarPoint):
				vNearPoint.Subtract(vStart)
				if (lNearest is None)  or  (vNearPoint.SqrLength() < fNearest):
					lNearest = lInfo
					fNearest = vNearPoint.SqrLength()

		if not lNearest:
			return 0

		# Need to avoid lNearest object.
		# We need to turn far enough away from the object so
		# that we'll fly clear around it.
		vToObject = App.TGPoint3()
		vToObject.Set(lNearest[0])
		vToObject.Subtract(vStart)

		vUp = vToObject.UnitCross( vRay )

		# Rotate vToObject around vUp until it points far enough away..
		import math
		try:
			fCombinedRadius = fShipSize + lInfo[1]
			fAngle = math.acos( math.sqrt(vToObject.SqrLength() - (fCombinedRadius * fCombinedRadius)) / vToObject.Length() )
		except ValueError:
			fAngle = App.HALF_PI

		mRotation = App.TGMatrix3()
		mRotation.MakeRotation(-fAngle, vUp)

		vToObject.MultMatrixLeft(mRotation)

		# Push the new destination out so it's the same distance as the old destination.
		vToObject.Unitize()
		vToObject.Scale(vRay.Length())
		
		vToObject.Add(vStart)
		vDestination.Set(vToObject)

		#debug("Adjusted destination to <%f,%f,%f>" % (vDestination.GetX(), vDestination.GetY(), vDestination.GetZ()))

		return 1

