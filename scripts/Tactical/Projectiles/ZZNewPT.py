# File: Z (Python 1.5)

import App
import trails.ZZKrilosTrail
import trails.OriBeam

def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(140.0 / 255.0, 40.0 / 255.0, 255.0 / 255.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(200.0 / 255.0, 80.0 / 255.0, 255.0 / 255.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZKrilosCore.tga', kCoreColor, 0.12, 7.0, 'data/Textures/Tactical/ZZBlackGlow.tga', kGlowColor, 1.2, 0.2, 0.35, 'data/Textures/Tactical/ZZKrilosCore.tga', kGlowColor, 40, 0.5, 0.12)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    trails.OriBeam.AddCreationHandler(pTorp, __name__ + '.AttachSmoke')
    return 0


def AttachSmoke(self, pEvent = None):
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return 1
    
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZKrilosTrail.tga', 8, 1)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZKrilosTrail.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 3.0, sEmitLife = 0.035, elVar = 0.1, sEffectLifetime = 20.0, leDamp = 0.2, sAngleVariance = 120.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), sDrawOldToNew = 1, inhVel = -1, pEffectRoot = pTorpedo, pFunction = trails.ZZKrilosTrail.DefaultColorKeyFunc)
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZKrilosTrail2.tga', 8, 1)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZKrilosTrail2.tga', fFrequency = 0.01, fVelocity = 0.01, evVar = 0.1, fSize = pTorpedo.GetRadius() * 1.0, sEmitLife = 0.035, elVar = 0.1, sEffectLifetime = 20.0, leDamp = 0.2, sAngleVariance = 120.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 1, 0), sDrawOldToNew = 1, inhVel = -1, pEffectRoot = pTorpedo, pFunction = trails.ZZKrilosTrail.DefaultColorKeyFunc)
    return 0


def GetLaunchSpeed():
    return 25.0


def GetLaunchSound():
    return 'ZZKrilosTorpedo'


def GetPowerCost():
    return 1.0


def GetName():
    return 'New Plasma'

def GetDamageMin():
    return 1000.0


def GetDamageMax():
    return 15000.0

def GetDamage():
    return GetDamageMax()

def GetGuidanceLifetime():
    return 8.0

def GetMaxAngularAccel():
    return 0.33

def GetLifetime():
    return 20.0

def GetRangeNear():
    return 56.0

def GetRangeFar():
    return 393.0


def GetRangeFloor():
    return 5.0


def GetSearchRadius():
    return GetRangeFar()

"""
def GetFiringShip(pEvent):
    
    try:
        if pEvent != None:
            pWeapon = App.Weapon_Cast(pEvent.GetSource())
            if pWeapon != None:
                pShip = pWeapon.GetShip()
                if pShip != None:
                    return pShip
                
            
    except:
        pass

    return None


def GetDistanceBetween(pFrom, pTo):
    
    try:
        kDist = pFrom.GetWorldLocation()
        kDist.Subtract(pTo.GetWorldLocation())
        return kDist.Length()
    except:
        return None



def FindNearestShip(pTorp, pExclude = None):
    
    try:
        pSet = pTorp.GetContainingSet()
        if pSet == None:
            return (None, None)
        
        pProx = pSet.GetProximityManager()
        if pProx == None:
            return (None, None)
        
        kLoc = pTorp.GetWorldLocation()
        kIter = pProx.GetNearObjects(kLoc, GetSearchRadius(), 1)
        fNearest = None
        idNearest = None
        while 1:
            pObj = pProx.GetNextObject(kIter)
            if pObj == None:
                break
            
            if not pObj.IsShip():
                continue
            
            pShip = App.ShipClass_Cast(pObj)
            if pShip == None:
                continue
            
            if pExclude != None and pShip.GetObjID() == pExclude.GetObjID():
                continue
            
            fDist = GetDistanceBetween(pTorp, pShip)
            if fDist == None:
                continue
            
            if fNearest == None or fDist < fNearest:
                fNearest = fDist
                idNearest = pShip.GetObjID()
            
        return (fNearest, idNearest)
    except:
        return (None, None)



def ResolveTargetForTorpedo(pTorp, pEvent = None):
    
    try:
        idTarget = pTorp.GetTargetID()
        if idTarget != None and idTarget != App.NULL_ID:
            pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
            if not pTarget:
                pTarget = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(idTarget))
            
            if pTarget != None:
                return (GetDistanceBetween(pTorp, pTarget), idTarget)
            
    except:
        pass

    pExclude = GetFiringShip(pEvent)
    (fDist, idNearest) = FindNearestShip(pTorp, pExclude)
    if idNearest != None and idNearest != App.NULL_ID:
        
        try:
            pTorp.SetTarget(idNearest)
        except:
            pass

        return (fDist, idNearest)
    
    return (None, None)


def CalcDamageFromDistance(fDist):
    dmgMin = GetDamageMin()
    dmgMax = GetDamageMax()
    near = GetRangeNear()
    far = GetRangeFar()
    floor = GetRangeFloor()
    if fDist == None:
        return dmgMax
    
    if fDist <= near:
        return dmgMax
    
    if fDist >= far:
        return dmgMin
    
    if fDist < floor:
        fDist = floor
    
    invNear = 1.0 / near
    invFar = 1.0 / far
    invDist = 1.0 / fDist
    denom = invNear - invFar
    if denom <= 1e-005:
        return dmgMax
    
    t = (invDist - invFar) / denom
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    
    return dmgMin + t * (dmgMax - dmgMin)

import traceback

try:
    import FoundationTech
    
    class ZZNewPlasmaTorpedoOnFire:
        
        def OnFire(self, pEvent, pTorp):
            if not pTorp:
                return None
            
            (fDist, idTarget) = ResolveTargetForTorpedo(pTorp, pEvent)
            fDamage = CalcDamageFromDistance(fDist)
            if fDamage < 1e-005:
                fDamage = 1e-005
            
            pTorp.SetDamage(fDamage)


    FoundationTech.dOnFires[__name__] = ZZNewPlasmaTorpedoOnFire()
except:
    print 'ZZNewPT: inverse range OnFire hook failed'
    traceback.print_exc()
"""

import traceback
try:
	import FoundationTech
	import ftb.Tech.TimedTorpedoesExpansion

	# You would need to add another import for each different file you are importing a function from.
	# import ftb.Tech.TimedTorpedoesExpansion
	repeatClass = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassDLoop
	newFuncRepeat = ftb.Tech.TimedTorpedoesExpansion.newCustomFunctionFor1           # <--- and you would change that, too

	ActClass = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassLoop
	newFuncAct = ftb.Tech.TimedTorpedoesExpansion.newCustomFunctionFor2              # <--- and you would change that, too

	oFire = ftb.Tech.TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2(
		'MIRVMultiSingleTargetTorpedoFire2', {
		'alternateClassCall1': repeatClass,
		'alternateClassCall2': ActClass,
		'alternateClassCall1Extras': 1,
		'multipleTargetSelect': 1,
		'spreadNumber': 1,
		'spreadDensity': 1,
		'warheadModule': "Tactical.Projectiles.ZZNewPT",
		'shellLive': 0,
		'CustomFunction': newFuncRepeat,
		'CustomFunction2': newFuncAct,
		'LOOK_CUSTOM_XTRA_DMG': -0.1,
		'LOOK_CUSTOM_MAX_DMG': GetDamageMax(), # GetDamage() from the projectile script
		'LOOK_CUSTOM_MIN_DMG': GetDamageMin(),
		'LOOK_CUSTOM_INI_DMG': (GetDamageMax()-GetDamageMin()),
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()

