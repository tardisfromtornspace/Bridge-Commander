###############################################################################
#	Filename:	KazonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
#
#	Modified by:	Queball - 5/12/2003
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
	kCoreColor.SetRGBA(253.0 / 255.0, 255.0 / 255.0, 213.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(253.0 / 255.0, 255.0 / 255.0, 204.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(80.0 / 255.0, 120.0 / 255.0, 70.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.2,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					0.2,	 
					0.7,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					15,		
					0.05,		
					0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.KAZONTORPEDO)

	return(0)

def GetLaunchSpeed():
	return(39.0)

def GetLaunchSound():
	return("Sona Photon")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Kazon Torpedo")

def GetDamage():
	return 700.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.4
