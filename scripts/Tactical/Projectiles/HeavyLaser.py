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

##	kOuterShellColor = App.TGColorA()
##	kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 0.000000)	
##	kOuterCoreColor = App.TGColorA()
##	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.639216, 1.000000)
##
##	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.0, 0.2)

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.00000, 1.00000, 0.00000, 1.00000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.0, 1.0, 1.0, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 5, 0.1) 
	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(90.0)

def GetLaunchSound():
	return("TurboLaser")

def GetPowerCost():
	return(80.0)

def GetName():
	return("TurboLaser")

def GetDamage():
	return 50.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 2.0
