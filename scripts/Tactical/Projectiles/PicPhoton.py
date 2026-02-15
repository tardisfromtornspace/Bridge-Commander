#script modified by Dkealt and Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 18.0 / 255.0, 2.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(250.0 / 255.0, 49.0 / 255.0, 48.0 / 255., 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ds9torp.tga",
					kCoreColor, 
					0.25,
					6.0,	 
					"data/Textures/Tactical/ds9torp.tga", 
					kGlowColor,
					1.15,	
					0.75,	 
					1.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,						
					15,		
					0.65,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("PicardPhoton2")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Adv Photon")

def GetDamage():
	return 1150.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 0.5
