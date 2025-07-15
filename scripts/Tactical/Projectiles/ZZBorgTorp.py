# File: Z (Python 1.5)

import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(41.0 / 255.0, 118.0 / 255.0, 54.0 / 255.0, 0.1)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 0.2)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(41.0 / 255.0, 118.0 / 255.0, 54.0 / 255.0, 0.2)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZ_FMPACore.tga', kCoreColor, 0.35, 6.0, 'data/Textures/Tactical/ZZ_FMPAGlow1.tga', kGlowColor, 8.0, 0.5, 0.9, 'data/Textures/Tactical/ZZ_FMPAFlares.tga', kCoreColor, 50, 0.7, 0.8)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.15)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 35.0


def GetLaunchSound():
    return 'ZZBorgTorp'


def GetPowerCost():
    return 20.0


def GetName():
    return 'Borg Drainer'


def GetDamage():
    return 0.00001


def GetGuidanceLifetime():
    return 7.0


def GetMaxAngularAccel():
    return 0.95


def GetMinDamage():
    return 240


def GetPercentage():
    return 0.2


def TargetHit(pObject, pEvent):
    pTarget = App.ShipClass_Cast(pEvent.GetDestination())

    if pTarget == None:
        return None

    targetID = pTarget.GetObjID()
    if targetID == None or targetID == App.NULL_ID:
        return None

    pShip2 = App.ShipClass_GetObjectByID(None, targetID)
    if (pShip2==None):
        return None

    if pTarget.IsDead() or pTarget.IsDying():
        return None

    pShields = pTarget.GetShields()
    if not pShields:
        return None

    MinYield = GetMinDamage()
    Percentage = GetPercentage()

    for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
        pShieldStatus = pShields.GetCurShields(ShieldDir)
        pShieldChunk = pShields.GetMaxShields(ShieldDir) * Percentage
        if MinYield > pShieldChunk:
            pShieldChunk = MinYield
        
        if pShieldStatus <= pShieldChunk:
            pShieldStatus = 0
        
        pShields.SetCurShields(ShieldDir, pShieldStatus - pShieldChunk)
    
    return None


def WeaponFired(pObject, pEvent):
    return None

