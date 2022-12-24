import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(253.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 0.0 / 139.0, 1.0)
    pTorp.CreateTorpedoModel(
                    'data/Textures/Tactical/ZZ_FCPhotonCore.tga', 
                    kCoreColor, 
                    0.06, 
                    4.2, 
                    'data/textures/tactical/ZZ_FCPhotonGlow.tga', 
                    kGlowColor, 
                    3.0, 
                    0.5, 
                    0.8, 
                    'data/textures/tactical/ZZ_FCPhotonFlares.tga', 
                    kGlowColor, 
                    8, 
                    0.17, 
                    0.4)

    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 100.0


def GetLaunchSound():
    return 'SCIFIPhotonTorp'


def GetPowerCost():
    return 20.0


def GetName():
    return 'ADVPhoton'


def GetDamage():
    return 1850.0


def GetGuidanceLifetime():
    return 13.0


def GetMaxAngularAccel():
    return 3.16


def GetLifetime():
    return 20.0