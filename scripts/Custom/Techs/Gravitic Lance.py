#################################################################################################################
#         GraviticLance by Alex SL Gato
#         Version 1.51
#         19th October 2024
#         Based on FiveSecsGodPhaser by USS Frontier, scripts/ftb/Tech/TachyonProjectile by the FoundationTechnologies team, and scripts/ftb/Tech/FedAblativeArmour by the FoundationTechnologies team
#                          
#################################################################################################################
# Little simple tech. Any ships with phasers and equipped with this will have a nasty weapon at their disposal.
# With this equipped, any special beam of the ship that hit their target for 5 seconds, or a custom time, continuously, will make their shields drop.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
# Time: seconds needed for the tachyon beam to drop the shields must be above 0. Value is 0.25 by default
# TimeEffect: how many seconds does the power keep getting drained. Must be above 0. 5 by default
# RadDepletionStrength: how much power is drained or gained per 100 ms. 100 by default.
# Beams: this field indicates which beams on your ship have tachyon beam properties. Don't add the field or leave it empty to consider all phasers tachyon beams
# Immune: Immune makes this ship immune to its effects. Set it to greater or lesser than 0 to be immune! negatives also make it immune without the weapon, while 1 keeps it active
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"GraviticLance": { "Time": 5.0, "TimeEffect": 5.0, "RadDepletionStrength": 500, "Beams": ["PhaserNsme1", "PhaserName2", "PhaserName3", "PhaserName4"], "Immune": 1}
}
"""
# As for immunities, there is another way, legacy from 0.9 and before, directly through the Custom script, so you'll have to add these at the end of the scripts/ships script:
"""
def IsGraviticLanceImmune():
	return 1
"""
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.51",
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
  "AsuranSatellite",
  "B5LordShip",
  "B5TriadTriumviron",
  "Battlecrab",
  "BattleTardis",
  "BattleTardisChamaleon",
  "CA8472",
  "CorsairTardis",
  "CorsairTardisChamaleon",
  "crossfield31",
  "DalekEmperorSaucer",
  "DalekGenesisArk",
  "DalekSaucer",
  "DalekSaucerShielded",
  "DalekVoidShip",
  "EAOmegaX",
  "EAShadow_Hybrid",
  "Firebird",
  "HaririrHatak",
  "janeway",
  "kirk",
  "MindridersThoughtforce",
  "PlanetExpress",
  "saturn",
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
  "Supergate",
  "SuperHiveShip",
  "Tardis",
  "TardisType89",
  "TardisType89Chamaleon",
  "TorvalusDarkKnife",
  "vger",
  "VOR_Destroyer",
  "VOR_DestroyerClosed",
  "VOR_Fighter",
  "VOR_FighterOpen",
  "VulcanXRT55D",
  "Wells",
  "Windrunner",
  "XOverAlteranWarship",
  "XOverAncientCityFed",
  "XOverAncientSatelliteFed",
  )

class GraviticLance(FoundationTech.TechDef):
	def __init__(self, name):
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_STARTED_HITTING, self.pEventHandler, "PhaserStartedHitting")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_STOPPED_HITTING, self.pEventHandler, "PhaserStoppedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PHASER_STARTED_HITTING, self.pEventHandler, "PhaserStartedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PHASER_STOPPED_HITTING, self.pEventHandler, "PhaserStoppedHitting")
		#print "Initialized GraviticLance"

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__['GraviticLance']
		else:
			pass
			#print "GraviticLance Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
		pInstance.lTechs.append(self)
		#print "EJGL: attached to ship:", pShip.GetName()
	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__['GraviticLance']
		else:
			#print "GraviticLance Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.remove(self)
		#print "EJGL: detached from ship:", pShip.GetName()


	def PhaserStartedHitting(self, pEvent):
		pPhaser = App.Weapon_Cast(pEvent.GetSource())
		#print "EJGL: phasers started hitting"
		if pPhaser == None:
			#print "EJGL: cancelling... no phaser weapon"
			return
		pShip = pPhaser.GetParentShip()
		try:
			pInstance = FoundationTech.dShips[pShip.GetName()]
			if pInstance == None:
				#print "EJGL: cancelling, no FTech Ship Instance obj"
				return
		except:
			#print "EJGL: cancelling, error in try found..."
			return

		if not pInstance.__dict__.has_key("GraviticLance"):
			#print "EJGL: cancelling, ship does not have EJGL equipped..."
			return

		if pInstance.__dict__['GraviticLance'].has_key("Immune") and pInstance.__dict__['GraviticLance']["Immune"] < 0:
			#print "EJGL: cancelling, ship is immune but NOT meant to have EJGL equipped..."
			return
		
		if pInstance.__dict__['GraviticLance'].has_key("Beams") and len(pInstance.__dict__['GraviticLance']["Beams"]) > 0:
			#print "EJGL: I have beams key, verifying the phaser is among them"
			lBeamNames = pInstance.__dict__['GraviticLance']["Beams"]		

			if not pPhaser.GetName() in lBeamNames:
				#print "EJGL: cancelling, ship has EJGL equipped but not for that phaser..."
				return
		#else:
		#	print "EJGL: I do not have beams key, I will assume all phasers have gravitic lance ability"

		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		if pTarget == None:
			#print "EJGL: cancelling, no target..."
			return
		sTargetName = pTarget.GetName()
		#print "EJGL: Mark 1, Target is:", sTargetName
		if not pInstance.__dict__['GraviticLance'].has_key(sTargetName):
			pInstance.__dict__['GraviticLance'][sTargetName] = {"HittingNames": [], "Target": pTarget}

			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			eType = App.Mission_GetNextEventType()
			App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "HandlePowerDrop")
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(eType)
			pEvent.SetDestination(pMission)
			pEvent.SetString(pShip.GetName()+">|<"+sTargetName)
			pTimer = App.TGTimer_Create()
			if not pInstance.__dict__['GraviticLance'].has_key("Time") or pInstance.__dict__['GraviticLance']["Time"] <= 0.0:
				pInstance.__dict__['GraviticLance']["Time"] = 0.25
			pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime()+pInstance.__dict__['GraviticLance']["Time"] )
			pTimer.SetDelay(0)
			pTimer.SetDuration(0)
			pTimer.SetEvent(pEvent)
			App.g_kTimerManager.AddTimer(pTimer)

			pInstance.__dict__['GraviticLance'][sTargetName]['Timer'] = pTimer
			#print "EJGL: first time hitting target, setting up data."

		#however we still need to store their names so that the events are properly handled
		if not pPhaser.GetName() in pInstance.__dict__['GraviticLance'][sTargetName]['HittingNames']:
			pInstance.__dict__['GraviticLance'][sTargetName]['HittingNames'].append( pPhaser.GetName() )
			#print "EJGL: adding phaser", pPhaser.GetName(), "to Target hitting list."
	def PhaserStoppedHitting(self, pEvent):
		pPhaser = App.Weapon_Cast(pEvent.GetSource())
		if pPhaser == None:
			#print "EJGL (Stop): cancelling, no phaser..."
			return
		pShip = pPhaser.GetParentShip()
		try:
			pInstance = FoundationTech.dShips[pShip.GetName()]
			if pInstance == None:
				#print "EJGL (Stop): cancelling, no FTech Ship Instance obj"
				return
		except:
			#print "EJGL (Stop): cancelling, error in try found."
			return
		if not pInstance.__dict__.has_key("GraviticLance"):
			#print "EJGL (Stop): ship does not have EJGL equipped."
			return

		if pInstance.__dict__['GraviticLance'].has_key("Immune") and pInstance.__dict__['GraviticLance']["Immune"] < 0:
			#print "EJGL: cancelling, ship is immune but NOT meant to have EJGL equipped..."
			return
	
		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		if pTarget == None:
			#print "EJGL (Stop): cancelling, no target"
			return
		sTargetName = pTarget.GetName()
		#print "EJGL (Stop): Mark 1, target is:", sTargetName
		if not pInstance.__dict__['GraviticLance'].has_key(sTargetName):
			# if: ship was just destroyed by this phaser fire, thus her entry deleted from our data dict,
			# but phaser was still hitting her and stopped after the destruction. So we simply return here...
			return
		if pPhaser.GetName() in pInstance.__dict__['GraviticLance'][sTargetName]['HittingNames']:
			pInstance.__dict__['GraviticLance'][sTargetName]['HittingNames'].remove( pPhaser.GetName() )
			#print "EJGL (Stop): removing phaser", pPhaser.GetName(), "from target hitting list."

		if len(pInstance.__dict__['GraviticLance'][sTargetName]['HittingNames']) <= 0:
			#instance-secs hitting sequence aborted... cancel it.
			App.g_kTimerManager.DeleteTimer(pInstance.__dict__['GraviticLance'][sTargetName]['Timer'].GetObjID())
			pInstance.__dict__['GraviticLance'][sTargetName]['Timer'] = None
			del pInstance.__dict__['GraviticLance'][sTargetName]
			#print "EJGL (Stop): instance-sec hitting sequence aborted..."

	def HandlePowerDrop(self, pEvent):
		sMasterStr = pEvent.GetCString()
		lStrs = string.split(sMasterStr, ">|<")
		sShipName = lStrs[0]
		sTargetName = lStrs[1]
		#print "EJGL (HIK): Handle Power Drop called..."
		#print "EJGL (HIK): Ship:", sShipName, " ||Target:", sTargetName
		try:
			pInstance = FoundationTech.dShips[sShipName]
			if pInstance == None:
				#print "EJGL (HIK): cancelling, no FTech Ship Instance obj"
				return
		except:
			#print "EJGL (HIK): cancelling, error at try found..."
			return
		if not pInstance.__dict__.has_key("GraviticLance"):
			#print "EJGL (HIK): cancelling, ship is not equipped with EJGL..."
			return

		if pInstance.__dict__['GraviticLance'].has_key("Immune") and pInstance.__dict__['GraviticLance']["Immune"] < 0:
			#print "EJGL: cancelling, ship is immune but NOT meant to have EJGL equipped..."
			return

		if pInstance.__dict__['GraviticLance'].has_key(sTargetName):
			#okydokey, we did it. Drain the target energy, then delete our data about it.
			pTarget = pInstance.__dict__['GraviticLance'][sTargetName]['Target']

			self.TheYield(pTarget, pInstance, pEvent)

			App.g_kTimerManager.DeleteTimer(pInstance.__dict__['GraviticLance'][sTargetName]['Timer'].GetObjID())
			pInstance.__dict__['GraviticLance'][sTargetName]['Timer'] = None
			del pInstance.__dict__['GraviticLance'][sTargetName]
			#print "EJGL (HIK): instance-sec hitting sequence completed, draining target power."

	def IsDrainYield(self): # Added this in case someone ever makes a Breen Drainer Beam and doesn't code it properly, so this tech doesn't crash
		return 0

	def IsPhaseYield(self):# Added this in case someone ever makes an Anti-proton burst Beam and doesn't code it properly, so this tech doesn't crash
		return 0

	def TheYield(self, pShip, pInstance, pEvent):
		global lImmuneShips

		sScript     = pShip.GetScript()
		sShipScript = string.split(sScript, ".")[-1]

		pShipModule =__import__(sScript)
		pShields = pShip.GetShields()
		if sShipScript in lImmuneShips:
			return

		pShipInst = None
		vibechecker = 1
		try: 
			pShipInst = FoundationTech.dShips[pShip.GetName()]
			if pShipInst == None:
				#print "After looking, no instance for Ship:", pShip.GetName(), "How odd..."
				vibechecker = 0
		except:
			#print "Error, so no instance for Ship:", pShip.GetName(), "How odd..."
			vibechecker = 0
		if vibechecker == 1 and pShipInst.__dict__.has_key('GraviticLance') and pShipInst.__dict__['GraviticLance'].has_key("Immune") and not pShipInst.__dict__['GraviticLance']["Immune"] == 0:
			return


		if not pInstance.__dict__['GraviticLance'].has_key("RadDepletionStrength"):
			pInstance.__dict__['GraviticLance']["RadDepletionStrength"] = 100.0 # energy
		iPower = pInstance.__dict__['GraviticLance']["RadDepletionStrength"]

		pSeq = App.TGSequence_Create()
		#print "depleting energy"

		if not pInstance.__dict__['GraviticLance'].has_key("TimeEffect") or pInstance.__dict__['GraviticLance']["TimeEffect"] <= 0.0:
			pInstance.__dict__['GraviticLance']["TimeEffect"] = 5.0 # seconds
		iTime = pInstance.__dict__['GraviticLance']["TimeEffect"]
		while(iTime >= 0):
			pAction	= App.TGScriptAction_Create(__name__, "Update", self, pShip.GetObjID(), iPower)
			pSeq.AppendAction(pAction, 0.1)
			iTime = iTime - 0.1
		pAction	= App.TGScriptAction_Create(__name__, "Update", self, pShip.GetObjID(), iPower)
		pSeq.AppendAction(pAction, 0.1)
		pSeq.Play()

	def GetShip(self, shipID):
		return App.ShipClass_GetObjectByID(None, shipID)

	def GetPower(self, shipID):
		pShip = self.GetShip(shipID)
		if pShip:
			return pShip.GetPowerSubsystem()

def Update(pAction, self, shipID, iPower):
	pPowerSubsystem = self.GetPower(shipID)
	if pPowerSubsystem:
		if iPower <= 0:
			pPowerSubsystem.AddPower(-iPower)
		else:
			pPowerSubsystem.StealPower(iPower)
	return 0
		
oGraviticLance = GraviticLance("GraviticLance")