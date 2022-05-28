#script modified by Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(128.0 / 255.0, 235.0 / 128.0, 108.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1.0 / 128.0, 108.0 / 5.0, 1.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(128.0 / 255.0, 255.0 / 128.0, 118.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAPlasma.tga",
					kCoreColor, 
					0.4,
					3.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					8.0,	
					0.4,	 
					0.45,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					0,		
					0.4,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(10.0)

def GetLaunchSound():
	return("Romulan Heavy")

def GetPowerCost():
	return(80.0)

def GetName():
	return("Heavy Plasma")

def GetDamage():
	return 2000.0

def GetGuidanceLifetime():
	return 30.0

def GetMaxAngularAccel():
	return 0.2

