# File: Z (Python 1.5)

import App
import MissionLib

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(217.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 0.1)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 0.1)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 0.1)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZBorgCore.tga', kCoreColor, 0.5, 17.5, 'data/Textures/Tactical/ZZBorgGlow.tga', kGlowColor, 12.0, 0.2, 0.8, 'data/Textures/Tactical/ZZBorgCore.tga', kFlareColor, 30, 0.3, 0.5)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 80.0


def GetLaunchSound():
    return 'ZZBorgSpatial'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Borg Spatial'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 0.1


def GetLifetime():
    return 6.0


def GetRepulsionForce():
    return 0.001


def GetRotationalForce():
    return 50


def TargetHit(pObject, pEvent):
    pShip = App.ShipClass_Cast(pEvent.GetDestination())
    if pShip == None:
        return None

    targetID = pShip.GetObjID()
    if targetID == None or targetID == App.NULL_ID:
        return None

    pShip2 = App.ShipClass_GetObjectByID(None, targetID)
    if (pShip2==None):
        return None

    if pShip.IsDead() or pShip.IsDying():
        return None
    
    vNiWorldHitPoint = pEvent.GetWorldHitPoint()
    vWorldHitPoint = App.TGPoint3()
    vWorldHitPoint.SetXYZ(vNiWorldHitPoint.x, vNiWorldHitPoint.y, vNiWorldHitPoint.z)
    MissionLib.SetRandomRotation(pShip, GetRotationalForce())
    vVelocity = pShip.GetWorldLocation()
    vVelocity.Subtract(vWorldHitPoint)
    vVelocity.Unitize()
    vVelocity.Scale(GetRepulsionForce())
    pShip.SetVelocity(vVelocity)
    return None


def WeaponFired(pObject, pEvent):
    return None

