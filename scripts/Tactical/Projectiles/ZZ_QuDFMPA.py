# File: Z (Python 1.5)

import App
import MissionLib
import traceback
trailsWork = 0

try:
    import trails.ZZQuDTrail
    import trails.OriBeam
    trailsWork = 1
except:
    trailsWork = 0
    print (__name__, ' will not load effects because dependencies are missing:')
    traceback.print_exc()


def Create(pTorp):
    kGlowColor = App.TGColorA()
    kGlowColor.SetRGBA(1.0, 1.0, 1.0, 1.0)
    kCoreColor = App.TGColorA()
    kCoreColor.SetRGBA(1.0, 1.0, 1.0, 1.0)
    pTorp.CreateTorpedoModel('data/Textures/Tactical/ZZQuDCore.tga', kCoreColor, 0.1, 10.0, 'data/textures/Tactical/ZZQuDGlow.tga', kGlowColor, 15.0, 0.1, 0.3, 'data/textures/Tactical/ZZQuDCore.tga', kGlowColor, 8, 0.1, 0.3)
    pTorp.SetDamage(GetDamage())
    pTorp.SetDamageRadiusFactor(0.25)
    pTorp.SetGuidanceLifetime(GetGuidanceLifetime())
    pTorp.SetMaxAngularAccel(GetMaxAngularAccel())
    pTorp.SetLifetime(GetLifetime())
    import Multiplayer.SpeciesToTorp
    pTorp.SetNetType(Multiplayer.SpeciesToTorp.PHOTON)
    if trailsWork:
        trails.OriBeam.AddCreationHandler(pTorp, __name__ + '.AttachSmoke')
    
    return 0


def AttachSmoke(self, pEvent = None):
    '''Attach dual plasma smoke trails (center yellow + outer orange/red).'''
    pTorpedo = App.Torpedo_Cast(pEvent.GetDestination())
    if not pTorpedo:
        return 1
    
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZQuDTrail1.tga', 4, 4)
    trails.OriBeam.LoadTexture('data/Textures/Effects/ZZQuDTrail3.tga', 4, 4)
    baseSize = pTorpedo.GetRadius() * 1.0
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZQuDTrail1.tga', fFrequency = 0.018, fVelocity = 0.28, fSize = baseSize * 1.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 0, 0), sAngleVariance = 360.0, leDamp = 0.1, gravy = [
        0.0,
        0.0,
        0.0], detEO = 1, sEmitLife = 0.025, sEffectLifetime = 9.5, sDrawOldToNew = 0, inhVel = 0, pFunction = trails.ZZQuDTrail.DefaultColorKeyFunc)
    trails.OriBeam.SetupSmokeTrail(pTorpedo, sTexture = 'data/Textures/Effects/ZZQuDTrail3.tga', fFrequency = 0.025, fVelocity = 0.32, fSize = baseSize * 1.0, kEmitPos = App.NiPoint3(0, 0, 0), kEmitDir = App.NiPoint3(0, 0, 0), sAngleVariance = 360.0, leDamp = 0.025, gravy = [
        0.0,
        0.0,
        0.0], detEO = 1, sEmitLife = 0.05, sEffectLifetime = 9.5, sDrawOldToNew = 0, inhVel = 0, pFunction = trails.ZZQuDTrail.DefaultColorKeyFunc)
    return 0


def GetLaunchSpeed():
    return 45.0


def GetLaunchSound():
    return 'ZZ_VerPSPear'


def GetPowerCost():
    return 1.0


def GetName():
    return 'FMPA'


def GetDamage():
    return 0.0001


def GetGuidanceLifetime():
    return 10.0


def GetMaxAngularAccel():
    return 0.35


def GetLifetime():
    return 10.0


def GetDamageDistance():
    return 40


try:
    import FoundationTech
    import ftb.Tech.ZZShieldDrain
    ftb.Tech.ZZShieldDrain.oZZShieldDrain.AddTorpedo(__name__, fPercent = 0.15, sTexture = 'data/Textures/Effects/ZZFMPA9.tga', kColor = [
        1.0,
        0.2,
        0.9], iFrameW = 8, iFrameH = 2, iAmount = 1, fSizeMult = 2.0, fLife = 1.5)
except Exception, e:
    print "Failed to register ZZ Drain Yield:", str(e)
    traceback.print_exc()

