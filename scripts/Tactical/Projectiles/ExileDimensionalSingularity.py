import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.000000)	
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(400.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 5.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					1.0,
					1.0,	 
					"data/Textures/Tactical/TorpedoGlow.tga", 
					kGlowColor,
					8.0,	
					1.5,	 
					0.5,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					5,		
					0.2,		
					0.1)

	pTorp.SetDamage(GetDamage())
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.UNKNOWN)

	return(0)

def GetLaunchSpeed():
    return 85.0

def GetLaunchSound():
    return ("DimensionalSingularity")

def GetDamage():
	return 3500000

def GetRotationalForce():
	return 0.00

def GetPowerCost():
    return 500.0

def GetName():
    return ("Dimensional Singularity")

def GetGuidanceLifetime():
    return 10.0

def GetMaxAngularAccel():
    return 1.0

def TargetHit(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip==None):
		return
	vNiWorldHitPoint=pEvent.GetWorldHitPoint()
	vWorldHitPoint=App.TGPoint3()
	vWorldHitPoint.SetXYZ(vNiWorldHitPoint.x,vNiWorldHitPoint.y,vNiWorldHitPoint.z)
	
	# Set spin to ship
	MissionLib.SetRandomRotation(pShip,GetRotationalForce());
	return

def WeaponFired(pObject, pEvent):
	return