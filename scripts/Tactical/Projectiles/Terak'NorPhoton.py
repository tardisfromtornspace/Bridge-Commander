###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(199.0 / 255.0, 133.0 / 255.0, 61.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/DS9Glow.tga",
					kCoreColor, 
					0.25,
					6.0,	 
					"data/Textures/Tactical/DS9Glow.tga", 
					kGlowColor,
					2.3,	
					0.6,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					3,		
					0.22,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(95.0)

def GetLaunchSound():
	return("ds9torp")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Photon")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 2.0

def GetMaxAngularAccel():
	return 1.5
