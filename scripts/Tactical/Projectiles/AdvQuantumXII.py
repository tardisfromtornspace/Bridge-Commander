#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(100.0 / 255.0 , 100.0 / 255.0 , 100.0 / 255.0 , 1.00000)	
	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.60,
					3.70,	 
					"data/Textures/Tactical/NemQuantumGlow.tga", 
					kGlowColor,
					7.0,	
					7.25,	 
					8.25,	
					"data/Textures/Tactical/NemQuantumBlank.tga",
					kGlowColor,										
					0,		
					0.10,		
					0.15)

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
	return(65.0)

def GetLaunchSound():
	return("AdvQuantumXII")

def GetPowerCost():
	return(35.0)

def GetName():
	return("QuantumXII Advanced")

def GetDamage():
	return 6000.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 1.20
