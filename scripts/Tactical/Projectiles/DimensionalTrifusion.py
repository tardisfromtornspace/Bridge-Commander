###############################################################################
#	Filename:	Disruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a disruptor blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	PulseCoreColor = App.TGColorA()
	PulseCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	PulseGlowColor = App.TGColorA()
	PulseGlowColor.SetRGBA(255.0 / 255.0, 75.0 / 255.0, 75.0 / 255.0, 1.000000)	
	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					PulseCoreColor, 
					0.0625,
					0.0625,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					PulseGlowColor,
					0.0,	
					0.125,	 
					0.125,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					PulseGlowColor,
					0,		
					0.0,		
					0.0) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(200)

def GetLaunchSound():
	return("DimensionalTrifusion")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Dimensional Trifusion")

def GetDamage():
	return 6500.0

def GetGuidanceLifetime():
	return 0.25

def GetMaxAngularAccel():
	return 5.5

def GetLifetime():
	return 24.0

def GetFlashColor():
	return (255.0, 0.0, 0.0)