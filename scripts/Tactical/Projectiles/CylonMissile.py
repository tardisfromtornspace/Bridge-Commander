###############################################################################
#	Filename:	Solonite Missile.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
#       Modified:       29/10/2006 -    Lost_Jedi
#                                           Now includes torpedo trails
###############################################################################

import App
import LJTorpLib.LibTorp

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
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(84.0 / 255.0, 67.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(84.0 / 255.0, 67.0 / 255.0, 255.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/c2xtorpedo.tga",
					kCoreColor,
					0.45,
					0.60,	 
					"data/Textures/Tactical/c2xtorpedo.tga", 
					kGlowColor,
					4.0,	
					0.35,	 
					0.675,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					0,		
					0.0,		
					0.0)


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)


        ## Add a creation handler to the torpedo :)
        LJTorpLib.LibTorp.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
	return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    LJTorpLib.LibTorp.SetupSmokeTrail(pTorpedo)
    return (0)


def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("MissileFire")

def GetPowerCost():
	return(500.0)

def GetName():
	return("Cylon Missile")

def GetDamage():
	return 5.0

def GetGuidanceLifetime():
	return 60.0

def GetMaxAngularAccel():
	return 4.0
