# Made by Lost Jedi

# Adapted for UMM purposes by USS Sovereign
# Revision Note: Clean code there LJ, very clean and nice.

import App
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig


def ApplyTrailToPlayer():
    # this an example of how to add a comet trail to a ship
    pPlayer = App.Game_GetCurrentGame().GetPlayer()
    CometTrail(pPlayer)

def CreateSingleAnimated(strFile = None,iNumXFrames = None,iNumYFrames = None):
    fX = 0.0
    fY = 0.0
    pContainer = App.g_kTextureAnimManager.AddContainer(strFile)
    if not pContainer:
        raise RuntimeError, "DS9FX CometFX: Couldn't access texture file at: " + str(strFile)
    else:
        pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
        for index in range(iNumXFrames * iNumYFrames):
                pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                fX = fX + (1.0 / iNumXFrames)
                if (fX == 1.0):
                        fX = 0.0
                        fY = fY + (1.0 / iNumYFrames)
    return strFile


class CometTrail:

    reload (DS9FXSavedConfig)
    if  DS9FXSavedConfig.CometAlphaTrailTexture == 1:
        ## This is declared as a shared public data item of the CometTrail Class so its only loaded once
        TrailTexture = CreateSingleAnimated("scripts/Custom/DS9FX/DS9FXCometFX/GFX/Trail0.tga",8,4)

    else:
        TrailTexture = CreateSingleAnimated("scripts/Custom/DS9FX/DS9FXCometFX/GFX/Comet0.tga",8,4)


    ## Set our ship
    def __init__(self,pCometShip):

        ## A few constructors
        self.pComet = pCometShip
        self.pSequence = None

        ## Create our trails
        self.CreateTrails()

    def GetSet(self):
        if self.pComet:
            return self.pComet.GetContainingSet()

    def AbortTrails(self):
        if self.pSequence:
            self.pSequence.Destroy()
            self.pSequence = None
    
    def CreateTrails(self):
        pSet = self.GetSet()

        ## Trail
	pPlayer = self.pComet
	
        ## Some Data
        pController = App.AnimTSParticleController_Create()

        ## Brightness / R / G / B
        pController.AddColorKey(0.1,   1.0,		1.0,		1.0)
        pController.AddColorKey(0.2,   0.9,		0.9,		1.0)

        
        pController.AddAlphaKey(0.5, 1.0)
        pController.AddAlphaKey(0.3, 0.6)
        pController.AddAlphaKey(0.1, 0.0)

        ## Setup Size Stuff
        pController.AddSizeKey(0.0, 1.0 * pPlayer.GetRadius() * 0.7)
        pController.AddSizeKey(1.0, 1.0 * pPlayer.GetRadius()* 2)

        ## Animation Properties
        pController.SetEmitLife(12.0)
        pController.SetEmitFrequency(0.01)
        pController.SetEffectLifeTime(999*9999)
        pController.CreateTarget(CometTrail.TrailTexture)

        ## Physics Properties
        pController.SetEmitVelocity(0.3)
        pController.SetAngleVariance(300.0)
        pController.SetEmitRadius(0.8)

        ## Alpha Blend Mode
        pController.SetTargetAlphaBlendModes(0, 7)

        ## TG Object Properties	
        pController.SetEmitFromObject(App.TGModelUtils_CastNodeToAVObject(pPlayer.GetNode()))
        pController.SetEmitPositionAndDirection(App.NiPoint3(0, 0, 0), App.NiPoint3(0, 0, 2.0))
        pController.SetInheritsVelocity(0)
        pController.SetDetachEmitObject(0)
        pController.AttachEffect(pSet.GetEffectRoot())

        ## Compile Effect
        pEffect = App.EffectAction_Create(pController)

        if self.pSequence:
            self.pSequence.Destroy()
            
        self.pSequence = App.TGSequence_Create()
        self.pSequence.AddAction(pEffect)
        self.pSequence.Play()
