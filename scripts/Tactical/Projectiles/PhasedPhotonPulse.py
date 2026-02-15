###############################################################################
#	Filename:	RepulsionTorp.py
#	By:		edtheborg
###############################################################################
# This torpedo uses the FTA mod...
#
# when a target is hit by this torpedo, the target is repelled at warp speed
# and sent spinning out of control
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App
import MissionLib

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(231.0 / 255.0, 16.0 / 255.0, 86.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1.000000, 0.000000, 0.000000, 1.000000)	
	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,
					0.0,	 
					"data/Textures/Tactical/PhotonPhasXJ.tga", 
					kGlowColor,
					0.1,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/PhotonPhasXJ.tga",
					kGlowColor,										
					20,		
					0.3,		
					0.06)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(2.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(80)

def GetLaunchSound():
	return("PhasedPhotonPulse")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Phased Photon")

def GetDamage():
	return 2400.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.69