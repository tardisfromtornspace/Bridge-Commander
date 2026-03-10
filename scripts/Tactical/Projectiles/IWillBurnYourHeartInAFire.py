#script modified by Greystar

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 0.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.0001,
					4.2,		 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.0,	 
					0.0,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,						
					0,		
					0.001,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.01)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEPHASER)

	return(0)

def GetLaunchSpeed():
	return(5000.0)

def GetLaunchSound():
	return("IWillBurnYourHeartInAFire")

def GetPowerCost():
	return(1.0)

def GetName():
	return("IWillBurnYourHeartInAFire")

def GetDamage():
	return 2.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0
