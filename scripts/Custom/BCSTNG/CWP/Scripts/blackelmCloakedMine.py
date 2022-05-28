import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(13.0 / 255.0, 13.0 / 255.0, 13.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.6,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,										
					12,		
					0.5,		
					0.4)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.8)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)
	return(0)

def GetLaunchSpeed():
	return(0.0)

def GetLaunchSound():
	return("CloakedMine")

def GetPowerCost():
	return(0.0)

def GetName():
	return("CloakedMine")

def GetDamage():
	return 9999.9

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0
