import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoCore.tga",
					kCoreColor, 
					0.2,
					0.7,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoGlow.tga", 
					kGlowColor,
					0.0,	
					0.6,	 
					0.6,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,										
					5,		
					0.6,		
					1.0)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)
	return(0)

def GetLaunchSpeed():
	return(32.0)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Neutron Torpedo")

def GetDamage():
	return 900.0

def GetGuidanceLifetime():
	return 4.0

def GetMaxAngularAccel():
	return 0.15
