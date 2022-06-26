###############################################################################
#	Filename:	Fusion Missile.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App
import Custom.NanoFXv2.NanoFX_ScriptActions

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
	kCoreColor.SetRGBA(240.0 / 255.0, 60.0 / 255.0, 10.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(180.0 / 255.0, 40.0 / 255.0, 40.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(80.0 / 255.0, 120.0 / 255.0, 70.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.02,
					0.05,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.0,	
					0.01,	 
					0.035,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					0,		
					0.1,		
					0.05)


	## Attach smoke to it ????

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(69.0)

def GetLaunchSound():
	return("EA_Torp1")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Fusion Missile")

def GetDamage():
	return 160.0

def GetGuidanceLifetime():
	return 16.0

def GetMaxAngularAccel():
	return 8.5

def IsRocket():
	return 1
