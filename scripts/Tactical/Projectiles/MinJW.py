###############################################################################
#	Filename:	PositronTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of positron torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App
import string
pWeaponLock = {}

###############################################################################
#	Create(pTorp)
#	
#	Creates a positron torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 82.0 / 255.0, 255.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					1.2,
					2.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					8.0,	
					3.6,	 
					6.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					12,		
					3.4,		
					0.8)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.20)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.POSITRON)

	return(0)

def GetLaunchSpeed():
	return(40.0)

def GetLaunchSound():
	return("Positron Torpedo")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Jumpspace Tunnel")

def GetDamage():
	return 8000.0

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 8000

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.00001

def GetGuidanceLifetime():
	return 0.1

def GetMaxAngularAccel():
	return 9.9

global lImmuneShips   #Tardis is immune because it's the TARDIS, a wormhole is not gonna appear inside the ship, Borg ships because of the subspace shields which may interfere with the formation of a jump-point inside the cube, super-future ships because they may have adapted to that too, the Thirdspace aliens and some First Ones to be more scary, and that odd Hatak there because of another mod where a Hatak is powered by Harry Potter energy blocking teleporting and wormholes or something.
lImmuneShips = (
                "Tardis",
                "BorgCube",
                "BorgDiamond",
                "HaririrHatak",
                "DS9FXBorgDetector",
                "LowCube",
                "sphere",
                "vger",
                "VulcanXRT55D",
                "EnterpriseJ",
                "ThirdspaceCapitalShip",
                "B5TriadTriumviron",
                "SigmaWalkerScienceLab",
                "MindridersThoughtforce",
                "TorvalusDarkKnife",
                "VOR_Planetkiller",
                )

def TargetHit(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pShip==None):
		return
	try:
		id=pTorp.GetObjID()
		pSubsystem=pWeaponLock[id]
		del pWeaponLock[id]
	except:
		pSubsystem=pShip.GetHull()

### LJ INSERTS - CHECK FOR VULNERABLE SHIP
	global lImmuneShips
	sScript     = pShip.GetScript()
	sShipScript = string.split(sScript, ".")[-1]
	if sShipScript in lImmuneShips:
		return
	######################################
	if (pSubsystem==None):
		return
	Dmg=pSubsystem.GetMaxCondition()*GetPercentage()
	if (Dmg<GetMinDamage()):
		Dmg=GetMinDamage()
	if (pSubsystem.GetCondition()>Dmg):
		pSubsystem.SetCondition(pSubsystem.GetCondition()-Dmg)
	else:
		pShip.DestroySystem(pSubsystem)
	return
	######################################


def WeaponFired(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pTube==None):
		return
	pShip=pTube.GetParentShip()
	if (pShip==None):
		return
	try:
		pWeaponLock[pTorp.GetObjID()]=pShip.GetTargetSubsystem()
	except:
		return
	return

