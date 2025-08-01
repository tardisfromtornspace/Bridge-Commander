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
import trails.METrail
import trails.OriBeam

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
	kOuterShellColor.SetRGBA(162.0/255.0, 222.0/255.0, 255.0/255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(232.0/255.0, 247.0/255.0, 255.0/255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 2.0, 0.35) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)
	trails.OriBeam.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")

	return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    trails.OriBeam.SetupSmokeTrail(pTorpedo, 
					sTexture = 'data/Textures/Effects/ExplosionC.tga',
					fFrequency = 0.01,
					fVelocity = 0.1,
					fSize = pTorpedo.GetRadius() * 2,
					#kEmitPos = App.NiPoint3(0, 0, 0),
					#kEmitDir = App.NiPoint3(0, 0, 0),
					sAngleVariance = 60.0,
					sEmitLife = 5.5,
					sEffectLifetime = 8.3,
					sDrawOldToNew = 0,
					#sTargetAb1 = 0,
					#sTargetAb2 = 0,
					pFunction= trails.METrail.DefaultColorKeyFunc
					)
    return (0)


def GetLaunchSpeed():
	return(250.0)

def GetLaunchSound():
	return("MESpinalMassAccelerator")

def GetPowerCost():
	return(25.0)

def GetName():
	return("Spinal Mass Accelerator")

def GetDamage():
	return 82.5

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 0.0

def GetLifetime():
	return 30.0

def HullDmgMultiplier():
	return 7.5

def ShieldDmgMultiplier():
	return 15

try:
	modMERailgunWeaponTorp = __import__("Custom.Techs.MERailgunWeapon")
	if(modMERailgunWeaponTorp):
		modMERailgunWeaponTorp.oMERailgunWeaponTorp.AddTorpedo(__name__)
except:
	print "MERailgunWeapon projectile script not installed, or you are missing Foundation Tech"
