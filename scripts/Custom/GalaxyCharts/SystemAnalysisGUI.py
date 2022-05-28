from bcdebug import debug
###############################################################################################################
#   SystemAnalysisGUI.py                 by Fernando Aluani
############
# This script that contains the code that sets up and handles the System Analysis window, which is used from
# the galaxy map.
###############################################################################################################
import App
import MissionLib
import Foundation
import string
import Custom.GravityFX.Logger
import Galaxy
import GalaxyMapGUI
from GalaxyLIB import *
from Custom.GravityFX.GravityFXguilib import *

pGUICreator = None
pAnaRegion = None
bIsOpened = 0
#####################################################################
def SetAnalysisRegion(pRegion):
	debug(__name__ + ", SetAnalysisRegion")
	global pAnaRegion, lPossibleNames, dActButtonsVisibleID, dIndexActions, dActButtonsNames
	pAnaRegion = pRegion
	# now get all of it's possible names (region and contained sets names)
	lPossibleNames = [pAnaRegion.GetName() + " System"]
	if pAnaRegion.GetAllSets() != []:
		lSets = pAnaRegion.GetAllSets()
		for pSet in lSets:
			lPossibleNames.append(pSet.GetName())
	else:
		for sSystem in pAnaRegion.Systems:
			sSystemName = string.split(sSystem, ".")[-1]
			lPossibleNames.append(sSystemName)

	# delete any previous analysis action buttons
	lIDkeys = dActButtonsVisibleID.keys()
	for iID in lIDkeys:
		pGUICreator.ButtonCreator.DeleteButtonByID(iID)
	dActButtonsVisibleID = {}
	dActButtonsNames = {}
	dIndexActions = {}

def CreateSAGUI(pRegion):
	debug(__name__ + ", CreateSAGUI")
	global pGUICreator, pAnaRegion
	if pGUICreator == None:
		pGUICreator = GUICreator()
	
	pPlayerRegion = GalaxyMapGUI.pPlayerRegion
	if pPlayerRegion == None:
		return
	if pRegion != None:
		SetAnalysisRegion(pRegion)
	else:
		SetAnalysisRegion(pPlayerRegion)
	SAOpenClose()


def SAOpenClose():
	debug(__name__ + ", SAOpenClose")
	global bIsOpened
	pSA = pGUICreator.GetElement("System Analysis")
	if not pSA:
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pGUICreator.SetInfoForName("System Analysis", 0.4, 0.1, 0.5, 0.8, 0)
		pSA = pGUICreator.CreateWindow("System Analysis", pTCW)
		pSA.SetUseScrolling(1)
		pSA.SetScrollViewHeight(25.0)
		pSA.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSA.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		pGUICreator.SetInfoForName("Analyse", 0.2, 0.1, 0.2, 0.5, 0)
		pAM = pGUICreator.CreateWindow("Analyse", pTCW)
		pAM.SetUseScrolling(1)
		pAM.SetScrollViewHeight(25.0)
		pAM.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pAM.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		pGUICreator.SetInfoForName("Sensors Status", 0.2, 0.6, 0.2, 0.15, 0)
		pSenSta = pGUICreator.CreateWindow("Sensors Status", pTCW)
		pSenSta.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSenSta.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		pGUICreator.SetInfoForName("Static Actions", 0.2, 0.75, 0.2, 0.15, 0)
		pStA = pGUICreator.CreateWindow("Static Actions", pTCW)
		pStA.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pStA.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")

		CreateSAStaticContents(pSA, pAM, pStA)
	if pSA.IsVisible():
		pGUICreator.CloseElement("System Analysis")
		pGUICreator.CloseElement("Analyse")
		pGUICreator.CloseElement("Sensors Status")
		pGUICreator.CloseElement("Static Actions")
		bIsOpened = 0
	else:
		pGUICreator.ShowElement("System Analysis")
		pGUICreator.ShowElement("Analyse")
		pGUICreator.ShowElement("Sensors Status")
		pGUICreator.ShowElement("Static Actions")
		bIsOpened = 1
		UpdateSystemAnalysis()
	
		
def SAClose(pObject = None, pEvent = None):
	debug(__name__ + ", SAClose")
	global bIsOpened
	if pGUICreator != None:
		pGUICreator.CloseElement("System Analysis")
		pGUICreator.CloseElement("Analyse")
		pGUICreator.CloseElement("Sensors Status")
		pGUICreator.CloseElement("Static Actions")
	bIsOpened = 0
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def CreateSAStaticContents(pSA, pAM, pStA):
	# Create static GUI contents.
	debug(__name__ + ", CreateSAStaticContents")
	ButtonDict = {'X': 0.01, 'Y': 0.0, 'WIDTH': 0.18, 'HEIGTH': 0.095}
	pGUICreator.ButtonCreator.CreateButton("Close", None, __name__ + ".SAClose", 1, pStA, ButtonDict, ButtonDict)


# Create dynamic GUI contents.
def UpdateSystemAnalysis():
	debug(__name__ + ", UpdateSystemAnalysis")
	global pAnaRegion, bIsOpened 
	if bIsOpened == 0:
		return
	
	pSA = pGUICreator.GetElement("System Analysis")
	pAM = pGUICreator.GetElement("Analyse")
	pSenSta = pGUICreator.GetElement("Sensors Status")

	sList = []
	fAnaFactor = EvaluateAnalysis(pAnaRegion)
	if type(fAnaFactor) == type(""):
		# something bad happened, like no sensors or thing like that "warn" the user
		sList.append("")
		sList.append("     WARNING    WARNING")
		sList.append("")
		sList.append(fAnaFactor)
		sList.append("")
		sList.append("     WARNING    WARNING")
		HandleActionButtons("NONE")
		sGrade = ""
	else:
		#[scan grade] Analysis Factor values (fAnaFactor): info to be shown
		#[E] 0  - 25:  type, name, controlling empire and sector, additional positional info(quadrant, etc)
		#[D] 25 - 50:  + description, image, contained sets (names only)
		#[C] 50 - 75: each set: name, alt name, economy, strategic, defence, description, nº of astronomical body
		#[B] 75 - 90: + all astronomical bodies info (name, type, etc), nº of normal objs
		#[A] 90 -100: + all normal objs info (name, type, etc), particle/radiation info
		#####
		# get the analysis info relative to the analysis factor and object to analyze selected
		# create/update the "objects to analyze" buttons accordingly
		if fAnaFactor <= 25:
			HandleActionButtons("REGION")
			sList = GetAnalysisInfo(fAnaFactor, sList)
			sGrade = "E"
		if 25 < fAnaFactor <= 50:
			HandleActionButtons("REGION")
			sList = GetAnalysisInfo(fAnaFactor, sList)
			sGrade = "D"
		if 50 < fAnaFactor <= 75:
			HandleActionButtons("ALL")
			sList = GetAnalysisInfo(fAnaFactor, sList)
			sGrade = "C"
		if 75 < fAnaFactor <= 90:
			HandleActionButtons("ALL")
			sList = GetAnalysisInfo(fAnaFactor, sList)
			sGrade = "B"
		if 90 < fAnaFactor <= 100:
			HandleActionButtons("ALL")
			sList = GetAnalysisInfo(fAnaFactor, sList)
			sGrade = "A"

	# assemble sensor status paragraph information
	lSenStat = []
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer != None:
		pSensors = pPlayer.GetSensorSubsystem()
		if pSensors != None:
			lSenStat.append("Sensors Base Range: "+GetStrFromFloat(pSensors.GetBaseSensorRange(), 2)+" ly")
			lSenStat.append("Sensors Range: "+GetStrFromFloat(pSensors.GetSensorRange(), 2)+" ly")
		else:
			lSenStat.append("NO SENSOR SYSTEM")
	if type(fAnaFactor) == type(""):
		lSenStat.append("Analysis was unsucessfull...")
	else:
		lSenStat.append("Analysis Scan Grade: "+str(sGrade))
		lSenStat.append("Analysis Factor: "+str(fAnaFactor))

	#####
	# create/update the sensor status paragraph
	pSSPara = pGUICreator.GetElement("SensorStatParag")
	if pSSPara == None:
		pGUICreator.SetInfoForName("SensorStatParag", 0, 0)
		pGUICreator.CreateParagraph("SensorStatParag", lSenStat, pSenSta)
	else:
		pGUICreator.UpdateParagraph("SensorStatParag", lSenStat)
		pSSPara.SetPosition(0, 0)

	#####
	# Create/update the system analysis paragraph
	pPara = pGUICreator.GetElement("SystemAnalysisParag")
	if pPara == None:
		pGUICreator.SetInfoForName("SystemAnalysisParag", 0, 0)
		pPara = pGUICreator.CreateParagraph("SystemAnalysisParag", sList, pSA)
		pPara.SetWrapWidth(0.48)
	else:
		pGUICreator.UpdateParagraph("SystemAnalysisParag", sList)
		pPara.SetPosition(0, 0)

	pSA.SetUseScrolling(1)
	pSA.SetScrollViewHeight(25.0)

dActButtonsVisibleID = {}
dActButtonsNames = {}
dIndexActions = {}
lPossibleNames = []
def HandleActionButtons(sType):
	debug(__name__ + ", HandleActionButtons")
	global pAnaRegion, dActButtonsVisibleID, dIndexActions, dActButtonsNames, lPossibleNames, iSelectedInt
	pAM = pGUICreator.GetElement("Analyse")
	if sType == "NONE":
		lIDkeys = dActButtonsVisibleID.keys()
		for iID in lIDkeys:
			if dActButtonsVisibleID[iID] == 1:
				pButton = pGUICreator.ButtonCreator.GetButtonByID(iID)
				pButton.SetNotVisible()
				dActButtonsVisibleID[iID] = 0
	if sType == "REGION":
		sName = lPossibleNames[0]
		if dActButtonsNames.has_key(sName):
			regbID = dActButtonsNames[sName]
			if dActButtonsVisibleID[regbID] == 0:
				pButton = pGUICreator.ButtonCreator.GetButtonByID(regbID)
				pButton.SetVisible()
				dActButtonsVisibleID[regbID] = 1
		else:
			ButtonDict = {'X': 0.01, 'Y': 0.0, 'WIDTH': 0.15, 'HEIGTH': 0.03}
			fIntValue = 1
			pButton = pGUICreator.ButtonCreator.CreateYesNoButton(sName, None, __name__ + ".AnalysisActionClick", fIntValue, pAM, ButtonDict, ButtonDict)
			iSelectedInt = 1
			regbID = pButton.GetObjID()
			dActButtonsNames[sName] = regbID
			dActButtonsVisibleID[regbID] = 1
			dIndexActions[fIntValue] = "REGION INFO"
		lIDkeys = dActButtonsVisibleID.keys()
		for iID in lIDkeys:
			if dActButtonsVisibleID[iID] == 1 and iID != regbID:
				pButton = pGUICreator.ButtonCreator.GetButtonByID(iID)
				pButton.SetNotVisible()
				dActButtonsVisibleID[iID] = 0
	if sType == "ALL":
		fIntValue = 1
		Y = 0.0
		for sName in lPossibleNames:
			if dActButtonsNames.has_key(sName):
				regbID = dActButtonsNames[sName]
				if dActButtonsVisibleID[regbID] == 0:
					pButton = pGUICreator.ButtonCreator.GetButtonByID(regbID)
					pButton.SetVisible()
					dActButtonsVisibleID[regbID] = 1
			else:
				ButtonDict = {'X': 0.01, 'Y': Y, 'WIDTH': 0.15, 'HEIGTH': 0.03}
				pButton = pGUICreator.ButtonCreator.CreateYesNoButton(sName, None, __name__ + ".AnalysisActionClick", fIntValue, pAM, ButtonDict, ButtonDict)
				if fIntValue != 1:
					pButton.SetChosen(0)
				else:
					iSelectedInt = 1
				regbID = pButton.GetObjID()
				dActButtonsNames[sName] = regbID
				dActButtonsVisibleID[regbID] = 1
				if fIntValue == 1:
					dIndexActions[fIntValue] = "REGION INFO"	
				else:
					dIndexActions[fIntValue] = sName
			Y = Y + 0.04
			fIntValue = fIntValue + 1
	pAM.SetUseScrolling(1)
	pAM.SetScrollViewHeight(25.0)

#[scan grade] Analysis Factor values (fAnaFactor): info to be shown
#[E] 0  - 25:  type, name, controlling empire and sector, additional positional info(quadrant, etc)
#[D] 25 - 50:  + description, image, contained sets (names only)
#[C] 50 - 75: each set: name, alt name, economy, strategic, defence, description, nº of astronomical body
#[B] 75 - 90: + all astronomical bodies info (name, type, etc), nº of normal objs
#[A] 90 -100: + all normal objs info (name, type, etc), particle/radiation info
def EvaluateAnalysis(pRegion):
	debug(__name__ + ", EvaluateAnalysis")
	pPlayerRegion = GalaxyMapGUI.pPlayerRegion
	pPlayer = App.Game_GetCurrentPlayer()
	pTravel = App.g_kTravelManager.GetTravel(pPlayer)
	if pPlayerRegion == None or pRegion == None or pPlayer == None:
		return "GalaxyCharts System Analysis: shit happened - no player region or normal region in evaluate."
	if pRegion.GetObjID() == pPlayerRegion.GetObjID():
		fDist = 0.0
	else:
		vWasLoc = pPlayerRegion.GetLocation()
		vGoLoc = pRegion.GetLocation()
		if vWasLoc != "DEFAULT" and vGoLoc != "DEFAULT" and pTravel != None:
			vDist = App.NiPoint2(vGoLoc.x - vWasLoc.x, vGoLoc.y - vWasLoc.y)
			fDist = vDist.Length()
			dWarpValues = Galaxy.GetWarpValues(fDist, pTravel.GetRealSpeed())
		else:
			return "GalaxyCharts System Analysis: WasLoc or GoLoc is DEFAULT, or Player Travel is NONE."
	sList = []
	pSensors = pPlayer.GetSensorSubsystem()
	if pSensors != None:
		if pSensors.GetCondition() <= 0:
			return "System Analysis was not sucessfull... Ship sensors are destroyed..."
		elif pSensors.IsDisabled() == 1:
			return "System Analysis was not sucessfull... Ship sensors are disabled..."
		elif pSensors.IsOn() == 0:
			return "System Analysis was not sucessfull... Ship sensors are offline..."
		else:
			fRange = pSensors.GetSensorRange()
			if fRange == 0 or fDist == 0:
				fAnaFactor = 100.0
			else:
				fAnaFactor = 100.0 - 100.0/(fRange/fDist)
			return fAnaFactor
	else:
		return "System Analysis was not sucessfull... Ship doesn't have sensors..."

iSelectedInt = -1
def AnalysisActionClick(pObject, pEvent):
	debug(__name__ + ", AnalysisActionClick")
	global iSelectedInt
	try:
		iInt = pEvent.GetInt()
	except:
		iInt = -1
	iSelectedInt = iInt
	iPressedID = pEvent.GetSource().GetObjID()
	lIDkeys = dActButtonsVisibleID.keys()
	for iID in lIDkeys:
		if iID != iPressedID:
			pButton = pGUICreator.ButtonCreator.GetButtonByID(iID)
			pButton.SetChosen(0)
	UpdateSystemAnalysis()

#[scan grade] Analysis Factor values (fAnaFactor): info to be shown
#[E] 0  - 25:  type, name, controlling empire and sector, additional positional info(quadrant, etc)
#[D] 25 - 50:  + description, image, contained sets (names only)
#[C] 50 - 75: each set: name, alt name, economy, strategic, defence, description, nº of astronomical body
#[B] 75 - 90: + all astronomical bodies info (name, type, etc), nº of normal objs
#[A] 90 -100: + all normal objs info (name, type, etc), particle/radiation info
def GetAnalysisInfo(fAnaFactor, sList):
	debug(__name__ + ", GetAnalysisInfo")
	global pAnaRegion, iSelectedInt, lPossibleNames
	if fAnaFactor <= 0:
		sList.append("Region is too far away to be analysed...")
	#[scan grade] Analysis Factor values (fAnaFactor): info to be shown
	#[E] 0  - 25:  type, name, controlling empire and sector, additional positional info(quadrant, etc)
	if 0 < fAnaFactor <= 25:
		sList.append("Name: "+pAnaRegion.GetName())
		sList.append("")
		sList.append("Type: "+pAnaRegion.GetType())
		sList.append("")
		if pAnaRegion.GetSectorNumber != 0:
			sList.append("Sector Number: "+str(pAnaRegion.GetSectorNumber()))
		else:
			sList.append("Sector Number:  unknown")
		sList.append("")
		sList.append("Controlling Empire: "+pAnaRegion.GetControllingEmpire())
		sList.append("")
		vLoc = pAnaRegion.GetLocation()
		if vLoc != None:
			X = vLoc.x
			Y = vLoc.y
			sQuadrant = "Unknown"
			if X < 0 and Y < 0:
				sQuadrant = "Gamma Quadrant"
			if X > 0 and Y < 0:
				sQuadrant = "Delta Quadrant"
			if X < 0 and Y > 0:
				sQuadrant = "Alpha Quadrant"
			if X > 0 and Y > 0:
				sQuadrant = "Beta Quadrant"
			if X == 0 and Y < 0:
				sQuadrant = "Gamma/Delta Quadrant Border"
			if X == 0 and Y > 0:
				sQuadrant = "Alpha/Beta Quadrant Border"
			if X > 0 and Y == 0:
				sQuadrant = "Beta/Delta Quadrant Border"
			if X < 0 and Y == 0:
				sQuadrant = "Alpha/Gamma Quadrant Border"
			if X == 0 and Y == 0:
				sQuadrant = "Galaxy Core"
			sList.append("Located in the "+sQuadrant+". Absolute location in galaxy: "+GetStrFromFloat(X, 2)+", "+GetStrFromFloat(Y, 2))
			sList.append("")
			if pAnaRegion.GetOnlyByRestrictedMethods() == 1:
				sList.append("Is Restricted: Yes, only accessible by listed restricted travelling methods.")
			else:
				sList.append("Is Restricted: No, accessible by non-restricted travelling methods and listed restricted methods.")
			sList.append("")
			sStr = ""
			if len(pAnaRegion.GetRestrictedFor()) >= 1:
				for sRestTravMethod in pAnaRegion.GetRestrictedFor():
					sStr = sStr + sRestTravMethod + ", "
				sStr = sStr[0:len(sStr)-2] + "."
			else:
				sStr = "None."
			sList.append("Restricted Travelling Methods: "+sStr)
			sList.append("")
	#[D] 25 - 50:  + description, image, contained sets (names only)
	if 25 < fAnaFactor <= 50:
		sList = GetAnalysisInfo(25, sList)
		sList.append("Description: "+pAnaRegion.GetDescription())
		sList.append("")
		lSnames = lPossibleNames
		sRegName = lPossibleNames[0]
		sList.append("Contained Sets: ")
		bSkip = 1
		for sSName in lPossibleNames:
			if bSkip == 1:
				bSkip = 0
			else:
				sList.append(" -"+sSName)
		# put image as well
	#[C] 50 - 75: each set: name, alt name, economy, strategic, defence, description, nº of astronomical body
	if 50 < fAnaFactor <= 75:
		if iSelectedInt == 1:
			# show the region info, so we just call for this function with a analysis factor of 50
			# considering that from 0 to 50 the only values to show are the region ones, and in 50 we have the most
			# region values we can get
			sList = GetAnalysisInfo(50, sList)
		else:
			sName = lPossibleNames[iSelectedInt - 1]
			sList.append("> GENERAL  INFORMATION")
			sList.append("Set Name: "+sName)
			pSetPlug = pAnaRegion.GetSet(sName)
			sSetScript = ""
			if pSetPlug != None:
				# okay we have the Set Plugin obj... add some additional info, mostly New Frontier stuff
				sList.append("Alternate Name: "+pSetPlug.GetAltName())
				sList.append("Economic Value: "+str(pSetPlug.GetEconomy()))
				sList.append("Strategic Value: "+str(pSetPlug.GetStrategicValue()))
				sList.append("Default Defence Value: "+str(pSetPlug.GetDefaultDefence()))
				sList.append("Description: "+pSetPlug.GetDescription())
				sSetScript = pSetPlug.GetScriptFile()
			else:
				sList.append("Unfortunately, a plugin with the additional info about this set wasn't found...")
				for sSystem in pAnaRegion.Systems:
					sSystemName = string.split(sSystem, ".")[-1]
					if sSystemName == sName:
						sSetScript = sSystem
			if sSetScript != "":
				# now try to get the App.SetClass obj of the set, form it we can get some other values.
				try:
					SetModule = __import__(sSetScript)
					pSet = SetModule.GetSet()
					if pSet != None:
						bDeleteSetAfter = 0
					else:
						# the set doesn't exist, so we'll just create it and then delete it after.
						# let's hope that way it won't lag or use too much memory
						SetModule.Initialize()
						pSet = SetModule.GetSet()
						if pSet != None:
							bDeleteSetAfter = 1
						else:
							sList.append("Couldn't get the SetClass object...")
					if pSet != None:
						dObjs = GetDictObjsInSet(pSet)
						del dObjs[App.CT_SHIP]
						sList.append("")
						sList.append("> INFORMATION  ABOUT  OBJECTS")
						sList.append("Astronomical Bodies Count:")
						sList.append(" -Suns: "+str(len(dObjs[App.CT_SUN])))
						sList.append(" -Planets: "+str(len(dObjs[App.CT_PLANET])))
						sList.append(" -Asteroid Fields: "+str(len(dObjs[App.CT_ASTEROID_FIELD])))
						sList.append(" -Nebulas: "+str(len(dObjs[App.CT_NEBULA])))
						#if bDeleteAfterSet == 1:
						#	App.g_kSetManager.DeleteSet(pSet.GetName())
				except:
					sList.append("Couldn't load Set Script Module...")
	#[B] 75 - 90: + all astronomical bodies info (name, type, etc), nº of normal objs
	if 75 < fAnaFactor <= 90:
		if iSelectedInt == 1:
			# show the region info, so we just call for this function with a analysis factor of 50
			# considering that from 0 to 50 the only values to show are the region ones, and in 50 we have the most
			# region values we can get
			sList = GetAnalysisInfo(50, sList)
		else:
			sName = lPossibleNames[iSelectedInt - 1]
			sList.append("> GENERAL  INFORMATION")
			sList.append("Set Name: "+sName)
			pSetPlug = pAnaRegion.GetSet(sName)
			sSetScript = ""
			if pSetPlug != None:
				# okay we have the Set Plugin obj... add some additional info, mostly New Frontier stuff
				sList.append("Alternate Name: "+pSetPlug.GetAltName())
				sList.append("Economic Value: "+str(pSetPlug.GetEconomy()))
				sList.append("Strategic Value: "+str(pSetPlug.GetStrategicValue()))
				sList.append("Default Defence Value: "+str(pSetPlug.GetDefaultDefence()))
				sList.append("Description: "+pSetPlug.GetDescription())
				sSetScript = pSetPlug.GetScriptFile()
			else:
				sList.append("Unfortunately, a plugin with the additional info about this set wasn't found...")
				for sSystem in pAnaRegion.Systems:
					sSystemName = string.split(sSystem, ".")[-1]
					if sSystemName == sName:
						sSetScript = sSystem
			if sSetScript != "":
				# now try to get the App.SetClass obj of the set, form it we can get some other values.
				try:
					SetModule = __import__(sSetScript)
					pSet = SetModule.GetSet()
					if pSet != None:
						bDeleteSetAfter = 0
					else:
						# the set doesn't exist, so we'll just create it and then delete it after.
						# let's hope that way it won't lag or use too much memory
						SetModule.Initialize()
						pSet = SetModule.GetSet()
						if pSet != None:
							bDeleteSetAfter = 1
						else:
							sList.append("Couldn't get the SetClass object...")
					if pSet != None:
						dObjs = GetDictObjsInSet(pSet)
						lKeys = dObjs.keys()
						sList.append("")
						sList.append("> INFORMATION  ABOUT  OBJECTS")
						sList.append("Astronomical Bodies:")
						for pSun in dObjs[App.CT_SUN]:
							sList.append(" -"+pSun.GetName()+"  (Sun):")
							vObjLoc = pSun.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pSun.GetRadius()), 2)+" km")
							sList.append("    -Atmosphere Radius: "+GetStrFromFloat(ConvertGUtoKM(pSun.GetAtmosphereRadius()), 2)+" km")
							try:
								sList.append("    -Density: "+GetStrFromFloat(pSun.GetDensity(), 2)+" g/cm^3")
								sList.append("    -Mass: "+GetStrFromFloat(pSun.GetMass(), 2)+" kg")
								sList.append("    -Class: "+str(pSun.GetClass()))
								GW = App.g_kGravityManager.GetGravWell(pSun.GetName())
								if GW != None:
									sList.append("    -Gravity Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius), 2)+" km")
							except:
								pass
							sList.append("")
						for pPlanet in dObjs[App.CT_PLANET]:
							sList.append(" -"+pPlanet.GetName()+"  (Planet):")
							vObjLoc = pPlanet.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pPlanet.GetRadius()), 2)+" km")
							sList.append("    -Atmosphere Radius: "+GetStrFromFloat(ConvertGUtoKM(pPlanet.GetAtmosphereRadius()), 2)+" km")
							try:
								sList.append("    -Density: "+GetStrFromFloat(pPlanet.GetDensity(), 2)+" g/cm^3")
								sList.append("    -Mass: "+GetStrFromFloat(pPlanet.GetMass(), 2)+" kg")
								sList.append("    -Class: "+str(pPlanet.GetClass()))
								GW = App.g_kGravityManager.GetGravWell(pPlanet.GetName())
								if GW != None:
									sList.append("    -Gravity Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius), 2)+" km")
							except:
								pass
							sList.append("")
						for pAsteroidField in dObjs[App.CT_ASTEROID_FIELD]:
							sList.append(" -"+pAsteroidField.GetName()+"  (Asteroid Field):")
							vObjLoc = pAsteroidField.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pAsteroidField.GetRadius()), 2)+" km")
							sList.append("    -Outer Field Radius: "+GetStrFromFloat(ConvertGUtoKM(pAsteroidField.GetOuterFieldRadius()), 2)+" km")
							sList.append("    -Inner Field Radius: "+GetStrFromFloat(ConvertGUtoKM(pAsteroidField.GetInnerFieldRadius()), 2)+" km")
							sList.append("    -Asteroids Per Tile: "+str(pAsteroidField.GetNumAsteroidsPerTile()))
							sList.append("    -Asteroid Size Factor: "+str(pAsteroidField.GetAsteroidSizeFactor()))
							sList.append("    -Tile Size: "+str(pAsteroidField.GetTileSize()))
							sList.append("")
						for pNebula in dObjs[App.CT_NEBULA]:
							sList.append(" -"+pNebula.GetName()+"  (Nebula):")
							vObjLoc = pNebula.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pNebula.GetRadius()), 2)+" km")
							sList.append("")
						sList.append("Ships Count:")
						dShipClasses = {}
						for pShip in dObjs[App.CT_SHIP]:
							sShipType = GetShipType(pShip)
							if dShipClasses.has_key(sShipType):
								dShipClasses[sShipType] = dShipClasses[sShipType] + 1
							else:
								dShipClasses[sShipType] = 1
						lClasses = dShipClasses.keys()
						if lClasses != []:
							sList.append("Ships Count:")
						else:
							sList.append("No Ship Count.")
						for sClass in lClasses:
							sList.append(" -"+sClass+": "+str(dShipClasses[sClass]))
						#if bDeleteAfterSet == 1:
						#	App.g_kSetManager.DeleteSet(pSet.GetName())
				except:
					sList.append("Couldn't load Set Script Module...")
	#[A] 90 -100: + all normal objs info (name, type, etc), particle/radiation info
	if 90 < fAnaFactor <= 100:
		if iSelectedInt == 1:
			# show the region info, so we just call for this function with a analysis factor of 50
			# considering that from 0 to 50 the only values to show are the region ones, and in 50 we have the most
			# region values we can get
			sList = GetAnalysisInfo(50, sList)
		else:
			sName = lPossibleNames[iSelectedInt - 1]
			sList.append("> GENERAL  INFORMATION")
			sList.append("Set Name: "+sName)
			pSetPlug = pAnaRegion.GetSet(sName)
			sSetScript = ""
			if pSetPlug != None:
				# okay we have the Set Plugin obj... add some additional info, mostly New Frontier stuff
				sList.append("Alternate Name: "+pSetPlug.GetAltName())
				sList.append("Economic Value: "+str(pSetPlug.GetEconomy()))
				sList.append("Strategic Value: "+str(pSetPlug.GetStrategicValue()))
				sList.append("Default Defence Value: "+str(pSetPlug.GetDefaultDefence()))
				sList.append("Description: "+pSetPlug.GetDescription())
				sSetScript = pSetPlug.GetScriptFile()
			else:
				sList.append("Unfortunately, a plugin with the additional info about this set wasn't found...")
				for sSystem in pAnaRegion.Systems:
					sSystemName = string.split(sSystem, ".")[-1]
					if sSystemName == sName:
						sSetScript = sSystem
			if sSetScript != "":
				# now try to get the App.SetClass obj of the set, form it we can get some other values.
				try:
					SetModule = __import__(sSetScript)
					pSet = SetModule.GetSet()
					if pSet != None:
						bDeleteSetAfter = 0
					else:
						# the set doesn't exist, so we'll just create it and then delete it after.
						# let's hope that way it won't lag or use too much memory
						SetModule.Initialize()
						pSet = SetModule.GetSet()
						if pSet != None:
							bDeleteSetAfter = 1
						else:
							sList.append("Couldn't get the SetClass object...")
					if pSet != None:
						dObjs = GetDictObjsInSet(pSet)
						lKeys = dObjs.keys()
						sList.append("")
						sList.append("> INFORMATION  ABOUT  OBJECTS")
						sList.append("Astronomical Bodies:")
						for pSun in dObjs[App.CT_SUN]:
							sList.append(" -"+pSun.GetName()+"  (Sun):")
							vObjLoc = pSun.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pSun.GetRadius()), 2)+" km")
							sList.append("    -Atmosphere Radius: "+GetStrFromFloat(ConvertGUtoKM(pSun.GetAtmosphereRadius()), 2)+" km")
							try:
								sList.append("    -Density: "+GetStrFromFloat(pSun.GetDensity(), 2)+" g/cm^3")
								sList.append("    -Mass: "+GetStrFromFloat(pSun.GetMass(), 2)+" kg")
								sList.append("    -Class: "+str(pSun.GetClass()))
								GW = App.g_kGravityManager.GetGravWell(pSun.GetName())
								if GW != None:
									sList.append("    -Gravity Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius), 2)+" km")
							except:
								pass
							sList.append("")
						for pPlanet in dObjs[App.CT_PLANET]:
							sList.append(" -"+pPlanet.GetName()+"  (Planet):")
							vObjLoc = pPlanet.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pPlanet.GetRadius()), 2)+" km")
							sList.append("    -Atmosphere Radius: "+GetStrFromFloat(ConvertGUtoKM(pPlanet.GetAtmosphereRadius()), 2)+" km")
							try:
								sList.append("    -Density: "+GetStrFromFloat(pPlanet.GetDensity(), 2)+" g/cm^3")
								sList.append("    -Mass: "+GetStrFromFloat(pPlanet.GetMass(), 2)+" kg")
								sList.append("    -Class: "+str(pPlanet.GetClass()))
								GW = App.g_kGravityManager.GetGravWell(pPlanet.GetName())
								if GW != None:
									sList.append("    -Gravity Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius), 2)+" km")
							except:
								pass
							sList.append("")
						for pAsteroidField in dObjs[App.CT_ASTEROID_FIELD]:
							sList.append(" -"+pAsteroidField.GetName()+"  (Asteroid Field):")
							vObjLoc = pAsteroidField.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pAsteroidField.GetRadius()), 2)+" km")
							sList.append("    -Outer Field Radius: "+GetStrFromFloat(ConvertGUtoKM(pAsteroidField.GetOuterFieldRadius()), 2)+" km")
							sList.append("    -Inner Field Radius: "+GetStrFromFloat(ConvertGUtoKM(pAsteroidField.GetInnerFieldRadius()), 2)+" km")
							sList.append("    -Asteroids Per Tile: "+str(pAsteroidField.GetNumAsteroidsPerTile()))
							sList.append("    -Asteroid Size Factor: "+str(pAsteroidField.GetAsteroidSizeFactor()))
							sList.append("    -Tile Size: "+str(pAsteroidField.GetTileSize()))
							sList.append("")
						for pNebula in dObjs[App.CT_NEBULA]:
							sList.append(" -"+pNebula.GetName()+"  (Nebula):")
							vObjLoc = pNebula.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pNebula.GetRadius()), 2)+" km")
							sList.append("")
						for pShip in dObjs[App.CT_SHIP]:
							sShipType = GetShipType(pShip)
							sList.append(" -"+pShip.GetName()+"  (Ship/Object):")
							vObjLoc = pShip.GetWorldLocation()
							sList.append("    -Location In Set: "+GetStrFromFloat(vObjLoc.x, 2)+" ,  "+GetStrFromFloat(vObjLoc.y, 2)+" ,  "+GetStrFromFloat(vObjLoc.z, 2))
							sList.append("    -Radius: "+GetStrFromFloat(ConvertGUtoKM(pShip.GetRadius()), 2)+" km")
							sList.append("    -Class: "+sShipType)
							sList.append("    -Mass: "+GetStrFromFloat(pShip.GetMass(), 2))
							pHull = pShip.GetHull()
							if pHull != None:
								fPerc = 100.0/(pHull.GetMaxCondition()/pHull.GetCondition())
								sList.append("    -Hull Condition: "+GetStrFromFloat(fPerc, 2)+"%")
							try:
								GW = App.g_kGravityManager.GetGravWell(pShip.GetName())
								if GW != None:
									sList.append("    -Gravity Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius), 2)+" km")
							except:
								pass
							sList.append("")
						#if bDeleteAfterSet == 1:
						#	App.g_kSetManager.DeleteSet(pSet.GetName())
				except:
					sList.append("Couldn't load Set Script Module...")
			if pSetPlug != None:
				sList.append("")
				sList.append("> ENVIRONMENTAL INFORMATION")
				sList.append("Explanation: 0.1 is the lowest concentration value possible, while 10.0 is the biggest concentration value possible")
				sList.append("")
				sList.append("Radiations:")
				lRadiationNames = ["Chroniton","Cosmic","Delta","EM","Gamma","Hyperonic","Kinoplasmic","Thalaron","Theta","Metaphasic","Omicron","Plasma","Polarc","Subnucleonic","Subspace","Temporal","Thermionic","Thoron"]
				for sRadName in lRadiationNames:
					sList.append(" -"+sRadName+": "+str(pSetPlug.GetRadiationValue(sRadName)))
				sList.append("")
				sList.append("Particles:")
				lParticleNames = ["AntiProtons","AntiNeutrinos","AntiGravitons","DarkMatter","Duderons","Metreons","Gravitons","Omega","Polarons","Positrons","Tetryons","Verterons","Mesons","Neutrinos"]
				for sParName in lParticleNames:
					sList.append(" -"+sParName+": "+str(pSetPlug.GetParticleValue(sParName)))
	return sList

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