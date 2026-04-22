###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	1/26/05 -      Spade
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(245.0 / 255.0, 40.0 / 255.0, 145.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					'data/Textures/Tactical/TransGravCore.tga',
					kCoreColor,
					0.75,
					1.0,
					'data/Textures/Tactical/BorgAkiraTorpGlow.tga',
					kGlowColor,
					2.5,
					1.5,
					3.5,
					'data/Textures/Tactical/TorpedoFlares.tga',
					kFlareColor,
					85,
					0.95,
					0.02)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.165)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("LightMonopoleTorpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Light Monopole Torpedo")

def GetDamage():
	return 8500.0

def GetGuidanceLifetime():
	return 5.75

def GetMaxAngularAccel():
	return 1.0
