###############################################################################
#	Filename:	PhotonTorpedo2.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	10/29/01 -	Evan Birkby
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
	"""
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.2,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.3,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					8,		
					0.7,		
					0.4)

	"""

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(84.0 / 255.0, 67.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.5, 0.06)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.53)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Send Ambassadors")

def GetDamage():
	return 7500.0

def GetGuidanceLifetime():
	return 11.0

def GetMaxAngularAccel():
	return 3.7


import traceback
try:
	import FoundationTech
	import ftb.Tech.SolidProjectiles
	# The line below is a hypotehthical example if you want customized AI - uncomment and adjust accordingly if you want
	#import path.to.tailoredAI.tailoredAIfilename
	#myAIfunction = tailoredAIfilename.CreateAI
	# Remember, if you don't want AI, do not add the "sAI" field.
	oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "ambassador", "sScale" : 1.0, "sShield": 1, "sCollide": 2, "sHideProj": 0, "sTargetable": 1, "sAI": {"AI": None, "Side": "Friendly", "Team": "Friendly"}})
	#oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "ambassador", "sScale" : 1.0, "sShield": 1, "sCollide": 2, "sHideProj": 0, "sTargetable": 1}) 
	FoundationTech.dOnFires[__name__] = oFire
	FoundationTech.dYields[__name__] = oFire
except:
	print "Error with firing solid projectile"
	traceback.print_exc()