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
					"data/textures/tactical/ZZQuantumGlow.tga", 
					kGlowColor,
					3.5,	
					3.6,	 
					4.2,	
					"data/textures/tactical/ZZHeavyPhotonFlares.tga",
					kGlowColor,										
					30,		
					0.21,		
					0.4)

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
	return(45.0)

def GetLaunchSound():
	return("Nemesis")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 1800.0

def GetGuidanceLifetime():
	return 1.7

def GetMaxAngularAccel():
	return 0.2

def GetLifetime():
	return 20.0
