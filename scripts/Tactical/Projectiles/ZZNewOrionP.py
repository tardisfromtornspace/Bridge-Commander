# File: Z (Python 1.5)

import App
import trails.ZZPDTrailY
import trails.OriBeam

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(1.0, 0.75, 0.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(1.0, 0.0, 0.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(1.0, 0.0, 0.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZCore6bw.tga', kCoreColor, 0.2, 10.0, 'data/Textures/Tactical/ZZCore1bw.tga', kGlowColor, 6.0, 0.2, 0.4, 'data/textures/tactical/ZZCore6bw.tga', kFlareColor, 6, 0.25, 3.0)
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
    
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZPhotonTrailbw.tga', 4, 4)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZPhotonTrailbw.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 0.5, sEmitLife = 0.035, elVar = 0.1, sEffectLifetime = 10.0, leDamp = 0.2, inhVel = 0, sAngleVariance = 360.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), pFunction = trails.ZZPDTrailY.DefaultColorKeyFunc)
    return 0


def GetLaunchSpeed():
    return 110.0


def GetLaunchSound():
    return 'ZZNewOrion'


def GetPowerCost():
    return 1.0


def GetName():
    return 'Orion Disruptor'


def GetDamage():
    return 100.0


def GetGuidanceLifetime():
    return 0.0


def GetMaxAngularAccel():
    return 0.0


def GetLifetime():
    return 10.0

