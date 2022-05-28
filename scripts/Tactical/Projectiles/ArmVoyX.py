#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 225.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 225.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					0.0,	 
					"data/Textures/Tactical/ArmVoyX.tga", 
					kCoreColor,
					0.1,	
					0.3,	 
					0.05,	
					"data/Textures/Tactical/ArmVoyX.tga",
					kGlowColor,										
					5,		
					0.1,		
					0.06)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(90.99)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(60.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(890.0)

def GetName():
	return("ArmVoyX")

def GetDamage():
	return 999.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 0.60
