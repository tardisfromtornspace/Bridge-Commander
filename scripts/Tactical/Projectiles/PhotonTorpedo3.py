import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 155.0 / 255.0, 128.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/CAPhoton.tga', kCoreColor, 0.6, 0.3, 'data/Textures/Tactical/TorpedoGlow.tga', kGlowColor, 2.0, 0.3, 0.3, 'data/Textures/Tactical/TorpedoFlares.tga', kGlowColor, 10, 0.1, 0.6)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.14)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON3)
    return 0


def GetLaunchSpeed():
    return 30.0


def GetLaunchSound():
    return 'FedPulsePhoton'


def GetPowerCost():
    return 30.0


def GetName():
    return 'Photon'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 15.0


def GetMaxAngularAccel():
    return 1.0

