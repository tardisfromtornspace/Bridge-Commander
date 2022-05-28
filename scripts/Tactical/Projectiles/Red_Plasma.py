###############################################################################
#	Filename:	PhasedPlasma.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of antimatter torpedoes.
#	
#	Created:	07/3/01 -	Evan Birkby
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a Phased Plasma torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(215.0 / 255.0, 35.0 / 255.0, 35.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(80.0 / 255.0, 60.0 / 255.0, 100.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.09,
					7.2,	 
					"data/Textures/Tactical/cmdr1glow.tga", 
					kGlowColor,
					9.9,	
					0.09,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares2.tga",
					kFlareColor,										
					29,		
					0.25,		
					0.1)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.62)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(25)

def GetLaunchSound():
	return("Antimatter Torpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Red Plasma Torp")

def GetDamage():
	return 5990.0

def GetGuidanceLifetime():
	return 30.0

def GetMaxAngularAccel():
	return 0.26
