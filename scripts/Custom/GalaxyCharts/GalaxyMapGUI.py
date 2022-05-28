from bcdebug import debug
################################################################
#######  SystemMap Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is the script that handles the great System Map window GUI in-game lol
####################################################################
import App
import MissionLib
import Foundation
import string
import Custom.GravityFX.Logger
import Galaxy
import SystemAnalysisGUI
import HelmAddonGUI
import GalacticWarSimulator
from GalaxyLIB import *
from Custom.GravityFX.GravityFXguilib import *

pGUICreator = None
eRefresh = None
ET_GALAXY_MAP = None
ShowAllNames = 1
InfoNamesList = []
pPlayerRegion = None
pSelectedRegion = None
bWasRegionsCreated = 0
sSelectedSubSet = None
lSubSetsNames = []
sOldPlayerReg = 0
###########################################################
#   The Icon's colors, for easy reference later
###########################################################
COLOR_PLAYER = App.TGColorA()
COLOR_PLAYER.SetRGBA(0.0, 1.0, 0.0, 1.0)     #green
COLOR_REGION = App.TGColorA()
COLOR_REGION.SetRGBA(1.0, 1.0, 0.0, 1.0)     #yellow
COLOR_SELECTED = App.TGColorA()
COLOR_SELECTED.SetRGBA(0.0, 0.0, 1.0, 1.0)   #blue
COLOR_HOSTILE = App.TGColorA()
COLOR_HOSTILE.SetRGBA(1.0, 0.0, 0.0, 1.0)    #red
COLOR_ALLIED = App.TGColorA()
COLOR_ALLIED.SetRGBA(0.133, 0.635, 1.0, 1.0)     #clear blue

###########################################################
#   The Icon Group Name, for easy reference later
###########################################################
GALAXY_ICONS = "GalaxyChartIcons"

###########################################################
#   The Icon's numbers, for easy reference later
###########################################################
ICON_HORIZONTAL_BAR = 0
ICON_VERTICAL_BAR = 1
ICON_REGION = 2
ICON_MILKYWAY = 3

###########################################################
#   The MAP's X/Y/W/H, for some easy math later
###########################################################
MAP_X = 0.00781250093132 
MAP_Y = 0.0229167640209
MAP_W = 0.788477003574 - MAP_X    # do these little subtractions on W and H because it's actually the subtraction
MAP_H = 0.745312333107 - MAP_Y    # EndX - X = Width
Real_MAP_W = MAP_W
Real_MAP_H = MAP_H
Pos_MAP_X = 0.0
Pos_MAP_Y = 0.0
###########################################################

def CreateGalaxyMapGUI():
	debug(__name__ + ", CreateGalaxyMapGUI")
	global ET_GALAXY_MAP, pGUICreator
	pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
	pBridge = App.g_kSetManager.GetSet("bridge")
	pScience = App.CharacterClass_GetObject(pBridge, "Science")
	pHelm = App.CharacterClass_GetObject(pBridge, "Helm")
	if pHelm == None or pScience == None:
		return
	pScienceMenu = pScience.GetMenu()
	pHelmMenu = pHelm.GetMenu()
	if pScienceMenu == None or pHelmMenu == None:
		return

	pGUICreator = GUICreator()

	ET_GALAXY_MAP = GetNextEventType()
	# Just to be sure, tho its kinda impossible to have any at this point. 
	PurgeGalaxyMap()
	
	pGUICreator.ButtonCreator.CreateButton("Stellar Cartography", ET_GALAXY_MAP, None, 1, pScienceMenu)
	pGUICreator.ButtonCreator.CreateButton("Stellar Cartography", ET_GALAXY_MAP, None, 1, pHelmMenu)
	
	App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_GALAXY_MAP, pMission, __name__ + ".GMOpenClose")
	pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".GMClose")
	pHelm.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".GMClose")
	# As the System Analysis GUI is pratically dependant of this, we'll do the following here
	pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, "Custom.GalaxyCharts.SystemAnalysisGUI.SAClose")
	pHelm.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, "Custom.GalaxyCharts.SystemAnalysisGUI.SAClose")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(pGUICreator.GetGenericOKEventType(), pMission, __name__ + ".MsgBoxOK")

def GMOpenClose(pObject, pEvent):
	debug(__name__ + ", GMOpenClose")
	pGM = pGUICreator.GetElement("Galaxy Map")
	if not pGM:
		pGUICreator.SetInfoForName("Galaxy Map", 0.0, 0.0, 0.8, 0.8, 0)
		pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
		pGM = pGUICreator.CreateWindow("Galaxy Map", pTCW)

		pGUICreator.SetInfoForName("Information", 0.8, 0.0, 0.2, 0.3, 0)
		pInfoW = pGUICreator.CreateWindow("Information", pTCW)
		pInfoW.SetUseScrolling(1)
		pInfoW.SetScrollViewHeight(25.0)

		pGUICreator.SetInfoForName("Sub-Sets", 0.8, 0.3, 0.2, 0.5, 0)
		pSubSetW = pGUICreator.CreateWindow("Sub-Sets", pTCW)
		pSubSetW.SetUseScrolling(1)
		pSubSetW.SetScrollViewHeight(25.0)

		pGUICreator.SetInfoForName("Actions", 0.0, 0.8, 0.65, 0.2, 0)
		pActW = pGUICreator.CreateWindow("Actions", pTCW)

		pGUICreator.SetInfoForName("Travelling", 0.8, 0.8, 0.2, 0.2, 0)
		pTraW = pGUICreator.CreateWindow("Travelling", pTCW)

		pGUICreator.SetInfoForName("Preset Views", 0.65, 0.8, 0.15, 0.2, 0)
		pPVW = pGUICreator.CreateWindow("Preset Views", pTCW)
		pPVW.SetUseScrolling(1)
		pPVW.SetScrollViewHeight(25.0)

		pGM.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pInfoW.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pSubSetW.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pActW.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pTraW.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pPVW.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
		pGM.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		pInfoW.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		pSubSetW.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		pActW.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		pTraW.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		pPVW.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		NamesList = ["GM Layer: Grid", "GM Layer: Regions", "GM Layer: Info"]
		for sName in NamesList:
			pGUICreator.SetInfoForName(sName, MAP_X, MAP_Y, MAP_W, MAP_H, 0)	
			pPane = pGUICreator.CreatePane(sName, pTCW)
			pPane.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
			pPane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
		CreateGMContents()
	if pGM.IsVisible():
		pGUICreator.CloseElement("Galaxy Map")
		pGUICreator.CloseElement("Information")
		pGUICreator.CloseElement("Sub-Sets")
		pGUICreator.CloseElement("Actions")
		pGUICreator.CloseElement("Travelling")
		pGUICreator.CloseElement("Preset Views")
		pGUICreator.CloseElement("GM Layer: Grid")
		pGUICreator.CloseElement("GM Layer: Regions")
		pGUICreator.CloseElement("GM Layer: Info")
		DeleteRegionIcons()
	else:
		pGUICreator.ShowElement("Galaxy Map")
		pGUICreator.ShowElement("Information")
		pGUICreator.ShowElement("Sub-Sets")
		pGUICreator.ShowElement("Actions")
		pGUICreator.ShowElement("Travelling")
		pGUICreator.ShowElement("Preset Views")
		pGUICreator.ShowElement("GM Layer: Grid")
		pGUICreator.ShowElement("GM Layer: Regions")
		pGUICreator.ShowElement("GM Layer: Info")
		CreateRegionIcons()
		SOIClick(None, None)
		HandleMapBackground()
		
def GMClose(pObject, pEvent):
	debug(__name__ + ", GMClose")
	if pGUICreator != None:
		pGUICreator.CloseElement("Galaxy Map")
		pGUICreator.CloseElement("Information")
		pGUICreator.CloseElement("Sub-Sets")
		pGUICreator.CloseElement("Actions")
		pGUICreator.CloseElement("Travelling")
		pGUICreator.CloseElement("Preset Views")
		pGUICreator.CloseElement("GM Layer: Grid")
		pGUICreator.CloseElement("GM Layer: Regions")
		pGUICreator.CloseElement("GM Layer: Info")
	DeleteRegionIcons()
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def CreateGMContents():
	debug(__name__ + ", CreateGMContents")
	global eRefresh
	pGM = pGUICreator.GetElement("Galaxy Map")
	pActW = pGUICreator.GetElement("Actions")
	pTraW = pGUICreator.GetElement("Travelling")
	pPVW = pGUICreator.GetElement("Preset Views")	

	pGUICreator.IconCreator.CreateIconGroup(GALAXY_ICONS, 'scripts/Custom/GalaxyCharts/Icons')
	pIconGroup = App.g_kIconManager.GetIconGroup(GALAXY_ICONS)
	if pIconGroup:
		Texture = pIconGroup.LoadIconTexture("scripts/Custom/GalaxyCharts/Icons/MilkyWay.tga")
		pIconGroup.SetIconLocation(ICON_MILKYWAY, Texture, 0, 0, 512, 512)

	HandleScalePara()  #Do this to create the scale paragraph before any buttons. otherwise: BUG! yay!
	UpdateTTPara()

	#Create Buttons
	CloseButtonDict = {'X': 0.01, 'Y': 0.11, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pGUICreator.ButtonCreator.CreateButton("Close", None, __name__ + ".GMClose", 1, pActW, CloseButtonDict, CloseButtonDict)

	SOIButtonDict = {'X': 0.01, 'Y': 0.06, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pGUICreator.ButtonCreator.CreateYesNoButton("Show All Names of All Regions", None, __name__ + ".SOIClick", 1, pActW, SOIButtonDict, SOIButtonDict)	

	SAButtonDict = {'X': 0.35, 'Y': 0.06, 'WIDTH': 0.25, 'HEIGTH': 0.03}
	pGUICreator.ButtonCreator.CreateButton("System Analysis", None, __name__ + ".SystemAnalysis", 1, pActW, SAButtonDict, SAButtonDict)	

	SGButtonDict = {'X': 0.35, 'Y': 0.11, 'WIDTH': 0.25, 'HEIGTH': 0.03}
	pGUICreator.ButtonCreator.CreateYesNoButton("Show Grid", None, __name__ + ".HandleMapBars", 1, pActW, SGButtonDict, SGButtonDict)		

	WarpButtonDict = {'X': 0.025, 'Y': 0.03, 'WIDTH': 0.15, 'HEIGTH': 0.03}
	pWarpButton = pGUICreator.ButtonCreator.CreateButton("Engage", None, __name__ + ".WarpClick", 1, pTraW, WarpButtonDict, WarpButtonDict)
	pWarpButton.SetDisabled()

	DropButtonDict = {'X': 0.025, 'Y': 0.07, 'WIDTH': 0.15, 'HEIGTH': 0.03}
	pDropOut = pGUICreator.ButtonCreator.CreateButton("Drop Out Of Travel", None, __name__ + ".DropOutClick", 1, pTraW, DropButtonDict, DropButtonDict)
	pDropOut.SetDisabled()

	SWSButtonDict = {'X': 0.025, 'Y': 0.11, 'WIDTH': 0.15, 'HEIGTH': 0.03}
	pSTSButton = pGUICreator.ButtonCreator.CreateButton("Select Travel Speed", None, "Custom.NanoFXv2.WarpFX.WarpFX_GUI.Window", 1, pTraW, SWSButtonDict, SWSButtonDict)

	BarButtonDict = {'X': 0.01, 'Y': 0.01, 'WIDTH': 0.3, 'HEIGTH': 0.03}
	pScaleBar = pGUICreator.ButtonCreator.CreateBar("Map Zoom", None, __name__+".ZoomBarUpdate", 100000.0, [100.0, 100000.0], 100000.0, 0, pActW, BarButtonDict, BarButtonDict)
	pScaleBar.SetKeyInterval(0.1)

	PVButton1Dict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.14, 'HEIGTH': 0.025}
	pGUICreator.ButtonCreator.CreateButton("Alpha Quadrant", None, __name__+".PresetViewsClick", 1, pPVW, PVButton1Dict, PVButton1Dict)
	PVButton1Dict = {'X': 0.0, 'Y': 0.026, 'WIDTH': 0.14, 'HEIGTH': 0.025}
	pGUICreator.ButtonCreator.CreateButton("Beta Quadrant", None, __name__+".PresetViewsClick", 2, pPVW, PVButton1Dict, PVButton1Dict)
	PVButton1Dict = {'X': 0.0, 'Y': 0.052, 'WIDTH': 0.14, 'HEIGTH': 0.025}
	pGUICreator.ButtonCreator.CreateButton("Delta Quadrant", None, __name__+".PresetViewsClick", 3, pPVW, PVButton1Dict, PVButton1Dict)
	PVButton1Dict = {'X': 0.0, 'Y': 0.078, 'WIDTH': 0.14, 'HEIGTH': 0.025}
	pGUICreator.ButtonCreator.CreateButton("Gamma Quadrant", None, __name__+".PresetViewsClick", 4, pPVW, PVButton1Dict, PVButton1Dict)
	PVButton1Dict = {'X': 0.0, 'Y': 0.104, 'WIDTH': 0.14, 'HEIGTH': 0.025}
	pGUICreator.ButtonCreator.CreateButton("Known Space", None, __name__+".PresetViewsClick", 5, pPVW, PVButton1Dict, PVButton1Dict)
	PVButton1Dict = {'X': 0.0, 'Y': 0.13, 'WIDTH': 0.14, 'HEIGTH': 0.025}
	pGUICreator.ButtonCreator.CreateButton("Maelstrom", None, __name__+".PresetViewsClick", 6, pPVW, PVButton1Dict, PVButton1Dict)

	pPVW.SetUseScrolling(1)
	pPVW.SetScrollViewHeight(25.0)

	# Create the map background
	HandleMapBackground()
	# Create the regions icons
	CreateRegionIcons()
	# As the "Show Names of All Regions" starts as selected, let already create all of the region icons
	SOIClick(None, None)


def HandleMapBackground():
	debug(__name__ + ", HandleMapBackground")
	if pGUICreator == None:
		return
	pGM = pGUICreator.GetElement("Galaxy Map")
	if pGM == None:
		return
	pIcon = pGUICreator.IconCreator.GetIcon("Back-MilkyWay")
	if pIcon == None:
		pGUICreator.IconCreator.SetInfoForIcon("Back-MilkyWay", GALAXY_ICONS, ICON_MILKYWAY, Pos_MAP_X, Pos_MAP_Y)
		pIcon = pGUICreator.IconCreator.CreateIcon("Back-MilkyWay", pGM)
	else:
		pIcon.SetPosition(Pos_MAP_X, Pos_MAP_Y)
	pIcon.Resize(MAP_W, MAP_H)
	pGUICreator.IconCreator.ShowIcon("Back-MilkyWay")
	HandleMapBars()
	return pIcon

lCreatedBarNames = []
def HandleMapBars(pObject = None, pEvent = None):
	# we have those args here because this function can be called like usual "name()", or by a event handler,
	# which also happens, because when pressing the 'Show Grid' YesNo button this function will be called.
	# as so, we need those args to work like a event handler as well, but we wont use, also there isn't a need
	# to call the next handler here because we are (and should be) the only handler.
	debug(__name__ + ", HandleMapBars")
	global lCreatedBarNames
	if pGUICreator == None:
		return
	pGridLayer = pGUICreator.GetElement("GM Layer: Grid")
	pShowGrid = pGUICreator.ButtonCreator.GetButtonByName("Show Grid")
	if pGridLayer == None or pShowGrid == None:
		return
	
	bUseBars = pShowGrid.IsChosen()
	if bUseBars == 0:
		# don't show grid, delete the icons and update the icon bar names list
		for sCreatedBarName in lCreatedBarNames:
			pGUICreator.IconCreator.DeleteIcon(sCreatedBarName)
		lCreatedBarNames = []
		return
	
	# bUseBars = 1, so we create/update the icons.

	# okay, first we get the amount of lightyears the user is seeing at the map
	# from it we get the ratio of 'squares' that the grid would have.
	# that's because the bigger the zoom, the smaller the grid needs to be, so that it is usefull  lol
	fDiameter = (100000.0/MAP_W)*Real_MAP_W
	if fDiameter > 50000.0:  
		fRatio = 10             # show 10000 ly  areas
	elif fDiameter > 10000.0:   
		fRatio = 20             # show 5000 ly areas
	elif fDiameter > 5000.0:
		fRatio = 100            # show 1000 ly areas
	elif fDiameter > 1000.0:
		fRatio = 200            # show 500 ly areas
	elif fDiameter > 500.0:
		fRatio = 500            # show 200 ly areas
	else:
		fRatio = 5000     # show sectors (20ly size)

	# now we get all 'in-screen' horizontal and vertical grid bar coordinates, and store them.
	lHorPos = []
	lVerPos = []
	for i in range(fRatio):
		index = i #+ 1
		GalPosX = ( (100000.0 / fRatio ) * index ) - 50000.0
		GalPosY = GalPosX
		
		PosX, PosY = ((GalPosX+50000.0)/100000.0) *MAP_W + Pos_MAP_X, ((GalPosY+50000.0)/100000.0) *MAP_H + Pos_MAP_Y

		if PosX >= 0.0 and PosX <= Real_MAP_W:
			lVerPos.append(PosX)
		if PosY >= 0.0 and PosY <= Real_MAP_H:
			lHorPos.append(PosY)

	lBarNames = []   # this list will store the bar names we created now.

	# now we create the horizontal bars, using the coordinates from the above acquired list
	iHorIndex = 0
	for fH_Pos in lHorPos:
		iHorIndex = iHorIndex + 1
		sBarName = "HorBar"+str(iHorIndex)
		BAR_H = 0.001
		HorX = 0
		HorY = fH_Pos
		lBarNames.append(sBarName)
		pHorIcon = pGUICreator.IconCreator.GetIcon(sBarName)
		if pHorIcon == None:
			pGUICreator.IconCreator.SetInfoForIcon(sBarName, GALAXY_ICONS, ICON_HORIZONTAL_BAR, HorX, HorY, Real_MAP_W, BAR_H)
			pHorIcon = pGUICreator.IconCreator.CreateIcon(sBarName, pGridLayer)
		else:
			pHorIcon.SetPosition(HorX, HorY)

	# same as above but for the vertical bars.
	iVerIndex = 0
	for fV_Pos in lVerPos:
		iVerIndex = iVerIndex + 1
		sBarName = "VerBar"+str(iVerIndex)
		BAR_W = 0.001
		VerX = fV_Pos
		VerY = 0
		lBarNames.append(sBarName)
		pVerIcon = pGUICreator.IconCreator.GetIcon(sBarName)
		if pVerIcon == None:
			pGUICreator.IconCreator.SetInfoForIcon(sBarName, GALAXY_ICONS, ICON_VERTICAL_BAR, VerX, VerY, BAR_W, Real_MAP_H)
			pVerIcon = pGUICreator.IconCreator.CreateIcon(sBarName, pGridLayer)
		else:
			pVerIcon.SetPosition(VerX, VerY)

	# now we discover which bars were created before, but not now, and delete them.
	for sCreatedBarName in lCreatedBarNames:
		if not sCreatedBarName in lBarNames:
			pGUICreator.IconCreator.DeleteIcon(sCreatedBarName)
	# and finally we reset the last created bars names.
	lCreatedBarNames = lBarNames
	# maybe the following will fix the flickering of the bars.... >_<
	for sBarName in lBarNames:
		pGUICreator.IconCreator.ShowIcon(sBarName)
	return

def CreateRegionIcons():
	debug(__name__ + ", CreateRegionIcons")
	global pPlayerRegion, pSelectedRegion, bWasRegionsCreated
	if bWasRegionsCreated == 1 or pGUICreator == None:
		return
	pRLayer = pGUICreator.GetElement("GM Layer: Regions")
	lRegions = GetAllRegions()
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = None
	if pPlayer:
		pSet = pPlayer.GetContainingSet()
		if pSet:
			pPlayerRegion = pSet.GetRegion()
	pEndCombatB = GetSTButton("End Combat")
	if pEndCombatB != None:
		bEndComS = pEndCombatB.IsEnabled()
	else:
		bEndComS = 1
	bIsMult = App.g_kUtopiaModule.IsMultiplayer()
	for pRegion in lRegions:
		bCanContinue = 1
		if pRegion.GetOnlyInQB() == 1:
			bCanContinue = bEndComS
		if pRegion.GetOnlyMult() == 1:
			bCanContinue = bIsMult
		if bCanContinue == 1:
			pLoc = pRegion.GetLocation()
			if pLoc == "DEFAULT":
				# Region doesn't have a location set... So just set the location of it as something that after the
				# X Y equation will make the icon appear off screen, so that the region isn't showed.
				pLoc = App.NiPoint2(100000.0, 100000.0)
			X, Y = ((pLoc.x+50000.0)/100000.0) *MAP_W + Pos_MAP_X, ((pLoc.y+50000.0)/100000.0) *MAP_H + Pos_MAP_Y
			nSize = 0.01
			pIcon = pGUICreator.IconCreator.GetIcon(pRegion.Name)
			if pIcon:
				pIcon.SetPosition(X-(nSize/2), Y-(nSize/2))
			else:
				pIcon = CreateIcon(pRegion.Name, ICON_REGION, X, Y, nSize, pRLayer, 1)
			pColor = GetColorForRegion(pRegion)
			if pPlayerRegion:
				if pRegion.Name == pPlayerRegion.Name:
					pColor = COLOR_PLAYER
			if pRegion.Region == GetPlayerWarpDestination() and pRegion.Name != pPlayerRegion.Name:
				pSelectedRegion = pRegion
				pColor = COLOR_SELECTED
			elif GetPlayerSubSet() == GetPlayerWarpDestination() and pRegion.Name == pPlayerRegion.Name:
				SetPlayerWarpDestination(None)
			pIcon.SetColor(pColor)
	CreateSubSetButtons()
	UpdateInformation()
	bWasRegionsCreated = 1

def UpdateRegionPositions():
	debug(__name__ + ", UpdateRegionPositions")
	if pGUICreator == None:
		return
	lRegions = GetAllRegions()
	for pRegion in lRegions:
		pLoc = pRegion.GetLocation()
		if pLoc == "DEFAULT":
			# Region doesn't have a location set... So just set the location of it as something that after the
			# X Y equation will make the icon appear off screen, so that the region isn't showed.
			pLoc = App.NiPoint2(100000.0, 100000.0)
		X, Y = ((pLoc.x+50000.0)/100000.0) * MAP_W + Pos_MAP_X, ((pLoc.y+50000.0)/100000.0) * MAP_H + Pos_MAP_Y
		nSize = 0.01
		pIcon = pGUICreator.IconCreator.GetIcon(pRegion.Name)
		if pIcon != None:
			pIcon.SetPosition(X-(nSize/2), Y-(nSize/2))
			pCTACo = GetColorForRegion(pRegion)  #CTACo - Color To Apply Correctly
			pColor = App.TGColorA()
			pIcon.GetColor(pColor)
			if pColor.GetR() != pCTACo.GetR() or pColor.GetG() != pCTACo.GetG() or pColor.GetB() != pCTACo.GetB():
				pIcon.SetColor(  pCTACo  )


def DeleteRegionIcons():
	debug(__name__ + ", DeleteRegionIcons")
	global pPlayerRegion, pSelectedRegion, bWasRegionsCreated, lSubSetsNames, sOldPlayerReg, sSelectedSubSet, lCreatedBarNames
	if bWasRegionsCreated == 0 or pGUICreator == None:
		return		
	lRegions = GetAllRegions()
	for pRegion in lRegions:
		pGUICreator.IconCreator.DeleteIcon(pRegion.Name)
	pPlayerRegion = None
	pSelectedRegion = None
	sSelectedSubSet = None
	sOldPlayerReg = 0
	for sName in lSubSetsNames:
		pGUICreator.ButtonCreator.DeleteButtonByName(sName)
	lSubSetsNames = []
	bWasRegionsCreated = 0
	pGUICreator.IconCreator.DeleteIcon("Back-MilkyWay")
	for sCreatedBarName in lCreatedBarNames:
		pGUICreator.IconCreator.DeleteIcon(sCreatedBarName)
	lCreatedBarNames = []
	#UpdateInformation()

def CreateSubSetButtons():
	debug(__name__ + ", CreateSubSetButtons")
	global pPlayerRegion, lSubSetsNames, sOldPlayerReg, sSelectedSubSet
	if pGUICreator == None:
		return
	if pPlayerRegion:
		if sOldPlayerReg == 0:
			sOldPlayerReg = pPlayerRegion.Name
		if pPlayerRegion.Name != sOldPlayerReg:
			for sName in lSubSetsNames:
				pGUICreator.ButtonCreator.DeleteButtonByName(sName)
			lSubSetsNames = []
			sOldPlayerReg = pPlayerRegion.Name
		pSubSetW = pGUICreator.GetElement("Sub-Sets")
		fSubSetY = 0.05
		fSubSetH = 0.03
		if len(pPlayerRegion.Systems) <= 1:
			return
		for sSystem in pPlayerRegion.Systems:
			sSystemName = string.split(sSystem, ".")[-1]
			if not sSystemName in lSubSetsNames:
				SSButtonDict = {'X': 0.0, 'Y': fSubSetY, 'WIDTH': 0.3, 'HEIGTH': fSubSetH}
				bIsChosen = int(sSystem == GetPlayerWarpDestination())
				if bIsChosen == 1:
					sSelectedSubSet = sSystem
				pButton = pGUICreator.ButtonCreator.CreateYesNoButton(sSystemName, None, __name__ + ".SubSetClick", bIsChosen, pSubSetW, SSButtonDict, SSButtonDict)
				if sSystem == GetPlayerSubSet():
					pButton.SetDisabled()
				fSubSetY = fSubSetY + fSubSetH + 0.004
				lSubSetsNames.append(sSystemName)
			else:
				pButton = pGUICreator.ButtonCreator.GetButtonByName(sSystemName)
				if pButton:
					if sSystem == GetPlayerSubSet():
						if pButton.IsEnabled() == 1:
							pButton.SetDisabled()
					else:
						if pButton.IsEnabled() == 0:
							pButton.SetEnabled()

def SOIClick(pObject, pEvent):
	debug(__name__ + ", SOIClick")
	global ShowAllNames, InfoNamesList
	if pGUICreator == None:
		return
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Show All Names of All Regions")
	pILayer = pGUICreator.GetElement("GM Layer: Info")
	pPlayer = App.Game_GetCurrentPlayer()
	if pButton and pPlayer:
		if pButton.IsChosen():
			ShowAllNames = 1
			lRegions = GetAllRegions()
			pPlayerSet = pPlayer.GetContainingSet()
			for pRegion in lRegions:
				if pRegion.Name == "SpaceSet":
					sList = ["Player Location"]
				elif pPlayerSet and IsPlayerWarping() and pRegion.Name == pPlayerSet.GetRegion().GetName():
					sList = ["Player (Travelling)"]
				else:
					sList = [pRegion.Name]
				pPara = pGUICreator.GetElement(pRegion.Name+"RegionInfo")
				pIcon = pGUICreator.IconCreator.GetIcon(pRegion.Name)
				if pIcon:
					pPOS = App.NiPoint2(0,0)
					pIcon.GetPosition(pPOS)
					X, Y = pPOS.x+pIcon.GetWidth(), pPOS.y
					if pPara == None:
						pGUICreator.SetInfoForName(pRegion.Name+"RegionInfo", X, Y)
						pGUICreator.CreateParagraph(pRegion.Name+"RegionInfo", sList, pILayer)
					else:
						pGUICreator.UpdateParagraph(pRegion.Name+"RegionInfo", sList)
						pPara.SetPosition(X, Y)
					InfoNamesList.append(pRegion.Name+"RegionInfo")
			pRIPara = pGUICreator.GetElement("RegionInfo")
			if pRIPara != None:	
				pGUICreator.DeleteElement("RegionInfo")
		else:
			ShowAllNames = 0
			for sName in InfoNamesList:
				pGUICreator.DeleteElement(sName)
			InfoNamesList = []

def SubSetClick(pObject, pEvent):
	debug(__name__ + ", SubSetClick")
	global lSubSetsNames, pPlayerRegion, sSelectedSubSet, pSelectedRegion
	if pGUICreator == None:
		return
	pButton = pGUICreator.ButtonCreator.GetButtonByID(pEvent.GetSource().GetObjID())
	if pButton:
		if pButton.IsChosen():
			sSystemName = ""
			for sName in lSubSetsNames:
				pSubButt = pGUICreator.ButtonCreator.GetButtonByName(sName)
				if pSubButt and pSubButt.GetObjID() == pButton.GetObjID():
					sSystemName = sName
				elif pSubButt:
					pSubButt.SetChosen(0)
			if pPlayerRegion:
				sSelectedSubSet = pPlayerRegion.GetModuleOfSystem(sSystemName)
				SetPlayerWarpDestination(sSelectedSubSet)
				if pSelectedRegion:		
					pSelIcon = pGUICreator.IconCreator.GetIcon(pSelectedRegion.Name)
					pSelectedRegion = None
					if pSelIcon:
						pSelColor = GetColorForRegion(pRegion)
						pSelIcon.SetColor(pSelColor)
		else:
			SetPlayerWarpDestination(pSelectedRegion)
			sSelectedSubSet = None
		UpdateInformation()

# This function is called by both the galaxy map GUI's Warp button and the Helm's Warp button.
# So take care in modifying it. Also, make sure that "pObject.CallNextHandler(pEvent)" IS NOT CALLED!
# If it is, and the user press the Helm Warp button, it will cause problems...
def WarpClick(pObject, pEvent):
	debug(__name__ + ", WarpClick")
	sDestination = GetPlayerWarpDestination()
	if sDestination != "" and HelmAddonGUI.sSelectedTravelType != "None" and pGUICreator != None:
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			if IsPlayerWarping() == 1:
				App.g_kTravelManager.ChangeDestinationOfShip(pPlayer, sDestination)
			else:
				oResult = App.g_kTravelManager.EngageTravelToOfShip(pPlayer, sDestination, HelmAddonGUI.sSelectedTravelType)
				if oResult == 1:
					GMClose(None, None)
					pButton = pGUICreator.ButtonCreator.GetButtonByName("Engage")
					if pButton:
						pButton.SetDisabled()
				else:
					pGUICreator.CreateMessageBox("Traveler System Message", "Sorry Captain but our ship could not engage travel. According to our computer the reason is as follows: \n\n"+oResult )

def DropOutClick(pObject, pEvent):
	debug(__name__ + ", DropOutClick")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer:
		pTravel = App.g_kTravelManager.GetTravel(pPlayer)
		if pTravel.Started == 1:
			pTravel.DropOutOfTravel()
			# Traveler will force the tactical view, and before that, dropping all bridge menus and making the
			# characters turn back when dropping out of travel. So if the user had any menu/window opened,
			# it'll be closed. And as this GUI makes a full update when it is opened, don't need to worry about
			# updating here.

def SystemAnalysis(pObject, pEvent):
	debug(__name__ + ", SystemAnalysis")
	global pSelectedRegion
	SystemAnalysisGUI.CreateSAGUI(pSelectedRegion)

def ZoomBarUpdate(pObject, pEvent):
	debug(__name__ + ", ZoomBarUpdate")
	global MAP_W, MAP_H, Pos_MAP_X, Pos_MAP_Y
	if pGUICreator == None:
		return
	pActW = pGUICreator.GetElement("Actions")
	pBar = pGUICreator.ButtonCreator.GetButtonByName("Map Zoom")
	if pBar:
		fValue = pBar.GetValue()
		MAP_W = (100000.0/fValue)*Real_MAP_W
		MAP_H = (100000.0/fValue)*Real_MAP_H

		pLoc = None
		X, Y = 0,0
		if pPlayerRegion:
			pLoc = pPlayerRegion.GetLocation()
			if pLoc == "DEFAULT":
				# Region doesn't have a location set... So just set the location of it as something that after the
				# X Y equation will make the icon appear off screen, so that the region isn't showed.
				pLoc = App.NiPoint2(100000.0, 100000.0)
			X, Y = ((pLoc.x+50000.0)/100000.0) * MAP_W + Pos_MAP_X, ((pLoc.y+50000.0)/100000.0) * MAP_H + Pos_MAP_Y

		if pLoc != None:
			iCenterX = Real_MAP_W / 2
			iCenterY = Real_MAP_H / 2
			iPosX = X - Pos_MAP_X
			iPosY = Y - Pos_MAP_Y
			Pos_MAP_X = iCenterX - iPosX
			Pos_MAP_Y = iCenterY - iPosY

		if Pos_MAP_Y + MAP_H < Real_MAP_H:
			Pos_MAP_Y = Real_MAP_H-MAP_H
		if Pos_MAP_Y > 0.0:
			Pos_MAP_Y = 0.0
		if Pos_MAP_X + MAP_W < Real_MAP_W:
			Pos_MAP_X = Real_MAP_W-MAP_W
		if Pos_MAP_X > 0.0:
			Pos_MAP_X = 0.0

		HandleMapBackground()
		UpdateRegionPositions()
		SOIClick(None, None)
	else:
		fValue = 100000.0

	HandleScalePara()
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def PresetViewsClick(pObject, pEvent):
	debug(__name__ + ", PresetViewsClick")
	global Pos_MAP_X, Pos_MAP_Y, MAP_W, MAP_H, Real_MAP_W, Real_MAP_H
	try:
		iCode = pEvent.GetInt()
	except:
		return
	if iCode in [1, 2, 3, 4]:
		MAP_W = 2.0*Real_MAP_W
		MAP_H = 2.0*Real_MAP_H

	if iCode == 1:     # ALPHA Quadrant
		Pos_MAP_X = 0.0
		Pos_MAP_Y = -(MAP_H / 2.0)

	elif iCode == 2:     # BETA Quadrant
		Pos_MAP_X = -(MAP_W / 2.0)
		Pos_MAP_Y = -(MAP_H / 2.0)

	elif iCode == 3:     # DELTA Quadrant
		Pos_MAP_X = -(MAP_W / 2.0)
		Pos_MAP_Y = 0.0

	elif iCode == 4:     # GAMMA Quadrant
		Pos_MAP_X, Pos_MAP_Y = 0.0, 0.0

	elif iCode == 5:     # Known Space      (known region of space near Earth (Sol)
		MAP_W = 66.6666666666*Real_MAP_W
		MAP_H = 66.6666666666*Real_MAP_H
		SolPosX = 0.0
		SolPosY = 25800.0
		X, Y = ((SolPosX+50000.0)/100000.0) * MAP_W + Pos_MAP_X, ((SolPosY+50000.0)/100000.0) * MAP_H + Pos_MAP_Y
		iCenterX = Real_MAP_W / 2
		iCenterY = Real_MAP_H / 2
		iPosX = X - Pos_MAP_X
		iPosY = Y - Pos_MAP_Y
		Pos_MAP_X = iCenterX - iPosX
		Pos_MAP_Y = iCenterY - iPosY

	elif iCode == 6:     # Maelstrom    stock BC's campaign space sector
		MAP_W = 1000.0*Real_MAP_W
		MAP_H = 1000.0*Real_MAP_H
		# Beol is located pratically at the center of the Maelstrom, so we'll use it as a reference point
		MCPosX = -90.0
		MCPosY = 25869.0
		X, Y = ((MCPosX+50000.0)/100000.0) * MAP_W + Pos_MAP_X, ((MCPosY+50000.0)/100000.0) * MAP_H + Pos_MAP_Y
		iCenterX = Real_MAP_W / 2
		iCenterY = Real_MAP_H / 2
		iPosX = X - Pos_MAP_X
		iPosY = Y - Pos_MAP_Y
		Pos_MAP_X = iCenterX - iPosX
		Pos_MAP_Y = iCenterY - iPosY

	# Now update the GUI 
	UpdateGUI()
	pActW = pGUICreator.GetElement("Actions")
	pBar = pGUICreator.ButtonCreator.GetButtonByName("Map Zoom")
	if pBar != None:
		pBar.Resize(0.3, 0.03, 0)
		if iCode == 5:
			pBar.SetValue(1500.0)
		elif iCode == 6:
			pBar.SetValue(100.0)
		else:
			pBar.SetValue(50000.0)
		pBar.UpdateGauge()
		HandleScalePara()
		pActW.InteriorChangedSize()
		pActW.Layout()
	if pObject != None and pEvent != None:
		pObject.CallNextHandler(pEvent)

def HandleScalePara():
	debug(__name__ + ", HandleScalePara")
	if pGUICreator == None:
		return
	pActW = pGUICreator.GetElement("Actions")
	if pActW == None:
		return
	pBar = pGUICreator.ButtonCreator.GetButtonByName("Map Zoom")
	if pBar != None:
		fValue = pBar.GetValue()
	else:
		fValue = 100000.0

	fDiameter = (100000.0/MAP_W)*Real_MAP_W
	if fDiameter > 50000.0:  
		sGridSize = '10000'             # show 10000 ly  areas
	elif fDiameter > 10000.0:   
		sGridSize = '5000'             # show 5000 ly areas
	elif fDiameter > 5000.0:
		sGridSize = '1000'            # show 1000 ly areas
	elif fDiameter > 1000.0:
		sGridSize = '500'            # show 500 ly areas
	elif fDiameter > 500.0:
		sGridSize = '200'            # show 200 ly areas
	else:
		sGridSize = '20 (1 sector)'   # show sectors (20ly size)

	sList = ["Map Width (<->): "+GetStrFromFloat(fValue)+" lightyears"]
	sList.append("Grid Width (<->): "+sGridSize+" lightyears")
	pPara = pGUICreator.GetElement("Scale Para")
	if pPara == None:
		pGUICreator.SetInfoForName("Scale Para", 0.35, 0.01)
		pPara = pGUICreator.CreateParagraph("Scale Para", sList, pActW)
	else:
		pGUICreator.UpdateParagraph("Scale Para", sList)

# Master update function. Only thing that may possibly update the GUI better than this functions is the reinitialization
# of the GUI  (that is, closing and opening it again)
def UpdateGUI():
	debug(__name__ + ", UpdateGUI")
	if pGUICreator == None:
		return
	pGM = pGUICreator.GetElement("Galaxy Map")
	if pGM == None:
		return
	UpdateInformation()
	HandleMapBackground()
	UpdateRegionPositions()
	SOIClick(None, None)

def UpdateInformation():
	debug(__name__ + ", UpdateInformation")
	global pPlayerRegion, pSelectedRegion, sSelectedSubSet
	if pGUICreator == None:
		return
	pInfoW = pGUICreator.GetElement("Information")
	pPara = pGUICreator.GetElement("InformationParag")
	if pInfoW == None:
		return
	sList = []
	if IsPlayerWarping() == 1:
		sList.append("Current Region: TRAVELLING")
	elif pPlayerRegion:
		sList.append("Current Region: "+pPlayerRegion.Name)
		sList.append("Current Sub-Set: "+string.split(GetPlayerSubSet(), ".")[-1])
	else:
		sList.append("Current Region: NONE")
	if sSelectedSubSet:
		sList.append("Selected Sub-Set: "+string.split(sSelectedSubSet, ".")[-1])
	elif pSelectedRegion:
		sList.append("Selected Region: "+pSelectedRegion.Name)
	else:
		sList.append("Selected Region: NONE")
	pPlayer = App.Game_GetCurrentPlayer()
	if pSelectedRegion != None:
		if GalacticWarSimulator.WarSimulator.IsInitialized() == 1 and pPlayer != None:
			sEmpire = pSelectedRegion.GetControllingEmpire()
			if GetRaceClassObj(sEmpire) != None:
				if IsShipFriendlyOfRace(pPlayer, sEmpire) == 1 or GetShipRace(pPlayer) == sEmpire:
					sList.append("Destination is: ALLIED")
				elif IsShipEnemyOfRace(pPlayer, sEmpire) == 1:
					sList.append("Destination is: HOSTILE")
				else:
					sList.append("Destination is: NEUTRAL")
			else:
				sList.append("Destination is: NEUTRAL")
	sSpeedString = "Didn't acquire speed..."
	fRealSpeed = None
	if pPlayer != None:
		pTravel = App.g_kTravelManager.GetTravel(pPlayer)
		if pTravel != None:
			sSpeedString = pTravel.GetTravelType()+" Speed: "+str(pTravel.GetSpeed())
			fRealSpeed = pTravel.GetRealSpeed()
	sList.append(sSpeedString)
	if pPlayerRegion and sSelectedSubSet:
		iDist = pPlayerRegion.GetDistanceBetweenSystems(GetPlayerSubSet(), sSelectedSubSet)
		dWarpValues = Galaxy.GetWarpValues(iDist, fRealSpeed)
		sList.append("Distance: "+GetStrFromFloat(iDist)+" lightyears")
		lsTimes = GetTimeStrings(dWarpValues['Time'])
		for sTimeValue in lsTimes:
			sList.append(sTimeValue)
	elif pPlayerRegion and pSelectedRegion:
		vWasLoc = pPlayerRegion.GetLocation()
		vGoLoc = pSelectedRegion.GetLocation()
		if vWasLoc != "DEFAULT" and vGoLoc != "DEFAULT":
			vDist = App.NiPoint2(vGoLoc.x - vWasLoc.x, vGoLoc.y - vWasLoc.y)
			iDist = vDist.Length()
			dWarpValues = Galaxy.GetWarpValues(iDist, fRealSpeed)
			sList.append("Distance: "+GetStrFromFloat(iDist)+" lightyears")
			lsTimes = GetTimeStrings(dWarpValues['Time'])
			for sTimeValue in lsTimes:
				sList.append(sTimeValue)
		else:
			sList.append("Player or Selected region Location is none")
	if pPara == None:
		pGUICreator.SetInfoForName("InformationParag", 0, 0)
		pGUICreator.CreateParagraph("InformationParag", sList, pInfoW)
	else:
		pGUICreator.UpdateParagraph("InformationParag", sList)
		pPara.SetPosition(0, 0)
	CreateSubSetButtons()
	UpdateWarpButtonStatus()

def MouseHandler(pObject, pEvent):
	debug(__name__ + ", MouseHandler")
	global ShowAllNames, pPlayerRegion, pSelectedRegion, sSelectedSubSet
	pObject.CallNextHandler(pEvent)
	if pGUICreator == None:
		return
	if pEvent.EventHandled() == 0:
		pEvent.SetHandled()
	
	MouseX = pEvent.GetX()
	MouseY = pEvent.GetY()
	lRegions = GetAllRegions()
	pMouseOverReg = None
	pMouseOverIcon = None
	for pRegion in lRegions:
		pPOS = App.NiPoint2(0,0)
		pIcon = pGUICreator.IconCreator.GetIcon(pRegion.Name)
		if pIcon:
			pIcon.GetPosition(pPOS)
			X, Y = pPOS.x, pPOS.y
			EndX, EndY = X+pIcon.GetWidth(), Y+pIcon.GetHeight()
			if X <= MouseX <= EndX and Y <= MouseY <= EndY:
				pMouseOverReg = pRegion
				pMouseOverIcon = pIcon
				if ShowAllNames == 0:
					ShowInfoOnRegion(pRegion, EndX, Y)
	if pMouseOverReg == None:
		ShowInfoOnRegion(None, 0, 0)

	if pEvent.IsButtonEvent():
		nNum = pEvent.GetButtonNum()
		if nNum == App.TGMouseEvent.MEF_BUTTON_LEFT and pPlayerRegion:
			if pMouseOverReg and pMouseOverReg.Name != pPlayerRegion.Name and pSelectedRegion and pSelectedRegion.Name != pMouseOverReg.Name:
				pSelIcon = pGUICreator.IconCreator.GetIcon(pSelectedRegion.Name)
				if pSelIcon:
					pSelColor = GetColorForRegion(pRegion, pMouseOverReg)
					pSelIcon.SetColor(pSelColor)
				pColor = GetColorForRegion(pRegion, pMouseOverReg)
				pMouseOverIcon.SetColor(pColor)
				pSelectedRegion = pMouseOverReg
				SetPlayerWarpDestination(pSelectedRegion)
				if sSelectedSubSet:
					pButton = pGUICreator.ButtonCreator.GetButtonByName(string.split(sSelectedSubSet, ".")[-1])
					if pButton:
						pButton.SetChosen(0)
				sSelectedSubSet = None
				UpdateInformation()
				UpdateRegionPositions()
			elif pMouseOverReg and pMouseOverReg.Name != pPlayerRegion.Name:
				pColor = GetColorForRegion(pRegion, pMouseOverReg)
				pMouseOverIcon.SetColor(pColor)
				pSelectedRegion = pMouseOverReg
				SetPlayerWarpDestination(pSelectedRegion)
				if sSelectedSubSet:
					pButton = pGUICreator.ButtonCreator.GetButtonByName(string.split(sSelectedSubSet, ".")[-1])
					if pButton:
						pButton.SetChosen(0)
				sSelectedSubSet = None
				UpdateInformation()
				UpdateRegionPositions()
		elif nNum == App.TGMouseEvent.MEF_BUTTON_RIGHT:
			if pSelectedRegion:		
				pSelIcon = pGUICreator.IconCreator.GetIcon(pSelectedRegion.Name)
				pSelectedRegion = None
				if pSelIcon:
					pSelColor = GetColorForRegion(pRegion)
					pSelIcon.SetColor(pSelColor)
				SetPlayerWarpDestination(None)
			if sSelectedSubSet:
				pButton = pGUICreator.ButtonCreator.GetButtonByName(string.split(sSelectedSubSet, ".")[-1])
				if pButton:
					pButton.SetChosen(0)
				sSelectedSubSet = None
			UpdateInformation()
			UpdateRegionPositions()

def KeyHandler(pObject, pEvent):
	debug(__name__ + ", KeyHandler")
	global Pos_MAP_X, Pos_MAP_Y
	bWasMoved = 0
	# check for if arrow keys are pressed, and move the galaxy icon position accordingly
	eUni = pEvent.GetUnicode()
	if eUni == App.WC_UP:
		Pos_MAP_Y = Pos_MAP_Y + 0.01
		bWasMoved = 1
	elif eUni == App.WC_DOWN:
		Pos_MAP_Y = Pos_MAP_Y - 0.01
		bWasMoved = 1
	elif eUni == App.WC_LEFT:
		Pos_MAP_X = Pos_MAP_X + 0.01
		bWasMoved = 1
	elif eUni == App.WC_RIGHT:
		Pos_MAP_X = Pos_MAP_X - 0.01
		bWasMoved = 1

	# now safety check: see if the galaxy is inside the screen, and if it isn't, put it in the screen :P
	if Pos_MAP_Y + MAP_H < Real_MAP_H:
		Pos_MAP_Y = Real_MAP_H-MAP_H
	if Pos_MAP_Y > 0.0:
		Pos_MAP_Y = 0.0
	if Pos_MAP_X + MAP_W < Real_MAP_W:
		Pos_MAP_X = Real_MAP_W-MAP_W
	if Pos_MAP_X > 0.0:
		Pos_MAP_X = 0.0

	# and then update the map if it was moved.
	if bWasMoved == 1:
		HandleMapBackground()
		UpdateRegionPositions()
		SOIClick(None, None)

	pObject.CallNextHandler(pEvent)

def MsgBoxOK(pObject, pEvent):
	debug(__name__ + ", MsgBoxOK")
	pTop = App.TopWindow_GetTopWindow()
	if pTop:
		pTop.ToggleBridgeAndTactical()
		pTop.ToggleBridgeAndTactical()
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def UpdateWarpButtonStatus():
	debug(__name__ + ", UpdateWarpButtonStatus")
	global pPlayerRegion, pSelectedRegion, sSelectedSubSet
	if pGUICreator == None:
		return
	pPlayer = App.Game_GetCurrentPlayer()
	pButton = pGUICreator.ButtonCreator.GetButtonByName("Engage")
	pDropOut = pGUICreator.ButtonCreator.GetButtonByName("Drop Out Of Travel")
	if pButton and pDropOut:
		pName = App.TGString("")
		pButton.GetName(pName)
		sName = pName.GetCString()
		if IsPlayerWarping() == 1:
			if pSelectedRegion != None:
				pButton.SetEnabled()
				if sName != "Change Destination":
					pButton.SetName(App.TGString("Change Destination"))
			else:
				pButton.SetDisabled()
			bCanDropOut = 1
			if pPlayer != None:
				pTravel = App.g_kTravelManager.GetTravel(pPlayer)
				if pTravel != None:
					 bCanDropOut = pTravel.CanDropOut()
			if bCanDropOut == 1:
				pDropOut.SetEnabled()
			else:
				pDropOut.SetDisabled()
		elif HelmAddonGUI.sSelectedTravelType == "None":
			pButton.SetDisabled()
			if sName != "Engage":
				pButton.SetName(App.TGString("Engage"))
			pDropOut.SetDisabled()
		elif GetPlayerSubSet() != None and sSelectedSubSet != None:
			pButton.SetEnabled()
			if sName != "Engage":
				pButton.SetName(App.TGString("Engage"))
			pDropOut.SetDisabled()
		elif pPlayerRegion == None or pSelectedRegion == None:
			pButton.SetDisabled()
			if sName != "Engage":
				pButton.SetName(App.TGString("Engage"))
			pDropOut.SetDisabled()
		elif pPlayerRegion != None and pSelectedRegion != None:
			pButton.SetEnabled()
			if sName != "Engage":
				pButton.SetName(App.TGString("Engage"))
			pDropOut.SetDisabled()


def UpdateSelectSpeedButtons(bEnable):
	debug(__name__ + ", UpdateSelectSpeedButtons")
	if pGUICreator == None:
		return
	pSTSButton = pGUICreator.ButtonCreator.GetButtonByName("Select Travel Speed")
	if pSTSButton != None:
		if bEnable == 1:
			pSTSButton.SetEnabled()
		else:
			pSTSButton.SetDisabled()
	import Custom.NanoFXv2.WarpFX.WarpFX_GUI
	pSSButton = Custom.NanoFXv2.WarpFX.WarpFX_GUI.pSSButton
	if pSSButton != None:
		if bEnable == 1:
			pSSButton.SetEnabled()
		else:
			pSSButton.SetDisabled()

def UpdateTTPara():
	debug(__name__ + ", UpdateTTPara")
	if pGUICreator == None:
		return
	pTraW = pGUICreator.GetElement("Travelling")
	if pTraW == None:
		return
	
	sList = ["Selected Travel Type: "+HelmAddonGUI.sSelectedTravelType]

	pPara = pGUICreator.GetElement("TT Para")
	if pPara == None:
		pGUICreator.SetInfoForName("TT Para", 0.0, 0.0)
		pPara = pGUICreator.CreateParagraph("TT Para", sList, pTraW)
	else:
		pGUICreator.UpdateParagraph("TT Para", sList)

def ShowInfoOnRegion(pRegion, X, Y):
	debug(__name__ + ", ShowInfoOnRegion")
	pPlayer = App.Game_GetCurrentPlayer()
	if pGUICreator == None or pPlayer == None:
		return
	pILayer = pGUICreator.GetElement("GM Layer: Info")
	pPara = pGUICreator.GetElement("RegionInfo")
	if pRegion == None:
		pGUICreator.DeleteElement("RegionInfo")
	else:
		pPlayerSet = pPlayer.GetContainingSet()
		if pRegion.Name == "SpaceSet":
			sList = ["Player Location"]
		elif pPlayerSet and IsPlayerWarping() and pRegion.Name == pPlayerSet.GetRegion().GetName():
			sList = ["Player (Travelling)"]
		else:
			sList = [pRegion.Name]
		if pPara == None:
			pGUICreator.SetInfoForName("RegionInfo", X, Y)
			pGUICreator.CreateParagraph("RegionInfo", sList, pILayer)
		else:
			pGUICreator.UpdateParagraph("RegionInfo", sList)
			pPara.SetPosition(X, Y)	

def CreateIcon(sName, IconNum, X, Y, nSize, Parent, ShowIcon = 0):
	debug(__name__ + ", CreateIcon")
	if pGUICreator == None:
		return
	pGUICreator.IconCreator.SetInfoForIcon(sName, GALAXY_ICONS, IconNum, X-(nSize/2), Y-(nSize/2), nSize, nSize)
	pIcon = pGUICreator.IconCreator.CreateIcon(sName, Parent)	
	if ShowIcon:
		pGUICreator.IconCreator.ShowIcon(sName)
	return pIcon

def GetAllRegions():
	debug(__name__ + ", GetAllRegions")
	return App.g_kRegionManager.GetAllRegions()

def SetPlayerWarpDestination(pRegion):
	debug(__name__ + ", SetPlayerWarpDestination")
	pWarpButton = App.SortedRegionMenu_GetWarpButton()
	if pWarpButton:
		if pRegion:
			if type(pRegion) == type(""):
				pWarpButton.SetDestination(pRegion)
			else:
				pWarpButton.SetDestination(pRegion.Region)
		else:
			pWarpButton.SetDestination(None)

def GetPlayerWarpDestination():
	debug(__name__ + ", GetPlayerWarpDestination")
	pWarpButton = App.SortedRegionMenu_GetWarpButton()
	if pWarpButton:
		return pWarpButton.GetDestination()

def GetPlayerSubSet():
	debug(__name__ + ", GetPlayerSubSet")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer:
		pSet = pPlayer.GetContainingSet()
		if pSet:
			return pSet.GetRegionModule()

def GetColorForRegion(pRegion, pDestReg = None):
	debug(__name__ + ", GetColorForRegion")
	global pPlayerRegion, pSelectedRegion
	pPlayer = App.Game_GetCurrentPlayer()
	if pDestReg == None:
		pDestReg = pSelectedRegion
	if pRegion != None:
		if pDestReg != None and pRegion.GetName() == pDestReg.GetName():
			return COLOR_SELECTED
		elif pPlayerRegion != None and pRegion.GetName() == pPlayerRegion.GetName():
			return COLOR_PLAYER
		elif GalacticWarSimulator.WarSimulator.IsInitialized() == 1 and pPlayer != None:
			sEmpire = pRegion.GetControllingEmpire()
			sPlayerRace = str(GetShipRace(pPlayer))
			if GetRaceClassObj(sEmpire) != None:
				if IsShipFriendlyOfRace(pPlayer, sEmpire) == 1 or sPlayerRace == sEmpire:
					return COLOR_ALLIED
				elif IsShipEnemyOfRace(pPlayer, sEmpire) == 1:
					return COLOR_HOSTILE
	return COLOR_REGION

def GetTimeStrings(fSeconds, bReturnInList = 1):
	# make a little loop to count years, days, hours and minutes out of the seconds
	# the reason of those bunch of IFs is to make the loop faster.
	##
	# bReturnInList = 1 will return the values in a couple strings in a list: [" -Y years", " -M months" and so on]
	# if it's = 0, it'll return the values in a "condensed" string:  "Y ye, M mo, D days, etc"
	debug(__name__ + ", GetTimeStrings")
	fMins = 0
	fHours = 0
	fDays = 0
	fYears = 0
	while fSeconds >= 60.0:
		if fSeconds >= 360000000.0:
			fHours = fHours + 100000
			fSeconds = fSeconds - 360000000.0
		elif fSeconds >= 180000000:
			fHours = fHours + 50000
			fSeconds = fSeconds - 180000000.0
		elif fSeconds >= 36000000.0:
			fHours = fHours + 10000
			fSeconds = fSeconds - 36000000.0
		elif fSeconds >= 18000000:
			fHours = fHours + 5000
			fSeconds = fSeconds - 18000000.0
		elif fSeconds >= 3600000.0:
			fHours = fHours + 1000
			fSeconds = fSeconds - 3600000.0
		elif fSeconds >= 1800000:
			fHours = fHours + 500
			fSeconds = fSeconds - 1800000.0
		elif fSeconds >= 360000.0:
			fHours = fHours + 100
			fSeconds = fSeconds - 360000.0
		elif fSeconds >= 180000:
			fHours = fHours + 50
			fSeconds = fSeconds - 180000.0
		elif fSeconds >= 36000.0:
			fHours = fHours + 10
			fSeconds = fSeconds - 36000.0
		elif fSeconds >= 18000:
			fHours = fHours + 5
			fSeconds = fSeconds - 18000.0
		elif fSeconds >= 3600.0:
			fHours = fHours + 1
			fSeconds = fSeconds - 3600.0
		elif fSeconds >= 1800:
			fMins = fMins + 30 
			fSeconds = fSeconds - 1800.0
		else:
			fMins = fMins + 1
			fSeconds = fSeconds - 60.0
	while fHours >= 24:
		fDays = fDays + 1
		fHours = fHours - 24
	while fDays >= 365:
		fYears = fYears + 1
		fDays = fDays - 365
	# finally, a little math to remove some decimal plates from the fSeconds variable
	fSeconds = float(GetStrFromFloat(fSeconds, 2))

	if bReturnInList == 1:
		lsTimes = ["Time to reach:"]
	else:
		lsTimes = ""
	if fYears > 0:
		if bReturnInList == 1:
			lsTimes.append("- "+str(fYears)+" years")
		else:
			lsTimes = lsTimes + str(fYears) + " years, "
	if fDays > 0:
		if bReturnInList == 1:
			lsTimes.append("- "+str(fDays)+" days")
		else:
			lsTimes = lsTimes + str(fDays) + " days, "
	if fHours >0:
		if bReturnInList == 1:
			lsTimes.append("- "+str(fHours)+" hours")
		else:
			lsTimes = lsTimes + str(fHours) + " hours, "
	if fMins > 0:
		if bReturnInList == 1:
			lsTimes.append("- "+str(fMins)+" minutes")
		else:
			lsTimes = lsTimes + str(fMins) + " minutes, "
	if bReturnInList == 1:
		lsTimes.append("- "+str(fSeconds)+" seconds")
	else:
		lsTimes = lsTimes + str(fSeconds) + " secs."
	return lsTimes

def IsPlayerWarping():
	debug(__name__ + ", IsPlayerWarping")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer:
		return App.g_kTravelManager.IsShipTravelling(pPlayer)
	else:
		return 0

def PurgeGalaxyMap():
	debug(__name__ + ", PurgeGalaxyMap")
	global InfoNamesList
	if pGUICreator == None:
		return
	DeleteRegionIcons()
	for sName in InfoNamesList:
		pGUICreator.DeleteElement(sName)
	InfoNamesList = []
	pGUICreator.MasterPurge()