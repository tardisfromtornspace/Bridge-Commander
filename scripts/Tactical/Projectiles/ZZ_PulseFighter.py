# File: Z (Python 1.5)

import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(1.0, 0.4, 1e-006, 0.0005)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(1.0, 1.0, 0.7, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 0.5, 0.07)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.15)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.DISRUPTOR)
    return 0


def GetLaunchSpeed():
    return 75.0


def GetLaunchSound():
    return 'ZZ_DefiantPulse'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Pulse Phaser'


def GetDamage():
    return 80.0


def GetGuidanceLifetime():
    return 0.5


def GetMaxAngularAccel():
    return 0.08

