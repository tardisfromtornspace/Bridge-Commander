###############################################################################
#	Filename:	PulseDisruptor.py
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
	kOuterShellColor.SetRGBA(1.0, 0.0, 0.0, 1.0)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.0, 0.8, 0.8, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.1, 0.01) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("sflaser")

def GetPowerCost():
	return(10.0)

def GetName():
	return("KX9 Laser")

def GetDamage():
	return 13.0

def GetGuidanceLifetime():
	return 0.0001

def GetMaxAngularAccel():
	return 0.025

def GetLifetime():
	return 7.0

def GetFlashColor():
	return (200.0, 25.0, 25.0)
