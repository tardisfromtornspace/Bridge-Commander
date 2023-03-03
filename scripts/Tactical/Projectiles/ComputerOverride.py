#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(200.0 / 255.0, 230.0 / 200.0, 199.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(36.0 / 255.0, 255.0 / 55.0, 17.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					1.9,
					2.0,	 
					"data/Textures/Tactical/ComputerOverride.tga", 
					kGlowColor,
					7.0,	
					0.60,	 
					3.3,	
					"data/Textures/Tactical/ComputerOverride.tga",
					kGlowColor,										
					20,		
					0.5,		
					0.6)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(3.99)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("ComputerOverride")

def GetPowerCost():
	return(10.0)

def GetName():
	return("ComputerOverride")

def GetDamage():
	return 650.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 10.0
