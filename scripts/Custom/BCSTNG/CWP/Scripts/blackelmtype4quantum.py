import App
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(100.0 / 255.0,179.0 / 255.0,255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(23.0 / 255.0,47.0 / 255.0,202.0 / 255.0, 1.000000)	
	pTorp.CreateTorpedoModel(
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmtorpedomulti.tga",
					kCoreColor, 
					0.5,
					0.1,	 
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmtorpedomulti.tga", 
					kGlowColor,
					0.8,	
					0.2,	 
					0.1,	
					"Scripts/Custom/BCSTNG/CWP/Textures/blackelmTorpedoFlares.tga",
					kGlowColor,									70,		
					0.3,		
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
	return("blackelmtype3quantum")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Type 4 Quantum")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.4
