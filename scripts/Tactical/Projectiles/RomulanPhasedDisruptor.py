import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.007843, 1.0, 0.007843, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.639216, 1.0, 0.639216, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 1.2, 0.1)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.15)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.ROMPHASEDDISRUPTOR)
    return 0


def GetLaunchSpeed():
    return 63.0


def GetLaunchSound():
    return 'Romulan Disruptor'


def GetPowerCost():
    return 30.0


def GetName():
    return 'Phased Disruptor'


def GetDamage():
    return 200.0


def GetGuidanceLifetime():
    return 0.0


def GetMaxAngularAccel():
    return 0.25


def GetLifetime():
    return 10.0
