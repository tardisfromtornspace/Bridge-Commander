import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((200.0 / 255.0), (200.0 / 255.0), (255.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((150.0 / 255.0), (150.0 / 255.0), (255.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.7, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 4.0, 3.3, 3.3, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 60, 1.7, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0


def GetLaunchSpeed():
    return 75.0


def GetLaunchSound():
    return '10026Pulse'


def GetPowerCost():
    return 10.0


def GetName():
    return("1 V'GER PLASMA")


def GetDamage():
    return 7500.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.6

