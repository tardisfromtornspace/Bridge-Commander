import App
def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((255.0 / 255.0), (255.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((25.0 / 255.0), (25.0 / 255.0), (50.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((50.0 / 255.0), (50.0 / 255.0), (100.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel(
                                "Scripts/Custom/BCSTNG/CWP/Textures/BlackelmtorpedoCore.tga",
                                kCoreColor,
                                0.2,
                                1.2,
                                "Scripts/Custom/BCSTNG/CWP/Textures/BlackelmtorpedoGlow.tga",
                                kGlowColor,
                                3.0,
                                0.3,
                                0.4,
                                "Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
                                kFlareColor,
                                0,
                                0.15,
                                0.3)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.14)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return (0)

def GetLaunchSpeed():
    return (40.0)

def GetLaunchSound():
    return ("blackelmtype2quantum")

def GetPowerCost():
    return (10.0)

def GetName():
    return ("Quantum")

def GetDamage():
    return 1000.0

def GetGuidanceLifetime():
    return 8.0

def GetMaxAngularAccel():
    return 0.4

