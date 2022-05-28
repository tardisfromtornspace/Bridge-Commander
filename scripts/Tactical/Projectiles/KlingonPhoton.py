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
	kGlowColor.SetRGBA(13.0 / 255.0, 164.0 / 255.0, 32.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/KlingonGlow.tga",
					kCoreColor, 
					0.3,
					6.0,	 
					"data/Textures/Tactical/KlingonGlow.tga", 
					kGlowColor,
					2.3,	
					0.9,	 
					0.7,	
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
	return(60.0)

def GetLaunchSound():
	return("Klingon Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Klingon photon")

def GetDamage():
	return 1100.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 4.8
