# THIS FILE IS NOT SUPPORTED BY ACTIVISION
###############################################################################
#		
#	Script for filling in the attributes of Fusion torpedoes.
#	
#	Created:	012/10/04 -	 MRJOHN
###############################################################################

import App
import string
pWeaponLock = {}

"""
# if you want the ship to be immune to this weapon, add this at the end of your scripts/ships file
def IsStargateDroneImmune():
	return 1
"""

###############################################################################
#	Create(pTorp)
#	
#	Creates a Fusion torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	
	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(1.000000, 0.823000, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.15, 0.025) 	
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
        return 60

def GetLaunchSpeed():
	return(25.0)

def GetLaunchSound():
	return("Drone")

def GetPowerCost():
	return(500)

def GetName():
	return("Drone")

def GetDamage():
	return 50.001

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 200
# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.001

def GetGuidanceLifetime():
	return 700.0

def GetMaxAngularAccel():
	return 7.5


global lImmuneShips
lImmuneShips = (
                "Aegean",
                "Aegian",
                "AMVogager",
                "AncientCity",
                "Andromeda",
                "ArmoredVoyager",
                "Atlantis",
                "B5LordShip",
                "B5TriadTriumviron",
                "BattleTardis",
                "bcnarada",
                "BorgDiamond",
                "CA8472",
                "crossfield31",
                "DalekEmperorSaucer",
                "DalekGenesisArk",
                "DalekVoidShip",
                "DanielJackson",
                "DCMPDefiant",
                "DJEnterpriseG",
                "DJEnterpriseGDrive",
                "DJEnterpriseGSaucer",
                "DSC304Apollo",
                "DSC304ApolloRefit",
                "DSC304ApolloRefitS",
                "DSC304Daedalus",
                "DSC304DaedalusRefit",
                "DSC304DaedalusRefitS",
                "DSC304SunTzu",
                "DSC304SunTzuRefit",
                "DSC304SunTzuRefitS",
                "DSC304Korolev",
                "DSC304Odyssey",
                "DSC304OdysseyRefit",
                "DSC304OdysseyUpgrade",
                "DyExcalibur",
                "GalaxyX",
                "Enterprise",
                "EnterpriseF",
                "EnterpriseG",
                "EnterpriseH",
                "EnterpriseI",
                "EnterpriseJ",
                "Excalibur",
                "Firebird",
                "janeway",
                "Korolev",
                "MindridersThoughtforce",
                "MvamPrometheus",
                "MvamPrometheusDorsal",
                "MvamPrometheusSaucer",
                "MvamPrometheusVentral",
                "novaII",
                "Odyssey",
                "OdysseyRefit",
                "OdysseyUpgrade",
                "ONeill",
                "OdysseyRefit",
                "OdysseyUpgrade",
                "PsVoyagerA",
                "Satellite",
                "Sovereign",
                "Supership",
                "Tardis",
                "TardisType89",
                "ThirdspaceCapitalShip",
                "Valhalla",
                "VulcanXRT55D",
                "WCNemEntE",
                "Wells",
                "Windrunner",
                "WCNemEntEnoyacht",  
                "XOverAlteranWarship",
                "XOverAncientCityFed",
                "XOverAncientSatelliteFed",
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

	pSubsystem = None
	try:
		id=pTorp.GetObjID()
		pSubsystem=pWeaponLock[id]
		del pWeaponLock[id]
	except:
		pSubsystem = None
		try:
			pParentID = pTorp.GetParentID()
			if pParentID != None and pParentID != App.NULL_ID:
				pParentShip = App.ShipClass_GetObjectByID(None, pParentID)
				if pParentShip and not pParentShip.IsDead():
					pSubsys=pParentShip.GetTargetSubsystem()
					if pSubsys and hasattr(pSubsys, "GetParentShip"):
						pNewTarget = pSubsys.GetParentShip()
						if pNewTarget and hasattr(pNewTarget, "GetObjID"):
							pShip3ID = pNewTarget.GetObjID()
							if (pShip3ID != None) and (pShip3ID != App.NULL_ID) and (pShip3ID == targetID):
								pSubsystem = pSubsys

			if pSubsystem == None:
				pSubsystem=pShip.GetHull()
		except:
			pSubsystem=pShip.GetHull()

	### LJ + ALEX SL GATO INSERTS - CHECK FOR IMMUNE SHIP
	global lImmuneShips

	sScript     = pShip.GetScript()
	sShipScript = string.split(sScript, ".")[-1]

	pShipModule =__import__(sScript)
	pShields = pShip.GetShields()
	if pShields and (hasattr(pShipModule, "IsStargateDroneImmune") or sShipScript in lImmuneShips):
		# print "the target is immune to drones via ship script"
		shieldsStrong = 6
		for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
			fCurr = pShields.GetCurShields(shieldDir)
			fMax = pShields.GetMaxShields(shieldDir)
			if fMax == 0.0 or (fCurr < 0.3 * fMax):
				shieldsStrong = shieldsStrong - 1
		if shieldsStrong > 3:
			for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
				fCurr = pShields.GetCurShields(shieldDir)
				fMax = pShields.GetMaxShields(shieldDir)
				fCurr = fCurr - (GetMinDamage()/6.0)
				if fCurr <= 0.0:
					fCurr = 0.0
				elif fCurr > fMax:
					fCurr = fMax
				pShields.SetCurShields(shieldDir, fCurr)
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

def RicochetChance(): # Chance of the projectile to do a comeback
	return 92

try:
	modSGRealisticHoppingTorp = __import__("Custom.Techs.SGRealisticHoppingTorp")
	if(modSGRealisticHoppingTorp):
		modSGRealisticHoppingTorp.oSGRealisticHoppingTorp.AddTorpedo(__name__, RicochetChance())

except:
	print "SG Hopping Torpedo script not installed, or you are missing Foundation Tech"