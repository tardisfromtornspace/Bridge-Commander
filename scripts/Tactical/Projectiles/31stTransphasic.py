###############################################################################
#		
#	Script for filling in the attributes of Fusion torpedoes.
#	
#	Created:	012/10/04 -	 MRJOHN
###############################################################################

import App
from Custom.Techs.PhasedTorpedoV1 import *


###############################################################################
#	Create(pTorp)
#	
#	Creates a Fusion torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(230.0 / 255.0, 220.0 / 255.0, 78.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(230.0 / 255.0, 245.0 / 255.0, 208.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.175,
					0.93,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.8,	
					0.23,	 
					0.47,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					16,		
					0.4,		
					0.20)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.005)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(100.0)

def GetLaunchSound():
	return("Transphasic")

def GetPowerCost():
	return(90.01)

def GetName():
	return("Transphasic")

def GetDamage():
        # For phasedPlasmaTorp foundation scripts
        return 991.91

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 39991.91

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.70

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.335