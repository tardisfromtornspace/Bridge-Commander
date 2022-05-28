from bcdebug import debug
###############################################################################
## GravityFX Config plugin for UMM			by Fernando Aluanu aka USS Frontier
#######
# The purpose of this is to let users easily modify some key configuration aspects of the GravityFX mod easily,
# in the Main Menu of BridgeCommander.
# With this users will be able to set the System Map scale, the Gravity Force multiplying factor, to leave the
# grav force with it's real value or up to 2000 times stronger, to set or no a random density for the planets/suns
# that came with BC. And maybe some other things.
################################################################################
import App
import Foundation
import string
import nt
from Custom.GravityFX.GravityFXguilib import *

pModule = __import__("SavedConfigs.GravityFXConfigValues")
pBar = None
pSetButton = None
pSMScaleBar = None
pSMScaleButton = None
SetUseLog = {}
pCloseDmgBar = None
pStationsButton = None
pThrusterStat = None

#####################################################
## Required Functions for UMM
#############################################
def GetName():
	debug(__name__ + ", GetName")
	return "GravityFX Config"

def CreateMenu(pOptionsPane, pContentPanel, bGameEnded = 0):
	debug(__name__ + ", CreateMenu")
	CreateGravFXConfigMenu(pOptionsPane, pContentPanel)
	ET_SAVE = GetNextEventType()
	pSaveButton = CreateMenuButton("Save Configuration", ET_SAVE, 0)
	pContentPanel.AddChild(pSaveButton)
	pTopWindow = App.TopWindow_GetTopWindow()
	pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)
	pOptionsWindow.AddPythonFuncHandlerForInstance(ET_SAVE, __name__ + ".SaveConfig")
	return App.TGPane_Create(0,0)
##########################################################


#####################################################
## Helper Functions
#############################################
def CreateGravFXConfigMenu(pOptionsPane, pContentPanel):
	debug(__name__ + ", CreateGravFXConfigMenu")
	global pBar, pSetButton, pModule, pSMScaleBar, pSMScaleButton, SetUseLog, pCloseDmgBar, pStationsButton, pThrusterStat
	ET_BAR = GetNextEventType()
	nValue = pModule.GravForceXvalue
	WIDTH = 0.32
	pBar = CreateVolumeButton("Gravity Force Multiplying Factor", ET_BAR, nValue, WIDTH, nRange = [1.0, 2000.0], nMarker = 1.0)
	pContentPanel.AddChild(pBar)

	ET_SMSCALE_BAR = GetNextEventType()
	nSMScaleValue = pModule.SystemMapScale
	WIDTH = 0.32
	pSMScaleBar = CreateVolumeButton("System Map Scale", ET_SMSCALE_BAR, nSMScaleValue, WIDTH, nRange = [1.0, 100000.0], nMarker = 5000.0)
	pContentPanel.AddChild(pSMScaleBar)

	ET_SET_SMSCALE_LIGHTYEAR = GetNextEventType()
	pSMScaleButton = CreateMenuYesNoButton("Set System Map Scale to 1 Lightyear", ET_SET_SMSCALE_LIGHTYEAR, pModule.SetSMScaleLightyear)
	pContentPanel.AddChild(pSMScaleButton)

	ET_SET_STOCK_PLANETS_DENSITY = GetNextEventType()
	pSetButton = CreateMenuYesNoButton("Set Stock Planets Random Density", ET_SET_STOCK_PLANETS_DENSITY, pModule.SetStockPlanetsDensity)
	pContentPanel.AddChild(pSetButton)

	ET_CLOSE_DMG = GetNextEventType()
	nCDValue = pModule.GravDmgFac
	WIDTH = 0.32
	pCloseDmgBar = CreateVolumeButton("Gravity Damage Factor", ET_CLOSE_DMG, nCDValue, WIDTH, nRange = [0.0, 100.0], nMarker = (1.0/120*100))
	pContentPanel.AddChild(pCloseDmgBar)

	ET_STATIONS_AFFECT = GetNextEventType()
	pStationsButton = CreateMenuYesNoButton("Gravity will affect Stations?", ET_STATIONS_AFFECT, pModule.StationsAreAffected)
	pContentPanel.AddChild(pStationsButton)

	ET_THRUSTER_STATE = GetNextEventType()
	pThrusterStat = CreateMenuYesNoButton("Initial Thruster State", ET_THRUSTER_STATE, pModule.ThrusterState)
	pContentPanel.AddChild(pThrusterStat)

	pSULMenu = CreateCharMenu("Produce Logs about GravityFX Activities", pContentPanel)

	ET_USE_LOGS = GetNextEventType()
	SetUseLog['LoadGravityFX'] = CreateMenuYesNoButton("Log LoadGravityFX script Activities", ET_USE_LOGS, pModule.SetUseLogs.LoadGravityFX)
	pSULMenu.AddChild(SetUseLog['LoadGravityFX'])

	ET_USE_LOGS2 = GetNextEventType()
	SetUseLog['GravityManager'] = CreateMenuYesNoButton("Log Gravity Manager Activities", ET_USE_LOGS2, pModule.SetUseLogs.GravityManager)
	pSULMenu.AddChild(SetUseLog['GravityManager'])

	ET_USE_LOGS3 = GetNextEventType()
	SetUseLog['GravWellPlugins'] = CreateMenuYesNoButton("Log GravWellPlugins Activities", ET_USE_LOGS3, pModule.SetUseLogs.GravWellPlugins)
	pSULMenu.AddChild(SetUseLog['GravWellPlugins'])

	ET_USE_LOGS4 = GetNextEventType()
	SetUseLog['TorpGravEffects'] = CreateMenuYesNoButton("Log TorpGravEffects Activities", ET_USE_LOGS4, pModule.SetUseLogs.TorpGravEffects)
	pSULMenu.AddChild(SetUseLog['TorpGravEffects'])

	ET_USE_LOGS5 = GetNextEventType()
	SetUseLog['SystemMap'] = CreateMenuYesNoButton("Log System Map Activities", ET_USE_LOGS5, pModule.SetUseLogs.SystemMap)
	pSULMenu.AddChild(SetUseLog['SystemMap'])

	ET_USE_LOGS6 = GetNextEventType()
	SetUseLog['GravSensors'] = CreateMenuYesNoButton("Log Grav Sensors Activities", ET_USE_LOGS6, pModule.SetUseLogs.GravSensors)
	pSULMenu.AddChild(SetUseLog['GravSensors'])

	ET_USE_LOGS7 = GetNextEventType()
	SetUseLog['GravWells'] = CreateMenuYesNoButton("Log Grav Wells Activities", ET_USE_LOGS7, pModule.SetUseLogs.GravWells)
	pSULMenu.AddChild(SetUseLog['GravWells'])

	ET_USE_LOGS8 = GetNextEventType()
	SetUseLog['Astrometrics'] = CreateMenuYesNoButton("Log Astrometrics Activities", ET_USE_LOGS8, pModule.SetUseLogs.Astrometrics)
	pSULMenu.AddChild(SetUseLog['Astrometrics'])

	ET_USE_LOGS9 = GetNextEventType()
	SetUseLog['GravGen'] = CreateMenuYesNoButton("Log Grav Generator Activities", ET_USE_LOGS9, pModule.SetUseLogs.GravGenerator)
	pSULMenu.AddChild(SetUseLog['GravGen'])

	return pContentPanel

def SaveConfig(pObject, pEvent):
	debug(__name__ + ", SaveConfig")
	global pBar, pSetButton, pStationsButton, pThrusterStat 
	GravForceXvalue = pBar.GetValue()
	if GravForceXvalue == 0.0:
		GravForceXvalue = 1.0
	nSystemMapScale = pSMScaleBar.GetValue()
	if nSystemMapScale < 1.0:
		nSystemMapScale = 1.0
	ConfigPath  = "scripts\\Custom\\UnifiedMainMenu\\ConfigModules\\Options\\SavedConfigs\\GravityFXConfigValues.py"
	file = nt.open(ConfigPath, nt.O_WRONLY | nt.O_TRUNC | nt.O_CREAT | nt.O_BINARY)
	nt.write(file, "# Saved Configuration File for Gravity FX,   by USS Frontier" + "\n")
	nt.write(file, "GravForceXvalue = " + str(GravForceXvalue) + "\n")
	nt.write(file, "SetStockPlanetsDensity = " + str(pSetButton.IsChosen()) + "\n")
	nt.write(file, "SystemMapScale = " + str(nSystemMapScale) + "\n")
	nt.write(file, "SetSMScaleLightyear = " + str(pSMScaleButton.IsChosen()) + "\n")
	nt.write(file, "GravDmgFac = " + str(pCloseDmgBar.GetValue()) + "\n")
	nt.write(file, "class SetUseLogs:" + "\n")
	nt.write(file, "\t"+ "LoadGravityFX = " +str(SetUseLog['LoadGravityFX'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "GravityManager = " +str(SetUseLog['GravityManager'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "GravWellPlugins = " +str(SetUseLog['GravWellPlugins'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "TorpGravEffects = " +str(SetUseLog['TorpGravEffects'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "SystemMap = " +str(SetUseLog['SystemMap'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "GravSensors = " +str(SetUseLog['GravSensors'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "GravWells = " +str(SetUseLog['GravWells'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "Astrometrics = " +str(SetUseLog['Astrometrics'].IsChosen())+ "\n")
	nt.write(file, "\t"+ "GravGenerator = " +str(SetUseLog['GravGen'].IsChosen())+ "\n")
	nt.write(file, "StationsAreAffected = "+str(pStationsButton.IsChosen()) + "\n")
	nt.write(file, "ThrusterState = "+str(pThrusterStat.IsChosen()) + "\n")
	nt.close(file)

	pModule.GravForceXvalue = GravForceXvalue
	pModule.SetStockPlanetsDensity = pSetButton.IsChosen()
	pModule.SystemMapScale = nSystemMapScale
	pModule.SetSMScaleLightyear = pSMScaleButton.IsChosen()
	pModule.GravDmgFac = pCloseDmgBar.GetValue()
	pModule.SetUseLogs.LoadGravityFX = SetUseLog['LoadGravityFX'].IsChosen()
	pModule.SetUseLogs.GravityManager = SetUseLog['GravityManager'].IsChosen()
	pModule.SetUseLogs.GravWellPlugins = SetUseLog['GravWellPlugins'].IsChosen()
	pModule.SetUseLogs.TorpGravEffects = SetUseLog['TorpGravEffects'].IsChosen()
	pModule.SetUseLogs.SystemMap = SetUseLog['SystemMap'].IsChosen()
	pModule.SetUseLogs.GravSensors = SetUseLog['GravSensors'].IsChosen()
	pModule.SetUseLogs.GravWells = SetUseLog['GravWells'].IsChosen()
	pModule.SetUseLogs.Astrometrics = SetUseLog['Astrometrics'].IsChosen()
	pModule.SetUseLogs.GravGenerator = SetUseLog['GravGen'].IsChosen()
	pModule.StationsAreAffected = pStationsButton.IsChosen()
	pModule.ThrusterState = pThrusterStat.IsChosen()
