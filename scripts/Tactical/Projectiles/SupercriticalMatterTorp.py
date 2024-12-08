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
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.600000, 0.370588, 1.000000, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(250.0 / 255.0, 18.0 / 255.0, 2.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/naradaCore.tga",
					kCoreColor, 
					1.0,
					1.2, 	 
					"data/Textures/Tactical/naradaGlow.tga", 
					kGlowColor,
					0.3,	
					0.3,	 
					0.3,	
					"data/Textures/Tactical/naradaFlares.tga",
					kGlowColor,										
					8,		
					0.9,		
					0.5)

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
	return("ScMatterTorp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Supercritical Matter Torp")

def GetDamage():
	return 175000.0

def GetGuidanceLifetime():
	return 7.5

def GetMaxAngularAccel():
	return 0.45
