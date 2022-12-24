import App

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(104.0 / 255.0, 124.0 / 255.0, 197.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel(
					'data/Textures/Tactical/ZZ_TitanQCORE.tga', 
					kCoreColor, 
					0.2, 3.5, 
					'data/textures/tactical/ZZ_TitanQGLOW.tga', 
					kGlowColor, 
					3.5, 
					0.8, 
					1.0, 
					'data/textures/tactical/ZZHeavyPhotonFlares.tga', 
					kGlowColor, 
					30, 
					0.07, 
					0.4)
   
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    return 0


def GetLaunchSpeed():
    return 120.0


def GetLaunchSound():
    return 'OdysseyClassQuantumTorps'


def GetPowerCost():
    return 0.0


def GetName():
    return 'Quantum'


def GetDamage():
    return 2300.0


def GetGuidanceLifetime():
    return 15.0


def GetMaxAngularAccel():
    return 3.18


def GetLifetime():
    return 20.0