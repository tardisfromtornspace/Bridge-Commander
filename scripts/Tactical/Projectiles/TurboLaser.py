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
	kOuterShellColor.SetRGBA(1.000000, 0.400000, 0.000001, 0.0005000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.700000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.15) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(95.0)

def GetLaunchSound():
	return("Pulse PhaserJLH")

def GetPowerCost():
	return(10.0)

def GetName():
	return("TurboLaser")

def GetDamage():
	return 50.0

def GetLifetime():
	return 3.0

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 20

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.00001

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.05

global lImmuneShips   #In this case the name could have been VulnerableShips, since it targets those listed below
lImmuneShips = (
                "ancientshuttle",
                "AndArchlike",
                "AndSlipfighter",
                "AstralQueen",
                "B5Station",
                "Battlecrab",
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
                "DamagedWarship",
                "DRA_Raider",
                "EAOmega",
                "Fighter",
                "FPhoenix",
                "Galactica",
                "GalacticaClosed",
                "GalaticaBS75",
                "GemTrans",
                "GemTrav",
                "GoauldAlkesh",
                "GoauldStarbase",
                "GQuan",
                "GQuanKlingonRefit",
                "GraceShip",
                "GraceShip2",
                "HadesBasestar",
                "HadesBasestar2003",
                "HeavyRaider",
                "HebridanDrone",
                "HiveShip",
                "Horizon",
                "jclass",
                "jclasspod",
                "jclasstug",
                "MartinLloydsShip",
                "MartinsShip",
                "MilkyWayInactive",
                "Mk10Raider",
                "MkXRaider",
                "OsirisCruiser",
                "PegInactive",
                "Primus",
                "Prometheus",
                "Raptor",
                "Raptor2",
                "Raptor3",
                "Rycon",
                "SentriFighter",
                "Solaria",
                "SuperHiveShip",
                "TelTak",
                "TENeptune",
                "ThNor",
                "Thunderbolt",
                "TOSColDefender",
                "Viper",
                "ViperMk1",
                "ViperMk2",
                "ViperMk7",
                "ViperMkI",
                "VOR_Fighter",
                "Vorchan",
                "Warlock",
                "WraithDart",
                "WraithCruiser",
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
	if (pShip.IsDead()) or (pShip.IsDying()):
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
