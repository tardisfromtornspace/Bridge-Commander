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
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/Quantum01.tga",
					kCoreColor, 
					0.2,
					0.1,	 
					"data/Textures/Tactical/Quantum01Glow.tga", 
					kGlowColor,
					2.4,	
					0.3,	 
					0.19,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					162,		
					0.15,		
					0.7)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.14)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.ZZ_BREENTORP)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("BreenD")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Breen Drain")

def GetDamage():
	return 4.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.15

##################################################################################
# Foundation Technologies, copyright 2004 by Daniel Rollings AKA Dasher42
#
# This string is used to set a yield type using Foundation Technology plugins.
# If you wish extra functionality, subclassing an existing plugin here is acceptable,
# but the easiest way to set a special yield is to set this string to the name of an
# existing technology.
sYieldName = 'Breen Drainer Weapon'
sFireName = None


##################################################
# Do not edit below.


import FoundationTech
import ftb.Tech.BreenDrainer


#oFire = FoundationTech.oTechs[sFireName]
oFire = ftb.Tech.BreenDrainer.oDrainerWeapon
FoundationTech.dOnFires[__name__] = oFire

oYield = FoundationTech.oTechs[sYieldName]
FoundationTech.dYields[__name__] = oYield

