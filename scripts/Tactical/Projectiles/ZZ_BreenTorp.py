###############################################################################
#	Filename:	FtaBreenTorp.py
#	By:		edtheborg
###############################################################################

import App

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 186.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_BreenCore.tga",
					kCoreColor,
					0.2,
					1.2,	 
					"data/Textures/Tactical/ZZ_BreenGlow.tga", 
					kGlowColor,
					2.0,	
					0.34,	 
					0.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					20,		
					0.08,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.ZZ_BREENTORP)

	return(0)

def GetLaunchSpeed():
    return 15.0


def GetLaunchSound():
    return 'BreenTorpedoXL'


def GetPowerCost():
    return 30.0


def GetName():
    return 'Drain Weapon'


def GetDamage():
    return 5.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.2

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
