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

import traceback

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
	kGlowColor.SetRGBA(0.0 / 255.0, 100.0 / 255.0, 255.0 / 255.0, 1.000000)
	#kGlowColor.SetRGBA(10.0 / 255.0, 6.5 / 255.0, 2.3 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 255.0 / 255.0, 0.8000000)
	#kFlareColor.SetRGBA(10.0 / 255.0, 6.5 / 255.0, 2.3 / 255.0, 1.0000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					1.1,
					2.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					8.0,	
					5.6,	 
					6.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					1200,		
					3.6,		
					1.99)

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
	return 4000.0

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 8000

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.05

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

	targetID = pShip.GetObjID()
	if targetID == None or targetID == App.NULL_ID:
		return
	pShip2 = App.ShipClass_GetObjectByID(None, targetID)
	if (pShip2==None):
		return

	pAttacker = None
	finalRadius = 1.0
	defenderRadius = pShip.GetRadius()

	try:
		import impactEffects.ImpactTexture
	
		defaultCk = [1, 1, 1]


		baseTexture = 'scripts/Custom/Jumpspace/GFX/JumpspaceFlashAlternate.tga'
		pAttacker = App.ShipClass_GetObjectByID(None, pTorp.GetParentID())
		if pAttacker:
			finalRadius = pAttacker.GetRadius() * 5 #* 50 # TO-DO REMOVE THIS "* 50" LINE

			pSet = pAttacker.GetContainingSet()
			if pSet and hasattr(pSet, "GetName") and pSet.GetName() == "JumpspaceTunnel1" or pSet.GetName() == "JumpspaceTunnel":
				baseTexture = 'scripts/Custom/Jumpspace/GFX/JumpspaceFlash.tga'

		impactEffects.ImpactTexture.DriveEnterFlash(None, pShip.GetObjID(), None, amount=1, sparkSize=1, sFile = baseTexture, sFileFrameW = 4, sFileFrameH = 4, colorKey=defaultCk, pAttachTo = pTorp, pEmitFrom = pTorp, fSize = finalRadius, fFrequency=1,fEmitLife=1,fSpeed=1.0, fLife=1)
	except:
		traceback.print_exc()

	if pShip.IsDead() or pShip.IsDying():
		return

	try:
		id=pTorp.GetObjID()
		pSubsystem=pWeaponLock[id]
		del pWeaponLock[id]
	except:
		pSubsystem=pShip.GetHull()

	hullDmgBoostMultiplier = (finalRadius + 0.01)/(pShip.GetRadius() + 0.01)

	if finalRadius < 5 * defenderRadius:
		hullDmgBoostMultiplier = hullDmgBoostMultiplier * 0.2
	elif finalRadius > 3.14 * 5 * defenderRadius:
		hullDmgBoostMultiplier = hullDmgBoostMultiplier * 3.14 * 1.618 * 2

	if hullDmgBoostMultiplier < 1:
		hullDmgBoostMultiplier = 1

	if not pAttacker:
		hullDmgBoostMultiplier = 0.001
		

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
	if (Dmg<(GetMinDamage() * hullDmgBoostMultiplier)):
		Dmg=GetMinDamage() * hullDmgBoostMultiplier
	if (pSubsystem.GetCondition()>Dmg):
		pSubsystem.SetCondition(pSubsystem.GetCondition()-Dmg)
	else:
		pSubsystem.SetCondition(-1)
		if not (pShip.IsInvincible() and pSubsystem.IsCritical()):
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

