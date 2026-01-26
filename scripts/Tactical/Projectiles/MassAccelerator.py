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
	kOuterShellColor.SetRGBA(0.0/255.0, 180.0/255.0, 255.0/255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(230.0/255.0, 246.0/255.0, 255.0/255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.8, 0.1) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEPHASER)

	return(0)

def GetLaunchSpeed():
	return(80.0)

def GetLaunchSound():
	return("MassAccelerator1")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Mass Accelerator")

def GetDamage():
	return 18.0 # 28.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.05

def GetLifetime():
	return 8.0

def HullDmgMultiplier():
	return 3

def ShieldDmgMultiplier():
	return 3

try:
	modMERailgunWeaponTorp = __import__("Custom.Techs.MERailgunWeapon")
	if(modMERailgunWeaponTorp):
		modMERailgunWeaponTorp.oMERailgunWeaponTorp.AddTorpedo(__name__)
except:
	print "MERailgunWeapon projectile script not installed, or you are missing Foundation Tech"
