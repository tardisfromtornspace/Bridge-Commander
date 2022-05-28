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
	kOuterShellColor.SetRGBA(0.539216, 1.000000, 0.339216, 1.000000)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.007843, 1.000000, 0.00000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.1) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.VALDOREDISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("Disruptor")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Disruptor")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 0.2

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 7.0
