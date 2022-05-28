from bcdebug import debug
###############################################################################################################
#   HelmAddonGUI.py                 by Fernando Aluani
############
# This script is the one that contains the code which sets up and handles the Helm Addons GUI
# in the Helm Menu. Which is pretty much the "simple" buttons/features added to the Helm.
###############################################################################################################
import App
import MissionLib
import string
from Custom.GravityFX.GravityFXguilib import *
import GalaxyLIB
import GalaxyMapGUI
import GalacticWarSimulator

pGUICreator = None
ET_EVENT = None
pDropOutButton = None
pEmergencyOut = None
pMenu = None
dCodeTT = {}
bIsCreated = 0
sSelectedTravelType = ""
iPlayerID = 0
lOldTTlist = []
pFleetStats = None

#####################################################################
def CreateHAGUI():
	debug(__name__ + ", CreateHAGUI")
	global ET_EVENT, pGUICreator, pDropOutButton, pMenu, pEmergencyOut, pFleetStats

	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet("bridge")
	pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
	if pHelm == None:
		return
	pHelmMenu = pHelm.GetMenu()
	if pHelmMenu == None:
		return

	pGUICreator = GUICreator()

	ET_EVENT = GetNextEventType()
	
	pDropOutButton = pGUICreator.ButtonCreator.CreateButton("Drop Out of Travel", None, "Custom.GalaxyCharts.GalaxyMapGUI.DropOutClick", 1, pHelmMenu)
	pDropOutButton.SetDisabled()
	pEmergencyOut = pGUICreator.ButtonCreator.CreateButton("Emergency ", None, __name__+".EmergencyOutClick", 1, pHelmMenu)
	pEmergencyOut.SetDisabled()
	pMenu = CreateCharMenu("Travel Method: default", pHelmMenu)

	if GalacticWarSimulator.WarSimulator.IsInitialized() == 1:
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pGUICreator.SetInfoForName("Player Fleet Status", 0.7, 0.0, 0.3, 0.0625, 1, 0, "NormalStyle")
		pFleetStats = pGUICreator.CreateWindow("Player Fleet Status", pTCW)
		#pFleetStats.SetUseScrolling(1)
		#pFleetStats.SetScrollViewHeight(25.0)

		pGUICreator.SetInfoForName("FS_NamePara", 0.0, 0.0)
		pGUICreator.CreateParagraph("FS_NamePara", ["names..."], pFleetStats)
		##
		pGUICreator.SetInfoForName("FS_StatPara", 0.1, 0.0)
		pGUICreator.CreateParagraph("FS_StatPara", ["status..."], pFleetStats)
		##
		pGUICreator.SetInfoForName("FS_InfoPara", 0.15, 0.0)
		pGUICreator.CreateParagraph("FS_InfoPara", ["details and info..."], pFleetStats)

# This function is called constantly by the Player's Chaser Update loop, just as it needs to be (delay 0.1 secs)
def CreateTravelTypeButtons():
	debug(__name__ + ", CreateTravelTypeButtons")
	global pMenu, dCodeTT, bIsCreated, sSelectedTravelType, iPlayerID, lOldTTlist
	if pGUICreator == None:
		return
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		print "Error at HelmAddonGUI: couldn't find player to create travel type buttons"
		return
	UpdateFleetStatsWindow()

	lTravelTypes = GetAllTTAvailableForPlayer(pPlayer)
	if lTravelTypes == lOldTTlist:
		return
	lOldTTlist = lTravelTypes

	ClearTravelTypeMenu()
	dCodeTT = {0: "None"}
	iIndex = 0
	for sTravelType in lTravelTypes:
		iIndex = iIndex + 1
		dCodeTT[iIndex] = sTravelType
		pGUICreator.ButtonCreator.CreateButton(sTravelType, None, __name__ + ".UpdateTravelType", iIndex, pMenu)
	if sSelectedTravelType == "" or sSelectedTravelType == "None" or pPlayer.GetObjID() != iPlayerID or not sSelectedTravelType in lTravelTypes:
		UpdateTravelType(iIndex)
	UpdateEmergencyOutButton()
	iPlayerID = pPlayer.GetObjID()
	bIsCreated = 1

# this function can be called as a event handler, or as a single INT argument(pObject) function.
def UpdateTravelType(pObject, pEvent = None):
	debug(__name__ + ", UpdateTravelType")
	global pMenu, dCodeTT, sSelectedTravelType
	if type(pObject) == type(1):
		iIndex = pObject
	else:
		if pEvent == None:
			return
		iIndex = pEvent.GetInt()
	sSelectedTravelType = dCodeTT[iIndex]
	pMenu.SetName(App.TGString("Travel Method: "+sSelectedTravelType))
	pMenu.Close()
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer != None:
		pTravel = App.g_kTravelManager.GetTravel(pPlayer)
		if pTravel != None:
			pTravel.SetTravelType(sSelectedTravelType)
			pTravel.SetSpeed(pTravel.GetActualCruiseSpeed())
	GalaxyMapGUI.UpdateTTPara()
	UpdateEmergencyOutButton()

iLastFleetSize = 0
def UpdateFleetStatsWindow():
	debug(__name__ + ", UpdateFleetStatsWindow")
	global pFleetStats, iLastFleetSize
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None or pFleetStats == None:
		return
	pTop = App.TopWindow_GetTopWindow()
	if pTop.IsTacticalVisible():
		pFleetStats.SetVisible()
	else:
		pBridge = App.g_kSetManager.GetSet("bridge")
		pTac = App.CharacterClass_GetObject(pBridge, "Tactical")
		pTacMenu = None
		if pTac != None:
			pTacMenu = pTac.GetMenu()
		if pTacMenu != None and pTacMenu.IsVisible():
			pFleetStats.SetVisible()
		else:
			pFleetStats.SetNotVisible()
			return
	lNamesList = []
	lStatsList = []
	lInfoList = []
	pFleet = GalacticWarSimulator.FleetManager.GetFleetOfShip(pPlayer)
	if pFleet != None:
		sName = pFleetStats.GetName().GetCString()
		if sName != pFleet.GetName()+" Status":
			pFleetStats.SetName(App.TGString(pFleet.GetName()+" Status"))
			pFleetStats.SetTitleBarThickness(0.0)
		lShips = pFleet.GetShipObjList()
		if len(lShips) > 1:
			for pShip in lShips:
				if pShip.GetObjID() != pPlayer.GetObjID():
					lNamesList.append(pShip.GetName() )
					if pFleet.GetShipStatus(pShip) == pFleet.ACTIVE:
						lStatsList.append("ACTIVE")
					else:
						lStatsList.append("IDLE")
					pWSShip = GalacticWarSimulator.WarSimulator.GetWSShipObjForShip(pShip)
					if pWSShip.IsShipDocking() == 1:
						lInfoList.append( pWSShip.GetStatusStr() )
					else:
						pAI = pShip.GetAI()
						if pAI != None:
							lFAIs = pAI.GetFocusAIs()
							if lFAIs != None and len(lFAIs) >= 1:
								index = len(pAI.GetFocusAIs()) - 1
								lInfoList.append( pAI.GetFocusAIs()[index].GetName() )
							else:
								lInfoList.append("doing nothing...")
						else:
							lInfoList.append("no further details...")
		else:
			lNamesList.append("There are no ships in player's fleet.")
	else:
		lNamesList.append("Player is not in any fleet...")
	pGUICreator.UpdateParagraph("FS_NamePara", lNamesList)
	pGUICreator.UpdateParagraph("FS_StatPara", lStatsList)
	pGUICreator.UpdateParagraph("FS_InfoPara", lInfoList)
	pPara1 = pGUICreator.GetElement("FS_NamePara")
	pPara1.SetPosition(0.0, 0.0)
	pPara2 = pGUICreator.GetElement("FS_StatPara")
	pPara2.SetPosition(0.1, 0.0)
	pPara3 = pGUICreator.GetElement("FS_InfoPara")
	pPara3.SetPosition(0.15, 0.0)
	if len(lNamesList) != iLastFleetSize:
		pFleetStats.SetFixedSize(pFleetStats.GetWidth(), (len(lNamesList)*0.0195)+0.043 )
		iLastFleetSize = len(lNamesList)
	
def ClearTravelTypeMenu():
	debug(__name__ + ", ClearTravelTypeMenu")
	global pMenu, bIsCreated
	if bIsCreated == 1:
		pMenu.KillChildren()
		pMenu.Close()
		bIsCreated = 0

def GetAllTTAvailableForPlayer(pShip):
	debug(__name__ + ", GetAllTTAvailableForPlayer")
	global lOldTTlist
	lList = []
	for sTravelType in App.g_kTravelManager.dTravelTypes.keys():
		if App.g_kTravelManager.IsShipEquippedWithTravelType(pShip, sTravelType) == 1:
			lList.append(sTravelType)
		elif App.g_kTravelManager.IsTravelTypeShipBased(sTravelType) == 0:
			if App.g_kTravelManager.IsShipInLaunchPosFor(pShip, sTravelType) != None:
				if not sTravelType in lOldTTlist:
					# show warning "reached launch coordinates"
					GalaxyLIB.ShowTextBanner("Reached Launch Coordinates", 0.3, 0.25, 3.0, 15, 1, 0)
					GalaxyLIB.ShowTextBanner("for "+sTravelType, 0.3, 0.3, 3.0, 15, 1, 0)
				lList.append(sTravelType)
	lList.sort()
	return lList

def EmergencyOutClick(pObject, pEvent):
	debug(__name__ + ", EmergencyOutClick")
	oTravelType = CanEmergencyTravelOut()
	if oTravelType == 0:
		return
	pPlayer = App.Game_GetCurrentPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pTravel == None:
		return
	if pTravel.IsTravelling() == 1:
		return
	pRegion = GetClosestRegionToPlayer(oTravelType)
	if pTravel.GetTravelType() != oTravelType:
		pTravel.SetTravelType(oTravelType)
	pTravel.SetSpeed( pTravel.GetActualCruiseSpeed() )
	pTravel.TravelTo( pRegion.BorderSet.GetScriptFile() )


def CanEmergencyTravelOut():
	debug(__name__ + ", CanEmergencyTravelOut")
	global pEmergencyOut
	# return:
	# 0 = no emergency out
	# string = travel type to use to emergency travel out
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		return 0
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pTravel == None or pPlayer.IsDocked():
		return 0
	if CheckBasicPlayerCanTravel(pTravel.GetTravelType()) == 1:
		return pTravel.GetTravelType()

	# ship can't travel using selected travel type. Try checking for other types...
	lTTs = App.g_kTravelManager.GetAllTTAvailableForShip(pPlayer)
	if len(lTTs) <= 0:
		return 0

	sOldType = pTravel.GetTravelType()
	oBestType = 0
	fBestSpeed = 0.0
	for sTravelType in lTTs:
		pTravel.__dict__['_Travel__travelType'] = sTravelType
		if CheckBasicPlayerCanTravel(sTravelType) == 1:
			fSpeed = pTravel.GetRealSpeed()
			fFactor = App.g_kSystemWrapper.GetRandomNumber(100)
			fChance = 5.0
			if oBestType == 0:
				fChance = 100.0
			if fSpeed > fBestSpeed:
				fChance = fChance + 32.5
			if pTravel.CanDropOut() == 1:
				fChance = fChance + 17.5
			if pTravel.CanChangeCourse() == 1:
				fChance = fChance + 22.5
			if pTravel.CanChangeSpeed() == 1:
				fChance = fChance + 17.5
			if fFactor <= fChance:
				fBestSpeed = fSpeed
				oBestType = sTravelType
	pTravel.__dict__['_Travel__travelType'] = sOldType
	return oBestType

def CheckBasicPlayerCanTravel(sTravelType):
	# we use this here because we can't let the Travel obj check for restrictions. We'll check the restrictions ourselves.
	debug(__name__ + ", CheckBasicPlayerCanTravel")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		return 0
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pTravel == None:
		return 0
	pFunc = App.g_kTravelManager.GetTravelTypeAttr(sTravelType, "CanTravel")
	oRet = pFunc(pTravel)
	if type(oRet) == type(1):
		return oRet
	return 0

def UpdateEmergencyOutButton():
	debug(__name__ + ", UpdateEmergencyOutButton")
	global pEmergencyOut
	pName = App.TGString()
	pEmergencyOut.GetName(pName)
	sName = pName.GetCString()
	oTravelType = CanEmergencyTravelOut()
	pRegion = GetClosestRegionToPlayer(oTravelType)
	if oTravelType == 0:
		if sName != "Emergency Travel Out":
			pEmergencyOut.SetName(App.TGString("Emergency Travel Out"))
		if pEmergencyOut.IsEnabled() == 1:
			pEmergencyOut.SetDisabled()
	elif pRegion == None:
		if pEmergencyOut.IsEnabled() == 1:
			pEmergencyOut.SetDisabled()
	else:
		sCorName = "Emergency "+oTravelType+" Out"
		if sName != sCorName:
			pEmergencyOut.SetName(App.TGString(sCorName))
		pPlayer = App.Game_GetCurrentPlayer()
		pTravel = App.g_kTravelManager.GetTravel(pPlayer)
		if pTravel != None and pTravel.IsTravelling() == 1:
			if pEmergencyOut.IsEnabled() == 1:
				pEmergencyOut.SetDisabled()
		elif pEmergencyOut.IsEnabled() == 0:
			pEmergencyOut.SetEnabled()


def GetClosestRegionToPlayer(oTravelType = None):
	debug(__name__ + ", GetClosestRegionToPlayer")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		return
	pPlayerRegion = pPlayer.GetContainingSet().GetRegion()
	if pPlayerRegion == None:
		return None
	if oTravelType == None:
		oTravelType = CanEmergencyTravelOut()
	if oTravelType == 0:
		return None
	pClosestReg = None
	fCloseDist = 200000.0
	for pRegion in App.g_kRegionManager.GetAllRegions():
		bNotRestricted = CheckForEmergencyOutRestriction(pPlayer, pRegion, oTravelType)
		if pRegion.GetName() != pPlayerRegion.GetName() and type(pRegion.GetLocation()) != type("") and bNotRestricted == 1:
			vWasLoc = pPlayerRegion.GetLocation()
			vGoLoc = pRegion.GetLocation()
			vDist = App.NiPoint2(vGoLoc.x - vWasLoc.x, vGoLoc.y - vWasLoc.y)
			fDist = vDist.Length()
			if fDist < fCloseDist and pRegion.BorderSet != None:
				sEmpire = pRegion.GetControllingEmpire()
				bWarOrRDF = int(GalaxyLIB.GetConfigValue("UseWarSim") == 1 or GalaxyLIB.GetConfigValue("GetRDFConfig").UseRDF == 1)
				if sEmpire == "Unknown" or sEmpire == "None" or bWarOrRDF == 0 or GalaxyLIB.IsShipEnemyOfRace(pPlayer, sEmpire) != 1:
					fCloseDist = fDist
					pClosestReg = pRegion
	return pClosestReg

def CheckForEmergencyOutRestriction(pShip, pDestRegion, sTravelType):
	debug(__name__ + ", CheckForEmergencyOutRestriction")
	pTravel = App.g_kTravelManager.GetTravel(pShip)
	iRF = App.g_kTravelManager.GetTravelTypeAttr(sTravelType, "iRestrictionFlag")
	if type(iRF) != type(1):
		return 0
	if not iRF in [0, 1, 2, 3]:
		return 0

	pRegion = pShip.GetContainingSet().GetRegion()
	ISA = [pRegion.GetOnlyByRestrictedMethods(), int(sTravelType in pRegion.GetRestrictedFor())]
	DSA = [pDestRegion.GetOnlyByRestrictedMethods(), int(sTravelType in pDestRegion.GetRestrictedFor())]
	
	if ISA == [1,0]:
		return 0
	elif DSA == [1,0]:
		return 0
	elif iRF == 0: #no restriction
		return 1
	elif iRF == 1: #can only be used between RSs  (when in a RS to travel to another RS)
		if ISA[1] == 1 and DSA[1] == 1:
			return 1
		else:
			return 0
	elif iRF == 2: #travel from anywhere to a RS, but can only return to the system where ship came from
		if DSA[1] == 1:
			return 1
		elif ISA[1] == 1 and DSA == [0,0]:
			#check if is the initial non-RS system
			if pTravel.dSysRestrictionF2.has_key(sTravelType) and pDestRegion.GetName() == pTravel.dSysRestrictionF2[sTravelType]:
				return 1
			else:
				return 0
		else:
			return 0