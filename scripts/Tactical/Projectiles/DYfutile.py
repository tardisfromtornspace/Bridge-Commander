import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.0, 0.0, 0.0, 0.0)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.0, 0.0, 0.0, 0.0)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 0.0, 0.0)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
    return 15.0


def GetLaunchSound():
    return 'DYfutile'


def GetPowerCost():
    return 5.0


def GetName():
    return 'DYfutile'


def GetDamage():
    return 0.01


def GetGuidanceLifetime():
    return 0.0


def GetMaxAngularAccel():
    return 0.125


def GetLifetime():
    return 16.0


