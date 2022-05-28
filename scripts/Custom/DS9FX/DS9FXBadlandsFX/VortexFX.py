# Simulates Vortex FX seen in Star Trek

# by Sov

# Imports
import App
import MissionLib
from Custom.DS9FX import DS9FXmain
from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
from Custom.DS9FX.DS9FXBadlandsFX import ExplosionGFX, RotationFX
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

# Vars
bOverflow = 0
pTimer = None

# Functions
def StartUpTimingProcess():
    global pTimer, bOverflow

    if not bOverflow:
        pTimer = BadlandsMonitor()
    else:
        return

class BadlandsMonitor:
    def __init__(self):
        global bOverflow
        bOverflow = 1
        self.pTiming = None
        sVortex = "Vortex "
        self.lVortex = []
        for i in range(57):
            s = sVortex + str(i)
            self.lVortex.append(s)
        self.iCounter = 0
        self.countdown()

    def countdown(self):
        if not self.pTiming:
            self.pTiming = App.PythonMethodProcess()
            self.pTiming.SetInstance(self)
            self.pTiming.SetFunction("updater")
            self.pTiming.SetDelay(10)
            self.pTiming.SetPriority(App.TimeSliceProcess.LOW)

    def updater(self, fTime):
        reload(DS9FXSavedConfig)
        if not DS9FXSavedConfig.BadlandsDamageFX == 1:
            return 0         

        pSet = App.g_kSetManager.GetSet("DS9FXBadlands1")
        if not pSet:
            return 0

        pProx = pSet.GetProximityManager()
        if not pProx:
            return 0

        lDamage = []

        for kShip in pSet.GetClassObjectList(App.CT_DAMAGEABLE_OBJECT):
            if not kShip.GetName() in self.lVortex:
                continue
            pShip = App.ShipClass_GetObject(pSet, kShip.GetName())
            if not pShip:
                continue
            kIter = pProx.GetNearObjects(pShip.GetWorldLocation(), 500, 1)
            while 1:
                pObject = pProx.GetNextObject(kIter)
                if not pObject:
                    break
                if pObject.IsTypeOf(App.CT_DAMAGEABLE_OBJECT):
                    if not pObject.GetName() in self.lVortex:
                        lDamage.append(pObject.GetObjID())

            pProx.EndObjectIteration(kIter)

        self.iCounter = self.iCounter + 1
        if self.iCounter > 3:
            self.iCounter = 0

        self.damage(lDamage)

    def damage(self, lDamage):
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
                        self.processshields(pShields)
                        continue

            pHullConOld = pShip.GetHull().GetCondition()

            pList.TGBeginIteration()
            for i in range(pList.TGGetNumItems()):
                pProp = App.SubsystemProperty_Cast(pList.TGGetNext().GetProperty())
                pSys = pShip.GetSubsystemByProperty(pProp)
                if not pSys:
                    continue
                self.processdamage(pShip, pSys)

            pList.TGDoneIterating()
            pList.TGDestroy()

            if self.iCounter == 3:
                self.seteffects(pShip)

            pHullConNew = pShip.GetHull().GetCondition()
            iHullDamage = pHullConOld - pHullConNew
            if iHullDamage <= 0:
                continue
            DS9FXGlobalEvents.Trigger_Custom_Damage(pShip, iHullDamage)

    def processshields(self, pShields):
        for pShield in range(App.ShieldClass.NUM_SHIELDS):
            iMax = pShields.GetMaxShields(pShield)
            iDmg = int(iMax * 0.01)
            iCur = pShields.GetCurShields(pShield)
            iVal = iCur - iDmg
            if iVal <= 0:
                iVal = 0
            pShields.SetCurShields(pShield, iVal)

    def processdamage(self, pShip, pSys):        
        iMax = pSys.GetMaxCondition()
        iCur = pSys.GetCondition()
        RandNo = int(App.g_kSystemWrapper.GetRandomNumber(99)) + 1 # Smbw: Added random factor
        RandFactor = 0.01 * (RandNo / 24) # 24% Chance for: No dmg, normal dmg, double dmg, triple dmg | 4% for 4x dmg
        if RandFactor > 0:
            iDmg = int(iMax * RandFactor)
            iVal = iCur - iDmg
            if iVal <= 1:
                try:
                    pShip.DestroySystem(pSys)
                    return 0
                except:
                    iVal = 1
            pSys.SetCondition(iVal)

    def seteffects(self, pShip):
        iNum = App.g_kSystemWrapper.GetRandomNumber(9) + 1
        ExplosionGFX.StartGFX()
        for i in range(iNum):
            ExplosionGFX.CreateGFX(pShip)
        RotationFX.Rotate(pShip)
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
            return 0
        pID = pPlayer.GetObjID()
        if pShip.GetObjID() == pID:
            App.g_kSoundManager.PlaySound("DS9FXExplosion")
