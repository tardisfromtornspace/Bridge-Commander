###############################################################################
#	Filename:	DeltaBorg.py
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
#	Creates a Alpha torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(55.0 / 255.0, 655.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(55.0 / 255.0, 655.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(55.0 / 255.0, 655.0 / 255.0, 0.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/Quantum01.tga",
					kCoreColor, 
					0.06,
					0.05,	 
					"data/Textures/Tactical/Micro01Glow.tga", 
					kGlowColor,
					0.25,	
					0.2,	 
					0.2,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					42,		
					0.05,		
					0.25)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.Alpha)

	return(0)

def GetLaunchSpeed():
	return(25)

def GetLaunchSound():
	return("BreenP")

def GetPowerCost():
	return(6.0)

def GetName():
	return("Breen Pulse")

def GetDamage():
	return 250.0

def GetGuidanceLifetime():
	return 9.0

def GetMaxAngularAccel():
	return 0.03

def GetLifetime():
	return 19.0

