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
	kGlowColor.SetRGBA(255.0 / 255.0, 20.0 / 255.0, 20.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(205.0 / 255.0, 50.0 / 255.0, 20.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/CAKlingon.tga",
					kCoreColor, 
					0.2,
					0.5,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.2,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					28,		
					0.4,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.TMPKLINGONTORP)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("Klingon TMP")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Photon")

def GetDamage():
	return 900.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 0.4
