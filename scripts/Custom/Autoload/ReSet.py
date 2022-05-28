from bcdebug import debug
import App
import Foundation
import MissionLib

TorpType = 0
PhaserState = 1
TractorState = 1

mode = Foundation.MutatorDef("MLeoDaalder\'s Detail/Nit Fix")
# Defiant deactivated for FBCMP
#mode3 = Foundation.MutatorDef("\\_Broad Picture TV View")
#Foundation.OverrideDef.NitFixingModEndCutscene = Foundation.OverrideDef("NitFixingModEndCutscene", "MissionLib.EndCutscene", __name__ + ".ReworkedEndCutscene", dict = { "modes": [ mode3 ] } )

ET_TRACTOR_TYPE_TOGGLE = App.UtopiaModule_GetNextEventType()
ET_SLIDER_POWER = App.UtopiaModule_GetNextEventType()
TURN_OFF_SYSTEM_FOR_TIME_UPDATE_TIMER = App.UtopiaModule_GetNextEventType()
TractorTypeToggle = None
pPhaserBar = None

NonSerializedObjects = (
"oPlayerChecking",
"TractorTypeToggle",
"pPhaserBar",
)

class PlayerCheckingTrigger(Foundation.TriggerDef):
	def __init__(self):
		debug(__name__ + ", __init__")
		global mode
		self.Inited = 0
		Foundation.TriggerDef.__init__(self, "MLeoDaalder Detail Fix", App.ET_OBJECT_CREATED, dict = {"modes": [mode]})
		self.Mission = None
		self.pTimer = None

	def __call__(self, pObject, pEvent, bForce=0):
		debug(__name__ + ", __call__")
		
		if bForce:
			pShip = App.Game_GetCurrentPlayer()
		else:
			pShip = App.ShipClass_Cast(pEvent.GetDestination()) # needed, because if there is a torpedo created this also get's triggerd
			if(pShip == None):
				return 0

		# Do not start in SP
		pGame = App.Game_GetCurrentGame()
		if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
			return

		pShip.SetDisabledEngineDeceleration(0.0)
		global ET_TRACTOR_TYPE_TOGGLE, ET_SLIDER_POWER
		if App.Game_GetCurrentPlayer() and pShip.GetObjID() == App.Game_GetCurrentPlayer().GetObjID():
			global TorpType, PhaserState, TractorState
			TorpType = 0
			PhaserState = 1
			TractorState = 1
			pTacWindow = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
                        # Defiant deactivated for FBCMP
                        """
			global mode3
			if(mode3.IsEnabled()):
				pTopWindow = App.TopWindow_GetTopWindow()
				pTopWindow.StartCutscene(1.0, 0.19, 0)
				pTopWindow.AllowKeyboardInput(1)
				pTopWindow.AllowMouseInput(1)
				App.g_kRootWindow.SetCursorVisible(1)
"""
			if(pTacWindow):
				pTractorToggle = pTacWindow.GetBeamToggle()
				if(pTractorToggle):
					TractorStates = GetTractorPlug()
					if(TractorStates):
						global TractorState
						if(TractorStates.has_key("Prefix")):
							pTractorToggle.SetPrimaryCaption(TractorStates["Prefix"])
						if(TractorStates.has_key("OtherStates")):
							if(TractorStates["OtherStates"] == 1):
								pTopWindow = App.TopWindow_GetTopWindow()
								pEvent = App.TGIntEvent_Create()
								pEvent.SetEventType(ET_TRACTOR_TYPE_TOGGLE)
								pEvent.SetInt(0)
								
								pPlayer = App.Game_GetCurrentPlayer()
								pTractor = pPlayer.GetTractorBeamSystem()
								TractorState = pTractor.GetMode()
								global TractorTypeToggle
								ButtonName = "Tractor Types"
								if(TractorStates.has_key("GetNameByMode")):
									ButtonName = TractorStates["GetNameByMode"](TractorState)
								TractorTypeToggle = App.STButton_Create(ButtonName, pEvent)
								pEvent.SetDestination(TractorTypeToggle)
								TractorTypeToggle.SetVisible(1)

								pBottom = App.TGPane_Cast(pTacWindow.GetLastChild()).GetBottom() + App.globals.DEFAULT_ST_INDENT_VERT
								pLeft = pTractorToggle.GetLeft()

								pTacWindow.AddChild(TractorTypeToggle)
								TractorTypeToggle.Resize(pTractorToggle.GetWidth(), pTractorToggle.GetHeight())
								TractorTypeToggle.SetPosition(pLeft, pBottom)
								TractorTypeToggle.Layout()
					else:
						pTractorToggle.SetPrimaryCaption("Tractor:")
					pTacWindow.RefreshTractorToggle()

				pCloakToggle = pTacWindow.GetCloakToggle()
				if(pCloakToggle):
					pCloakToggle.SetPrimaryCaption("Cloak:")
					pTacWindow.RefreshCloakToggle()

				pPhaserToggle = pTacWindow.GetPhaserIntensityToggle()
				if(pPhaserToggle):
					states = GetPhaserStates()
					if(states):
						prefix = ""
						if(states.has_key("Prefix")):
							prefix = states["Prefix"]
						suffix = ""
						if(states.has_key("SuffixSelection")):
							suffix = states["SuffixSelection"](1)
						pPhaserToggle.SetName(App.TGString(prefix + suffix))
					else:
						pPhaserToggle.SetName(App.TGString("Intensity: Med"))
					global pPhaserBar
					pPhaserBar = App.STNumericBar_Create()
					pPhaserBar.SetRange(0.0, 2.0)
					pPhaserBar.SetKeyInterval(0.05)
					pPhaserBar.SetMarkerValue(1)
					pPhaserBar.SetValue(PhaserState)
					pPhaserBar.SetUseMarker(0)
					pPhaserBar.SetUseAlternateColor(0)
					pPhaserBar.SetUseButtons(1)

					pTacWindow.SetUseScrolling(1)
					kNormalColor = App.g_kSTMenu3NormalBase
					kEmptyColor = App.g_kSTMenu3Disabled

					pPhaserBar.SetNormalColor(kNormalColor)
					pPhaserBar.SetEmptyColor(kEmptyColor)
					pText = pPhaserBar.GetText()
					pText.SetStringW(App.TGString(""))

					pPhaserBar.Resize (pPhaserToggle.GetWidth(), pPhaserToggle.GetHeight(), 0)

					pEvent = App.TGFloatEvent_Create ()
					pTopWindow = App.TopWindow_GetTopWindow()
					pOptionsWindow = pTopWindow.FindMainWindow(App.MWT_OPTIONS)

					pEvent.SetDestination(pOptionsWindow)
					pEvent.SetSource(pPhaserBar)
					pEvent.SetFloat(PhaserState)
					pEvent.SetEventType(ET_SLIDER_POWER)

					pPhaserBar.SetUpdateEvent(pEvent)
					pPhaserBar.SetVisible()
 					pPhaserToggle.GetParent().AddChild(pPhaserBar, pPhaserToggle.GetLeft(), pPhaserToggle.GetTop(), 0)
					pPhaserToggle.SetNotVisible()
					pPhaserToggle.SetDisabled()
					# Let's hope this works...
					#pPhaserToggle.this = pPhaserBar.this
					pPhaserToggle.GetParent().Layout()


				global type
				type = None
				global TorpType
				pTorpTypeToggle = pTacWindow.GetTorpTypeToggle()
				pOldType = TorpType
				pPlayer = App.Game_GetCurrentPlayer()
				pTorp = pPlayer.GetTorpedoSystem()
				if pTorp != None:
					types = GetTorpTypes()
					if types == None:
						pCurType = 0
						pName = pTorp.GetAmmoType(pCurType).GetAmmoName()
						pTorpTypeToggle.SetName(App.TGString("Type: " + pName))
						TorpType = pCurType
					else: #Tricky...
						pCurType = 0
						pName = GetTorpName(types["AmmoTypes"][1][pCurType])
						pTorpTypeToggle.SetName(App.TGString("Type: " + pName))

						for iType in range(pTorp.GetProperty().GetNumAmmoTypes()):
							pTorp.RemoveAmmoType(iType)
						pTorp.GetProperty().SetNumAmmoTypes(1)

						pTorpProp = pTorp.GetProperty()
						pTorpProp.SetMaxTorpedoes(0, types["AmmoTypes"][0][pCurType])
						pTorpProp.SetTorpedoScript(0, types["AmmoTypes"][1][pCurType])
						NumToLoad = types["AmmoStat"][pCurType]
						pTorp.LoadAmmoType(0, types["AmmoStat"][pCurType])
						pTorp.LoadAmmoType(0, NumToLoad)
						pPlayer.UpdateNodeOnly()
						TorpType = pCurType
			if self.Inited:
				App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_INTENSITY_TOGGLE_CLICKED,	self.Mission,	__name__ + ".PhaserIntensityToggle")
				App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORP_TYPE_TOGGLE_CLICKED,		self.Mission,	__name__ + ".TorpTypeToggle")
				App.g_kEventManager.RemoveBroadcastHandler(App.ET_SB12_RELOAD,				self.Mission,	__name__ + ".ReloadTorps")
				#App.g_kEventManager.RemoveBroadcastHandler(App.ET_KEYBOARD,				self.Mission,	__name__ + ".BPTV")
				App.g_kEventManager.RemoveBroadcastHandler(ET_TRACTOR_TYPE_TOGGLE,			self.Mission,	__name__ + ".TractorTypeToggleDef")
				#App.g_kEventManager.RemoveBroadcastHandler(App.ET_POWER_CONTROL_REFRESH_TIMER,		self.Mission,	__name__ + ".GravUpdate")
				App.g_kEventManager.RemoveBroadcastHandler(ET_SLIDER_POWER,				self.Mission,	__name__ + ".SliderPowerUpdate")
				#App.g_kEventManager.RemoveBroadcastHandler(App.ET_SUBSYSTEM_POWER_CHANGED,		self.Mission,	__name__ + ".TurnOffSystemForTimeUpdate")
				App.g_kEventManager.RemoveBroadcastHandler(App.ET_LOAD_MISSION,				self.Mission,	__name__ + ".Reset")
				#App.g_kEventManager.RemoveBroadcastHandler(App.ET_POWER_CONTROL_REFRESH_TIMER,		self.Mission,	__name__ + ".TurnOffSystemForTimeUpdate")
				App.g_kEventManager.RemoveBroadcastHandler(App.ET_QUIT,					self.Mission,	__name__ + ".Reset")
				#App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_NEBULA,			self.Mission,	__name__ + ".EnteredNebula")
				#App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXITED_NEBULA,			self.Mission,	__name__ + ".ExitedNebula")
				App.g_kTimerManager.DeleteTimer(self.pTimer.GetObjID())

			self.Mission = App.Game_GetCurrentGame().GetCurrentEpisode().GetCurrentMission()
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_PHASER_INTENSITY_TOGGLE_CLICKED,	self.Mission,	__name__ + ".PhaserIntensityToggle")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TORP_TYPE_TOGGLE_CLICKED,		self.Mission,	__name__ + ".TorpTypeToggle")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SB12_RELOAD,				self.Mission,	__name__ + ".ReloadTorps")
			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_KEYBOARD,				self.Mission,	__name__ + ".BPTV")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_TRACTOR_TYPE_TOGGLE,			self.Mission,	__name__ + ".TractorTypeToggleDef")
			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_POWER_CONTROL_REFRESH_TIMER,		self.Mission,	__name__ + ".GravUpdate")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(ET_SLIDER_POWER,				self.Mission,	__name__ + ".SliderPowerUpdate")
			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SUBSYSTEM_POWER_CHANGED,		self.Mission,	__name__ + ".TurnOffSystemForTimeUpdate")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_LOAD_MISSION,				self.Mission,	__name__ + ".Reset")
			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_POWER_CONTROL_REFRESH_TIMER,		self.Mission,	__name__ + ".TurnOffSystemForTimeUpdate")
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_QUIT,					self.Mission,	__name__ + ".Reset")
			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_ENTERED_NEBULA,			self.Mission,	__name__ + ".EnteredNebula")
			#App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_NEBULA,			self.Mission,	__name__ + ".ExitedNebula")
			if not self.pTimer:
				self.pTimer = MissionLib.CreateTimer(TURN_OFF_SYSTEM_FOR_TIME_UPDATE_TIMER, __name__ + ".TurnOffSystemForTimeUpdate", App.g_kUtopiaModule.GetGameTime() + 1, 0, 0)
			self.Inited = 1

			#App.PhaserBank_SetMaxPhaserRange(App.PhaserBank_GetMaxPhaserRange() * 3)

		else:
			return 0

	def __del__(self):
		debug(__name__ + ", __del__")
		global ET_TRACTOR_TYPE_TOGGLE, ET_SLIDER_POWER, TractorTypeToggle, pPhaserBar
		if self.Inited:
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_INTENSITY_TOGGLE_CLICKED,	self.Mission,	__name__ + ".PhaserIntensityToggle")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORP_TYPE_TOGGLE_CLICKED,		self.Mission,	__name__ + ".TorpTypeToggle")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_SB12_RELOAD,				self.Mission,	__name__ + ".ReloadTorps")
			#App.g_kEventManager.RemoveBroadcastHandler(App.ET_KEYBOARD,				self.Mission,	__name__ + ".BPTV")
			App.g_kEventManager.RemoveBroadcastHandler(ET_TRACTOR_TYPE_TOGGLE,			self.Mission,	__name__ + ".TractorTypeToggleDef")
			#App.g_kEventManager.RemoveBroadcastHandler(App.ET_POWER_CONTROL_REFRESH_TIMER,		self.Mission,	__name__ + ".GravUpdate")
			App.g_kEventManager.RemoveBroadcastHandler(ET_SLIDER_POWER,				self.Mission,	__name__ + ".SliderPowerUpdate")
			#App.g_kEventManager.RemoveBroadcastHandler(App.ET_SUBSYSTEM_POWER_CHANGED,		self.Mission,	__name__ + ".TurnOffSystemForTimeUpdate")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_LOAD_MISSION,				self.Mission,	__name__ + ".Reset")
			#App.g_kEventManager.RemoveBroadcastHandler(App.ET_POWER_CONTROL_REFRESH_TIMER,		self.Mission,	__name__ + ".TurnOffSystemForTimeUpdate")
			App.g_kEventManager.RemoveBroadcastHandler(App.ET_QUIT,					self.Mission,	__name__ + ".Reset")
			MissionLib.g_lMissionTimers.remove(self.pTimer)
			App.g_kTimerManager.DeleteTimer(self.pTimer.GetObjID())
		self.Inited = 0
		del self.Mission
		del self.pTimer
		TractorTypeToggle.GetParent().DeleteChild(TractorTypeToggle)
		#del TractorTypeToggle
		pPhaserBar.GetParent().DeleteChild(pPhaserBar)
		#del pPhaserBar
		if Foundation.TriggerDef.__dict__.has_key("__del__"):
			Foundation.TriggerDef.__del__(self)

oPlayerChecking = PlayerCheckingTrigger()

def Reset(pObject, pEvent):
	debug(__name__ + ", Reset")
	global oPlayerChecking
	del oPlayerChecking
	oPlayerChecking = PlayerCheckingTrigger()

class WarpSetFixer(Foundation.TriggerDef):
	def __init__(self):
		debug(__name__ + ", __init__")
		global mode
		Foundation.TriggerDef.__init__(self, "MLeoDaalder\'s Nit Fix Warp Set", App.ET_WARP_BUTTON_PRESSED, dict = {"modes": [mode]})
	def __call__(self, pObject, pEvent):
		debug(__name__ + ", __call__")
		try:
			s = __import__("Custom.QuickBattleGame.QuickBattle")
			if(s):
				if(s.ET_PRELOAD_DONE == None):
					App.SetClass_Cast(App.WarpSequence_GetWarpSet()).SetProximityManagerActive(1)
					App.WarpSequence_GetWarpSet().SetProximityManagerActive(1)
			else:
				App.SetClass_Cast(App.WarpSequence_GetWarpSet()).SetProximityManagerActive(1)
				App.WarpSequence_GetWarpSet().SetProximityManagerActive(1)
		except:
			App.SetClass_Cast(App.WarpSequence_GetWarpSet()).SetProximityManagerActive(1)
			App.WarpSequence_GetWarpSet().SetProximityManagerActive(1)

# deactivated by Defiant: seems to crash the game randomly, even if the Trigger is not called?!?
#oWarpSetFixer = WarpSetFixer()

def EnteredNebula(pObject, pEvent):
	debug(__name__ + ", EnteredNebula")
	pSet = App.g_kSetManager.GetSet("bridge")
	pCamera = App.ZoomCameraObjectClass_GetObject(pSet, "maincamera")
	if pCamera:
		pCamera.SetShake(3, -1)

def ExitedNebula(pObject, pEvent):
	debug(__name__ + ", EnteredNebula")
	pSet = App.g_kSetManager.GetSet("bridge")
	pCamera = App.ZoomCameraObjectClass_GetObject(pSet, "maincamera")
	if pCamera:
		pCamera.SetShake(0, -1)

def PhaserIntensityToggle(pObject, pEvent):
	debug(__name__ + ", PhaserIntensityToggle")
	pTacWindow = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
	if(pTacWindow):
		global PhaserState
		pPhaserToggle = pTacWindow.GetPhaserIntensityToggle()
		pPlayer = App.Game_GetCurrentPlayer()
		pPhaser = pPlayer.GetPhaserSystem()
		pOldMode = PhaserState
		pCurMode = pOldMode + 1
		states = None
		states = GetPhaserStates()
		if(states == None):	
			if(pCurMode == 3):
				pCurMode = 0
			pPhaser.SetPowerLevel(pCurMode)
			pStates = ["Low", "Med", "High"]
			pPhaserToggle.SetName(App.TGString("Intensity: " + pStates[pCurMode]))
			pPhaser.SetPowerLevel(pCurMode)
			if pPlayer.GetPulseWeaponSystem():
				pPulseWeapon = pPlayer.GetPulseWeaponSystem()
				for i in range(pPulseWeapon.GetNumChildSubsystems()):
					pPulse = App.PulseWeapon_Cast(pPulseWeapon.GetChildSubsystem(i))
					pPulse.SetPowerSetting(pCurMode)

			PhaserState = pCurMode
		else: #Tricky...
			if(pCurMode > 2):
				if(states.has_key("max")):
					if(pCurMode == states["max"]):
						if(states.has_key("min")):
							pCurMode = states["min"] + 1
						else:
							pCurMode = 0
				else:
					pCurMode = 0
			else:
				if(states.has_key("ChangePhaserStats")):
					states.ChangePhaserStats(pCurMode)

			prefix = ""
			if(states.has_key("Prefix")):
				prefix = states["Prefix"]
			suffix = ""
			if(states.has_key("SuffixSelection")):
				suffix = states["SuffixSelection"](pCurMode)
			pPhaserToggle.SetName(App.TGString(prefix + suffix))
			NewMode = pCurMode
			if(states.has_key("LevelSelection")):
				NewMode = states["LevelSelection"](pCurMode)
			else:
				NewMode = pCurMode
			pPhaser.SetPowerLevel(NewMode)
			PhaserState = pCurMode
	else:
		return 0

def SliderPowerUpdate(pObject, pEvent):
	debug(__name__ + ", SliderPowerUpdate")
	pFloatEvent = App.TGFloatEvent_Cast(pEvent)
        if not pFloatEvent:
                return
	pSetting = pFloatEvent.GetFloat()
	if pSetting:
		pPlayer = App.Game_GetCurrentPlayer()
		pPhaser = pPlayer.GetPhaserSystem()
		pPulseWeaponSystem = pPlayer.GetPulseWeaponSystem()
		if pPhaser:
			pPhaser.SetPowerLevel(pSetting)
		if pPulseWeaponSystem:
			for i in range(pPulseWeaponSystem.GetNumChildSubsystems()):
				pPulse = App.PulseWeapon_Cast(pPulseWeaponSystem.GetChildSubsystem(i))
				if pPulse:
					pPulse.SetPowerSetting(pSetting)

def TorpTypeToggle(pObject, pEvent):
	debug(__name__ + ", TorpTypeToggle")
	pTacWindow = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
	if(pTacWindow):
		global TorpType
		pTorpTypeToggle = pTacWindow.GetTorpTypeToggle()
		pOldType = TorpType
		pPlayer = App.Game_GetCurrentPlayer()
		pTorp = pPlayer.GetTorpedoSystem()
		types = GetTorpTypes()
		if(types == None):
			if pTorp.GetProperty().GetNumAmmoTypes() == 1:
				return 0
                        
                        # this whole thing should fix the reload bug when num available = 0
			pCurType = pOldType + 1
                        if pCurType > pTorp.GetProperty().GetNumAmmoTypes() - 1:
                                pCurType = 0
                        iNumCur = pTorp.GetNumAvailableTorpsToType(pCurType)
                        while(iNumCur == 0 and pCurType != pOldType):
                                iNumCur = pTorp.GetNumAvailableTorpsToType(pCurType)
                                pCurType = pCurType + 1
                                if pCurType > pTorp.GetProperty().GetNumAmmoTypes() - 1:
                                        pCurType = 0
                        # no change?
                        if pCurType == pOldType:
                                return
                        
			if(pCurType == pTorp.GetProperty().GetNumAmmoTypes()):
				pCurType = 0

			pName = GetTorpName(pTorp.GetAmmoType(pCurType).GetTorpedoScript())
			pTorpTypeToggle.SetName(App.TGString("Type: " + pName))
			pTorp.SetAmmoType(pCurType, pTorp.GetNumAvailableTorpsToType(pCurType))
			TorpType = pCurType
		else: #Tricky... Or not... lol
			if types["NumAmmoTypes"] == 1:
				return 0
			types["AmmoStat"][pOldType] = pTorp.GetNumAvailableTorpsToType(0)
                        iNumLeft = 0
                        pCurType = pOldType + 1
			if(pCurType == types["NumAmmoTypes"]):
				pCurType = 0
			pName = GetTorpName(types["AmmoTypes"][1][pCurType])
			pTorpTypeToggle.SetName(App.TGString("Type: " + pName))
			pTorpProp = pTorp.GetProperty()
			pTorpProp.SetMaxTorpedoes(0, types["AmmoTypes"][0][pCurType])
			pTorpProp.SetTorpedoScript(0, types["AmmoTypes"][1][pCurType])
			NumToLoad = types["AmmoStat"][pCurType]
			if(types["AmmoStat"][pCurType] < types["AmmoTypes"][0][pCurType]):
				NumToLoad = (types["AmmoStat"][pCurType] - types["AmmoTypes"][0][pCurType])
			pTorp.LoadAmmoType(0, types["AmmoStat"][pCurType])
			pTorp.LoadAmmoType(0, NumToLoad)
			pPlayer.UpdateNodeOnly()
			TorpType = pCurType
			if types.has_key("AmmoLoadTime"):
				if str(types["AmmoLoadTime"])[0] == "[":
					iTime = types["AmmoLoadTime"][pCurType]
				else:
					iTime = types["AmmoLoadTime"]
				TurnOffSystemForTime(pPlayer, pTorp, iTime)
			else:
				pTorp.SetAmmoType(0)
	return 0

dSystems = {}
def TurnOffSystemForTime(pShip, pSystem, iTime):
	debug(__name__ + ", TurnOffSystemForTime")
	if iTime == 0:
		return 0
	# check if ship still exists before we modify it
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return 0
	pSystem.TurnOff()
	global dSystems
	if not dSystems.has_key(pShip.GetObjID()):
		dSystems[pShip.GetObjID()] = []
	dSystems[pShip.GetObjID()].append([pSystem, App.g_kUtopiaModule.GetGameTime() + iTime])
	return 0

def TurnOffSystemForTimeUpdate(pObject, pEvent):
	debug(__name__ + ", TurnOffSystemForTimeUpdate")
	global dSystems
	for key in dSystems.keys():
		system = dSystems[key]
		if system:
			for subsystem in system:
				# check if ship still exists before we modify it
				pParentShip = subsystem[0].GetParentShip()
				pShip = App.ShipClass_GetObjectByID(None, pParentShip.GetObjID())
				if not pShip:
					system.remove(subsystem)
					continue
				if App.g_kUtopiaModule.GetGameTime() >= subsystem[1]:
					subsystem[0].TurnOn()
					system.remove(subsystem)
				else:
					subsystem[0].TurnOff()
			if system == []:
				del dSystems[key]
	
	MissionLib.CreateTimer(TURN_OFF_SYSTEM_FOR_TIME_UPDATE_TIMER, __name__ + ".TurnOffSystemForTimeUpdate", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
	return 0

def TractorTypeToggleDef(pObject, pEvent):
	debug(__name__ + ", TractorTypeToggleDef")
	global TractorState
	pTacWindow = App.TacWeaponsCtrl_GetTacWeaponsCtrl()
	if(pTacWindow):
		pTractorToggle = pTacWindow.GetBeamToggle()
		pPlayer = App.Game_GetCurrentPlayer()
		pTractor = pPlayer.GetTractorBeamSystem()
		pOldMode = TractorState
		pCurMode = pOldMode + 1
		TractorPlug = GetTractorPlug()
		if(TractorPlug):
			if(TractorPlug.has_key("OtherStates")):
				if(TractorPlug["OtherStates"] != 1):
					return
			if(TractorPlug.has_key("NumStates")):
				if(pCurMode == TractorPlug["NumStates"]):
					pCurMode = 0
			if(TractorPlug.has_key("GetNameByMode")):
				ButtonName = TractorPlug["GetNameByMode"](pCurMode)
				global TractorTypeToggle
				TractorTypeToggle.SetName(App.TGString(ButtonName))

			if(TractorPlug.has_key("SetTractorByMode")):
				TractorPlug["SetTractorByMode"](pCurMode)
		pTacWindow.RefreshTractorToggle()
		TractorState = pCurMode
	else:
		return 0

def GravUpdate(pObject, pEvent):
#	global mode5
#	return
#	if(not mode5.IsEnabled()):
#		return
	debug(__name__ + ", GravUpdate")
	return
	pPlayer = App.Game_GetCurrentPlayer()
	pSet = pPlayer.GetContainingSet()
	if(pSet):
		# Get the list of planets.
		lGravs = list(pSet.GetClassObjectList(App.CT_PLANET))

		pShips = list(pSet.GetClassObjectList(App.CT_SHIP))
		pDebris = list(pSet.GetClassObjectList(App.CT_DEBRIS))
		for item in pDebris:
			pShips.append(item)
		lObjects = []
		for ship in pShips:
			lObjects.append([ship, ship.GetWorldLocation()])
		if(lGravs and lObjects):
			for pObject in lObjects:
				Vector = []
				for pGrav in lGravs:
					Vector.append(CalcSpeedVec(pGrav, pObject))
	return 0

def CalcSpeedVec(pGrav, pObject):
	debug(__name__ + ", CalcSpeedVec")
	dis = Distance(pGrav.GetWorldLocation(), pObject.GetWorldLocation())
	retval = App.TGPoint3()

	kGravLocation = pGrav.GetWorldLocation()
	kObjectLocation = pObject.GetWorldLocation()

	kObjectLocation.Subtract(kGravLocation)
	kFwd = kObjectLocation
	kFwd.Unitize()
	kPerp = kFwd.Perpendicular()
	kPerp2 = App.TGPoint3()
	kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

	return retval

def GetPhaserStates():
	debug(__name__ + ", GetPhaserStates")
	Plug = GetPlug()
	if(Plug == 0):
		return None
	if(Plug.__dict__.has_key("GetPhaserStates")):
		return Plug.GetPhaserStates(Plug)
	return None

type = None
def GetTorpTypes():
	debug(__name__ + ", GetTorpTypes")
	global type
	Plug = GetPlug()
	if(Plug == 0):
		return None
	if(Plug.__dict__.has_key("GetTorpTypes")):
		if(type == None):
			if str(Plug.GetTorpTypes)[0] == "<":
				type = Plug.GetTorpTypes(Plug)
			else:
				type = Plug.GetTractorTypes

			if(not type.has_key("AmmoStat")):
				type["AmmoStat"] = []
				for i in range(len(type["AmmoTypes"][0])):
					type["AmmoStat"].append(type["AmmoTypes"][0][i])
				
		return type
	return None

def GetTractorPlug():
	debug(__name__ + ", GetTractorPlug")
	Plug = GetPlug()
	if(Plug == 0):
		return 0
	if(Plug.__dict__.has_key("GetTractorPlug")):
		return Plug.GetTractorPlug(Plug)
	return None

def BPTV(pObject, pEvent):
        # Defiant deactivated for FBCMP
        debug(__name__ + ", BPTV")
	#global mode3
	#if(not mode3.IsEnabled()):
	#	return
	#wChar = pEvent.GetUnicode()
	#if(wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_OPTIONS, App.KeyboardBinding.GET_EVENT, 0.0)):
	#	return

	#if wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_MAP_MODE, App.KeyboardBinding.GET_EVENT, 0.0):
	#	DoBPTV()
	#elif wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_CINEMATIC_MODE, App.KeyboardBinding.GET_EVENT, 0.0):
	#	DoBPTV()
	#elif wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_BRIDGE_AND_TACTICAL, App.KeyboardBinding.GET_EVENT, 0.0):
	#	DoBPTV()

def DoBPTV():
	debug(__name__ + ", DoBPTV")
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.EndCutscene(0.0)
	pTopWindow.StartCutscene(0.0, 0.19, 0)
	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)
	if(pTopWindow.IsBridgeVisible()):
		App.g_kRootWindow.SetCursorVisible(0)
	else:
		App.g_kRootWindow.SetCursorVisible(1)

def ReworkedEndCutscene(pAction, fTimeToLeave = 1.0):
	debug(__name__ + ", ReworkedEndCutscene")
	global mode3
        # Defiant deactivated for FBCMP
	"""if(mode3.IsEnabled()):
		pTopWindow = App.TopWindow_GetTopWindow()
		pTopWindow.EndCutscene(0.0)
		pTopWindow.StartCutscene(0.01, 0.19, 1)
		pTopWindow.AllowKeyboardInput(1)
		pTopWindow.AllowMouseInput(1)
		App.g_kRootWindow.SetCursorVisible(1)
		return 0"""

	App.TopWindow_GetTopWindow().EndCutscene(fTimeToLeave)

	pTop = App.TopWindow_GetTopWindow()
	pTCW = App.TacticalControlWindow_GetTacticalControlWindow()

	# Ensure that the cinematic window is set interactive. If we were in warp
	# during a cutscene, then the normal mechanism will not be triggered.
	pCinematic = App.CinematicWindow_Cast(pTop.FindMainWindow(App.MWT_CINEMATIC))
	if pCinematic:
		pCinematic.SetInteractive(1)

	pBridgeSet = App.g_kSetManager.GetSet("bridge")
	pRenderedSet = App.g_kSetManager.GetRenderedSet()

	# If the bridge is not the rendered set, then force tactical to be visible.
	# Otherwise, make sure that the bridge is visible.
	if (str(pBridgeSet) != str(pRenderedSet)):
		pTop.ForceTacticalVisible()
		pTCW.SetVisible()

		pSubtitle = App.SubtitleWindow_Cast(pTop.FindMainWindow(App.MWT_SUBTITLE))
		pSubtitle.SetPositionForMode(App.SubtitleWindow.SM_END_CINEMATIC)	# first cancel cinematic mode.
		pSubtitle.SetPositionForMode(App.SubtitleWindow.SM_TACTICAL)
	else:
		pTop.ForceBridgeVisible()

		pSubtitle = App.SubtitleWindow_Cast(pTop.FindMainWindow(App.MWT_SUBTITLE))
		pSubtitle.SetPositionForMode(App.SubtitleWindow.SM_END_CINEMATIC)	# first cancel cinematic mode.
		pSubtitle.SetPositionForMode(App.SubtitleWindow.SM_BRIDGE)
		
	# Make sure the call-outs are back at their previous levels
	MissionLib.SetSpeakingVolume(None, App.CSP_SPONTANEOUS, 1.0)

	return 0

# Next 4 copied from my WIP tools script and alterd when needed... It seems to do the trick...
def GetPlug(pShip = None):
	debug(__name__ + ", GetPlug")
	import string
	if(pShip == None):
		pShip = App.Game_GetCurrentPlayer()
	pScript = string.split(pShip.GetScript(), ".")[-1]
	if Foundation.shipList._keyList.has_key(pShip.GetShipProperty().GetShipName()):
		if Foundation.shipList._keyList[pShip.GetShipProperty().GetShipName()].shipFile == pScript:
			return Foundation.shipList._keyList[pShip.GetShipProperty().GetShipName()]
		else:
			if Foundation.shipList._keyList.has_key(pScript):
				return Foundation.shipList._keyList[pScript]
			else:
				return 0
	elif Foundation.shipList._keyList.has_key(pScript):
		return Foundation.shipList._keyList[pScript]
	else:
		return 0

def GetStringFromNumOn(string, i):
	debug(__name__ + ", GetStringFromNumOn")
	retval = ""
	for j in range(len(string) - i):
		retval = retval + string[j + i]
	return retval

def Distance(pObject1, pObject2):
	debug(__name__ + ", Distance")
	pLoc1 = pObject1.GetWorldLocation()
	pLoc2 = pObject2.GetWorldLocation()
	dX = pLoc1.GetX() - pLoc2.GetX()
	if(dX < 0):
		dX = pLoc2.GetX() - pLoc1.GetX()
	dY = pLoc1.GetY() - pLoc2.GetY()
	if(dY < 0):
		dY = pLoc2.GetY() - pLoc1.GetY()
	dZ = pLoc1.GetZ() - pLoc2.GetZ()
	if(dZ < 0):
		dZ = pLoc2.GetZ() - pLoc1.GetZ()
	return ((dX * dX) + (dY * dY) + (dZ * dZ)) ** 0.5

def GetTorpName(pScript):
	debug(__name__ + ", GetTorpName")
	s = __import__(pScript)
	if(s):
		if(hasattr(s, "GetName")):
			return str(s.GetName())
	return str("Do not fire!")

def ReloadTorps(pObject, pEvent):
	debug(__name__ + ", ReloadTorps")
	pPlayer = App.Game_GetCurrentPlayer()
	global type
	if(type):
		for i in range(len(type["AmmoTypes"][0])):
			type["AmmoStat"][i]= type["AmmoTypes"][0][i]
	return

def CalcGravForPlanet(pPlanet):
	debug(__name__ + ", CalcGravForPlanet")
	return

def CalcGravForSun(pSun):
	debug(__name__ + ", CalcGravForSun")
	return

