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
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(104.0 / 255.0, 124.0 / 255.0, 197.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.078431, 0.972549, 0.725490, 0.466667)

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
					35,
					1.2,
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
	return("LTTranscendentalGravimetric")

def GetPowerCost():
	return(20.0)

def GetName():
	return("LT Transcendental Gravimetric")

def GetDamage():
	return 6500.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 1.0
