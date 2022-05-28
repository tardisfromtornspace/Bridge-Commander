import App
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 150.0, 40.0 / 50.0, 40.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TNGGlow.tga",
					kCoreColor, 
					0.3,
					6.0,	 
					"data/Textures/Tactical/TNGGlow.tga", 
					kGlowColor,
					2.3,	
					0.9,	 
					0.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					3,		
					0.3,		
					0.1)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)
	return(0)

def GetLaunchSpeed():
	return(40)

def GetLaunchSound():
	return("blackelmtype9photon")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Type 9 Photon")

def GetDamage():
	return 900.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.4
