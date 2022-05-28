from bcdebug import debug
#############################################################
# Preprocessors
#
# This file contains a collection of scripts and classes
# intended for use with PreprocessingAI objects.
#############################################################
import App
import math

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " Preprocessing module...")


# There's no point in unloading this module as missions, episodes,
# or games away.  Make it persistent at the game level.
# During serialization/unserialization, the current game will
# be None, and we don't want to call AddPersistentModule then anyways.
pGame = App.Game_GetCurrentGame()
if pGame:
	pGame.AddPersistentModule(__name__)
del pGame
# del's are there because I don't want pEpisode and pGame global variables sticking around.


#
# AvoidObstacles
#
# If this detects that a collision is imminent (or our
# personal space is a little cramped), it changes course
# and moves to fix the situation.
#
class AvoidObstaclesRam:
	def __init__(self):
		# Setup how often we'll do our check...
		debug(__name__ + ",AvoidObstacles __init__")
		self.fMinimumUpdateDelay = 0.0 # 0.25
		self.fMaximumUpdateDelay = 0.25 # 1.25
		self.fUpdateDelay = self.fMaximumUpdateDelay

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

		# If we're overriding the ship's course, we need
		# to know what direction to head toward, and what
		# speed to go.
		self.vOverrideDirection = None
		self.fOverrideSpeed = None
		
		# How long into the future we'll anticipate
		# collisions...
		self.fPredictionTime = 15.0

		# Minimum radius around which to look for incoming
		# objects.
		self.fMinimumRadius = 225.0 # 225 is about 40km.

		# Set how much space we want around ourselves, as
		# a multiple of our radius.
		self.fPersonalSpace = 2.5

		# Angles that determine how we maneuver...
		self.fFrontAngle = 20.0 / 180.0 * App.PI
		self.fSideAngle = App.HALF_PI
		self.fBackAngle = 170.0 / 180.0 * App.PI
		
		self.fFrontSpeed = 0.0
		self.fSideSpeed = 1.0
		self.fBackSpeed = 1.0

		# Types of objects that we won't bother avoiding:
		self.lDontAvoidTypes = [
			App.CT_PROXIMITY_CHECK,
			App.CT_DEBRIS,
			App.CT_TORPEDO,
			App.CT_ASTEROID_FIELD,
			App.CT_NEBULA,
			App.CT_SHIP,
			]

	def __getstate__(self):
		debug(__name__ + ", __getstate__")
		dState = self.__dict__.copy()
		dState["pModule"] = self.pModule.__name__
		return dState

	def __setstate__(self, dict):
		debug(__name__ + ", __setstate__")
		self.__dict__ = dict
		self.pModule = __import__(self.pModule)

	def GetNextUpdateTime(self):
		# Update time varies...
		debug(__name__ + ", GetNextUpdateTime")
		return self.fUpdateDelay

	def Update(self, dEndTime):
		# Under normal circumstances, we'll pass through
		# and let our contained AI do its stuff.
		debug(__name__ + ", Update")
		eRet = App.PreprocessingAI.PS_NORMAL
		self.fUpdateDelay = self.fMaximumUpdateDelay

		pShip = self.pCodeAI.GetShip()
		if (pShip == None):
			return App.PreprocessingAI.PS_DONE

		# If we're in-system warping, don't check for collisions, because
		# the in-system warp check already does that.
		if pShip.IsDoingInSystemWarp():
			return App.PreprocessingAI.PS_NORMAL

		# Update whether or not we should be overriding
		# the ship's course.
		self.vOverrideDirection, self.fOverrideSpeed = self.TestCourseOverride()

		if self.vOverrideDirection:
			# We're overriding the ship's course.
			# Don't let our contained AI do anything.
			eRet = App.PreprocessingAI.PS_SKIP_ACTIVE

			# Set the ship's course and speed.
			pShip.TurnTowardDirection( self.vOverrideDirection )
			pShip.SetImpulse( self.fOverrideSpeed, App.TGPoint3_GetModelForward(), App.ShipClass.DIRECTION_MODEL_SPACE)

			self.fUpdateDelay = self.fMinimumUpdateDelay

		# Done.
		return eRet

	def TestCourseOverride(self):
		# Get our ship...
		debug(__name__ + ", TestCourseOverride")
		pShip = self.pCodeAI.GetShip()
		if (pShip == None):
			return (None, None)

		pSet = pShip.GetContainingSet()
		if (pSet == None):
			# Not in a set.  Guess we can't collide with
			# anything.  :)
			return (None, None)

		# Predict our location in the near future...
		vPredictedLocation = pShip.GetPredictedPosition(
			pShip.GetWorldLocation(),
			pShip.GetVelocityTG(),
			pShip.GetAccelerationTG(),
			self.fPredictionTime)

		# Figure out how far that is from us...
		vDiff = App.TGPoint3()
		vDiff.Set( vPredictedLocation )
		vDiff.Subtract( pShip.GetWorldLocation() )
		fDistance = vDiff.Length()

		# Find any objects within the sphere centered at
		# our predicted location, with a radius of fDistance
		# plus our personal space.
		fPersonalSpaceRadius = pShip.GetRadius() * self.fPersonalSpace
		fCheckRadius = fDistance + fPersonalSpaceRadius
		if fCheckRadius < self.fMinimumRadius:
			fCheckRadius = self.fMinimumRadius

		pProxManager = pSet.GetProximityManager()
		lAvoidObjects = []
		if (pProxManager != None):
			pObjectIter = pProxManager.GetNearObjects( vPredictedLocation, fCheckRadius )
			pObject = pProxManager.GetNextObject( pObjectIter )
			while (pObject != None):
				# This object is inside the radius...
				# Is it our ship?
				if pObject.GetObjID() != pShip.GetObjID():
					# Nope.  It's something else.  Test whether
					# or not we need to avoid this object.
					if self.NeedToAvoid( pShip, fPersonalSpaceRadius, pObject ):
						# Probably going to collide, if we
						# don't do something.  Add this to
						# the list of objects we should avoid.
						lAvoidObjects.append( pObject )
				pObject = pProxManager.GetNextObject( pObjectIter )
			pProxManager.EndObjectIteration( pObjectIter )

		# Determine what our avoidance direction and speed
		# should be, based on the objects we need to avoid.
		return self.AvoidObjects( pShip, lAvoidObjects )

	def NeedToAvoid(self, pShip, fPersonalSpaceRadius, pObject):
		# Don't bother evading certain objects
		debug(__name__ + ", NeedToAvoid")
		for eType in self.lDontAvoidTypes:
			if pObject.IsTypeOf(eType):
				return 0

		# If the object is already within our personal space,
		# we need to avoid it.
		vDiff = pObject.GetWorldLocation()
		vDiff.Subtract(pShip.GetWorldLocation())
		fDist = vDiff.Length()
		if fDist < (fPersonalSpaceRadius + pObject.GetRadius()):
			return 1

		# Get the object's velocity.		
		vOtherVelocity = App.TGPoint3()
		pPhysObj = App.PhysicsObjectClass_Cast(pObject)
		if (pPhysObj != None):
			# This is a physics object.  It has a velocity..
			vOtherVelocity.Set(pPhysObj.GetVelocityTG())
		else:
			vOtherVelocity.SetXYZ(0,0,0)

		# Find our relative velocity...
		vVelDiff = App.TGPoint3()
		vVelDiff.Set( pShip.GetVelocityTG() )
		vVelDiff.Subtract(vOtherVelocity)
		
		# This thing is an incoming hazard if the distance between us
		# will drop below our personal space + their radius anytime
		# in the near future.
		# Setup vars for quadratic formula:
		# a = (Vsx - Vtx)^2 + (Vsy - Vty)^2 + (Vsz - Vtz)^2
		a = vVelDiff.SqrLength()
		if a > 0:
			# b = 2((Psx - Ptx)(Vsx - Vtx) + (Psy - Pty)(Vsy - Vty) + (Psz - Ptz)(Vsz - Vtz))
			vPosDiff = App.TGPoint3()
			vPosDiff.Set( pShip.GetWorldLocation() )
			vPosDiff.Subtract( pObject.GetWorldLocation() )
			b = 2 * vPosDiff.Dot(vVelDiff)

			# c = (Rs + Rt)^2  +  (Psx - Ptx)^2 + (Psy - Pty)^2 + (Psz - Ptz)^2
			fRadiusSum = (fPersonalSpaceRadius  +  pObject.GetRadius())
			c = -(fRadiusSum * fRadiusSum)  +  vPosDiff.SqrLength()

			# Find the soonest collision time:
			fHitTime = -1.0

			fSqrtPart = b*b - 4.0*a*c
			if fSqrtPart >= 0:
				fSqrt = math.sqrt(fSqrtPart)
				t1 = (-b + fSqrt) / (2*a)
				t2 = (-b - fSqrt) / (2*a)
			
				if t1 < t2:
					if t1 >= 0:
						fHitTime = t1
					else:
						fHitTime = t2
				else:
					if t2 >= 0:
						fHitTime = t2
					else:
						fHitTime = t1

			if fHitTime >= 0:
				# We found a collision sometime in the future.
				# If it's within our "incoming time" threshold, then
				# this object is a hazard.
				if fHitTime < self.fPredictionTime:
					return 1

		# Nope, not a hazard.
		return 0

	def AvoidObjects(self, pShip, lAvoidObjects):
		debug(__name__ + ", AvoidObjects")
		"""Determine what our direction and speed should be to
		avoid the given list of objects."""
		# If the list is empty, we do nothing.
		if len( lAvoidObjects ) == 0:
			return None, None

		# Build a list of directions, angles around those
		# directions, and favorability values for each direction.
		lpDirectionInfo = []
		for pObject in lAvoidObjects:
			# ***FIXME: If this object is HUGE (like
			# a starbase is), break up its main spheres
			# into smaller ones that are more representative
			# of the actual obstacle).
			vDirection = pObject.GetWorldLocation()
			vDirection.Subtract(pShip.GetWorldLocation())
			fDistance = vDirection.Unitize()

			pPhys = App.PhysicsObjectClass_Cast(pObject)
			if pPhys:
				vObstacleVelocity = pPhys.GetVelocityTG()
			else:
				vObstacleVelocity = App.TGPoint3()
				vObstacleVelocity.SetXYZ(0,0,0)

			# If there's no distance between the
			# two, how can we possibly avoid the other object?
			# Just ignore it, if that's the case.
			if fDistance > 0.0:
				# Change this so it just does multiplies and
				# a sqrt, rather than 2 trig functions..
				fBlockedAngle = math.atan((pObject.GetRadius() + pShip.GetRadius()) / fDistance)
				fBlockedDot = math.cos(fBlockedAngle)

				fFavorability = -self.fMinimumRadius / fDistance

				lpDirectionInfo.append((pObject.GetWorldLocation(), vDirection, vObstacleVelocity, fBlockedDot, fFavorability))

		# Next, we need to find a good direction to flee.
		# First, test the opposites of the directions in
		# the direction info...
		vFleeDir = None
		fFleeDirAppeal = -1.0e20
		for vPosition, vDirection, vObstacleVelocity, fBlockedAngle, fFavorability in lpDirectionInfo:
			# Get the opposite of the direction..
			vFleeTestDir = App.TGPoint3()
			vFleeTestDir.Set(vDirection)
			vFleeTestDir.Scale(-1.0)

			# Calculate its appeal.
			fTestDirAppeal = self.CalculateDirectionAppeal(pShip, vFleeTestDir, lpDirectionInfo)

			# Better than our last test?
			if fTestDirAppeal > fFleeDirAppeal:
				fFleeDirAppeal = fTestDirAppeal
				vFleeDir = vFleeTestDir

		# Then test a few random directions to see if there's a better one.
		for iAttempt in range(8):
			vFleeTestDir = App.TGPoint3_GetRandomUnitVector()

			# Calculate its appeal.
			fTestDirAppeal = self.CalculateDirectionAppeal(pShip, vFleeTestDir, lpDirectionInfo)

			# Better than our last test?
			if fTestDirAppeal > fFleeDirAppeal:
				fFleeDirAppeal = fTestDirAppeal
				vFleeDir = vFleeTestDir

		vNewHeading = vFleeDir

		# Our speed depends on whether we're currently facing
		# a safe direction or not.
		bFacingSafe = self.IsDirectionSafe(pShip.GetWorldForwardTG(), lpDirectionInfo)

		fSpeed = 0.0
		if bFacingSafe:
			fSpeed = 1.0

		return (vNewHeading, fSpeed)

	def CalculateDirectionAppeal(self, pShip, vTestDirection, lpDirectionInfo):
		# Compare this direction against the various
		# directions in the direction info.
		debug(__name__ + ", CalculateDirectionAppeal")
		fOverallAppeal = 0.0
		for vPosition, vDirection, vVelocity, fBlockedDot, fFavorability in lpDirectionInfo:
			# Find the dot product to this direction.
			fDot = vTestDirection.Dot(vDirection)

			# If our dot is inside fBlockedDot, we get the
			# full favorability value for this direction.
			if fDot >= fBlockedDot:
				fAppeal = fFavorability
				continue
			else:
				# Otherwise, the value of this direction
				# goes to the negative of the favorability
				# value, as the dot approaches 0, and
				# half the negative of the favorability
				# at -1.
				if fDot >= 0:
					try:
						fAppeal = fFavorability - (2.0 * fFavorability * (fBlockedDot - fDot) / fBlockedDot)
					except ZeroDivisionError:
						fAppeal = -fFavorability
				else:
					fAppeal = (fFavorability * fDot * 0.5)  +  (fFavorability * (1.0 + fDot))

			fOverallAppeal = fOverallAppeal + (fAppeal * 2.0)

			# Similar calculations against the velocity.
			vVelDir = App.TGPoint3()
			vVelDir.Set(vVelocity)
			vVelDir.Unitize()
			if vVelDir.SqrLength() > 0.0625:
				# Not a zero vector...
				fDot = vVelDir.Dot(vTestDirection)

				# Appeal goes from fFavorability at 1 to
				# -fFavorability at 0 to fFavorability at -1
				fAppeal = (abs(fDot) - 0.5) * 2.0 * fFavorability

				fOverallAppeal = fOverallAppeal + fAppeal

				# More calculations, to ensure that we aren't moving
				# in front of the other object.
				fDot = vDirection.Dot(vVelocity)
				if 1: #fDot < (0.125 / vVelocity.Length()):
					# We're roughly in front of the other object.  If
					# the direction is toward their front (the direction
					# they're moving), that's bad.
					vTestPerpendicular = vTestDirection.GetPerpendicularComponent( vVelocity )
					vDirectionPerpendicular = vDirection.GetPerpendicularComponent( vVelocity )

					vTestPerpendicular.Unitize()
					vDirectionPerpendicular.Unitize()

					fDot = vTestPerpendicular.Dot( vDirectionPerpendicular )
					fAppeal = fDot * fFavorability
				else:
					fAppeal = -fFavorability
				fOverallAppeal = fOverallAppeal + fAppeal

			# Finally, a little bit of goodness if this direction is
			# near our forward vector.
			fAppeal = pShip.GetWorldForwardTG().Dot(vDirection) * 0.1
			fOverallAppeal = fOverallAppeal + fAppeal

		return fOverallAppeal

	def IsDirectionSafe(self, vTestDirection, lpDirectionInfo):
		# Compare this direction against the various
		# directions in the direction info.
		debug(__name__ + ", IsDirectionSafe")
		for vPosition, vDirection, vVelocity, fBlockedDot, fFavorability in lpDirectionInfo:
			# Find the dot product to this direction.
			fDot = vTestDirection.Dot(vDirection)

			# If our dot is inside fBlockedDot, this
			# direction is not safe.
			if fDot >= fBlockedDot:
				return 0

		# This direction should be safe (ignoring our
		# own radius...).
		return 1
