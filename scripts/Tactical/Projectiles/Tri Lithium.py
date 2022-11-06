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
	kCoreColor.SetRGBA(104.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(155.0 / 255.0, 195.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(155.0 / 255.0, 195.0 / 255.0, 255.0 / 255.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/Quantum01.tga",
					kCoreColor, 
					0.5,
					0.0,	 
					"data/Textures/Tactical/Quantum01Glow.tga", 
					kGlowColor,
					4.0,	
					0.9,	 
					0.9,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					82,		
					0.6,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.34)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(108.7)

def GetLaunchSound():
	return("Trilithium")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Hypercharged Trilithium Tropedo")

def GetDamage():
	return 240550.0

def GetGuidanceLifetime():
	return 60.0

def GetMaxAngularAccel():
	return 0.105
