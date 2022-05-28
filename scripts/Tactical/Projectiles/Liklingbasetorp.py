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
	kGlowColor.SetRGBA(190.0 / 255.0, 49.0 / 255.0, 48.0 / 255., 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(250.0 / 255.0, 218.0 / 255.0, 202.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.3,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					12,		
					0.5,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KLINGONBASETORP)

	return(0)

def GetLaunchSpeed():
	return(39.0)

def GetLaunchSound():
	return("klingbasetorp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("klingonbasetorp")

def GetDamage():
	return 1000.0

def GetGuidanceLifetime():
	return 75.0

def GetMaxAngularAccel():
	return 0.70
