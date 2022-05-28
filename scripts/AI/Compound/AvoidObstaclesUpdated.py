from bcdebug import debug
import App
import math

class AvoidObstaclesUpdated:

    def __init__(self):
        debug(__name__ + ", __init__")
        self.fMinimumUpdateDelay = 0.2
        self.fMaximumUpdateDelay = 0.4
        self.fUpdateDelay = self.fMaximumUpdateDelay
        self.pModule = __import__(__name__)
        self.vOverrideDirection = None
        self.fOverrideSpeed = None
        self.fPredictionTime = 10.0
        self.fMinimumRadius = 70
        self.fPersonalSpace = 1.08
        self.fFrontAngle = ((15.0 / 180.0) * App.PI)
        self.fSideAngle = ((45.0 / 180.0) * App.PI)
        self.fBackAngle = ((90.0 / 180.0) * App.PI)
        self.fFrontSpeed = 0.0
        self.fSideSpeed = 0.8
        self.fBackSpeed = 0.8
        self.lDontAvoidTypes = [App.CT_PROXIMITY_CHECK, App.CT_DEBRIS, App.CT_TORPEDO, App.CT_ASTEROID_FIELD, App.CT_NEBULA]


    def __getstate__(self):
        debug(__name__ + ", __getstate__")
        dState = self.__dict__.copy()
        dState['pModule'] = self.pModule.__name__
        return dState


    def __setstate__(self, dict):
        debug(__name__ + ", __setstate__")
        self.__dict__ = dict
        self.pModule = __import__(self.pModule)


    def GetNextUpdateTime(self):
        debug(__name__ + ", GetNextUpdateTime")
        return self.fUpdateDelay


    def Update(self, dEndTime):
        debug(__name__ + ", Update")
        eRet = App.PreprocessingAI.PS_NORMAL
        self.fUpdateDelay = self.fMaximumUpdateDelay
        pShip = self.pCodeAI.GetShip()
        if (pShip == None):
            return App.PreprocessingAI.PS_DONE
        if pShip.IsDoingInSystemWarp():
            return App.PreprocessingAI.PS_NORMAL
        (self.vOverrideDirection, self.fOverrideSpeed,) = self.TestCourseOverride()
        if self.vOverrideDirection:
            eRet = App.PreprocessingAI.PS_SKIP_ACTIVE
            pShip.TurnTowardDirection(self.vOverrideDirection)
            pShip.SetImpulse((self.fOverrideSpeed * 0.8), App.TGPoint3_GetModelForward(), App.ShipClass.DIRECTION_MODEL_SPACE)
            self.fUpdateDelay = self.fMinimumUpdateDelay
        return eRet


    def TestCourseOverride(self):
        debug(__name__ + ", TestCourseOverride")
        pShip = self.pCodeAI.GetShip()
        if (pShip == None):
            return (None, None)
        pSet = pShip.GetContainingSet()
        if (pSet == None):
            return (None, None)
        vPredictedLocation = pShip.GetPredictedPosition(pShip.GetWorldLocation(), pShip.GetVelocityTG(), pShip.GetAccelerationTG(), self.fPredictionTime)
        vDiff = App.TGPoint3()
        vDiff.Set(vPredictedLocation)
        vDiff.Subtract(pShip.GetWorldLocation())
        fDistance = vDiff.Length()
        fPersonalSpaceRadius = ((pShip.GetRadius() * 0.8) * self.fPersonalSpace)
        fCheckRadius = (fDistance + fPersonalSpaceRadius)
        if (fCheckRadius < self.fMinimumRadius):
            fCheckRadius = self.fMinimumRadius
        pProxManager = pSet.GetProximityManager()
        lAvoidObjects = []
        if (pProxManager != None):
            pObjectIter = pProxManager.GetNearObjects(vPredictedLocation, fCheckRadius)
            pObject = pProxManager.GetNextObject(pObjectIter)
            while (pObject != None):
                if (pObject.GetObjID() != pShip.GetObjID()):
                    if self.NeedToAvoid(pShip, fPersonalSpaceRadius, pObject):
                        lAvoidObjects.append(pObject)
                pObject = pProxManager.GetNextObject(pObjectIter)

            pProxManager.EndObjectIteration(pObjectIter)
        return self.AvoidObjects(pShip, lAvoidObjects)


    def NeedToAvoid(self, pShip, fPersonalSpaceRadius, pObject):
        debug(__name__ + ", NeedToAvoid")
        for eType in self.lDontAvoidTypes:
            if pObject.IsTypeOf(eType):
                return 0

        vDiff = pObject.GetWorldLocation()
        vDiff.Subtract(pShip.GetWorldLocation())
        fDist = vDiff.Length()
        if (fDist < (fPersonalSpaceRadius + (pObject.GetRadius() * 0.45))):
            return 1
        vOtherVelocity = App.TGPoint3()
        pPhysObj = App.PhysicsObjectClass_Cast(pObject)
        if (pPhysObj != None):
            vOtherVelocity.Set(pPhysObj.GetVelocityTG())
        else:
            vOtherVelocity.SetXYZ(0, 0, 0)
        vVelDiff = App.TGPoint3()
        vVelDiff.Set(pShip.GetVelocityTG())
        vVelDiff.Subtract(vOtherVelocity)
        a = vVelDiff.SqrLength()
        if (a > 0):
            vPosDiff = App.TGPoint3()
            vPosDiff.Set(pShip.GetWorldLocation())
            vPosDiff.Subtract(pObject.GetWorldLocation())
            b = (2 * vPosDiff.Dot(vVelDiff))
            fRadiusSum = (fPersonalSpaceRadius + (pObject.GetRadius() * 0.8))
            c = (-(fRadiusSum * fRadiusSum) + vPosDiff.SqrLength())
            fHitTime = -1.0
            fSqrtPart = ((b * b) - ((4.0 * a) * c))
            if (fSqrtPart >= 0):
                fSqrt = math.sqrt(fSqrtPart)
                t1 = ((-b + fSqrt) / (2 * a))
                t2 = ((-b - fSqrt) / (2 * a))
                if (t1 < t2):
                    if (t1 >= 0):
                        fHitTime = t1
                    else:
                        fHitTime = t2
                elif (t2 >= 0):
                    fHitTime = t2
                else:
                    fHitTime = t1
            if (fHitTime >= 0):
                if (fHitTime < self.fPredictionTime):
                    return 1
        return 0


    def AvoidObjects(self, pShip, lAvoidObjects):
        debug(__name__ + ", AvoidObjects")
        'Determine what our direction and speed should be to\012\011\011avoid the given list of objects.'
        if (len(lAvoidObjects) == 0):
            return (None, None)
        lpDirectionInfo = []
        for pObject in lAvoidObjects:
            vDirection = pObject.GetWorldLocation()
            vDirection.Subtract(pShip.GetWorldLocation())
            fDistance = vDirection.Unitize()
            pPhys = App.PhysicsObjectClass_Cast(pObject)
            if pPhys:
                vObstacleVelocity = pPhys.GetVelocityTG()
            else:
                vObstacleVelocity = App.TGPoint3()
                vObstacleVelocity.SetXYZ(0, 0, 0)
            if (fDistance > 0.0):
                fBlockedAngle = math.atan((((pObject.GetRadius() * 0.8) + (pShip.GetRadius() * 0.8)) / fDistance))
                fBlockedDot = math.cos(fBlockedAngle)
                fFavorability = (-self.fMinimumRadius / fDistance)
                lpDirectionInfo.append((pObject.GetWorldLocation(), vDirection, vObstacleVelocity, fBlockedDot, fFavorability))

        vFleeDir = None
        fFleeDirAppeal = -1e+20
        for (vPosition, vDirection, vObstacleVelocity, fBlockedAngle, fFavorability,) in lpDirectionInfo:
            vFleeTestDir = App.TGPoint3()
            vFleeTestDir.Set(vDirection)
            vFleeTestDir.Scale(-1.0)
            fTestDirAppeal = self.CalculateDirectionAppeal(pShip, vFleeTestDir, lpDirectionInfo)
            if (fTestDirAppeal > fFleeDirAppeal):
                fFleeDirAppeal = fTestDirAppeal
                vFleeDir = vFleeTestDir

        for iAttempt in range(8):
            vFleeTestDir = App.TGPoint3_GetRandomUnitVector()
            fTestDirAppeal = self.CalculateDirectionAppeal(pShip, vFleeTestDir, lpDirectionInfo)
            if (fTestDirAppeal > fFleeDirAppeal):
                fFleeDirAppeal = fTestDirAppeal
                vFleeDir = vFleeTestDir

        vNewHeading = vFleeDir
        bFacingSafe = self.IsDirectionSafe(pShip.GetWorldForwardTG(), lpDirectionInfo)
        fSpeed = 0.0
        if bFacingSafe:
            fSpeed = 0.8
        return (vNewHeading, fSpeed)


    def CalculateDirectionAppeal(self, pShip, vTestDirection, lpDirectionInfo):
        debug(__name__ + ", CalculateDirectionAppeal")
        fOverallAppeal = 0.0
        for (vPosition, vDirection, vVelocity, fBlockedDot, fFavorability,) in lpDirectionInfo:
            fDot = vTestDirection.Dot(vDirection)
            if (fDot >= fBlockedDot):
                fAppeal = fFavorability
                continue
            elif (fDot >= 0):
                try:
                    fAppeal = (fFavorability - (((2.0 * fFavorability) * (fBlockedDot - fDot)) / fBlockedDot))
                except ZeroDivisionError:
                    fAppeal = -fFavorability
            else:
                fAppeal = (((fFavorability * fDot) * 0.5) + (fFavorability * (1.0 + fDot)))
            fOverallAppeal = (fOverallAppeal + (fAppeal * 2.0))
            vVelDir = App.TGPoint3()
            vVelDir.Set(vVelocity)
            vVelDir.Unitize()
            if (vVelDir.SqrLength() > 0.0625):
                fDot = vVelDir.Dot(vTestDirection)
                fAppeal = (((abs(fDot) - 0.5) * 2.0) * fFavorability)
                fOverallAppeal = (fOverallAppeal + fAppeal)
                fDot = vDirection.Dot(vVelocity)
                if 1:
                    vTestPerpendicular = vTestDirection.GetPerpendicularComponent(vVelocity)
                    vDirectionPerpendicular = vDirection.GetPerpendicularComponent(vVelocity)
                    vTestPerpendicular.Unitize()
                    vDirectionPerpendicular.Unitize()
                    fDot = vTestPerpendicular.Dot(vDirectionPerpendicular)
                    fAppeal = (fDot * fFavorability)
                else:
                    fAppeal = -fFavorability
                fOverallAppeal = (fOverallAppeal + fAppeal)
            fAppeal = (pShip.GetWorldForwardTG().Dot(vDirection) * 0.2)
            fOverallAppeal = (fOverallAppeal + fAppeal)

        return fOverallAppeal


    def IsDirectionSafe(self, vTestDirection, lpDirectionInfo):
        debug(__name__ + ", IsDirectionSafe")
        for (vPosition, vDirection, vVelocity, fBlockedDot, fFavorability,) in lpDirectionInfo:
            fDot = vTestDirection.Dot(vDirection)
            if (fDot >= fBlockedDot):
                return 0

        return 1
