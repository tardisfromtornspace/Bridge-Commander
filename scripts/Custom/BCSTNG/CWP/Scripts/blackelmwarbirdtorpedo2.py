import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(36.0 / 255.0, 255.0 / 55.0, 17.0 / 255.0, 1.000000)
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.5,
					1.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.8,	 
					0.6,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kFlareColor,										
					22,		
					0.5,		
					0.4)					
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)
	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("blackelmwarbirdtorpedo2")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Rom Flux Plasma")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 1.0
