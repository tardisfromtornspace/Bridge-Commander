import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 124.0 / 255.0, 197.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.6,
					3.5,	 
					"data/Textures/Tactical/ZZQuantumGlow.tga", 
					kGlowColor,
					3.5,	
					3.75,	 
					5.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					250,		
					0.35,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("EminQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Quantum XI")

def GetDamage():
	return 1700.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.4

def GetLifetime():
	return 35.0
