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
	kCoreColor.SetRGBA(222.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(61.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)	
	
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoFlares.tga",
					kCoreColor,
					0.1,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kCoreColor,
					4.0,	
					0.6,	 
					0.3,	
					"data/Textures/Tactical/TorpedoCore.tga",
					kGlowColor,										
					400,		
					0.3,		
					0.05)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(2.99)
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
	return("NovaBombTorpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("NovaBombTorpedo")

def GetDamage():
	return 230.0

def GetGuidanceLifetime():
	return 7.0

def GetMaxAngularAccel():
	return 0.99

# this sets the speed at which the target is repelled
def GetRepulsionForce():
	return 20000

# this sets how fast the target is sent spinning
def GetRotationalForce():
	return 50000

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