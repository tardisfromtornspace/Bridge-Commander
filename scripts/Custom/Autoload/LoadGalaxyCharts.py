from bcdebug import debug
################################################################
#######  LoadGalaxyCharts Script ###################
################################################################
#################        by Fernando Aluani aka USS Frontier
############################################################
# Here's the autoload script of Galaxy Charts, it loads and sets up everything.
####################################################################
##########################################################################################################################
##### Importing our champion team     ####################################################################################
##########################################################################################################################
import App
import Foundation
import MissionLib
import Custom.GalaxyCharts.Galaxy
import Custom.GalaxyCharts.GalaxyLIB
import Custom.GalaxyCharts.Cartographer
from Custom.GalaxyCharts.GalacticWarSimulator import WarSimulator
import Custom.GalaxyCharts.GalaxyMapGUI
import Custom.GalaxyCharts.ChronoInfoGUI
import Custom.GalaxyCharts.HelmAddonGUI
import Custom.GalaxyCharts.StrategicCommandGUI
import Custom.GalaxyCharts.Traveler
import Custom.GalaxyCharts.TravelerAI_Override
import Custom.Systems.PluginUtils                   # this will load the system plugins
from Custom.GalaxyCharts.GalaxyLIB import *
import Custom.Eras                              # this will load the Era plugins. (must be after loading system plugins)
import Custom.GravityFX.Logger

NonSerializedObjects = (
"oGalaxyTrigger",
"oRandomDefenceForceTrigger",
"oGalaxyDelTrigger",
"PauseTriggerOpt",
"PauseTriggerCon",
"oCoreEjectFix",
)

##########################################################################################################################
##### Foundation Related Defs      #######################################################################################
##########################################################################################################################
mode = Foundation.MutatorDef("USS Frontier's Galaxy Charts")

### System Related Overrides
Foundation.OverrideDef('zzzOverrideCreateSystemMenus', 'Systems.Utils.CreateSystemMenu', 'Custom.GalaxyCharts.Cartographer.CreateSystemMenu_Override', dict = { "modes": [ mode ] } )

### Helm Related Overrides
Foundation.OverrideDef('zzzOverrideHelmWarp', 'Bridge.HelmMenuHandlers.WarpPressed', 'Custom.GalaxyCharts.GalaxyMapGUI.WarpClick', dict = { "modes": [ mode ] } )

### AI Related Overrides
Foundation.OverrideDef('zzzGalaxyWarpAI', 'AI.PlainAI.Warp.Warp', 'Custom.GalaxyCharts.TravelerAI_Override.TravelerWarp', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef('zzzGalaxyFollowWarpAI', 'AI.PlainAI.FollowThroughWarp.FollowThroughWarp', 'Custom.GalaxyCharts.TravelerAI_Override.TravelerFollowThroughWarp', dict = { 'modes': [ mode ] } )

try:
	import Custom.NanoFXv2.WarpFX.AI.NanoWarp
	Foundation.OverrideDef('zzzNanoGalaxyWarpAI', 'Custom.NanoFXv2.WarpFX.AI.NanoWarp.NanoWarp', 'Custom.GalaxyCharts.TravelerAI_Override.TravelerWarp', dict = { 'modes': [ mode ] } )
except:
	pass
try:
	import Custom.NanoFXv2.WarpFX.AI.NanoFollowThroughWarp
	Foundation.OverrideDef('zzzNanoGalaxyFollowWarpAI', 'Custom.NanoFXv2.WarpFX.AI.NanoFollowThroughWarp.NanoFollowThroughWarp', 'Custom.GalaxyCharts.TravelerAI_Override.TravelerFollowThroughWarp', dict = { 'modes': [ mode ] } )
except:
	pass

Foundation.OverrideDef('zzzCompoundFTW_AI', 'AI.Compound.FollowThroughWarp.CreateAI', 'Custom.GalaxyCharts.TravelerAI_Override.CreateAI', dict = { 'modes': [ mode ] } )

Foundation.OverrideDef('zzzWarpInterceptAI', 'AI.PlainAI.Intercept.Intercept', 'Custom.GalaxyCharts.WarpIntercept.WarpIntercept', dict = { "modes": [ mode ] } )

#MethodOverrideDef('WarAI_FleetSelectTarget', 'AI.Preprocessors', 'SelectTarget', 'FindGoodTarget', 'Custom.GalaxyCharts.WarAI.FindGoodTarget_UpdateForFleet', dict = { 'modes': [ mode ] } )

### Warp Sequence Related Overrides
MethodOverrideDef('WEGalaxyGetPlacement', 'App', 'WarpEngineSubsystem', 'GetPlacement', 'Custom.GalaxyCharts.WarpSequence_Override.GetPlacement', dict = { 'modes': [ mode ] } )
MethodOverrideDef('WEGalaxyGetWarpExit', 'App', 'WarpEngineSubsystem', 'GetWarpExitLocation', 'Custom.GalaxyCharts.WarpSequence_Override.GetWarpExitLocation', dict = { 'modes': [ mode ] } )
MethodOverrideDef('WEGalaxyGetExitRot', 'App', 'WarpEngineSubsystem', 'GetWarpExitRotation', 'Custom.GalaxyCharts.WarpSequence_Override.GetWarpExitRotation', dict = { 'modes': [ mode ] } )
MethodOverrideDef('WEGalaxyGetSequence', 'App', 'WarpEngineSubsystem', 'GetWarpSequence', 'Custom.GalaxyCharts.WarpSequence_Override.GetWarpSequence', dict = { 'modes': [ mode ] } )
MethodOverrideDef('WEGalaxyWarp', 'App', 'WarpEngineSubsystem', 'Warp', 'Custom.GalaxyCharts.WarpSequence_Override.Warp', dict = { 'modes': [ mode ] } )
MethodOverrideDef('WEGalaxtySetPlacement', 'App', 'WarpEngineSubsystem', 'SetPlacement', 'Custom.GalaxyCharts.WarpSequence_Override.SetPlacement', dict = { 'modes': [ mode ] } )
MethodOverrideDef('WEGalaxySetExitPoint', 'App', 'WarpEngineSubsystem', 'SetExitPoint', 'Custom.GalaxyCharts.WarpSequence_Override.SetExitPoint', dict = { 'modes': [ mode ] } )

Foundation.OverrideDef('WSGalaxyCreate', 'App.WarpSequence_Create', 'Custom.GalaxyCharts.WarpSequence_Override.WarpSequence_Create', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef('WSGalaxyCast', 'App.WarpSequence_Cast', 'Custom.GalaxyCharts.WarpSequence_Override.WarpSequence_Cast', dict = { 'modes': [ mode ] } )
Foundation.OverrideDef('WSGalaxyGetWarpSet', 'App.WarpSequence_GetWarpSet', 'Custom.GalaxyCharts.WarpSequence_Override.WarpSequence_GetWarpSet', dict = { 'modes': [ mode ] } )

Foundation.OverrideDef('GalaxyWarpSequence', 'App.WarpSequence', 'Custom.GalaxyCharts.WarpSequence_Override.TravelerWarpSequence', dict = { 'modes': [ mode ] } )

### Ship Class Related Overrides
MethodOverrideDef('GCInSystemWarp', 'App', 'ShipClass', 'InSystemWarp', 'Custom.GalaxyCharts.TravelerAI_Override.ShipClass_InSystemWarp', dict = { 'modes': [ mode ] } )
MethodOverrideDef('GCStopInSystemWarp', 'App', 'ShipClass', 'StopInSystemWarp', 'Custom.GalaxyCharts.TravelerAI_Override.ShipClass_StopInSystemWarp', dict = { 'modes': [ mode ] } )
MethodOverrideDef('GCIsDoingInSystemWarp', 'App', 'ShipClass', 'IsDoingInSystemWarp', 'Custom.GalaxyCharts.TravelerAI_Override.ShipClass_IsDoingInSystemWarp', dict = { 'modes': [ mode ] } )

Foundation.OverrideDef('QBShipDestroyed', 'QuickBattle.QuickBattle.ShipDestroyed', 'Custom.GalaxyCharts.GalacticWarSimulator.QBShipDestroyed_Override', dict = { 'modes': [ mode ] } )

##########################################################################################################################
##### Direct Method Overrides/Adds #######################################################################################
##########################################################################################################################
# no problem with these because it's a simple creation of a method for App.ShipClass, since these methods shouldn't
# exist in BC.
App.ShipClass.GetWarpSpeed = Custom.GalaxyCharts.GalaxyLIB.ShipClass_GetWarpSpeed
App.ShipClass.GetMaxWarpSpeed = Custom.GalaxyCharts.GalaxyLIB.ShipClass_GetMaxWarp
App.ShipClass.GetCruiseWarpSpeed = Custom.GalaxyCharts.GalaxyLIB.ShipClass_GetCruiseWarp
App.ShipClass.SetWarpSpeed = Custom.GalaxyCharts.GalaxyLIB.ShipClass_SetWarpSpeed

# these we do here because they aren't overrides. It's a simple copy of a method to another name.
# the real overrides we do above, using the MethodOverrideDef
App.ShipClass.Intercept = App.ShipClass.InSystemWarp
App.ShipClass.StopIntercept = App.ShipClass.StopInSystemWarp
App.ShipClass.IsIntercepting = App.ShipClass.IsDoingInSystemWarp


#App.ShipClass.InSystemWarp = Custom.GalaxyCharts.TravelerAI_Override.ShipClass_InSystemWarp
#App.ShipClass.StopInSystemWarp = Custom.GalaxyCharts.TravelerAI_Override.ShipClass_StopInSystemWarp
#App.ShipClass.IsDoingInSystemWarp = Custom.GalaxyCharts.TravelerAI_Override.ShipClass_IsDoingInSystemWarp


##########################################################################################################################
##### Trigger Classes/Initialization      ################################################################################
##########################################################################################################################

####################
### Entered Set - a lot of things xD
class GalaxyTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.Initialized = 0
		self.lNAVPoints = []
	def __call__(self, pObject, pEvent, dict = {}):
		# create just one time the Galaxy Map GUI
		debug(__name__ + ", __call__")
		if App.g_kUtopiaModule.IsMultiplayer():
			return
		if MissionLib.GetMission().GetScript() != "QuickBattle.QuickBattle":
			# only enable in QB right now
			return
		import Custom.Systems.PluginUtils
		Custom.Systems.PluginUtils.LoadSystemPlugins()
		if self.Initialized == 0:
			# CHECK if War Simulator is enabled in options. If it is, initialize it.
			bWarSimulatorEnabled = GetConfigValue("UseWarSim")
			try:
				if bWarSimulatorEnabled == 1:
					WarSimulator.Initialize()

				Custom.GalaxyCharts.HelmAddonGUI.CreateHAGUI()
				Custom.GalaxyCharts.GalaxyMapGUI.CreateGalaxyMapGUI()
				Custom.GalaxyCharts.ChronoInfoGUI.CreateCIGUI()
				Custom.GalaxyCharts.StrategicCommandGUI.CreateSCGUI()
				Custom.Eras.SetSelectedEraPlugin(GetSelectedEraName())
			except:
				Custom.GalaxyCharts.Galaxy.LogError("Galaxy Trigger Initialize")
			self.Initialized = 1
		pPlayer = App.Game_GetCurrentPlayer()
		pDestShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pDestShip != None and pPlayer != None:
			App.g_kTravelManager.CreateChaser(pDestShip, None)
			self.HandleLaunchCoordinatesNAVs(pDestShip.GetContainingSet())
			if pDestShip.GetObjID() == pPlayer.GetObjID():
				pSeq = App.TGSequence_Create()
				pAction = App.TGScriptAction_Create(__name__, "ApplyEraSettingsAction")
				pSeq.AddAction(pAction, None, 3.0)
				pSeq.Play()
	def HandleLaunchCoordinatesNAVs(self, pSet):
		debug(__name__ + ", HandleLaunchCoordinatesNAVs")
		try:
			#print "HLCNAVs: START"
			if pSet == None:
				return
			#print "HLCNAVs: MARK 1 - Set: ", pSet.GetName()
			# get the new NAVs info
			lTravelTypes = App.g_kTravelManager.GetAllTravelTypes()
			dNAVs = {}  # NAV name = pos
			for sTravelType in lTravelTypes:
				#print "HLCNAVs: checking travel type", sTravelType
				if App.g_kTravelManager.IsTravelTypeShipBased(sTravelType) == 0:
					#print "HLCNAVs: checked, is not ship based..."
					lCoords = App.g_kTravelManager.GetLaunchCoordinatesForTT(sTravelType, pSet)
					if len(lCoords) >= 1:
						#print "HLCNAVs: checked, has 1 or more launching coordinates"
						iIndex = 1
						for vPos in lCoords:
							sNAVName = sTravelType + " Coords " + str(iIndex)
							dNAVs[sNAVName] = vPos
							#print "HLCNAVs: added pair: ", sNAVName, vPos, "(", vPos.x, vPos.y, vPos.z, ")"
							iIndex = iIndex + 1

			# check if new NAVs are different than old NAVs
			bNAVsAreDifferent = 0
			if len(self.lNAVPoints) <= 0 and len(dNAVs.keys()) >= 1:
				bNAVsAreDifferent = 1
				#print "HLCNAVs: NAVs are different, old NAVPoints is empty and current one has 1 or more."
			else:
				for pNAV in self.lNAVPoints:
					if pNAV.GetName() in dNAVs.keys():
						vNewPos = dNAVs[pNAV.GetName()]
						vOldPos = pNAV.GetWorldLocation()
						if vNewPos.x != vOldPos.x or vNewPos.y != vOldPos.y or vNewPos.z != vOldPos.z:
							bNAVsAreDifferent = 1
							#print "HLCNAVs: NAVs are different: ", pNAV.GetName()
							break
					else:
						bNAVsAreDifferent = 1
						#print "HLCNAVs: NAVs are different, not in current: ", pNAV.GetName()
						break
			if bNAVsAreDifferent == 0:
				#print "HLCNAVs: NAVs are not different..."
				return

			# delete old NAVs
			for pToBeDelNAV in self.lNAVPoints:
				#print "HLCNAVs: deleting NAV ", pToBeDelNAV.GetName(), "("+str(pToBeDelNAV.GetObjID())+")"
				pToBeDelNAV.SetNavPoint(0)
				pToBeDelNAV.__del__()
				pToBeDelNAV = None
			self.lNAVPoints = []
			
			# finally create the new NAVs
			sNAVName = ""
			for sNAVName in dNAVs.keys():
				pNAVPoint = CreateNAVPoint(sNAVName, pSet, dNAVs[sNAVName])
				#print "HLCNAVs: created NAV ", sNAVName, "("+str(pNAVPoint.GetObjID())+")"
				self.lNAVPoints.append(pNAVPoint)
		except:
			Custom.GalaxyCharts.Galaxy.LogError("GalaxyTrigger: HandleLaunchCoordinatesNAVs")

			
def ApplyEraSettingsAction(pAction):
	# Just make a little call to make the Era that is selected to apply it's values.
	# because it may be possible that upon entering a set, some of them get back to defaults.
	debug(__name__ + ", ApplyEraSettingsAction")
	pEraPlugin = Custom.Eras.GetSelectedEraPlugin()
	if pEraPlugin != None:
		pEraPlugin.ApplyEraValues()
	return 0

oGalaxyTrigger = GalaxyTrigger('GalaxyCharts Trigger', App.ET_ENTERED_SET, dict = { 'modes': [ mode ] } )


######################
### RDF Trigger event - used for the Random Defence Force
class RandomDefenceForceTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.TravelSets = ["warp", "SlipstreamTunnel1", "HyperdriveTunnel1", "BajoranWormhole1"]

		if GetConfigValue("LogRDF") == 1:
			self.Logger = Custom.GravityFX.Logger.LogCreator("Random Defence Force Logger", "scripts\Custom\GalaxyCharts\Logs\RandomDefenceForceLOG.txt")
			self.Logger.LogString("Initialized Random Defence Force logger")
		else:
			self.Logger = Custom.GravityFX.Logger.DummyLogger()
	def GetRandomNum(self, fMin, fMax):
		debug(__name__ + ", GetRandomNum")
		if fMin == fMax:
			return fMin
		elif fMin > fMax:
			return fMax
		elif fMin < fMax:
			return GetRandomInRange(fMin, fMax)	
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		pConfig = GetConfigValue("GetRDFConfig")
		if pConfig.UseRDF == 0 or WarSimulator.IsInitialized() == 1:
			# User disabled Random Defence Force or has the war simulation going in
			#print "RDF is disabled"
			return
		# now handle the random defence force arrival
		pPlayer = App.Game_GetCurrentPlayer()
		#sExitedName = pEvent.GetCString()     # name of set from which object exited (in EXITED_SET event)
		sTravelTypeUsed = pEvent.GetCString()     # name of travel type from which object exited (in RDF_TRIGGER event)
		#if not sExitedName in self.TravelSets:
		#	# ship (or whatever lol) isn't exiting one of the sets used by travelling methods. So return here.
		#	return
		pDestShip = App.ShipClass_Cast(pEvent.GetDestination())
		pRegion = None
		pSet = None
		bCanCheckForRandomDefence = 0
		if pDestShip != None:
			#self.Logger.LogString("Ship "+pDestShip.GetName()+" is exiting set "+sExitedName)
			self.Logger.LogString("Ship "+pDestShip.GetName()+" is exiting travel. Travel Type: "+sTravelTypeUsed)
			pSet = pDestShip.GetContainingSet()
			if pSet != None:
				self.Logger.LogString("Ship "+pDestShip.GetName()+" is entering set "+pSet.GetName())
				pRegion = pSet.GetRegion()
			bAffectAIs = pConfig.AffectAI
			if bAffectAIs == 0:
				if pPlayer != None:
					if pDestShip.GetObjID() == pPlayer.GetObjID():
						bCanCheckForRandomDefence = 1
			else:
				bCanCheckForRandomDefence = 1
			self.Logger.LogString("Ship "+pDestShip.GetName()+" is of the race: "+GetShipRaceByWarSim(pDestShip))
		if pRegion != None and bCanCheckForRandomDefence == 1 and pPlayer != None:
			sEmpire = pRegion.GetControllingEmpire()
			self.Logger.LogString("Ship "+pDestShip.GetName()+" entered "+sEmpire+" territory...")
			pSetPlug = pRegion.GetSetByModule(pSet.GetRegionModule())
			pRaceObj = GetRaceClassObj(sEmpire)
			if sEmpire != "Unknown" and sEmpire != "None" and pRaceObj != None:
				# first we get all values and do the checks.
				self.Logger.LogString(sEmpire+" race class obj exists.")
				fChance = float(pConfig.DetectionChance)
				fFactor = App.g_kSystemWrapper.GetRandomNumber(100)
				bUsePeaceValues = pConfig.UsePeace
				bUseStrategicValue = pConfig.UseStrategic
				bUseEconomyValue = pConfig.UseEconomic
				bCloakCounts = pConfig.CloakCounts
				bUseDefaultDefence = pConfig.UseDefence
				iNumDefensiveShips = pRegion.GetNumDefensiveShips()

				## check peace value
				if bUsePeaceValues == 1:
					fPeaceValue = GetRacePeaceValue(sEmpire)
					fChance = fChance - ( fPeaceValue * 10 )
					# this "*10", is because as far as I saw, peace values are in the range of 0 to 1, so they
					# are pretty small, but if I multiply by 100 too they might get a bit very big :P
				if pSetPlug != None:
					## check strategic value
					if bUseStrategicValue == 1:
						fChance = fChance + pSetPlug.GetStrategicValue()
					## check economy value
					if bUseEconomyValue == 1:
						fChance = fChance + pSetPlug.GetEconomy()
					## check if ship is cloaked
					if bCloakCounts == 1 and pDestShip.IsCloaked() == 1:
						fAmount = 70.0
						if pSetPlug.GetStrategicValue() < fAmount:
							fChance = fChance - ( fAmount - pSetPlug.GetStrategicValue() )
					## check the set's default defence
					if bUseDefaultDefence == 1:
						fChance = fChance + pSetPlug.GetDefaultDefence()

				## check if player is being pursued
				if pConfig.AffectAI == 0 and pDestShip.GetObjID() == pPlayer.GetObjID():
					if IsShipFriendlyOfRace(pPlayer, sEmpire) == 1:
						bIsPlayerPursued = CheckIfShipIsBeingPursued(pPlayer)
						self.Logger.LogString("Player is friendly. Is he being pursued: "+str(bIsPlayerPursued))
					else:
						bIsPlayerPursued = 0
						self.Logger.LogString("Player is not friendly of the empire he entered.")
				else:
					bIsPlayerPursued = 0
				
				## then check if we can do the next check, the chance check
				bCanCheck = bIsPlayerPursued
				if bCanCheck == 0:
					bCanCheck = IsShipEnemyOfRace(pDestShip, sEmpire)

				# finally, check chance
				if fFactor <= fChance and bCanCheck == 1:
					self.Logger.LogString(sEmpire+" is sending defence forces to handle the situation...")
					# okay, ships WILL come after this ship
					iNumShips = iNumDefensiveShips + int(self.GetRandomNum(pConfig.MinNumShips, pConfig.MaxNumShips))
					iNumReinforcementShips = int(self.GetRandomNum(pConfig.MinReinShips, pConfig.MaxReinShips))
					iNumOfReinforcements = int(pConfig.NumOfReins)
					fTimeToEnter = self.GetRandomNum(pConfig.MinTimeToEnter, pConfig.MaxTimeToEnter)
					fTimeToReinforce = self.GetRandomNum(pConfig.MinTimeToRein, pConfig.MaxTimeToRein)
					bIncludeGodShips = pConfig.IncludeGodShips
					bIncludeEscorts = pConfig.IncludeEscorts
					if pDestShip.GetObjID() == pPlayer.GetObjID() and bIsPlayerPursued == 0:
						ShowTextBanner("You were detected, defence forces are coming...", 0.5, 0.5, 3, 14, 1, 1)
					elif pDestShip.GetObjID() == pPlayer.GetObjID() and bIsPlayerPursued == 1:
						ShowTextBanner("Friendly defence forces are coming to your aid...", 0.5, 0.5, 3, 14, 1, 1)
					RandomDefenceForce(sEmpire, iNumShips, iNumReinforcementShips, iNumOfReinforcements, pSet, fTimeToEnter, fTimeToReinforce, bIncludeGodShips, bIncludeEscorts)
					pRegion.DeductDefenseShipAmount(iNumDefensiveShips)
					self.Logger.LogString("RandomDefenceForce instance created for empire "+sEmpire)

oRandomDefenceForceTrigger = RandomDefenceForceTrigger('RandomDefenceForce Trigger', Custom.GalaxyCharts.Traveler.ET_RDF_TRIGGER, dict={'modes': [mode]})
# RDF Trigger was App.ET_EXITED_SET before...

#########################
### Object Exploding - To delete a dying ship's Travel instance.
class GalaxyDelTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip:
			# The ship is exploding, that means she's making the badabin-badabum, before actually being set as
			# destroyed. Anyways, we should stop/delete her Travel(or Chaser) instance if she has one.
			App.g_kTravelManager.DeleteTravel(pShip)

oGalaxyDelTrigger = GalaxyDelTrigger('GalaxyCharts Trigger', App.ET_OBJECT_EXPLODING, dict = { 'modes': [ mode ] } )

##########################################################################################################################
##### Trigger Classes/Fixes and Other     ################################################################################
##########################################################################################################################

### input console / options
## used to mark the real time the user spent with the game paused, either in the options menu or in the console
## that way when he returns to the game, the Traveler system will be correctly updated, to make this time spent paused 
## not be counted by the real time clock counting the time left to reach the destination
class PauseTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.Type = "unknown"
		if eventKey == App.ET_INPUT_TOGGLE_OPTIONS:
			self.Type = "OPTIONS"
		if eventKey == App.ET_INPUT_TOGGLE_CONSOLE:
			self.Type = "CONSOLE"
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		pTop = App.TopWindow_GetTopWindow()
		if pTop != None:
			pOptWin = pTop.FindMainWindow(App.MWT_OPTIONS)
			if self.Type == "OPTIONS":
				if pOptWin != None:
					if pOptWin.IsVisible() == 0:
						#not visible - unpausing
						App.g_kTravelManager.TravelerPauseCheck(0)
					else:
						# visible - pausing
						App.g_kTravelManager.TravelerPauseCheck(1)

			elif self.Type == "CONSOLE":
				pConWin = pTop.FindMainWindow(App.MWT_CONSOLE)
				if pConWin != None and pOptWin != None:
					if pOptWin.IsVisible() == 0:
						# if the options window is visible, we don't need to continue this part here, because
						# even if the console is opened while in the main menu - the opening of the main menu
						# itself will already have updated the Traveler system accordingly.
						if pConWin.IsVisible() == 0:
							#not visible - unpausing
							App.g_kTravelManager.TravelerPauseCheck(0)
						else:
							# visible - pausing
							App.g_kTravelManager.TravelerPauseCheck(1)

PauseTriggerOpt = PauseTrigger('PauseConsole Trigger', App.ET_INPUT_TOGGLE_CONSOLE, dict = { 'modes': [ mode ] } )
PauseTriggerCon = PauseTrigger('PauseOptions Trigger', App.ET_INPUT_TOGGLE_OPTIONS, dict = { 'modes': [ mode ] } )

### Tractor Beam Started Hitting
### this is used to fix a bug in CoreEject which makes ships unable to warp after dumping and reacquiring their warp cores
class CoreEjectFix(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		try:
			CoreActions = __import__('Custom.Sneaker.CoreEject.CoreActions')
			sCoreName = CoreActions.g_CoreName
			pPlayer = App.Game_GetCurrentPlayer()
			pTargShip = App.ShipClass_Cast(pEvent.GetDestination())
			if pTargShip != None and pPlayer != None and pTargShip.GetName() == sCoreName:
				pTractorProjector	= App.TractorBeamProjector_Cast(pEvent.GetSource())
				pTractorSystem = App.TractorBeamSystem_Cast(pTractorProjector.GetParentSubsystem())
				pShip = pTractorSystem.GetParentShip()
				if pShip != None and pShip.GetObjID() == pPlayer.GetObjID():
					pSeq = App.TGSequence_Create()
					pAction = App.TGScriptAction_Create(__name__, "FixWarpEngineCoreEject")
					pSeq.AddAction(pAction, None, 10.0)
					pSeq.Play()
		except:
			pass
		pObject.CallNextHandler(pEvent)

def FixWarpEngineCoreEject(pAction):
	debug(__name__ + ", FixWarpEngineCoreEject")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer != None:
		fPercentage = 0.5
		pWarpEngines = pPlayer.GetWarpEngineSubsystem()
		pWarpProp = pWarpEngines.GetProperty()
		pWarpProp.SetDisabledPercentage(fPercentage)
		for i in range(pWarpEngines.GetNumChildSubsystems()):
			pChild = pWarpEngines.GetChildSubsystem(i)
			if pChild != None:
				pChildProp = pChild.GetProperty()
				pChildProp.SetDisabledPercentage(fPercentage)
	return 0

oCoreEjectFix = CoreEjectFix('CoreEjectFix Trigger', App.ET_TRACTOR_BEAM_STARTED_HITTING, dict = { 'modes': [ mode ] } )

##########################################################################################################################
##### NICE INITIALIZING PRINT     ########################################################################################
##########################################################################################################################
# As this mod doesn't have a sole 'entry point' like GravityFX, we do this here then, in lack of a better place to do it
import Custom.FoundationConfig
if mode.name in Custom.FoundationConfig.lActiveMutators:
	print "Galaxy Charts v" + str(Custom.GalaxyCharts.Galaxy.MOD_VERSION) + " is online"
# =P
