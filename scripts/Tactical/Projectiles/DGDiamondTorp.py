#script modified by Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(200.0 / 255.0, 210.0 / 255.0, 10.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 0.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAGravimetric2.tga",
					kCoreColor, 
					0.3,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					1.0,	
					0.1,	 
					0.11,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					1,		
					0.05,		
					9.0)

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
	return(60.0)

def GetLaunchSound():
	return("DGBorgTorp")

def GetPowerCost():
	return(5.0)

def GetName():
	return("Gravimetric Pulse")

def GetDamage():
	return 50.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.4
