###############################################################################
#	Filename:	ST1torp.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of WOKtorp torpedoes.
#	
#	Created:	8/9/05 -	by WileyCoyote
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a ST1torp torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(55.0 / 255.0, 120.0 / 255.0, 250.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(55.0 / 255.0, 120.0 / 255.0, 250.0 / 255.0, 1.000000)	
	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.10,
					5.0,	 
					"data/Textures/Tactical/WC_ST2torpGlow.tga", 
					kGlowColor,
					1.0,	
					0.3,	 
					0.35,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					12,		
					0.6,		
					0.3)

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
	return("ST1 Photon")

def GetPowerCost():
	return(5.0)

def GetName():
	return("Type 2 Photon")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 3.15
