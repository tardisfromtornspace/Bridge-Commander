#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(202.0 / 255.0, 232.0 / 255.0, 255.0 / 255.0, 1.000000)   # was 222.0 / 255.0, 322.0 / 255.0, 253.0 / 255.0, 1.000000
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 218.0 / 255.0, 169.0 / 255.0, 1.000000)	# was 61.0 / 255.0, 198.0 / 255.0, 239.0 / 255.0, 1.000000

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.75,
					0.0,	 
					"data/textures/tactical/nemesis2.tga", 
					kGlowColor,
					2.0,	
					2.2,	 
					2.1,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.15,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CAPHASEQUANTUM)

	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("PhasedQuantum")

def GetPowerCost():
	return(50.0)

def GetName():
	return("Phased Quantum")

def GetDamage():
	return 2450.0

def GetGuidanceLifetime():
	return 42.0

def GetMaxAngularAccel():
	return 0.79
