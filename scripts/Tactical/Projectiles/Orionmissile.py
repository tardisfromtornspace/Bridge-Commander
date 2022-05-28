###############################################################################
#	Filename:	QuantumTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of quantum torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a quantum torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/MissileCore.tga",
					kCoreColor, 
					0.5,
					0.5,	 
					"data/Textures/Tactical/MissileGlow.tga", 
					kGlowColor,
					4.0,	
					1.8,	 
					1.8,	
					"data/Textures/Tactical/MissileFlares.tga",
					kGlowColor,										
					40,		
					0.4,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Orionmissile")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Orion Missile")

def GetDamage():
	return 750.0

def GetGuidanceLifetime():
	return 2.0

def GetMaxAngularAccel():
	return 0.83
