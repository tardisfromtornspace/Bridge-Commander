import App
import string

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((150.0 / 255.0), (150.0 / 255.0), (255.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((150.0 / 255.0), (150.0 / 255.0), (255.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((150.0 / 255.0), (150.0 / 255.0), (255.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/Digitizer.tga', kCoreColor, 0.7, 1.0, 'data/Textures/Tactical/Digitizer.tga', kGlowColor, 4.0, 3.3, 3.3, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 60, 1.15, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(200.0)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHASEDPLASMA)
    return 0


def GetLaunchSpeed():
    return 75.0


def GetLaunchSound():
    return("SubspaceDigitizer")


def GetPowerCost():
    return 10.0


def GetName():
    return("Subspace Digitizer")


def GetDamage():
    return 20000.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.75

try:
	modDigitizerTorp = __import__("Custom.Techs.DigitizerTorp")
	if(modDigitizerTorp):
		modDigitizerTorp.oDigitizerTorp.AddTorpedo(__name__)
except:
	print "Digitizer Torpedo script not installed, or you are missing Foundation Tech"