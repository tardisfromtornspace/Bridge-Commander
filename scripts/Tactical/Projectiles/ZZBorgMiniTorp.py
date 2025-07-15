# File: Z (Python 1.5)

import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(41.0 / 255.0, 118.0 / 255.0, 54.0 / 255.0, 0.1)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 0.0 / 255.0, 0.2)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(41.0 / 255.0, 118.0 / 255.0, 54.0 / 255.0, 0.2)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZ_FMPACore.tga', kCoreColor, 0.4, 4.0, 'data/Textures/Tactical/ZZ_FMPAGlow1.tga', kGlowColor, 10.0, 0.1, 0.2, 'data/Textures/Tactical/ZZ_FMPAFlares.tga', kCoreColor, 20, 0.15, 0.5)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.15)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 30.0


def GetLaunchSound():
    return 'ZZBorgTorp'


def GetPowerCost():
    return 20.0


def GetName():
    return 'Borg Antimatter'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 12.0


def GetMaxAngularAccel():
    return 0.98

