###############################################################################
#	Filename:	BorgPulse.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	8/28/01 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Borg Pulse Blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

#	kOuterShellColor = App.TGColorA()
#	kOuterShellColor.SetRGBA(0.007843, 1.000000, 0.007843, 1.000000)	
#	kOuterCoreColor = App.TGColorA()
#	kOuterCoreColor.SetRGBA(0.588235, 1.000000, 0.588235, 1.000000)


	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.275000, 0.003922, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.0, 0.2)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("ZZ_BorgPulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Borg Cannon")

def GetDamage():
	return 500.0

def GetGuidanceLifetime():
	return 5.0

def GetMaxAngularAccel():
	return 0.05

def GetLifetime():
	return 5.0
