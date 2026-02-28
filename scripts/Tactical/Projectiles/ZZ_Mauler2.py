import App
def Create(pTorp):

	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 174.0 / 255.0, 254.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(175.0 / 255.0, 12.0 / 255.0, 173.0 / 255.0, 1.000000)	
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(241.0 / 255.0, 211.0 / 255.0, 241.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZMauler2Core.tga",
					kCoreColor,
					0.2,
					6.0,	 
					"data/Textures/Tactical/ZZMauler2Glow.tga", 
					kGlowColor,
					6.0,	
					0.4,	 
					0.8,	
					"data/Textures/Tactical/ZZMauler2Core.tga",
					kCoreColor,										
					15,		
					0.6,		
					0.8)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("")

def GetPowerCost():
	return(0.0)

def GetName():
	return("")

def GetDamage():
	return 4500.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.0

def GetLifetime():
	return 20.0

def TargetHit(pObject, pEvent):
	pTarget=App.ShipClass_Cast(pEvent.GetDestination())
	MinYield=240
	Percentage=0.05
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
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	pShip=pTube.GetParentShip()
	return