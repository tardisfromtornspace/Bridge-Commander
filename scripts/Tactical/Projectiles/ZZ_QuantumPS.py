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
					0.2,
					3.5,	 
					"data/Textures/Tactical/ZZQuantumGlow.tga", 
					kGlowColor,
					3.5,	
					1.2,	 
					1.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					30,		
					0.07,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("NemQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 1750.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 1.20

def GetLifetime():
	return 20.0
