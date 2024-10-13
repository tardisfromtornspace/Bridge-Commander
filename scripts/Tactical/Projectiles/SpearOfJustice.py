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

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(84.0 / 255.0, 67.0 / 255.0, 255.0 / 255.0, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.5, 0.06)
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.43)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(80.0)

def GetLaunchSound():
	return("UndyneRisingSpear")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Spears of Justice")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 11.0

def GetMaxAngularAccel():
	return 8.25


import traceback
try:
	import FoundationTech
	import ftb.Tech.SolidProjectiles
	# The line below is a hypothethical example if you want customized AI - uncomment and adjust accordingly if you want
	#import path.to.tailoredAI.tailoredAIfilename
	#myAIfunction = tailoredAIfilename.CreateAI
	# Remember, if you don't want AI, do not add the "sAI" field.
	random = App.g_kSystemWrapper.GetRandomNumber(100)
	#oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "SpearOfJustice", "sScale" : 5.0, "sShield": 1, "sCollide": 2, "sHideProj": 0, "sTargetable": 1, "sAI": {"AI": None, "Side": "Friendly", "Team": "Friendly"}})
	oFire = ftb.Tech.SolidProjectiles.Rocket('Spatial Projectiles', {"sModel" : "SpearOfJustice", "sScale" : 5.0, "sShield": 1, "sCollide": 0, "sHideProj": 0, "sTargetable": 0}) 
	FoundationTech.dOnFires[__name__] = oFire
	FoundationTech.dYields[__name__] = oFire
except:
	print "Error with firing solid projectile fix"
	traceback.print_exc()