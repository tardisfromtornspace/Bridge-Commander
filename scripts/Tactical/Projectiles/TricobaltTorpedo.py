# Source Generated with Decompyle++
# File: TricobaltTorpedo.pyc (Python 1.5)

import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(175.0 / 255.0, 224.0 / 255.0, 239.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(48.0 / 255.0, 80.0 / 255.0, 128.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.2, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 0.3, 0.6, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, 12, 0.5, 0.4)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(2.0)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp as Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.TRICOBALT)
    return 0


def GetLaunchSpeed():
    return 15.0


def GetLaunchSound():
    return 'TricobaltTorpedo'


def GetPowerCost():
    return 500.0


def GetName():
    return 'TricobaltTorpedo'


def GetDamage():
    return 3500.0


def GetGuidanceLifetime():
    return 2.0


def GetMaxAngularAccel():
    return 0.1