# File: Z (Python 1.5)

import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(219.0 / 255.0, 140.0 / 255.0, 14.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(252.0 / 255.0, 255.0 / 255.0, 171.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 85.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.1, 15.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 5.0, 0.01, 0.1, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 40, 0.02, 0.5)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.15)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON1)
    return 0


def GetLaunchSpeed():
    return 35.0


def GetLaunchSound():
    return 'ZZRepTorp'


def GetPowerCost():
    return 30.0


def GetName():
    return 'Cobra Antimatter'


def GetDamage():
    return 250.0


def GetGuidanceLifetime():
    return 3.0


def GetMaxAngularAccel():
    return 0.16

