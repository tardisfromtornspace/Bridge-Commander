#script modified by D&G Productions

import App
import MissionLib

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(170.0 / 255.0, 240.0 / 255.0, 240.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(1.0 / 255.0, 159.0 / 255.0, 250.0 / 255.0, 1.000000)	


	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/QuasarFX.tga",
					kCoreColor, 
					0.65,
					6.0,	 
					"data/Textures/Tactical/wave.tga", 
					kGlowColor,
					3.0,	
					1.6,	 
					1.65,	
					"data/Textures/Tactical/MegaPhaserFX.tga",
					kGlowColor,										
					35,		
					0.675,		
					0.5)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.42)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(120.0)

def GetLaunchSound():
	return("Pulsewave")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Metreon Pulsewave Torpedo")

def GetDamage():
	return 6850.0

def GetGuidanceLifetime():
	return 35.0

def GetMaxAngularAccel():
	return 1.0

# this sets the speed at which the target is repelled
def GetRepulsionForce():
	return 25

# this sets how fast the target is sent spinning
def GetRotationalForce():
	return 96

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