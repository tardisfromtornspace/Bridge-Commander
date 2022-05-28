################################################################
#######  AstrometricsGUI Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is the script that handles the astrometrics features in-game
# (informative text on BC's 3D map)
####################################################################
import App
import MissionLib
import Custom.GravityFX.Logger
from GravityFXlib import *
from ListLib import *
GUILIB = __import__('GravityFXguilib')
GravSensors = __import__('Custom.GravityFX.GravSensorsOptGUI')

pGUICreator = None
eRefresh = None
Logger = None
MapID = 0
MapObjsList = []
MapIDlist = []
bMapVisible = 0
bMapContPurged = 1

def CreateAstroGUI():
	global pGUICreator, eRefresh, Logger
	try:
		pGUICreator = GUILIB.GUICreator()
		if GetConfigValue("LogAstro"):
			Logger = Custom.GravityFX.Logger.LogCreator("Astrometrics Logger", "scripts\Custom\GravityFX\Logs\AstrometricsLOG.txt")
			Logger.LogString("Initialized Astrometrics logger")
		else:
			Logger = Custom.GravityFX.Logger.DummyLogger()

		eRefresh = RefreshEventHandler(UpdateGUI, 0.05)
		
		Logger.LogString("Created Astro GUI")
	except:
		LogError("CreateAstroGUI")

def Create3DMapContent():
	try:
		pTCW = App.TopWindow_GetTopWindow()  #App.TacticalControlWindow_GetTacticalControlWindow()
		if pTCW:
			if pGUICreator.GetElement("3DMap Content Pane"):
				pGUICreator.DeleteElement("3DMap Content Pane")
			pGUICreator.SetInfoForName("3DMap Content Pane", 0.0, 0.0, 1.0, 1.0)
			pGUICreator.CreatePane("3DMap Content Pane", pTCW)
			Logger.LogString("Created 3D Map Content Pane")
	except:
		LogError("Create3DMapContent")

def Show3DMapContent():
	try:
		global bMapVisible
		if bMapVisible == 0:
			pGUICreator.ShowElement("3DMap Content Pane")
			bMapVisible = 1
			Logger.LogString("Show 3D Map Content Pane")
	except:
		LogError("Show3DMapContent")

def Close3DMapContent():
	try:
		global bMapVisible
		if bMapVisible == 1:
			pGUICreator.CloseElement("3DMap Content Pane")
			bMapVisible = 0
			# Now when closing the 3D Map delete the Content Pane.
			# Why? Because doing it will fix a bug that was causing when you opened the map for the second time 
			#  the paragraphs to not show up
			# Why? Ask TG. They're the ones who coded the game and these misterious bugs.
			pGUICreator.DeleteElement("3DMap Content Pane")
			Logger.LogString("Close 3D Map Content Pane")
	except:
		LogError("Close3DMapContent")

def UpdateGUI(pObject, pEvent):
	try:
		global MapIDlist, bMapContPurged
		pMapWindow = Get3DMapWindow()
		pEAButton = GravSensors.pGUICreator.ButtonCreator.GetButtonByName("Enable Astrometrics")
		if pMapWindow and pEAButton:
			if pGUICreator.GetElement("3DMap Content Pane") == None:
				Create3DMapContent()
			if pMapWindow.IsWindowActive() == 0 or pEAButton.IsChosen() == 0:
				if bMapContPurged == 0:
					for sName in MapIDlist:
						pGUICreator.DeleteElement(sName)
					pPane = pGUICreator.GetElement("3DMap Content Pane")
					if pPane:
						pPane.KillChildren()
						Logger.LogString("3DMap Content Pane Killed Children")
					bMapContPurged = 1
					Logger.LogString("3DMap Content Purged")
				Close3DMapContent()
			elif pMapWindow.IsWindowActive() == 1 and pEAButton.IsChosen():
				Show3DMapContent()
				Update3DWellInfo()
				if bMapContPurged == 1:
					bMapContPurged = 0
	except:
		LogError("UpdateGUI")
	
def Update3DWellInfo():
	global MapObjsList, MapIDlist
	try:
		pPane = pGUICreator.GetElement("3DMap Content Pane")
		if not pPane:
			return
		ObjsList = GetObjsInSet()
		for pObj in MapObjsList:
			if IsObjInList(pObj, ObjsList):
				# update 
				pIPara = UpdateInfoOnObj(pObj)   # this actually updates / creates
			else:
				#delete pObj para
				Logger.LogString("Astro:   Deleting "+pObj.GetName()+" 3D Map Paragraph")
				pGUICreator.DeleteElement(str(pObj.GetObjID()))
				if str(pObj.GetObjID()) in MapIDlist:
					MapIDlist.remove(str(pObj.GetObjID()))
		MapObjsList = ObjsList
	except:
		LogError("Update3DWellInfo")

def UpdateInfoOnObj(pObject):
	global MapIDlist
	try:
		pPane = pGUICreator.GetElement("3DMap Content Pane")
		if pObject and pPane:
			sName = str(pObject.GetObjID())
			pPara = pGUICreator.GetElement(sName)
			sList = App.g_kGravityManager.GetGravInfoOnObj(pObject, 1)
			tCoords = GetScreenCoordsForObj(pObject)
			X, Y = tCoords[0], tCoords[1]
			if pPara == None:
				pGUICreator.SetInfoForName(sName, X, Y)
				pGUICreator.CreateParagraph(sName, sList, pPane)
				MapIDlist.append(sName)
			else:
				if pObject.IsTypeOf(App.CT_SHIP):
					if pObject.IsCloaked():
						X, Y = -1.0, -1.0
				pGUICreator.UpdateParagraph(sName, sList)
				pPara.SetPosition(X, Y)
			return pPara
	except:
		LogError("UpdateInfoOnObj")

def GetObjsInSet(pSet = None):
	try:
		if pSet == None:
			pPlayer = App.Game_GetCurrentPlayer()
			pSet = pPlayer.GetContainingSet()
		List = []
		if pSet == None:
			return List
		for pObj in pSet.GetClassObjectList(App.CT_SHIP):
			List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_WAYPOINT):
			List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_SUN):
			if pObj.IsAtmosphereObj() == None:
				List.append(pObj)
		for pObj in pSet.GetClassObjectList(App.CT_PLANET):
			if pObj.IsAtmosphereObj() == None:
				List.append(pObj)
		return List	
	except:
		LogError("GetObjsInSet")


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