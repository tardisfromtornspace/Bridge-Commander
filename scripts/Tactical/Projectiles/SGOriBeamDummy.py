###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App
import trails.OriBeam

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 200.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.1) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(2.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)
	pTorp.SetLifetime(0.0)
	trails.OriBeam.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
	return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    trails.OriBeam.SetupSmokeTrail(pTorpedo)
    return (0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("OriBeam Loop")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Jumpspace Tunnel")

def GetDamage():
	return 63.75 #85.0 #63.75

def GetGuidanceLifetime():
	return 0.0 #100.0

def GetMaxAngularAccel():
	return 0.0 #9999.7 # 0.0 would be the correct one tho