#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 128.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 129.0 / 255.0, 239.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					1.0,	 
					"data/Textures/Tactical/PhotonX.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.1,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					82,		
					0.3,		
					0.04)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.40)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(199.0)

def GetLaunchSound():
	return("MarsTorpedo")

def GetPowerCost():
	return(1.0)

def GetName():
	return("MarsTorpedo")

def GetDamage():
	return 3100.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 5.80
