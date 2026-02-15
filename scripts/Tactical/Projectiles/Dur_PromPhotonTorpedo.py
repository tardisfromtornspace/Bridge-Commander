# File: D (Python 1.5)

import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.1, 1.2, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 1.5, 0.2, 0.25, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, 4, 0.25, 0.3)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.13)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 19.0


def GetLaunchSound():
    return 'Photon Torpedo'


def GetPowerCost():
    return 20.0


def GetName():
    return 'Photon'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 6.0


def GetMaxAngularAccel():
    return 0.95

