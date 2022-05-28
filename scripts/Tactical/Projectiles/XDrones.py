###############################################################################
#	Filename:	XDrones.py
#	By:		edtheborg and others
###############################################################################
# This torpedo uses the FTA mod...
#
# it actually passes through shields and damages whatever subsystem it was
# targeted at
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App
import string
pWeaponLock = {}

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.823000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.3, 0.05) 	
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

def GetLifetime():
        return 300

def GetLaunchSpeed():
	return(300)

def GetLaunchSound():
	return("Drone")

def GetPowerCost():
	return(500.0)

def GetName():
	return("What if...? SuperDrone")

def GetDamage():
	return 20.0001

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 800

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.0001

def GetGuidanceLifetime():
	return 300.0

def GetMaxAngularAccel():
	return 17.5


global lImmuneShips
lImmuneShips = (
                "Satellite",
                "Sovereign",
                "AMVogager",
                "ArmoredVoyager",
                "BorgDiamond",
                "CA8472",
                "Firebird",
                "DJEnterpriseG",
                "GalaxyX",
                "EnterpriseF",
                "EnterpriseJ",
                "Excalibur",
                "Tardis",
                "DRA_Raider",
                "enterprise",
                "DCMPDefiant",
                "AncientCity",
                "Atlantis",   
                "VulcanXRT55D",
                "MvamPrometheus",
                "novaII",
                "WCNemEntE",
                "WCNemEntEnoyacht",  
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

	### LJ INSERTS - CHECK FOR IMMUNE SHIP
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
