#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.850000, 1.000000, 0.600000, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.000000, 0.780000, 0.720000, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.000000, 1.000000, 0.650000, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.1,
					1.0,	 
					"data/Textures/Tactical/NemQuantumGlow.tga", 
					kGlowColor,
					4.0,	
					4.3,	 
					4.1,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kFlareColor,										
					300,		
					0.2,		
					0.04)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1250)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("AndisiteLightPlasma")

def GetPowerCost():
	return(10.0)

def GetName():
	return("A Light Plasma")

def GetDamage():
	return 6500.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.60
