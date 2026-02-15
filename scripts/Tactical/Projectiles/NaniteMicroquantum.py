###############################################################################
#	Filename:	ImperialTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of Imperial Quantum Torpedoes.
#	
#	Created:	10/10/02 -	Dante Robinson
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Micro Quantum Torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(78.0 / 255.0, 120.0 / 255.0, 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(118.0 / 245.0, 255.0 / 255.0, 255.0 / 255., 1.000000)
	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
                    kCoreColor,
					0.1,
					0.2,	 
					"data/Textures/Tactical/KlingonTorpCore.tga", 
					kGlowColor,
					1.4,	
					0.9,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlare.tga",
					kFlareColor,										
					4,		
					0.5,		
					0.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.Quantum)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("NaniteMicroquantum")

def GetPowerCost():
	return(25.0)

def GetName():
	return("Nanite Microquantum")

def GetDamage():
	return 1050.0

def GetGuidanceLifetime():
	return 6.5

def GetMaxAngularAccel():
	return 0.75

try:
	import FoundationTech
	import ftb.Tech.NanoprobeProjectile
	oFire = ftb.Tech.NanoprobeProjectile.NanoprobeProjectileDef('Nanoprobe Projectile')
	FoundationTech.dYields[__name__] = oFire
except:
	pass