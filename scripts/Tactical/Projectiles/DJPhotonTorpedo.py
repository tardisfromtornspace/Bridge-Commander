#script modified by DJ Curtis

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/DJPhotonTorpedo.tga",
					kCoreColor, 
					0.2,
					6.0,	 
					"data/Textures/Tactical/DJPhotonTorpedo.tga", 
					kGlowColor,
					1.0,	
					0.5,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,						
					12,		
					0.4,		
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
	return(40.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 30.0

def GetMaxAngularAccel():
	return 1.0
