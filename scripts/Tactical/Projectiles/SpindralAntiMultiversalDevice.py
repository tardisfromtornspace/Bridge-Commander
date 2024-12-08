# uncompyle6 version 3.9.0
# Python bytecode version base 1.5 (20121)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: .\Scripts\Tactical\Projectiles\WDRchroniton.py
# Compiled at: 2023-09-01 00:03:05
import App

def Create(pTorp):
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(0.0 / 255.0, 0.0 / 255.0, 0.0 / 255.0, 1.0)
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(255.0 / 255.0, 215.0 / 255.0, 245.0 / 255.0, 1.0)
    kFlareColor = App.TGColorA()
    kFlareColor.SetRGBA(48.0 / 255.0, 0.0 / 255.0, 100.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ExistentialUnteatheringCore.tga', kCoreColor, 1.5, 3.2, 'data/Textures/Tactical/SpindralAntiMultiversalGlow.tga', kGlowColor, 1.0, 7.5, 4.5, 'data/Textures/Tactical/ExistentialUnteatheringCore.tga', kFlareColor, 500.0, 4.0, 1.0)
    pTorp.SetDamage(250000000)
    pTorp.SetDamageRadiusFactor(150)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())

    import Multiplayer
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.QUANTUM)

    return 0

def GetLaunchSpeed():
    return 65.0

def GetLaunchSound():
    return 'SpindralAntiMultiversalDevice'

def GetPowerCost():
    return 35.0

def GetName():
    return 'Spindral Anti Multiversal Device'

def GetPercentage():
    return 1000.0

def GetMinDamage():
    return 250000000

def GetGuidanceLifetime():
    return 1000.0

def GetMaxAngularAccel():
    return 50.0

def TargetHit(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pShip=App.ShipClass_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pShip==None):
		return
	try:
		id=pTorp.GetObjID()
		pSubsystem=pWeaponLock[id]
		del pWeaponLock[id]
	except:
		pSubsystem=pShip.GetHull()
	if (pSubsystem==None):
		return
	Dmg=pSubsystem.GetMaxCondition()*GetPercentage()
	if (Dmg<GetMinDamage()):
		Dmg=GetMinDamage()
	if (pSubsystem.GetCondition()>Dmg):
		pSubsystem.SetCondition(pSubsystem.GetCondition()-Dmg)
	else:
		pShip.DestroySystem(pSubsystem)
	return

def WeaponFired(pObject, pEvent):
	global pWeaponLock
	pTorp=App.Torpedo_Cast(pEvent.GetSource())
	pTube=App.TorpedoTube_Cast(pEvent.GetDestination())
	if (pTorp==None) or (pTube==None):
		return
	pShip=pTube.GetParentShip()
	if (pShip==None):
		return
	try:
		pWeaponLock[pTorp.GetObjID()]=pShip.GetTargetSubsystem()
	except:
		return
	return