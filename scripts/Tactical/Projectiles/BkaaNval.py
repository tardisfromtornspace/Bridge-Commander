import App

def Create(pTorp):

    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(25.0 / 255.0, 25.0 / 255.0, 25.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(100.0 / 255.0, 100.0 / 255.0, 100.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(5.0 / 255.0, 5.0 / 255.0, 5.0 /255.0, 1.0)

    pTorp.CreateTorpedoModel(
    'data/Textures/Tactical/BkaaNvalCore.tga',
                kCoreColor,
                0.8,
                1.5,
    'data/Textures/Tactical/BkaaNvalGlow.tga',
                kGlowColor,
                2.5,
                1.5,
                4.0,
    'data/Textures/Tactical/TorpedoFlares.tga',
                kFlareColor,
                200,
                0.750,
                1.75)

    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.1)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())

    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.POSITRON)

    return (0)

def GetLaunchSpeed():
    return 105.0

def GetLaunchSound():
    return 'BkaaNval'

def GetPowerCost():
    return 100000.0

def GetName():
    return 'Bkaa Nval'

def GetDamage():
    return 5000.0

def GetGuidanceLifetime():
    return 7.0

def GetMaxAngularAccel():
    return 1.0

try:
	import FoundationTech
	import ftb.Tech.BkaaNvalProjectile
	oFire = ftb.Tech.BkaaNvalProjectile.BkaaNvalProjectileDef('BkaaNval Projectile')
	FoundationTech.dYields[__name__] = oFire
except:
	pass
