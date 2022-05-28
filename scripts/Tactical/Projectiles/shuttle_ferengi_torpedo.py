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
	kGlowColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)
        kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(1.0 / 1.0, 1.0 / 1.0, 1.0 / 1.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/Quantum01.tga",
					kCoreColor, 
					0.1,
					0.0,	 
					"data/Textures/Tactical/Micro01Glow.tga", 
					kGlowColor,
					0.5,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					42,		
					0.1,		
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
	return(21.0)

def GetLaunchSound():
	return("shuttle_ferengi_torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Torpedo")

def GetDamage():
	return 450.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 1.25
