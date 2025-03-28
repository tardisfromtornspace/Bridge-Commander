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
	kCoreColor.SetRGBA(22.0 / 255.0, 55.0 / 255.0, 116.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(16.0 / 255.0, 86.0 / 255.0, 231.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(22.0 / 255.0, 55.0 / 255.0, 116.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/PhqCore.tga",
					kCoreColor,
					0.1,
					1.2,	 
					"data/Textures/Tactical/PhqGlow.tga", 
					kGlowColor,
					2.0,	
					0.34,	 
					0.4,	
					"data/Textures/Tactical/PhqFlares.tga",
					kFlareColor,										
					130,		
					0.08,		
					0.27)

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
	return(28)

def GetLaunchSound():
	return("ftsHyperon")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Hyperon")

def GetDamage():
	return 0.000001

def GetGuidanceLifetime():
	return 10.0

def GetMaxAngularAccel():
	return 0.17

# Sets the minimum damage the torpedo will do
def GetMinDamage():
	return 240

# Sets the percentage of damage the torpedo will do
def GetPercentage():
	return 0.1

def TargetHit(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pShip==None):
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