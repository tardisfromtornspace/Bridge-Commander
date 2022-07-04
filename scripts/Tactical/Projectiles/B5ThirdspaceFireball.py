###############################################################################
#	Filename:	Disruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App
import string
pWeaponLock = {}

###############################################################################
#	Create(pTorp)
#	
#	Creates a disruptor blast.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.500000, 0.500000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.450000, 0.450000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 4.0, 0.4) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.09)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(30.0)

def GetLaunchSound():
	return("Centbeam Start")

def GetPowerCost():
	return(10.0)

def GetName():
	return("B5Thirdspace Fireball")

def GetDamage():
	return 1500.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.3

def GetLifetime():
	return 38.0

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 10

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.00001

global lImmuneShips   #In this case the name could have been VulnerableShips, since it targets those listed below
lImmuneShips = (
                "AstralQueen",
                "Battlestar",
                "Blackbird",
                "bluestar",
                "Celestra",
                "Cloud9",
                "Col1",
                "ColAgro",
                "ColDefender",
                "ColLine1",
                "ColLine2",
                "ColLine3",
                "ColLine4",
                "ColLine5",
                "ColLine6",
                "ColMvr1",
                "ColRef",
                "ColShuttle",
                "ColTube1",
                "CylonBasestar",
                "CylonRaider",
                "Galactica",
                "GalacticaClosed",
                "GalaticaBS75",
                "GQuan",
                "SentriFighter",
                "SuperHiveShip",
                "TOSColDefender",
                "VOR_Fighter",
                "Vorlon_Fighter",
                "WraithDart",
                "WraithCruiser",
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
	if sShipScript not in lImmuneShips:
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