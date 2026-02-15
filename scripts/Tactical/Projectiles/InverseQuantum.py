import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(250.0 / 255.0, 49.0 / 255.0, 48.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 18.0 / 255.0, 2.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZQuantumCore.tga",
					kCoreColor, 
					0.6,
					3.5,	 
					"data/Textures/Tactical/ZZQuantumGlow.tga", 
					kGlowColor,
					7,	
					7.10,	 
					7.75,	
					"data/Textures/Tactical/TorpedoFlares.tga",
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
	return(55.0)

def GetLaunchSound():
	return("InverseQuantum")

def GetPowerCost():
	return(75.0)

def GetName():
	return("Inverse Quantum")

def GetDamage():
	return 7500.0

def GetGuidanceLifetime():
	return 5.5

def GetMaxAngularAccel():
	return 1.5

def GetLifetime():
	return 50.0
