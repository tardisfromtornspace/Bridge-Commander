import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA((150.0 / 255.0), (255.0 / 255.0), (150.0 / 255.0), 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA((0.0 / 255.0), (255.0 / 255.0), (0.0 / 255.0), 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA((20.0 / 255.0), (255.0 / 255.0), (20.0 / 255.0), 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/Digitizer.tga', kCoreColor, 0.5, 1.0, 'data/Textures/Tactical/Digitizer.tga', kGlowColor, 4.0, 3.0, 3.0, 'data/Textures/Tactical/TorpedoFlares.tga', kFlareColor, 60, 0.95, 0.04)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.05)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHASEDPLASMA)
    return 0


def GetLaunchSpeed():
    return 75.0


def GetLaunchSound():
    return("ScanningDigitizer")


def GetPowerCost():
    return 10.0


def GetName():
    return("Scanning Digitizer")


def GetDamage():
    return 1000.0


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.75

def GetMinDamage():
	return 1000.0

def GetPercentage():
	return 0.7

def TargetHit(pObject, pEvent):
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pShip==None):
		return
	vNiWorldHitPoint=pEvent.GetWorldHitPoint()
	vWorldHitPoint=App.TGPoint3()
	vWorldHitPoint.SetXYZ(vNiWorldHitPoint.x,vNiWorldHitPoint.y,vNiWorldHitPoint.z)

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