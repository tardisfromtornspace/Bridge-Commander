# File: Z (Python 1.5)

import App
import trails.ZZPDTrailY
import trails.OriBeam

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(1.0, 0.8, 0.4, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(1.0, 0.98, 0.7, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 0.3, 0.05)
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
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZPDTrailY.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 1.0, sEmitLife = 0.25, elVar = 0.1, sEffectLifetime = 25.0, leDamp = 0.2, inhVel = 0, sAngleVariance = 180.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), pFunction = trails.ZZPDTrailY.DefaultColorKeyFunc)

    return 0


def GetLaunchSpeed():
    return 10.0


def GetLaunchSound():
    return 'ZZKzintiSuper'


def GetPowerCost():
    return 5.0


def GetName():
    return 'Super Weapon'


def GetDamage():
    return 4000.0


def GetGuidanceLifetime():
    return 30.0


def GetMaxAngularAccel():
    return 0.2


def GetLifetime():
    return 30.0

import traceback

try:
    import FoundationTech
    import ftb.Tech.SolidProjectiles
    oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {
        'sModel': 'ZZMirakWeap',
        'sScale': 1.5,
        'sShield': 0,
        'sCollide': 3,
        'sX': 0,
        'sY': 0.6,
        'sZ': 0,
        'sShipRmOrDeath': 1,
        'sHideProj': 0,
        'sTargetable': 1,
        'LeftoverDetonation': 0.001 })
    FoundationTech.dOnFires[__name__] = oFire
    FoundationTech.dYields[__name__] = oFire
except:
    print 'Error with firing solid projectile fix'
    traceback.print_exc()

