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
	kGlowColor.SetRGBA(204.0 / 255.0, 204.0 / 255.0, 255.0 / 255.0, 2.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 235.0 / 255.0, 255.0 / 255.0, 2.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NXBeoPulseQuantumCore.tga",
					kCoreColor, 
					0.15, #was 0.6
					3.5,	 
					"data/Textures/Tactical/NXBeoPulseQuantumGlow.tga", 
					kGlowColor,
					7,	
					1.45,	#was 7.10 
					2.05,	#was 7.75
					"data/Textures/Tactical/NXBeoPulseQuantumBlank.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.14)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.12) #was 0.14
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(57.0)

def GetLaunchSound():
	return("25thCenturyQuantum")

def GetPowerCost():
	return(25.0)

def GetName():
	return("Enhanced Quantum")

def GetDamage():
	return 1800.0

def GetGuidanceLifetime():
	return 15.0

def GetMaxAngularAccel():
	return 2.6
