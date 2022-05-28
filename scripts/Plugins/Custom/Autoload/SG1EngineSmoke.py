# SG1EngineSmoke.py
__author__      = "John Hardy aka Lost_Jedi"
__copyright__   = "Copyright (C) 2007 BCS:TNG"
__license__     = "GNU"
__version__     = "1.0"


import App
import Foundation
import string

oEngineSmoke = Foundation.MutatorDef('Engine Smoke (SG1)')
dEngineSmoke = { 'modes': [ oEngineSmoke ] }

global dShipTimingTable
dShipTimingTable = {}           #(Velocity, TotalLife, Size, ParticleLife)
dShipTimingTable["Horizon"] =   (0.0, 99999, 0.1, 1.5)


def addSmokeTrails(pShip, sScriptKey):
    global dShipTimingTable
    pSequence = App.TGSequence_Create()
    pImpulseEngineSystem = pShip.GetImpulseEngineSubsystem()
    if pImpulseEngineSystem:
        ## For each Impulse engine
        iNumberEngines = pImpulseEngineSystem.GetNumChildSubsystems()
        for iEngine in range(iNumberEngines):
            pImpulseEngine = pImpulseEngineSystem.GetChildSubsystem(iEngine)
            if pImpulseEngine:                       
                ## Build Effect
                pEmitPos        = pImpulseEngine.GetPositionTG()
                pEmitDir        = App.NiPoint3(0, 0, 0)
                pEmitFrom       = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
                pEffectRoot     = pShip.GetContainingSet().GetEffectRoot()
                fVelocity       = dShipTimingTable[sScriptKey][0]
                fLife           = dShipTimingTable[sScriptKey][1]
                fSize           = dShipTimingTable[sScriptKey][2]
                fParticleLife   = dShipTimingTable[sScriptKey][3]
                pSmokeAction    = CreateSmokeHigh(fVelocity, fLife, fSize, fParticleLife, pEmitFrom, pEmitPos, pEmitDir, pEffectRoot)
                pSequence.AddAction(pSmokeAction)
                print "creating"
                
    ## Play The Sequence
    pSequence.Play()





class EngineSmokeTrigger(Foundation.TriggerDef):

    def __init__(self, name, eventKey, dict = {}):
        Foundation.TriggerDef.__init__(self, name, eventKey, dict)	

    def __call__(self, pObject, pEvent, dict = {}):

        
        pObject = App.ShipClass_Cast(pEvent.GetDestination())
        
        if not pObject:
            return
        
        if not pObject.IsTypeOf(App.CT_SHIP):
            return

        pSet = pObject.GetContainingSet()
        if not pSet:
            return
            
        if pSet.GetName() == "bridge": # or pSet.GetName() == "warp":
            return
        
        sShipScript = pObject.GetScript()
        sShipScript = string.split(sShipScript, ".")[-1]
        global dShipTimingTable
        if dShipTimingTable.has_key(sShipScript):
            addSmokeTrails(pObject, sShipScript)          


def CreateSmokeHigh(fVelocity, fLife, fSize, fParticleLife, pEmitFrom, kEmitPos, kEmitDir, pAttachTo):
    pSmoke = App.AnimTSParticleController_Create()
    pSmoke.AddColorKey(0.0, 1.0, 1.0, 1.0)
    pSmoke.AddAlphaKey(0.0, 0.6)
    pSmoke.AddAlphaKey(0.5, 0.5)
    pSmoke.AddAlphaKey(1.0, 0.0)
    pSmoke.AddSizeKey(0.0, 0.2 * fSize)
    pSmoke.AddSizeKey(0.6, 1.0 * fSize)
    pSmoke.AddSizeKey(0.9, 2.0 * fSize)
    pSmoke.SetEmitVelocity(fVelocity)
    pSmoke.SetAngleVariance(0.0)
    fFrequency = 0.05
    pSmoke.SetEmitLife(fParticleLife)
    pSmoke.SetEmitFrequency(fFrequency)
    pSmoke.SetEffectLifeTime(fLife)
    pSmoke.SetDrawOldToNew(0)
    pSmoke.CreateTarget("data/Textures/Effects/ExplosionB.tga")
    pSmoke.SetEmitFromObject(pEmitFrom)
    pSmoke.SetEmitPositionAndDirection(kEmitPos, kEmitDir)
    pSmoke.SetInheritsVelocity(0)
    pSmoke.AttachEffect(pAttachTo)
    return App.EffectAction_Create(pSmoke)

    
EngineSmokeTrigger('Engine Smoke', App.ET_ENTERED_SET, dEngineSmoke)




