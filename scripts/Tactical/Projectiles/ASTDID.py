
import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(235.0 / 255.0, 215.0 / 255.0, 255.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(205.0 / 255.0, 195.0 / 255.0, 245.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 90.0 / 255.0, 90.0 / 255.0, 1.000000)	#Red, Green, Blue, Alpha - all values other than alpha are devided by 255
	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ASTDID.tga",
					kCoreColor, 
					6.0,	#size
					3.2,	#rotation speed, positive is counterclockwise -negative clockwise
					"data/Textures/Tactical/IonStormTorpCore.tga", 
					kGlowColor,
					1.0,	#glow pulsate speed 
					10.0,	#glow max radius
					9.0,	#glow min radius
					"data/Textures/Tactical/TMPFlares.tga",
					kGlowColor,										
					0.0,	#number of flares
					0.5,	#flare size
					0.5)	#flare speed

	pTorp.SetDamage(84000000)
	pTorp.SetDamageRadiusFactor(1000.4)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

    # Multiplayer specific stuff.  Please, if you create a new torp
    # type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
    return(75.0)

def GetLaunchSound():
    return("ASTDID")

def GetPowerCost():
    return(1000.0)

def GetName():
    return("ASTDID")

def GetMinDamage():
    return 84000000

def GetPercentage():
    return 101.0

def GetGuidanceLifetime():
    return 1000.0

def GetMaxAngularAccel():
    return 0.2

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
