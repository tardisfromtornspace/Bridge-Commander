import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.5, 0.5, 1.0, 1.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.7, 0.7, 1.0, 1.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 1.0, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PULSEDISRUPT)
    return 0


def GetLaunchSpeed():
    return 100.0


def GetLaunchSound():
    return 'Invader Cannon'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Disruptor'


def GetDamage():
    return 300.0


def GetGuidanceLifetime():
    return 0.0


def GetMaxAngularAccel():
    return 0.1


def GetLifetime():
    return 3.0
