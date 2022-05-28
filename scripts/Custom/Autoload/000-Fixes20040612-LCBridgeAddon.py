from bcdebug import debug
import App
import Foundation
import LoadBridge
import MissionLib
if not MissionLib.__dict__.has_key("SetupCharacter"):
	reload(MissionLib)# Reloading seems to give MissionLib it's functions back.
import string
import nt
import LibConfig

class ListCompare:
	def __init__(self, list):
		debug(__name__ + ", __init__")
		self.list = list

	def __cmp__(self, other):# Not entirely according to convention, but it does the trick
		return not other in self.list

#import types
##################################################
##						##
## Right, this acts like a module replacement,	##
## since global variables need to be "imported"	##
## using the global keyword while globals from	##
## a module don't. Using static variables from	##
## a class give the same effect while loosing	##
## the dependance of the module.		##
##						##
##################################################
class types:
	debug(__name__ + ", __cmp__")
	DictionaryType = type({})
	ListType = type([])
	TupleType= type(())
	StringType = type("")
	ArrayType    = ListCompare([ListType, TupleType])
	SequenceType = ListCompare([StringType, ArrayType])
	ContainerType= ListCompare([DictionaryType, SequenceType])

types.InstanceType = type(types())
# The above is a little trick I developed for BP Uniforms. ^_^ -MLeo


NonSerializedObjects = (
"bDebug",
"oEventQueue",
"FTBEventUser",
"FTBEvent",
"Debug",
"oConfigModule",
"oBridgeInfo",
"lBridgePluginList",
"inited",
"test",
"dConvNameToSystem",
"lET",
"dSubsystemDict",
"lShieldNumConv",
"PBLMode",
"g_idMasterSequenceObj",
)

bDebug = 1

sVersion = "20070204"


oConfigModule = None

def Load(sBridgeConfigScript):
	# First, try and load the bridge plugin menu and config
	debug(__name__ + ", Load")
	global oConfigModule
	oConfigModule = LibConfig.Config("BridgePluginConfig")

	Foundation.pCurrentBridge = Foundation.bridgeList[sBridgeConfigScript]

	Plug = None
	OldPlug = None
	if Foundation.bridgeList._keyList.has_key(sBridgeConfigScript):
		Plug = Foundation.bridgeList._keyList[sBridgeConfigScript]

		# Check if the bridge is marked implicit, and if it is, evaluate it
		if Plug and Plug.__dict__.get("IsImplicit", 0):
			Load(Plug())
			return

	pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"));
	if (pBridgeSet == None):
		pBridgeSet = LoadBridge.CreateAndPopulateBridgeSet()
	else:
		if pBridgeSet.IsSameConfig(sBridgeConfigScript):
			InitBridgeEvents(Plug, pBridgeSet)
			CheckPlugins(Plug, pBridgeSet)
			return
		else:
			pcOldBridgeConfigScript = pBridgeSet.GetConfig ()
			pOldMod = __import__("Bridge." + pcOldBridgeConfigScript)

			if Foundation.bridgeList._keyList.has_key(pcOldBridgeConfigScript):
				OldPlug = Foundation.bridgeList._keyList[pcOldBridgeConfigScript]
				if OldPlug.__dict__.has_key("ExtraObjects"):
					#Debug("DEBUG: The old bridge has extra objects, remove them")
					pBridgeObject = App.BridgeObjectClass_Cast(pBridgeSet.GetObject('bridge'))
					for i in OldPlug.__dict__["ExtraObjects"].keys():
						pBridgeObject.DetachObject(App.BridgeObjectClass_Cast(pBridgeSet.GetObject(i)))
						pBridgeSet.DeleteObjectFromSet(i)

			pOldMod.UnloadAnimations()
			pOldMod.UnloadSounds()

	pCamera = None
	pViewScreen = pBridgeSet.GetViewScreen()
	if (pViewScreen != None):
		pCamera = pViewScreen.GetRemoteCam()

	pBridgeSet.DeleteObjectFromSet("bridge")
	pBridgeSet.DeleteObjectFromSet("viewscreen")
	pBridgeSet.DeleteCameraFromSet("maincamera")

	pMod = __import__("Bridge." + sBridgeConfigScript)
	pMod.CreateBridgeModel(pBridgeSet)

	# Delete extra's
	lExtraNames = ["MaleExtra1", "MaleExtra2", "MaleExtra3", "FemaleExtra1", "FemaleExtra2", "FemaleExtra3"]
	for pcName in lExtraNames:
		if App.CharacterClass_GetObject(pBridgeSet, pcName):
			pBridgeSet.DeleteObjectFromSet(pcName)

	# Let's do the extra's a bit better
	iExtraMode = 1 # 1 stock 2 modded 3 predefined list
	iNumExtras = 3
	
	lLoadedExtras = []

	if Foundation.bridgeList._keyList.has_key(sBridgeConfigScript):
		Plug = Foundation.bridgeList._keyList[sBridgeConfigScript]
		if Plug.__dict__.has_key("ExtraObjects") and (oConfigModule != None and (oConfigModule.get("Disable Extra Models", 0) == 0 and oConfigModule.get(Plug.name, 0) == 0)):
			pLight = pBridgeSet.GetLight("ambientlight1")
			pBridgeObject = App.BridgeObjectClass_Cast(pBridgeSet.GetObject('bridge'))
			for name, config in Plug.ExtraObjects.items():
				iDetail = App.g_kImageManager.GetImageDetail()
				pcDetail = [ "Low/", "Medium/", "High/" ]
				pcEnvPath = config[1] + pcDetail[iDetail]

				App.g_kModelManager.LoadModel(config[0], None, pcEnvPath)

				pObject = App.BridgeObjectClass_Create(config[0])
				pBridgeSet.AddObjectToSet(pObject, name)

				if len(config) > 2:
					apply(pObject.SetTranslateXYZ, config[2].get("Translation", (0,0,0)))
					apply(pObject.SetAngleAxisRotation, config[2].get("Rotation", (0,1,0,0)))

				pLight.AddIlluminatedObject(pObject)
				pBridgeObject.AttachObject(pObject)
				pObject.UpdateNodeOnly()

		if Plug.__dict__.has_key("NumExtras") and (oConfigModule != None and (oConfigModule.get("Disable Extra Crew Extensions", 0) == 0 and oConfigModule.get(Plug.name, 0) == 0)):
			if type(Plug.NumExtras) == types.ArrayType:
				lExtraNames = Plug.NumExtras
				iExtraMode = 3
			else:
				iExtraMode = 2
				iNumExtras = int(Plug.NumExtras)

	if iExtraMode == 1:
		for i in range(3):
			pcPath = None
			if not App.g_kSystemWrapper.GetRandomNumber(2):
				pcPath = "Bridge.Characters.FemaleExtra" + str(i+1)
			else:
				pcPath = "Bridge.Characters.MaleExtra" + str(i+1)
			lLoadedExtras.append(__import__(pcPath).CreateCharacter(pBridgeSet))
	elif iExtraMode == 2:
		lPicked = []
		for j in range(iNumExtras):
			i = App.g_kSystemWrapper.GetRandomNumber(Plug.NumExtras)
			while lExtraNames[i] in lPicked:
				i = App.g_kSystemWrapper.GetRandomNumber(Plug.NumExtras)
			lLoadedExtras.append(__import__("Bridge.Characters." + lExtraNames[i]).CreateCharacter(pBridgeSet))
			lPicked.append(lExtraNames[i])
	elif iExtraMode == 3:
		for n in lExtraNames:
			if type(n) == types.ArrayType:
				i = App.g_kSystemWrapper.GetRandomNumber(len(n))
				lLoadedExtras.append(__import__(n[i]).CreateCharacter(pBridgeSet))
			else:
				lLoadedExtras.append(__import__(n).CreateCharacter(pBridgeSet))

	LoadBridge.LoadSounds()

	pMod.LoadSounds()

	SetupCustomEvents(Plug, pBridgeSet)

	pMod.ConfigureCharacters(pBridgeSet)
	pMod.PreloadAnimations ()

	if (pCamera != None):
		pViewScreen = pBridgeSet.GetViewScreen()
		pViewScreen.SetRemoteCam(pCamera)
		pViewScreen.SetIsOn(1)

	pBridgeSet.SetConfig(sBridgeConfigScript)

	import Bridge.Characters.CommonAnimations
	Bridge.Characters.CommonAnimations.PutGuestChairOut()

	# Last but not least, check the plugins...
	CheckPlugins(Plug, pBridgeSet)

if int(Foundation.version[0:8]) < 20040612:

	LoadBridge.Load = Load
	try:
		test = __import__("Fixes20030217")
		if not test:
			raise ImportError
		test.LoadBridge_Load = Load
		LoadBridge.Load = Load
		test = None
	except ImportError:
		pass
	except:
		pass

	# Copying all information from the plugin to the bridge object
	def __init__r(self, name, bridgeString, dict = {}):
		debug(__name__ + ", __init__r")
		self.bridgeString = bridgeString
		self.num = Foundation.bridgeList.Register(self, name)

		Foundation.bridgeList._keyList[bridgeString] = self
		self.IsImplicit = 0

		self.locations = None
		self.__dict__.update(dict)

		Foundation.MutatorElementDef.__init__(self, name, dict)

	Foundation.BridgeDef.__init__ = __init__r

	class ImplicitBridgeDef(Foundation.BridgeDef):
		def __init__(self, name, dict = {}):
			debug(__name__ + ", __init__")
			Foundation.BridgeDef.__init__(self, name, name, dict)
			self.IsImplicit = 1

		def __call__(self):
			debug(__name__ + ", __call__")
			raise NotImplementedError("This function is required to be implemented for an implicit Bridge")

	Foundation.ImplicitBridgeDef = ImplicitBridgeDef

	class RandomBridge(Foundation.ImplicitBridgeDef):
		def __call__(self):
			debug(__name__ + ", __call__")
			sSelectedBridge = "Random Bridge"
			Random = lambda iMax : int(App.g_kSystemWrapper.GetRandomNumber(iMax * 1000) / 1000)
			while sSelectedBridge == "Random Bridge":
				sSelectedBridge = Foundation.bridgeList._arrayList[Random(len(Foundation.bridgeList._arrayList))]
			return Foundation.bridgeList._keyList[sSelectedBridge].bridgeString

	oRandomBridge = RandomBridge("Random Bridge")

	Foundation.version = "20040612"

lBridgePluginList = []
class BridgePluginDef(Foundation.OverrideDef):
	def __init__(self, name, dict = None):
		debug(__name__ + ", __init__")
		Foundation.MutatorElementDef.__init__(self, name, dict) # Bypass the override stuff, we are only interrested in the Activate/Deactivate part
		if dict:
			self.__dict__.update(dict)
		global lBridgePluginList
		self.name = name
		lBridgePluginList.append(self)

		self.bActivated = 1

	def __call__(self, Plug, pBridgeSet, oBridgeInfo):
		debug(__name__ + ", __call__")
		pass

	def PlayerCreated(self, Plug, pBridgeSet, oBridgeInfo, pShip):
		debug(__name__ + ", PlayerCreated")
		pass

	def CreateMenu(self, pOptionsPane, pContentPanel, bGameEnded = 0):
		debug(__name__ + ", CreateMenu")
		return None
		#return App.TGPane_Create()

	# Used for (de)activation other than the configuration menu
	def Activate(self):
		debug(__name__ + ", Activate")
		self.bActivated = 1

	def Deactivate(self):
		debug(__name__ + ", Deactivate")
		self.bActivated = 0

	def _SwapInModules(self, pre, post):
		debug(__name__ + ", _SwapInModules")
		pass

	def _SwapOutModules(self, pre, post):
		debug(__name__ + ", _SwapOutModules")
		pass

Foundation.BridgePluginDef = BridgePluginDef

def DelayPluginLoad(pObject, pEvent):
	debug(__name__ + ", DelayPluginLoad")
	if pEvent: # We got here through the non FoundationTrigger way, check if the ship is the player
		pPlayer = App.Game_GetCurrentPlayer()
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		bExit = 0
		if pPlayer and pShip:
			if not pPlayer.GetObjID() == pShip.GetObjID():
				bExit = 1
			else:# Remove ourselfs
				App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_CREATED, MissionLib.GetMission(), __name__ + ".DelayPluginLoad2")
		else:
			bExit = 1
		if bExit:
			pObject.CallNextHandler(pEvent)
			return
	global oBridgeInfo
	if oBridgeInfo:
		oBridgeInfo.pShip = App.Game_GetCurrentPlayer().this
		pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
		Plug = Foundation.bridgeList._keyList[pBridgeSet.GetConfig()]
		CheckPlugins(Plug, pBridgeSet)
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def PlayerCreated(pObject, pEvent):
	debug(__name__ + ", PlayerCreated")
	pPlayer = App.ShipClass_Cast(pEvent.GetDestination())
	if pPlayer and pPlayer.GetObjID()==App.Game_GetCurrentPlayer().GetObjID():
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_CREATED, MissionLib.GetMission(), __name__ + ".PlayerCreated")

		pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
		Plug = Foundation.bridgeList._keyList[pBridgeSet.GetConfig()]

		AttachPlayerEvents(Plug, pBridgeSet)

		global oBridgeInfo, oConfigModule, bDebug

		if oBridgeInfo:
			for plugin in lBridgePluginList:
				if not oConfigModule.get("Disable " + plugin.name, 0):
					if oConfigModule.get("Debug Mode", 0) or bDebug:
						plugin.PlayerCreated(Plug, pBridgeSet, oBridgeInfo, App.ShipClassPtr(oBridgeInfo.pShip))
					else:
						try:
							plugin.PlayerCreated(Plug, pBridgeSet, oBridgeInfo, App.ShipClassPtr(oBridgeInfo.pShip))
						except:
							print plugin.name, "failed to load"
							continue


	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

def CheckPlugins(Plug, pBridgeSet):
	debug(__name__ + ", CheckPlugins")
	global oBridgeInfo, oConfigModule, bDebug

	if oConfigModule == None and (oConfigModule.get("Disable Plugins", 0) or oConfigModule.get(Plug.name, 0)):
		return

	bPlayerLoaded = 0
	if oBridgeInfo.pShip:
		bPlayerLoaded = 1

	if oBridgeInfo:
		for plugin in lBridgePluginList:
			if plugin.bActivated and not oConfigModule.get("Disable " + plugin.name, 0):
				if oConfigModule.get("Debug Mode", 0) or bDebug:
					plugin(Plug, pBridgeSet, oBridgeInfo)
					if bPlayerLoaded:
						plugin.PlayerCreated(Plug, pBridgeSet, oBridgeInfo, App.ShipClassPtr(oBridgeInfo.pShip))
				else:
					try:
						plugin(Plug, pBridgeSet, oBridgeInfo)
						if bPlayerLoaded:
							plugin.PlayerCreated(Plug, pBridgeSet, oBridgeInfo, App.ShipClassPtr(oBridgeInfo.pShip))
					except:
						print plugin.name, "failed to load"
						continue

class BridgeInformation:
	def __init__(self):

		# Initialize to default values
		debug(__name__ + ", __init__")
		self.Prefix		= ""
		self.pMission		= 0
		# The next 2 are just here for conveinience, not the "proper" way though. ;)
		self.BridgeDamageAni	= ["bridgelightdamage.nif", "bridgemediumdamage.nif", "bridgeharddamage.nif"]
		self.HullDamageAni	= ["hulllightdamage.nif", "hullmediumdamage.nif", "hullharddamage.nif", "hullholes.nif"]
		self.CurrentMaps	= {}
		self.NormalMaps		= {}
		self.GreenMaps		= {}
		self.YellowMaps		= {}
		self.RedMaps		= {}
		self.WarpMaps		= {}
		self.PhaserMaps		= {}
		self.TorpedoMaps	= {}
		self.EngineMaps		= {}
		self.ShieldMaps		= {}
		self.pShip		= 0
		self.pHull		= 0
		self.pBridge		= 0
		# 0=HullState, 1=BrdState
		self.DamInfo		= [0,0]
		self.ExtraObjects	= {}
		#self.LastInfo		= {"Warp": -1, "Torpedo": -1, "Phaser": -1, "Engine": -1}
		self.lShields		= [0,0,0,0,0,0]
		self.dDamageInfo	= {}
		self.lCurrentRangeChecks= []
		self.bMVAM		= 0
		self.TexturedObjects	= {}

		# Per Bridge Loading screen
		self.LoadingScreen = "data/Icons/ViewscreenLoading.tga"

#	def __del__(self):
#		self.Clean()

	def Clean(self):
		debug(__name__ + ", Clean")
		self.pShip = self.pHull = self.pBridge = self.pMission = 0

		if self.__dict__.has_key("AllAnimations"):
			kAM = App.g_kAnimationManager
			for ani in self.__dict__["AllAnimations"]:
				if kAM.IsLoaded(ani):
					kAM.FreeAnimation(ani)
			self.AllAnimations = []

		# It might just be that the ship itself does no longer exist, so why would these range checks still exist then?
		"""while len(self.lCurrentRangeChecks)>0:
			idWatcher, idRange = self.lCurrentRangeChecks.pop(0)
			App.Appc.FloatRangeWatcher_RemoveRangeCheck(idWatcher, idRange)"""

oBridgeInfo = None
inited = 0

def SetupCustomEvents(Plug, pBridgeSet):
	debug(__name__ + ", SetupCustomEvents")
	global inited, oBridgeInfo, oConfigModule
	if oBridgeInfo:
		oBridgeInfo.Clean()
	oBridgeInfo = None

	if oConfigModule == None and (oConfigModule.get(Plug.name, 0) or oConfigModule.get("Disable Active LCARs", 0)):
		return

	oBridgeInfo = BridgeInformation()
	# Getting bridge prefix
	if not Plug.__dict__.has_key("locations") or Plug.locations == None or len(Plug.locations.keys()) <= 0:
		if Plug.bridgeString == "GalaxyBridge":
			oBridgeInfo.sPrefix = "Gal"
		elif Plug.bridgeString == "SovereignBridge":
			oBridgeInfo.sPrefix = "Sov"
		else:
			return
	else:
		oBridgeInfo.sPrefix = Plug.locations.keys()[0][0:3]

	oBridgeInfo.__dict__.update(Plug.__dict__)
	for name in (["bridge"] + oBridgeInfo.ExtraObjects.keys()):
		oBridgeInfo.TexturedObjects[name] = BridgeObject(name)

	if Plug.__dict__.has_key("Maps"):
		oBridgeInfo.__dict__.update(Plug.Maps)
		if Plug.Maps.has_key("GreenMaps") and not Plug.Maps.has_key("CurrentMaps"):
			oBridgeInfo.CurrentMaps = {}
			for key, map in Plug.Maps["GreenMaps"].items():
				SwitchMaps(key, map)
			
		# Normal Maps are maps that should be displayed when the bridge is first loaded, similar to my starship Skinning and Damaging Tool
		for name, map in oBridgeInfo.NormalMaps.items():
			SwitchMaps(name, map)


	kAM = App.g_kAnimationManager
	if oBridgeInfo.__dict__.has_key("Animations"):
		# Obtain all the animations
		oBridgeInfo.__dict__["AllAnimations"] = []
		for key in oBridgeInfo.Animations.keys():
			if key == "AnimationInfo":
				oBridgeInfo.Animations["AnimationInfo"] = {}
				continue
			for aniObj in oBridgeInfo.Animations[key].keys():
				for ani in oBridgeInfo.Animations[key][aniObj]:
					if type(ani)==types.DictionaryType:
						ani = ani["ani"]
					if type(ani)==types.TupleType:
						ani = ani[0]
					if ani not in oBridgeInfo.AllAnimations:
						oBridgeInfo.AllAnimations.append(ani)
						if not kAM.IsLoaded(ani):
							kAM.LoadAnimation(ani, ani)
							if not kAM.IsLoaded(ani):
								print "WARNING custom animation:", ani, "failed to load!"

	InitBridgeEvents(Plug, pBridgeSet)

dConvNameToSystem = {	"Hull":	App.ShipClass.GetHull,
			"Phaser":  App.ShipClass.GetPhaserSystem,
			"Torpedo": App.ShipClass.GetTorpedoSystem,
			"Pulse":   App.ShipClass.GetPulseWeaponSystem,
			"Power":   App.ShipClass.GetPowerSubsystem,
			"Warp":	App.ShipClass.GetWarpEngineSubsystem,
			"Impulse": App.ShipClass.GetImpulseEngineSubsystem,
			"Cloak":   App.ShipClass.GetCloakingSubsystem,
}

lET = []
def InitBridgeEvents(Plug, pBridgeSet):
	# Now I need to init the stuff...

	debug(__name__ + ", InitBridgeEvents")
	global oBridgeInfo, oConfigModule
	if (oBridgeInfo == None) or (oConfigModule == None) or oConfigModule.get(Plug.name, 0) or oConfigModule.get("Disable Active LCARs", 0):
		return

	pNewMission = MissionLib.GetMission()
	if oBridgeInfo.pMission != pNewMission.this:
		oBridgeInfo.pMission = pNewMission.this
		if oBridgeInfo.pMission:
			App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_ALERT_LEVEL, oBridgeInfo.pMission, __name__ + ".AlertLevel")


	if Plug.__dict__.has_key("Sounds"):
		if Plug.Sounds.has_key("Preload"): # This needs to be done first, or later on it won't register as preloaded.
			for key in Plug.Sounds["Preload"].keys():
				InitSound(key, Plug.Sounds["Preload"][key])

		for key in Plug.Sounds.keys():
			# Filter out special cases
			if key == "Preload":
				continue
			elif key == "Shields":
				for key2 in Plug.Sounds["Shields"].keys():
					prefix = "Shields" + key2
					for key3 in Plug.Sounds["Shields"][key2].keys():
						if not Plug.SoundCache.has_key(prefix + str(key3)):
							InitSound(prefix + str(key3), Plug.Sounds["Shields"][key2][key3])
			elif key in dConvNameToSystem.values():
				for key2 in Plug.Sounds[key].keys():
					if not Plug.SoundCache.has_key(key + str(key2)):
						InitSound(key + str(key2), Plug.Sounds[key][key2])
			else:# Just for readability.
				if not Plug.Sounds.has_key(key):
					InitSound(key, Plug.Sounds[key])

	if not App.Game_GetCurrentPlayer():
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED, MissionLib.GetMission(), __name__ + ".PlayerCreated")
		return

	AttachPlayerEvents(Plug, pBridgeSet)

def AttachPlayerEvents(Plug, pBridgeSet):

	debug(__name__ + ", AttachPlayerEvents")
	global oBridgeInfo, oConfigModule
	if (oBridgeInfo == None) or (oConfigModule == None) or oConfigModule.get(Plug.name, 0) or oConfigModule.get("Disable Active LCARs", 0):
		return

	pShip = App.Game_GetCurrentPlayer()
	if not pShip:
		return
	oBridgeInfo.pShip = pShip.this
	if not oBridgeInfo.pShip:
		return

	# For End Simulation in Quick Battle
	pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertLevel")

	oBridgeInfo.pHull = pShip.GetHull().this
	if Plug.__dict__.has_key("BridgeName"):
		pSystemIter = pShip.StartGetSubsystemMatch(App.CT_HULL_SUBSYSTEM)
		pSystem = pShip.GetNextSubsystemMatch( pSystemIter )
		while pSystem != None:
			if pSystem.GetName() == Plug.BridgeName:
				oBridgeInfo.pBridge = pSystem.this
				oBridgeInfo.DamInfo[1] = oBridgeInfo.DamInfo[3] = pSystem.GetCondition()
				break
			pSystem = App.Appc.ShipClass_GetNextSubsystemMatch(oBridgeInfo.pShip, pSystemIter)
		pShip.EndGetSubsystemMatch(pSystemIter)

	pShields = pShip.GetShields()
	if pShields and oBridgeInfo.__dict__.has_key("ShieldMaps"):
		for i in range(6):
			oBridgeInfo.lShields[i] = pShields.GetCurShields(i)
		lRanges = []
		for key in oBridgeInfo.ShieldMaps.keys():
			for iLevel in oBridgeInfo.ShieldMaps[key].keys():
				fLevel = iLevel / 100.0
				if fLevel not in lRanges:
					lRanges.append(fLevel)

		pShieldWatcher = pShields.GetShieldWatcher(6)
		for fRange in lRanges:
			pEvent = App.TGFloatEvent_Create()
			pEvent.SetEventType(App.ET_TACTICAL_SHIELD_LEVEL_CHANGE)
			pEvent.SetDestination(pShip)
			oBridgeInfo.lCurrentRangeChecks.append((pShieldWatcher.this, pShieldWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BOTH, pEvent)))

		pShip.AddPythonFuncHandlerForInstance(App.ET_TACTICAL_SHIELD_LEVEL_CHANGE, __name__ + ".ShieldChange")
		pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".ShieldChange")
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_SET_ALERT_LEVEL, oBridgeInfo.pMission, __name__ + ".ShieldChange")

	for key in dConvNameToSystem.keys():
		if oBridgeInfo.__dict__.has_key(key + "Maps"):
			pSubsystem = dConvNameToSystem[key](pShip)
			if pSubsystem:
				lRanges = []
				for i in oBridgeInfo.__dict__[key + "Maps"].keys():
					lRanges.append(i/100.0)
				# Need an event for this range check..
				pSubsystemWatcher = pSubsystem.GetCombinedPercentageWatcher()
				for fRange in lRanges:
					pEvent = App.TGFloatEvent_Create()
					pEvent.SetEventType(App.ET_SUBSYSTEM_STATE_CHANGED)
					pEvent.SetDestination(pShip)
					pEvent.SetSource(pSubsystem)
					oBridgeInfo.lCurrentRangeChecks.append((pSubsystemWatcher.this, pSubsystemWatcher.AddRangeCheck(fRange, App.FloatRangeWatcher.FRW_BOTH, pEvent)))

	pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemChange")
	
	pBridgeObject = App.BridgeObjectClass_Cast(pBridgeSet.GetObject('bridge'))
	iLevel = pShip.GetAlertLevel()
	if iLevel == App.ShipClass.GREEN_ALERT:
		pBridgeObject.GoToGreenAllert()
	elif iLevel == App.ShipClass.YELLOW_ALERT:
		pBridgeObject.GoToYellowAllert()
	elif iLevel == App.ShipClass.RED_ALERT:
		pBridgeObject.GoToRedAllert()
	inited = 1

	# Now, give the ship the most recent status textures by checking all main systems
	lSystems = [
		App.ShipClass.GetHull,
		App.ShipClass.GetShields,
		App.ShipClass.GetPowerSubsystem,
		App.ShipClass.GetSensorSubsystem,
		App.ShipClass.GetImpulseEngineSubsystem,
		App.ShipClass.GetWarpEngineSubsystem,
		App.ShipClass.GetTorpedoSystem,
		App.ShipClass.GetPhaserSystem,
		App.ShipClass.GetPulseWeaponSystem,
		App.ShipClass.GetTractorBeamSystem,
		App.ShipClass.GetRepairSubsystem,
		App.ShipClass.GetCloakingSubsystem,
	]
	for func in lSystems:
		CheckSubsystem(func(pShip), 0, 0)
	ShieldChange(None, None, 0, 0)

sLastAlertEvent = None

def AlertLevel(pObject, pEvent):
	debug(__name__ + ", AlertLevel")
	if (pObject and pEvent):
		pObject.CallNextHandler(pEvent)

	global sLastAlertEvent
	if pEvent:
		if sLastAlertEvent == pEvent.this:
			return
		else:
			sLastAlertEvent = pEvent.this

	global oBridgeInfo
	if not oBridgeInfo:
		oBridgeInfo = BridgeInformation()
	if not oBridgeInfo.pShip:
		oBridgeInfo.pShip = App.Game_GetCurrentPlayer().this
	level = App.Appc.ShipClass_GetAlertLevel(oBridgeInfo.pShip)

	if not oBridgeInfo.bMVAM:
		if level == 0:
			if oBridgeInfo.GreenMaps.keys():
				for key, item in oBridgeInfo.GreenMaps.items():
					SwitchMaps(key, item)
			if oBridgeInfo.__dict__.has_key("Sounds") and oBridgeInfo.Sounds.has_key("GreenAlert"):
				for key in oBridgeInfo.Sounds["GreenAlert"].keys():
					PlaySoundByName(key)

			HandleTypeBasedAnimation("GreenAlert", oBridgeInfo, 1)

		elif level == 1:
			if oBridgeInfo.YellowMaps.keys():
				for key, item in oBridgeInfo.YellowMaps.items():
					SwitchMaps(key, item)
			if oBridgeInfo.__dict__.has_key("Sounds") and oBridgeInfo.Sounds.has_key("YellowAlert"):
				for key in oBridgeInfo.Sounds["YellowAlert"].keys():
					PlaySoundByName(key)
			HandleTypeBasedAnimation("YellowAlert", oBridgeInfo, 1)

		elif level == 2:
			if oBridgeInfo.RedMaps.keys():
				for key, item in oBridgeInfo.RedMaps.items():
					SwitchMaps(key, item)
			if oBridgeInfo.__dict__.has_key("Sounds") and oBridgeInfo.Sounds.has_key("RedAlert"):
				for key in oBridgeInfo.Sounds["RedAlert"].keys():
					PlaySoundByName(key)

			HandleTypeBasedAnimation("RedAlert", oBridgeInfo, 1)

	elif oBridgeInfo.bMVAM == 1:
		for name, item in oBridgeInfo.RedMaps.items():# Flush it to red alert
			SwitchMaps(name, item)
		pBridgeObject = App.BridgeObjectClass_Cast(App.g_kSetManager.GetSet("bridge").GetObject("bridge"))
		pBridgeObject.GoToRedAllert()

		if hasattr(oBridgeInfo, "MVAMMaps"):
			for key, item in oBridgeInfo.MVAMMaps.items():
				SwitchMaps(key, item)

		HandleTypeBasedAnimation("MVAMSeparating", oBridgeInfo, 1)
		oBridgeInfo.bMVAM = 0 # Reset this

	elif oBridgeInfo.bMVAM == -1:
		for key, item in oBridgeInfo.RedMaps.items():# Flush it to red alert
			SwitchMaps(key, item)
		pBridgeObject = App.BridgeObjectClass_Cast(App.g_kSetManager.GetSet("bridge").GetObject("bridge"))
		pBridgeObject.GoToRedAllert()
		oBridgeInfo.bMVAM = 0
		HandleTypeBasedAnimation("MVAMReintegrating", oBridgeInfo, 1)


dSubsystemDict = {App.CT_POWER_SUBSYSTEM:	"Power",
		  App.CT_PHASER_SYSTEM:		"Phaser",
		  App.CT_PHASER_BANK:		"Phaser",
		  App.CT_TORPEDO_SYSTEM:	"Torpedo",
		  App.CT_TORPEDO_TUBE:		"Torpedo",
		  App.CT_PULSE_WEAPON_SYSTEM:	"Pulse",
		  App.CT_PULSE_WEAPON:		"Pulse",
		  App.CT_HULL_SUBSYSTEM:	"Hull",
		  App.CT_WARP_ENGINE_SUBSYSTEM:	"Warp",
		  App.CT_IMPULSE_ENGINE_SUBSYSTEM:"Impulse",
		  App.CT_CLOAKING_SUBSYSTEM:	"Cloak",
}

sLastSubsystemChangeEvent = None

def SubsystemChange(pObject, pEvent):

	debug(__name__ + ", SubsystemChange")
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

	global sLastSubsystemChangeEvent
	if pEvent:
		if sLastSubsystemChangeEvent == pEvent.this:
			return
		else:
			sLastSubsystemChangeEvent = pEvent.this

	pSubsystem = App.ShipSubsystem_Cast(pEvent.GetSource())
	CheckSubsystem(pSubsystem)
	if (pObject and pEvent):
		pObject.CallNextHandler(pEvent)

def CheckSubsystem(pSubsystem, bSounds = 1, bAnimations = 1):
	debug(__name__ + ", CheckSubsystem")
	if not pSubsystem:
		return
	global oBridgeInfo
	sType = "Undefined"
	if pSubsystem:
		if dSubsystemDict.has_key(pSubsystem.GetObjType()):
			sType = dSubsystemDict[pSubsystem.GetObjType()]
			if sType == "Hull":
				if oBridgeInfo.pBridge and oBridgeInfo.pBridge == pSubsystem.this:
					sType = "Bridge"
			if CheckCondition(pSubsystem):
				if oBridgeInfo.__dict__.has_key(sType + "Maps"):
					if oBridgeInfo.__dict__[sType+"Maps"]:
						level = FindClosest(int(pSubsystem.GetConditionPercentage()*100), oBridgeInfo.__dict__[sType + "Maps"].keys())
						for key, map in oBridgeInfo.__dict__[sType + "Maps"][level].items():
							SwitchMaps(key, map)

				if oBridgeInfo.__dict__.has_key("Sounds") and oBridgeInfo.Sounds.has_key(sType) and bSounds:
					level = FindClosest(int(pSubsystem.GetConditionPercentage()*100), oBridgeInfo.Sounds[sType].keys())
					if oBridgeInfo.Sounds[sType][level]:
						for sSound in oBridgeInfo.Sounds[sType][level]:
							PlaySoundByName(sSound)
				if bAnimations:
					HandleTypeBasedAnimation(sType, oBridgeInfo)

def CheckCondition(pSubsystem):
	debug(__name__ + ", CheckCondition")
	sSubsystem = str(pSubsystem)
	iRetval = 1
	if oBridgeInfo.dDamageInfo.has_key(sSubsystem):
		iRetval = pSubsystem.GetCondition() != oBridgeInfo.dDamageInfo[sSubsystem]
	oBridgeInfo.dDamageInfo[sSubsystem] = pSubsystem.GetCondition()
	return iRetval

lShieldNumConv = [	"Front",
			"Rear",
			"Top",
			"Bottom",
			"Left",
			"Right"]


sLastShieldChangeEvent = None

# It would appear that shields don't really get changed when the alert changes, it just changes the GUI not the actual values of the shield
# Fake it if the ship is at green alert...
# The 2 extra parameters are here for when I only want map changes.
def ShieldChange(pObject, pEvent, bSounds = 1, bAnimations = 1):

	debug(__name__ + ", ShieldChange")
	if pObject and pEvent:
		pObject.CallNextHandler(pEvent)

	global sLastShieldChangeEvent
	if pEvent:
		if sLastShieldChangeEvent == pEvent.this:
			return
		else:
			sLastShieldChangeEvent = pEvent.this

	global oBridgeInfo
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer:
		iLevel = pPlayer.GetAlertLevel()
		pShields = pPlayer.GetShields()
		for i in range(6):
			if oBridgeInfo and oBridgeInfo.ShieldMaps.has_key(lShieldNumConv[i]):
				if len(oBridgeInfo.ShieldMaps[lShieldNumConv[i]].keys()) > 0:
					iShieldValue = int(pShields.GetSingleShieldPercentage(i)*100)
					if iLevel == App.ShipClass.GREEN_ALERT:
						iShieldValue = 0
					level = FindClosest(iShieldValue, oBridgeInfo.ShieldMaps[lShieldNumConv[i]].keys())
					for key in oBridgeInfo.ShieldMaps[lShieldNumConv[i]][level].keys():
						SwitchMaps(key, oBridgeInfo.ShieldMaps[lShieldNumConv[i]][level][key])

					if oBridgeInfo.__dict__.has_key("Sounds") and oBridgeInfo.__dict__.has_key("Shields") and bSounds:
						level = FindClosest(iShieldValue, oBridgeInfo.Sounds["Shields"][lShieldNumConv[i]].keys())
						for sSound in oBridgeInfo.Sounds["Shields"][lShieldNumConv[i]][level]:
							PlaySoundByName(sSound)
					if bAnimations:
						HandleTypeBasedAnimation("Shields", oBridgeInfo, 1)

def FindClosest(fValue, lOptions):
	debug(__name__ + ", FindClosest")
	lOptions.sort()
	for val in lOptions:
		if fValue <= val:
			return val
	return lOptions[0]
	
def Restore():
	debug(__name__ + ", Restore")
	global oBridgeInfo
	for key in oBridgeInfo.NormalMaps.keys():
		SwitchMaps(key, oBridgeInfo.NormalMaps[key])
	return 0

def PlaySoundByName(sKey):
	debug(__name__ + ", PlaySoundByName")
	global oBridgeInfo, oConfigModule
	if (not oBridgeInfo) or (not oConfigModule):
		return
	if not oConfigModule.get("Disable Sounds At Events", 0):
		return

	if not oBridgeInfo.__dict__.has_key("SoundCache"):
		return

	if not oBridgeInfo.SoundCache.has_key(sKey):
		return
	App.Appc.TGSound_Play(oBridgeInfo.SoundCache[sKey]["this"])

def InitSound(sKey, dConfig):
	debug(__name__ + ", InitSound")
	global oBridgeInfo
	if not oBridgeInfo:
		return
	if not oBridgeInfo.__dict__.has_key("SoundCache"):
		oBridgeInfo.__dict__["SoundCache"] = {}

	pGame = App.Game_GetCurrentGame()
	if not App.g_kSoundManager.GetSound(sKey):
		pSound = pGame.LoadSoundInGroup(sKey, dConfig["file"], "BridgeGeneric")
		pSound.SetVolume(dConfig.get("volume", 1.0))
		pRegion = App.TGSoundRegion_GetRegion("bridge")
		pRegion.AddSound(pSound)
		oBridgeInfo.SoundCache[sKey] = {"this": pSound.this}
		oBridgeInfo.SoundCache[sKey].update(dConfig)

# sOldMap is the map name it should have (so the "key")
# sNewMap is the path (relative to the root) with "proper" path seperation so / instead of the (wrong if you ask me) \ of Windows
#   This is with the extension of .tga but no (real) need for high/ med/ or low/ since BC does that for us.
def SwitchMaps(sOldMap, sNewMap):
	debug(__name__ + ", SwitchMaps")
	global oBridgeInfo, oConfigModule

	if oBridgeInfo == None or oConfigModule == None:
		return

	# Check if sOldMap contains references to specific objects
	lOldMap = list(sOldMap)

	lObjects = oBridgeInfo.TexturedObjects.keys()
	if lOldMap.count('@'):
		iAt = lOldMap.index('@')
		lObjects = []
		lOldMap.append(',')
		iLast = iAt
		while(lOldMap[iLast:].count(',')):
			lObjects.append(sOldMap[iLast:lOldMap.index(',')])
			iLast = lOldMap.index(',')+1

		sOldMap = sOldMap[:iAt]

	for name in lObjects:
		oObject = oBridgeInfo.TexturedObjects.get(name, None)
		if not oObject:
			print "Invalid object target for SwitchMaps:", name
			continue
		oObject.SwitchMap(sOldMap, sNewMap)

class BridgeObject:
	def __init__(self, sName):
		debug(__name__ + ", __init__")
		self.name = sName
		self.CurrentMaps = {}

	def SwitchMap(self, sMap, sNewMap):
		debug(__name__ + ", SwitchMap")
		oTexture = self.CurrentMaps.get(sMap, None)
		if not oTexture:
			oTexture = TextureMap(sMap, self.name)
			self.CurrentMaps[sMap] = oTexture
		oTexture.SwitchMap(sNewMap)

class TextureMap:
	def __init__(self, sName, sObject):
		debug(__name__ + ", __init__")
		self.name = sName
		self.object=sObject
		self.CurrentMap = sName[:]
		self.pSequence = None
		self.bInSequence = 0

	def SwitchMap(self, newmap):
		debug(__name__ + ", SwitchMap")
		self.StopAnimation()
		# Detect if newmap is an animation
		if type(newmap) == types.ArrayType and len(newmap) >= 2:# Animation packed as a list
			bLooping = newmap[0]
			dTrack = newmap[-1]
			iLoopNumTimes=-1
			if len(newmap) > 2:
				iLoopNumTimes = newmap[1]
			self.SwitchAnimatedMap(bLooping, iLoopNumTimes, dTrack)
		elif type(newmap) == types.DictionaryType:# Animation packed as a dictionary
			if newmap.has_key("dTrack"):
				self.SwitchAnimatedMap(newmap.get("bLooping", 0), newmap.get("iLoopNumTimes", -1), newmap["dTrack"])
			else:
				self.SwitchAnimatedMap(0, -1, newmap)
		elif type(newmap) == types.StringType:# Normal texture swap
			self.InternalSwitchMap(newmap)
		else:
			print "Faulty map action for:", self.name, '@', self.object, newmap

	def StopAnimation(self):
		debug(__name__ + ", StopAnimation")
		if self.bInSequence:
			self.bInSequence = 0
			if self.pSequence and self.pSequence.IsPlaying():
				self.pSequence.Abort()
			self.pSequence = None
			return 1
		return 0

	def SwitchAnimatedMap(self, bLooping, iLoopNumTimes, dTrack):
		debug(__name__ + ", SwitchAnimatedMap")
		global oBridgeInfo, oConfigModule

		if not(oBridgeInfo and oConfigModule) or oConfigModule.get("Disable Animated Maps", 0):
			return

		lItems = dTrack.items()
		lItems.sort()

		self.pSequence = App.TGSequence_Create()

		if bLooping or iLoopNumTimes == -1:
			iLoopNumTimes = 1

		for i in range(iLoopNumTimes):
			fTiming = 0.0
			for index, map in lItems:
				self.pSequence.AppendAction(ImmersionMethodScriptAction_Create(self, "InternalSwitchMap", map), index-fTiming)
				fTiming = index

		self.pSequence.AppendAction(ImmersionMethodScriptAction_Create(self, "FinalSequenceAction"))
		if bLooping:
			self.pSequence.AppendAction(ImmersionMethodScriptAction_Create(self, "SwitchAnimatedMap", bLooping, iLoopNumTimes, dTrack))

		self.pSequence.Play()
		self.bInSequence = 1

	def InternalSwitchMap(self, newmap):
		debug(__name__ + ", InternalSwitchMap")
		if self.CurrentMap == newmap:
			return
		pBridgeSet = App.g_kSetManager.GetSet("bridge")
		DirectSwitchMapsObject(self.CurrentMap, newmap, pBridgeSet.GetObject(self.object))
		self.CurrentMap = DistillNewMapName(newmap)

	def FinalSequenceAction(self):
		debug(__name__ + ", FinalSequenceAction")
		self.bInSequence = 0
		self.pSequence = None

def DirectSwitchMapsObject(sOldMap, sNewMap, pObject):
	debug(__name__ + ", DirectSwitchMapsObject")
	if pObject:
		pObject.ReplaceTexture(sNewMap, sOldMap)
		pObject.RefreshReplacedTextures()

def DirectSwitchMaps(sOldMap, sNewMap, sObject=None):
	debug(__name__ + ", DirectSwitchMaps")
	lObjects = oBridgeInfo.ExtraObjects.keys()
	#if sObject:
	#	if type(sObjects) == types.ArrayType:
	#		lObjects = sObjects
	#	else:
	#		lObjects = [sObjects]
 
	pBridgeSet = App.g_kSetManager.GetSet("bridge")
	for key in lObjects:
		DirectSwitchMapsObject(pBridgeSet.GetObject(key))
	return

def DistillNewMapName(sPath):
	debug(__name__ + ", DistillNewMapName")
	return string.split(string.split(sPath, "\\")[-1], "/")[-1][:-4]

# The next 2 functions are from Immersion, with thanks from LJ.
# They are used to call methods on objects from TGSequences.
# Slightly modified to recieve variable number of arguments by MLeo

def ImmersionMethodScriptAction_Create(oObject, sMethod, *args):
	debug(__name__ + ", ImmersionMethodScriptAction_Create")
	return apply(App.TGScriptAction_Create, (__name__, "RedirectClassAction", oObject, sMethod,) + args)

def RedirectClassAction(pAction, oObject, sMethod, *args):
	debug(__name__ + ", RedirectClassAction")
	if oObject:
		pyAttr = getattr(oObject, sMethod)
		if pyAttr:
			apply(pyAttr, args)
	return 0

# Per Bridge Loading screen mod integration (old mod of me and Mark, never really saw the daylight :( )
# For the moment use a mutator

PBLMode = Foundation.MutatorDef('Per Bridge Loading screen')

Foundation.OverrideDef.PBLScreen = Foundation.OverrideDef('Per Bridge Loading Screen', 'MissionLib.ShowLoadingText', __name__ + '.ShowLoadingText', dict = { 'modes': [ PBLMode ] } )

# The diffrence between the old mod and this one is that it uses the Bridge Plugin instead of a variable in the bridge file
#   Much shorter and cleaner :P
def ShowLoadingText(pAction):
	debug(__name__ + ", ShowLoadingText")
	global oBridgeInfo
	MissionLib.LookForward(None)
	pViewscreen = MissionLib.GetViewScreen()
	if (pViewscreen):
		if oBridgeInfo != None:
			pViewscreen.SetOffTexture(oBridgeInfo.LoadingScreen)
		else:
			pViewscreen.SetOffTexture("data/Icons/ViewscreenLoading.tga")
		pViewscreen.SetIsOn(0)
		pViewscreen.SetStaticIsOn(0)

	# Add a handler to remove the screen when the mission is done loading
	pGame = App.Game_GetCurrentGame()
	App.g_kEventManager.RemoveBroadcastHandler(App.ET_MISSION_START, pGame, "MissionLib.EndLoadingText")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_MISSION_START, pGame, "MissionLib.EndLoadingText")

	return 0


# At the request of Mark (Ignis) this part here is to ensure that you can't "stack" alerts
# This function is modified from Bridge.XOMenuHandlers
def SetAlertLevel(pObject, pEvent):
	debug(__name__ + ", SetAlertLevel")
	iType = pEvent.GetInt()

	pGame = App.Game_GetCurrentGame()
	pPlayer = App.ShipClass_Cast(pGame.GetPlayer())

	if not App.IsNull(pPlayer):
		iLevel = 0
		if (iType == App.CharacterClass.EST_ALERT_GREEN):
			iLevel = pPlayer.GREEN_ALERT
		if (iType == App.CharacterClass.EST_ALERT_YELLOW):
			iLevel = pPlayer.YELLOW_ALERT
		if (iType == App.CharacterClass.EST_ALERT_RED):
			iLevel = pPlayer.RED_ALERT

		# This is the changed part, if there is an action, skip it and remove it then do the new action
		if (iLevel != pPlayer.GetAlertLevel()):
			if (iType == App.CharacterClass.EST_ALERT_GREEN):
				QueueActionToPlay(App.TGSoundAction_Create("GreenAlertSound"))
			if (iType == App.CharacterClass.EST_ALERT_YELLOW):
				QueueActionToPlay(App.TGSoundAction_Create("YellowAlertSound"))
			if (iType == App.CharacterClass.EST_ALERT_RED):
				QueueActionToPlay(App.TGSoundAction_Create("RedAlertSound"))

			# Set up an event to send to the ship, which will change its
			# alert level.
			pAlertEvent = App.TGIntEvent_Create()
			pAlertEvent.SetSource(pObject)
			pAlertEvent.SetDestination(pPlayer)
			pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
			pAlertEvent.SetInt(iLevel)

			App.g_kEventManager.AddEvent(pAlertEvent)
	pObject.CallNextHandler(pEvent)
	
import Bridge.XOMenuHandlers
Bridge.XOMenuHandlers.SetAlertLevel = SetAlertLevel

# Copied from MissionLib, I need my own "g_idMasterSequenceObj"
# This is slightly modified to abort a running sequence.
# Instead of appending to that one.
g_idMasterSequenceObj=App.NULL_ID
def QueueActionToPlay(pActionToAdd):
	debug(__name__ + ", QueueActionToPlay")
	global g_idMasterSequenceObj

	assert pActionToAdd
	if pActionToAdd is None:
		return

	pPlayingSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(g_idMasterSequenceObj))

	# If the player is none or dying, bail
	pPlayer = MissionLib.GetPlayer()
	if (pPlayer == None) or (pPlayer.IsDying()):
		# Create event to skip action.
		pEvent = App.TGObjPtrEvent_Create()
		pEvent.SetDestination(App.g_kTGActionManager)
		pEvent.SetEventType(App.ET_ACTION_SKIP)
		pEvent.SetObjPtr(pActionToAdd)
		App.g_kEventManager.AddEvent(pEvent)

		if pPlayingSequence:
			# Create event to skip master sequence.
			pEvent = App.TGObjPtrEvent_Create()
			pEvent.SetDestination(App.g_kTGActionManager)
			pEvent.SetEventType(App.ET_ACTION_SKIP)
			pEvent.SetObjPtr(pPlayingSequence)
			App.g_kEventManager.AddEvent(pEvent)

		return

	if pPlayingSequence:
		DeleteQueuedActions()
	pPlayingSequence = App.TGSequence_Create()
	pPlayingSequence.AddAction(pActionToAdd)
	g_idMasterSequenceObj = pPlayingSequence.GetObjID()
	pPlayingSequence.Play()

def DeleteQueuedActions():
	debug(__name__ + ", DeleteQueuedActions")
	pPlayingSequence = App.TGSequence_Cast(App.TGObject_GetTGObjectPtr(g_idMasterSequenceObj))
	if (pPlayingSequence):
		pPlayingSequence.Abort()

# Flickering LCARs, this isn't really my favourite way, but I haven't found a better way yet.
def FlickerLCARs(self, duration):
	debug(__name__ + ", FlickerLCARs")
	import Appc
	Appc.BridgeObjectClass_FlickerLCARs(self, duration)
	global oBridgeInfo, oConfigModule
	if oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable LCARs Flickering", 0):
		return
	if self.GetName() == "bridge":
		if oBridgeInfo.__dict__.has_key("FlickerLCARs"):
			for i in range(duration):
				pSubSequence = App.TGSequence_Create()
				for key, map in oBridgeInfo.FlickerLCARs.items():
					pSubSequence.AddAction(App.TGScriptAction_Create(__name__, "SwitchMapsAction", key, oBridgeInfo.FlickerLCARs[key]))
				pSubSequence.Play()

# Oh well, let's do the others as well
def TurnLCARsOff(self):
	debug(__name__ + ", TurnLCARsOff")
	import Appc
	Appc.BridgeObjectClass_TurnLCARsOff(self)
	global oBridgeInfo, oConfigModule
	if not oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable LCARs Flickering", 0):
		return
	if self.GetName() == "bridge":
		if oBridgeInfo.__dict__.has_key("TurnLCARsOff"):
			for key, map in oBridgeInfo.TurnLCARsOff.items():
				SwitchMaps(key, map)

def TurnLCARsOn(self):
	debug(__name__ + ", TurnLCARsOn")
	import Appc
	Appc.BridgeObjectClass_TurnLCARsOff(self)
	global oBridgeInfo, oConfigModule
	if not oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable LCARs Flickering", 0):
		return
	if self.GetName() == "bridge":
		for key, map in oBridgeInfo.__dict__.get("TurnLCARsOff", {}).items():
			SwitchMaps(key, map)

# Btw, I know of the typo's, but that's TGs fault.
def GoToGreenAllert(self):
	debug(__name__ + ", GoToGreenAllert")
	import Appc
	Appc.BridgeObjectClass_GoToGreenAllert(self)
	global oBridgeInfo, oConfigModule
	if oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable Active LCARs", 0):
		return
	for key, map in oBridgeInfo.__dict__.get("GreenMaps", {}).items():
		SwitchMaps(key, map)

def GoToYellowAllert(self):
	debug(__name__ + ", GoToYellowAllert")
	import Appc
	Appc.BridgeObjectClass_GoToYellowAllert(self)
	global oBridgeInfo, oConfigModule
	if oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable Active LCARs", 0):
		return
	for key, map in oBridgeInfo.__dict__.get("YellowMaps", {}).items():
		SwitchMaps(key, map)

def GoToRedAllert(self):
	debug(__name__ + ", GoToRedAllert")
	import Appc
	Appc.BridgeObjectClass_GoToRedAllert(self)
	global oBridgeInfo, oConfigModule
	if not oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable Active LCARs", 0):
		return
	for key, item in oBridgeInfo.__dict__.get("RedMaps", {}).items():
		SwitchMaps(key, item)
#App.BridgeObjectClass.FlickerLCARs = FlickerLCARs
#App.BridgeObjectClass.TurnLCARsOff = TurnLCARsOff
#App.BridgeObjectClass.TurnLCARsOn = TurnLCARsOn
App.BridgeObjectClass.GoToGreenAllert = GoToGreenAllert
App.BridgeObjectClass.GoToYellowAllert = GoToYellowAllert
App.BridgeObjectClass.GoToRedAllert = GoToRedAllert


# Special SwitchMaps for actions
def SwitchMapsAction(pAction, sOldMap, sNewMap):
	debug(__name__ + ", SwitchMapsAction")
	SwitchMaps(sOldMap, sNewMap)
	return 0

# (NIF) Animation related functions
def HandleTypeBasedAnimation(sType, oBridgeInfo, bFullName = 0):

	debug(__name__ + ", HandleTypeBasedAnimation")
	global oConfigModule# oBridgeInfo, see parameters
	if oBridgeInfo == None or oConfigModule == None:
		return
	if oConfigModule.get("Disable Animations", 0):
		return

	if not bFullName:
		sType = sType + "Animations"

	if oBridgeInfo.__dict__.has_key("Animations") and oBridgeInfo.Animations.has_key(sType):
		kAM = App.g_kAnimationManager
		for object, dAnimations in oBridgeInfo.Animations[sType].items():
			pBridgeSet = App.g_kSetManager.GetSet("bridge")
			pAniObject = pBridgeSet.GetObject(object)
			if not pAniObject: continue

			pAnimNode = pAniObject.GetAnimNode()

			if not oBridgeInfo.Animations.has_key("AnimationInfo"):
				oBridgeInfo.Animations["AnimationInfo"] = {}

			dAniInfo = oBridgeInfo.Animations["AnimationInfo"]

			for ani in dAnimations:
				iParam1 = 0
				iParam2 = 0
				iParam3 = 1

				if type(ani) != types.DictionaryType:
					ani = {"ani": ani}

				sAnimation = ani["ani"]

				key = sType + "::" + object + "::" + sAnimation + " played"
				if ani.has_key("Requirement") and not ani["Requirement"](dAniInfo, key):
					continue

				exec(ani.get("Custom", ""))

				if type(sAnimation) == types.ArrayType:
					sAnimation = ani[0]
					if len(ani) > 1:
						iParam1 = ani[1]
					if len(ani) > 2:
						iParam2 = ani[2]
					if len(ani) > 3:
						iParam3 = ani[3]
				pAction = App.TGAnimAction_Create(pAnimNode, sAnimation, iParam1, iParam2, iParam3)
				pAction.Play()

				dAniInfo[key] = dAniInfo.get(key, 0) + 1



