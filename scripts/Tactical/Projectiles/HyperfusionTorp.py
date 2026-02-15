###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	
###############################################################################

import App

###############################################################################
#	
#	
#	
#	
#	
#	
#	
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(225.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(60.0 / 255.0, 100.0 / 255.0, 240.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(225.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/AlphaQuantumCore.tga",
					kCoreColor, 
					0.5,
					0.93,	 
					"data/Textures/Tactical/HyperfusionGlow.tga", 
					kGlowColor,
					3.0,	
					2.3,	 
					1.85,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					150,		
					0.54,		
					0.08) 

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(5.5)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(90)

def GetLaunchSound():
	return("HyperfusionTorpedo")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Hyperfusion Torpedoes")

def GetDamage():
	return 750000.0

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 0.075

def GetFlashColor():
	return (255.0, 0.0, 0.0)