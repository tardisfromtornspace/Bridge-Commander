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
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)		
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 130.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.07,
					0.8,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.55,	 
					0.65,
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					5,		
					0.7,		
					0.22)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(21.0)

def GetLaunchSound():
	return("PFT2")

def GetPowerCost():
	return(21.0)

def GetName():
	return("Photon Torpedo")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.16
