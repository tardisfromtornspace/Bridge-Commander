###############################################################################
#	Filename:	HyperonTorpedo.py
#	Date:		10-22-2004
#	Descr:		Hyperon shield-draining torpedoes
#	By:		ed
#	
#	Requires: Future Technology Addition's script torpedo support
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App

###############################################################################
#	
#	
#	
#	
#	
#	
#	
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 0.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 252.0 / 255.0, 100.0 / 255.0, 1.000000)	
	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,
					0.0,	 
					"data/Textures/Tactical/QuantumX.tga", 
					kGlowColor,
					0.1,	
					0.3,	 
					0.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					4,		
					0.1,		
					0.08)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.19)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(60)

def GetLaunchSound():
	return("ftsChronoton")

def GetPowerCost():
	return(40.0)

def GetName():
	return("WarTorpedo")

def GetDamage():
	return 600.0

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 1.17

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 200

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.61

def TargetHit(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip==None):
		return

	targetID = pShip.GetObjID()
	if targetID == None or targetID == App.NULL_ID:
		return
	pTarget = App.ShipClass_GetObjectByID(None, targetID)
	if (pTarget==None):
		return
	if (pShip.IsDead()) or (pShip.IsDying()):
		return

	MinYield=GetMinDamage()
	Percentage=GetPercentage()
	pShields = pTarget.GetShields()
	for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
		pShieldStatus=pShields.GetCurShields(ShieldDir)
		pShieldChunk=pShields.GetMaxShields(ShieldDir)*Percentage
		if (MinYield>pShieldChunk):
			pShieldChunk=MinYield
		if (pShieldStatus<=pShieldChunk):
			pShieldStatus=0
		pShields.SetCurShields(ShieldDir,pShieldStatus-pShieldChunk)
	return

def WeaponFired(pObject, pEvent):
	return