#script modified by Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(225.0 / 255.0, 225.0 / 255.0, 1.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(225.0 / 255.0, 225.0 / 255.0, 1.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(225.0 / 255.0, 225.0 / 255.0, 1.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAPlasma.tga",
					kCoreColor, 
					16.0,
					120.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					320.0,	
					16.0,	 
					16.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.5,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.90)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.CAROMULANHEAVY)

	return(0)

def GetLaunchSpeed():
	return(150.0)

def GetLaunchSound():
	return("Romulan Heavy")

def GetPowerCost():
	return(80.0)

def GetName():
	return("2 V'GER PLASMA")

def GetDamage():
	return 2000000.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.6

