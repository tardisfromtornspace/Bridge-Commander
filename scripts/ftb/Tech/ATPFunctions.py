from bcdebug import debug
import App
import math

# import DummyApp
# App = DummyApp.DummyApp()

import MissionLib

# These functions are adapted from Apollo's Advanced Technologies.
# Changes are, generally speaking, a stripping of the flag system
# which would be redundant to Foundation Tech, and some minor
# syntactic cleanup.  -Dasher42

#########################################################################################################################
#### ADVANCED TECHNOLOGIES 3												#
#### MADE BY Alexis Rombaut aka Apollo 											#
#### (c) 30/09/2003													#
####															#
#### Contact: Alexis.Rombaut@skynet.be											#
#########################################################################################################################


def ShieldDistributePos(pShip, fDamage):
	debug(__name__ + ", ShieldDistributePos")
	i = 0
	L = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	iNumber = 6.0
	fYield = fDamage

	pShields = pShip.GetShields()

	if pShields and fYield > 0:
		while (iNumber>0) and (fYield>0):
			i = 0
			fSum = 0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fAdd = fYield/iNumber+pShields.GetCurShields(ShieldDir)
				fMax = pShields.GetMaxShields(ShieldDir)
				fExcess = 0

				if (L[i] <= 0.0):
					if(fAdd<fMax):
						pShields.SetCurShields(ShieldDir, fAdd)
					else:
						pShields.SetCurShields(ShieldDir, fMax)
						fExcess = fAdd-fMax
						fSum = fSum+fExcess
						L[i] = fExcess
				i = i+1

			fYield = fSum

			iNumber = L.count(0.0)


def ShieldDistributeNeg(pShip, fDamage):
	debug(__name__ + ", ShieldDistributeNeg")
	i = 0
	L = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	iNumber = 6.0
	fYield = fDamage

	pShields = pShip.GetShields()

	if pShields and fYield > 0:
		while (iNumber>0) and (fYield>0):
			i = 0
			fSum = 0.0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fSus = pShields.GetCurShields(ShieldDir)-fYield/iNumber
				fExcess = 0

				if (L[i] <= 0.0):
					if(fSus>0):
						pShields.SetCurShields(ShieldDir, fSus)
					else:
						pShields.SetCurShields(ShieldDir, 0.0)
						fExcess = (-1.0)*fSus
						fSum = fSum+fExcess
						L[i] = fExcess
				i = i+1

			fYield = fSum



def FireTorpFromPoint(pAction, kPoint,
					  pcTorpScriptName, idTarget = App.NULL_ID, pShipID = App.NULL_ID,
					  idTargetSubsystem = App.NULL_ID, fSpeed = 0.0,
					  pcSetName = None):

	# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs -Apollo

	debug(__name__ + ", FireTorpFromPoint")
	pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

	if (pcSetName != None):
		pSet = App.g_kSetManager.GetSet(pcSetName)
	elif (pTarget != None):
		pSet = pTarget.GetContainingSet()
	else:
		# No idea what set this is supposed to be in.
		return 0

	if (pSet ==  None):
		# No set.
		return 0

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)

	if (idTargetSubsystem != App.NULL_ID):
		pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(idTargetSubsystem))
		if (pSubsystem != None):
			pTorp.SetTargetOffset(pSubsystem.GetPosition())
		else:
			pTorp.SetTargetOffset(kPoint)
	else:
		pTorp.SetTargetOffset(kPoint)

	pTorp.SetParent(pShipID)

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)

	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	if (pTarget != None):
		kTorpLocation = pTorp.GetWorldLocation()
		kTargetLocation = pTarget.GetWorldLocation()

		kTargetLocation.Subtract(kTorpLocation)
		kFwd = kTargetLocation
		kFwd.Unitize()
		kPerp = kFwd.Perpendicular()
		kPerp2 = App.TGPoint3()
		kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

		pTorp.AlignToVectors(kFwd, kPerp2)
		pTorp.UpdateNodeOnly()

	kVelocity = pTorp.GetWorldForwardTG()

	# Give the torpedo an appropriate speed.
	if (fSpeed ==  0.0):
		kVelocity.Scale(pTorp.GetLaunchSpeed())
	else:
		kVelocity.Scale(fSpeed)

	pTorp.SetVelocity(kVelocity)

	return pTorp


def FireTorpFromPointWithVector(kPoint, kVector, pcTorpScriptName, idTarget, pShipID, fSpeed, TGOffset = None):

	# This is an slightly altered version of the original definition (MissionLib.py), to suit specific needs

	debug(__name__ + ", FireTorpFromPointWithVector")
	pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
	pSet = pTarget.GetContainingSet()
	if not pSet:
		return None

	# Create the torpedo.
	pTorp = App.Torpedo_Create(pcTorpScriptName, kPoint)
	pTorp.UpdateNodeOnly()

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

	# Set up its target and target subsystem, if necessary.
	pTorp.SetTarget(idTarget)
	if not TGOffset and pShip:
		pTorp.SetTargetOffset(pShip.GetHull().GetPosition())
	else:
		pTorp.SetTargetOffset(TGOffset)
	pTorp.SetParent(pShipID)

	# Add the torpedo to the set, and place it at the specified placement.
	pSet.AddObjectToSet(pTorp, None)
	pTorp.UpdateNodeOnly()

	# If there was a target, then orient the torpedo towards it.
	kTorpLocation = pTorp.GetWorldLocation()
	kTargetLocation = pTarget.GetWorldLocation()

	kTargetLocation.Subtract(kTorpLocation)
	kFwd = kTargetLocation
	kFwd.Unitize()
	kPerp = kFwd.Perpendicular()
	kPerp2 = App.TGPoint3()
	kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)
	pTorp.AlignToVectors(kFwd, kPerp2)
	pTorp.UpdateNodeOnly()

	# Give the torpedo an appropriate speed.
	kSpeed = CopyVector(kVector)
	kSpeed.Unitize()
	kSpeed.Scale(fSpeed)
	pTorp.SetVelocity(kSpeed)

	return pTorp



def DirectReflector(pShip, pInstance, pTorp, oYield, pEvent):
	debug(__name__ + ", DirectReflector")
	pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())

	pTorpPath = pTorp.GetModuleName()
	life = pTorp.GetGuidanceLifeTime()

	pSet = pAttacker.GetContainingSet()

	X = pAttacker.GetWorldLocation()

	kVectNiWorldHitPoint = pEvent.GetWorldHitPoint()
	Y = App.TGPoint3()
	Y.SetX(kVectNiWorldHitPoint.x)
	Y.SetY(kVectNiWorldHitPoint.y)
	Y.SetZ(kVectNiWorldHitPoint.z)
	kVectNiWorldHitNormal = pEvent.GetWorldHitNormal()
	N = App.TGPoint3()
	N.SetX(kVectNiWorldHitNormal.x)
	N.SetY(kVectNiWorldHitNormal.y)
	N.SetZ(kVectNiWorldHitNormal.z)

	X.Subtract(Y)
	X.Unitize()
	U = X.Cross(N)
	V = N.Cross(U)
	V.Unitize()
	V.Scale(-2.0*X.Dot(V))
	X.Add(V)
	
	FireTorpFromPointWithVector(Y,X,pTorpPath,pAttacker.GetObjID(),pShip.GetObjID(),pTorp.GetLaunchSpeed())

	# Remove damage caused by the torpedo
	pTorp.SetLifetime(0.0)
	fDamage = pEvent.GetDamage() / 10#The power to reflect the weapon causes damage, 10% of the original damage
	#ShieldDistributePos(pShip,fDamage)
	ShieldDistributeNeg(pShip, fDamage)


def RandomReflector(pShip, pInstance, pTorp, oYield, pEvent):
	debug(__name__ + ", RandomReflector")
	pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())

	pTorpPath = pTorp.GetModuleName()
	life = pTorp.GetGuidanceLifeTime()

	pSet = pAttacker.GetContainingSet()

	X = pAttacker.GetWorldLocation()

	kVectNiWorldHitPoint = pEvent.GetWorldHitPoint()
	Y = App.TGPoint3()
	Y.SetX(kVectNiWorldHitPoint.x)
	Y.SetY(kVectNiWorldHitPoint.y)
	Y.SetZ(kVectNiWorldHitPoint.z)
	kVectNiWorldHitNormal = pEvent.GetWorldHitNormal()
	N = App.TGPoint3()
	N.SetX(kVectNiWorldHitNormal.x)
	N.SetY(kVectNiWorldHitNormal.y)
	N.SetZ(kVectNiWorldHitNormal.z)

	X.Subtract(Y)
	X.Unitize()
	U = X.Cross(N)
	V = N.Cross(U)
	V.Unitize()
	V.Scale(-2.0*X.Dot(V))
	X.Add(V)

	X.Add(App.TGPoint3_GetRandomUnitVector()) # MLeo addition, add a little bit of randomness to this.
	
	FireTorpFromPointWithVector(Y,X,pTorpPath,pAttacker.GetObjID(),pShip.GetObjID(),pTorp.GetLaunchSpeed())

	# Remove damage caused by the torpedo
	pTorp.SetLifetime(0.0)
	fDamage = pEvent.GetDamage()/10#The power to reflect the weapon causes damage, 10% of the original damage
	#ShieldDistributePos(pShip,fDamage)
	ShieldDistributeNeg(pShip, fDamage)


def CopyVector(kVect):
	debug(__name__ + ", CopyVector")
	kCopy = App.TGPoint3()
	kCopy.SetXYZ(kVect.GetX(),kVect.GetY(),kVect.GetZ())
	return kCopy


def ToDegree(a):
	debug(__name__ + ", ToDegree")
	return a*180.0/math.pi


def IsEnemy(pShip):
	debug(__name__ + ", IsEnemy")
	pGame = App.Game_GetCurrentGame()

	pEpisode = pGame.GetCurrentEpisode()

	pMission = pEpisode.GetCurrentMission()
	pEnemies = pMission.GetEnemyGroup()
	return(pEnemies.IsNameInGroup(pShip.GetName()))


def IsFriend(pShip):
	debug(__name__ + ", IsFriend")
	pGame = App.Game_GetCurrentGame()

	pEpisode = pGame.GetCurrentEpisode()

	pMission = pEpisode.GetCurrentMission()
	pFriendlies = pMission.GetFriendlyGroup()
	return(pFriendlies.IsNameInGroup(pShip.GetName()))


def MakeFriendShipList(pSet = None):
	debug(__name__ + ", MakeFriendShipList")
	pGame = App.Game_GetCurrentGame()

	pEpisode = pGame.GetCurrentEpisode()

	pMission = pEpisode.GetCurrentMission()
	pFriendlies = pMission.GetFriendlyGroup()

	pPlayer = MissionLib.GetPlayer ()
	pPlayerID = pPlayer.GetObjID()

	lFriendlyShips = []

	if pFriendlies != None:
		if(pSet == None):
			ObjTuple = pFriendlies.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		else:
			ObjTuple = pFriendlies.GetActiveObjectTupleInSet(pSet)
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:
					lFriendlyShips.append(pObj.GetObjID())

	# Apollo, this list is global now, so returning a list copied
	# with [:] is unnecessary.  Yay for efficiency!
	return lFriendlyShips


def MakeEnemyShipList(pSet = None):
	debug(__name__ + ", MakeEnemyShipList")
	pGame = App.Game_GetCurrentGame()

	pEpisode = pGame.GetCurrentEpisode()

	pMission = pEpisode.GetCurrentMission()
	pEnemies = pMission.GetEnemyGroup()
	pPlayer = MissionLib.GetPlayer ()
	pPlayerID = pPlayer.GetObjID()

	lEnemyShips = []

	if pEnemies != None:
		if(pSet == None):
			ObjTuple = pEnemies.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		else:
			ObjTuple = pEnemies.GetActiveObjectTupleInSet(pSet)
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:
					lEnemyShips.append(pObj.GetObjID())

	return lEnemyShips


def MakeNeutralShipList(pSet = None):
	debug(__name__ + ", MakeNeutralShipList")
	pGame = App.Game_GetCurrentGame()

	pEpisode = pGame.GetCurrentEpisode()

	pMission = pEpisode.GetCurrentMission()
	pNeutral = pMission.GetNeutralGroup()
	pPlayer = MissionLib.GetPlayer ()
	pPlayerID = pPlayer.GetObjID()

	g_NeutralShipList = []

	if pNeutral != None:
		if(pSet == None):
			ObjTuple = pNeutral.GetActiveObjectTupleInSet(pPlayer.GetContainingSet())
		else:
			ObjTuple = pNeutral.GetActiveObjectTupleInSet(pSet)
		if len(ObjTuple):
			for i in ObjTuple:
				pObj = App.ShipClass_Cast(i)
				if pObj:
					g_NeutralShipList.append(pObj.GetObjID())

	return g_NeutralShipList


def DistanceSort(lShips, kPoint, fMax = 0):
	debug(__name__ + ", DistanceSort")
	dDistance = {}

	for i in lShips:
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(i))
		kTemp = App.TGPoint3()
		kTemp = pShip.GetWorldLocation()
		kTemp.Subtract(kPoint)
		fKey = kTemp.Length()
		if fMax ==  0:
			dDistance[fKey] = i
		elif fKey <= fMax:
			dDistance[fKey] = i

	lKeys = dDistance.keys()
	lKeys.sort()

	lRetShips = []

	for i in lKeys:
		lRetShips.append(dDistance[i])

	return lRetShips


def GetDebrisListInSet(pSet = None):
	debug(__name__ + ", GetDebrisListInSet")
	if pSet == None:
		pPlayer = MissionLib.GetPlayer()
		pSet = pPlayer.GetContainingSet()

	RetList = []

	pFirst = pSet.GetFirstObject()
	pObject = pSet.GetNextObject(pFirst.GetObjID())

	i = 0
	while pObject:
		i = i+1
		if pObject.IsTypeOf(App.CT_BASE_OBJECT):
			RetList.append(pObject)

		pObject = pSet.GetNextObject(pObject.GetObjID())

		if pObject.GetObjID() == pFirst.GetObjID():
			break
		if i>1000:
			print "OVERFLOW"
			break

	return RetList


