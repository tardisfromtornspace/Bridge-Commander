import App

def Create(pTorp):

    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(165.0 / 255.0, 40.0 / 255.0, 0.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 185.0 / 255.0, 20.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(80.0 / 255.0, 0.0 / 255.0, 165.0 /255.0, 1.0)

    pTorp.CreateTorpedoModel(
    'data/Textures/Tactical/TyphoonCore.tga',
                kCoreColor,
                0.6,
                1.5,
    'data/Textures/Tactical/TorpedoGlow.tga',
                kGlowColor,
                2.5,
                1.5,
                5.0,
    'data/Textures/Tactical/TorpedoFlares.tga',
                kFlareColor,
                55,
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
    return 75.0

def GetLaunchSound():
    return 'InvertedEnergyDestroyer'

def GetPowerCost():
    return 10.0

def GetName():
    return 'Energy Destroyer'

def GetDamage():
    return 25000.0

def GetGuidanceLifetime():
    return 10.0

def GetMaxAngularAccel():
    return 3.0

# Sets the percentage of shield damage the torpedo will do
def GetPercentage():
	return 0.2

try:
	modEnergyDiffusing = __import__("Custom.Techs.EnergyDiffusing")
	if(modEnergyDiffusing):
		modEnergyDiffusing.oEnergyDiffusing.AddTorpedo(__name__, GetPercentage())
except:
	print "Energy Diffusing script not installed, or you are missing Foundation Tech"

def WeaponFired(pObject, pEvent):
	return