import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 5.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(400.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 5.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(850.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 5.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/StreamedPlasmaCore.tga",
					kCoreColor,
					0.4,
					1.2,
					"data/Textures/Tactical/StreamedPlasmaGlow.tga",
					kGlowColor,
					10.0,
					0.01,
					0.5,
					"data/Textures/Tactical/StreamedPlasmaFlare.tga",
					kFlareColor,
					40,
					0.98,
					0.5)

	pTorp.SetDamage(GetDamage())
	pTorp.SetDamageRadiusFactor(0.16)
	pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
	pTorp.SetMaxAngularAccel(GetMaxAngularAccel())

	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("MHeavyGrav")

def GetPowerCost():
	return(100.0)

def GetName():
	return("M Heavy Gravimetric")

def GetDamage():
	return 5500.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 0.35
