__author__      = "John Hardy aka Lost_Jedi"
__copyright__   = "Copyright (C) 2006 BCS:TNG"
__license__     = "GNU"
__version__     = "1.0"
__notes__       = "Immersion Framework v4.0 ++"


## Import API
####################################
import App


## Event Stuff
####################################
def AddInstanceHandler(pObject, sFunction, iEventType):
    pObject.AddPythonFuncHandlerForInstance(iEventType, sFunction)

def AddCreationHandler(pObject, sFunction):
    AddInstanceHandler(pObject, sFunction, App.ET_TORPEDO_ENTERED_SET)

def AddHitHandler(pObject, sFunction):
    AddInstanceHandler(pObject, sFunction, App.ET_WEAPON_HIT)            
       

## Effects
####################################
def CreateSmokeHigh(sTexture, fFrequency, fVelocity, fSize, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):
    ## Create the smoke object
    pSmoke = App.AnimTSParticleController_Create()

    ## Setup colour and alpha
    pSmoke.AddColorKey(0.0, 0.0, 1.0, 1.0)
    #pSmoke.AddColorKey(1.0, 211.0 / 255.0, 46.0 / 255.0, 253.0 / 255.0)

    pSmoke.AddAlphaKey(0.0, 0.6)
    pSmoke.AddAlphaKey(0.5, 0.5)
    pSmoke.AddAlphaKey(1.0, 0.0)

    pSmoke.AddSizeKey(0.0, 0.010 * fSize)
    pSmoke.AddSizeKey(0.025, 0.40 * fSize)
    pSmoke.AddSizeKey(0.040, 0.10 * fSize)

    ## Setup properties
    pSmoke.SetEmitVelocity(fVelocity)
    pSmoke.SetAngleVariance(60.0)
    pSmoke.SetEmitLife(2.0)
    pSmoke.SetEmitFrequency(fFrequency)
    pSmoke.SetEffectLifeTime(30.0)
    pSmoke.SetDrawOldToNew(0)
    pSmoke.CreateTarget(sTexture)
    pSmoke.SetEmitFromObject(pEmitFrom)
    pSmoke.SetEmitPositionAndDirection(kEmitPos, kEmitDir)	
    pSmoke.AttachEffect(pAttachTo)
    return App.EffectAction_Create(pSmoke)


## Common
####################################
def SetupSmokeTrail(pTorpedo):
    pSequence   = App.TGSequence_Create()
    pEffectRoot = GetSetEffectRoot(pTorpedo)
    pEmitFrom   = GetNIAVNode(pTorpedo)
    pSequence.AddAction(CreateSmokeHigh('data/Textures/Effects/ExplosionB.tga', 0.01, 0.2, pTorpedo.GetRadius() * 1, pEmitFrom, App.NiPoint3(0, 0, 0), App.NiPoint3(0, 0, 0), pEffectRoot))
    pSequence.Play()


    
#### Sync With Immersion Framework
####################################
##pyImmersion = __import__("Custom.Immersion.core")
##if pyImmersion:
##    ## Load Immersion Tools
##    from Custom.Immersion.core import *
##else:
##    ## Load Local Tools
    
## Tools
####################################
global lLoadedTexturesCache
lLoadedTexturesCache = ['data/Textures/Effects/ExplosionB.tga','data/Textures/Effects/ExplosionA.tga']

def LoadTexture(sTexturePath = None, iNumXFrames = 1, iNumYFrames = 1):
    global lLoadedTexturesCache
    if (sTexturePath in lLoadedTexturesCache):
        return sTexturePath
    fX = 0.0
    fY = 0.0
    if sTexturePath:
        pContainer = App.g_kTextureAnimManager.AddContainer(sTexturePath)
        if pContainer:
            pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
            for index in range(iNumXFrames * iNumYFrames):
                    pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                    fX = fX + (1.0 / iNumXFrames)
                    if (fX == 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)
    lLoadedTexturesCache.append(sTexturePath)
    return sTexturePath



def GetNIAVNode(pObject):
    return App.TGModelUtils_CastNodeToAVObject(pObject.GetNode())

def GetSetEffectRoot(pObject):
    return pObject.GetContainingSet().GetEffectRoot()


def CreateEffectSequence(pEffect):
    ## Create and Play a sequence
    pSequence = App.TGSequence_Create()
    pSequence.AddAction(pEffect)
    return pSequence
