# Nothing out of interest towards regular user and modder

import App
import PulsarFX
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents

bOverflow = 0
pTimer = None

def Start():
    global pTimer, bOverflow

    if not bOverflow:
        pTimer = PulsarMonitor()
    else:
        return

def End():
    PulsarFX.Reset()

class PulsarMonitor:
    def __init__(self):
        global bOverflow
        bOverflow = 1
        self.pTiming = None
        self.pTimer = None
        self.countdown()  
    def countdown(self):
        if not self.pTiming:
            self.pTiming = App.PythonMethodProcess()
            self.pTiming.SetInstance(self)
            self.pTiming.SetFunction("monitor")
            self.pTiming.SetDelay(0.001)
            self.pTiming.SetPriority(App.TimeSliceProcess.CRITICAL)    
            self.pTiming.SetDelayUsesGameTime(1)
        if not self.pTimer:
            self.pTimer = App.PythonMethodProcess()
            self.pTimer.SetInstance(self)
            self.pTimer.SetFunction("damager")
            self.pTimer.SetDelay(15)
            self.pTimer.SetPriority(App.TimeSliceProcess.LOW)    
            self.pTimer.SetDelayUsesGameTime(1)            
    def monitor(self, fTime):
        PulsarFX.Update()
    def damager(self, fTime):
        for k in PulsarFX.dData.keys():
            dSetData = PulsarFX.dData[k]
            sSet = dSetData["Set"]
            iRange = dSetData["RadiationRange"]
            iDamage = dSetData["RadiationDamage"]
            iSun = dSetData["Sun"]

            pSet = App.g_kSetManager.GetSet(sSet)
            if not pSet:
                continue

            pProx = pSet.GetProximityManager()
            if not pProx:
                continue

            pSun = App.Sun_Cast(App.TGObject_GetTGObjectPtr(iSun))
            if not pSun:
                continue

            lDamage = []

            kIter = pProx.GetNearObjects(pSun.GetWorldLocation(), iRange, 1)
            while 1:
                pObject = pProx.GetNextObject(kIter)
                if not pObject:
                    break
                if pObject.IsTypeOf(App.CT_DAMAGEABLE_OBJECT):
                    lDamage.append(pObject.GetObjID())

            pProx.EndObjectIteration(kIter)  
            
            self.damage(lDamage, iDamage)

    def damage(self, lDamage, iDamage):
        if len(lDamage) == 0:
            return 0
        
        for kShip in lDamage:
            pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(kShip))
            if not pShip:
                continue
            pSet = pShip.GetPropertySet()
            if not pSet:
                continue
            pList = pSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
            if not pList:
                continue
            pShields = pShip.GetShields()
            bShieldsDown = 0
            if pShields and pShields.IsOn():
                if not pShields.IsDisabled():
                    for pShield in range(App.ShieldClass.NUM_SHIELDS):
                        iCur = pShields.GetCurShields(pShield)
                        iMax = pShields.GetMaxShields(pShield)
                        iAllowed = int(iMax * 0.01)
                        iAllowed = iAllowed * 2
                        if iCur <= iAllowed:
                            bShieldsDown = 1
                            break
                    if not bShieldsDown:
                        self.processshields(pShields, iDamage)
                        continue

            pHullConOld = pShip.GetHull().GetCondition()

            pList.TGBeginIteration()
            for i in range(pList.TGGetNumItems()):
                pProp = App.SubsystemProperty_Cast(pList.TGGetNext().GetProperty())
                pSys = pShip.GetSubsystemByProperty(pProp)
                if not pSys:
                    continue
                self.processdamage(pShip, pSys, iDamage)

            pList.TGDoneIterating()
            pList.TGDestroy()   

            pHullConNew = pShip.GetHull().GetCondition()
            iHullDamage = pHullConOld - pHullConNew
            if iHullDamage <= 0:
                continue
            DS9FXGlobalEvents.Trigger_Custom_Damage(pShip, iHullDamage)                

    def processshields(self, pShields, iDamage):
        iRnd = int(App.g_kSystemWrapper.GetRandomNumber(iDamage)) + iDamage / 2
        for pShield in range(App.ShieldClass.NUM_SHIELDS):
            iCur = pShields.GetCurShields(pShield)
            iVal = iCur - iRnd
            if iVal <= 0:
                iVal = 0
            pShields.SetCurShields(pShield, iVal)

    def processdamage(self, pShip, pSys, iDamage):        
        iCur = pSys.GetCondition()
        iRnd = int(App.g_kSystemWrapper.GetRandomNumber(iDamage)) + iDamage / 2
        iVal = iCur - iRnd
        if iVal <= 1:
            try:
                pShip.DestroySystem(pSys)
                return 0
            except:
                iVal = 1
        pSys.SetCondition(iVal)  
