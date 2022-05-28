import App

def Create(pTorp):

    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(254.0 / 255.0, 254.0 / 255.0, 254.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(0.0 / 255.0, 185.0 / 255.0, 17.0 / 255.0, 1.000000)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(88.0 / 255.0, 193.0 / 255.0, 147.0 / 255.0, 1.000000)

    pTorp.CreateTorpedoModel("data/Textures/Tactical/JLH03.tga", kCoreColor, 0.2, 7.5,
                             "data/Textures/Tactical/JLH05.tga", kGlowColor, 10.0, 0.3, 0.4,                                                      "data/Textures/Tactical/TyphoonFlare.tga", kFlareColor, 50, 0.2, 2.0)


    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return (0)


def GetLaunchSpeed():
    return 20.0


def GetLaunchSound():
    return 'ftsHyperon'


def GetPowerCost():
    return 30.0


def GetName():
    return 'Typhoon Torpedo'


def GetDamage():
    return 1000.0


def GetGuidanceLifetime():
    return 8.0


def GetMaxAngularAccel():
    return 0.15

