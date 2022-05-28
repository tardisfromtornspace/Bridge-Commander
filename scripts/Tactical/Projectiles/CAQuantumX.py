#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.10,
					4.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.1,	 
					0.2,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					55,		
					0.35,		
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
	return(50.0)

def GetLaunchSound():
	return("Quantum Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Type3 Quantum")

def GetDamage():
	return 2000.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.5
