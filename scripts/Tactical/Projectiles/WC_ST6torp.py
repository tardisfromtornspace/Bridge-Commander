###############################################################################
#	Filename:	ST6torp.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of ST6torp torpedoes.
#	
#	Created:	8/9/05 -	Sonic14 modified by WileyCoyote
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a ST6torp torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 247.0 / 255.0, 153.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(237.0 / 255.0, 28.0 / 255.0, 36.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(237.0 / 255.0, 28.0 / 255.0, 36.0 / 255.0, 1.000000)	
	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.10,
					6.0,	 
					"data/Textures/Tactical/WC_ST6torpGlow.tga", 
					kGlowColor,
					1.0,	
					0.60,	 
					0.70,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					15,		
					0.40,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.08)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("ST6 Photon")

def GetPowerCost():
	return(5.0)

def GetName():
	return("Photon")

def GetDamage():
	return 600.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 1.55
