import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((149.0 / 255.0), (192.0 / 255.0), (76.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/CABorg.tga', kCoreColor, 0.6, 1.0, 'data/Textures/Tactical/borgtorp.tga', kGlowColor, 4.0, 1.8, 3.3, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 12, 1.7, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.2)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
    return 40.0


def GetLaunchSound():
    return 'DGGravimetric'


def GetPowerCost():
    return 10.0


def GetName():
    return 'Mini-Gravimetric'


def GetDamage():
    return 1000.0


def GetGuidanceLifetime():
    return 3.0


def GetMaxAngularAccel():
    return 2.0

