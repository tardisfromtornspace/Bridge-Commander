#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/AlkeshCore.tga",
					kCoreColor, 
					0.3,
					6.0,	 
					"data/Textures/Tactical/AlkeshCore.tga", 
					kGlowColor,
					1.0,	
					0.4,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,						
					12,		
					0.2,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(5.0)

def GetLaunchSound():
	return("DGFire")

def GetPowerCost():
	return(5.0)

def GetName():
	return("Alkesh Bomb")

def GetDamage():
	return 700.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 1.0
