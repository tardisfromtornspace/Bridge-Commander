import App
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(64.0 / 255.0, 107.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(85.0 / 255.0, 255.0 / 255.0, 254.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/AdvancedBQuantumCore.tga",
					kCoreColor, 
					0.2,
					1.5,	 
					"data/textures/tactical/AdvancedBQuantumGlow.tga", 
					kGlowColor,
					0.5,	
					0.3,	 
					0.7,	
					"data/textures/tactical/AdvancedBQuantumFlare.tga",
					kGlowColor,										
					8,		
					0.4,		
					1.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.RAPIDQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("AdvancedQuantum")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Adv Quantum")

def GetDamage():
	return 2500.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 7.0
