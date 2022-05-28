from bcdebug import debug
"""
Functions:
==========
AddNameToGroup(pGroup, sName):
        Adds a name to the group

addShipToGroup(sShipName, sGroupName):
        Adds a ship to a group
        sGroupName: "enemy", "friendly" or "neutral"

autoAI(pShip):
        Sets the Foundation friendly or enemy ship depends on its group

chance(iRand):
        Calculates a chance
        iRand: between 0 and 99

Distance(pObject1, pObject2):
        returns the distance of two Objects

GetFoundationAI(pShip, sGroup):
        Returns the sGroup = "friendly" | "enemy" AI for pShip

getGroup(sGroupName):
        For "friendly" it returns the friendly group etc

getGroupFromShip(sShipName):
        Returns the group a ship is in. ("friendly", "enemy" or "neutral")

getOppositeGroup(sGroup):
        for "friendly" returns "enemy" and vice versa

GetRaceFromShip(pShip):
        Returns the Race of ship (Federation, Klingon...)

GetRaceFromShipType(sShipType):
	Returns the Race of a shiptype

GetShipType(pShip):
        Returns the ship file without folders

isNeutral(sShipName):
        Guess it

RemoveNameFromGroup(pGroup, sName):
        Remove a ship name of a group - the way without lag

Say(SayString, Person, sDatabase):
        Make a person say something
        sDatabase: Database path

SetAlertLevel(pShip, sType):
        Sets sType = "red" | "green" | "yellow" alert for pShip
        
GetRandomShipForRace(sRace):
        Returns a Random Ship for sRace

def IsSameGroup(pShip1, pShip2):
	debug(__name__ + ", IsSameGroup")
	True if same Group

def IsSameRace(pShip1, pShip2):
	debug(__name__ + ", IsSameRace")
	True if same Race
	
def GetSystemShortName(pSet):
	debug(__name__ + ", GetSystemShortName")
	Returns a short string for pSet
	
def GetStationaryShipsIn(pSet):
	debug(__name__ + ", GetStationaryShipsIn")
	Returns all stationary ships in pSet
	
def GetRacesForSet(pSet):
	debug(__name__ + ", GetRacesForSet")
	Returns a list which all races claiming to own pSet
"""


import App
import string
import MissionLib
import Foundation
import LibEngineering
from Races import Races

bMission4Available = 1
try:
	from Multiplayer.Episode.Mission4.Mission4 import SendGroupInfo
except:
	bMission4Available = 0
	pass


def chance(iRand):
        debug(__name__ + ", chance")
        return App.g_kSystemWrapper.GetRandomNumber(100) < iRand


def addShipToGroup(sShipName, sGroupName):
	debug(__name__ + ", addShipToGroup")
	pGroup = getGroup(sGroupName)
	
	if sGroupName == "friendly":
		RemoveNameFromGroup(getGroup("enemy"), sShipName)
		RemoveNameFromGroup(getGroup("neutral"), sShipName)
		if App.g_kUtopiaModule.IsMultiplayer() and bMission4Available:
			SendGroupInfo(sShipName, -1)
	elif sGroupName == "enemy":
		RemoveNameFromGroup(getGroup("friendly"), sShipName)
		RemoveNameFromGroup(getGroup("neutral"), sShipName)
		if App.g_kUtopiaModule.IsMultiplayer() and bMission4Available:
			SendGroupInfo(sShipName, -2)
	elif sGroupName == "neutral":
		RemoveNameFromGroup(getGroup("friendly"), sShipName)
		RemoveNameFromGroup(getGroup("neutral"), sShipName)
		if App.g_kUtopiaModule.IsMultiplayer() and bMission4Available:
			SendGroupInfo(sShipName, 0)
	if pGroup:
		AddNameToGroup(pGroup, sShipName)


def isNeutral(sShipName):
	debug(__name__ + ", isNeutral")
	if getGroupFromShip(sShipName) == "neutral" or getGroupFromShip(sShipName) == None:
		return 1
	return 0


def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        if pShip and pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None


def GetRaceFromShip(pShip):
	debug(__name__ + ", GetRaceFromShip")
	sShipType = GetShipType(pShip)
	return GetRaceFromShipType(sShipType)


def GetRaceFromShipType(sShipType):
        debug(__name__ + ", GetRaceFromShipType")
        if Foundation.shipList.has_key(sShipType):
                FdtnShip = Foundation.shipList[sShipType]
        
                if FdtnShip.GetRace():
                        return FdtnShip.GetRace().name
        return None


def getGroupFromShip(sShipName):
	debug(__name__ + ", getGroupFromShip")
	pFriendlys = MissionLib.GetFriendlyGroup()
	pEnemys = MissionLib.GetEnemyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	if pFriendlys and pFriendlys.IsNameInGroup(sShipName):
		return "friendly"
	elif pEnemys and pEnemys.IsNameInGroup(sShipName):
		return "enemy"
	elif pNeutrals and pNeutrals.IsNameInGroup(sShipName):
		return "neutral"
	return None


def getGroup(sGroupName):
	debug(__name__ + ", getGroup")
	if sGroupName == "friendly":
		return MissionLib.GetFriendlyGroup()
	elif sGroupName == "enemy":
		return MissionLib.GetEnemyGroup()
	else:
		return MissionLib.GetNeutralGroup()


def GetFoundationAI(pShip, sGroup):
	debug(__name__ + ", GetFoundationAI")
	FdtnShips = Foundation.shipList
	if GetShipType(pShip) and FdtnShips.has_key(GetShipType(pShip)):
		ship = FdtnShips[GetShipType(pShip)]
		if sGroup == "friendly":
			return ship.StrFriendlyAI()
		elif sGroup == "enemy":
			return ship.StrEnemyAI()
	return None


def autoAI(pShip):
	debug(__name__ + ", autoAI")
	if getGroupFromShip(pShip.GetName()) == "friendly":
		pFdtnAI = GetFoundationAI(pShip, "friendly")
                if not pFdtnAI:
                        return
		
		if pFdtnAI == "QuickBattleFriendlyAI":
			pShip.SetAI(LibEngineering.CreateFriendlyAI(pShip))
		elif pFdtnAI == "StarbaseFriendlyAI":
			# Add the starbase itself to the attacker list -- the AI needs to have
			# *something* on the attacker list so as not to crash, but it won't
			# try to attack itself
			pEnemies = getGroup("enemy")
			#AddNameToGroup(pEnemies, pShip.GetName())
			pShip.SetAI(LibEngineering.CreateStarbaseFriendlyAI(pShip))
			#RemoveNameFromGroup(pEnemies, pShip.GetName())
                else:
                        pAIModule = __import__("QuickBattle." + pFdtnAI)
                        try:
                                pShip.SetAI(pAIModule.CreateAI(pShip, getGroup("enemy")))
                        except:
                                pShip.SetAI(pAIModule.CreateAI(pShip))

	elif getGroupFromShip(pShip.GetName()) == "enemy":
		pFdtnAI = GetFoundationAI(pShip, "enemy")
                if not pFdtnAI:
                        return

                if pFdtnAI == "QuickBattleAI":
                        pShip.SetAI(LibEngineering.CreateEnemyAI(pShip))
                elif pFdtnAI == "StarbaseAI":
                        # Add the starbase itself to the attacker list -- the AI needs to have
                        # *something* on the attacker list so as not to crash, but it won't
                        # try to attack itself
                        pFriendlies = getGroup("friendly")
			#AddNameToGroup(pFriendlies, pShip.GetName())
                        pShip.SetAI(LibEngineering.CreateStarbaseEnemyAI(pShip))
                        #RemoveNameFromGroup(pFriendlies, pShip.GetName())
                else:
                        pAIModule = __import__("QuickBattle." + pFdtnAI)
                        try:
                                pShip.SetAI(pAIModule.CreateAI(pShip, getGroup("friendly")))
                        except:
                                pShip.SetAI(pAIModule.CreateAI(pShip))

        else:
                pShip.ClearAI()


def Say(SayString, Person=None, sDatabase=None, fDuration=5.0):
        debug(__name__ + ", Say")
        pBridge	= App.g_kSetManager.GetSet('bridge')

        if pBridge and Person and sDatabase:
                g_pPerson = App.CharacterClass_GetObject(pBridge, Person) 
                if g_pPerson:
                        pDatabase = App.g_kLocalizationManager.Load(sDatabase)
                        pSequence = App.TGSequence_Create()
                        pSequence.AppendAction(App.CharacterAction_Create(g_pPerson, App.CharacterAction.AT_SAY_LINE, SayString, None, 0, pDatabase))
                        pSequence.Play()
                        App.g_kLocalizationManager.Unload(pDatabase)
	# alternate message if we don't have a Bridge or not a person
	else:
		if Person: # no Bridge but person
			pcString = Person + ": " + SayString
		else: # other custom message, just print it
			pcString = SayString
		pSequence = App.TGSequence_Create()
        	pSubtitleAction = App.SubtitleAction_CreateC(pcString)
        	pSubtitleAction.SetDuration(fDuration)
        	pSequence.AddAction(pSubtitleAction)
        	pSequence.Play()
        
        	App.STMissionLog_GetMissionLog().AddLine(App.TGString(pcString))


def getOppositeGroup(sGroup):
        debug(__name__ + ", getOppositeGroup")
        if sGroup == "enemy":
                return "friendly"
        elif sGroup == "friendly":
                return "enemy"
        else:
                return None


"""def RemoveNameFromGroup(pGroup, sName):
        if pGroup:
                lNames = pGroup.GetNameTuple()
                pGroup.RemoveAllNames()

                for sCurName in lNames:
                        if sCurName != sName:
                                pGroup.AddName(sCurName)"""


def RemoveNameFromGroup(pGroup, sName):
        debug(__name__ + ", RemoveNameFromGroup")
        if pGroup and pGroup.IsNameInGroup(sName):
                pGroup.RemoveName(sName)
        

def AddNameToGroup(pGroup, sName):
        debug(__name__ + ", AddNameToGroup")
        if pGroup and not pGroup.IsNameInGroup(sName):
                pGroup.AddName(sName)


# pWarbird.SetAlertLevel(App.ShipClass.GREEN_ALERT)
def SetAlertLevel(pShip, sType):
        debug(__name__ + ", SetAlertLevel")
        pAlertEvent = App.TGIntEvent_Create()
        pAlertEvent.SetDestination(pShip)
        pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
        if sType == "green":
                pAlertEvent.SetInt(pShip.GREEN_ALERT)
        elif sType == "red":
                pAlertEvent.SetInt(pShip.RED_ALERT)
        else: # yellow
                pAlertEvent.SetInt(pShip.YELLOW_ALERT)
        App.g_kEventManager.AddEvent(pAlertEvent)


def Distance(pObject1, pObject2):
	debug(__name__ + ", Distance")
	vDifference = pObject1.GetWorldLocation()
	vDifference.Subtract(pObject2.GetWorldLocation())

	return vDifference.Length()


def GetRandomShipForRace(sRace):
        debug(__name__ + ", GetRandomShipForRace")
        sShipType = ""
        
        if len(Races[sRace].GetShips()) > 0:
                iRandTypeNum = App.g_kSystemWrapper.GetRandomNumber(len(Races[sRace].GetShips()))
                sShipType = Races[sRace].GetShips()[iRandTypeNum]
        return sShipType


def IsSameGroup(pShip1, pShip2):
	debug(__name__ + ", IsSameGroup")
	return getGroupFromShip(pShip1.GetName()) == getGroupFromShip(pShip2.GetName())


def IsSameRace(pShip1, pShip2):
	debug(__name__ + ", IsSameRace")
	return GetRaceFromShip(pShip1) == GetRaceFromShip(pShip2)


# not implemented yet
def IsMultiplayerHostAlone():
	debug(__name__ + ", IsMultiplayerHostAlone")
	return 1-App.g_kUtopiaModule.IsMultiplayer()


def GetSystemShortName(pSet):
	debug(__name__ + ", GetSystemShortName")
	if pSet and pSet.GetRegionModule():
		return string.split(pSet.GetRegionModule(), '.')[1]
	return ""


def GetStationaryShipsIn(pSet):
	debug(__name__ + ", GetStationaryShipsIn")
	lRet = []
	
	if not pSet:
		return lRet
	
	lObjects = pSet.GetClassObjectList(App.CT_SHIP)
	for pObject in lObjects:
		pShip = App.ShipClass_Cast(pObject)
		if pShip.GetShipProperty().IsStationary():
			lRet.append(pShip)
	
	return lRet


def GetRacesForSet(pSet):
	debug(__name__ + ", GetRacesForSet")
	lRet = []
	sSetName = GetSystemShortName(pSet)
	for sRace in Races.keys():
		if sSetName in Races[sRace].GetSystems():
			lRet.append(sRace)
	return lRet
