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
	kOuterShellColor.SetRGBA(1.000000, 0.501392, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.870588, 0.662745, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 16.0, 0.22) 	

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
	return(100.0)

def GetLaunchSound():
	return("IonHigh")

def GetPowerCost():
	return(30.0)

def GetName():
	return("BaseCannonXL")

def GetDamage():
	return 90.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 100.0

def GetLifetime():
	return 22.0
