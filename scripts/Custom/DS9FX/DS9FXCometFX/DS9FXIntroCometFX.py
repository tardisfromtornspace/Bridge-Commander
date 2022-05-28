# by USS Sovereign

import App
import Foundation
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig

GFX = 'scripts/Custom/DS9FX/DS9FXCometFX/GFX/'

def StartGFX():
                LoadGfx(8,4,GFX)

def CreateGFX(pShip):
		pAttachTo = pShip.GetNode()
		fSize     = 1
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

		vEmitDir = pShip.GetWorldUpTG()
                vEmitPos = pShip.GetHull().GetPosition()

                reload(DS9FXSavedConfig)
                if DS9FXSavedConfig.CometAlphaTrailTexture == 1:
                    sFile = GFX + "Trail0.tga"

                else:
                    sFile = GFX + "Comet0.tga"
                    
                fLifeTime = 999*9999 # simulating endless effect, nobody plays BC that long LOL
                fRed = 255.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 0.8
                fSpeed = 1
                fVelocity = 0.2
                                
                pEffect = App.AnimTSParticleController_Create()
                pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
                pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
                pEffect.AddAlphaKey(0.0, 1.0)
                pEffect.AddAlphaKey(1.0, 1.0)
                pEffect.AddSizeKey(0.0, fSize)
                pEffect.AddSizeKey(1.0, fSize)

                pEffect.SetEmitVelocity(fVelocity)
                pEffect.SetAngleVariance(1.0)
                pEffect.SetEmitRadius(10)
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(0.03)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.CreateTarget(sFile)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.SetEmitPositionAndDirection(vEmitPos, vEmitDir)
                pEffect.SetDetachEmitObject(0)
                pEffect.AttachEffect(pAttachTo)    
                pEffect.SetTargetAlphaBlendModes(0, 7)                                
                                
                oEffect = App.EffectAction_Create(pEffect)
                pSequence.AddAction(oEffect)
                pSequence.Play ()

def LoadGfx(iNumXFrames, iNumYFrames, Folder):
                FileNames = Foundation.GetFileNames(Folder, 'tga')       

                for loadIndex in FileNames:
                        strFile = Folder + str(loadIndex)
                        fX = 0.0
                        fY = 0.0

                        pContainer = App.g_kTextureAnimManager.AddContainer(strFile)   
                        pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                        for index in range(iNumXFrames * iNumYFrames):
                                pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                                fX = fX + (1.0 / iNumXFrames)

                                if (fX == 1.0):
                                        fX = 0.0
                                        fY = fY + (1.0 / iNumYFrames)

  
