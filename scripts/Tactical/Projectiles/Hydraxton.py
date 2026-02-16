import App



def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(54.0 / 255.0, 255.0 / 255.0, 30.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(81.0 / 255.0, 255.0 / 255.0, 249.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(110.0 / 255.0, 245.0 / 255.0, 255.0 / 255.0, 1.0)
    
    pTorp.CreateTorpedoModel(
                        'data/Textures/Tactical/Hydraxton.tga', 
                        kCoreColor, 
                        0.61, 
                        1.4, 
                        'data/Textures/Tactical/TriphasicRadionGlow.tga', 
                        kGlowColor, 
                        1.0, 
                        0.4, 
                        0.98, 
                        'data/Textures/Tactical/ZZ_TitanQCORE.tga', 
                        kFlareColor, 
                        45, 
                        0.8, 
                        0.09)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.49)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
    return 100


def GetLaunchSound():
    return "Hydraxton"


def GetPowerCost():
    return (20.0)


def GetName():
    return "Hydraxton"


def GetDamage():
    return 16516.4 #4129.1


def GetGuidanceLifetime():
    return 40.0


def GetMaxAngularAccel():
    return 0.94
