#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					0.0,	 
					"data/Textures/Tactical/QuantumX.tga", 
					kGlowColor,
					0.4,	
					0.5,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					4,		
					0.1,		
					0.03)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.250)
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
	return("TAntimatter")

def GetPowerCost():
	return(35.0)

def GetName():
	return("Traedon Antimatter")

def GetDamage():
	return 10250.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.60
