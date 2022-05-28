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
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 64.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ds9torp.tga",
					kCoreColor, 
					0.2,
					6.0,	 
					"data/Textures/Tactical/ds9torp.tga", 
					kGlowColor,
					2.3,	
					0.4,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					3,		
					0.2,		
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
	return(55.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Photon")

def GetDamage():
	return 785.0

def GetGuidanceLifetime():
	return 1.5

def GetMaxAngularAccel():
	return 0.3