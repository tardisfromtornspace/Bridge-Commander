# File: Z (Python 1.5)

import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(200.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 0.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 165.0 / 255.0, 0.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZOrionCore.tga', kCoreColor, 0.2, 14.2, 'data/Textures/Tactical/ZZOrionGlow.tga', kGlowColor, 15.0, 0.2, 0.5, 'data/Textures/Tactical/ZZOrionCore.tga', kFlareColor, 45, 0.09, 0.4)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
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
    return 'Orion Photon'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.15


def GetLifetime():
    return 20.0

