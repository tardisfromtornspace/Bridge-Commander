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

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 207.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(244.0 / 255.0, 71.0 / 255.0, 0.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 221.0 / 255.0, 85.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					7.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.07,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )


	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("photonic")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photonic")

def GetDamage():
	return 250.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 2.20
	
def GetLifetime():
	return 30.0

def GetFlashColor():
	return (200.0, 50.0, 20.0)
