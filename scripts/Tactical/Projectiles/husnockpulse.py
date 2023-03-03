###############################################################################
#	Filename:	PulseDisruptor.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of disruptor blasts.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App
import MissionLib

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
	kOuterShellColor.SetRGBA(0.000001, 0.000001, 1.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.600000, 0.370588, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 10.0, 1.0) 		

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.32)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PULSEDISRUPT)

	return(0)

def GetLaunchSpeed():
	return(605.0)

def GetLaunchSound():
	return("HusnockPulse")

def GetPowerCost():
	return(1500.0)

def GetName():
	return("HusnockPulse")

def GetDamage():
	return 5250.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

def GetLifetime():
	return 10.0

# this sets the speed at which the target is repelled
def GetRepulsionForce():
	return 0.00

# this sets how fast the target is sent spinning
def GetRotationalForce():
	return 0.00

# Sets the minimum shield damage the torpedo will do
def GetMinDamage():
	return 3500.0

# Sets the percentage of shield damage the torpedo will do
def GetPercentage():
	return 0.01

def TargetHit(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip==None):
		return
	vNiWorldHitPoint=pEvent.GetWorldHitPoint()
	vWorldHitPoint=App.TGPoint3()
	vWorldHitPoint.SetXYZ(vNiWorldHitPoint.x,vNiWorldHitPoint.y,vNiWorldHitPoint.z)
	
	# Set spin to ship
	MissionLib.SetRandomRotation(pShip,GetRotationalForce());

	# Repel Ship
	vVelocity = pShip.GetWorldLocation()
	vVelocity.Subtract(vWorldHitPoint)
	vVelocity.Unitize()
	vVelocity.Scale(GetRepulsionForce())
	pShip.SetVelocity(vVelocity)

	# do the shield drain
	MinYield=GetMinDamage()
	Percentage=GetPercentage()
	pShields = pShip.GetShields()
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