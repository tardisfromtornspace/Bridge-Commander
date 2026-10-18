# File: Z (Python 1.5)

import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 94.0 / 255.0, 0.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 200.0 / 255.0, 0.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZST6PhotonCore.tga', kCoreColor, 0.3, 1.2, 'data/Textures/Tactical/ZZST6PhotonGlow.tga', kGlowColor, 3.0, 0.5, 0.8, 'data/Textures/Tactical/ZZST6PhotonFlares.tga', kGlowColor, 12, 0.2, 0.2)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 30.0


def GetLaunchSound():
    return 'ZZ_ProtonTorp'


def GetPowerCost():
    return 5.0


def GetName():
    return 'Proton'


def GetDamage():
    return 150.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.3


def GetLifetime():
    return 20.0

