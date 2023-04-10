#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0, 255.0, 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0, 255.0, 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ds9torp.tga",
					kCoreColor, 
					0.2,
					6.0,	 
					"data/Textures/Tactical/ds9torp.tga", 
					kGlowColor,
					2.3,	
					0.4,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					3,		
					0.2,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(1.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(69.0)

def GetLaunchSound():
	return("IntrepidCannon")

def GetPowerCost():
	return(35.0)

def GetName():
	return("ArmVoyX")

def GetDamage():
	return 790.0

def GetGuidanceLifetime():
	return 4.0

def GetMaxAngularAccel():
	return 1.40