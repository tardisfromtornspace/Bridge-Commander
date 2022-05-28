import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/PoleronCore.tga', kCoreColor, 0.03, 1.0, 'data/Textures/Tactical/PoleronCore.tga', kGlowColor, 1.0, 0.03, 0.4, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 44, 0.01, 0.1)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0


def GetLaunchSpeed():
    return 23.8


def GetLaunchSound():
    return 'Quantum Torpedo'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Borg Torpedo'


def GetDamage():
    return 1300.0


def GetGuidanceLifetime():
    return 100.0


def GetMaxAngularAccel():
    return 3.0

