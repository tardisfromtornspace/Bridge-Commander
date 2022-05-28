import App

def Create(pTorp):
    kOuterShellColor = App.TGColorA()
    kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 1.000000)
    kOuterCoreColor = App.TGColorA()
    kOuterCoreColor.SetRGBA(0.588235, 1.000000, 0.588235, 1.000000)
    pTorp.CreateDisruptorModel(kOuterShellColor, kOuterCoreColor, 0.0, 0.02)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(3.99)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PULSEDISRUPT)
    return 0


def GetLaunchSpeed():
    return 20.0


def GetLaunchSound():
    return 'Photon Torpedo'


def GetPowerCost():
    return 500.0


def GetName():
    return 'PM6L Cannon'


def GetDamage():
    return 500.0


def GetGuidanceLifetime():
    return 900.0


def GetMaxAngularAccel():
    return 4.0


def GetLifetime():
    return 8.0

