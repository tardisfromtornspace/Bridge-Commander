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
	kCoreColor.SetRGBA(255.0 / 255.0,255.0 / 255.0,255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(23.0 / 255.0,47.0 / 255.0,202.0 / 255.0, 1.000000)	
        kFlareColor = App.TGColorA()
        kFlareColor.SetRGBA(50.0 / 255.0, 50.0 / 255.0, 100.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/nemesis2.tga",
					kCoreColor, 
					0.5,
					0.1,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.5,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,									
					70,		
					0.12,		
					0.27)

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
	return(35.0)

def GetLaunchSound():
	return("Quantum Torp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Quantum")

def GetDamage():
	return 2600.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 0.17
