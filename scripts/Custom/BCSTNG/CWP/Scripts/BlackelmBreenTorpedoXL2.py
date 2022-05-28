import App
def Create(pTorp):
	debug(__name__ + ' def Create')
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 128.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(125.0 / 255.0, 190.0 / 255.0, 183.0 / 255.0, 1.000000)	
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
	pTorp.SetDamageRadiusFactor(10.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)
	return(0)

def GetLaunchSpeed():
	return(15.0)

def GetLaunchSound():
	return("BreenTorpedoXL")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Drain Torpedo ")

def GetDamage():
	return 4000.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 1.2
