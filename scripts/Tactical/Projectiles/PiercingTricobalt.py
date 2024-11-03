#script modified by Sneaker98

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(175.0 / 255.0, 224.0 / 255.0, 239.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(48.0 / 255.0, 80.0 / 255.0, 128.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					55,		
					0.5,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(2.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("PiercingTricobalt")

def GetPowerCost():
	return(50.0)

def GetName():
	return("Piercing Tricobalt")

def GetDamage():
	return 5500.0

def GetGuidanceLifetime():
	return 7.50

def GetMaxAngularAccel():
	return 0.50
