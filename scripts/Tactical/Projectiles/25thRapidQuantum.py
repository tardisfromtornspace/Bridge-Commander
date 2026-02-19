import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.6,
					3.5,	 
					"data/Textures/Tactical/NemQuantumGlow.tga", 
					kGlowColor,
					7,	
					7.10,	 
					7.75,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.14)

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
	return(55.0)

def GetLaunchSound():
	return("RapidQuantum")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 1345.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 5.8

def GetLifetime():
	return 7.0
