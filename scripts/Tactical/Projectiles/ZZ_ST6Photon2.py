import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((200.0 / 255.0), (0.0 / 255.0), (0.0 / 255.0), 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (200.0 / 255.0), (0.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZST6PhotonCore.tga', kCoreColor, 0.05, 1.2, 'data/textures/tactical/ZZST6PhotonGlow.tga', kGlowColor, 3.0, 0.35, 0.6, 'data/textures/tactical/ZZST6PhotonFlares.tga', kGlowColor, 8, 0.5, 0.4)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 19.0


def GetLaunchSound():
    return 'ZZ_ST6Photon'


def GetPowerCost():
    return 20.0


def GetName():
    return 'Photon'


def GetDamage():
    return 600.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 1.55


def GetLifetime():
    return 20.0