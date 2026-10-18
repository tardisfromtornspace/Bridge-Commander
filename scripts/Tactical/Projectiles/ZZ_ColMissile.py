# File: Z (Python 1.5)

import App
import trails.ZZPDTrail
import trails.OriBeam

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.1, 0.9, 0.2, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(1.0, 1.0, 0.4, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 0.2, 0.05)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    trails.OriBeam.AddCreationHandler(pTorp, __name__ + '.AttachSmoke')
    return 0


def AttachSmoke(self, pEvent = None):
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return 1
    
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZPDTrail.tga', 4, 4)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZPDTrail.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 1.0, sEmitLife = 2.0, elVar = 0.1, sEffectLifetime = 12.0, leDamp = 0.2, inhVel = 0, sAngleVariance = 360.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), pFunction = trails.ZZPDTrail.DefaultColorKeyFunc)
    return 0


def GetLaunchSpeed():
    return 45.0


def GetLaunchSound():
    return 'ZZMirMiss'


def GetPowerCost():
    return 1.0


def GetName():
    return 'Fighter Missile'


def GetDamage():
    return 60.0


def GetGuidanceLifetime():
    return 12.0


def GetMaxAngularAccel():
    return 0.7


def GetLifetime():
    return 12.0

