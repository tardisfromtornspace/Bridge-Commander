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
	kOuterShellColor.SetRGBA(1.000000, 0.400000, 0.000001, 0.0005000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.700000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.2, 0.03) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.005)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("DGFire2")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Staff")

def GetDamage():
	return 27.0

def GetGuidanceLifetime():
	return 0.01

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 12.0

def HullDmgMultiplier():
	return 8

def ShieldDmgMultiplier():
	return 8

try:
	modSGPlasmaWeaponTorp = __import__("Custom.Techs.SGPlasmaWeapon")
	if(modSGPlasmaWeaponTorp):
		modSGPlasmaWeaponTorp.oSGPlasmaWeaponTorp.AddTorpedo(__name__)
except:
	print "SGPlasmaWeapon projectile script not installed, or you are missing Foundation Tech"
