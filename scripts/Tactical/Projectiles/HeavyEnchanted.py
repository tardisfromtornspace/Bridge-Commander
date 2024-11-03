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
import MissionLib

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
					1.65,
					0.05,	 
					"data/Textures/Tactical/EnchantedGlow.tga", 
					kGlowColor,
					1.5,	
					5.5,	 
					2.2,	
					"data/Textures/Tactical/EnchantedCore.tga",
					kFlareColor,										
					50,		
					3.45,		
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
	return(45.0)

def GetLaunchSound():
	return("HeavyEnchantedTorp")

def GetPowerCost():
	return(3000.0)

def GetName():
	return("Heavy Enchanted")

def GetDamage():
	return 25000.0

# this sets the distance in kilometers at which the torpedo will have the yield set in GetDamage()
def GetDamageDistance():
	return 20

# this sets the maximum damage the torpedo will ever do
def GetMaxDamage():
	return 350000

def GetGuidanceLifetime():
	return 40.0

def GetMaxAngularAccel():
	return 0.25

def TargetHit(pObject, pEvent):
	return

# all the following is the code that actually does the variable damage
# this routine is called by fta when this torpedo is fired
def WeaponFired(pObject, pEvent):
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pTube==None):
		return
	pShip=pTube.GetParentShip()
	if (pShip==None):
		return
	pTarget=pShip.GetTarget()
	if (pTarget==None):
		return
	distance=App.UtopiaModule_ConvertGameUnitsToKilometers(MissionLib.GetDistance(pShip,pTarget))+0.01
	damage=GetDamage()*(GetDamageDistance()/distance)
	if (damage>GetMaxDamage()):
		damage=GetMaxDamage()
	pTorp.SetDamage(damage)
	return