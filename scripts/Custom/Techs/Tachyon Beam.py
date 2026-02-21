#################################################################################################################
#         TachyonBeam by Alex SL Gato
#         21st February 2026
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team
#                          
#################################################################################################################
# Little simple tech. Any ships with phasers and equipped with this will have a nasty weapon at their disposal.
# With this equipped, any special beam of the ship that hit their target for 5 seconds, or a custom time, continuously, will make their shields drop.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Time: seconds needed for the tachyon beam to drop the shields must be above 0. 5 by default
# TimeEffect: how many seconsd do the shields remain dropped. Must be above 0. 5 by default
# Beams: this field indicates which beams on your ship have tachyon beam properties. Don't add the field or leave it empty to consider all phasers tachyon beams
# Immune: NEW!!! Finally found how to add the immunity to another side of the party! Immune makes this ship immune to its effects. Set it to greater or lesser than 0 to be immune! negatives also make it immune without the weapon, while 1 keeps it active
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"TachyonBeam": { "Time": 5.0, "TimeEffect": 5.0, "Beams": ["PhaserNsme1", "PhaserName2", "PhaserName3", "PhaserName4"], "Immune": 1}
}
"""
# As for immunities, there is another way, elgacy from 1.0 and before, directly through the Custom script, so you'll have to add these at the end of the scripts/ships script:
"""
def IsTachyonImmune():
	return 1
"""
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.43",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
import App
import FoundationTech
from ftb.Tech.ATPFunctions import *

import MissionLib
from ftb.Tech.DisablerYields import *

import time
import string

import traceback

global lImmuneShips # A list meant only for backwards compatibility - do NOT edit
lImmuneShips = (
  "ActiveSupergate",
  "AncientCity",
  "AncientCruiser",
  "AncientSatellite",
  "AncientWarship",
  "AnArchlike",
  "Andromeda",
  "AndromedaBattleForm",
  "AndSlipFighter",
  "AndSlipFighterMK1",
  "AndSlipFighterMK2",
  "AndSlipFighterMK3",
  "AnubisFlagship",
  "ArmoredVoyager",
  "AshenShuumtian",
  "AsuranSatellite",
  "Atlantis",
  "B5LordShip",
  "B5PsiCorpMothership",
  "B5SoulHunterVessel",
  "B5Station",
  "B5TechnomageTransport",
  "B5TechnomageTransportIllusion",
  "B5TriadTriumviron",
  "Battlecrab",
  "Battlestar",
  "BattleTardis",
  "BattleTardisChamaleon",
  "bcnarada",
  "Beliskner",
  "BelisknerRefit",
  "bluestar",
  "BorgCube",
  "BorgDiamond",
  "borgshuttle",
  "BrakiriCruiser",
  "CA8472",
  "ClosedJumper",
  "CorsairTardis",
  "CorsairTardisChamaleon",
  "crossfield31",
  "CubeA",
  "CubeB",
  "CubeC",
  "CubeD",
  "CubeE",
  "CubeF",
  "CubeG",
  "CubeH",
  "CylonBasestar",
  "CylonRaider",
  "Daedalus",
  "DalekCaan",
  "DalekEmperorSaucer",
  "DalekGenesisArk",
  "DalekJast",
  "DalekNewParadigmEternal",
  "DalekSaucer",
  "DalekSaucerShielded",
  "DalekSec",
  "DalekVoidShip",
  "DamagedWarship"
  "DanielJackson",
  "DRA_Carrier",
  "DRA_Cruiser",
  "DRA_Raider",
  "DRA_Shuttle",
  "DraziSkySerpent",
  "DraziSunHawk",
  "DraziSunHawkWithSerpent",
  "DS9FXBorgCube",
  "DS9FXBorgDetector",
  "DS9FXBorgSphere",
  "DS9FXBorgTacticalCube",
  "DSC304Apollo",
  "DSC304Daedalus",
  "DSC304Korolev",
  "DSC304Odyssey",
  "DSC304OdysseyRefit",
  "DSC304OdysseyUpgrade",
  "EAAsimov",
  "EAExplorer",
  "EAForceOne",
  "EAOmega",
  "EAOmegaX",
  "EAShadow_Hybrid",
  "EAStealthStarfury",
  "EIntrepid",
  "Firebird",
  "GalaticaBS75",
  "GQuan",
  "HadesBasestar",
  "HalcyonPromise",
  "HaririrHatak",
  "janeway",
  "kirk",
  "Korolev",
  "LowCube",
  "MidwayStation",
  "MillionVoices",
  "MinbariNial",
  "B5MinbariSharlin",
  "MinbariSharlin",
  "MindridersThoughtforce",
  "MvamFusionCube",
  "Odyssey",
  "OdysseyRefit",
  "OdysseyUpgrade",
  "ONeill",
  "OriFighter",
  "OriSatellite",
  "OriWarship",
  "PaxMagellanic",
  "PlanetExpress",
  "Primus",
  "PrometheusRefit",
  "PrometheusUpgrade",
  "Protector",
  "PuddleJumper",
  "ReplicatorBeliskner",
  "ReplicatorHatak",
  "ReplicatorVessel",
  "ReplicatorWarship",
  "saturn",
  "SentriFighter",
  "Shadow_Fighter",
  "Shadow_Fighter1",
  "Shadow_Fighter2",
  "Shadow_Fighter3",
  "Shadow_Fighter4",
  "Shadow_Fighter5",
  "Shadow_Fighter6",
  "Shadow_Fighter7",
  "Shadow_FighterBall",
  "Shadow_Scout",
  "SigmaWalkerScienceLab",
  "sphere",
  "Spider",
  "Supergate",
  "SuperHiveShip",
  "Superweapon",
  "Tardis",
  "TardisType89",
  "TardisType89Chamaleon",
  "TENeptune",
  "ThNor",
  "TorvalusDarkKnife",
  "TOSColDefender",
  "UENeptune",
  "vger",
  "B5Victory",
  "Victory",
  "VOR_Destroyer",
  "VOR_DestroyerClosed",
  "VOR_Fighter",
  "VOR_FighterOpen",
  "Vorchan",
  "VreeXill",
  "VreeXorr",
  "VulcanXRT55D",
  "B5Warlock",
  "Warlock",
  "WCnx01",
  "WCnxColumbia",
  "WCnxmirror",
  "WCnxmirroravenger",
  "Wells",
  "whitestar",
  "Whitestar",
  "Windrunner",
  "X303",
  "x303",
  "X303Refit",
  "X303Upgrade",
  "XCV330a",
  "XCV330o",
  "XInsect",
  "XOverAlteranWarship",
  "XOverAncientCityFed",
  "XOverAncientSatelliteFed",
  )

class TachyonBeam(FoundationTech.TechDef):
	def __init__(self, name):
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_STARTED_HITTING, self.pEventHandler, "PhaserStartedHitting")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_STOPPED_HITTING, self.pEventHandler, "PhaserStoppedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PHASER_STARTED_HITTING, self.pEventHandler, "PhaserStartedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PHASER_STOPPED_HITTING, self.pEventHandler, "PhaserStoppedHitting")
		#print "Initialized TachyonBeam"

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__[self.name]
		else:
			pass
			#print "TachyonBeam Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
		pInstance.lTechs.append(self)
		#print "FSTB: attached to ship:", pShip.GetName()
	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__[self.name]
		else:
			#print "TachyonBeam Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.remove(self)
		#print "FSTB: detached from ship:", pShip.GetName()


	def PhaserStartedHitting(self, pEvent):
		pPhaser = App.Weapon_Cast(pEvent.GetSource())
		#print __name__, ": phasers started hitting"
		if pPhaser == None or not hasattr(pPhaser, "GetParentShip"):
			#print __name__, " (Start): cancelling... no phaser weapon"
			return
		pShip = pPhaser.GetParentShip()
		if not pShip or not hasattr(pShip, "GetObjID"):
			return

		iShipID = pShip.GetObjID()
		if iShipID is None or iShipID == App.NULL_ID:
			return

		pShip = GetWellShipFromID(iShipID)
		if not pShip:
			return

		pInstance = findShipInstance(pShip)
		if not pInstance:
			#print __name__, ": (Start) cancelling, no FTech Ship Instance obj"
			return

		if not pInstance.__dict__.has_key(self.name):
			#print __name__, " (Start): cancelling, ship does not have FSTB equipped..."
			return

		if pInstance.__dict__[self.name].has_key("Immune") and pInstance.__dict__[self.name]["Immune"] < 0:
			#print __name__, " (Start): cancelling, ship is immune but NOT meant to have FSTB equipped..."
			return
		
		if pInstance.__dict__[self.name].has_key("Beams") and len(pInstance.__dict__[self.name]["Beams"]) > 0:
			#print __name__, " (Start): I have beams key, verifying the phaser is among them"
			lBeamNames = pInstance.__dict__[self.name]["Beams"]		

			if not pPhaser.GetName() in lBeamNames:
				#print __name__, " (Start): cancelling, ship has FSTB equipped but not for that phaser..."
				return
		#else:
		#	print "FSTB: I do not have beams key, I will assume all phasers have tachyon ability"

		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		if pTarget == None or not hasattr(pTarget, "GetObjID"):
			#print __name__, " (Start): cancelling, no target..."
			return

		iTargetID = pTarget.GetObjID()
		if iTargetID is None or iTargetID == App.NULL_ID:
			#print __name__, " (Start): cancelling, no target ID..."
			return

		pTarget = GetWellShipFromID(iTargetID)
		if not pTarget:
			return

		sTargetName = pTarget.GetName()
		sPhaserName = pPhaser.GetName()
		#print "FSTB: Mark 1, Target is:", sTargetName
		if not pInstance.__dict__[self.name].has_key(sTargetName):
			pInstance.__dict__[self.name][sTargetName] = {"HittingNames": [], "Target": pTarget}

			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			eType = App.Mission_GetNextEventType()
			App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "HandleShieldDrop")
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(eType)
			pEvent.SetDestination(pMission)
			pEvent.SetString(pShip.GetName()+">|<"+sTargetName)

			pTimer = App.TGTimer_Create()
			if not pInstance.__dict__[self.name].has_key("Time") or pInstance.__dict__[self.name]["Time"] <= 0.0:
				pInstance.__dict__[self.name]["Time"] = 5.0

			pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime()+pInstance.__dict__[self.name]["Time"] )
			pTimer.SetDelay(0)
			pTimer.SetDuration(0)
			pTimer.SetEvent(pEvent)
			App.g_kTimerManager.AddTimer(pTimer)

			pInstance.__dict__[self.name][sTargetName]['Timer'] = pTimer
			#print __name__, " (Start): first time hitting target, setting up data."

		#however we still need to store their names so that the events are properly handled
		if not sPhaserName in pInstance.__dict__[self.name][sTargetName]['HittingNames']:
			pInstance.__dict__[self.name][sTargetName]['HittingNames'].append( sPhaserName )
			#print __name__, " (Start): adding phaser", sPhaserName, "to Target hitting list."

	def PhaserStoppedHitting(self, pEvent):
		pPhaser = App.Weapon_Cast(pEvent.GetSource())
		#print __name__, ": phasers stopped hitting"
		if pPhaser == None or not hasattr(pPhaser, "GetParentShip"):
			#print __name__, " (Stop): cancelling... no phaser weapon"
			return
		pShip = pPhaser.GetParentShip()
		if not pShip or not hasattr(pShip, "GetObjID"):
			return

		iShipID = pShip.GetObjID()
		if iShipID is None or iShipID == App.NULL_ID:
			return

		pShip = GetWellShipFromID(iShipID, ignoreDying=1)
		if not pShip:
			return

		pInstance = findShipInstance(pShip)
		if not pInstance:
			#print __name__, " (Stop): cancelling, no FTech Ship Instance obj"
			return

		if not pInstance.__dict__.has_key(self.name):
			#print __name__, " (Stop): ship does not have FSTB equipped."
			return

		if pInstance.__dict__[self.name].has_key("Immune") and pInstance.__dict__[self.name]["Immune"] < 0:
			#print __name__, " (Stop): cancelling, ship is immune but NOT meant to have FSTB equipped..."
			return

		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		if pTarget == None or not hasattr(pTarget, "GetObjID"):
			#print __name__, " (Stop): cancelling, no target..."
			return

		iTargetID = pTarget.GetObjID()
		if iTargetID is None or iTargetID == App.NULL_ID:
			#print __name__, " (Stop): cancelling, no target ID..."
			return

		pTarget = GetWellShipFromID(iTargetID, ignoreDying=1)
		if not pTarget:
			return

		sTargetName = pTarget.GetName()
		sPhaserName = pPhaser.GetName()
		#print "FSTB (Stop): Mark 1, target is:", sTargetName
		if not pInstance.__dict__[self.name].has_key(sTargetName):
			#most likely scenario, and hopefully the only one, for this if:  ship was just destroyed by this phaser fire, thus her entry deleted
			#from our data dict, but phaser was still hitting her and stopped after the destruction. So we simply return here...
			return

		if sPhaserName in pInstance.__dict__[self.name][sTargetName]['HittingNames']:
			pInstance.__dict__[self.name][sTargetName]['HittingNames'].remove( sPhaserName )
			#print __name__, " (Stop): removing phaser", sPhaserName, "from target hitting list."

		if len(pInstance.__dict__[self.name][sTargetName]['HittingNames']) <= 0:
			#instance-secs hitting sequence aborted... cancel it.
			if pInstance.__dict__[self.name][sTargetName].has_key('Timer'):
				if hasattr(pInstance.__dict__[self.name][sTargetName]['Timer'], "GetObjID"):
					App.g_kTimerManager.DeleteTimer(pInstance.__dict__[self.name][sTargetName]['Timer'].GetObjID())
				pInstance.__dict__[self.name][sTargetName]['Timer'] = None

			del pInstance.__dict__[self.name][sTargetName]
			#print "FSTB (Stop): instance-sec hitting sequence aborted..."

	def HandleShieldDrop(self, pEvent):
		sMasterStr = pEvent.GetCString()
		lStrs = string.split(sMasterStr, ">|<")
		sShipName = lStrs[0]
		sTargetName = lStrs[1]
		#print "FSTB (HSD): Handle Shield Drop called..."
		#print "FSTB (HSD): Ship:", sShipName, " ||Target:", sTargetName

		pInstance = findShipInstance(None, sShipName)
		if not pInstance:
			#print __name__, " (HSD): cancelling, no FTech Ship Instance obj"
			return

		if not pInstance.__dict__.has_key(self.name):
			#print __name__, " (HSD): cancelling, ship is not equipped with FSTB..."
			return

		if pInstance.__dict__[self.name].has_key("Immune") and pInstance.__dict__[self.name]["Immune"] < 0:
			#print __name__, " (HSD): cancelling, ship is immune but NOT meant to have FSTB equipped..."
			return

		if pInstance.__dict__[self.name].has_key(sTargetName):
			#okydokey, we did it. Drop the target shields. then delete our data about it.
			pTarget = None
			iHaveTarget = (pInstance.__dict__[self.name][sTargetName].has_key('Target'))
			if iHaveTarget:
				pTarget = pInstance.__dict__[self.name][sTargetName]['Target']
			forgetIt = 1
			if pTarget:
				iTargetID = pTarget.GetObjID()
				if iTargetID != None and iTargetID != App.NULL_ID:
					pTarget = GetWellShipFromID(iTargetID)
					if pTarget:
						forgetIt = 0
						self.TheYield(pTarget, pInstance, pEvent)

			if pInstance.__dict__[self.name][sTargetName].has_key('Timer'):
				if hasattr(pInstance.__dict__[self.name][sTargetName]['Timer'], "GetObjID"):
					App.g_kTimerManager.DeleteTimer(pInstance.__dict__[self.name][sTargetName]['Timer'].GetObjID())
				pInstance.__dict__[self.name][sTargetName]['Timer'] = None

			if iHaveTarget:
				del pInstance.__dict__[self.name][sTargetName]['Target']
			del pInstance.__dict__[self.name][sTargetName]

			#print __name__, " (HSD): instance-sec hitting sequence completed, dropping target shields."

	def IsDrainYield(self): # Added this in case someone ever makes a Breen Drainer Beam and doesn't code it properly, so this tech doesn't crash
		return 1

	def IsPhaseYield(self):# Added this in case someone ever makes an Anti-proton burst Beam and doesn't code it properly, so this tech doesn't crash
		return 0

	def TheYield(self, pShip, pInstance, pEvent):
		global lImmuneShips

		sScript     = pShip.GetScript()
		sShipScript = string.split(sScript, ".")[-1]
		if sShipScript in lImmuneShips:
			return

		pShipModule = None
		try:
			pShipModule =__import__(sScript)
		except:
			pShipModule = None
			traceback.print_exc()

		if not pShipModule:
			return
		
		pShields = pShip.GetShields()
		if (hasattr(pShipModule, "IsTachyonImmune") and (pShipModule.IsTachyonImmune() == 1) and pShields) or sShipScript in lImmuneShips:
			return

		pShipInst = None
		vibechecker = 1

		pShipInst = findShipInstance(pShip)
		if pShipInst == None:
			vibechecker =0

		if vibechecker == 1 and pShipInst.__dict__.has_key(self.name) and pShipInst.__dict__[self.name].has_key("Immune") and not pShipInst.__dict__[self.name]["Immune"] == 0:
			return

		pPlayer = MissionLib.GetPlayer()
		pBridge = App.g_kSetManager.GetSet("bridge")

		if pPlayer and pPlayer.GetObjID() == pShip.GetObjID() and pBridge:
			pEngineer = App.CharacterClass_GetObject(pBridge, "Engineer")
			pDatabase = pEngineer.GetDatabase()
			# only play when shields are online
			if self.GetShieldStatus(pShip.GetObjID()):
				pSequence = App.TGSequence_Create()
				pSequence.AppendAction(App.CharacterAction_Create(pEngineer, App.CharacterAction.AT_SPEAK_LINE, "ShieldsFailed", None, 0, pDatabase, App.CSP_SPONTANEOUS))
				pSequence.Play()
                        
		if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
			pSeq = App.TGSequence_Create()
			if not pInstance.__dict__[self.name].has_key("TimeEffect") or pInstance.__dict__[self.name]["TimeEffect"] <= 0.0:
				pInstance.__dict__[self.name]["TimeEffect"] = 5.0 # seconds
			iTime = pInstance.__dict__[self.name]["TimeEffect"]
			while(iTime >= 0):
				pAction	= App.TGScriptAction_Create(__name__, "Update", self, 0, pShip.GetObjID())
				pSeq.AppendAction(pAction, 0.1)
				iTime = iTime - 0.1
			pAction	= App.TGScriptAction_Create(__name__, "Update", self, 1, pShip.GetObjID())
			pSeq.AppendAction(pAction, 0.1)
			pSeq.Play()

	def GetShip(self, shipID):
		return App.ShipClass_GetObjectByID(None, shipID)

	def GetShields(self, shipID):
		pShip = GetWellShipFromID(shipID) #self.GetShip(shipID)
		if pShip:
			return pShip.GetShields()

	def GetShieldStatus(self, shipID):
		pShields = self.GetShields(shipID)
		if pShields:
			return pShields.IsOn()

def GetWellShipFromID(pShipID, ignoreDying=0):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip:
		return None

	if ignoreDying == 0 and (pShip.IsDead() or pShip.IsDying()):
		return None

	return pShip

def findShipInstance(pShip, alternateName=None):
	debug(__name__ + ", findShipInstance")
	pInstance = None
	try:
		myName = None
		if alternateName == None:
			if not pShip:
				return pInstance
			myName = pShip.GetName()
		else:
			myName = alternateName
		if FoundationTech.dShips.has_key(myName):
			pInstance = FoundationTech.dShips[myName]
	except:
		pInstance = None
		pass

	return pInstance

def Update(pAction, self, iOnOff, shipID):
	pShields = self.GetShields(shipID)
	if pShields:
		if iOnOff == 0:
			pShields.TurnOff()
		else:
			pShip = self.GetShip(shipID)
			# turn Shields on if we are not green alert
			if pShip.GetAlertLevel() > 0:
				pShields.TurnOn()	
	else:
		return 1
	return 0
		
oTachyonBeam = TachyonBeam("TachyonBeam")