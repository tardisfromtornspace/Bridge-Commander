import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.01,
					0.1,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmVCore01JLH.tga",
					kGlowColor,
					0.5,	
					0.3,	 
					0.3,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmJLH05.tga",
					kGlowColor,										
					42,		
					0.1,		
					0.5)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)
	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("blackelmtype6fixedinstallation")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Micro Quantum")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.4
