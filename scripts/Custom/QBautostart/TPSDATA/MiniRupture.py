from bcdebug import debug
# just FIY from LJ here...
# this is a mod in its own right.  its makes the plasma nacelle vent mini streams if
# it gets hit. problem is finding out where the warp engine is IMO.
# if i can remeber right anyway! lol
# to start it up ingame:
#
#   1) Open the Console
#   2) enter the following:
#           from Custom.QBautostart.TPSDATA.MiniRupture import Load
#   3) then on the next line (assuming thre are no errors):
#           Load()
#
# This will add a listenr to the Hull hit event of each ship.  Hopefully creating miniplasma streams.
#

import App
from Custom.NanoFXv2.ExplosionFX.ExpFX import *
from Custom.QBautostart.TargetablePlasmaStreams import CreateMiniPlasmaEffect
import Custom.NanoFXv2.NanoFX_ScriptActions
import Custom.NanoFXv2.NanoFX_Lib
import math
FALSE = 0
TRUE = 1

def Load():
    debug(__name__ + ", Load")
    pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
    App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT,pMission, __name__ + ".BCSWeaponHullHit")
###############################################################################
## Phaser Hitting Hull Event
def BCSWeaponHullHit(pObject, pEvent):
        debug(__name__ + ", BCSWeaponHullHit")
        pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
        if pShip:
            if pShip.GetRadius() < 0.1:  ### Fix the crash with small objects bug
                    pObject.CallNextHandler(pEvent)
                    return
        if pEvent.IsHullHit():
            ### Run the Mini Rupture Function 5% Chance
            if (App.g_kSystemWrapper.GetRandomNumber(100) < 5):
                    pSequence = App.TGSequence_Create()
                    pSequence.AddAction(CreateBCSMiniRuptureSequence(pEvent, "PhaserHullHit"))
                    pSequence.AppendAction(App.TGScriptAction_Create("Custom.NanoFXv2.NanoFX_ScriptActions", "DestroyTGSequence", pSequence), 1.0)
                    pSequence.Play()
	pObject.CallNextHandler(pEvent)
		
###############################################################################
## Mini Rupture Creation Sequence
def CreateBCSMiniRuptureSequence(pEvent, sType):
	### Create Sequence
	debug(__name__ + ", CreateBCSMiniRuptureSequence")
	pSequence = App.TGSequence_Create()
	### Setup
	pShip = App.ShipClass_Cast(pEvent.GetTargetObject())
	if not pShip:
		return pSequence
        ### Fix the crash with small objects bug
        if pShip.GetRadius() < 0.1:
                return pSequence
	pSet = pShip.GetContainingSet()
	pAttachTo = pShip.GetNode()
        pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	vEmitPos = pEvent.GetObjectHitPoint()
	vEmitDir = pEvent.GetObjectHitNormal()

	if sType == "PhaserHullHit":
            if (App.g_kSystemWrapper.GetRandomNumber(100) < 100):
                pWarpSys = pShip.GetWarpEngineSubsystem()
                if pWarpSys:
                    iNumWarp = pWarpSys.GetNumChildSubsystems()
                    for iEng in range(iNumWarp):
                        pWarpEngine = pWarpSys.GetChildSubsystem(iEng)

                        #if (App.g_kSystemWrapper.GetRandomNumber(100) < 101):
                        if PointInSphere(vEmitPos, pWarpEngine.GetRadius(), pWarpEngine.GetWorldLocation()) == TRUE:
                            ### Point is on my engine
                            #if pWarpEngine.GetSqrLength() - vEmitPos.GetSqrLength() > SQ(pWarpEngine.GetRadius():       
                            pAction = (VentMiniPlasma(pWarpEngine, pShip,vEmitPos,vEmitDir))
                            pSequence.AddAction(pAction)
                
##
##	if sType == "TorpHullHit":
##		if (pEvent.GetDamage() >= 100 and sType == "TorpHullHit"):
##			if (App.g_kSystemWrapper.GetRandomNumber(100) < 50):
##                            pWarpSys = pShip.GetWarpEngineSubsystem()
##                            if pWarpSys:
##                                iNumWarp = pWarpSys.GetNumChildSubsystems()
##                                for iEng in range(iNumWarp):
##                                    pWarpEngine = pWarpSys.GetChildSubsystem(iEng)
##                                    if PointInSphere(vEmitPos, pWarpEngine.GetRadius(), pWarpEngine.GetWorldLocation()) == TRUE:
##                                        ### Point is on my engine
##                                        pAction = (VentMiniPlasma(pWarpEngine, pShip,vEmitPos))
##                                        pSequence.AddAction(pAction)
                            

	return pSequence

###################################################################################
# Create mini plasma streams *built from the ground up!*
def VentMiniPlasma(pWarpChild = None, pShip = None, VPos = None,vEmitDir = None):
    debug(__name__ + ", VentMiniPlasma")
    pSet          = pShip.GetContainingSet()
    pAttachTo     = pShip.GetNode()
    pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
    fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "PlasmaFX")
    if (fPlasmaColor == None):
            sRace	      = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
            fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)
    Seq = App.TGSequence_Create()

    for iMiniS in range(round(App.g_kSystemWrapper.GetRandomNumber(2) + 1)):
        # for each potential rupture
        if pWarpChild:
            if not vEmitDir:
                vEmitDir = App.TGPoint3()
                vEmitDir.SetXYZ(1,1,1)
            if not VPos:
                vEmitPos = pWarpChild.GetPosition()
            else:
                vEmitPos = VPos

                
            fSize = pShip.GetRadius() * 0.01
            pPlasma = CreateMiniPlasmaEffect(pEmitFrom,
                            
                                          pAttachTo,
                                          fSize,
                                          vEmitPos,
                                          vEmitDir,
                                          fVelocity = 0.2,
                                          fRed = fPlasmaColor[0],
                                          fGreen = fPlasmaColor[1],
                                          fBlue = fPlasmaColor[2],
                                          fBrightness = 0.10, fLen = pWarpChild.GetRadius())
            Seq.AddAction(pPlasma)

            fSize = pShip.GetRadius() * 0.005
            pPlasma = CreateMiniPlasmaEffect(pEmitFrom,
                            
                                          pAttachTo,
                                          fSize,
                                          vEmitPos,
                                          vEmitDir,
                                          fVelocity = 0.2,
                                          fRed = fPlasmaColor[0],
                                          fGreen = fPlasmaColor[1],
                                          fBlue = fPlasmaColor[2],
                                          fBrightness = 0.6, fLen = pWarpChild.GetRadius())
            Seq.AddAction(pPlasma)
    return Seq #.Play()  

###################################################################################
# Maths functions! oooo!
def SQ(num):
    debug(__name__ + ", SQ")
    return num*num

def Get2VectorLength(v1, v2):
    # Get the distance between two vectors
    debug(__name__ + ", Get2VectorLength")
    try:
        ### For NiPoint3
        return math.sqrt(SQ(v2.x - v1.x) + SQ(v2.y - v1.y) + SQ(v2.z - v1.z))
    except:
        ### For TGPoint3
        return math.sqrt(SQ(v2.GetX() - v1.GetX()) + SQ(v2.GetY() - v1.GetY()) + SQ(v2.GetZ() - v1.GetZ()))
    #return math.sqrt(SQ(v2.x - v1.GetX()) + SQ(v2.y - v1.GetY()) + SQ(v2.z - v1.GetZ()))

def PointInSphere(Point, SphereRadius, SphereCenter):
    # Determine if a point is within a sphere
    debug(__name__ + ", PointInSphere")
    if Get2VectorLength(SphereCenter, Point) >= SphereRadius:
        return FALSE
    else:
        return TRUE
