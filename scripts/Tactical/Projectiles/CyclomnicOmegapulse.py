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
	kCoreColor.SetRGBA(15.0 / 255.0, 0.0 / 255.0, 185.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(150.0 / 255.0, 100.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(230.0 / 255.0, 195.0 / 255.0, 255.0 / 255.0, 0.800000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CyclomnicOmegapulseCore.tga",
					kCoreColor, 
					1.5,
					3.0,	 
					"data/Textures/Tactical/CyclomnicOmegapulseGlow.tga", 
					kGlowColor,
					50.0,	
					5.8,	 
					5.4,	
					"data/Textures/Tactical/CyclomnicOmegapulseCore.tga",
					kFlareColor,								
					500,		
					4.0,		
					0.075)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.65)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("CyclomnicOmegapulse")

def GetPowerCost():
	return(300000.0)

def GetName():
	return("Cyclomnic Omegapulse")

def GetDamage():
	return 3000000.0

def GetGuidanceLifetime():
	return 7.5

def GetMaxAngularAccel():
	return 0.5