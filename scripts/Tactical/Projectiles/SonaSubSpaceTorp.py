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
	kCoreColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(200.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					0.1,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					5.1,	
					0.1,	 
					0.1,	
					"data/Textures/Tactical/SubspaceFlares.tga",
					kGlowColor,										
					100.0,		
					100.0,		
					25.0)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(1.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(5.0)

def GetLaunchSound():
	return("SonaSubSpaceTorp")

def GetPowerCost():
	return(100.0)

def GetName():
	return("Sub-Space Torpedo")

def GetDamage():
	return 100000.0

def GetGuidanceLifetime():
	return 60.0

def GetMaxAngularAccel():
	return 1.0

def GetLifetime():
	return 600.0
