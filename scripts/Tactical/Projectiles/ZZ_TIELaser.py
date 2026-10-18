# File: Z (Python 1.5)

import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.007843, 1.0, 0.007843, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.639216, 1.0, 0.639216, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 1.5, 0.08)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.DISRUPTOR)
    return 0


def GetLaunchSpeed():
    return 80.0


def GetLaunchSound():
    return 'ZZTIE'


def GetPowerCost():
    return 0.0


def GetName():
    return 'Laser'


def GetDamage():
    return 24.0


def GetGuidanceLifetime():
    return 1.0


def GetMaxAngularAccel():
    return 0.125


def GetLifetime():
    return 10.0

