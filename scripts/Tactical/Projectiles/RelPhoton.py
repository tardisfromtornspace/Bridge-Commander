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
	kGlowColor.SetRGBA(25.0 / 25.0, 25.0 / 25.0, 240.0 / 240.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(25.0 / 25.0, 25.0 / 25.0, 240.0 / 240.0, 1.000000)
	kFlareColor = App.TGColorA()
   	kFlareColor.SetRGBA(25.0 / 25.0, 25.0 / 25.0, 240.0 / 240.0, 1.000000)
	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.18,
					8,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.8,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,													
					40,		
					0.15,		
					0.15)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FEDERATION)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("RelPhoton")

def GetPowerCost():
	return(15.0)

def GetName():
	return("Rel Photon")

def GetDamage():
	return 3500.0

def GetGuidanceLifetime():
	return 8.5

def GetMaxAngularAccel():
	return 4.0
