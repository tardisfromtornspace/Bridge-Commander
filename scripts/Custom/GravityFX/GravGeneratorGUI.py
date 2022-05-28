################################################################
#######  GravGeneratorGUI Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# This is the script that handles the Gravity Generator Options Menu in-game
####################################################################
import App
import MissionLib
import Custom.GravityFX.Logger
from GravityFXlib import *
from ListLib import *
GUILIB = __import__('GravityFXguilib')

pGUICreator = None
Logger = None
ET_GG = None
ET_POWERBAR = None
eRefresh = None
dBarToGen = {}
iPlayerID = 0

def CreateGravGenGUI():
	global pGUICreator, ET_GG, Logger, iPlayerID, ET_POWERBAR, eRefresh
	try:
		pGUICreator = GUILIB.GUICreator()
		pMission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
		pBridge = App.g_kSetManager.GetSet('bridge')
		pEngineer = App.CharacterClass_GetObject(pBridge, "Engineer")
		pEngMenu = pEngineer.GetMenu()
		if GetConfigValue("LogGravGen"):
			Logger = Custom.GravityFX.Logger.LogCreator("Grav Generator Logger", "scripts\Custom\GravityFX\Logs\GravGeneratorLOG.txt")
			Logger.LogString("Initialized Grav Generator logger")
		else:
			Logger = Custom.GravityFX.Logger.DummyLogger()

		ET_POWERBAR = GUILIB.GetNextEventType()
		ET_GG = GUILIB.GetNextEventType()
		App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_GG, pMission, __name__+".GravGenOpenClose")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_POWERBAR, pMission, __name__+".GravGenPowerChanged")		

		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			GW = App.g_kGravityManager.GetGravWell(pPlayer.GetName())
			if GW:
				if GW.Generator != None:
					iPlayerID = pPlayer.GetObjID()
		pGUICreator.ButtonCreator.CreateButton("Gravity Generator Options", ET_GG, None, 1, pEngMenu)
		
		pEngineer.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__+".GravGenClose")

		eRefresh = RefreshEventHandler(UpdateGravGenGUI, 0.1)
		
		Logger.LogString("Created GravGen GUI")
	except:
		LogError("CreateGravGenGUI")

def GravGenOpenClose(pObject, pEvent):
	try:
		pGG = pGUICreator.GetElement("Gravity Generator Options Menu")
		if not pGG:
			pGUICreator.SetInfoForName("Gravity Generator Options Menu", 0.32, 0.1, 0.3, 0.6, 0)
			pTCW = App.TacticalControlWindow_GetTacticalControlWindow()
			pGG = pGUICreator.CreateWindow("Gravity Generator Options Menu", pTCW)
			Logger.LogString("Created GravGen Menu")
			pGG.AddPythonFuncHandlerForInstance(App.ET_MOUSE, __name__+".MouseHandler")
			CreateGravGenContents()
		if pGG.IsVisible():
			Logger.LogString("Showing GravGen")
			pGUICreator.CloseElement("Gravity Generator Options Menu")
		else:
			Logger.LogString("Closing GravGen")
			pGUICreator.ShowElement("Gravity Generator Options Menu")
	except:
		LogError("GravGenOpenClose")

def CreateGravGenContents():
	try:
		global dBarToGen, ET_POWERBAR
		pGG = pGUICreator.GetElement("Gravity Generator Options Menu")

		sName2 = ["Gravity Well Generator System Status:"]
		pGUICreator.SetInfoForName("GravGen StatTitle", 0.0, 0.01)
		pStatTitle = pGUICreator.CreateParagraph("GravGen StatTitle", sName2, pGG)

		sName4 = ["Gravity Well Info: Un-Updated"]
		pGUICreator.SetInfoForName("GravWell Info", 0.0, 0.32)
		pGUICreator.CreateParagraph("GravWell Info", sName4, pGG)

		pGUICreator.SetInfoForName("Gravity Generator List:", 0.0, 0.03, 0.3, 0.29, 1)
		pWin = pGUICreator.CreateWindow("Gravity Generator List:", pGG)
		pWin.SetUseScrolling(1)
		pWin.SetScrollViewHeight(25.0)
		pGUICreator.ShowElement("Gravity Generator List:")

		CreatePowerBars()

		CloseButtonDict = {'X': 0.0, 'Y': 0.5, 'WIDTH': 0.1, 'HEIGTH': 0.03}
		pGUICreator.ButtonCreator.CreateButton("Close", None, __name__+".GravGenClose", 0, pGG, CloseButtonDict , CloseButtonDict )

		Logger.LogString("Created GravGen Static Contents")
	except:
		LogError("CreateGravGenContents")

def GravGenClose(pObject, pEvent):
	try:
		if pGUICreator.ButtonCreator.GetButtonByName("Gravity Generator Options"):
			pGUICreator.CloseElement("Gravity Generator Options Menu")  
			Logger.LogString("Closed GravGen")
		pObject.CallNextHandler(pEvent)
	except:
		LogError("GravGenClose")

def GravGenPowerChanged(pObject, pEvent):
	try:
		global dBarToGen
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			GW = App.g_kGravityManager.GetGravWell(pPlayer.GetName())
			if GW and GW.Generator != None:
				pPowerBar = App.STNumericBar_Cast(pEvent.GetSource())
				if pPowerBar:
					pGen = dBarToGen[pPowerBar.GetObjID()]
					GW.Generator.SetPowerPercentageOfGen(pGen, pPowerBar.GetValue())
	except:
		LogError("GravGenPowerChanged")

def UpdateGravGenGUI(pObject, pEvent):
	try:
		global iPlayerID, dBarToGen
		
		pGGButt = pGUICreator.ButtonCreator.GetButtonByName("Gravity Generator Options")
		pInfoPara = pGUICreator.GetElement("GravWell Info")
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer:
			GW = App.g_kGravityManager.GetGravWell(pPlayer.GetName())
			if pPlayer.GetObjID != iPlayerID:
				# Reset GUI  -  Player Changed
				if pGGButt:
					if GW and GW.Generator != None:
						pGGButt.SetEnabled()
					else:
						pGGButt.SetDisabled()
				else:
					if GW and GW.Generator != None:
						pBridge = App.g_kSetManager.GetSet('bridge')
						pEngineer = App.CharacterClass_GetObject(pBridge, "Engineer")
						pGUICreator.ButtonCreator.CreateButton("Gravity Generator Options", None, __name__+".GravGenOpenClose", 1, pEngineer.GetMenu())
				iPlayerID = pPlayer.GetObjID()
				CreatePowerBars(1)
			else:
				if pGGButt and pGGButt.IsEnabled() == 0 and GW and GW.Generator != None:
					pGGButt.SetEnabled()

			if dBarToGen:
				lBarsIDs = dBarToGen.keys()
				for ID in lBarsIDs:
					pGen = dBarToGen[ID]
					sStat = "not-updated"
					if GW:
						if GW.Generator != None:
							if pGen.GetCondition() <= 0:
								sStat = "Destroyed"
							elif pGen.IsDisabled():
								sStat = "Disabled"
							elif GW.Generator.GetPowerPercentageOfGen(pGen) > 0:
								sStat = "Online"
							else:
								sStat = "Offline"
						else:
							sStat = "Not Present"
					else:
						sStat = "No Grav Well"
					pPowerBar = App.STNumericBar_Cast(App.TGObject_GetTGObjectPtr(ID))
					pPowerBar.GetText().SetStringW(App.TGString(pGen.GetName()+" Power: "+sStat))

			if pInfoPara:
				InfoList = []
				if GW:
					InfoList.append("Gravity Well Info:")
					InfoList.append("-Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Radius))+" Kms")
					InfoList.append("-Ship Mass: "+str(GW.Parent.GetMass()))
					InfoList.append("-Ship Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.Parent.GetRadius()))+" Kms")
					InfoList.append("-Gravity Well Mass: "+str(GW.Mass))
					InfoList.append("-Power Used Per Second: "+GetStrFromFloat(GW.GetPowerNeedPerSecond()))
					InfoList.append("-Damage Distance Radius: "+GetStrFromFloat(ConvertGUtoKM(GW.MaxDamageDistance))+" Kms")
					InfoList.append("-Age: "+GetStrFromFloat(GW.Age)+" Secs")
					InfoList.append("-Type: "+str(GW.Type))
				else:
					InfoList.append("No Gravity Well")
				pGUICreator.UpdateParagraph("GravWell Info", InfoList)
		elif pGGButt:
			pGGButt.SetDisabled()
	except:
		LogError("UpdateGravGenGUI")

def CreatePowerBars(bPurgeFirst = 0):
	try:
		global dBarToGen, ET_POWERBAR
		if bPurgeFirst == 1:
			lOldGens = dBarToGen.values()
			for pOldGen in lOldGens:
				pGUICreator.ButtonCreator.DeleteButtonByName(pOldGen.GetName()+" Power")
			dBarToGen = {}
		pWin = pGUICreator.GetElement("Gravity Generator List:")
		pPlayer = App.Game_GetCurrentPlayer()
		fValue = 1.0
		if pPlayer and pWin:
			GW = App.g_kGravityManager.GetGravWell(pPlayer.GetName())
			if GW and GW.Generator != None:
				PowerBarDict = {'X': 0.0, 'Y': 0.0, 'WIDTH': 0.28, 'HEIGTH': 0.03}
				for pGen in GW.Generator.Generators:
					fValue = GW.Generator.GetPowerPercentageOfGen(pGen)
					pPowerBar = pGUICreator.ButtonCreator.CreateBar(pGen.GetName()+" Power", ET_POWERBAR, None, fValue, [0.0, 10.0], 1.0, 0, pWin, PowerBarDict, PowerBarDict)	
					dBarToGen[pPowerBar.GetObjID()] = pGen
					PowerBarDict['Y'] = PowerBarDict['Y'] + PowerBarDict['HEIGTH']		
				pWin.InteriorChangedSize()
	except:
		LogError("CreatePowerBars")

def MouseHandler(pObject, pEvent):
	try:
		pObject.CallNextHandler(pEvent)
		if pEvent.EventHandled() == 0:
			pEvent.SetHandled()
	except:
		LogError("MouseHandler")

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