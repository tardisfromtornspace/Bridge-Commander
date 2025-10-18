#script modified by FekLeyrTarg

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TargAxanarTorp1Core.tga",
					kCoreColor, 
					0.2,
					6.0,	 
					"data/Textures/Tactical/TargAxanarTorp1Glow.tga", 
					kGlowColor,
					6.0,	
					1.2,	 
					1.3,	
					"data/Textures/Tactical/TargAxanarTorp1Flares.tga",
					kGlowColor,						
					1,		
					1.8,		
					1.4)

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
	return(15.0)

def GetLaunchSound():
	return("TOSPhoton1")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photon")

def GetDamage():
	return 180.0

def GetGuidanceLifetime():
	return 4.0

def GetMaxAngularAccel():
	return 0.3
