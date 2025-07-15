# File: Z (Python 1.5)

import App
import MissionLib

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(41.0 / 255.0, 118.0 / 255.0, 54.0 / 255.0, 0.1)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 0.2)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 0.2)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZ_DeathCore.tga', kCoreColor, 0.1, 4.5, 'data/Textures/Tactical/ZZ_DeathGlow.tga', kGlowColor, 3.0, 0.25, 0.4, 'data/Textures/Tactical/ZZ_DeathFlares.tga', kFlareColor, 35, 0.4, 1.0)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 65.0


def GetLaunchSound():
    return 'DeathPhoton'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Borg Pulse'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 0.1


def GetLifetime():
    return 10.0

