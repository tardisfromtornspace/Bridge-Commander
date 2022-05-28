#script modified by D&G Productions

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(10.0 / 255.0, 255.0 / 255.0, 180.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(10.0 / 255.0, 255.0 / 255.0, 150.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAGravimetric.tga",
					kCoreColor, 
					0.6,
					3.0,	 
					"data/Textures/Tactical/CAGravimetric.tga", 
					kGlowColor,
					4.0,	
					0.2,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					2,		
					0.2,		
					0.5)

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
	return(26.0)

def GetLaunchSound():
	return("DGGravimetric")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Gravimetric Torpedo")

def GetDamage():
	return 600.0

def GetGuidanceLifetime():
	return 16.0

def GetMaxAngularAccel():
	return 3.3
