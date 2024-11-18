###############################################################################
#	Filename:	PhotonTorpedo2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	10/29/01 -	Evan Birkby
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
	kGlowColor.SetRGBA(255.0 / 255.0, 55.0 / 255.0, 55.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 220.0 / 255.0, 220.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.4,	 
					0.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					25,		
					0.12,		
					0.12)

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
	return(100.0)

def GetLaunchSound():
	return("FedPulsePhoton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Type 6 Photon Torpedo")

def GetDamage():
	return 850.0

def GetGuidanceLifetime():
	return 10.1

def GetMaxAngularAccel():
	return 10.0
