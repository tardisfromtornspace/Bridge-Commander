# No damage through shields

# by Sov & SMBW

import App
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib

lModified = []

def ShipCreated(pObject, pEvent):
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
                return

        if App.DamageableObject_IsDamageGeometryEnabled():
                pShip.SetVisibleDamageRadiusModifier(0.0)
                pShip.SetVisibleDamageStrengthModifier(0.0)

                global lModified
                lModified.append(pShip.GetObjID())

def WeaponHit(pObject, pEvent):
        pHit = pEvent.IsHullHit()
        if not pHit == 1:
                return

        pWeaponType = pEvent.GetWeaponType()
        if pWeaponType == pEvent.TRACTOR_BEAM:
                return

        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
                return

        pDamage = pEvent.GetDamage()
        if pDamage <= 0:
                return

        fShieldStats = DS9FXLifeSupportLib.GetShieldPerc(pShip)
        if fShieldStats < 20:
                pShDmg = 1
        else:
                pShDmg = 0

        if not pShDmg:
                if pShip.GetShields().IsOn():
                        global lModified
                        if not pShip.GetObjID() in lModified:
                                lModified.append(pShip.GetObjID())
                                pShip.SetVisibleDamageRadiusModifier(0.0)
                                pShip.SetVisibleDamageStrengthModifier(0.0)

                        pDamageRadius = pEvent.GetRadius()

                        pObjectHitPoint = pEvent.GetObjectHitPoint()
                        HitPoint = App.TGPoint3()
                        HitPoint.SetXYZ(pObjectHitPoint.x, pObjectHitPoint.y, pObjectHitPoint.z)

                        pSet = pShip.GetPropertySet()
                        if not pSet:
                                return

                        pList = pSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
                        if not pList:
                                return

                        pList.TGBeginIteration()
                        for i in range(pList.TGGetNumItems()):
                                pProp = App.SubsystemProperty_Cast(pList.TGGetNext().GetProperty())
                                pSys = pShip.GetSubsystemByProperty(pProp)
                                if not pSys:
                                        continue

                                iCon = pSys.GetCondition()
                                iMax = pSys.GetMaxCondition()

                                if iCon <= 0.0 or iCon >= iMax:
                                        continue

                                if pWeaponType == pEvent.TORPEDO and (iMax - iCon) < (pDamage - 0.01):
                                        continue

                                pSysPos = pSys.GetPosition()

                                vDistance = App.TGPoint3()
                                vDistance.SetXYZ(pSysPos.x, pSysPos.y, pSysPos.z)
                                vDistance.Subtract(HitPoint)

                                if (vDistance.Length() / pShip.GetRadius()) > (pSys.GetRadius() + pDamageRadius):
                                        continue

                                iNewCon = iCon + pDamage

                                if iNewCon > iMax:
                                        iNewCon = iMax

                                pSys.SetCondition(iNewCon)

                        pList.TGDoneIterating()
                        pList.TGDestroy()

                        return 

        if App.DamageableObject_IsDamageGeometryEnabled():
                global lModified
                if pShip.GetObjID() in lModified:
                        pScript = pShip.GetScript()
                        pModule = __import__(pScript)
                        try:
                                kShipStats = pModule.GetShipStats()
                                if kShipStats.has_key('DamageRadMod'):
                                        pShip.SetVisibleDamageRadiusModifier(kShipStats['DamageRadMod'])
                                else:
                                        pShip.SetVisibleDamageRadiusModifier(1.0)
                                if kShipStats.has_key('DamageStrMod'):
                                        pShip.SetVisibleDamageStrengthModifier(kShipStats['DamageStrMod'])
                                else:
                                        pShip.SetVisibleDamageStrengthModifier(1.0)
                        except:
                                pShip.SetVisibleDamageRadiusModifier(1.0)
                                pShip.SetVisibleDamageStrengthModifier(1.0)
                        lModified.remove(pShip.GetObjID())

                        return 