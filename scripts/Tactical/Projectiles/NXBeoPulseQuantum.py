###############################################################################
#	Filename:	QuantumTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of quantum torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a quantum torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 225.0 / 255.0, 200.0 / 255.0, 1.000000)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/NXBeoPulseQuantumCore.tga",
					kCoreColor, 
					0.17, 
					3.5,	 
					"data/textures/tactical/NXBeoPulseQuantumGlow.tga", 
					kGlowColor,
					2,	
					2.00,	 
					2.15,	
					"data/textures/tactical/NXBeoPulseQuantumBlank.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.14)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.18) 
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(43.0)

def GetLaunchSound():
	return("NXBeoPulseQuantum")

def GetPowerCost():
	return(16.0)

def GetName():
	return("NXBeoPulseQuantum")

def GetDamage():
	return 1860.0

def GetGuidanceLifetime():
	return 4.0

def GetMaxAngularAccel():
	return 2.0

def GetLifetime():
	return 9.0

# this sets the speed at which the target is repelled
def GetRepulsionForce():
	return 4

# this sets how fast the target is sent spinning
def GetRotationalForce():
	return 120

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
	return

def WeaponFired(pObject, pEvent):
	return

