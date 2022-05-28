#script modified by MRJOHN

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					1.0,	 
					"data/Textures/Tactical/ArmVoyX.tga", 
					kCoreColor,
					3.0,	
					0.3,	 
					0.5,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					0.06,		
					0.0,		
					0.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.18)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(66.0)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(35.0)

def GetName():
	return("PhotonMicrotopedo")

def GetDamage():
	return 550.0

def GetGuidanceLifetime():
	return 14.0

def GetMaxAngularAccel():
	return 6.0
