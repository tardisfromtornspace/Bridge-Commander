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
	kOuterShellColor.SetRGBA(255.0, 35.0, 35.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(139.0, 2.000000, 2.0, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.08) 	

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
	return(75.0)

def GetLaunchSound():
	return("TradoPulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Tradophian Medium")

def GetDamage():
	return 37500.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.5

def GetLifetime():
	return 15.0
