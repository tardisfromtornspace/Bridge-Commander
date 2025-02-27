###############################################################################
#	Filename:	PhotonTorpedo2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	10/29/01 -	Evan Birkby
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

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(55.0 / 255.0, 255.0 / 55.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.02,
					30.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					30.0,	
					12.3,	 
					10.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					80,		
					1.7,		
					10.4)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(9.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("zneutrino")

def GetPowerCost():
	return(20.0)

def GetName():
	return("micro single-string Z-neutrino")

def GetDamage():
	return 0.1

def GetGuidanceLifetime():
	return 11.0

def GetMaxAngularAccel():
	return 3.7

try:
	modMicrozneutrinosingleStringBomb = __import__("Custom.Techs.MicrozneutrinosingleStringBomb")
	if(modMicrozneutrinosingleStringBomb):
		modMicrozneutrinosingleStringBomb.oMicrozneutrinosingleStringBombTorpe.AddTorpedo(__name__)
except:
	print "Micro Z-Neutrino Wave flattened into a single String Bomb script not installed, or you are missing Foundation Tech"