###############################################################################
#	Filename:	PoleronTorp.py
#	By:		edtheborg
###############################################################################
# This torpedo uses the FTA mod...
#
# it actually passes through shields and damages whatever subsystem it was
# targeted at
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App
pWeaponLock = {}

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ChronitomorphicTorp.tga",
					kCoreColor,
					0.1,
					1.2,	 
					"data/Textures/Tactical/ChronitomorphicTorp.tga", 
					kGlowColor,
					8.0,	
					0.375,	 
					0.75,	
					"data/Textures/Tactical/ChronitomorphicTorp.tga",
					kFlareColor,										
					300,		
					1.25,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(65)

def GetLaunchSound():
	return("MultidiquantallicExponensiveDevice")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Multi-diquantallic Exponensive Device")

def GetDamage():
	return 4250000

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 2.75