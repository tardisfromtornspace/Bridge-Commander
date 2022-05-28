import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (0.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((255.0 / 255.0), (153.0 / 255.0), (0.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((255.0 / 255.0), (255.0 / 128.0), (0.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.2, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 8.0, 0.5, 0.9, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 15, 0.05, 0.27)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.19)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
    return 40.0


def GetLaunchSound():
    return 'Sona Torpedo'


def GetPowerCost():
    return 25.0


def GetName():
    return 'Plasma Torpedo'


def GetDamage():
    return 1000.0


def GetGuidanceLifetime():
    return 8.5


def GetMaxAngularAccel():
    return 0.5
