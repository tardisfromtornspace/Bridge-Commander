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

global lImmuneShips   #In this case the name could have been VulnerableShips, since it targets those listed below
lImmuneShips = (
                "aaAssaultFrigate",
                "aaBulkCruiser",
                "aaBulkFreighter",
                "aaCarrack",
                "aaCorevette",
                "aaCorgun",
                "aaDreadnaught",
                "aaEscortCarrier",
                "aaLancerFrigate",
                "aaMarauderCorvette",
                "aaMobquet",
                "aaModCorvette",
                "aaModifiedNebulonB",
                "aaModularConveyor",
                "aaNebulonB",
                "aaStarGalleon",
                "aaStrikeCruiser",
                "aaSuprosa",
                "aaXiytiar",
                "ActiveSupergate",
                "Alkesh",
                "AlkeshTransport",
                "AncientCruiser",
                "AncientSatellite",
                "ancientshuttle",
                "AndArchlike",
                "AndSlipfighter",
                "AncientWarship",
                "AnubisFlagship",
                "ApophisFlagship",
                "AshenShuumtian",
                "AstralQueen",
                "B5Station",
                "Battlecrab",
                "Battlestar",
                "bcjjenterprisev3",
                "Beliskner",
                "BelisknerRefit",
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
                "Daedalus",
                "DamagedSatellite",
                "DamagedWarship",
                "Dart1",
                "Dart2",
                "Dart3",
                "Dart4",
                "Dart5",
                "Dart6",
                "Dart7",
                "Dart8",
                "Dart9",
                "Dart10",
                "Dart11",
                "Dart12",
                "DeathStarII",
                "destiny",
                "destinymain",
                "DKir",
                "DRA_Raider",
                "EAOmega",
                "EarlyHatak",
                "FedConstOpen",
                "Fighter",
                "FPhoenix",
                "Flagship",
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
                "HatakRefit",
                "HatakVariant",
                "HeavyRaider",
                "HebridanDrone",
                "HiveShip",
                "Horizon",
                "ImperatorIII",
                "IntersunLine",
                "ISS",
                "jclass",
                "jclasspod",
                "jclasstug",
                "JediStarfighter",
                "Kumari",
                "lambdashuttle",
                "MartinLloydsShip",
                "MartinsShip",
                "MidwayStation",
                "MilkyWayInactive",
                "Millenium",
                "MinbariSharlin",
                "Mk10Raider",
                "MkXRaider",
                "naboofighter",
                "NeedleThreader",
                "Odyssey",
                "OriFighter",
                "OriSatellite",
                "OriWarship",
                "OsirisCruiser",
                "Pegasus",
                "PegInactive",
                "PlanetExpress",
                "Primus",
                "Prometheus",
                "PrometheusRefit",
                "PrometheusUpgrade",
                "PuddleJumper",
                "PyramidShip",
                "Raptor",
                "Raptor2",
                "Raptor3",
                "ReplicatorBeliskner",
                "ReplicatorHatak",
                "ReplicatorVessel",
                "Rycon",
                "SentriFighter",
                "SFRD_Promellian",
                "SGGalacticaRefit",
                "SLAVE1",
                "Solaria",
                "SpaceFacility",
                "Supergate",
                "SuperHiveShip",
                "Superweapon",
                "Surrok",
                "TelTak",
                "TelTakRefit",
                "TelTakUpgrade",
                "TelTakVariant",
                "TENeptune",
                "ThNor",
                "Thunderbolt",
                "TOSColDefender",
                "UpgradedHatak",
                "venator",
                "venimp",
                "Vicstar",
                "Victory",
                "Viper",
                "ViperMk1",
                "ViperMk2",
                "ViperMk7",
                "ViperMkI",
                "VOR_Fighter",
                "Vorchan",
                "Warlock",
                "whitestar",
                "WraithDart",
                "WraithCruiser",
                "X301",
                "x303",
                "X303Refit",
                "X303Upgrade",
                "XInsect",
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

