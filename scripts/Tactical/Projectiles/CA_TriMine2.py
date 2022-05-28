###############################################################################
#	Filename:	PositronTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of positron torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a positron torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CATriMine2.tga",
					kCoreColor, 
					0.10,
					3.0,	 
					"data/Textures/Tactical/CATriMine2.tga", 
					kGlowColor,
					3.0,	
					0.12,	 
					0.2,	
					"data/Textures/Tactical/CATriMine2.tga",
					kGlowColor,										
					50,		
					0.05,		
					0.05)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.10)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(5.0)

def GetLaunchSound():
	return("CATriMine2")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Tricobalt Mine")

def GetDamage():
	return 4000.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 3.0
