###############################################################################
#	Filename:	KlingonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of klingon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a klingon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(25.0 / 255.0, 255.0 / 255.0, 28.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(55.0 / 255.0, 255.0 / 255.0, 38.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAKlingonGreen.tga",
					kCoreColor, 
					0.2,
					6.0,	 
					"data/Textures/Tactical/CAKlingonGreen.tga", 
					kGlowColor,
					2.3,	
					0.5,	 
					0.8,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					12,		
					0.4,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("KlingonGreen")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Adv Photon")

def GetDamage():
	return 1200.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 0.5
