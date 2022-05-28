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
	kGlowColor.SetRGBA(104.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.6,
					3.5,	 
					"data/textures/tactical/NemQuantumGlow.tga", 
					kGlowColor,
					7,	
					7.10,	 
					7.75,	
					"data/textures/tactical/NemQuantumBlank.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.14)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("FedQuantum")

def GetPowerCost():
	return(45.0)

def GetName():
	return("Quantum Torpedo")

def GetDamage():
	return 8000.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.13
