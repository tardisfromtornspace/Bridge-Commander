from bcdebug import debug
###############################################################################################################
#   StrategicCommandGUI.py                 by Fernando Aluani
############
# This script that contains the code that sets up and handles the Strategic Command window, and its sub components
###############################################################################################################
import App
import MissionLib
import Foundation
import string
import Galaxy
import GalacticWarSimulator
import Custom.QBautostart.Libs.Races
from GalaxyLIB import *
from Custom.GravityFX.GravityFXguilib import *

pGUICreator = None
eRefresh = None
ET_STRATEGIC_COMMAND = None
bIsOpened = 0
pBuyTimer = None
ET_BUY_TIMER = None
ET_SELL_TIMER = None
ET_DEVELOP_TIMER = None
ET_MADC_TIMER = None
ET_MESSAGE_BOX = None
#####################################################################
def CreateSCGUI():
	debug(__name__ + ", CreateSCGUI")
	global pGUICreator, ET_STRATEGIC_COMMAND, ET_BUY_TIMER, ET_SELL_TIMER, ET_DEVELOP_TIMER, ET_MADC_TIMER, ET_MESSAGE_BOX
	if GalacticWarSimulator.WarSimulator.IsInitialized() == 0:
		return
	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet("bridge")
	pXO = App.CharacterClass_GetObject(pBridge, "XO")
	if pXO == None:
		return
	pXOMenu = pXO.GetMenu()
	if pXOMenu == None:
		return

	if pGUICreator == None:
		pGUICreator = GUICreator()

	ET_STRATEGIC_COMMAND = GetNextEventType()
	ET_BUY_TIMER = GetNextEventType()
	ET_SELL_TIMER = GetNextEventType()
	ET_DEVELOP_TIMER = GetNextEventType()
	ET_MADC_TIMER = GetNextEventType()

	pButton = pGUICreator.ButtonCreator.CreateButton("Strategic Command", ET_STRATEGIC_COMMAND, None, 1, pXOMenu)
	#pXOMenu.DeleteChild(pButton)
	#pXOMenu.PrependChild(pButton)
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_STRATEGIC_COMMAND, pMission, __name__ + ".SCOpenClose")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(pGUICreator.GetGenericOKEventType(), pMission, __name__ + ".MsgBoxOK")

	#pXO.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".SCClose")

	import SaveGameGUI
	SaveGameGUI.CreateSaveGameGUI()


def SCOpenClose(pObject = None, pEvent = None):
	debug(__name__ + ", SCOpenClose")
	global bIsOpened, iSelectedType
	pSC = pGUICreator.GetElement("Strategic Command")
	if not pSC:
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pGUICreator.SetInfoForName("Strategic Command", 0.45, 0.0, 0.55, 0.15, 0)
		pSC = pGUICreator.CreateWindow("Strategic Command", pTCW)
		pSC.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSC.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		pGUICreator.SetInfoForName("Strategic Data", 0.6, 0.15, 0.4, 0.5, 0)
		pSD = pGUICreator.CreateWindow("Strategic Data", pTCW)
		pSD.SetUseScrolling(1)
		pSD.SetScrollViewHeight(25.0)
		pSD.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSD.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		pGUICreator.SetInfoForName("Sub-Actions", 0.45, 0.15, 0.15, 0.5, 0)
		pSD = pGUICreator.CreateWindow("Sub-Actions", pTCW)
		pSD.SetUseScrolling(1)
		pSD.SetScrollViewHeight(25.0)
		pSD.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSD.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		CreateSCStaticContents(pSC)
	if pSC.IsVisible():
		pGUICreator.CloseElement("Strategic Command")
		pGUICreator.CloseElement("Strategic Data")
		pGUICreator.CloseElement("Sub-Actions")
		bIsOpened = 0
	else:
		pGUICreator.ShowElement("Strategic Command")
		pGUICreator.ShowElement("Strategic Data")
		pGUICreator.ShowElement("Sub-Actions")
		bIsOpened = 1
		UpdateSDPane(iSelectedType)
	
		
def SCClose(pObject = None, pEvent = None):
	debug(__name__ + ", SCClose")
	global bIsOpened
	if pGUICreator != None:
		pGUICreator.CloseElement("Strategic Command")
		pGUICreator.CloseElement("Strategic Data")
		pGUICreator.CloseElement("Sub-Actions")
	bIsOpened = 0
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def CreateSCStaticContents(pSC):
	debug(__name__ + ", CreateSCStaticContents")
	global eRefresh
	# Create static GUI contents.
	ButtonDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pGUICreator.ButtonCreator.CreateButton("News Line", None, __name__ + ".CommandClick", 1, pSC, ButtonDict, ButtonDict)

	ButtonDict = {'X': 0.18, 'Y': 0.0, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pGUICreator.ButtonCreator.CreateButton("War/Race Stats", None, __name__ + ".CommandClick", 2, pSC, ButtonDict, ButtonDict)

	ButtonDict = {'X': 0.36, 'Y': 0.0, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pGUICreator.ButtonCreator.CreateButton("Database", None, __name__ + ".CommandClick", 3, pSC, ButtonDict, ButtonDict)

	ButtonDict = {'X': 0.0, 'Y': 0.05, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pButton = pGUICreator.ButtonCreator.CreateButton("Military Command", None, __name__ + ".CommandClick", 4, pSC, ButtonDict, ButtonDict)
	bPlayerHasRaceCommand = GetConfigValue("GetWarSimConfig").PlayerHasRaceCommand
	if bPlayerHasRaceCommand == 0:
		pButton.SetDisabled()

	ButtonDict = {'X': 0.18, 'Y': 0.05, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pButton2 = pGUICreator.ButtonCreator.CreateButton("System Development", None, __name__ + ".CommandClick", 5, pSC, ButtonDict, ButtonDict)
	pButton2.SetDisabled()

	ButtonDict = {'X': 0.36, 'Y': 0.05, 'WIDTH': 0.16, 'HEIGTH': 0.04}
	pGUICreator.ButtonCreator.CreateButton("Close", None, __name__ + ".SCClose", 1, pSC, ButtonDict, ButtonDict)

	dTICoords = {'X': 0.0, 'Y': 0.4}
	AddTextInput("Type here", 0.2, dTICoords)
	CreatePlaceStarbaseButtons()
	CreateDevelopmentButton()

	eRefresh = RefreshEventHandler(UpdateGUI, 1.0)
	return

# master function to update the whole GUI
def UpdateGUI(pObject = None, pEvent = None):
	debug(__name__ + ", UpdateGUI")
	global iSelectedType, iSelectedSubType
	if pGUICreator == None:
		return
	pPlayer = App.Game_GetCurrentPlayer()
	pRaceObj = GetRaceClassObj(GetShipRace(pPlayer))
	pSet = pPlayer.GetContainingSet()
	pRegion = None
	if pSet != None:
		pRegion = pSet.GetRegion()
	bPlayerHasRaceCommand = GetConfigValue("GetWarSimConfig").PlayerHasRaceCommand
	if pRaceObj != None and pRegion != None and bPlayerHasRaceCommand == 1:
		pSDButton = pGUICreator.ButtonCreator.GetButtonByName("System Development")
		if pRegion.GetControllingEmpire() == pRaceObj.GetRaceName() and pSDButton.IsEnabled() == 0:
			pSDButton.SetEnabled()
		elif pRegion.GetControllingEmpire() != pRaceObj.GetRaceName() and pSDButton.IsEnabled() == 1:
			if iSelectedType == 4 or iSelectedType == 5:
				iSelectedType = 1
				iSelectedSubType = 1
				UpdateSDPane(1)
			pSDButton.SetDisabled()

	if iSelectedType == 3:
		# don't keep updating the GUI incase the user is seeing the ships database, since it's data doesn't change with time, and the process
		# to keep needlessly updating it would be resource consuming...
		# the GUI will be properly updated in case the user chooses another ship class.
		return 
	UpdateSDData(iSelectedType, iSelectedSubType)


# Command Button INT listing:
# News Line                  - 1
# War Stats / Race Rankings  - 2
# Database                   - 3
# Military Command           - 4
# System Development         - 5
iSelectedType = 1
def CommandClick(pObject, pEvent):
	debug(__name__ + ", CommandClick")
	global iSelectedType 
	try:
		iInt = pEvent.GetInt()
	except:
		return
	iSelectedType = iInt
	UpdateSDPane(iInt)

# sub-actions button handling
iSelectedSubType = 1
def SubActionClick(pObject, pEvent):
	debug(__name__ + ", SubActionClick")
	global iSelectedType, iSelectedSubType 
	try:
		iInt = pEvent.GetInt()
	except:
		return
	iSelectedSubType = iInt
	UpdateSDData(iSelectedType, iInt)

# Create dynamic GUI contents.
dDynamicSAConnection = {}
def UpdateSDPane(iType):
	debug(__name__ + ", UpdateSDPane")
	global bIsOpened, iSelectedSubType, dDynamicSAConnection
	if bIsOpened == 0 or pGUICreator == None:
		return

	pSD = pGUICreator.GetElement("Strategic Data")
	pSA = pGUICreator.GetElement("Sub-Actions")
	pSA.KillChildren()

	iSelectedSubType = 1
	if iType == 1:   #News Line
		dDynamicSAConnection = {}
		AddSubActionButton("All Events", 0.0, 1)
		dDynamicSAConnection[1] = "ALL"
		lNewsTypes = GalacticWarSimulator.WarSimulator.GetNewsTypes()
		if not "Ship" in lNewsTypes:
			lNewsTypes.append("Ship")
		if not "Region" in lNewsTypes:
			lNewsTypes.append("Region")
		if not "Travel" in lNewsTypes:
			lNewsTypes.append("Travel")
		iIndex = 1
		fY = 0.0
		for sNewsType in lNewsTypes:
			iIndex = iIndex + 1
			fY = fY + 0.03 + 0.02  # +button heigth + offset
			AddSubActionButton("Only "+sNewsType+" Events", fY, iIndex)
			dDynamicSAConnection[iIndex] = sNewsType
		UpdateSDData(iType, 1)

	elif iType == 2:  #War Stats / Race Rankings
		dDynamicSAConnection = {}
		AddSubActionButton("War Stats", 0.0, 1)
		AddSubActionButton("Race Rankings", 0.037, 2)
		iIndex = 2
		fY = 0.037
		for pRaceObj in Custom.QBautostart.Libs.Races.Races.values():
			if pRaceObj.GetRaceName() != "GodShips":
				iIndex = iIndex + 1
				fY = fY + 0.03 + 0.007  # + button heigth + offset
				AddSubActionButton(pRaceObj.GetRaceName(), fY, iIndex)
				dDynamicSAConnection[iIndex] = pRaceObj
		UpdateSDData(iType, 1)

	elif iType == 3:  #Database
		dDynamicSAConnection = {}
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			pRaceObj = GetRaceClassObj( GetShipRace(pPlayer) )
			if pRaceObj != None:
				iIndex = 0
				fY = 0.0
				for sShipClass in pRaceObj.GetAllShipClasses():
					pShipDef = GetShipDefByScript(sShipClass)
					if pShipDef != None:
						iIndex = iIndex + 1
						AddSubActionButton(sShipClass, fY, iIndex)
						fY = fY + 0.03 + 0.007  # + button heigth + offset
						dDynamicSAConnection[iIndex] = pShipDef
		UpdateSDData(iType, 0)

	elif iType == 4:  #Military Command
		dDynamicSAConnection = {}
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			pPlayerRace = GetRaceClassObj( GetShipRace(pPlayer) )
			if pPlayerRace != None:
				AddSubActionButton("General Options", 0.0, 1)
				iIndex = 1
				fY = 0.0
				for pRaceObj in Custom.QBautostart.Libs.Races.Races.values():
					if pRaceObj.GetRaceName() != "GodShips" and pRaceObj.GetRaceName() != pPlayerRace.GetRaceName():
						iIndex = iIndex + 1
						fY = fY + 0.03 + 0.007  # + button heigth + offset
						AddSubActionButton(pRaceObj.GetRaceName(), fY, iIndex)
						dDynamicSAConnection[iIndex] = pRaceObj
		UpdateSDData(iType, 0)

	elif iType == 5:  #System Development
		AddSubActionButton("Bases", 0.0, 1)
		AddSubActionButton("Infrastructure", 0.05, 2)
		AddSubActionButton("Technologic Assets", 0.1, 3)
		AddSubActionButton("Military Assets", 0.15, 4)
		UpdateSDData(iType, 1)

	pSD.SetUseScrolling(1)
	pSD.SetScrollViewHeight(25.0)
	pSA.SetUseScrolling(1)
	pSA.SetScrollViewHeight(25.0)

# this one gonna be big... 
def UpdateSDData(iType, iSubType):
	debug(__name__ + ", UpdateSDData")
	global bIsOpened, dDynamicSAConnection, pTI
	if bIsOpened == 0 or pGUICreator == None:
		return

	pSD = pGUICreator.GetElement("Strategic Data")
	lStrList = []

	if iType == 1:   #News Line
		HandleMCButtons(0)
		SetTIVisible(0)
		DeletePlaceStarbaseButtons()
		DeleteDevelopmentButton()
		sNewsType = dDynamicSAConnection[iSubType]
		if sNewsType == "ALL":
			lStrList = GalacticWarSimulator.WarSimulator.GetNewsList()
		else:
			lStrList = GalacticWarSimulator.WarSimulator.GetNewsList(sNewsType)
		if len(lStrList) <= 0:
			lStrList.append("No news items in selected category.")

	elif iType == 2:  #War Stats / Race Rankings
		HandleMCButtons(0)
		SetTIVisible(0)
		DeletePlaceStarbaseButtons()
		DeleteDevelopmentButton()
		if iSubType == 1: # war stats
			# Yup, this easy...
			lStrList = GalacticWarSimulator.WarSimulator.GetStatsList()
			# Ok ok... The WarSim and a couple other things do all the work...
			# And these useless comments where just to put a couple more lines inside this IF. =)
		elif iSubType == 2: #rankings
			dRacePoints = {}
			for pRaceObj in Custom.QBautostart.Libs.Races.Races.values():
				if pRaceObj.GetRaceName() != "GodShips":
					fRacePoints = GetRacePoints(pRaceObj)
					if dRacePoints.has_key(fRacePoints):
						if type(dRacePoints[fRacePoints]) == type([]):
							dRacePoints[fRacePoints].append(pRaceObj)
						else:
							pFirstRace = dRacePoints[fRacePoints]
							dRacePoints[fRacePoints] = [pFirstRace, pRaceObj]
					else:
						dRacePoints[fRacePoints] = pRaceObj
			lPoints = dRacePoints.keys()
			lPoints.sort()
			lPoints.reverse()
			for fPoints in lPoints:
				if type(dRacePoints[fPoints]) == type([]):
					sStr = ""
					for pRaceObj in dRacePoints[fPoints]:
						sStr = sStr + " > "+str(lPoints.index(fPoints)+1)+" Place: "+pRaceObj.GetRaceName()+"  (Points: "+str(fPoints)+")\n"
					sStr = sStr[0:len(sStr)-2]
					lStrList.append( sStr )
				else:
					lStrList.append( " > "+str(lPoints.index(fPoints)+1)+" Place: "+dRacePoints[fPoints].GetRaceName()+"  (Points: "+str(fPoints)+")"  )
				lStrList.append( "" )

		elif iSubType > 2:  #specific race
			pRaceObj = dDynamicSAConnection[iSubType]
			lStrList.append( pRaceObj.GetRaceName()+" Status:" )
			lStrList.append( "" )
			lStrList.append( "> Total Ranking Points: "+str(GetRacePoints(pRaceObj)) )
			lStrList.append( "" )
			lStrList.append( "> Total Funds: "+str(pRaceObj.GetTotalFunds()))
			lStrList.append( "> Total Economic Production: "+str(pRaceObj.GetTotalEconomyProduction()))
			lStrList.append( "> Total Defence Value: "+str(pRaceObj.GetTotalDefenceValue()))
			lStrList.append( "> Total Strategic Value: "+str(pRaceObj.GetTotalStrategicValue()))
			lStrList.append( "" )
			lAllies = GetAlliedRacesOf(pRaceObj.GetRaceName())
			sAllies = "NONE"
			if len(lAllies) > 0:
				sAllies = ""
				for sAlly in lAllies:
					sAllies = sAllies + sAlly + ", "
				sAllies = sAllies[0:len(sAllies)-2] + "."
			lStrList.append( "> Allied Races:   "+sAllies )
			lStrList.append( "" )
			if pRaceObj.GetIsEnemyToAll() == 1:
				sEnemies = "ALL OTHERS"
			else:
				lEnemies = GetEnemyRacesOf(pRaceObj.GetRaceName())
				sEnemies = "NONE"
				if len(lEnemies) > 0:
					sEnemies = ""
					for sEnemy in lEnemies:
						sEnemies = sEnemies + sEnemy + ", "
					sEnemies = sEnemies[0:len(sEnemies)-2] + "."
			lStrList.append( "> Enemy Races:   "+sEnemies )
			lStrList.append( "" )
			lRegions = pRaceObj.GetSystems()
			if len(lRegions) > 0:
				lStrList.append( "> Systems:" )
				for pRegion in lRegions:
					lStrList.append( "    - "+pRegion.GetName()+" (Importance: "+str(GetRegionImportance(pRegion))+")" )
			else:
				lStrList.append( "> Systems:   NONE" )
			lStrList.append( "" )
			if len(pRaceObj.lShipNames) >= 1:
				lStrList.append( "> Commissioned Ships:" )
				for sShipName in pRaceObj.lShipNames:
					if pRaceObj.dWSShips.has_key(sShipName):
						sStatus = "ACTIVE"
					else:
						sStatus = "DESTROYED"
					pShip = MissionLib.GetShip(sShipName, None, 1)
					sFleetStat = "Not in a fleet"
					if pShip != None:
						if IsStation(pShip) == 1:
							sFleetStat = "Station"
						else:
							pFleet = GalacticWarSimulator.FleetManager.GetFleetOfShip(pShip)
							if pFleet != None:
								sFleetStat = "In "+pFleet.GetName()
					# shipname (fleetname(or station), active/destroyed)
					lStrList.append( "    - "+sShipName+" ("+sFleetStat+", "+sStatus+")" )
			else:
				lStrList.append( "> Commissioned Ships:   NONE" )

	elif iType == 3:  #Database
		HandleMCButtons(0)
		SetTIVisible(0)
		DeletePlaceStarbaseButtons()
		DeleteDevelopmentButton()
		lStrList.append( "Ship Class Information Database" )
		lStrList.append( "" )
		if iSubType == 0:
			lStrList.append( "Choose a ship class..." )
		elif iSubType >= 1:
			pShipDef = dDynamicSAConnection[iSubType]
			sShipClass = pShipDef.shipFile
			print "SCGUI  (SDDATA): ", iSubType, sShipClass, pShipDef
			lStrList.append( "Ship Class:  "+sShipClass )
			lStrList.append( "" )
			sRace = str(GetShipDefRace(pShipDef))
			lStrList.append( "From Race:  "+sRace )
			lStrList.append( "" )
			lStrList.append( "Total Fund Cost:  "+str(GalacticWarSimulator.WarSimulator.GetShipClassCost(sShipClass)) )
			lStrList.append( "" )
			if hasattr(pShipDef, "fCrew"):
				if pShipDef.fCrew == "Off":
					sShipCrew = sMaxShipCrew = "N/A"
				else:
					sShipCrew = str( int(pShipDef.fCrew) )
					sMaxShipCrew = str( int(pShipDef.fCrew * 1.5) )
			else:
				sShipCrew = sMaxShipCrew = "unable to detect..."
			lStrList.append( "Normal Crew Count:  "+sShipCrew )
			lStrList.append( "Maximum Crew Count:  "+sMaxShipCrew )
			lStrList.append( "" )
			pShipsDatabase = App.g_kLocalizationManager.Load("data/TGL/Ships.tgl")
			if pShipsDatabase.HasString(pShipDef.abbrev + " Description"):
				lStrList.append( str(pShipsDatabase.GetString(pShipDef.abbrev + " Description").GetCString()))
			else:
				sDesc = str(pShipDef.desc)
				if sDesc == "":
					sDesc = "No description available...."
				lStrList.append( sDesc )
			App.g_kLocalizationManager.Unload(pShipsDatabase)
			lStrList.append( "" )
			pRaceObj = GetRaceClassObj(sRace)
			sESLine = "NONE"
			if pRaceObj != None:
				lEscorts = pRaceObj.GetEscorts(sShipClass)
				if lEscorts != None:
					sESLine = ""
					for sEscort in lEscorts:
						sESLine = sESLine + sEscort + ", "
					sESLine = sESLine[0:len(sESLine)-2] + "."
			lStrList.append( "Escorts (Ship Classes):  "+sESLine )
			lStrList.append( "" )
			pGodRace = GetRaceClassObj("GodShips")
			sIsGod = "No"
			if pGodRace != None:
				if sShipClass in pGodRace.myShips:
					sIsGod = "Yes"
			lStrList.append( "Is Classified as a God Ship:  "+sIsGod )
			lStrList.append( "" )
			lStrList.append( "Subsystem Listing:" )
			# now try to get subsystem data from this ship class, kinda like how we do in the GetShipFundCost function.
			# however do it shorter here, and don't mind much about errors :P
			# the GetShipFundCost, when used with this ship class, will care about them.
			Galaxy.Logger.LogString("SCGUI: Getting Ship Subsystems Info")
			try:
				pShipScript = __import__("ships." + sShipClass)
				print "SCGUI  ship script:  ", pShipScript
				Galaxy.Logger.LogString("SCGUI: MARK 1")
				sHardpointFile = pShipScript.GetShipStats()["HardpointFile"]
				print "SCGUI  hardpoint file:  ", sHardpointFile
				Galaxy.Logger.LogString("SCGUI: MARK 2")
				pHardpoint = __import__("ships.Hardpoints." + sHardpointFile)
				print "SCGUI  HP script:  ", pHardpoint
				Galaxy.Logger.LogString("SCGUI: MARK 3")

				pPropertySet = App.TGModelPropertySet()
				App.g_kModelPropertyManager.ClearLocalTemplates()
				reload(pHardpoint)
				pHardpoint.LoadPropertySet(pPropertySet)

				pPropertyList = pPropertySet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
				pPropertyList.TGBeginIteration()

				for i in range(pPropertyList.TGGetNumItems()):
					pShipProperty = App.SubsystemProperty_Cast(pPropertyList.TGGetNext().GetOriginalTemplate())
					if pShipProperty != None:
						Galaxy.Logger.LogString("SCGUI: MARK 7")
						sLine = pShipProperty.GetName().GetCString()
						Galaxy.Logger.LogString("SCGUI: MARK 7.A - "+sLine)
						sSubClass = ""
						lExtras = []
						fMaxHP = pShipProperty.GetMaxCondition()
						Galaxy.Logger.LogString("SCGUI: MARK 7.B")
						bIsPrimary = pShipProperty.IsPrimary()
						Galaxy.Logger.LogString("SCGUI: MARK 7.C")		
						lExtras.append("Structural Integrity:  "+str(fMaxHP))
						Galaxy.Logger.LogString("SCGUI: MARK 7.D")
						if App.HullProperty_Cast(pShipProperty) != None:
							sSubClass = "Hull Subsystem"
						elif App.PowerProperty_Cast(pShipProperty) != None:
							sSubClass = "Power Generator Subsystem"
							pPowerProp = App.PowerProperty_Cast(pShipProperty)
							lExtras.append("Total Power Output:  "+str(pPowerProp.GetPowerOutput()))
							lExtras.append("Main Battery Charge:  "+str(pPowerProp.GetMainBatteryLimit()))
							lExtras.append("Backup Battery Charge:  "+str(pPowerProp.GetBackupBatteryLimit()))
						elif App.CloakingSubsystemProperty_Cast(pShipProperty) != None:
							sSubClass = "Cloaking System"
						elif App.PoweredSubsystemProperty_Cast(pShipProperty) != None:
							pPoweredSys = App.PoweredSubsystemProperty_Cast(pShipProperty)
							if App.ImpulseEngineProperty_Cast(pPoweredSys) != None:
								pImpSys = App.ImpulseEngineProperty_Cast(pPoweredSys)
								sSubClass = "Impulse Engine System"
								lExtras.append("Max Acceleration:  "+str(pImpSys.GetMaxAccel()))
								lExtras.append("Max Speed:  "+str(pImpSys.GetMaxSpeed()))
								lExtras.append("Max Angular Acceleration:  "+str(pImpSys.GetMaxAngularAccel()))
								lExtras.append("Max Angular Speed:  "+str(pImpSys.GetMaxAngularVelocity()))
							elif App.WarpEngineProperty_Cast(pPoweredSys) != None:
								sSubClass = "Warp Engine System"
								if hasattr(pShipDef, "fMaxWarp"):
									fMaxWarp = float(str(pShipDef.fMaxWarp)[0:3+1])
									if fMaxWarp < 1.0:	fMaxWarp = 1.0
									if fMaxWarp > 9.99:	fMaxWarp = 9.99
									lExtras.append("Max Warp Speed:  "+str(fMaxWarp) )
								else:
									lExtras.append("Max Warp Speed:  9.99" )
								if hasattr(pShipDef, "fCruiseWarp"):
									fCruiseWarp = float(str(pShipDef.fCruiseWarp)[0:3+1])
									if fCruiseWarp < 1.0:	fCruiseWarp = 1.0
									if fCruiseWarp > 9.99:	fCruiseWarp = 9.99
									lExtras.append("Cruise Warp Speed:  "+str(fCruiseWarp) )
								else:
									lExtras.append("Cruise Warp Speed:  9.99" )
							elif App.RepairSubsystemProperty_Cast(pPoweredSys) != None:
								sSubClass = "Repair System"
								pRepairSys = App.RepairSubsystemProperty_Cast(pPoweredSys)
								lExtras.append("Repair Teams:  "+str(pRepairSys.GetNumRepairTeams()))
							elif App.SensorProperty_Cast(pPoweredSys) != None:
								sSubClass = "Sensor System"
								pSensorSys = App.SensorProperty_Cast(pPoweredSys)
								lExtras.append("Range:  "+str(pSensorSys.GetBaseSensorRange()))
								lExtras.append("Probe Count:  "+str(pSensorSys.GetMaxProbes()))
							elif App.ShieldProperty_Cast(pPoweredSys) != None:
								sSubClass = "Shield Generator System"
								pShieldSys = App.ShieldProperty_Cast(pPoweredSys)
								FRONT_MS = pShieldSys.GetMaxShields(pShieldSys.FRONT_SHIELDS)
								REAR_MS = pShieldSys.GetMaxShields(pShieldSys.REAR_SHIELDS)
								TOP_MS = pShieldSys.GetMaxShields(pShieldSys.TOP_SHIELDS)
								BOTTOM_MS = pShieldSys.GetMaxShields(pShieldSys.BOTTOM_SHIELDS)
								LEFT_MS = pShieldSys.GetMaxShields(pShieldSys.LEFT_SHIELDS)
								RIGHT_MS = pShieldSys.GetMaxShields(pShieldSys.RIGHT_SHIELDS)
								FRONT_SC = pShieldSys.GetShieldChargePerSecond(pShieldSys.FRONT_SHIELDS)
								REAR_SC = pShieldSys.GetShieldChargePerSecond(pShieldSys.REAR_SHIELDS)
								TOP_SC = pShieldSys.GetShieldChargePerSecond(pShieldSys.TOP_SHIELDS)
								BOTTOM_SC = pShieldSys.GetShieldChargePerSecond(pShieldSys.BOTTOM_SHIELDS)
								LEFT_SC = pShieldSys.GetShieldChargePerSecond(pShieldSys.LEFT_SHIELDS)
								RIGHT_SC = pShieldSys.GetShieldChargePerSecond(pShieldSys.RIGHT_SHIELDS)
								lExtras.append("Forward Vector Power (Recharge Rate):  "+str(FRONT_MS)+" ("+str(FRONT_SC)+")")
								lExtras.append("Aft Vector Power (Recharge Rate):  "+str(REAR_MS)+" ("+str(REAR_SC)+")")
								lExtras.append("Left Vector Power (Recharge Rate):  "+str(LEFT_MS)+" ("+str(LEFT_SC)+")")
								lExtras.append("Right Vector Power (Recharge Rate):  "+str(RIGHT_MS)+" ("+str(RIGHT_SC)+")")
								lExtras.append("Top Vector Power (Recharge Rate):  "+str(TOP_MS)+" ("+str(TOP_SC)+")")
								lExtras.append("Bottom Vector Power (Recharge Rate):  "+str(BOTTOM_MS)+" ("+str(BOTTOM_SC)+")")
							elif App.WeaponSystemProperty_Cast(pPoweredSys) != None:
								pWeaponSys = App.WeaponSystemProperty_Cast(pPoweredSys)
								if pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_TRACTOR:
									sSubClass = "Tractor Beam System"
								elif pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_TORPEDO:
									sSubClass = "Torpedo System"
									pTorpSys = App.TorpedoSystemProperty_Cast(pPoweredSys)
									if pTorpSys != None:
										for index in range(pTorpSys.GetNumAmmoTypes()):
											sTorpScript = pTorpSys.GetTorpedoScript(index)
											iTorpAmmo = pTorpSys.GetMaxTorpedoes(index)
											try:
												pTorp = __import__(sTorpScript)
												fDmg = pTorp.GetDamage()
											except:
												fDmg = "Unknown"
											sTorpName = string.split(sTorpScript, ".")[-1]
											lExtras.append("Ammo:  "+str(iTorpAmmo)+" rounds of "+str(sTorpName)+" (Damage: "+str(fDmg)+")")
								elif pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_PULSE:
									sSubClass = "Pulse Weapon System"
								elif pWeaponSys.GetWeaponSystemType() == pWeaponSys.WST_PHASER:
									sSubClass = "Beam Weapon System"
						elif App.EngineProperty_Cast(pShipProperty) != None:
							pEngine = App.EngineProperty_Cast(pShipProperty)
							if pEngine.GetEngineType() == pEngine.EP_WARP:
								sSubClass = "Warp Engine"
							else:
								sSubClass = "Impulse Engine"
						elif App.WeaponProperty_Cast(pShipProperty) != None:
							pWeapon = App.WeaponProperty_Cast(pShipProperty)
							if App.TorpedoTubeProperty_Cast(pWeapon) != None:
								sSubClass = "Torpedo Tube"
								pTube = App.TorpedoTubeProperty_Cast(pWeapon)
								fImmediateDelay = pTube.GetImmediateDelay()
								fMaxReady = pTube.GetMaxReady()
								if fMaxReady != 0.0:
									secondstofireonetorp = ((((fMaxReady * fImmediateDelay) - fImmediateDelay) + pTube.GetReloadDelay()) / fMaxReady)
								else:
									secondstofireonetorp = 0
								if secondstofireonetorp != 0.0:
									torpsfiredpersecond = 1.0 / secondstofireonetorp
								else:
									torpsfiredpersecond = 0.1
								lExtras.append("Shots Per Second:  "+str(torpsfiredpersecond))
							elif App.TractorBeamProperty_Cast(pWeapon) != None:
								pTractor = App.TractorBeamProperty_Cast(pWeapon)
								sSubClass = "Tractor Beam Projector"
							elif App.PulseWeaponProperty_Cast(pWeapon) != None:
								sSubClass = "Pulse Weapon Cannon"
								pPulseWeapon = App.PulseWeaponProperty_Cast(pWeapon)
								try:
									pPulse = __import__(pPulseWeapon.GetModuleName())
									fDmg = pPulse.GetDamage()
								except:
									fDmg = "Unknown"
								fMaxCharge = pPulseWeapon.GetMaxCharge()
								if pPulseWeapon.GetNormalDischargeRate() != 0.0 and pPulseWeapon.GetMinFiringCharge() != 0.0:
									ShotsFactor = ((fMaxCharge / pPulseWeapon.GetNormalDischargeRate()) / pPulseWeapon.GetMinFiringCharge())
								else:
									ShotsFactor = 0.0
								if ShotsFactor != 0.0 and pPulseWeapon.GetRechargeRate() != 0.0:
									secsforoneshot = ( ((ShotsFactor*pPulseWeapon.GetCooldownTime())+(fMaxCharge/pPulseWeapon.GetRechargeRate()))/ShotsFactor )
								else:
									secsforoneshot = 0.0
								if secsforoneshot != 0.0:
									shotspersec = 1.0/ secsforoneshot
								else:
									shotspersec = 0.01
								lExtras.append("Shots Per Second:  "+str(shotspersec))
								lExtras.append("Pulse Damage:  "+str(fDmg))
							elif App.PhaserProperty_Cast(pWeapon) != None:
								sSubClass = "Beam Weapon Array"
								pBeam = App.PhaserProperty_Cast(pWeapon)
								lExtras.append("Damage Output:  "+str(pBeam.GetMaxDamage()))
								lExtras.append("Range:  "+str(pBeam.GetMaxDamageDistance()))
						if sLine != "" and sSubClass != "":
							lStrList.append( "" )
							lStrList.append( "   >>>"+str(sLine)+" ("+str(sSubClass)+")" )
							if len(lExtras) > 0:
								for sExtra in lExtras:
									lStrList.append( "     -"+str(sExtra) )
				# finish iterating...
				pPropertyList.TGDoneIterating()
				pPropertyList.TGDestroy()
				Galaxy.Logger.LogString("SCGUI: MARK  8")
			except:
				lStrList.append( "  >->-> WARNING! DATABASE ERROR <-<-<" )
				lStrList.append( "  >-> CANT ACQUIRE SHIP CLASS SUBSYSTEM DATA <-<" )
				Galaxy.LogError("SCGUI: Getting Ship Subsystems Info")
			lStrList.append( "" )
			lStrList.append( "" )
			# now check for ship based FoundationTech techs this ship has.
			if hasattr(pShipDef, "dTechs") == 1:
				lStrList.append( "Advanced Technological Systems:" )
				for sTechName in pShipDef.dTechs.keys():
					# just list some known techs to add their values as another piece of info.
					# all other techs will be listed generically.
					if sTechName == "Ablative Armour":
						oAblative = pShipDef.dTechs[sTechName]
						if type(oAblative) == type([]):
							oAblative = oAblative[0]
						lStrList.append( "   -"+sTechName+" (Integrity: "+str(oAblative)+")" )
					elif sTechName == "Regenerative Shields":
						lStrList.append( "   -"+sTechName+" (Regeneration Factor: "+str(pShipDef.dTechs[sTechName])+")" )
					elif sTechName == "Multivectral Shields" or sTechName == "Reflector Shields":
						lStrList.append( "   -"+sTechName+" (Efficiency: "+str(pShipDef.dTechs[sTechName])+"%)" )
					elif sTechName == "Fed Ablative Armor":
						oFedArmor = pShipDef.dTechs[sTechName]
						lPlateList = oFedArmor['Plates']
						lStrList.append( "   -"+sTechName+" (Number of Plates: "+str(len(lPlateList))+")" )
					elif sTechName == "AdvancedHull":
						oAdvHull = pShipDef.dTechs[sTechName]
						sNames = ""
						for sSubsystem in oAdvHull.keys():
							sNames = sNames + sSubsystem + ", "
						sNames = sNames[0:len(sNames)-2]
						lStrList.append( "   -"+sTechName+" (Integrated Systems: "+str(sNames)+")" )
					elif sTechName == "AutoTargeting":
						oAutoTarget = pShipDef.dTechs[sTechName]
						sLine = ""
						for sWeaponType in oAutoTarget.keys():	
							if sWeaponType in ["Pulse", "Phaser", "Torpedo"]:
								iMaxSecTargets = oAutoTarget[sWeaponType]
								sLine = sLine + str(iMaxSecTargets) + " secondary " + sWeaponType + " targets. "
						lStrList.append( "   -"+sTechName+" (Capabilities: "+str(sLine)+")" )
					else:
						lStrList.append( "   -"+sTechName)
			else:
				lStrList.append( "Advanced Technological Systems:   NONE" )

	elif iType == 4:  #Military Command
		DeletePlaceStarbaseButtons()
		DeleteDevelopmentButton()
		if iSubType == 0:  # nothing selected
			HandleMCButtons(0)
			SetTIVisible(0)
			lStrList.append( "Military Command" )
			lStrList.append( "" )
			lStrList.append( "> Select a Command Order sub-action." )
		if iSubType == 1: #general options
			lStrList.append( "Military Command - General Options and Instructions" )
			lStrList.append( "" )
			lStrList.append( ">Alliances and Diplomatic Relations:" )
			lStrList.append( " -Diplomatic Alliance (Peace Treaty): with this kind of treaty, 2 races will consider each other as neutral." )
			lStrList.append( " -Military Alliance (War Treaty, Prerequisite: Peace Treaty): Races allied under a war treaty will merge military forces to defend allied systems and attack enemies." )
			lStrList.append( " -Declare War: this will promptly cut off any treaties with the race, and both races will consider each other an enemy." )
			lStrList.append( " -Chance of the other race accepting a treaty will depend on the peace value of both races, and their rank, amongst other things." )
			lStrList.append( "" )
			lStrList.append( ">Attack Orders:" )
			lStrList.append( " -Size and force of attack fleets will be based on the target system importance." )
			lStrList.append( " -Selecting the checkbox \'Player Leads Attack\' will make that when the user enters an enemy system, an allied attack fleet will follow him in." )
			lStrList.append( "" )
			lStrList.append( "Select a race in the sub-actions menu, and select appropriate action." )
			SetTIVisible(0)
			HandleMCButtons(1)
		elif iSubType > 1:  #specific race
			pRaceObj = dDynamicSAConnection[iSubType]
			pPlayer = App.Game_GetCurrentPlayer()
			pPlayerRace = GetRaceClassObj( GetShipRace(pPlayer) )
			lStrList.append( "Military Command - Commands concerning race "+pRaceObj.GetRaceName() )
			lStrList.append( "" )
			lStrList.append( ">Alliances and Diplomatic Relations:" )
			# check race alliance status
			sAllianceStatus = "Peace Treaty (Neutral)"
			iTreatyIndex = 2
			if AreRacesEnemies(pPlayerRace.GetRaceName(), pRaceObj.GetRaceName()) == 1:
				sAllianceStatus = "Declared War (Hostile)"
				iTreatyIndex = 1
			elif AreRacesAllied(pPlayerRace.GetRaceName(), pRaceObj.GetRaceName()) == 1:
				sAllianceStatus = "War Treaty (Allied)"
				iTreatyIndex = 0
			fChance = 0.0
			if iTreatyIndex > 0:
				fChance = (pPlayerRace.GetPeaceValue() + pRaceObj.GetPeaceValue()) * 10.0    #max 20
				fChance = fChance + (  len(pPlayerRace.GetFriendlys()) - len(pPlayerRace.GetEnemys()) )   #max ?, possible negative nºs
				iNumSystems = len(pPlayerRace.GetSystems())
				fChance = fChance + iNumSystems
				fChance = fChance + ((pPlayerRace.GetTotalEconomyProduction()/(iNumSystems+1)) / 10.0)
				fChance = fChance + ((pPlayerRace.GetTotalStrategicValue()/(iNumSystems+1)) / 10.0)
				fChance = fChance + ((pPlayerRace.GetTotalDefenceValue()/(iNumSystems+1)) / 10.0)
				fChance = fChance * (1.0/iTreatyIndex)
				if pRaceObj.GetIsEnemyToAll() == 1:
					fChance = 0.0
			lStrList.append( "  -Current Alliance Status: "+sAllianceStatus )
			if iTreatyIndex == 2:
				lStrList.append( "  -Chance of Signing a Successfull War Treaty:  "+GetStrFromFloat(fChance, 2)+"%" )
			elif iTreatyIndex == 1:
				lStrList.append( "  -Chance of Signing a Successfull Peace Treaty:  "+GetStrFromFloat(fChance, 2)+"%" )
			elif iTreatyIndex == 0:
				lStrList.append( "  -Peace and War Treaties are signed with this race." )
			lStrList.append( "" )
			lStrList.append( "" )
			lStrList.append( ">Attack Orders" )
			sSystems = "NONE"
			lRaceRegions = pRaceObj.GetSystems()
			if len(lRaceRegions) > 0:
				sSystems = ""
				for pRaceRegion in lRaceRegions:
					sSystems = sSystems + pRaceRegion.GetName() + ", "
				sSystems = sSystems[0:len(sSystems)-2] + "."
			lStrList.append( "  -Systems:  "+sSystems )
			HandleMCButtons(2, pRaceObj)
			SetTIVisible(1)

	elif iType == 5:  #System Development
		# Subtypes:
		# bases = 1
		# infrastructure = 2
		# technology assets = 3
		# military assets = 4
		HandleMCButtons(0)
		pPlayer = App.Game_GetCurrentPlayer()
		pRaceObj = GetRaceClassObj(GetShipRace(pPlayer))
		pSet = pPlayer.GetContainingSet()
		pRegion = None
		if pSet != None:
			pRegion = pSet.GetRegion()
		if pRaceObj != None and pRegion != None:
			if iSubType == 1:
				lStrList.append( "System Development - Starbase Placement")
				lStrList.append( "" )
				lStrList.append( "System:  "+pRegion.GetName() )
				lStrList.append( "Set:     "+pSet.GetName() )
				lStrList.append( "" )
				sBases = "NONE"
				lStarbases = GetBasesOfSet(pSet)
				if len(lStarbases) > 0:
					sBases = ""
					for pStarbase in lStarbases:
						sBases = sBases + pStarbase.GetName() + ", "
					sBases = sBases[0:len(sBases)-2] + "."
				lStrList.append( "Name of Starbases in Set:  "+sBases )
				lStrList.append( "" )
				lBases = pRaceObj.GetBases()
				sBaseClasses = "NONE"
				if len(lBases) > 0:
					sBaseClasses = ""
					for sBaseClass in lBases:
						sCost = GetStrFromFloat(GalacticWarSimulator.WarSimulator.GetShipClassCost(sBaseClass), 2)
						sBaseClasses = sBaseClasses + sBaseClass + "(Cost: "+sCost+"), "
					sBaseClasses = sBaseClasses[0:len(sBaseClasses)-2] + "."
				lStrList.append( "Starbase Classes Available:  "+sBaseClasses )
				lStrList.append( "" )
				lStrList.append( "Available Race Funds: "+GetStrFromFloat(pRaceObj.GetTotalFunds(), 2))
				lStrList.append( "" )
				lStrList.append( "" )
				lStrList.append( "INSTRUCTIONS:" )
				#lStrList.append( " >> About Set Starbases: a set can only have 1 bought starbase, however any starbase can be sold. The starbase that was bought will be placed in the set somewhere between 2 to 5 minutes." )
				lStrList.append( " >> To Buy a Starbase: type a starbase class name in the text input box and press buy starbase." )
				lStrList.append( " >> To Sell a Starbase: type a starbase name in the text input box and press sell starbase." )
				SetTIVisible(1)
				CreatePlaceStarbaseButtons()
				DeleteDevelopmentButton()
			elif iSubType in [2, 3, 4]:
				if iSubType == 2:
					sAttr = "Economic"
					sAltName = "Infrastructure"
				elif iSubType == 3:
					sAttr = "Strategic"
					sAltName = "Technological Assets"
				elif iSubType == 4:
					sAttr = "Default Defence"
					sAltName = "Military Assets"
				lStrList.append( "System Development - "+sAltName)
				lStrList.append( "" )
				lStrList.append( "System:  "+pRegion.GetName() )
				lStrList.append( "Set:     "+pSet.GetName() )
				lStrList.append( "" )
				lStrList.append( "Improving the "+sAltName+" of the set improves it\'s "+sAttr+" value." )
				lStrList.append( "" )
				pSetPlug = pRegion.GetSetByModule(pSet.GetRegionModule())
				if pSetPlug != None:
					SetTIVisible(1)
					CreateDevelopmentButton()
					DeletePlaceStarbaseButtons()
					lStrList.append( "Available Race Funds: "+GetStrFromFloat(pRaceObj.GetTotalFunds(), 2))
					lStrList.append( "" )
					if iSubType == 2:
						fCPP = App.g_kRegionManager.fEconomyPointCost  #cost per * point
						fCurrentValue = pSetPlug.GetEconomy()   #current set economic value
						fTotalValue = pRegion.GetTotalEconomy()  #total region economic value
						fLimit = pRegion.fEconomyLimit
					elif iSubType == 3:
						fCPP = App.g_kRegionManager.fStrategicPointCost  #cost per * point
						fCurrentValue = pSetPlug.GetStrategicValue()   #current set strategic value
						fTotalValue = pRegion.GetTotalStrategicValue()  #total region strategic value
						fLimit = pRegion.fStrategicLimit
					elif iSubType == 4:
						fCPP = App.g_kRegionManager.fDefencePointCost  #cost per * point
						fCurrentValue = pSetPlug.GetDefaultDefence()   #current set default defence value
						fTotalValue = pRegion.GetTotalDefaultDefence()  #total region default defence value
						fLimit = pRegion.fDefaultDefenceLimit
					lStrList.append( "Max Possible "+sAttr+" Value (per system):  "+GetStrFromFloat(fLimit, 2) )
					lStrList.append( "Current Total System "+sAttr+" Value:  "+GetStrFromFloat(fTotalValue, 2) )
					lStrList.append( "Current Set "+sAttr+" Value:  "+GetStrFromFloat(fCurrentValue, 2) )
					fPointsLeft = fLimit - fTotalValue
					lStrList.append( "Points left to max "+sAttr+" value: "+GetStrFromFloat(fPointsLeft, 2) )
					lStrList.append( "Cost per "+sAltName+" point:  "+str(fCPP)+" funds" )
					lStrList.append( "" )
					try:
						fAmount = float( pTI[1].GetCString() )
						if fAmount > fPointsLeft:
							fAmount = fPointsLeft
					except:
						fAmount = 0
					if fPointsLeft <= 0:
						lStrList.append( "The "+sAltName+" of this system is maxed out. No more development can be achieved." )
					elif fAmount > 0.0:
						fTotalCost = (fCPP*fAmount) + ((fCurrentValue*fCPP)*0.001)
						lStrList.append( "Amount selected: "+GetStrFromFloat(fAmount, 2) )
						lStrList.append( "Total Cost to Develop:  "+str(fTotalCost)+" funds" )
					else:
						lStrList.append( "Total Cost to Develop:  No amount selected" )
				else:
					lStrList.append( "Error: Couldn\'t acquire this set's SetPlugin object..." )
	if len(lStrList) > 0:
		pPara = pGUICreator.GetElement("DataPara")
		if pPara == None:
			pGUICreator.SetInfoForName("DataPara", 0, 0)
			pPara = pGUICreator.CreateParagraph("DataPara", lStrList, pSD)
			pPara.SetWrapWidth(0.39)
		else:
			pGUICreator.UpdateParagraph("DataPara", lStrList)
			pPara.SetPosition(0, 0)

	pSD.SetUseScrolling(1)
	pSD.SetScrollViewHeight(25.0)

def AddSubActionButton(sName, fYpos, iType):
	debug(__name__ + ", AddSubActionButton")
	if pGUICreator == None:
		return
	pSA = pGUICreator.GetElement("Sub-Actions")
	if pSA != None:
		ButtonDict = {'X': 0.0, 'Y': fYpos, 'WIDTH': 0.14, 'HEIGTH': 0.03}
		return pGUICreator.ButtonCreator.CreateButton(sName, None, __name__ + ".SubActionClick", iType, pSA, ButtonDict, ButtonDict)

##############################
# military command functions
###########
def HandleMCButtons(bCreate, pRaceObj = None):
	debug(__name__ + ", HandleMCButtons")
	global iMADCType
	if pGUICreator == None:
		return
	pParent = pGUICreator.GetElement("Strategic Data")
	if bCreate == 1:
		pGUICreator.ButtonCreator.DeleteButtonByName("Call For A Treaty")
		pGUICreator.ButtonCreator.DeleteButtonByName("Declare War")
		pGUICreator.ButtonCreator.DeleteButtonByName("Order Attack")
		pButton = pGUICreator.ButtonCreator.GetButtonByName("Player Leads Attack")
		if pButton == None:
			BDict = {'X': 0.15, 'Y': 0.41, 'WIDTH': 0.18, 'HEIGTH': 0.03}
			bPLA = GalacticWarSimulator.WarSimulator.GetPlayerLeadsAttack()
			pButton = pGUICreator.ButtonCreator.CreateYesNoButton("Player Leads Attack", None, __name__ + ".PLAEventHandler", bPLA, pParent, BDict, BDict)
	elif bCreate == 2:
		pGUICreator.ButtonCreator.DeleteButtonByName("Player Leads Attack")
		pPlayer = App.Game_GetCurrentPlayer()
		pPlayerRace = GetRaceClassObj( GetShipRace(pPlayer) )
		sAlliance = "NONE"
		iNumPlayerEnemies = 2  #default is something bigger than 1
		if pPlayerRace != None and pRaceObj != None:
			sAlliance = "Neutral"  #Peace Treaty
			if AreRacesEnemies(pPlayerRace.GetRaceName(), pRaceObj.GetRaceName()) == 1:
				sAlliance = "Hostile"  #Declared War
			elif AreRacesAllied(pPlayerRace.GetRaceName(), pRaceObj.GetRaceName()) == 1:
				sAlliance = "Allied"  #War Treaty
			iNumPlayerEnemies = len( pPlayerRace.GetEnemys() )

		pButton1 = pGUICreator.ButtonCreator.GetButtonByName("Call For A Treaty")
		if pButton1 == None:
			BDict = {'X': 0.02, 'Y': 0.25, 'WIDTH': 0.15, 'HEIGTH': 0.03}
			pButton1 = pGUICreator.ButtonCreator.CreateButton("Call For A Treaty", None, __name__ + ".MADCHandler", 1, pParent, BDict, BDict)
			if iMADCType == 1:
				pButton1.SetName(App.TGString("Cancel Treaty Offer"))
		pButton2 = pGUICreator.ButtonCreator.GetButtonByName("Declare War")
		if pButton2 == None:
			BDict = {'X': 0.2, 'Y': 0.25, 'WIDTH': 0.15, 'HEIGTH': 0.03}
			pButton2 = pGUICreator.ButtonCreator.CreateButton("Declare War", None, __name__ + ".MADCHandler", 2, pParent, BDict, BDict)
			if iMADCType == 2:
				pButton2.SetName(App.TGString("Cancel War Declaration"))
		pButton3 = pGUICreator.ButtonCreator.GetButtonByName("Order Attack")
		if pButton3 == None:
			BDict = {'X': 0.24, 'Y': 0.4, 'WIDTH': 0.15, 'HEIGTH': 0.03}
			pButton3 = pGUICreator.ButtonCreator.CreateButton("Order Attack", None, __name__ + ".MADCHandler", 3, pParent, BDict, BDict)
			if iMADCType == 3:
				pButton3.SetName(App.TGString("Cancel Attack"))
		if sAlliance == "Allied":    #War Treaty
			pButton1.SetDisabled()
			if not iMADCType in [1, 2, 3]:
				pButton1.SetName(App.TGString("No more treaties."))
			pButton2.SetEnabled()
			pButton3.SetDisabled()
		elif sAlliance == "Neutral":   #Peace Treaty
			pButton1.SetEnabled()
			if not iMADCType in [1, 2, 3]:
				pButton1.SetName(App.TGString("Offer War Treaty"))
			pButton2.SetEnabled()
			pButton3.SetDisabled()
		elif sAlliance == "Hostile":   #Declared War
			if iNumPlayerEnemies >= 2:
				pButton1.SetEnabled()
			else:
				pButton1.SetDisabled()
			if not iMADCType in [1, 2, 3]:
				pButton1.SetName(App.TGString("Offer Peace Treaty"))
			pButton2.SetDisabled()
			pButton3.SetEnabled()
		elif sAlliance == "NONE":
			pButton1.SetDisabled()
			pButton2.SetDisabled()
			pButton3.SetDisabled()
		if iMADCType == 1:
			pButton2.SetDisabled()
			pButton3.SetDisabled()
		elif iMADCType == 2:
			pButton1.SetDisabled()
			pButton3.SetDisabled()
		elif iMADCType == 3:
			pButton1.SetDisabled()
			pButton2.SetDisabled()
		if pRaceObj.GetIsEnemyToAll() == 1:
			pButton1.SetDisabled()
			pButton2.SetDisabled()
		if GalacticWarSimulator.IsBattleHappening() == 1:
			# don't enable ordering an attack if a battle is happening.
			pButton3.SetDisabled()
	elif bCreate == 0:
		pGUICreator.ButtonCreator.DeleteButtonByName("Player Leads Attack")
		pGUICreator.ButtonCreator.DeleteButtonByName("Call For A Treaty")
		pGUICreator.ButtonCreator.DeleteButtonByName("Declare War")
		pGUICreator.ButtonCreator.DeleteButtonByName("Order Attack")

def PLAEventHandler(pObject, pEvent):  #PLA - Player Leads Attack
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Player Leads Attack")
	if pButton != None:
		debug(__name__ + ", PLAEventHandler")
		GalacticWarSimulator.WarSimulator.SetPlayerLeadsAttack( pButton.IsChosen() )

pMADCTimer = None
iMADCType = 0
oMADCObj = None
def MADCHandler(pObject, pEvent):   #MADC - Military And Diplomatic Command
	global pTI, ET_MADC_TIMER, iMADCType, oMADCObj, pMADCTimer, dDynamicSAConnection, iSelectedSubType
	try:
		debug(__name__ + ", MADCHandler")
		iType = pEvent.GetInt()
	except:
		return
	pPlayer = App.Game_GetCurrentPlayer()
	pPlayerRace = GetRaceClassObj( GetShipRace(pPlayer) )
	sNewsMsg = ""
	sMessageBoxName = "Military And Diplomatic Command"
	sMsgText = ""
	if pMADCTimer != None:
		if iType == 1:  #Call Treaty
			pButton1 = pGUICreator.ButtonCreator.GetButtonByName("Call For A Treaty")
			pButton1.SetName(App.TGString("Call For A Treaty"))
			sMsgText = "Treaty signment with race "+oMADCObj.GetRaceName()+" has been cancelled."
			sNewsMsg = pPlayerRace.GetRaceName()+" "+sMsgText
		elif iType == 2:   #Declare War
			pButton2 = pGUICreator.ButtonCreator.GetButtonByName("Declare War")
			pButton2.SetName(App.TGString("Declare War"))
			sMsgText = "Declaring war for race "+oMADCObj.GetRaceName()+" has been cancelled."
			sNewsMsg = pPlayerRace.GetRaceName()+" war declaration for race "+oMADCObj.GetRaceName()+" has been cancelled."
		elif iType == 3:   #Order Attack
			pButton3 = pGUICreator.ButtonCreator.GetButtonByName("Order Attack")
			pButton3.SetName(App.TGString("Order Attack"))
			sMsgText = "Attack on system "+oMADCObj.GetName()+" has been cancelled."
			sNewsMsg = pPlayerRace.GetRaceName()+" cancelled attack on system "+oMADCObj.GetName()+"."
		App.g_kTimerManager.DeleteTimer(pMADCTimer.GetObjID())
		pMADCTimer = None
		iMADCType = 0
		oMADCObj = None
	else:
		fTimeToMADC = GetRandomInRange(120.0, 300.0)
		sTMADC = GetStrFromFloat(fTimeToMADC, 2)
		if iType == 1:  #Call Treaty
			if not dDynamicSAConnection.has_key(iSelectedSubType):
				return
			pRaceObj = dDynamicSAConnection[iSelectedSubType]
			pButton1 = pGUICreator.ButtonCreator.GetButtonByName("Call For A Treaty")
			oMADCObj = pRaceObj
			pButton1.SetName(App.TGString("Cancel Treaty Offer"))
			sMsgText = "Treaty negotiations with race "+oMADCObj.GetRaceName()+" has been initiated. Negotiations will end in approx. "+sTMADC+" seconds."
			sNewsMsg = pPlayerRace.GetRaceName()+" has started treaty negotiations with race "+oMADCObj.GetRaceName()+". They\'ll last approx. "+sTMADC+" secs."
		elif iType == 2:   #Declare War
			if not dDynamicSAConnection.has_key(iSelectedSubType):
				return
			pRaceObj = dDynamicSAConnection[iSelectedSubType]
			pButton2 = pGUICreator.ButtonCreator.GetButtonByName("Declare War")
			oMADCObj = pRaceObj
			pButton2.SetName(App.TGString("Cancel War Declaration"))
			sMsgText = "Declaring war for race "+oMADCObj.GetRaceName()+" has been initiated. Declaration will be ready in approx. "+sTMADC+" seconds."
			sNewsMsg = "In approx. "+sTMADC+" secs, "+pPlayerRace.GetRaceName()+" will declare war for race "+oMADCObj.GetRaceName()+"."
		elif iType == 3:   #Order Attack
			if len(pTI) <= 0:
				return
			sTargetSystem = pTI[1].GetCString()
			pRegion = App.g_kRegionManager.GetRegion(sTargetSystem)
			if pRegion == None:
				# invalid target system
				return
			pButton3 = pGUICreator.ButtonCreator.GetButtonByName("Order Attack")
			oMADCObj = pRegion
			pButton3.SetName(App.TGString("Cancel Attack"))
			sMsgText = "An attack on system "+oMADCObj.GetName()+" has been ordered, and will occur in approx. "+sTMADC+" seconds."
			sNewsMsg = "In approx. "+sTMADC+" secs, "+pPlayerRace.GetRaceName()+" will attack system "+oMADCObj.GetName()+"."
		iMADCType = iType
		pMADCTimer = MissionLib.CreateTimer(ET_MADC_TIMER, __name__ + ".ProcessMADCEvent", App.g_kUtopiaModule.GetGameTime()+fTimeToMADC, 0, 0)
	if sNewsMsg != "":
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)
	if sMsgText != "":
		pGUICreator.CreateMessageBox(sMessageBoxName, sMsgText )

def ProcessMADCEvent(pObject, pEvent):
	debug(__name__ + ", ProcessMADCEvent")
	global iMADCType, oMADCObj, pMADCTimer
	pPlayer = App.Game_GetCurrentPlayer()
	pPlayerRace = GetRaceClassObj( GetShipRace(pPlayer) )
	sNewsMsg = ""
	sMessageBoxName = "Military And Diplomatic Command"
	sMsgText = ""
	if pPlayerRace != None and oMADCObj != None:
		if iMADCType == 1:  #Call Treaty
			sAlliance = "Neutral"  #Peace Treaty
			if AreRacesEnemies(pPlayerRace.GetRaceName(), oMADCObj.GetRaceName()) == 1:
				sAlliance = "Hostile"  #Declared War
			elif AreRacesAllied(pPlayerRace.GetRaceName(), oMADCObj.GetRaceName()) == 1:
				sAlliance = "Allied"  #War Treaty
			iNumPlayerEnemies = len( pPlayerRace.GetEnemys() )
			#iTreatyIndex: works like an inversed difficulty value. the bigger it it, the smaller the chance will be.
			#used to check the chance of a treaty being signed successfully.
			iTreatyIndex = 0
			sTreatyType = "NONE"
			if sAlliance == "Allied" or (sAlliance == "Hostile" and iNumPlayerEnemies <= 1) or oMADCObj.GetIsEnemyToAll() == 1:
				#do nothing, can't make a treaty better than war OR player must have at least one enemy race.
				#OR race is enemy to ALL, don't allow treaties.
				App.g_kTimerManager.DeleteTimer(pMADCTimer.GetObjID())
				pMADCTimer = None
				sMsgText = "Treaty negotiations with race "+oMADCObj.GetRaceName()+" has been cancelled, it is already an allied race."
				sNewsMsg = pPlayerRace.GetRaceName()+" has cancelled treaty negotiations with race "+oMADCObj.GetRaceName()+". They are allied."
				GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)
				pGUICreator.CreateMessageBox(sMessageBoxName, sMsgText )
				iMADCType = 0
				oMADCObj = None
				return
			elif sAlliance == "Neutral":
				#do war treaty
				iTreatyIndex = 2
				sTreatyType = "War"
			elif sAlliance == "Hostile":
				#do peace treaty
				iTreatyIndex = 1
				sTreatyType = "Peace"
			fChance = (pPlayerRace.GetPeaceValue() + oMADCObj.GetPeaceValue()) * 10.0    #max 20
			fChance = fChance + (  len(pPlayerRace.GetFriendlys()) - iNumPlayerEnemies  )   #max ?, possible negative nºs
			iNumSystems = len(pPlayerRace.GetSystems())
			fChance = fChance + iNumSystems
			fChance = fChance + ((pPlayerRace.GetTotalEconomyProduction()/(iNumSystems+1)) / 10.0)
			fChance = fChance + ((pPlayerRace.GetTotalStrategicValue()/(iNumSystems+1)) / 10.0)
			fChance = fChance + ((pPlayerRace.GetTotalDefenceValue()/(iNumSystems+1)) / 10.0)
			fChance = fChance * (1.0/iTreatyIndex)
			if App.g_kSystemWrapper.GetRandomNumber(100) <= fChance:
				# treaty was successfully signed. Make appropriate update.
				if sAlliance == "Neutral":
					if oMADCObj.GetRaceName() in pPlayerRace.myEnemys:
						pPlayerRace.myEnemys.remove(oMADCObj.GetRaceName())
					if pPlayerRace.GetRaceName() in oMADCObj.myEnemys:
						oMADCObj.myEnemys.remove(pPlayerRace.GetRaceName())
					pPlayerRace.AddFriendly(oMADCObj.GetRaceName())
					oMADCObj.AddFriendly(pPlayerRace.GetRaceName())
					UpdateShipsAllegiance(oMADCObj.GetRaceName(), "Friendly")
				elif sAlliance == "Hostile":
					if oMADCObj.GetRaceName() in pPlayerRace.myFriendlys:
						pPlayerRace.myFriendlys.remove(oMADCObj.GetRaceName())
					if pPlayerRace.GetRaceName() in oMADCObj.myFriendlys:
						oMADCObj.myFriendlys.remove(pPlayerRace.GetRaceName())
					if oMADCObj.GetRaceName() in pPlayerRace.myEnemys:
						pPlayerRace.myEnemys.remove(oMADCObj.GetRaceName())
					if pPlayerRace.GetRaceName() in oMADCObj.myEnemys:
						oMADCObj.myEnemys.remove(pPlayerRace.GetRaceName())
					UpdateShipsAllegiance(oMADCObj.GetRaceName(), "Neutral")
				sMsgText = sTreatyType + " Treaty negotiations with race "+oMADCObj.GetRaceName()+" has been successfull."
				sNewsMsg = pPlayerRace.GetRaceName()+" has successfully signed a "+sTreatyType+" Treaty with race "+oMADCObj.GetRaceName()+"."
			else:
				sMsgText = oMADCObj.GetRaceName()+" didn\'t accept our "+sTreatyType+" Treaty offer..."
				sNewsMsg = oMADCObj.GetRaceName()+" didn\'t accept "+sTreatyType+" Treaty offer from the "+pPlayerRace.GetRaceName()
		elif iMADCType == 2:   #Declare War
			if oMADCObj.GetRaceName() in pPlayerRace.myFriendlys:
				pPlayerRace.myFriendlys.remove(oMADCObj.GetRaceName())
			if pPlayerRace.GetRaceName() in oMADCObj.myFriendlys:
				oMADCObj.myFriendlys.remove(pPlayerRace.GetRaceName())
			pPlayerRace.AddEnemy(oMADCObj.GetRaceName())
			oMADCObj.AddEnemy(pPlayerRace.GetRaceName())
			UpdateShipsAllegiance(oMADCObj.GetRaceName(), "Enemy")
			sMsgText = "We declared war for race "+oMADCObj.GetRaceName()
			sNewsMsg = pPlayerRace.GetRaceName()+" has declared war for race "+oMADCObj.GetRaceName()+"."
		elif iMADCType == 3:   #Order Attack
			oMADCObj.RegionBattle.CallRAFofRace(pPlayerRace.GetRaceName(), 0.01)
			sMsgText = "Our attack on system "+oMADCObj.GetName()+" has started."
			sNewsMsg = pPlayerRace.GetRaceName()+" attack on system "+oMADCObj.GetName()+" has started."
	App.g_kTimerManager.DeleteTimer(pMADCTimer.GetObjID())
	pMADCTimer = None
	iMADCType = 0
	oMADCObj = None
	if sNewsMsg != "":
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)
	if sMsgText != "":
		pGUICreator.CreateMessageBox(sMessageBoxName, sMsgText )

################
#  place starbase functions
###
def CreatePlaceStarbaseButtons():
	debug(__name__ + ", CreatePlaceStarbaseButtons")
	global pBuyTimer 
	pParent = pGUICreator.GetElement("Strategic Data")
	pOKButton = pGUICreator.ButtonCreator.GetButtonByName("Buy Starbase")
	if pOKButton == None:
		ButtonDict = {'X': 0.25, 'Y': 0.38, 'WIDTH': 0.14, 'HEIGTH': 0.03}
		pOKButton = pGUICreator.ButtonCreator.CreateButton("Buy Starbase", None, __name__ + ".BuyStarbase", 1, pParent, ButtonDict, ButtonDict)
	if pBuyTimer != None:
		pOKButton.SetName(App.TGString("Cancel Buy Order"))
	pDELButton = pGUICreator.ButtonCreator.GetButtonByName("Sell Starbase")
	if pDELButton == None:
		ButtonDict = {'X': 0.25, 'Y': 0.42, 'WIDTH': 0.14, 'HEIGTH': 0.03}
		pDELButton = pGUICreator.ButtonCreator.CreateButton("Sell Starbase", None, __name__ + ".SellStarbase", 1, pParent, ButtonDict, ButtonDict)
	if pSellTimer != None:
		pDELButton.SetName(App.TGString("Cancel Sell Order"))

def DeletePlaceStarbaseButtons():
	debug(__name__ + ", DeletePlaceStarbaseButtons")
	pGUICreator.ButtonCreator.DeleteButtonByName("Buy Starbase")
	pGUICreator.ButtonCreator.DeleteButtonByName("Sell Starbase")

pSetPlugToPlaceIn = None
def BuyStarbase(pObject, pEvent):
	debug(__name__ + ", BuyStarbase")
	global pTI, pBuyTimer, ET_BUY_TIMER, ET_MESSAGE_BOX,  pSetPlugToPlaceIn
	if len(pTI) <= 0:
		return
	sClassName = pTI[1].GetCString()
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		return
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Buy Starbase")
	pSet = pPlayer.GetContainingSet()
	if pSet == None:
		return None
	pRegion = pSet.GetRegion()
	if pRegion == None:
		return None
	pSetPlug = pRegion.GetSetByModule(pSet.GetRegionModule())
	if pSetPlug == None:
		return None
	sMessageBoxName = "Buy Starbase Message"
	if string.count(pSetPlug.GetStarbaseName(), "<STARBASE IN CONSTRUCTION>") >= 1:
		# place starbase order was cancelled.
		App.g_kTimerManager.DeleteTimer(pBuyTimer.GetObjID())
		pBuyTimer = None
		pSetPlugToPlaceIn = None
		sOldClassName = string.replace(pSetPlug.GetStarbaseName(), "<STARBASE IN CONSTRUCTION>", "")
		sCancelMsg = "Place Starbase Order for this set of starbase class "+sOldClassName+" has been cancelled."
		pGUICreator.CreateMessageBox(sMessageBoxName, sCancelMsg )
		sNewsMsg = "Place Starbase Order for set "+pSet.GetName()+" of starbase class "+sOldClassName+" has been cancelled."
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)		
		pSetPlug.RemoveStarbaseName()
		pButton.SetName(App.TGString("Buy Starbase"))
		return
	elif pBuyTimer != None:
		pGUICreator.CreateMessageBox(sMessageBoxName, "Can't buy a starbase now - another Place Starbase Order is being processed.")
		return
	elif pSetPlug.GetStarbaseName() != "" and pSetPlug.GetStarbaseObj() != None:
		pGUICreator.CreateMessageBox(sMessageBoxName, "Warning: This set already has a starbase: \'"+pSetPlug.GetStarbaseName()+"\'. She needs to be destroyed or sold before a new starbase can be bought.")
		return
	else:
		pRaceObj = GetRaceClassObj(GetShipRace(pPlayer))
		if pRaceObj == None:
			pGUICreator.CreateMessageBox(sMessageBoxName, "Error: player race is invalid or none")
			return
		if not sClassName in pRaceObj.GetBases():
			pGUICreator.CreateMessageBox(sMessageBoxName, "Warning: starbase class name is invalid or none. Please enter a valid starbase class name.")
			return
		fCost = GalacticWarSimulator.WarSimulator.GetShipClassCost(sClassName)
		if fCost > pRaceObj.GetTotalFunds():
			pGUICreator.CreateMessageBox(sMessageBoxName, "Warning: race doesn\'t have enough funds to buy the selected starbase class. Please wait for your race to have enough funds, or select a different starbase class name.")
			return
		fTimeToBePlaced = GetRandomInRange(120.0, 300.0)
		pSetPlug.SetStarbaseName("<STARBASE IN CONSTRUCTION>"+sClassName)
		pSetPlugToPlaceIn = pSetPlug
		sOkMsg = "A "+sClassName+" type starbase has been ordered to be placed on this set, estimated time for completion: "+GetStrFromFloat(fTimeToBePlaced, 2)
		pGUICreator.CreateMessageBox(sMessageBoxName, sOkMsg)
		sNewsMsg = "A "+sClassName+" type starbase has been ordered to be placed on set "+pSet.GetName()+", estimated time for completion: "+GetStrFromFloat(fTimeToBePlaced, 2)
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)
		pBuyTimer = MissionLib.CreateTimer(ET_BUY_TIMER, __name__ + ".PlaceBoughtStarbase", App.g_kUtopiaModule.GetGameTime()+fTimeToBePlaced, 0, 0)
		pButton.SetName(App.TGString("Cancel Buy Order"))
		return
		
def PlaceBoughtStarbase(pObject, pEvent):
	debug(__name__ + ", PlaceBoughtStarbase")
	global pBuyTimer, pSetPlugToPlaceIn
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Buy Starbase")
	if pButton != None:
		pButton.SetName(App.TGString("Buy Starbase"))
	sClassName = string.replace(pSetPlugToPlaceIn.GetStarbaseName(), "<STARBASE IN CONSTRUCTION>", "")
	pSetPlugToPlaceIn.RemoveStarbaseName()
	pSet = pSetPlugToPlaceIn.GetSetObj()
	pShip = CreateShip(GetShipDefByScript(sClassName), pSet, "", "Friendly", 0)
	sNewsMsg = "Starbase "+pShip.GetName()+" (class: "+sClassName+") has been placed on set "+pSet.GetName()
	pSetPlugToPlaceIn.SetStarbaseName(pShip.GetName())
	GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)
	###
	pSetPlugToPlaceIn = None
	App.g_kTimerManager.DeleteTimer(pBuyTimer.GetObjID())
	pBuyTimer = None


pSellTimer = None
pStarbaseToSell = None
def SellStarbase(pObject, pEvent):
	debug(__name__ + ", SellStarbase")
	global pTI, pSellTimer, ET_SELL_TIMER, pStarbaseToSell
	if len(pTI) <= 0:
		return
	sName = pTI[1].GetCString()
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		return
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Sell Starbase")
	pSet = pPlayer.GetContainingSet()
	if pSet == None:
		return None
	pRegion = pSet.GetRegion()
	if pRegion == None:
		return None
	pSetPlug = pRegion.GetSetByModule(pSet.GetRegionModule())
	if pSetPlug == None:
		return None
	sMessageBoxName = "Sell Starbase Message"
	if pStarbaseToSell != None and pSellTimer != None:
		pButton.SetName(App.TGString("Sell Starbase"))
		App.g_kTimerManager.DeleteTimer(pSellTimer.GetObjID())
		pSellTimer = None
		sCancelSell = "Sell Starbase Order for starbase "+pStarbaseToSell.GetName()+" has been cancelled."
		pGUICreator.CreateMessageBox(sMessageBoxName, sCancelSell)
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sCancelSell)
		pStarbaseToSell = None
		return
	lStarbases = GetBasesOfSet(pSet)
	if len(lStarbases) <= 0:
		pGUICreator.CreateMessageBox(sMessageBoxName, "There is no starbases in this set to be sold.")
		return
	dBasesNames = {}
	for pStarbase in lStarbases:
		dBasesNames[pStarbase.GetName()] = pStarbase
	if dBasesNames.has_key(sName):
		pStarbase = dBasesNames[sName]
		if GetShipRace(pPlayer) == GetShipRaceByWarSim(pStarbase):
			pButton.SetName(App.TGString("Cancel Sell Order"))
			pStarbaseToSell = pStarbase
			pStarbase.ClearAI() # the ship is being descomissioned, we don't want it to keep firing away for example :P
			fTimeToBeSold = GetRandomInRange(120.0, 300.0)
			sSellMsg = "Starbase "+sName+" has been ordered to be descomissioned on this set, estimated time for completion: "+GetStrFromFloat(fTimeToBeSold, 2)
			pGUICreator.CreateMessageBox(sMessageBoxName, sSellMsg)
			sNewsMsg = "Starbase "+sName+" has been ordered to be descomissioned from set "+pSet.GetName()+", estimated time for completion: "+GetStrFromFloat(fTimeToBeSold, 2)
			GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNewsMsg)
			pSellTimer = MissionLib.CreateTimer(ET_SELL_TIMER, __name__ + ".ProcessSoldStarbase", App.g_kUtopiaModule.GetGameTime()+fTimeToBeSold, 0, 0)
		else:
			pGUICreator.CreateMessageBox(sMessageBoxName, "Starbase "+sName+" is not from your race to sell.")
			return
	else:
		pGUICreator.CreateMessageBox(sMessageBoxName, "There is no starbase with name "+sName+" in this set to be sold.")
		return

def ProcessSoldStarbase(pObject, pEvent):
	debug(__name__ + ", ProcessSoldStarbase")
	global pSellTimer, pStarbaseToSell
	pSet = pStarbaseToSell.GetContainingSet()
	pRegion = pSet.GetRegion()
	pSetPlug = pRegion.GetSetByModule(pSet.GetRegionModule())
	if pSetPlug.GetStarbaseName() == pStarbaseToSell.GetName():
		pSetPlug.RemoveStarbaseName()
	pRaceObj = GetRaceClassObj(GetShipRaceByWarSim(pStarbaseToSell))
	if pRaceObj != None:
		fBaseCost = GalacticWarSimulator.WarSimulator.GetShipClassCost(  GetShipType(pStarbaseToSell)  )
		pRaceObj.AddFunds(fBaseCost/2.0)
	sMessageBoxName = "Sell Starbase Message"
	sSoldMsg = "Starbase "+pStarbaseToSell.GetName()+" has been descomissioned from set "+pSet.GetName()
	pGUICreator.CreateMessageBox(sMessageBoxName, sSoldMsg)
	GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sSoldMsg)
	pSet.RemoveObjectFromSet(pStarbaseToSell.GetName())
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Sell Starbase")
	if pButton != None:
		pButton.SetName(App.TGString("Sell Starbase"))
	App.g_kTimerManager.DeleteTimer(pSellTimer.GetObjID())
	pSellTimer = None
	pStarbaseToSell = None

#####################
# system development functions
######
pDevelopTimer = None
def CreateDevelopmentButton(): 
	debug(__name__ + ", CreateDevelopmentButton")
	global pDevelopTimer
	pParent = pGUICreator.GetElement("Strategic Data")
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Develop Set")
	if pButton == None:
		ButtonDict = {'X': 0.24, 'Y': 0.4, 'WIDTH': 0.15, 'HEIGTH': 0.03}
		pButton = pGUICreator.ButtonCreator.CreateButton("Develop Set", None, __name__ + ".DevelopSet", 1, pParent, ButtonDict, ButtonDict)
	if pDevelopTimer != None:
		pButton.SetName(App.TGString("Cancel Development"))

def DeleteDevelopmentButton():
	debug(__name__ + ", DeleteDevelopmentButton")
	pGUICreator.ButtonCreator.DeleteButtonByName("Develop Set")

fAmountSelected = 0.0
pSetPlugToDevelop = ""
sDevType = ""
def DevelopSet(pObject, pEvent):
	debug(__name__ + ", DevelopSet")
	global ET_DEVELOP_TIMER, pDevelopTimer, fAmountSelected, pSetPlugToDevelop, iSelectedSubType, sDevType
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer == None:
		return
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Develop Set")
	pSet = pPlayer.GetContainingSet()
	if pSet == None:
		return None
	pRegion = pSet.GetRegion()
	pRaceObj = GetRaceClassObj(GetShipRace(pPlayer))
	if pRegion == None or pRaceObj == None:
		return None
	pSetPlug = pRegion.GetSetByModule(pSet.GetRegionModule())
	if pSetPlug == None:
		return None
	if iSelectedSubType == 2:
		fCPP = App.g_kRegionManager.fEconomyPointCost  #cost per * point
		fCurrentValue = pSetPlug.GetEconomy()   #current set economic value
		fTotalValue = pRegion.GetTotalEconomy()  #total region economic value
		fLimit = pRegion.fEconomyLimit
		sAttr = "Economic"
		sAltName = "Infrastructure"
	elif iSelectedSubType == 3:
		fCPP = App.g_kRegionManager.fStrategicPointCost  #cost per * point
		fCurrentValue = pSetPlug.GetStrategicValue()   #current set strategic value
		fTotalValue = pRegion.GetTotalStrategicValue()  #total region strategic value
		fLimit = pRegion.fStrategicLimit
		sAttr = "Strategic"
		sAltName = "Technological Assets"
	elif iSelectedSubType == 4:
		fCPP = App.g_kRegionManager.fDefencePointCost  #cost per * point
		fCurrentValue = pSetPlug.GetDefaultDefence()   #current set default defence value
		fTotalValue = pRegion.GetTotalDefaultDefence()  #total region default defence value
		fLimit = pRegion.fDefaultDefenceLimit
		sAttr = "Default Defence"
		sAltName = "Military Assets"
	sDevType = sAltName
	fPointsLeft = fLimit - fTotalValue
	try:
		fAmount = float( pTI[1].GetCString() )
		if fAmount > fPointsLeft:
			fAmount = fPointsLeft
	except:
		fAmount = 0
	sMessageBoxName = "Develop System Message"
	if pDevelopTimer != None:
		# cancel...
		pButton.SetName(App.TGString("Develop Set"))
		App.g_kTimerManager.DeleteTimer(pDevelopTimer.GetObjID())
		pDevelopTimer = None
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sAltName+" development on set "+pSetPlugToDevelop.GetName()+" of "+str(fAmountSelected)+" points has been cancelled.")
		sDevelopMsg = sAltName+" Development cancelled."		
		pGUICreator.CreateMessageBox(sMessageBoxName, sDevelopMsg)
		pSetPlugToDevelop = None
		fAmountSelected = 0.0
	elif fPointsLeft <= 0:
		sDevelopMsg = "The "+sAltName+" of this system is maxed out. No more development can be achieved."
		pGUICreator.CreateMessageBox(sMessageBoxName, sDevelopMsg)
	elif fAmount > 0.0:
		fTotalCost = (fCPP*fAmount) + ((fCurrentValue*fCPP)*0.001)
		if pRaceObj.GetTotalFunds() >= fTotalCost:
			# develop
			fTimeToDevelop = GetRandomInRange(120.0, 300.0)
			fAmountSelected = fAmount
			pSetPlugToDevelop = pSetPlug
			pDevelopTimer = MissionLib.CreateTimer(ET_DEVELOP_TIMER, __name__ + ".ProcessDevelopment", App.g_kUtopiaModule.GetGameTime()+fTimeToDevelop, 0, 0)
			pButton.SetName(App.TGString("Cancel Development"))
			sDevelopMsg = sAltName+" of this set will be developed by "+str(fAmount)+" points, for a total cost of "+str(fTotalCost)+" funds, in approximately "+GetStrFromFloat(fTimeToDevelop, 2)+" seconds."
			pGUICreator.CreateMessageBox(sMessageBoxName, sDevelopMsg)
			sNews = sAltName+" of set "+pSetPlug.GetName()+" will be developed by "+str(fAmountSelected)+" points, for a total cost of "+str(fTotalCost)+" funds, in "+GetStrFromFloat(fTimeToDevelop, 2)+" secs."
			GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sNews)
		else:
			fMissing = fTotalCost - pRaceObj.GetTotalFunds()
			sDevelopMsg = "Not enough funds to develop this set. Missing "+str(fMissing)+" funds."
			pGUICreator.CreateMessageBox(sMessageBoxName, sDevelopMsg)
	else:
		sDevelopMsg = "No amount selected."
		pGUICreator.CreateMessageBox(sMessageBoxName, sDevelopMsg)


def ProcessDevelopment(pObject, pEvent):
	debug(__name__ + ", ProcessDevelopment")
	global pDevelopTimer, fAmountSelected, pSetPlugToDevelop, sDevType
	pRegion = pSetPlugToDevelop.GetParentRegion()
	pRaceObj = GetRaceClassObj(pRegion.GetControllingEmpire())
	if sDevType == "Infrastructure":
		fCPP = App.g_kRegionManager.fEconomyPointCost    #cost per * point
		fCurrentValue = pSetPlugToDevelop.GetEconomy()   #current set economic value
		fTotalValue = pRegion.GetTotalEconomy()          #total region economic value
		fLimit = pRegion.fEconomyLimit
	elif sDevType == "Technological Assets":
		fCPP = App.g_kRegionManager.fStrategicPointCost  #cost per * point
		fCurrentValue = pSetPlugToDevelop.GetStrategicValue()   #current set strategic value
		fTotalValue = pRegion.GetTotalStrategicValue()         #total region strategic value
		fLimit = pRegion.fStrategicLimit
	elif sDevType == "Military Assets":
		fCPP = App.g_kRegionManager.fDefencePointCost  #cost per * point
		fCurrentValue = pSetPlugToDevelop.GetDefaultDefence()   #current set default defence value
		fTotalValue = pRegion.GetTotalDefaultDefence()          #total region default defence value
		fLimit = pRegion.fDefaultDefenceLimit
	fPointsLeft = fLimit - fTotalValue
	if fAmountSelected > fPointsLeft:
		fAmountSelected = fPointsLeft
	fTotalCost = (fCPP*fAmountSelected) + ((fCurrentValue*fCPP)*0.001)
	sMessageBoxName = "Develop System Message"
	if pRaceObj.GetTotalFunds() >= fTotalCost:
		if sDevType == "Infrastructure":
			pSetPlugToDevelop.Economy = pSetPlugToDevelop.Economy + fAmountSelected
		elif sDevType == "Technological Assets":
			pSetPlugToDevelop.StrategicValue = pSetPlugToDevelop.StrategicValue + fAmountSelected
		elif sDevType == "Military Assets":
			pSetPlugToDevelop.DefaultDefence = pSetPlugToDevelop.DefaultDefence + fAmountSelected
		pRaceObj.DeductFunds(fTotalCost)
		GalacticWarSimulator.WarSimulator.AddNewsItem("Set", sDevType+" development on set "+pSetPlugToDevelop.GetName()+" of "+str(fAmountSelected)+" points has been completed.")
		sDevelopMsg = sDevType+" development on set "+pSetPlugToDevelop.GetName()+" has been completed."
		pGUICreator.CreateMessageBox(sMessageBoxName, sDevelopMsg)
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Develop Set")
	if pButton != None:
		pButton.SetName(App.TGString("Develop Set"))
	App.g_kTimerManager.DeleteTimer(pDevelopTimer.GetObjID())
	pDevelopTimer = None
	pSetPlugToDevelop = None
	fAmountSelected = 0.0
########################

pTI = []
def AddTextInput(sDefaultValue, fMaxWidth, Coords):
	debug(__name__ + ", AddTextInput")
	global pTI
	pDefault = App.TGString(sDefaultValue)
	sName = "SC Text Input"
	sConfigName = "SC Text InputC"
	pParent = pGUICreator.GetElement("Strategic Data")
	iMaxCharNum = 30
	fLongestLength = 0.0
	pTI = pGUICreator.ButtonCreator.CreateTextInput(sName, pParent, pDefault, fMaxWidth, fLongestLength, sConfigName, iMaxCharNum, 1, None, Coords)
	pTI[0].AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".TIHandler")

# tentar adicionar um ET_KEYBOARD handler para App.TopWindow_GetTopWindow() (talvez para o TacticalControlWindow ou Bridge)
# nele, caso a TI esteja selecionada, agente lê a tecla apertada e passa ela para o texto da TI (checar Lib.MissionHelper pra ver como fazer isso)
# senao, soh dah um CallNextHandler...

def SetTIVisible(bVisible):
	debug(__name__ + ", SetTIVisible")
	global pTI
	if len(pTI) >= 1:
		if bVisible == 1 and pTI[0].IsVisible() <= 0:
			pTI[0].SetVisible()
			pTI[1].SetVisible()
		elif bVisible == 0 and pTI[0].IsVisible() >= 1:
			pTI[0].SetNotVisible()
			pTI[1].SetNotVisible()

def TIHandler(pObject, pEvent):
	debug(__name__ + ", TIHandler")
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()

def MouseHandler(pObject, pEvent):
	debug(__name__ + ", MouseHandler")
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()


def KeyHandler(pObject, pEvent):
	debug(__name__ + ", KeyHandler")
	pObject.CallNextHandler(pEvent)
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()

def MsgBoxOK(pObject, pEvent):
	debug(__name__ + ", MsgBoxOK")
	pTop = App.TopWindow_GetTopWindow()
	if pTop:
		pTop.ToggleBridgeAndTactical()
		pTop.ToggleBridgeAndTactical()
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def GetRacePoints(pRaceObj):
	debug(__name__ + ", GetRacePoints")
	fFunds = pRaceObj.GetTotalFunds()
	fEconomy = pRaceObj.GetTotalEconomyProduction()
	fDefence = pRaceObj.GetTotalDefenceValue()
	fStrategic = pRaceObj.GetTotalStrategicValue()
	fTotal = (fFunds/1.5) + (fEconomy*5) + (fDefence*4) + (fStrategic*3)
	return fTotal

def GetRegionImportance(pRegion):
	# this is basically the same formula used in the method RegionBattle.callRDF
	debug(__name__ + ", GetRegionImportance")
	fInitialImportance = pRegion.GetTotalDefaultDefence() * 10000.0
	fReinImportance = ( (pRegion.GetTotalEconomy()* 9000.0) + (pRegion.GetTotalStrategicValue()* 11000.0) )
	return fInitialImportance + fReinImportance