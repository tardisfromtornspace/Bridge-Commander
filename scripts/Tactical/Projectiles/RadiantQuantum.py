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
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 0.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 185.0 / 255.0, 185.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 185.0 / 255.0, 185.0 / 255.0, 0.100000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NemQuantumCore.tga",
					kCoreColor, 
					0.2,
					3.0,	 
					"data/Textures/Tactical/NemQuantumGlow.tga", 
					kGlowColor,
					4.0,	
					3.8,	 
					4.4,	
					"data/Textures/Tactical/NemQuantumBlank.tga",
					kFlareColor,								
					0,		
					0.15,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.3)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(55.0)

def GetLaunchSound():
	return("26thCenturyQuantum")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Advanced Quantum")

def GetDamage():
	return 8400.0

def GetGuidanceLifetime():
	return 20.0

def GetMaxAngularAccel():
	return 1.4
