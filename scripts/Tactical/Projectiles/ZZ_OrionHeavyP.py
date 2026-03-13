# File: Z (Python 1.5)

import App
import trails.ZZPDTrailY
import trails.OriBeam

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 0.0 / 255.0, 0.8)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 120.0 / 255.0, 0.8)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZBlackCore.tga', kCoreColor, 0.1, 13.0, 'data/Textures/Tactical/ZZBlackGlow.tga', kGlowColor, 10.0, 0.1, 0.6, 'data/textures/Tactical/ZZBlackCore.tga', kGlowColor, 30, 0.2, 1.5)
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
    
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZPDTrailY.tga', 4, 4)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZPDTrailY.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 0.8, sEmitLife = 0.1, elVar = 0.1, sEffectLifetime = 6.0, leDamp = 0.2, inhVel = 0, sAngleVariance = 360.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), pFunction = trails.ZZPDTrailY.DefaultColorKeyFunc)
    return 0


def GetLaunchSpeed():
    return 120.0


def GetLaunchSound():
    return 'DeathPulse'


def GetPowerCost():
    return 5.0


def GetName():
    return 'Orion Heavy Disruptor'


def GetDamage():
    return 200.0


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 0.15


def GetLifetime():
    return 8.0

