import App
import MissionLib


def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/LightDTRomPlasmaCore.tga",
						kCoreColor,
						0.150,
						0.70,
					"data/Textures/Tactical/LightDTRomPlasmaGlow.tga",	
						kGlowColor,
						1.85,
						1.0,
						0.85,
					"data/Textures/Tactical/LightDTRomPlasmaCore.tga",
						kGlowColor,
						40,
						0.2,
						0.05)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(65)

def GetLaunchSound():
	return("LightDTRomPlasma")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Metaplasma Light")

def GetDamage():
	return 600

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
	return 30