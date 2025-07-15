# File: Z (Python 1.5)

import App
import MissionLib

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(41.0 / 255.0, 118.0 / 255.0, 54.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZ_DeathCore.tga', kCoreColor, 0.1, 0.1, 'data/Textures/Tactical/ZZ_DeathGlow.tga', kGlowColor, 0.1, 0.1, 0.1, 'data/Textures/Tactical/ZZ_DeathFlares.tga', kFlareColor, 1, 0.1, 0.1)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.01)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 1.0


def GetLaunchSound():
    return 'ZZWeAre'


def GetPowerCost():
    return 1.0


def GetName():
    return 'We Are'


def GetDamage():
    return 0.001


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 0.1


def GetLifetime():
    return 15.0

