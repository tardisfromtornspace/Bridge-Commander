from bcdebug import debug
import App
import Foundation
import MissionLib
import LoadBridge
import LibConfig

oBridgePlugin = __import__("Custom.Autoload.000-Fixes20040612-LCBridgeAddon")

class BPSounds(Foundation.BridgePluginDef):
	def __call__(self, Plug, pBridgeSet, oBridgeInfo):

		# Hull impact part...
		debug(__name__ + ", __call__")
		lList =["sfx/Bridge/Impacts/impact1.wav", "sfx/Bridge/Impacts/impact2.wav", 
			"sfx/Bridge/Impacts/impact3.wav", "sfx/Bridge/Impacts/impact4.wav", 
			"sfx/Bridge/Impacts/impact5.wav"]

		if Plug.__dict__.has_key("HullHitSounds"):
			lList = Plug.HullHitSounds[:]
		pGame = App.Game_GetCurrentGame()
		pRegion = App.TGSoundRegion_GetRegion("bridge")
		for sSound in lList:
			if not App.g_kSoundManager.GetSound(sSound):
				pSound = pGame.LoadSoundInGroup(sSound, sSound, "BridgeGeneric")
				pSound.SetVolume(1.0)
				pRegion.AddSound(pSound)

		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_KEYBOARD, MissionLib.GetMission(), __name__ + ".BridgeToggle")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_MISSION_START, MissionLib.GetMission(), __name__ + ".MissionStart")

		# Bridge Sounds part
		pSound = App.g_kSoundManager.GetSound("AmbBridge")
		if pSound:
			pSound.SetLooping(0)
			pSound.SetVolume(0.0)
			pSound.Stop()
			App.g_kSoundManager.DeleteSound("AmbBridge")

		LoadBridge.LoadSounds() # Reset first, we don't want to load a TOS bridge first with TOS ambient sound and then a post nemesis one without an ambient sound.:P

		pGame = App.Game_GetCurrentGame()
		pBridgeRegion = App.TGSoundRegion_GetRegion("bridge")
		# Make sure the region has no filters muting it..
		pBridgeRegion.SetFilter(App.TGSoundRegion.FT_NONE)

		if Plug.__dict__.has_key("bridgeSound"):
			for key, value in Plug.bridgeSound.items():
				sGroup = "BridgeGeneric"
				if value.has_key("group"):
					sGroup = value["group"]

				pSound = pGame.LoadSoundInGroup(value["file"], key, sGroup)

				pBridgeRegion.AddSound(pSound)
				if value.has_key("volume"):
					pSound.SetVolume(value["volume"])
				else:
					pSound.SetVolume(1.0)

		# Ambient looping bridge SFX
		pSound = App.g_kSoundManager.GetSound("AmbBridge")
		if (pSound != None):
			pSound.SetLooping(1)
			pSound.SetPriority(1.0)
			pSound.Play()

	def PlayerCreated(self, Plug, pBridgeSet, oBridgeInfo, pShip):
		debug(__name__ + ", PlayerCreated")
		pShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_HIT, __name__ + ".HullHit")

	def CreateMenu(self, pOptionsPane, pContentPanel, bGameEnded = 0):

		debug(__name__ + ", CreateMenu")
		oConfig = LibConfig.Config("BridgePluginConfig")

		ET = App.UtopiaModule_GetNextEventType()
		pOptionsPane.AddPythonFuncHandlerForInstance(ET, __name__ + ".HandleFeature")

		#pButton = CreateStateButton("Bridge Sounds in Space: ", "Bridge Muffled", ["Muffled", "Clear"], oConfig.get("Bridge Muffled", 0), pOptionsPane, ET)

		#pContentPanel.AddChild(pButton)


		pButton = CreateStateButton("Outside noise:", "Space Muted2", ["On", "Off"], oConfig.get("Space Muted2", 0), pOptionsPane, ET)
		pContentPanel.AddChild(pButton)

		pButton = CreateStateButton("Hull impacts:", "Hull Impact", ["On", "Off"], oConfig.get("Hull Impact", 0), pOptionsPane, ET)
		pContentPanel.AddChild(pButton)

		return App.TGPane_Create()

oBPSounds = BPSounds("Bridge Sounds")

def CreateStateButton(pName, sVar, lStates, iState, pOptionsWindow, ET):
	debug(__name__ + ", CreateStateButton")
	kArgs = [pName, iState]
	kEvents=[]
	for kStateName in lStates:
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET)
		pEvent.SetDestination(pOptionsWindow)
		pEvent.SetString(sVar)

		kArgs.append(kStateName)
		kArgs.append(pEvent)
		kEvents.append(pEvent)
	kMenuButton = apply(App.STToggle_Create, kArgs)
	for pEvent in kEvents:
		pEvent.SetSource(kMenuButton)

	return kMenuButton

def HandleFeature(pObject, pEvent):
	debug(__name__ + ", HandleFeature")
	oConfig = LibConfig.Config("BridgePluginConfig")

	oConfig.set(pEvent.GetCString(), App.STToggle_Cast(pEvent.GetSource()).GetState())

	pObject.CallNextHandler(pEvent)

def HullHit(pObject, pEvent):
	debug(__name__ + ", HullHit")
	oConfig = LibConfig.Config("BridgePluginConfig")
	if pEvent.IsHullHit() and oConfig.get("Hull Impact", 0):# and App.TopWindow_GetTopWindow().IsBridgeVisible():
		lList =["sfx/Bridge/Impacts/impact1.wav", "sfx/Bridge/Impacts/impact2.wav", 
			"sfx/Bridge/Impacts/impact3.wav", "sfx/Bridge/Impacts/impact4.wav", 
			"sfx/Bridge/Impacts/impact5.wav"]
		if oBridgePlugin.oBridgeInfo.__dict__.has_key("HullHitSounds"):
			lList = oBridgePlugin.oBridgeInfo.HullHitSounds[:]
		iChosen = App.g_kSystemWrapper.GetRandomNumber(len(lList))
		sSound = lList[iChosen]

		pSound = App.g_kSoundManager.GetSound(sSound)

		if pSound:
			pSound.Play()

	pObject.CallNextHandler(pEvent)

def BridgeToggle(pObject, pEvent):
	debug(__name__ + ", BridgeToggle")
	wChar = pEvent.GetUnicode()

	if (wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_MAP_MODE, App.KeyboardBinding.GET_EVENT, 0.0)) or (wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_CINEMATIC_MODE, App.KeyboardBinding.GET_EVENT, 0.0)) or (wChar == App.g_kKeyboardBinding.FindKey(App.ET_INPUT_TOGGLE_BRIDGE_AND_TACTICAL, App.KeyboardBinding.GET_EVENT, 0.0)):
		if App.TopWindow_GetTopWindow().IsBridgeVisible():
			MuteSpace()
		elif App.TopWindow_GetTopWindow().IsTacticalVisible():
			MuteBridge()
	pObject.CallNextHandler(pEvent)

def MissionStart(pObject, pEvent):
	debug(__name__ + ", MissionStart")
	if App.TopWindow_GetTopWindow().IsBridgeVisible():
		MuteSpace()
	else:
		MuteBridge()
	pObject.CallNextHandler(pEvent)

def MuteBridge():
	debug(__name__ + ", MuteBridge")
	oConfig = LibConfig.Config("BridgePluginConfig")
	#iBridgeMute = App.TGSoundRegion.FT_MUFFLE
	#if oConfig.get("Bridge Muffled", 0):
	#	iBridgeMute = App.TGSoundRegion.FT_NONE
	
	#pBridge = App.TGSoundRegion_GetRegion("BridgeGeneric")
	#if pBridge:
	#	pBridge.SetFilter(iBridgeMute)
	#pBridge = App.TGSoundRegion_GetRegion("bridge")
	#if pBridge:
	#	pBridge.SetFilter(iBridgeMute)

	if App.Game_GetCurrentPlayer() and App.Game_GetCurrentPlayer().GetContainingSet():
		pSpace = App.TGSoundRegion_GetRegion(App.Game_GetCurrentPlayer().GetContainingSet().GetName())
		pSpace.SetFilter(App.TGSoundRegion.FT_NONE)


def MuteSpace():
	debug(__name__ + ", MuteSpace")
	oConfig = LibConfig.Config("BridgePluginConfig")
	iSpaceMute = App.TGSoundRegion.FT_NONE
	if oConfig.get("Space Muted2", 0):
		iSpaceMute = App.TGSoundRegion.FT_MUTE

	#pBridge = App.TGSoundRegion_GetRegion("BridgeGeneric")
	#if pBridge:
	#	pBridge.SetFilter(App.TGSoundRegion.FT_NONE)
	#pBridge = App.TGSoundRegion_GetRegion("bridge")
	#if pBridge:
	#	pBridge.SetFilter(App.TGSoundRegion.FT_NONE)

	# Restart the ambient sound
	#pSound = App.g_kSoundManager.GetSound("AmbBridge")
	#if (pSound != None):
	#	pSound.SetLooping(1)
	#	pSound.SetPriority(1.0)
	#	pSound.Play()

	if App.Game_GetCurrentPlayer() and App.Game_GetCurrentPlayer().GetContainingSet():
		pSpace = App.TGSoundRegion_GetRegion(App.Game_GetCurrentPlayer().GetContainingSet().GetName())
		pSpace.SetFilter(iSpaceMute)

# App override for the muting...
def ToggleBridgeAndTactical(self):
	debug(__name__ + ", ToggleBridgeAndTactical")
	App.Appc.TopWindow_ToggleBridgeAndTactical(self)
	if self.IsBridgeVisible():
		MuteSpace()
	else:
		MuteBridge()

def ToggleCinematicWindow(self):
	debug(__name__ + ", ToggleCinematicWindow")
	App.Appc.TopWindow_ToggleCinematicWindow(self)
	pCinematic = App.CinematicWindow_Cast(self.FindMainWindow(App.MWT_CINEMATIC))
	if pCinematic and pCinematic.IsWindowActive():
		MuteBridge()
	else:
		if self.IsBridgeVisible():
			MuteSpace()
		else:
			MuteBridge()

def ToggleMapWindow(self):
	debug(__name__ + ", ToggleMapWindow")
	App.Appc.TopWindow_ToggleMapWindow(self)
	pMap = App.CinematicWindow_Cast(self.FindMainWindow(App.MWT_TACTICAL_MAP))
	if pMap and pMap.IsWindowActive():
		MuteBridge()
	else:
		if self.IsBridgeVisible():
			MuteSpace()
		else:
			MuteBridge()

def ForceBridgeVisible(self):
	debug(__name__ + ", ForceBridgeVisible")
	App.Appc.TopWindow_ForceBridgeVisible(self)
	MuteSpace()

def ForceTacticalVisible(self):
	debug(__name__ + ", ForceTacticalVisible")
	App.Appc.TopWindow_ForceTacticalVisible(self)
	MuteBridge()

App.TopWindow.ToggleBridgeAndTactical = ToggleBridgeAndTactical
App.TopWindow.ToggleCinematicWindow = ToggleCinematicWindow
App.TopWindow.ToggleMapWindow = ToggleMapWindow
App.TopWindow.ForceBridgeVisible = ForceBridgeVisible
App.TopWindow.ForceTacticalVisible = ForceTacticalVisible


def MakeRenderedSet(self, pName):
	debug(__name__ + ", MakeRenderedSet")
	pCurrentSet = self.GetRenderedSet()
	if pCurrentSet:
		sOldName = pCurrentSet.GetName()
		pSpace = App.TGSoundRegion_GetRegion(sOldName)
		if sOldName and sOldName != "bridge":
			pSpace.SetFilter(App.TGSoundRegion.FT_MUTE)

	App.Appc.SetManager_MakeRenderedSet(self, pName)

	pCurrentSet = self.GetRenderedSet()
	sName = pCurrentSet.GetName()
	pSpace = App.TGSoundRegion_GetRegion(sName)
	if sName:
		pSpace.SetFilter(App.TGSoundRegion.FT_NONE)
App.SetManager.MakeRenderedSet = MakeRenderedSet
