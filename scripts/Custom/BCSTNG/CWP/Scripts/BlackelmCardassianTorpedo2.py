import App
def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (0.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((255.0 / 255.0), (153.0 / 255.0), (0.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((255.0 / 255.0), (255.0 / 128.0), (0.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel(
                'Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga',
                kCoreColor,
                0.2,
                1.0,
                'Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga', 
                kGlowColor, 
                8.0, 
                0.25, 
                0.45,
                'Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga', 
                kFlareColor, 
                2, 
                0.45, 
                0.9)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.19)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0

def GetLaunchSpeed():
    return 30.0


def GetLaunchSound():
    return 'blackelmcardassiantorpedo2'


def GetPowerCost():
    return 25.0


def GetName():
    return 'Card Adv Photon'


def GetDamage():
    return 800.0


def GetGuidanceLifetime():
    return 8.5


def GetMaxAngularAccel():
    return 0.35
