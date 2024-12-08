###############################################################################
#	Filename:	KessokDisruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	07/3/01 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Kessok disruptor cannon blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.000000, 0.000000, 1.000000, 2.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.501961, 0.000000, 0.501961, 2.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 15, 1.0) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.17)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KESSOKDISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(70.0)

def GetLaunchSound():
	return("VWarpPlasmaPulse")

def GetPowerCost():
	return(30.0)

def GetName():
	return("VWarpPlasmaPulse")

def GetDamage():
	return 6500.0

def GetGuidanceLifetime():
	return 0.5

def GetMaxAngularAccel():
	return 0.25

def GetLifetime():
	return 12.0
