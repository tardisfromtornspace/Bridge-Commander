#script modified by Dragon

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(155.0 / 255.0, 155.0 / 255.0, 58.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(155.0 / 255.0, 108.0 / 255.0, 0.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(155.0 / 255.0, 108.0 / 255.0, 0.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CADS9.tga",
					kCoreColor, 
					0.4,
					4.0,	 
					"data/Textures/Tactical/CADS92.tga", 
					kGlowColor,
					0.5,	
					0.3,	 
					0.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,						
					6,		
					0.4,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
        pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.STATIONPHOTON)

	return(0)

def GetLaunchSpeed():
	return(42.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Photon")

def GetDamage():
	return 600.0

def GetGuidanceLifetime():
	return 6.0

def GetLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 5.15
