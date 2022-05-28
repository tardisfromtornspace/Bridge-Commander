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
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 124.0 / 255.0, 197.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.07,
					0.8,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.275,	 
					0.325,
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					5,		
					0.35,		
					0.22)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.05)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )


	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(24.0)

def GetLaunchSound():
	return("PFm1")

def GetPowerCost():
	return(12.0)

def GetName():
	return("Micro Photon")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.15
	
def GetLifetime():
	return 60.0

def GetFlashColor():
	return (0.0, 0.0, 0.0)