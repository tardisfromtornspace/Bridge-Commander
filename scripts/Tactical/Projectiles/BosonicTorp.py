###############################################################################
#	SFRD_RFQuantumPulse
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
#	Creates a SFRD_RFQuantumPulse
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################


def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/SFRD_RFQuantumPulseCore2.tga",
					kCoreColor, 
					0.8,
					1.2,	 
					"data/Textures/Tactical/SFRD_RFQuantumPulseGlow2.tga", 
					kGlowColor,
					45.0,	
					0.7,	 
					1.8,	
					"data/Textures/Tactical/SFRD_25thQuamTorpedoFlares.tga",
					kGlowColor,						
					40,		
					0.35,		
					0.65)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(125.0)

def GetLaunchSound():
	return("BosonicTorp")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Bosonic Torp")

def GetDamage():
	return 2500000.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 1.5
