###############################################################################
#	Filename:	RepulsionTorp.py
#	By:		edtheborg
###############################################################################
# This torpedo uses the FTA mod...
#
# when a target is hit by this torpedo, the target is repelled at warp speed
# and sent spinning out of control
#
# please refer to the bottom of this file for details on changing effects
###############################################################################

import App
import MissionLib

###############################################################################
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(231.0 / 255.0, 16.0 / 255.0, 86.0 / 255.0, 1.000000)	
	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,
					0.0,	 
					"data/Textures/Tactical/QuantumX.tga", 
					kGlowColor,
					0.1,	
					0.2,	 
					0.3,	
					"data/Textures/Tactical/QuantumX.tga",
					kGlowColor,										
					4,		
					0.1,		
					0.06)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(1.99)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHASEDPLASMA)

	return(0)

def GetLaunchSpeed():
	return(50)

def GetLaunchSound():
	return("IntrepidCannon")

def GetPowerCost():
	return(40.0)

def GetName():
	return("WarBeoPulse")

def GetDamage():
	return 999.0

def GetGuidanceLifetime():
	return 0.9

def GetMaxAngularAccel():
	return 0.99

# this sets the speed at which the target is repelled
def GetRepulsionForce():
	return 2

# this sets how fast the target is sent spinning
def GetRotationalForce():
	return 8

def TargetHit(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip==None):
		return

	targetID = pShip.GetObjID()
	if targetID == None or targetID == App.NULL_ID:
		return
	pShip2 = App.ShipClass_GetObjectByID(None, targetID)
	if (pShip2==None):
		return
	if (pShip.IsDead()) or (pShip.IsDying()):
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