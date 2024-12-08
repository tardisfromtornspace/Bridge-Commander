###############################################################################
#	Filename:	TemporalTorp.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of TemporalTorp torpedoes.
#	
#	Created:	7/19/05 -	Sonic14
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a TemporalTorp torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(190.0 / 214.0, 24.0 / 237.0, 230.0 / 131.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(64.0 / 117.0, 36.0 / 23.0, 147.0 / 101.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(243.0/ 238.0, 39.0 / 151.0, 2.0 / 6.0, 1.000000)


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/Quantum01.tga",
					kCoreColor, 
					0.2,
					0.0,	 
					"data/Textures/Tactical/Quantum01Glow.tga", 
					kGlowColor,
					4.0,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					82,		
					0.4,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.10)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("MicropulsarDevice")

def GetPowerCost():
	return(500.0)

def GetName():
	return("Micropulsar Device")

def GetDamage():
	return 650000.0

def GetGuidanceLifetime():
	return 8.5

def GetMaxAngularAccel():
	return 0.55
