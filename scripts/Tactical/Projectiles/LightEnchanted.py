# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
###############################################################################
#	Filename:	Solonite Missile.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
#       Modified:       29/10/2006 -    Lost_Jedi
#                                           Now includes torpedo trails
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
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 135.0 / 255.0, 230.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/EnchantedCore.tga",
					kCoreColor,
					0.25,
					0.05,	 
					"data/Textures/Tactical/EnchantedGlow.tga", 
					kGlowColor,
					0.75,	
					1.5,	 
					1.2,	
					"data/Textures/Tactical/EnchantedCore.tga",
					kFlareColor,										
					50,		
					0.45,		
					0.01)


	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.5)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)
	return(0)

def GetLaunchSpeed():
	return(75.0)

def GetLaunchSound():
	return("LightEnchantedTorp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Light Enchanted")

def GetDamage():
	return 35000.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 5.0