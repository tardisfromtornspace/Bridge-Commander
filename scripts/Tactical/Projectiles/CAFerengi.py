import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(1.0 / 1.0, 1.0 / 1.0, 1.0 / 1.0, 1.000000)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/TorpedoCore.tga', kCoreColor, 0.2, 1.0, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 8.0, 0.5, 0.9, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, 30, 0.2, 0.4)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.19)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
    return 30.0


def GetLaunchSound():
    return 'Cardassian Torpedo'


def GetPowerCost():
    return 25.0


def GetName():
    return 'Photon'


def GetDamage():
    return 300.0


def GetGuidanceLifetime():
    return 0.5


def GetMaxAngularAccel():
    return 0.6
