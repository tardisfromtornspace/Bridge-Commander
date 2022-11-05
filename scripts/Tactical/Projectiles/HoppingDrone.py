###############################################################################
#		
#	Script for filling in the attributes of Fusion torpedoes.
#	
#	Created:	012/10/04 -	 MRJOHN
###############################################################################

import App
import string
pWeaponLock = {}

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
	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(230.0 / 255.0, 220.0 / 255.0, 78.0 / 255.0, 1.000000)
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(230.0 / 255.0, 245.0 / 255.0, 208.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor, 
					0.175,
					0.93,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					2.8,	
					0.23,	 
					0.47,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					16,		
					0.4,		
					0.20)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(2.50)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

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
	return 25.001

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 150

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.00001

def GetGuidanceLifetime():
	return 700.0

def GetMaxAngularAccel():
	return 7.5


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
                "Andromeda",
                "enterprise",
                "DCMPDefiant",
                "B5Station",
                "Aegean",
                "Aegian",
                "XOverAlteranWarship",
                "XOverAncientCityFed",
                "XOverAncientSatelliteFed",
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

#try:
#    sYieldName = 'Phased Torpedo'
#    import FoundationTech
#    try:
#        oYield = FoundationTech.oTechs[sYieldName]
#        FoundationTech.dYields[__name__] = oYield
#    except:

#        import FoundationTech
#        import ftb.Tech.FedTransphasic
#      
#        sYieldName = ''
#        sFireName = ''

#        oFire = ftb.Tech.FedTransphasic.oTransphasicWeapon
#        FoundationTech.dOnFires[__name__] = oFire
#        FoundationTech.dYields[__name__] = oFire
#        pass
#except:
#    pass

try:
        sYieldName = "Hopping Torpedo"

        import FoundationTech
        import Custom.Techs.HoppingTorp
	#modPhasedTorp = __import__("Custom.Techs.HoppingTorp")
	#if(modPhasedTorp):
	#	modPhasedTorp.oPhasedTorp.AddTorpedo(__name__)

        oFire = Custom.Techs.HoppingTorp.oHoppingTorp
        FoundationTech.dOnFires[__name__] = oFire

        oYield = FoundationTech.oTechs[sYieldName]
        FoundationTech.dYields[__name__] = oYield


except:
	print "Hopping Torpedo script not installed, or you are missing Foundation Tech"