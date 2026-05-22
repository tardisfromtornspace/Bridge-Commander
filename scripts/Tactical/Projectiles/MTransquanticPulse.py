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
import string
pWeaponLock = {}

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
	kOuterShellColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 4.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(85.0 / 255.0, 150.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 40.0, 0.15) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.7)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(320.0)

def GetLaunchSound():
	return("TransquanticPulse")

def GetPowerCost():
	return(5.0)

def GetName():
	return("MTransquanticPulse")

def GetDamage():
	return 2000.0 * 4

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 0.2

try:
	modTransphasicTorp = __import__("Custom.Techs.TransphasicTorp")
	if(modTransphasicTorp):
		modTransphasicTorp.oTransphasicTorp.AddTorpedo(__name__)
except:
	print "Transphasic Torpedo script not installed, or you are missing Foundation Tech"