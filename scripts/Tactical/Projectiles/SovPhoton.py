###############################################################################
#	Filename:	PhasedPlasma.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of antimatter torpedoes.
#	
#	Created:	07/3/01 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Phased Plasma torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 128.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 128.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/SovPhoton.tga",
					kCoreColor,
					0.6,
					0.3,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.46,	 
					0.42,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,						
					0,		
					0.1,		
					0.14)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("CGPhotorp")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Type 12 Photon")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 1.3

def GetMaxAngularAccel():
	return 0.3

def GetLifetime():
	return 100.0