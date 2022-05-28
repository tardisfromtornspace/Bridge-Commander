# Plays the Explosion GFX sequence, should enhance the experience of the Badlands

# by Sov

import App
import Foundation

GFX = 'scripts/Custom/DS9FX/DS9FXBadlandsFX/GFX/'

def StartGFX():
                LoadGfx(4,2,GFX)
                
def CreateGFX(pShip):
		pAttachTo = pShip.GetNode()
		fSize     = pShip.GetRadius()/8
		pSequence = App.TGSequence_Create()	
		pEmitFrom = pShip.GetRandomPointOnModel()

                sFile = GFX + "BadlandsExplosion.tga"
                fLifeTime = 1
                fRed = 255.0
                fGreen = 255.0
                fBlue = 255.0
                fBrightness = 0.8
                fSpeed = 1
    
		pEffect = App.AnimTSParticleController_Create()
		pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
		pEffect.AddAlphaKey(0.0, 1.0)
		pEffect.AddAlphaKey(1.0, 1.0)
		pEffect.AddSizeKey(0.0, fSize)
		pEffect.AddSizeKey(1.0, fSize)
		
                pEffect.SetEmitLife(fSpeed)
                pEffect.SetEmitFrequency(1)
                pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
                pEffect.SetInheritsVelocity(0)
                pEffect.SetDetachEmitObject(0)
                pEffect.CreateTarget(sFile)
                pEffect.SetTargetAlphaBlendModes(0, 7)
                pEffect.SetEmitFromObject(pEmitFrom)
                pEffect.AttachEffect(pAttachTo)                
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
