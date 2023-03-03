###############################################################################
#	Filename:	FusionBolt.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	2/27/00 -	Evan Birkby  redo MRJOHN 1/10/2004  www.freewebs.com/johnearl
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a fusion bolt.  This is a form of disruptor.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 1.000000, 0.700000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.639216, 1.000000, 0.700000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.6, 0.03) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.09)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.FUSIONBOLT)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("Antimatter Torpedo")

def GetPowerCost():
	return(26.0)

def GetName():
	return("BeoPhoton")

def GetDamage():
	return 590.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 2.0

def GetLifetime():
	return 9.0
