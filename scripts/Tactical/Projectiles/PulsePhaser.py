###############################################################################
#	Filename:	Disruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a disruptor blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 233, 147, 45)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 94, 18, 6)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.9, 0.07)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.10)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEPHASER)

	return(0)

def GetLaunchSpeed():
	return(56.0)

def GetLaunchSound():
	return("PulsePhaser")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Pulse Phaser")

def GetDamage():
	return 125.0

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 8.0
