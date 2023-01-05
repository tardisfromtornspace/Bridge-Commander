#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 2.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(225.0 / 255.0, 215.0 / 255.0, 255.0 / 255.0, 2.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.1,
					1.0,	 
					"data/Textures/Tactical/NemQuantumGlow.tga", 
					kCoreColor,
					4.0,	
					4.3,	 
					4.1,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					300,		
					0.2,		
					0.04)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("QuantumXII")

def GetPowerCost():
	return(1.0)

def GetName():
	return("QuantumXII")

def GetDamage():
	return 2920.9

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 3.60
