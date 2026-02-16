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
	kCoreColor.SetRGBA(190.0 / 255.0, 240.0 / 255.0, 230.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(120.0 / 255.0, 255.0 / 255.0, 250.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(150.0 / 255.0, 195.0 / 255.0, 174.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					4.0,	 
					"data/Textures/Tactical/BioElectricDischarge.tga", 
					kGlowColor,
					1.0,	
					1.0,	 
					1.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,								
     				20,		
					0.45,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("26cBioElectricDischarge")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Bio Electric Discharge")

def GetDamage():
	return 12000.0

def GetGuidanceLifetime():
	return 8.0

def GetMaxAngularAccel():
	return 0.95

def GetLifetime():
	return 100.0