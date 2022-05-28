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
from Custom.GravityFX.GravityFXlib import *
from Custom.GravityFX.GravityFXguilib import *
from Custom.GravityFX.ListLib import *

pGUICreator = None
eRefresh = None
ET_SYSTEM_MAP = None
pNAVPoint = None
OldObjList = []
Logger = None
ShowObjsInfo = 0
InfoIDsList = []

###########################################################
#   The Icon's numbers, for easy reference later
########################################################
ICON_ASTEROID = 0
ICON_BLACKHOLE = 1
ICON_ENEMY_MARKER = 2
ICON_FRIEND_MARKER = 3
ICON_GRAV_WELL = 4
ICON_GRAV_WELL_PLUGIN = 5
ICON_BACKGROUND_STARS = 6
ICON_HORIZONTAL_BAR = 7
ICON_VERTICAL_BAR = 8
ICON_NEBULA = 9
ICON_NEUTRAL_MARKER = 10
ICON_PLANET = 11
ICON_PLAYER_SHIP = 12
ICON_SHIP = 13
ICON_STATION = 14
ICON_SUN = 15
ICON_SM_NAV_POINT = 16
ICON_TARGET_MARKER = 17
ICON_TORP_GRAV_EFFECT = 18
ICON_UNKNOWN = 19
ICON_WAYPOINT = 20
###########################################################

def CreateSystemMapGUI():
	global ET_SYSTEM_MAP, ET_SHOW_ICON, pGUICreator, Logger
	try:
		pGUICreator = GUICreator()
		pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
		pBridge = App.g_kSetManager.GetSet("bridge")
		pScience = App.CharacterClass_GetObject(pBridge, "Science")
		pScienceMenu = pScience.GetMenu()
		if GetConfigValue("LogSystemMap"):
			Logger = Custom.GravityFX.Logger.LogCreator("System Map Logger", "scripts\Custom\GravityFX\Logs\SystemMapLOG.txt")
			Logger.LogString("Initialized System Map logger")
		else:
			Logger = Custom.GravityFX.Logger.DummyLogger()
		ET_SYSTEM_MAP = GetNextEventType()
	
		# Just to be sure, tho its kinda impossible to have any at this point. 
		pGUICreator.ButtonCreator.DeleteAllButtons()
		
		pGUICreator.ButtonCreator.CreateButton("System Map", ET_SYSTEM_MAP, None, 1, pScienceMenu)
		
		App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SYSTEM_MAP, pMission, __name__ + ".SMOpenClose")
	
		pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".SMClose")
	except:
		LogError("CreateSystemMapGUI")


def SMOpenClose(pObject, pEvent):
	try:
		pSM = pGUICreator.GetElement("System Map")
		if not pSM:
			pGUICreator.SetInfoForName("System Map", 0.0, 0.0, 1.0, 1.0, 0)
			pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
			pSM = pGUICreator.CreateWindow("System Map", pTCW)
			pSM.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
			pSM.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
			# Create the additional panes, the SM icons will be created on them. To fix layering problems with icons
			NamesList = ["SM Layer: GravWells", "SM Layer: Objects", "SM Layer: GWP Marker", "SM Layer: Allegiance Marker", "SM Layer: Info"]
			for sName in NamesList:
				pGUICreator.SetInfoForName(sName, 0.007, 0.024, 0.99, 0.9, 0)	
				pPane = pGUICreator.CreatePane(sName, pTCW)
				pPane.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
				pPane.AddPythonFuncHandlerForInstance(App.ET_KEYBOARD, __name__+".KeyHandler")
			Logger.LogString("Created SystemMap Window")
			CreateSMContents()
		if pSM.IsVisible():
			pGUICreator.CloseElement("System Map")
			pGUICreator.CloseElement("SM Layer: GravWells")
			pGUICreator.CloseElement("SM Layer: Objects")
			pGUICreator.CloseElement("SM Layer: GWP Marker")
			pGUICreator.CloseElement("SM Layer: Allegiance Marker")
			pGUICreator.CloseElement("SM Layer: Info")
		else:
			pGUICreator.ShowElement("System Map")
			pGUICreator.ShowElement("SM Layer: GravWells")
			pGUICreator.ShowElement("SM Layer: Objects")
			pGUICreator.ShowElement("SM Layer: GWP Marker")
			pGUICreator.ShowElement("SM Layer: Allegiance Marker")
			pGUICreator.ShowElement("SM Layer: Info")
	except:
		LogError("SM Open/Close")
		

def CreateSMContents():
	try:
		global eRefresh, ET_SM_CREATE_NAV_POINT
		pSM = pGUICreator.GetElement("System Map")
	
		pGUICreator.IconCreator.CreateIconGroup("GravityFXIcons", 'scripts/Custom/GravityFX/Icons')
		
		#Create paragraphs - MUST BE BEFORE CREATING BUTTONS
		pGUICreator.SetInfoForName("SM Scale Para Pane", 0.35, 0.91, 0.39, 0.03)
		pSMScalePane = pGUICreator.CreatePane("SM Scale Para Pane", pSM)
		slSMScale = ["System Map Scale: "+str(GetDivideFactor())+" Kms around the Player."]
		pGUICreator.SetInfoForName("System Map Scale Para", 0.0, 0.0)
		pGUICreator.CreateParagraph("System Map Scale Para", slSMScale, pSMScalePane)	
	
		#Create Buttons
		CloseButtonDict = {'X': 0.01, 'Y': 0.91, 'WIDTH': 0.1, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateButton("Close", None, __name__ + ".SMClose", 1, pSM, CloseButtonDict, CloseButtonDict)

		SOIButtonDict = {'X': 0.12, 'Y': 0.91, 'WIDTH': 0.22, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateYesNoButton("Show Objs Info", None, __name__ + ".SOIClick", 0, pSM, SOIButtonDict, SOIButtonDict)
	
		SMScaleBarButtonDict = {'X': 0.69, 'Y': 0.91, 'WIDTH': 0.3, 'HEIGTH': 0.03}
		pSMScaleBar = pGUICreator.ButtonCreator.CreateBar("Set the Scale+/- Amount", None, None, 100, [1.0, 1000.0], 100, 1, pSM, SMScaleBarButtonDict, SMScaleBarButtonDict)
		pSMScaleBar.SetKeyInterval(1.0)
	
		#Create the map background - stars and horizontal/vertical bars
		CreateMapBackground()

		eRefresh = RefreshEventHandler(UpdateSystemMap)
		Logger.LogString("Created System Map Constant Contents")
	except:
		LogError("Create SM Contents")


def CreateMapBackground():
	try:
		pSM = pGUICreator.GetElement("System Map")
		sBackStars = "SM Background Stars"
		nBackStarsXPOS = 0
		nBackStarsYPOS = -0.1
		CoordList = [[0, -0.1], [0.2, -0.1], [0.4, -0.1], [0.6, -0.1], [0.8, -0.1], 
				[0, 0.1], [0.2, 0.1], [0.4, 0.1], [0.6, 0.1], [0.8, 0.1],
				[0, 0.3], [0.2, 0.3], [0.4, 0.3], [0.6, 0.3], [0.8, 0.3],
				[0, 0.5], [0.2, 0.5], [0.4, 0.5], [0.6, 0.5], [0.8, 0.5],
				[0, 0.7], [0.2, 0.7], [0.4, 0.7], [0.6, 0.7], [0.8, 0.7]]
		for I in range(25):
			Coord = CoordList[I]
			X = Coord[0]
			Y = Coord[1]
			pGUICreator.IconCreator.SetInfoForIcon(sBackStars+str(I), "GravityFXIcons", ICON_BACKGROUND_STARS, X, Y)
			pIcon = pGUICreator.IconCreator.CreateIcon(sBackStars+str(I), pSM)
	
		sVerBar = "SM Grid Vertical Bar"
		nVerBarXPOS = 0
		for N in range(11):
			pGUICreator.IconCreator.SetInfoForIcon(sVerBar+str(N), "GravityFXIcons", ICON_VERTICAL_BAR, nVerBarXPOS, 0)
			pIcon = pGUICreator.IconCreator.CreateIcon(sVerBar+str(N), pSM)
			pIcon.Resize(0.001, 0.90)
			pGUICreator.IconCreator.ShowIcon(sVerBar+str(N))
			nVerBarXPOS = nVerBarXPOS + 0.1
		sHorBar = "SM Grid Horizontal Bar"
		nHorBarYPOS = 0
		for N in range(10):
			pGUICreator.IconCreator.SetInfoForIcon(sHorBar+str(N), "GravityFXIcons", ICON_HORIZONTAL_BAR, 0, nHorBarYPOS)
			pIcon = pGUICreator.IconCreator.CreateIcon(sHorBar+str(N), pSM)
			pIcon.Resize(1.0, 0.001)
			pGUICreator.IconCreator.ShowIcon(sHorBar+str(N))
			nHorBarYPOS = nHorBarYPOS + 0.1
	except:
		LogError("CreateMapBackground")


def SMClose(pObject, pEvent):
	try:
		pGUICreator.CloseElement("System Map")
		pGUICreator.CloseElement("SM Layer: GravWells")
		pGUICreator.CloseElement("SM Layer: Objects")
		pGUICreator.CloseElement("SM Layer: GWP Marker")
		pGUICreator.CloseElement("SM Layer: Allegiance Marker")
		pGUICreator.CloseElement("SM Layer: Info")
		pObject.CallNextHandler(pEvent)
		Logger.LogString("Closed System Map")
	except:
		LogError("SM Close")


def UpdateSystemMap(pObject, pEvent):
	global OldObjList
	try:
		pSM = pGUICreator.GetElement("System Map")
		pPlayer = MissionLib.GetPlayer()
		if pSM.IsVisible() and pPlayer:
			Logger.LogImportant("SM Update Cycle")
			#was handling player here
			UpdateIconNumForObject(pPlayer)
			pVec = pPlayer.GetWorldLocation()
			NewObjList = GetAllObjsInSet()
			for pObj in OldObjList:
				if IsObjInList(pObj, NewObjList):
					#The obj exists in both the old and the new obj List, so just move/resize it.
					pPOS = pObj.GetWorldLocation()
					pPOS.Subtract(pVec)
					nFactorKM = GetDivideFactor()
					nFactor = ConvertKMtoGU(nFactorKM)
					pPOS.Scale(1.0/nFactor)
					X, Y = pPOS.x/2 + 0.5, pPOS.y/2 + 0.5
					nSize = (1.0/nFactor)*pObj.GetRadius()*2
					if nSize < 0.01:
						nSize = 0.01
					Logger.LogString("Moving/Resizing icon for obj: "+pObj.GetName()+" "+str(pObj.GetObjID()))
					UpdateIconNumForObject(pObj)
					if ShowObjsInfo:
						UpdateInfoOnObj(pObj)
					pIcon = pGUICreator.IconCreator.GetIcon(str(pObj.GetObjID()))
					if pIcon:
						if pIcon.GetIconNum() == ICON_PLAYER_SHIP:
							Logger.LogError("Tried to M/R icon with ICON_PLAYER_SHIP icon num")
						else:
							pIcon.Resize(nSize, nSize)
							pIcon.SetPosition(X-(pIcon.GetWidth()/2), Y-(pIcon.GetHeight()/2))
					else:
						Logger.LogError("M/R icon for obj NOT WORKED: "+pObj.GetName()+" "+str(pObj.GetObjID())+", going to create Obj's Icons")
						CreateIconForObject(pObj)
					if pObj.IsTypeOf(App.CT_WAYPOINT):
						GravWell = App.g_kGravityManager.FindGravWellByID(pObj.GetName())
					else:
						GravWell = App.g_kGravityManager.GetGravWell(pObj.GetName())
					pGWIcon = pGUICreator.IconCreator.GetIcon("GravWell"+str(pObj.GetObjID()))
					if pGWIcon and GravWell:
						nGWSize = (1.0/nFactor)*GravWell.Radius
						pGWIcon.Resize(nGWSize, nGWSize)
						pGWIcon.SetPosition(X-(pGWIcon.GetWidth()/2), Y-(pGWIcon.GetHeight()/2))
					elif pGWIcon and not GravWell:
						pGUICreator.IconCreator.DeleteIcon("GravWell"+str(pObj.GetObjID()))
					pGWPMIcon = pGUICreator.IconCreator.GetIcon("GravWellPluginMarker"+str(pObj.GetObjID()))
					if pGWPMIcon and GravWell:
						pGWPMIcon.Resize(nSize, nSize)
						pGWPMIcon.SetPosition(X-(pGWPMIcon.GetWidth()/2), Y-(pGWPMIcon.GetHeight()/2))
					elif pGWPMIcon and not GravWell:
						pGUICreator.IconCreator.DeleteIcon("GravWellPluginMarker"+str(pObj.GetObjID()))
					pEMIcon = pGUICreator.IconCreator.GetIcon("EnemyMarker"+str(pObj.GetObjID()))
					if pEMIcon:
						pEMIcon.Resize(nSize, nSize)
						pEMIcon.SetPosition(X-(pEMIcon.GetWidth()/2), Y-(pEMIcon.GetHeight()/2))

					pFMIcon = pGUICreator.IconCreator.GetIcon("FriendMarker"+str(pObj.GetObjID()))
					if pFMIcon:
						pFMIcon.Resize(nSize, nSize)
						pFMIcon.SetPosition(X-(pFMIcon.GetWidth()/2), Y-(pFMIcon.GetHeight()/2))
					
					pNMIcon = pGUICreator.IconCreator.GetIcon("NeutralMarker"+str(pObj.GetObjID()))
					if pNMIcon:
						pNMIcon.Resize(nSize, nSize)
						pNMIcon.SetPosition(X-(pNMIcon.GetWidth()/2), Y-(pNMIcon.GetHeight()/2))
				else:
					#the obj previously existed but no longer exists on the new obj List, so delete it.
					pGUICreator.IconCreator.DeleteIcon(str(pObj.GetObjID()))
					Logger.LogString("Deleted icon for obj: "+pObj.GetName()+" "+str(pObj.GetObjID()))
					#And then delete any possible 'child' icon of the object
					#If there isn't any icon to be deleted, don't worry. IconCreator class handles it extremely well.
					pGUICreator.IconCreator.DeleteIcon("GravWell"+str(pObj.GetObjID()))
					pGUICreator.IconCreator.DeleteIcon("GravWellPluginMarker"+str(pObj.GetObjID()))
					pGUICreator.IconCreator.DeleteIcon("FriendMarker"+str(pObj.GetObjID()))
					pGUICreator.IconCreator.DeleteIcon("EnemyMarker"+str(pObj.GetObjID()))
					pGUICreator.IconCreator.DeleteIcon("NeutralMarker"+str(pObj.GetObjID()))
					pGUICreator.DeleteElement("Info"+str(pObj.GetObjID()))
			for pNewObj in NewObjList:
				#if not IsObjInList(pNewObj, OldObjList):
				pIcon = pGUICreator.IconCreator.GetIcon(str(pNewObj.GetObjID()))
				if pIcon == None:
					#The obj do not exists on the old obj list, but exists in the new list, so create the icon for it.
					CreateIconForObject(pNewObj)
			HandleTargetIcon()
			HandlerPlayerIcon()
			OldObjList = NewObjList
	except:
		LogError("UpdateSystemMap")


def GetDivideFactor():
	try:
		if GetConfigValue("SystemMapScaleLightyear") == 1:
			#So return 1 lightyear
			#1 lightyear = 9,460,800,000,000 Kms
			return 94608e+008
		else:
			return GetConfigValue("SystemMapScale")
	except:
		LogError("GetDivideFactor")

def SOIClick(pObject, pEvent):
	global ShowObjsInfo, InfoIDsList
	try:
		pButton = pGUICreator.ButtonCreator.GetButtonByName("Show Objs Info")
		if pButton:
			if pButton.IsChosen():
				ShowObjsInfo = 1
			else:
				ShowObjsInfo = 0
				for ID in InfoIDsList:
					pGUICreator.DeleteElement(str(ID))		
	except:
		LogError("SOIClick")

def KeyHandler(pObject, pEvent):
	try:
		eUni = pEvent.GetUnicode()
		pSMScaleBar = pGUICreator.ButtonCreator.GetButtonByName("Set the Scale+/- Amount")
		nScaleAmount = pSMScaleBar.GetValue()
		GravFXConfigValues = __import__('Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.GravityFXConfigValues')
		if eUni == App.WC_ADD:
			GravFXConfigValues.SystemMapScale = GravFXConfigValues.SystemMapScale + nScaleAmount/3
			if GravFXConfigValues.SystemMapScale < 1.0:
				GravFXConfigValues.SystemMapScale = 1.0
			slSMScale = ["System Map Scale: "+str(GetDivideFactor())+" Kms around the Player."]
			pGUICreator.UpdateParagraph("System Map Scale Para", slSMScale)
		elif eUni == App.WC_SUBTRACT:
			GravFXConfigValues.SystemMapScale = GravFXConfigValues.SystemMapScale - nScaleAmount/3
			if GravFXConfigValues.SystemMapScale < 1.0:
				GravFXConfigValues.SystemMapScale = 1.0
			slSMScale = ["System Map Scale: "+str(GetDivideFactor())+" Kms around the Player."]
			pGUICreator.UpdateParagraph("System Map Scale Para", slSMScale)
		return
	except:
		LogError("KeyHandler")

def MouseHandler(pObject, pEvent):
	global pNAVPoint
	try:
		pObject.CallNextHandler(pEvent)
		if pEvent.EventHandled() == 0:
			pEvent.SetHandled()
	
		if pEvent.IsButtonEvent():
			nNum = pEvent.GetButtonNum()
			if nNum == App.TGMouseEvent.MEF_BUTTON_LEFT:
				MouseX = pEvent.GetX()
				MouseY = pEvent.GetY()
				if MouseY <= 0.9:
					MouseWidth = App.g_kRootWindow.GetMouseCursor().GetWidth()
					MouseHeigth = App.g_kRootWindow.GetMouseCursor().GetHeight()
					pPlayer = App.Game_GetCurrentPlayer()
					if not pPlayer:
						return
					pVec = pPlayer.GetWorldLocation()
					pPOS = App.TGPoint3()
					X, Y = ((MouseX-0.5)*2), ((MouseY-0.5)*2)
					pPOS.SetXYZ(X, Y, 0)
					nFactorKM = GetDivideFactor()
					nFactor = ConvertKMtoGU(nFactorKM)
					pPOS.Scale(nFactor)
					pPOS.Add(pVec)
					
					if pNAVPoint == None:
						pNAVPoint = CreateNAVPoint("System Map NAV Point", pPlayer.GetContainingSet(), pPOS)
						Logger.LogString("Created System Map NAV Point")
					else:
						PosX, PosY = MouseX, MouseY
						ObjList = GetAllObjsInSet()
						TargetList = []
						for pObj in ObjList:
							TargetList.append(pObj)
						pNewTarget = None
						for pTarget in TargetList:
							pPOS = App.NiPoint2(0,0)
							pIcon = pGUICreator.IconCreator.GetIcon(str(pTarget.GetObjID()))
							if pIcon:
								pIcon.GetPosition(pPOS)
								X, Y = pPOS.x, pPOS.y
								EndX, EndY = X+pIcon.GetWidth(), Y+pIcon.GetHeight()
                						if X <= PosX <= EndX and Y <= PosY <= EndY:
									pNewTarget = pTarget
						if pNewTarget:
							pPlayer.SetTarget(pNewTarget.GetName())
                                                                
			elif nNum == App.TGMouseEvent.MEF_BUTTON_RIGHT:
				if pNAVPoint:
					pNAVPoint.SetNavPoint(0)
					pNAVPoint.__del__()
					pNAVPoint = None
					Logger.LogString("Deleted System Map NAV Point")
	except:
		LogError("MouseHandler")
	

def CreateIconForObject(pObject):
	try:
		pObjLayer = pGUICreator.GetElement("SM Layer: Objects")
		pGWLayer = pGUICreator.GetElement("SM Layer: GravWells")
		pGWPMLayer = pGUICreator.GetElement("SM Layer: GWP Marker")
		pPlayer = MissionLib.GetPlayer()
		if pPlayer and pObject.GetObjID() == pPlayer.GetObjID():
			Logger.LogError("Tried to create Player Icon on CreateIconForObject function, this is not supposed to happen")
			return
		pPOS = pObject.GetWorldLocation()
		pPOS.Unitize()
		X, Y = pPOS.x/2 + 0.5, pPOS.y/2 + 0.5      #We subtract half the size of the icon later, so that the center of the icon is placed at the correct X and Y
		nFactorKM = GetDivideFactor()
		nFactor = ConvertKMtoGU(nFactorKM)
		nSize = (1.0/nFactor)*pObject.GetRadius()*2
		if nSize < 0.01:
			nSize = 0.01
		if pObject.IsTypeOf(App.CT_WAYPOINT):
			GravWell = App.g_kGravityManager.FindGravWellByID(pObject.GetName())
		else:
			GravWell = App.g_kGravityManager.GetGravWell(pObject.GetName())
		if GravWell:
			if GravWell.IsBlackhole():
				IsNotBlackhole = 0
			else:
				IsNotBlackhole = 0
		else:
			IsNotBlackhole = 1
		if GravWell:
			nGWSize = (1.0/nFactor)*GravWell.Radius
			CreateIcon("GravWell"+str(pObject.GetObjID()), ICON_GRAV_WELL, X, Y, nGWSize, pGWLayer)
		CreateIcon(str(pObject.GetObjID()), ICON_UNKNOWN, X, Y, nSize, pObjLayer)
		if pObject.IsTypeOf(App.CT_SHIP) and IsNotBlackhole:
			pShipProp = pObject.GetShipProperty()
			if pShipProp:
				if pShipProp.GetGenus() == 3 and pShipProp.IsStationary() == 0:
					if GravWell:
						CreateIcon("GravWellPluginMarker"+str(pObject.GetObjID()), ICON_GRAV_WELL_PLUGIN, X, Y, nSize, pGWPMLayer, 1)
				else:
					CreateAllegianceMarker(pObject, X, Y, nSize)
		Logger.LogString("Created Icon for obj: "+pObject.GetName()+" "+str(pObject.GetObjID()))
	except:
		LogError("CreateIconForObject")

def UpdateIconNumForObject(pObject):
	try:
		pIcon = pGUICreator.IconCreator.GetIcon(str(pObject.GetObjID()))
		if not pIcon:
			return
		if pObject.IsTypeOf(App.CT_SUN):
			if pIcon.GetIconNum() != ICON_SUN:
				pIcon.SetIconNum(ICON_SUN)
				Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_SUN")
			################################################## SUN GRAV WELL
		elif pObject.IsTypeOf(App.CT_PLANET):
			if pIcon.GetIconNum() != ICON_PLANET:
				pIcon.SetIconNum(ICON_PLANET)
				Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_PLANET")
			########################################################### PLANET GRAV WELL
		elif pObject.IsTypeOf(App.CT_NEBULA):
			if pIcon.GetIconNum() != ICON_NEBULA:
				pIcon.SetIconNum(ICON_NEBULA)
				Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_NEBULA")
		elif pObject.IsTypeOf(App.CT_WAYPOINT):
			pWaypoint = App.Waypoint_Cast(pObject)
			if pNAVPoint and pWaypoint.GetObjID() == pNAVPoint.GetObjID():
				if pIcon.GetIconNum() != ICON_SM_NAV_POINT:
					pIcon.SetIconNum(ICON_SM_NAV_POINT)
					Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_SM_NAV_POINT")
			else:
				pTGE = App.g_kGravityManager.FindGravWellByID(pWaypoint.GetName())
				if pTGE:
					###################################################### TGE GRAV WELL
					if pIcon.GetIconNum() != ICON_TORP_GRAV_EFFECT:
						pIcon.SetIconNum(ICON_TORP_GRAV_EFFECT)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_TORP_GRAV_EFFECT")
				else:
					if pIcon.GetIconNum() != ICON_WAYPOINT:
						pIcon.SetIconNum(ICON_WAYPOINT)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_WAYPOINT")
		elif pObject.IsTypeOf(App.CT_SHIP):
			pShip = App.ShipClass_Cast(pObject)
			pPlayer = MissionLib.GetPlayer()
			pShipProp = pShip.GetShipProperty()
			pFriends = MissionLib.GetFriendlyGroup()
			pEnemies = MissionLib.GetEnemyGroup()
			pNeutrals = MissionLib.GetNeutralGroup()
			if pShip and pShipProp:
				pGWP = App.g_kGravityManager.GetGravWell(pShip.GetName())
				#if pGWP:
					##########################   SHIP GRAV WELL
				if pPlayer and pShip.GetObjID() == pPlayer.GetObjID():
					if pIcon.GetIconNum() != ICON_PLAYER_SHIP:
						pIcon.SetIconNum(ICON_PLAYER_SHIP)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_PLAYER_SHIP")
					#if pGWP:
						############################   PLAYER SHIP  GRAV WELL PLUGIN MARKER
				elif pGWP and pGWP.IsBlackhole():
					if pIcon.GetIconNum() != ICON_BLACKHOLE:
						pIcon.SetIconNum(ICON_BLACKHOLE)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_BLACKHOLE")
				elif pShipProp.GetGenus() == 1 and pShipProp.IsStationary() == 0:
					if pIcon.GetIconNum() != ICON_SHIP:
						pIcon.SetIconNum(ICON_SHIP)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_SHIP")
					if pFriends.IsNameInGroup(pShip.GetName()):
						pFMIcon = pGUICreator.IconCreator.GetIcon("FriendMarker"+str(pObject.GetObjID()))
						if pFMIcon and pFMIcon.GetIconNum() != ICON_FRIEND_MARKER:
							pFMIcon.SetIconNum(ICON_FRIEND_MARKER)
							Logger.LogString("Updated "+pObject.GetName()+" allegiance icon to ICON_FRIEND_MARKER")		
					elif pEnemies.IsNameInGroup(pShip.GetName()):
						pEMIcon = pGUICreator.IconCreator.GetIcon("EnemyMarker"+str(pObject.GetObjID()))
						if pEMIcon and pEMIcon.GetIconNum() != ICON_ENEMY_MARKER:
							pEMIcon.SetIconNum(ICON_ENEMY_MARKER)
							Logger.LogString("Updated "+pObject.GetName()+" allegiance icon to ICON_ENEMY_MARKER")		
					elif pNeutrals.IsNameInGroup(pShip.GetName()):
						pNMIcon = pGUICreator.IconCreator.GetIcon("NeutralMarker"+str(pObject.GetObjID()))
						if pNMIcon and pNMIcon.GetIconNum() != ICON_NEUTRAL_MARKER:
							pNMIcon.SetIconNum(ICON_NEUTRAL_MARKER)
							Logger.LogString("Updated "+pObject.GetName()+" allegiance icon to ICON_NEUTRAL_MARKER")
				elif pShipProp.GetGenus() == 2 or pShipProp.IsStationary() == 1:
					if pIcon.GetIconNum() != ICON_STATION:
						pIcon.SetIconNum(ICON_STATION)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_STATION")
					if pFriends.IsNameInGroup(pShip.GetName()):
						pFMIcon = pGUICreator.IconCreator.GetIcon("FriendMarker"+str(pObject.GetObjID()))
						if pFMIcon and pFMIcon.GetIconNum() != ICON_FRIEND_MARKER:
							pFMIcon.SetIconNum(ICON_FRIEND_MARKER)
							Logger.LogString("Updated "+pObject.GetName()+" allegiance icon to ICON_FRIEND_MARKER")		
					elif pEnemies.IsNameInGroup(pShip.GetName()):
						pEMIcon = pGUICreator.IconCreator.GetIcon("EnemyMarker"+str(pObject.GetObjID()))
						if pEMIcon and pEMIcon.GetIconNum() != ICON_ENEMY_MARKER:
							pEMIcon.SetIconNum(ICON_ENEMY_MARKER)
							Logger.LogString("Updated "+pObject.GetName()+" allegiance icon to ICON_ENEMY_MARKER")		
					elif pNeutrals.IsNameInGroup(pShip.GetName()):
						pNMIcon = pGUICreator.IconCreator.GetIcon("NeutralMarker"+str(pObject.GetObjID()))
						if pNMIcon and pNMIcon.GetIconNum() != ICON_NEUTRAL_MARKER:
							pNMIcon.SetIconNum(ICON_NEUTRAL_MARKER)
							Logger.LogString("Updated "+pObject.GetName()+" allegiance icon to ICON_NEUTRAL_MARKER")			
				elif pShipProp.GetGenus() == 3 and pShipProp.IsStationary() == 0:
					if pIcon.GetIconNum() != ICON_ASTEROID:
						pIcon.SetIconNum(ICON_ASTEROID)
						Logger.LogString("Updated "+pObject.GetName()+" icon to ICON_ASTEROID")
					#if pGWP:
						############################   ASTEROID GRAV WELL PLUGIN MARKER
	except:
		LogError("UpdateIconNumForObject")

def UpdateInfoOnObj(pObject):
	global InfoIDsList
	try:
		pILayer = pGUICreator.GetElement("SM Layer: Info")
		pPlayer = App.Game_GetCurrentPlayer()
		if pObject and pPlayer:
			if pObject.GetObjID() == pPlayer.GetObjID():
				sName = "InfoPlayer"
			else:
				sName = "Info"+str(pObject.GetObjID())
			pPara = pGUICreator.GetElement(sName)
			pPOS = pObject.GetWorldLocation()
			pPOS.Subtract(pPlayer.GetWorldLocation())
			sList = [pObject.GetName(), "Z Axis: "+GetStrFromFloat(ConvertGUtoKM(pPOS.z))]
			nFactorKM = GetDivideFactor()
			nFactor = ConvertKMtoGU(nFactorKM)
			pPOS.Scale(1.0/nFactor)
			X, Y = pPOS.x/2 + 0.5, pPOS.y/2 + 0.5
			nSize = (1.0/nFactor)*pObject.GetRadius()*2
			if nSize < 0.01:
				nSize = 0.01
			if pPara == None:
				pGUICreator.SetInfoForName(sName, X+(nSize/2), Y-(nSize/2))
				pGUICreator.CreateParagraph(sName, sList, pILayer)
				InfoIDsList.append(sName)
			else:
				pGUICreator.UpdateParagraph(sName, sList)
				pPara.SetPosition(X+(nSize/2), Y-(nSize/2))
			return pPara		
	except:
		LogError("UpdateInfoOnObj")

def HandleTargetIcon():
	try:
		pAMLayer = pGUICreator.GetElement("SM Layer: Allegiance Marker")
		pPlayer = MissionLib.GetPlayer()
		if pPlayer:
			pObject = pPlayer.GetTarget()
		if pObject:
			pTargetIcon = pGUICreator.IconCreator.GetIcon(str(pObject.GetObjID()))
			if pTargetIcon == None:
				pGUICreator.IconCreator.HideIcon("TargetMarker")
				return None
			pPOS = pObject.GetWorldLocation()
			pPOS.Subtract(pPlayer.GetWorldLocation())
			nFactorKM = GetDivideFactor()
			nFactor = ConvertKMtoGU(nFactorKM)
			pPOS.Scale(1.0/nFactor)
			X, Y = pPOS.x/2 + 0.5, pPOS.y/2 + 0.5
			nSize = (1.0/nFactor)*pObject.GetRadius()*2
			if nSize < 0.01:
				nSize = 0.01
			nSize = 0.05
			pIcon = pGUICreator.IconCreator.GetIcon("TargetMarker")
			if pIcon == None:
				CreateIcon("TargetMarker", ICON_TARGET_MARKER, X, Y, nSize, pAMLayer)
			else:
				pIcon.Resize(nSize, nSize)
				pIcon.SetPosition(X-(nSize/2), Y-(nSize/2))
			pGUICreator.IconCreator.ShowIcon("TargetMarker")
			return pIcon
		else:
			pGUICreator.IconCreator.HideIcon("TargetMarker")
			return None
	except:
		LogError("HandleTargetIcon")


def HandlerPlayerIcon():
	try:
		pObjLayer = pGUICreator.GetElement("SM Layer: Objects")
		pGWPMLayer = pGUICreator.GetElement("SM Layer: GWP Marker")
		pGWLayer = pGUICreator.GetElement("SM Layer: GravWells")
		pPlayer = App.Game_GetCurrentPlayer()
		pIcon = None
		if pPlayer:
			if ShowObjsInfo:
				UpdateInfoOnObj(pPlayer)
			pIcon = pGUICreator.IconCreator.GetIcon("PlayerIcon")
			pGWIcon = pGUICreator.IconCreator.GetIcon("GravWellPlayerIcon")
			pGWPMIcon = pGUICreator.IconCreator.GetIcon("GravWellPluginMarkerPlayerIcon")
			pGWP = App.g_kGravityManager.GetGravWell(pPlayer.GetName())
			nFactorKM = GetDivideFactor()
			nFactor = ConvertKMtoGU(nFactorKM)
			nSize = (1.0/nFactor)*pPlayer.GetRadius()*2
			if nSize < 0.01:
				nSize = 0.01
			if pGWP and pGWIcon == None:
				nGWSize = (1.0/nFactor)*pGWP.Radius
				CreateIcon("GravWellPlayerIcon", ICON_GRAV_WELL, 0.5, 0.5, nGWSize, pGWLayer)
			elif pGWP and pGWIcon:
				nGWSize = (1.0/nFactor)*pGWP.Radius
				pGWIcon.Resize(nGWSize, nGWSize)
				pGWIcon.SetPosition(0.5-(pGWIcon.GetWidth()/2), 0.5-(pGWIcon.GetHeight()/2))
			if pIcon == None:
				CreateIcon("PlayerIcon", ICON_PLAYER_SHIP, 0.5, 0.5, nSize, pObjLayer)
				Logger.LogString("Created Player Icons")
			else:
				Logger.LogString("Moving/Resizing Player Icons")
				pIcon.Resize(nSize, nSize)
				pIcon.SetPosition(0.5-(pIcon.GetWidth()/2), 0.5-(pIcon.GetHeight()/2))
				pGUICreator.IconCreator.ShowIcon("PlayerIcon")
			if pGWP and pGWPMIcon == None:
				CreateIcon("GravWellPluginMarkerPlayerIcon", ICON_GRAV_WELL_PLUGIN, 0.5, 0.5, nSize, pGWPMLayer, 1)
			elif pGWP and pGWPMIcon:
				pGWPMIcon.Resize(nSize, nSize)
				pGWPMIcon.SetPosition(0.5-(pGWPMIcon.GetWidth()/2), 0.5-(pGWPMIcon.GetHeight()/2))
			if pGWP == None:
				pGUICreator.IconCreator.DeleteIcon("GravWellPlayerIcon")
				pGUICreator.IconCreator.DeleteIcon("GravWellPluginMarkerPlayerIcon")
		else:
			Logger.LogString("Deleting Player Icons")
			pGUICreator.IconCreator.DeleteIcon("PlayerIcon")
			pGUICreator.IconCreator.DeleteIcon("GravWellPlayerIcon")
			pGUICreator.IconCreator.DeleteIcon("GravWellPluginMarkerPlayerIcon")
	except:
		LogError("HandlePlayerIcon")


def CreateAllegianceMarker(pShip, X, Y, nSize):
	try:
		pAMLayer = pGUICreator.GetElement("SM Layer: Allegiance Marker")
		pGWPMLayer = pGUICreator.GetElement("SM Layer: GWP Marker")
		pFriends = MissionLib.GetFriendlyGroup()
		pEnemies = MissionLib.GetEnemyGroup()
		pNeutrals = MissionLib.GetNeutralGroup()
		pIcon = None
		pGWP = App.g_kGravityManager.GetGravWell(pShip.GetName())
		if pGWP:
			CreateIcon("GravWellPluginMarker"+str(pShip.GetObjID()), ICON_GRAV_WELL_PLUGIN, X, Y, nSize, pGWPMLayer, 1)	
		if pFriends.IsNameInGroup(pShip.GetName()):
			CreateIcon("FriendMarker"+str(pShip.GetObjID()), ICON_FRIEND_MARKER, X, Y, nSize, pAMLayer, 1)			
		elif pEnemies.IsNameInGroup(pShip.GetName()):
			CreateIcon("EnemyMarker"+str(pShip.GetObjID()), ICON_ENEMY_MARKER, X, Y, nSize, pAMLayer, 1)		
		elif pNeutrals.IsNameInGroup(pShip.GetName()):
			CreateIcon("NeutralMarker"+str(pShip.GetObjID()), ICON_NEUTRAL_MARKER, X, Y, nSize, pAMLayer, 1)
		Logger.LogString("Created Allegiance Marker for ship: "+pShip.GetName()+" "+str(pShip.GetObjID()))
		return pIcon
	except:
		LogError("CreateAllegianceMarker")

def CreateIcon(sName, IconNum, X, Y, nSize, Parent, ShowIcon = 0):
	try:
		pGUICreator.IconCreator.SetInfoForIcon(sName, "GravityFXIcons", IconNum, X-(nSize/2), Y-(nSize/2), nSize, nSize)
		pIcon = pGUICreator.IconCreator.CreateIcon(sName, Parent)	
		if ShowIcon:
			pGUICreator.IconCreator.ShowIcon(sName)
		return pIcon
	except:
		LogError("CreateIcon")

def GetAllObjsInSet(pSet = None, IncludePlayer = 0):
	try:
		if pSet == None:
			pPlayer = App.Game_GetCurrentPlayer()
			pSet = pPlayer.GetContainingSet()
		List = []
		if pSet == None:
			return List
		# now thanks to USS Sovereign for telling me of this function: App.SetClass.GetClassObjectList(App.CT_SUN)
		for pObj in pSet.GetClassObjectList(App.CT_SHIP):
			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer and pPlayer.GetObjID() == pObj.GetObjID():
				if IncludePlayer == 1:
					List.append(pObj)
			else:
				List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_WAYPOINT):
			List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_NEBULA):
			List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_SUN):
			if pObj.IsAtmosphereObj() == None:
				List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_PLANET):
			if pObj.IsAtmosphereObj() == None:
				List.append(pObj)
		return List	
	except:
		LogError("GetAllObjsInSet")


def PurgeSystemMap():
	try:
		global OldObjList, pNAVPoint
		OldObjList = []
		if pNAVPoint:
			pNAVPoint.SetNavPoint(0)
			pNAVPoint.__del__()
			pNAVPoint = None
			Logger.LogString("Deleted System Map NAV Point  -- in the PURGE function")	
		pGUICreator.IconCreator.DeleteAllIcons()
		CreateMapBackground()
		Logger.LogString("Purged System Map")
	except:
		LogError("PurgeSystemMap")


def GetIconNumOfShip(ship):
	try:
		FdtnShips = Foundation.shipList
		for index in range(len(FdtnShips)):
			pShip = FdtnShips[index]
			shipScript = ship.GetScript()
			strShip = string.split(shipScript, '.')[-1]
			if pShip.GetShipFile() == strShip:
				return pShip.GetIconNum()
	except:
		LogError("GetIconNumOfShip")


def LogError(strFromFunc):
	import sys
	et = sys.exc_info()
	if strFromFunc == None:
		strFromFunc = "???"
	if Logger:
		Logger.LogException(et, "ERROR at "+strFromFunc)
	else:
		error = str(et[0])+": "+str(et[1])
		print "ERROR at "+strFromFunc+", details -> "+error
