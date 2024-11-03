###############################################################################
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
#	This is a form of disruptor 
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.000000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(135.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.0)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 3.8, 0.05) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.05)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FUSIONBOLT)

	return(0)

def GetLaunchSpeed():
	return(105.0)

def GetLaunchSound():
	return("DemonicPulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Demonic Pulse")

def GetDamage():
	return 3000.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 0.05

def GetLifetime():
	return 8.0
