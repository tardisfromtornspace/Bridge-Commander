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
	kOuterShellColor.SetRGBA(1.000000, 1.000000, 1.000000, 0.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.00000, 1.00000, 0.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 4.5, 0.1) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(35.0)

def GetLaunchSound():
	return("WarlockRail")

def GetPowerCost():
	return(10.0)

def GetName():
	return("LargeMissile")

def GetDamage():
	return 350.0

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 8.0
