import App
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.000000, 0.000000, 1.000000, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.15,
					2.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.0,	 
					0.3,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kFlareColor,										
					15,		
					0.15,		
					0.3)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONTORP)
	return(0)

def GetLaunchSpeed():
	return(47.0)

def GetLaunchSound():
	return("blackelmsiesmictorpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("10 : Seismic")

def GetDamage():
	return 800.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.2
