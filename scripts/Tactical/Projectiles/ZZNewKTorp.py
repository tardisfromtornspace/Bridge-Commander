# File: Z (Python 1.5)

import App
import traceback

trailsWork = 0
try:
    import trails.ZZNewKPhotonTrail
    import trails.OriBeam
    trailsWork = 1
except:
    trailsWork = 0
    print(__name__, " will not load effects because dependencies are missing:")
    traceback.print_exc()

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 86.0 / 255.0, 69.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 130.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 71.0 / 255.0, 42.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZST6PhotonCore.tga', kCoreColor, 0.06, 1.4, 'data/Textures/Tactical/ZZST6PhotonGlow.tga', kGlowColor, 3.0, 0.25, 0.45, 'data/Textures/Tactical/ZZST6PhotonCore.tga', kGlowColor, 10, 1.0, 0.5)
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
    
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZPhotonTrail.tga', 4, 4)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZPhotonTrail.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 0.8, sEmitLife = 0.025, elVar = 0.1, sEffectLifetime = 10.0, leDamp = 0.2, sAngleVariance = 360.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), sDrawOldToNew = 0, inhVel = 0, pFunction = trails.ZZNewKPhotonTrail.DefaultColorKeyFunc)
    return 0


def GetLaunchSpeed():
    return 19.0


def GetLaunchSound():
    return 'KlingonTMP'


def GetPowerCost():
    return 20.0


def GetName():
    return 'Photon'


def GetDamage():
    return 800.0


def GetGuidanceLifetime():
    return 9.0


def GetMaxAngularAccel():
    return 0.14


def GetLifetime():
    return 20.0

