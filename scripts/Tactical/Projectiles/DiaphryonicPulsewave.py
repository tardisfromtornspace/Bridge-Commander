import App



def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(140.0 / 255.0, 255.0 / 255.0, 0.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(135.0 / 255.0, 0.0 / 255.0, 249.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(0.0 / 255.0, 190.0 / 255.0, 255.0 / 255.0, 1.0)
    
    pTorp.CreateTorpedoModel(
                        'data/Textures/Tactical/DiaphryonicPulsewaveCore.tga', 
                        kCoreColor, 
                        0.625, 
                        1.2, 
                        'data/Textures/Tactical/DiaphryonicPulsewaveGlow.tga', 
                        kGlowColor, 
                        1.0, 
                        0.5, 
                        0.98, 
                        'data/Textures/Tactical/DiaphryonicPulsewaveFlare.tga', 
                        kFlareColor, 
                        65, 
                        0.5, 
                        0.09)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.45)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)
    return 0


def GetLaunchSpeed():
    return 90


def GetLaunchSound():
    return "DiaphryonicPulsewave"


def GetPowerCost():
    return (20.0)


def GetName():
    return "Diaphryonic Pulsewave"


def GetDamage():
    return 4350.0 * 4


def GetGuidanceLifetime():
    return 35.0


def GetMaxAngularAccel():
    return 1.00
