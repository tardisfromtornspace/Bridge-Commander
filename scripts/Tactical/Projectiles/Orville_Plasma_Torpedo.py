	###############################################################################
#	Filename:	PatriotQuantum.py
#	
#	
#	Created:	17/10/05 -	RBE
###############################################################################

import App
import LJTorpLib2.LibTorp2

###############################################################################
#	Create(pTorp)
#	
#	Creates a quantum torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(35.0 / 255.0, 70.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(165.0 / 255.0, 165.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/AdvQuantumCore.tga",
					kCoreColor, 
					0.3,
					5.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					5.0,	
					0.5,	 
					0.75,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,									
					0,		
					0.1,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

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
	return(75.0)

def GetLaunchSound():
	return("OrvillePlasmaTorpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Plasma Torpedoes")

def GetDamage():
	return 300.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 8.0
