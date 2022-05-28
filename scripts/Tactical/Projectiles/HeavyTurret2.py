###############################################################################
#	Filename:	Disruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
#       Modified:       29/10/2006 -    Lost_Jedi
#                                           Now includes torpedo trails
###############################################################################

import App
import LJTorpLib2.LibTorp2

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
	kOuterShellColor.SetRGBA(1.000000, 0.380392, 0.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 0.870588, 0.662745, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.0, 0.21) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)


        ## Add a creation handler to the torpedo :)
        LJTorpLib2.LibTorp2.AddCreationHandler(pTorp, __name__ + ".AttachSmoke")
        return(0)

def AttachSmoke(self, pEvent = None):
    ## Attach Missile Effect
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return (1)
    ## Create and Play a sequence
    LJTorpLib2.LibTorp2.SetupSmokeTrail(pTorpedo)
    return (0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("MainBattery2")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Main Batteries")

def GetDamage():
	return 7.5

def GetGuidanceLifetime():
	return 3.0

def GetMaxAngularAccel():
	return 0.125

def GetLifetime():
	return 5.0

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 7.5

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.00001

global lImmuneShips   #In this case the name could have been VulnerableShips, since it targets those listed below
lImmuneShips = (
                "B5Station",
                "Battlecrab",
                "Blackbird",
                "bluestar",
                "CylonRaider",
                "DamagedWarship",
                "DRA_Raider",
                "Fighter",
                "FPhoenix",
                "GQuan",
                "HeavyRaider",
                "HiveShip",
                "MinbariSharlin",
                "Raptor",
                "Raptor2",
                "Raptor3",
                "Rycon",
                "SentriFighter",
                "ThNor",
                "Thunderbolt",
                "Viper",
                "ViperMk1",
                "ViperMk2",
                "ViperMk7",
                "ViperMkI",
                "VOR_Fighter",
                "WraithDart",
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
