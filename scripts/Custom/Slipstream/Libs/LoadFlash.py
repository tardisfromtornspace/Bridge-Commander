# by USS Sovereign

# Imports
import App
import Foundation
import MissionLib
from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import SlipstreamConfiguration

# GFX Folder
GFX = 'scripts/Custom/Slipstream/GFX/'

# Load the GFX animation
def StartGFX():
                pPlayer = MissionLib.GetPlayer()
                pModule = __import__(pPlayer.GetScript())

                # Is there a customization for this ship available?
                if hasattr(pModule, "SlipstreamCustomizations"):
                    pCustomization = pModule.SlipstreamCustomizations()
                    
                    # Customization exists, but does the flash entry exist?
                    if pCustomization.has_key('FlashAnimation'):
                        # Yes it does exist!
                        pFlash = "scripts/Custom/Slipstream/GFX/" + pCustomization['FlashAnimation']
                        
                        LoadGFX(4, 4, pFlash)

                    else:
                        # There doesn't seem to be an entry of a custom flash for this ship so check for user defined ones
                        reload(SlipstreamConfiguration)
                        
                        if SlipstreamConfiguration.FlashGFX == 'Default':
                            LoadGFX(4, 4, GFX + "SlipstreamFlash.tga")
                            
                        else:
                            pFlash = "scripts/Custom/Slipstream/GFX/" + SlipstreamConfiguration.FlashGFX

                            LoadGFX(4, 4, pFlash)

                # No customizations available for this ship, now checking for user defined stuff
                else:
                        reload(SlipstreamConfiguration)
                        
                        if SlipstreamConfiguration.FlashGFX == 'Default':
                            LoadGFX(4, 4, GFX + "SlipstreamFlash.tga")
                            
                        else:
                            pFlash = "scripts/Custom/Slipstream/GFX/" + SlipstreamConfiguration.FlashGFX

                            LoadGFX(4, 4, pFlash)


# Create flash effect on a ship
def CreateGFX(pShip):
		pAttachTo = pShip.GetNode()
                fSize = pShip.GetRadius() * 10
		pSequence = App.TGSequence_Create()	
		pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())

                sFile = GetTexture()
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
                fEffect = App.EffectAction_Create(pEffect)
                pSequence.AddAction(fEffect)
                pSequence.Play ()
                
                return

# Returns texture filename
def GetTexture():
                pPlayer = MissionLib.GetPlayer()
                pModule = __import__(pPlayer.GetScript())

                # Is there a customization for this ship available?
                if hasattr(pModule, "SlipstreamCustomizations"):
                    pCustomization = pModule.SlipstreamCustomizations()
                    
                    # Customization exists, but does the flash entry exist?
                    if pCustomization.has_key('FlashAnimation'):
                        # Yes it does exist!
                        strFile = GFX + pCustomization['FlashAnimation']
                        
                    else:
                         # There doesn't seem to be an entry of a custom flash for this ship
                        reload(SlipstreamConfiguration)
                        
                        if SlipstreamConfiguration.FlashGFX == 'Default':
                            strFile = GFX + "SlipstreamFlash.tga"
                            
                        else:
                            strFile = GFX + SlipstreamConfiguration.FlashGFX

                # No customizations available for this ship
                else:
                        reload(SlipstreamConfiguration)
                        
                        if SlipstreamConfiguration.FlashGFX == 'Default':
                            strFile = GFX + "SlipstreamFlash.tga"
                            
                        else:
                            strFile = GFX + SlipstreamConfiguration.FlashGFX
                
                return strFile


# Loads textures
def LoadGFX(iNumXFrames, iNumYFrames, sFile):
                fX = 0.0
                fY = 0.0

                pContainer = App.g_kTextureAnimManager.AddContainer(sFile)   
                pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
                for index in range(iNumXFrames * iNumYFrames):
                        pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                        fX = fX + (1.0 / iNumXFrames)

                        if (fX == 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)
