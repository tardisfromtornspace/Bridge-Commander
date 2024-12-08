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
import MissionLib

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
	kOuterShellColor.SetRGBA(5.0, 255.0, 50.0, 0.850)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(255.0, 140.0, 250.0, 1.5)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.75, 0.0250) 		

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(85.0)

def GetLaunchSound():
	return("PhasedTemporalPulse")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Phased Temporal Pulse")

def GetDamage():
	return 4250.0

def GetGuidanceLifetime():
	return 3.75

def GetMaxAngularAccel():
	return 0.45