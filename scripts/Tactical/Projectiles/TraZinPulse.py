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
	kOuterShellColor.SetRGBA(40.0 / 255.0, 0.0 / 255.0, 185.0 / 255.0, 0.500000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.0 / 255.0, 135.0 / 255.0, 185.0 / 255.0, 0.500000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 20.0, 0.20) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.3)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.MPNEGHVARPULSE)

	return(0)

def GetLaunchSpeed():
	return(200.0)

def GetLaunchSound():
	return("TraZinPulse")

def GetPowerCost():
	return(15.0)

def GetName():
	return("TraZinPulse")

def GetDamage():
	return 925000.0

def GetGuidanceLifetime():
	return 0.50

def GetMaxAngularAccel():
	return 0.150

def GetLifetime():
	return 20.0
