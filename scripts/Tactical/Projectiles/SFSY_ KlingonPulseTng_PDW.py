###############################################################################
#	KlingonPulseTNG
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	2/27/00 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	This is a form of disruptor (nISwI)
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.5, 0.05) 	


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.3)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FUSIONBOLT)

	return(0)

def GetLaunchSpeed():
	return(48.0)

def GetLaunchSound():
	return("SFSY_ KlingonPulseTng_PDW")

def GetPowerCost():
	return(10.0)

def GetName():
	return("nISwI_Tng")

def GetDamage():
	return 975.0

def GetGuidanceLifetime():
	return 0.7

def GetMaxAngularAccel():
	return 0.25

def GetLifetime():
	return 8.0
