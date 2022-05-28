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
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 64.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 64.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NXGlow.tga",
					kCoreColor,
					0.3,
					6.0,	 
					"data/Textures/Tactical/NXGlow.tga", 
					kGlowColor,
					4.0,	
					0.46,	 
					0.42,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,						
					0,		
					0.0,		
					0.0)

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
	return(30.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Conventional torpedo")

def GetDamage():
	return 250.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 2.15
