import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(50.0 / 255.0, 50.0 / 255.0, 100.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(255.0 / 255.0, 81.0 / 255.0, 255.0 / 255.0, 1.000000)
    
    
    pTorp.CreateTorpedoModel(
        			'data/Textures/Tactical/ZZ_BreenCore.tga', #PoleronCore
           			kCoreColor, 
              		1.2, 
                	1.0, 
                 	'data/Textures/Tactical/ZZQuantumGlow.tga', #TorpedoGlow
                  	kGlowColor, 
                   	1.0, 
                    0.8, 
                    0.9, 
                    'data/Textures/Tactical/TorpedoFlares.tga', 
                    kFlareColor, 
                    64, 
                    0.6, 
                    0.15)
    
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.8)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)
    return 0


def GetLaunchSpeed():
    return (70.0)


def GetLaunchSound():
    return ('TetryonSlicingTorp')


def GetPowerCost():
    return (10.0)


def GetName():
    return ('Tetryon Slicing Torp')


def GetDamage():
    return (5500.0 * 4.2)


def GetGuidanceLifetime():
    return (20.0)


def GetMaxAngularAccel():
    return (0.8)
