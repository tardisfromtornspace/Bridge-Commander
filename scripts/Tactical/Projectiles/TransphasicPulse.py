###############################################################################
#	SFRD_6_Pulse
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	2/27/00 -	Evan Birkby
###############################################################################

import App
import string
pWeaponLock = {}

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
	kOuterShellColor.SetRGBA(1.000000, 103, 207, 45)
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 94, 118, 6)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.10) 	


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.45)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(85.0)

def GetLaunchSound():
	return("TransphasicPulse")

def GetPowerCost():
	return(1000.0)

def GetName():
	return("Transphasic Pulse")

def GetDamage():
	return 650.0

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 0.025

def GetLifetime():
	return 180.0

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"