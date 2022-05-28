###############################################################################
#	Filename:	StarSpade.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of quantum torpedoes.
#	
#	Created:	7/2004 -	Michael Frederick
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
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 255.0 / 255.0, 88.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(100.0 / 255.0, 255.0 / 255.0, 150.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					0.3,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.7,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					10,		
					0.8,		
					1.2)	

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
    return 25.0


def GetLaunchSound():
	return("GornTorp")


def GetPowerCost():
    return 30.0


def GetName():
    return "Gorn Torpedo"


def GetDamage():
    return 1000.0


def GetGuidanceLifetime():
    return 7.5


def GetMaxAngularAccel():
    return 0.55

