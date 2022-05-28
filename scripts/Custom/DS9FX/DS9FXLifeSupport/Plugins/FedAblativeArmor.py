import App
import Foundation
from Custom.DS9FX.DS9FXLib import DS9FXLifeSupportLib

# Most of these scripts operate under 1 mutator name, but is the actual script of the tech/mod in question present... 
def GetScript():
    try:
        import ftb.Tech.FedAblativeArmor
        pModule = ftb.Tech.FedAblativeArmor
        if hasattr(pModule, "oAblative"):
            bIsInstalled = 1
        else:
            bIsInstalled = 0
    except:
        bIsInstalled = 0
    return bIsInstalled

# Show how can DS9FX check if the mod is active. The code which checks for active mutators is a bit different and supports partial matching.
# I.E. You have a mutator called "Foundation Technologies 4.5", you can simply return "Foundation Technologies". 
def GetMutatorName():
    return "Foundation Technologies"

# The final function must be written manually and be pretty much based on the original mod you wrote, in short you must tell Life Support when it can kill crew members
# pObject and pEvent are params sent by the ET_WEAPON_HIT event
def CanKillCrewMembers(pObject, pEvent):
    try:
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        if not pShip:
            return 1

        pType = DS9FXLifeSupportLib.GetShipType(pShip)
        if not pType:
            return 1

        if Foundation.shipList.has_key(pType):
            fdShip = Foundation.shipList[pType]
            if fdShip:
                if hasattr(fdShip, "dTechs"):
                    pTech = fdShip.dTechs
                    if pTech.has_key("Fed Ablative Armor"):
                        pArmor = pTech["Fed Ablative Armor"]
                        if pArmor.has_key("Plates"):
                            kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
                            lPlates = pArmor["Plates"]
                            pRadius = pEvent.GetRadius()
                            if not pRadius:
                                return 1
                            
                            lArmors = []
                            kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
                            while (1):
                                    pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
                                    if not pSubsystem:
                                            break
                                    if pSubsystem.GetName() in lPlates:
                                            lArmors.append(pSubsystem)
                            pShip.EndGetSubsystemMatch(kIterator)

                            pProtectingPlate = None
                            bPlateDisabled = 0
                            for pPlate in lArmors:
                                vDifference = NiPoint3ToTGPoint3(pPlate.GetPosition())
                                vDifference.Subtract(kPoint)
                                if pRadius + pPlate.GetRadius() > vDifference.Length() and pPlate.GetConditionPercentage() > 0:
                                    pProtectingPlate = pPlate

                            if not pProtectingPlate:
                                return 1
                            if pProtectingPlate.IsDisabled():
                                return 1
                            
                            return 0
        return 1
    except:
        return 1

def NiPoint3ToTGPoint3(p):
    kPoint = App.TGPoint3()
    kPoint.SetXYZ(p.x, p.y, p.z)
    return kPoint
