# Adds a pulsar effect on a specified sun

import App
import math
import MissionLib

dData = {}

def Create(pSet, pSun, sBeamFlashPos, sBeamPos, sBeamType, fBeamSize, fBeamRotation, fFlashAngle1, fFlashAngle2, sSoundType, fVol, bSoundRepeat, sFlareType, fFlareSize1, fFlareSize2, iRadiationRange, iRadiationDamage):
    sBeamGFXPath = "scripts/Custom/DS9FX/DS9FXPulsarFX/BeamFX/"
    sFlaresPath = "Custom.DS9FX.DS9FXPulsarFX.FlareFX."
    sBeamPath = "Custom.DS9FX.DS9FXPulsarFX.BeamFX."
    sDummyModel = sBeamGFXPath + "/BeamDummy/Dummy.nif"
    
    try:
        sBeamScript = __import__(sBeamPath + sBeamType)
    except:
        print "DS9FX: Invalid Pulsar Beam type - " +  sBeamType
        return
    
    if hasattr(sBeamScript, "GetModel"):
        sModel = sBeamScript.GetModel()
        sModel = sBeamGFXPath + sModel
    else:
        print "DS9FX: Invalid Pulsar Beam plugin - " + sBeamType
        return 
    
    try:
        sFlareScript = __import__(sFlaresPath + sFlareType)
    except:
        print "DS9FX: Invalid Pulsar Flare type - " + sFlareType
        return
    
    if not hasattr(sFlareScript, "Add"):
        print "DS9FX: Invalid Pulsar Flare plugin - " + sFlareType
        return
    
    fRadius = float(pSun.GetRadius()) / 2.0
    if not fFlareSize1:
        fFlareSize1 = fRadius / 10000.0
        if fFlareSize1 <= 0.05:
            fFlareSize1 = 0.05
    if not fFlareSize2:
        fFlareSize2 = fRadius / 10000.0
        if fFlareSize2 <= 0.05:
            fFlareSize2 = 0.05
    fLow1 = fFlareSize1 * 2.0
    fLow2 = fFlareSize2 * 2.0
    fHigh1 = fFlareSize1 * 5.0
    fHigh2 = fFlareSize2 * 5.0
    
    sFlareScript.Add(pSet, pSun, 1, fFlareSize1, fFlareSize2)
  
    pProxManager = pSet.GetProximityManager()
    sName = sBeamPos + " Pulsar"
    pBeam = App.Planet_Create(fBeamSize, sModel)
    pSet.AddObjectToSet(pBeam, sName)
    pBeam.PlaceObjectByName(sBeamPos)
    pBeam.UpdateNodeOnly()
    pProxManager.RemoveObject(pBeam)      
    
    sName = sBeamPos + " Flash Pulsar"
    pFlash = App.Planet_Create(pSun.GetRadius(), sModel)
    pSet.AddObjectToSet(pFlash, sName)
    pFlash.PlaceObjectByName(sBeamPos)
    pFlash.SetHidden(1)
    pFlash.UpdateNodeOnly()
    pProxManager.RemoveObject(pFlash)   
    sFlareScript.Add(pSet, pFlash, 1, fLow1, fLow2)
    sFlareScript.Add(pSet, pFlash, 1, fHigh1, fHigh2)
    
    if sSoundType:
        pSound = App.g_kSoundManager.GetSound(sSoundType)
        if pSound:
            pSound.SetLooping(bSoundRepeat)
            pSound.SetSFX(1)
            pSound.SetInterface(0)
            pSound.SetVolume(fVol)
            pSound.AttachToNode(pSun.GetNode())            
    
    global dData
    sName = pSun.GetName()
    sTemp = sName
    i = 0
    while dData.has_key(sTemp):
        i = i + 1
        sTemp = sName + str(i)
        if dData.has_key(sTemp):
            sName = sTemp
            break

    if hasattr(pBeam, "SetDensity"):
        pBeam.SetDensity(0.1)
    
    if hasattr(pFlash, "SetDensity"):
        pFlash.SetDensity(0.1)    

    dSetData = {}
    dSetData["Set"] = pSet.GetName()
    dSetData["Beam"] = pBeam.GetObjID()
    dSetData["Flash"] = pFlash.GetObjID()
    dSetData["Sun"] = pSun.GetObjID()
    dSetData["Rotation"] = fBeamRotation
    dSetData["BeamPos"] = sBeamPos
    dSetData["FlashPos"] = sBeamFlashPos
    dSetData["FlashAngle1"] = fFlashAngle1
    dSetData["FlashAngle2"] = fFlashAngle2
    dSetData["Sound"] = sSoundType
    dSetData["Move"] = 1
    dSetData["SoundPlaying"] = 0
    dSetData["RadiationRange"] = iRadiationRange
    dSetData["RadiationDamage"] = iRadiationDamage
    
    dData[sName] = dSetData
    
def Update():
    global dData
    
    lToDelete = []
    
    for k in dData.keys():
        dSetData = dData[k]
        sSet = dSetData["Set"]
        iBeam = dSetData["Beam"]
        iFlash = dSetData["Flash"]
        iSun = dSetData["Sun"]
        fRot = dSetData["Rotation"]
        sBeamPos = dSetData["BeamPos"]
        sFlashPos = dSetData["FlashPos"]
        fFlashTreshold1 = dSetData["FlashAngle1"]
        fFlashTreshold2 = dSetData["FlashAngle2"]
        sSound = dSetData["Sound"]
        
        pSound = App.g_kSoundManager.GetSound(sSound)
        if pSound:
            pPlayer = MissionLib.GetPlayer()
            if pPlayer:
                pSet = pPlayer.GetContainingSet()
                if pSet:
                    if pSet.GetName() == sSet:
                        if dSetData["SoundPlaying"] == 0:
                            pSound.Play()
                            dSetData["SoundPlaying"] = 1
                    else:
                        if dSetData["SoundPlaying"] == 1:
                            App.g_kSoundManager.StopSound(sSound)
                            dSetData["SoundPlaying"] = 0
        
        pBeam = App.Planet_Cast(App.TGObject_GetTGObjectPtr(iBeam))
        pFlash = App.Planet_Cast(App.TGObject_GetTGObjectPtr(iFlash))
        pSun = App.Sun_Cast(App.TGObject_GetTGObjectPtr(iSun))
        if not pBeam or not pFlash or not pSun:
            lToDelete.append(k)
            continue
            
        kRot = App.TGMatrix3()
        kDir = pBeam.GetWorldUpTG()
        kRot.MakeRotation(fRot, kDir)
        pBeam.Rotate(kRot)
                 
        fFlashTreshold1 = math.cos(float(fFlashTreshold1) * App.PI / 180.0)
        fFlashTreshold2 = math.cos(float(fFlashTreshold2) * App.PI / 180.0)
        
        vDir = App.TGPoint3()
        vFwd = App.TGPoint3_GetModelForward()
        vDir.Set(vFwd)
        
        vGlobalDir = App.TGPoint3()
        vGlobalDir.Set(vDir)
        vGlobalDir.MultMatrixLeft(pBeam.GetWorldRotation())
        
        vDifference = pSun.GetWorldLocation()
        vDifference.Subtract(pBeam.GetWorldLocation())
        vDifference.Unitize()
        
        fDirDot = vGlobalDir.Dot(vDifference)
        lTreshold = [fFlashTreshold1, fFlashTreshold2]
        lTreshold.sort()
        
        bMoved = 0
        if fDirDot >= lTreshold[0] and fDirDot <= lTreshold[1]:
            pFlash.PlaceObjectByName(sFlashPos)
            dSetData["Move"] = 1
            bMoved = 1
            
        if dSetData["Move"] == 1 and not bMoved:
            pFlash.PlaceObjectByName(sBeamPos)
            dSetData["Move"] = 0
        
        dData[k] = dSetData
            
    for k in lToDelete:
        del dData[k]
        
def Reset():
    global dData
    
    for k in dData.keys():
        dSetData = dData[k]
        sSound = dSetData["Sound"]
        pSound = App.g_kSoundManager.GetSound(sSound)
        if pSound:
            App.g_kSoundManager.StopSound(sSound)
    
    dData = {}        