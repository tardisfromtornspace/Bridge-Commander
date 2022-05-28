from bcdebug import debug
import App
import MissionLib
import Libs.LibEngineering

from Libs.Races import Races
from Libs.LibQBautostart import *


MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "Version": "0.2",
                "License": "GPL",
                "Description": "Allows all ships to Surrender in QB",
                "needBridge": 0
            }


iChangeSideChance = 5
iSurrenderChance = 30
iFleetFollowSurrenderChance = 20

SurrenderLock = 0
lSurrenderDone = []

NonSerializedObjects = (
"lSurrenderDone"
)

lNeverSurrender = [
"cOWP"
]

def addShipsOfGroupAndSameRaceFromSetToGroup(sRace, pSet, sGroup1, sGroup2, bIgnorePlayer=1):
        debug(__name__ + ", addShipsOfGroupAndSameRaceFromSetToGroup")
        pGroupFrom = getGroup(sGroup1)
        if not pGroupFrom:
                return
        lpGroup = pGroupFrom.GetActiveObjectTupleInSet(pSet)
        for ship in lpGroup:
                pShip = App.ShipClass_Cast(ship)
                sCurRace = GetRaceFromShip(pShip)
                if sCurRace == sRace and not pShip.IsPlayerShip() and not pShip.GetObjID() in lSurrenderDone and not pShip.IsDead() and not pShip.IsDying() and pShip.GetAI():
			lSurrenderDone.append(pShip.GetObjID())
                        addShipToGroup(pShip.GetName(), sGroup2)
                        autoAI(pShip)


def UnlockSurrender(pAction):
        debug(__name__ + ", UnlockSurrender")
        global SurrenderLock
        SurrenderLock = 0
        return 0


def LockSurrender(fTime = 20.0):
        debug(__name__ + ", LockSurrender")
        global SurrenderLock
        SurrenderLock = 1
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UnlockSurrender"), fTime)
        pSeq.Play()
        

def getSurrenderChanceAgainst(pGroup, pSet):
        debug(__name__ + ", getSurrenderChanceAgainst")
        lpGroup = pGroup.GetActiveObjectTupleInSet(pSet)
        lRaces = []
        numRaces = 0
        fCurSurrenderChance = 0.0
        for ship in lpGroup:
                pShip = App.ShipClass_Cast(ship)
                sCurRace = GetRaceFromShip(pShip)
                if not sCurRace in lRaces:
                        if Races.has_key(sCurRace):
                                lRaces.append(sCurRace)
                                numRaces = numRaces + 1
                                fCurSurrenderChance = fCurSurrenderChance + Races[sCurRace].GetPeaceValue()
        
        if numRaces == 0:
                return 1.0
        return fCurSurrenderChance / numRaces


def IsHeavilyDamaged(pShip):
        debug(__name__ + ", IsHeavilyDamaged")
        pHull = pShip.GetHull()
        pShields = pShip.GetShields()
        pImpulse = pShip.GetImpulseEngineSubsystem()
        pPower = pShip.GetPowerSubsystem()
        pSensors = pShip.GetSensorSubsystem()
        inumSystemsCheck = 10 + 1 + 2 + 2 + 1

        if pImpulse:
                fImpulseCondition = pImpulse.GetConditionPercentage()
        else:
                fImpulseCondition = 0.5
        if pSensors:
                fSensorCondition = pSensors.GetConditionPercentage()
        else:
                fSensorCondition = 0.5
        
        fStatus = pHull.GetConditionPercentage() * 10 + pShields.GetConditionPercentage() + fImpulseCondition * 2 + pPower.GetConditionPercentage() * 2 + fSensorCondition
        #print fStatus, inumSystemsCheck, fStatus / inumSystemsCheck
	f = fStatus / inumSystemsCheck
	debug(__name__ + ", IsHeavilyDamaged End")
        if f < 0.5:
                return f
        return 0


def GetFleetDamage(sRace, sGroup, pSet):
        debug(__name__ + ", GetFleetDamage")
        pGroup = getGroup(sGroup)
        lpGroup = pGroup.GetActiveObjectTupleInSet(pSet)
        iNumShips = 0
        fDamageVal = 0.0
        for ship in lpGroup:
                pShip = App.ShipClass_Cast(ship)
                fcurDamageVal = IsHeavilyDamaged(pShip)
                if fcurDamageVal:
                        fDamageVal = fDamageVal + fcurDamageVal
                else:
                        fDamageVal = fDamageVal + 1.0
                iNumShips = iNumShips + 1
        if iNumShips > 0:
                return fDamageVal / iNumShips
        else:
                return 0


def CreateWarpOutAI(pShip):
	#########################################
	# Creating PlainAI WarpNowhere at (11, 19)
	debug(__name__ + ", CreateWarpOutAI")
	pWarpNowhere = App.PlainAI_Create(pShip, "WarpNowhere")
	pWarpNowhere.SetScriptModule("Warp")
	pWarpNowhere.SetInterruptable(1)
	# Done creating PlainAI WarpNowhere
	#########################################
	return pWarpNowhere


def IsGroupNotOutnumbered(sGroup):
	debug(__name__ + ", IsGroupNotOutnumbered")
	pGroup = getGroup(sGroup)
	pOppositeGroup = getGroup(getOppositeGroup(sGroup))
	if pGroup and pOppositeGroup and len(pOppositeGroup.GetNameTuple()) < len(pGroup.GetNameTuple()):
		return 1
	return 0


def CheckFleetFollowSurrender(sRace, sGroup, pSet):
        debug(__name__ + ", CheckFleetFollowSurrender")
        fFleetDamage = GetFleetDamage(sRace, sGroup, pSet)
        fSurrenderChance = (Races[sRace].GetPeaceValue() + (1 - fFleetDamage)) / 2
        iSurrenderChance = int((fSurrenderChance * 100))
        if chance(iSurrenderChance) and chance(iFleetFollowSurrenderChance) and not IsGroupNotOutnumbered(sGroup):
                # maybe warp out
                #pGroupFrom = getGroup(sGroup)
                #if chance(50) and pGroupFrom:
                #        lpGroup = pGroupFrom.GetActiveObjectTupleInSet(pSet)
                #        for ship in lpGroup:
                #                pShip = App.ShipClass_Cast(ship)
                #                sCurRace = GetRaceFromShip(pShip)
                #                if sCurRace == sRace:
                #                        pShip.SetAI(CreateWarpOutAI(pShip))
		#else:
                addShipsOfGroupAndSameRaceFromSetToGroup(sRace, pSet, sGroup, "neutral")


def SurrenderPlayer(pObject, pEvent):
	debug(__name__ + ", SurrenderPlayer")
	global lSurrenderDone
	
        pPlayer = MissionLib.GetPlayer()
        pEnemy = getGroup("enemy")
        pSet = pPlayer.GetContainingSet()
        
        # chance that they would accept the surrender
        iSurrenderChance = int((getSurrenderChanceAgainst(pEnemy, pSet) * 100))

        # now chance that they DO accept the surrender
        if not SurrenderLock and chance(iSurrenderChance) and not pPlayer.GetObjID() in lSurrenderDone:
                LockSurrender()
		lSurrenderDone.append(pPlayer.GetObjID())
                pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
                pButton = Libs.LibEngineering.GetButton("Surrender", pMenu)
                pButton.SetDisabled()
                pFriendlies = getGroup("friendly")
                RemoveNameFromGroup(pFriendlies, pPlayer.GetName())
                CheckFleetFollowSurrender(GetRaceFromShip(pPlayer), "friendly", pSet)
                Say("AcceptSurrender", "Helm", "data/TGL/Surrender.tgl")
                SetAlertLevel(pPlayer, "green")
        
        
def CheckState(pAttacker, pDamagedShip):
        debug(__name__ + ", CheckState")
        fStatus = IsHeavilyDamaged(pDamagedShip)
        if fStatus:
                SurrenderAI(pAttacker, pDamagedShip, fStatus)
	debug(__name__ + ", CheckState End")


def RaceCanChangeSide(sRace):
        debug(__name__ + ", RaceCanChangeSide")
        if sRace in ["Cardassian", "Ferengi"]:
                return 1
        return 0
        
        
def SurrenderAI(pAttacker, pDamagedShip, fStatus):
        debug(__name__ + ", SurrenderAI")
        global lSurrenderDone
        
        sDamagedRace = GetRaceFromShip(pDamagedShip)
        if not Races.has_key(sDamagedRace):
                return
        iDamagedShipPeaceVal = Races[sDamagedRace].GetPeaceValue() * 100
        sAttackerGroup = getGroupFromShip(pAttacker.GetName())
        sDamagedGroup = getGroupFromShip(pDamagedShip.GetName())
        pAttackerGroup = getGroup(sAttackerGroup)
        pSet = pDamagedShip.GetContainingSet()
        fRaceSurrenderChance = getSurrenderChanceAgainst(pAttackerGroup, pSet)
        iSurrenderChance = int(((((1-fStatus) + fRaceSurrenderChance) / 2.0) * 100))
        
        # check change side
        if not SurrenderLock and not pDamagedShip.IsDead() and not pDamagedShip.IsDying() and pDamagedShip.GetAI() and GetFleetDamage(sDamagedRace, sDamagedGroup, pSet) and RaceCanChangeSide(sDamagedRace) and chance(iChangeSideChance):
                LockSurrender()
                lSurrenderDone.append(pDamagedShip.GetObjID())
                addShipsOfGroupAndSameRaceFromSetToGroup(sDamagedRace, pSet, sDamagedGroup, sAttackerGroup)
                if sDamagedRace == "Cardassian":
                        Say("CardassianChangeSide", "Helm", "data/TGL/Surrender.tgl")
                else:
                        Say("ChangeSide", "Helm", "data/TGL/Surrender.tgl")
        
        elif not SurrenderLock and not pDamagedShip.IsDead() and not pDamagedShip.IsDying() and pDamagedShip.GetAI() and chance(iSurrenderChance) and chance(80) and not pDamagedShip.GetObjID() in lSurrenderDone and chance(iSurrenderChance) and chance(iDamagedShipPeaceVal):
                LockSurrender()
                lSurrenderDone.append(pDamagedShip.GetObjID())
                pGroup = getGroup(sDamagedGroup)
                pNeutralGroup = getGroup("neutral")
                if pGroup:
                        RemoveNameFromGroup(pGroup, pDamagedShip.GetName())
                        if not pNeutralGroup.IsNameInGroup(pDamagedShip.GetName()):
                                pNeutralGroup.AddName(pDamagedShip.GetName())
                        pDamagedShip.ClearAI()
                CheckFleetFollowSurrender(sDamagedRace, sDamagedGroup, pSet)
                Say("Surrender", "Helm", "data/TGL/Surrender.tgl")
                SetAlertLevel(pDamagedShip, "green")
	else:
        	# lock it for a random time
        	LockSurrender(App.g_kSystemWrapper.GetRandomNumber(10))


def CheckNeutralHit(pAttacker, pDamagedShip):
        debug(__name__ + ", CheckNeutralHit")
        if not SurrenderLock and isNeutral(pDamagedShip.GetName()):
                LockSurrender()
                firegroup = getGroupFromShip(pAttacker.GetName())
                sRace = GetRaceFromShip(pDamagedShip)
                pSet = pDamagedShip.GetContainingSet()
                if firegroup == "friendly":
                        addShipsOfGroupAndSameRaceFromSetToGroup(sRace, pSet, "neutral", "enemy")
                else:
                        addShipsOfGroupAndSameRaceFromSetToGroup(sRace, pSet, "neutral", "friendly")


def CheckIfNeutralFired(pAttacker, pDamagedShip):
        debug(__name__ + ", CheckIfNeutralFired")
        if pAttacker and isNeutral(pAttacker.GetName()):
                sDamagedGroup = getGroupFromShip(pDamagedShip.GetName())
                sGroup = getOppositeGroup(sDamagedGroup)
                if sGroup:
                        pGroup = getGroup(sGroup)
                        if not pGroup.IsNameInGroup(pAttacker.GetName()):
                                pGroup.AddName(pAttacker.GetName())
			pNeutralGroup = getGroup("neutral")
			if pNeutralGroup.IsNameInGroup(pAttacker.GetName()):
                                RemoveNameFromGroup(pNeutralGroup, pAttacker.GetName())
        
        
def WeaponHit(pObject, pEvent):
        # Get the ship that was hit
        debug(__name__ + ", WeaponHit")
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        # Get the the shooter.
        pAttacker = pEvent.GetFiringObject()

        # only non-player ships
        if not SurrenderLock and pAttacker and pShip and not pShip.GetNetPlayerID() > 0 and not GetShipType(pShip) in lNeverSurrender:
                CheckIfNeutralFired(pAttacker, pShip)
                CheckNeutralHit(pAttacker, pShip)
                if not pShip.GetObjID() in lSurrenderDone:
                        CheckState(pAttacker, pShip)

	debug(__name__ + ", WeaponHit End")
	pObject.CallNextHandler(pEvent)


def init():
        debug(__name__ + ", init")
        global SurrenderLock, lSurrenderDone, lSurrenderDone
        
        if not Libs.LibEngineering.CheckActiveMutator("Allow Surrender"):
                return
        
        # no MP support right now
        if App.g_kUtopiaModule.IsMultiplayer():
                return

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return

        pMission = MissionLib.GetMission()
        if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
                App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_WEAPON_HIT, pMission, __name__+ ".WeaponHit")
	pHelmMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
	if pHelmMenu:
		pMasterButton = App.STMenu_CreateW(App.TGString("Surrender"))
		pHelmMenu.PrependChild(pMasterButton)
        	Libs.LibEngineering.CreateMenuButton("Yes", "Helm", __name__ + ".SurrenderPlayer", 0, pMasterButton)

        SurrenderLock = 0
        lSurrenderDone = []


def Restart():
        debug(__name__ + ", Restart")
        global SurrenderLock, lSurrenderDone
        
	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	
        SurrenderLock = 0
        lSurrenderDone = []
        pMenu = Libs.LibEngineering.GetBridgeMenu("Helm")
        pButton = Libs.LibEngineering.GetButton("Surrender", pMenu)
        if pButton:
                pButton.SetEnabled()
