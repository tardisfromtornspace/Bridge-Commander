###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App
import string
pWeaponLock = {}

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
	kGlowColor.SetRGBA(253.0 / 255.0, 245.0 / 255.0, 203.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(254.0 / 255.0, 254.0 / 255.0, 254.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TransphasicFlares.tga",
					kCoreColor, 
					0.15,
					0.8,	 
					"data/Textures/Tactical/BorgAkiraTorpGlow.tga", 
					kGlowColor,
					3.5,	
					1.5,	 
					0.85,	
					"data/Textures/Tactical/TransphasicFlares.tga",
					kGlowColor,										
					20,		
					0.45,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(150.0)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(120.0)

def GetLaunchSound():
	return("EminTransphasic")

def GetPowerCost():
	return(80.0)

def GetName():
	return("Transphasic II")

def GetDamage():
	return 4150.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 0.265

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"

