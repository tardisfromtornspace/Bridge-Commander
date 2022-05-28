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
	kGlowColor.SetRGBA(0.0 / 255.0, 255.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(200.0 / 255.0, 255.0 / 255.0, 200.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.6,	 
					0.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.4,		
					0.4)

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
	return(22.0)

def GetLaunchSound():
	return("KlingonPhoton")

def GetPowerCost():
	return(22.0)

def GetName():
	return("Photon Torpedo")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.2
