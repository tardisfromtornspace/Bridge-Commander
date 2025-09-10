###############################################################################
#	Filename:	Disruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
#       Modified:       29/10/2006 -    Lost_Jedi
#                                           Now includes torpedo trails
#                       10/9/2025 -    CharaToLoki
#                                           Power and tech adjustments
###############################################################################

import App
import LJTorpLib2.LibTorp2

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
	kOuterShellColor.SetRGBA(1.000000, 0.380392, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.870588, 0.662745, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.5, 0.1) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.125)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	
        ## Add a creation handler to the torpedo :)
        LJTorpLib2.LibTorp2.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
        return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    LJTorpLib2.LibTorp2.SetupSmokeTrail(pTorpedo)
    return (0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("MainBattery")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Main Batteries")

def GetDamage():
	return 1.8

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 15.0

def HullDmgMultiplier():
	return 2.78

def ShieldDmgMultiplier():
	return 2.8

try:
	modMERailgunWeaponTorp = __import__("Custom.Techs.MERailgunWeapon")
	if(modMERailgunWeaponTorp):
		modMERailgunWeaponTorp.oMERailgunWeaponTorp.AddTorpedo(__name__)
except:
	print "MERailgunWeapon projectile script not installed, or you are missing Foundation Tech"
