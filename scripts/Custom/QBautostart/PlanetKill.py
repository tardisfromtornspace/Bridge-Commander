from bcdebug import debug
import App
import MissionLib
import loadspacehelper
import Foundation
from Libs.LibQBautostart import *

# Settings
sFirepointScript = "BigFirepoint"
sFirepointScriptLong = "ships." + sFirepointScript
iPlanetOffset = 300
fRemoveFPDelay = 10
fSetNumTilesPerAxisRadiusDiv = 60
iSetNumAsteroidsPerTile = 5
fRoidSizeFactor = 1.0
fFPPowerOutMult = 300
fRemovePlanetDelay = 5
iNumHitsToDestroy = 3

"""
Basicly we do this:
1. Create a firepoint so we can shoot the planet
2. destroy the firepoint with a big shockwave
2. create an asteroid field at the planet
3. remove the planet

TODO:
-Support for AI ships
-MP support
"""

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Description": "I felt a great disturbance in the Force, as if millions of voices suddenly cried out in terror and were suddenly silenced",
                "needBridge": 0
            }


g_fCount = 0


def IsPlanetKiller(pShip):
	debug(__name__ + ", IsPlanetKiller")
	sShipType = GetShipType(pShip)
	if not sShipType:
		return 0

	if Foundation.shipList.has_key(sShipType):
		pFoundationShip = Foundation.shipList[sShipType]
		if pFoundationShip and hasattr(pFoundationShip, "bPlanetKiller"):
			return pFoundationShip.bPlanetKiller
	return 0


def GetFirepointName(sPlanetName):
	debug(__name__ + ", GetFirepointName")
	return sPlanetName + " FP"


def PlayerFirePimary(pObject, pEvent):
	debug(__name__ + ", PlayerFirePimary")
	pObject.CallNextHandler(pEvent)
	pPlayer = MissionLib.GetPlayer()
	
	if pPlayer and pPlayer.GetTarget() and pPlayer.GetTarget().IsTypeOf(App.CT_PLANET) and IsPlanetKiller(pPlayer):
		pShip = pPlayer
		pPlanet = App.Planet_Cast(pShip.GetTarget())
		pSystem = pShip.GetPhaserSystem()
		if pPlanet and pSystem:
			sThisFirePointName = GetFirepointName(pPlanet.GetName())
			pSet = pShip.GetContainingSet()
			pFirePoint = MissionLib.GetShip(sThisFirePointName)
			if not pFirePoint:
				pFirePoint = loadspacehelper.CreateShip(sFirepointScript, pSet, sThisFirePointName, None)
			if pFirePoint:
				pFirePoint.SetTargetable(0)
				pFirePoint.SetInvincible(1)
				pFirePoint.SetCollisionsOn(0)
				kPlanetPoint = pPlanet.GetWorldLocation()
				kShipPoint = pShip.GetWorldLocation()
				kLocation = App.TGPoint3()
				# what we need todo: Find the closest point to the ship on the planet.
				# ok the idea here is to increase the radius of the planet so the ship becomes a point on it.
				# then we decrease the radius again
				x1 = kPlanetPoint.GetX()
				y1 = kPlanetPoint.GetY()
				z1 = kPlanetPoint.GetZ()
				r1 = pPlanet.GetRadius()
				x2 = kShipPoint.GetX() - x1 # translate the coordinate to the planet view
				y2 = kShipPoint.GetY() - y1
				z2 = kShipPoint.GetZ() - z1
				r2 = Distance(pPlanet, pShip) - iPlanetOffset # r2 is our increased radius. decrement a bit, so we are a bit from the planet away (and from the NanoFX clouds)
				rdiff = r2/r1
				xn = x2 / rdiff + x1 # decrease radius and retranslate to universe view.
				yn = y2 / rdiff + y1
				zn = z2 / rdiff + z1
				kLocation.SetXYZ(xn, yn, zn)
				pFirePoint.SetTranslate(kLocation)
				pFirePoint.UpdateNodeOnly()
				pSystem.StartFiring(pFirePoint, pFirePoint.GetTargetOffsetTG())

				pSeq = App.TGSequence_Create()
				pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, sThisFirePointName), fRemoveFPDelay)
				pSeq.Play()
		

def RemoveObjectDelayed(pAction, pSet, sName):        
	debug(__name__ + ", RemoveObjectDelayed")
	pSet.RemoveObjectFromSet(sName)
	return 0


def PlaceAsteroidField(pAction, pSet, sName, fRadius, kLocation):
	debug(__name__ + ", PlaceAsteroidField")
	kThis = App.AsteroidFieldPlacement_Create(sName + " Asteroid field", pSet.GetName(), None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslate(kLocation)
	kThis.SetFieldRadius(fRadius)
	kThis.SetNumTilesPerAxis(fRadius/fSetNumTilesPerAxisRadiusDiv)
	kThis.SetNumAsteroidsPerTile(iSetNumAsteroidsPerTile)
	kThis.SetAsteroidSizeFactor(fRoidSizeFactor)
	kThis.UpdateNodeOnly()
	kThis.ConfigField()
	kThis.Update(0)
	return 0
	

def DestroyPlanet(pObject, pFirepoint):
	debug(__name__ + ", DestroyPlanet")
	pSet = pObject.GetContainingSet()
	if pSet:
		pFirepoint.SetTranslate(pObject.GetWorldLocation())
		pPower = pFirepoint.GetPowerSubsystem().GetProperty()
		pPower.SetPowerOutput(pObject.GetRadius()*fFPPowerOutMult)
		pFirepoint.SetInvincible(0)
		pFirepoint.SetTargetable(0)
		pFirepoint.DestroySystem(pFirepoint.GetHull())

		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RemoveObjectDelayed", pSet, pObject.GetName()), fRemovePlanetDelay)
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "PlaceAsteroidField", pSet, pObject.GetName(), pObject.GetRadius(), pObject.GetWorldLocation()))
		pSeq.Play()


def WeaponHit(pObject, pEvent):
	debug(__name__ + ", WeaponHit")
	global g_fCount
	pObject.CallNextHandler(pEvent)
	
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip and pShip.GetScript() == sFirepointScriptLong:
		pFirepoint = pShip
		pFiringPhaser = App.PhaserBank_Cast(pEvent.GetSource())
		if pFiringPhaser:
			pSystem = App.PhaserSystem_Cast(pFiringPhaser.GetParentSubsystem())
			if pSystem:
				pShip = pSystem.GetParentShip()
				if pShip and IsPlanetKiller(pShip) and pShip.GetTarget() and pShip.GetTarget().IsTypeOf(App.CT_PLANET):
					g_fCount = g_fCount + 1
					if g_fCount > iNumHitsToDestroy:
						DestroyPlanet(pShip.GetTarget(), pFirepoint)
						pShip.SetTarget(pFirepoint.GetName())
						g_fCount = 0
		
	
def init():
	debug(__name__ + ", init")
	if App.g_kUtopiaModule.IsMultiplayer():
		return
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, MissionLib.GetMission(), __name__+ ".WeaponHit")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_INPUT_FIRE_PRIMARY, MissionLib.GetMission(), __name__+ ".PlayerFirePimary")

