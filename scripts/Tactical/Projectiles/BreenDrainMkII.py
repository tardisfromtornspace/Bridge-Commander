###############################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#	Filename:	BreenDrainMkII.py
#	
#	Based on BreenDrain.py (probably by Dasher42 under LGPL license and SDK License), which was based on QuantumTorpedo.py (which before the SDK was made, it was under Confidential and Proprietary, Copyright 2000 by Totally Games)
#	
#	Script for filling in the attributes of quantum torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales (for QuantumTorpedo.py)
#	Last Time Modified:	28 June 2023 -	Alex SL Gato
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

try:
	sYieldName = 'Upgraded Breen Drainer Weapon'
	sFireName = None

	import FoundationTech
	import Custom.Techs.UpgradedBreenDrainer

	oFire = Custom.Techs.UpgradedBreenDrainer.oUpgradedDrainerWeapon
	FoundationTech.dOnFires[__name__] = oFire

	oYield = FoundationTech.oTechs[sYieldName]
	FoundationTech.dYields[__name__] = oYield
except:
	print "Upgraded Breen Drainer Weapon not installed, or missing FoundationTech"

