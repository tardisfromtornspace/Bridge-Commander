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

import string
pWeaponLock = {}

import traceback

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
	kGlowColor.SetRGBA(250.0 / 255.0, 40.0 / 255.0, 250.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 100.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.38,
					4.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					9.0,	
					0.1,	 
					0.4,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,								
     					200,		
					0.15,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(GetDamageRadiusFactor())
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("QuantumSingularityTorp")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Singularity")

def GetDamage():
	return 4000.0

def GetDamageRadiusFactor():
	return 1.2

def GetGuidanceLifetime():
	return 2.2

def GetMaxAngularAccel():
	return 0.25

def GetDamage():
	return 4000.0

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 8000

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.05


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

def findShipInstance(pShip):
	pInstance = None
	try:
		import Foundation
		import FoundationTech
		if not pShip:
			return pInstance
		if FoundationTech.dShips.has_key(pShip.GetName()):
			pInstance = FoundationTech.dShips[pShip.GetName()]
	except:
		pass

	return pInstance

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
		pAttacker = App.ShipClass_GetObjectByID(None, pTorp.GetParentID())
		if pAttacker:
			finalRadius = pAttacker.GetRadius()
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

	hullDmgBoostMultiplier = (finalRadius + 0.01)/(defenderRadius + 0.01)

	if finalRadius < 5 * defenderRadius:
		hullDmgBoostMultiplier = hullDmgBoostMultiplier * 0.2
	elif finalRadius > 3.14 * 5 * defenderRadius:
		hullDmgBoostMultiplier = hullDmgBoostMultiplier * 3.14 * 1.618 * 2

	if hullDmgBoostMultiplier < 1:
		hullDmgBoostMultiplier = 1

	elif hullDmgBoostMultiplier > 3:
		hullDmgBoostMultiplier = 3
		

### LJ INSERTS - CHECK FOR VULNERABLE SHIP

	pInstance = None
	global lImmuneShips
	sScript     = pShip.GetScript()
	sShipScript = string.split(sScript, ".")[-1]
	if sShipScript in lImmuneShips:
		return
	else:
		pInstance = findShipInstance(pShip)
		if pInstance:
			pInstanceDict = pInstance.__dict__
			if pInstanceDict:
				if pInstanceDict.has_key("Singularity Dmg modulator"):
					if pInstanceDict["Singularity Dmg modulator"] <= 0:
						return
					else:
						hullDmgBoostMultiplier = hullDmgBoostMultiplier * pInstanceDict["B5 Jumppoint Dmg modulator"]
	######################################
	if (pSubsystem==None):
		return
	myDamage=pSubsystem.GetMaxCondition()*GetPercentage()
	if (myDamage<(GetMinDamage() * hullDmgBoostMultiplier)):
		myDamage=GetMinDamage() * hullDmgBoostMultiplier
	sysCondition = pSubsystem.GetCondition()
	if (sysCondition>myDamage):
		if not pInstance:
			pSubsystem.SetCondition(sysCondition-myDamage)
	else:
		myDamage=sysCondition+1
		if not pInstance:
			pSubsystem.SetCondition(-1)
			if not (pShip.IsInvincible() and pSubsystem.IsCritical()):
				pShip.DestroySystem(pSubsystem)

	if pInstance:
		try:
			import Custom.Techs.MEShields

			pEvent1 = Custom.Techs.MEShields.TGFakeWeaponHitEvent_Create() # Our "fake" event
			pEventSource = pTorp
			pEventDestination = pShip

			pEvent1.SetSource(pEventSource)
			pEvent1.SetDestination(pEventDestination)
			pEvent1.SetEventType(App.ET_WEAPON_HIT)

			pEvent1.SetFiringObject(pAttacker)
			pEvent1.SetTargetObject(pShip)

			myHullPos = Custom.Techs.MEShields.NiPoint3ToTGPoint3(pSubsystem.GetPosition())

			pEvent1.SetObjectHitPoint(myHullPos)

			pShipPositionV = pShip.GetWorldLocation()
			pShipPositionVI = Custom.Techs.MEShields.TGPoint3ToNiPoint3(pShipPositionV, -1.0)
			pShipNode = pShip.GetNiObject()

			pEvent1.SetObjectHitNormal(pShipPositionVI) 
			pEvent1.SetWorldHitPoint(myHullPos)
			pShipPositionVW = Custom.Techs.MEShields.TGPoint3ToNiPoint3(App.TGModelUtils_LocalToWorldUnitVector(pShipNode, pShipPositionVI), 1.0)
			pEvent1.SetWorldHitNormal(pShipPositionVW)

			eCondition = 1.0
			if pSubsystem:
				eCondition = pSubsystem.GetConditionPercentage()
			pEvent1.SetCondition(eCondition)
			valPlus = Custom.Techs.MEShields.torpCountersForInstance + 1

			pEvent1.SetWeaponInstanceID(valPlus) # Not needed... at least, I am not aware of any scripts handling it for torpedo defense

			myRadius = GetDamageRadiusFactor()
			pEvent1.SetRadius(myRadius)
			pEvent1.SetDamage(myDamage)
			pEvent1.SetHullHit(1)
			pEvent1.SetFiringPlayerID(0)

			affectedSys, nonTargetSys = Custom.Techs.MEShields.FindAllAffectedSystems(pShip, myHullPos, myRadius)
			Custom.Techs.MEShields.AdjustListedSubsystems(pShip, affectedSys, nonTargetSys, -myDamage, len(affectedSys) + 1, 1)

			pInstance.DefendVSTorp(pShip, pEvent1, pTorp)
		except:
			traceback.print_exc()
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
