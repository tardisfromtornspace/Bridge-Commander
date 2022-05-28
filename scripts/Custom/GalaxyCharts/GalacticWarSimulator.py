from bcdebug import debug
########################################################################################################################
###   GalacticWarSimulator.py
###                 by Fernando Aluani, aka USS Frontier
#######################
# This script, new in v2.0, introduces what I call "Galactic War Simulator" feature into Galaxy Charts. 
# This galactic war simulator, if online, introduces much more dynamism and action into BC, making that empires have a
# basic economy running, defending their territories and attacking their enemies to conquer their territories, and finally, the galaxy.
# For now it is a pretty basic simulator tho - it won't give the player any rewards like new ships or techs, but it will certainly
# add much needed dynamic action into BC, something we are wanting for ages, and New Frontier, the mod that is probably to give us all that, 
# might take a while to be released. So for now, this fun packed feature should be enough  ;)
########################################################################################################################
import App
import string
import nt
import Foundation
import MissionLib
import math
import time
import Galaxy
import GalaxyMapGUI
import SystemAnalysisGUI
from GalaxyLIB import *
import SavingSystem
import Custom.QBautostart.Libs.Races
import Custom.GravityFX.Logger

NonSerializedObjects = (
"FleetManager",
"WarSimulator",
)

###############################
# CUSTOM EVENTS
####
# While the War Simulator runs entirely on his own, the use of these events may help in the future to add new stuff without directly modifying the file
# or to listen to these events in other places.  ;)
###############################

# War Simulator events:
ET_WAR_SIM_INITIALIZED = App.UtopiaModule_GetNextEventType()     # Destination**: War Simulator
ET_WAR_SIM_UPDATE = App.UtopiaModule_GetNextEventType()          # Destination**: War Simulator
ET_REGION_CONQUERED = App.UtopiaModule_GetNextEventType()        # Destination**: Region Obj         ||  String: name of the race that used to control it.
ET_WAR_SIM_SHIP_ADDED = App.UtopiaModule_GetNextEventType()      # Destination: Ship Object
ET_WAR_SIM_SHIP_DELETED = App.UtopiaModule_GetNextEventType()    # Destination: Ship Object

# Fleet Manager events:
ET_FLEET_CREATED = App.UtopiaModule_GetNextEventType()           # Destination**: War Simulator (non-important)  || String: name of created fleet
ET_FLEET_DELETED = App.UtopiaModule_GetNextEventType()           # Destination**: War Simulator (non-important)  || String: name of created fleet

# Ship Fleet events:
ET_FLEET_SHIP_ADDED = App.UtopiaModule_GetNextEventType()        # Destination: Ship Object          || String: name of fleet the ship entered
ET_FLEET_SHIP_REMOVED = App.UtopiaModule_GetNextEventType()      # Destination: Ship Object          || String: name of fleet the ship was removed from
ET_FLEET_UPDATED_LEAD = App.UtopiaModule_GetNextEventType()      # Destination**: War Simulator (non-important)  || String: name of fleet updated

# WS Ship events:         (Both have the destinations as the ShipClass Obj that called them)
ET_SHIP_SET_ORDER = App.UtopiaModule_GetNextEventType()                     #  Int:  order number
ET_SHIP_SET_ASSIGNED_TO_REGION = App.UtopiaModule_GetNextEventType()        #  String:  name of the old region the ship was assigned to

# Ship events (fired by other, different parts of GC, tho still related to the War Simulator) (Destination in them all = Ship Object)
ET_SHIP_NEEDS_REPAIR_AND_RESUPPLY = App.UtopiaModule_GetNextEventType()  #  (fired by IsShipInNeedOfRepairAndResupply Conditional AI)
ET_SHIP_STARTED_DOCKING = App.UtopiaModule_GetNextEventType()            #  Int:  ship obj ID  (fired by IntelligentShipDocking PlainAI (WarAI module))
ET_SHIP_REPAIRED = App.UtopiaModule_GetNextEventType()                   #  Int:  ship obj ID  (fired by IntelligentShipDocking PlainAI (WarAI module))
ET_SHIP_FINISHED_DOCKING = App.UtopiaModule_GetNextEventType()           #  Int:  ship obj ID  (fired by IntelligentShipDocking PlainAI (WarAI module))

# Region Battle events:   (All 5 have the destination** as the Region Battle Obj that called them)
ET_BATTLE_SHIP_ADDED = App.UtopiaModule_GetNextEventType()         # String:   added ship name
ET_BATTLE_SHIP_REMOVED = App.UtopiaModule_GetNextEventType()       # String:   removed ship name
ET_BATTLE_STARTED = App.UtopiaModule_GetNextEventType()            #
ET_BATTLE_ATTACK_VICTORY = App.UtopiaModule_GetNextEventType()     # String:   name of the race that has been defeated
ET_BATTLE_DEFENCE_VICTORY = App.UtopiaModule_GetNextEventType()    # Float:    amount of funds recovered

# destinations with a '**' besides means that the destination value of those events isn't really the mentioned objs because of some technical difficulties.
# however, the mentioned objs can be acquired by using one of the following functions, localized here in this script, and passing as argument the 
# destination value of the '**' event.
#
# - GetRegionDestination(pDest)
# - GetRegionBattleDestination(pDest)
# - GetWarSimulatorDestination(pDest)   Obs: not very usefull since there's only 1 War Simulator obj created, and it'll be the same always.
#
# - GetRealDestinationObj(pDest)   Obs: this is a master function - it'll try to use one of the above to get your event's destination value.

###############################
# The Main Part 
###############################

# The main class of the galactic war simulator, she's the manager of it all. Handles ship creation/deletion, race economics and tactical decisions, etc.
class WarSimulatorClass:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.CLASS = "Galactic War Simulator"
		self.__ID = GetUniqueID("WarSimulator")
		self.__initialized = 0
		self.dShips = {}            # dict of "name" = WSShip instances
		self.dShipClassesCost = {}  # dict of "ship class name" = ship class cost    (ship class name = ship script)
		self.Refresher = None
		self.pEventHandler = None
		self.BattleEndedSound = None
		self.__createdSB12 = 0
		self.__timeSinceLastBattle = -1.0
		self.__RAFcalled = 0
		self.__playerLeadsAttack = 0
		self.__iCloneNum = 0
		self.__iActiveClones = 0
		self.lNews = []
		self.bIsLoadingGame = 0
		self.iAIResetCounter = 0
		self.sPlayerName = ""
		# dict to store 'stat' variables. These measure some statistics of the game being played, mostly from the player (the player stats).
		self.dStats = {"TotalBattlesOccured": 0, "TotalShipDeaths": 0, "TotalShipsMade": 0, "Deaths": 0, "Kills": 0, "BattlesParticipated": 0,
				   "SystemsDefended": 0, "SystemsConquered": 0, "PlayTime": 0, "RacesDefeated": 0, "TotalFriendlyShipKills": 0, 
				   "TotalFriendlyShipDeaths": 0, "FundsAcquired": 0, "FundsSpent": 0, "TimesSaved": 0, "StarbaseDocks": 0, "NebulasDestroyed": 0,
				   "TimesTraveled": 0}
		# dShipDamages dict should be <target name string, (dict<firing ship name str, damage float>) >
		# this tells us which ships damaged another ship and with how much damage in total, thus we can use this to check which ship most contributed
		# to the death of another ship.
		self.dShipDamages = {}
		self.lastClock = 0 
	def Initialize(self):
		# - do all loading and setting up.
		# start refresh event
		debug(__name__ + ", Initialize")
		if self.Refresher == None:
			self.Refresher = RefreshEventHandler(self.Update, 1.0)
		# start our personal event handler
		if self.pEventHandler == None:
			self.pEventHandler = App.TGPythonInstanceWrapper()
			self.pEventHandler.SetPyWrapper(self)

		# manage our events
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_CREATED, self.pEventHandler, "ObjectCreatedHandler")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_OBJECT_DESTROYED, self.pEventHandler, "ObjectDestroyedHandler")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SET_PLAYER, self.pEventHandler, "PlayerChangedHandler")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PLAYER_DOCKED_WITH_STARBASE, self.pEventHandler, "PlayerDockedWithStarbaseHandler")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, "WeaponHitHandler")

		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_CREATED, self.pEventHandler, "ObjectCreatedHandler")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_DESTROYED, self.pEventHandler, "ObjectDestroyedHandler")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SET_PLAYER, self.pEventHandler, "PlayerChangedHandler")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PLAYER_DOCKED_WITH_STARBASE, self.pEventHandler, "PlayerDockedWithStarbaseHandler")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_HIT, self.pEventHandler, "WeaponHitHandler")

		# And for DS9FX Xtended events ;)  -Thanks Sovvie
		try:
			from Custom.DS9FX import DS9FXVersionSignature
			from Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs import DS9FXSavedConfig
			if DS9FXSavedConfig.LifeSupport == 1 and DS9FXVersionSignature.DS9FXVersion == "Xtended":
				from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
				#Ok, now to the Life Support system events:

				#Ship lost all crew, AI is killed and is removed from the friendly\enemy group to prevent ships from attacking it further
				App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, self.pEventHandler, "LifeSup_ShipDead_Handler")
				App.g_kEventManager.AddBroadcastPythonMethodHandler(DS9FXGlobalEvents.ET_SHIP_DEAD_IN_SPACE, self.pEventHandler, "LifeSup_ShipDead_Handler")

				#Ship reactivated, new AI is assigned and is added to the friendly group
				App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, self.pEventHandler, "LifeSup_ShipReactivated_Handler")
				App.g_kEventManager.AddBroadcastPythonMethodHandler(DS9FXGlobalEvents.ET_SHIP_REACTIVATED, self.pEventHandler, "LifeSup_ShipReactivated_Handler")

				#Ship taken over, friendly AI is assigned and group changed from enemy to friendly
				App.g_kEventManager.RemoveBroadcastHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, self.pEventHandler, "LifeSup_ShipTaken_Handler")
				App.g_kEventManager.AddBroadcastPythonMethodHandler(DS9FXGlobalEvents.ET_SHIP_TAKEN_OVER, self.pEventHandler, "LifeSup_ShipTaken_Handler")
				Galaxy.Logger.LogString("WarSim Message: DS9FX Xtended was found. Life Support handlers online.") 
		except:
			Galaxy.Logger.LogString("WarSim Message: DS9FX Xtended not found... Not creating Life Support handlers...")

		# add a little starting funds for all races
		for sRaceName in Custom.QBautostart.Libs.Races.Races.keys():
			pRaceObj = Custom.QBautostart.Libs.Races.Races[sRaceName]
			pRaceObj.AddFunds(100000.0)
		# create our ship class cost table
		self.CreateShipClassCostTable()
		# create the sound alert we'll play when the player ends a battle
		self.BattleEndedSound = App.TGSound_Create("scripts\\Custom\\GalaxyCharts\\Sounds\\PlayerBattleEnded.mp3", "WarSim_BattleEnded", 0)
		self.BattleEndedSound.SetSFX(0)
		self.BattleEndedSound.SetInterface(1)
		# mark we are initialized
		self.__initialized = 1
		self.lastClock = time.clock()
		# and for debug, print stats
		#self.PrintStats()
		#####
		# load save game if possible and enabled	
		sSelectedSaveGame = GetConfigValue("SelectedSaveGame")
		if sSelectedSaveGame != "None":
			CreateMethodTimer(self.pEventHandler, "_loadSelectedSaveGame", App.g_kUtopiaModule.GetGameTime()+10.0)
			ShowTextBanner("Loading Saved Game... Please Wait.", 0.5, 0.4, 11.0, 13, 1, 1)
			self.bIsLoadingGame = 1
		#####
		# send our custom initialized event
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(ET_WAR_SIM_INITIALIZED)
		pEvent.SetDestination(self.pEventHandler)
		App.g_kEventManager.AddEvent(pEvent)
	def _loadSelectedSaveGame(self, pEvent = None):
		debug(__name__ + ", _loadSelectedSaveGame")
		sSelectedSaveGame = GetConfigValue("SelectedSaveGame")
		if sSelectedSaveGame != "None":
			SavingSystem.Load(sSelectedSaveGame)
		self.bIsLoadingGame = 0
	def IsInitialized(self):
		debug(__name__ + ", IsInitialized")
		return self.__initialized
	def CreateShipClassCostTable(self):
		debug(__name__ + ", CreateShipClassCostTable")
		self.dShipClassesCost = {}
		for pShipDef in Foundation.shipList:
			sShipScript = pShipDef.shipFile
			self.dShipClassesCost[sShipScript] = GetShipFundCost(sShipScript)
	# ship class = ship script name
	def GetShipClassCost(self, sShipClass):
		debug(__name__ + ", GetShipClassCost")
		if self.dShipClassesCost.has_key(sShipClass) == 1:
			return self.dShipClassesCost[sShipClass]
		else:
			return GetShipFundCost(sShipClass)
	def SetPlayerLeadsAttack(self, bPLA):
		debug(__name__ + ", SetPlayerLeadsAttack")
		self.__playerLeadsAttack = bPLA
	def GetPlayerLeadsAttack(self):
		debug(__name__ + ", GetPlayerLeadsAttack")
		return self.__playerLeadsAttack

	def Update(self, pObject = None, pEvent = None):
		# WAR! Who? Yeah! What is it good for? Absolutely nothing! Say that again, yoo!
		debug(__name__ + ", Update")
		if self.__initialized == 0:
			return
		# check if we're going to load a game to warn the player
		if self.bIsLoadingGame == 1:
			ShowTextBanner("Loading Saved Game... Please Wait.", 0.5, 0.4, 1.1, 13, 1, 1)
		else:
			#since we're not loading a game, count the game time.
			fCurrentClock = time.clock()
			fTimePassed =  fCurrentClock - self.lastClock
			self.lastClock = fCurrentClock
			self.dStats["PlayTime"] = self.dStats["PlayTime"] + fTimePassed
		# reset all WarAIs after some time, since sometimes the ships are getting "stuck" in the Attack AI components, not obeying the War AI tree.
		# resetting the AI makes them "come to their senses" and work as they should
		# dunno tho if this is the best way to do it...
		if self.iAIResetCounter >= 30:
			for pWSShip in self.dShips.values():
				if IsShipUsingWarAI(pWSShip.Ship) == 1:
					pWSShip.Ship.GetAI().Reset()
				#elif IsStation(pWSShip.Ship) == 1:
				#	ResetShipAI(pWSShip.Ship)
			self.iAIResetCounter = 0
		else:
			self.iAIResetCounter = self.iAIResetCounter + 1
		# update races stats.
		pPlayer = App.Game_GetCurrentPlayer()
		lAllRaces = Custom.QBautostart.Libs.Races.Races.keys()
		for sRaceName in lAllRaces:
			pRaceObj = Custom.QBautostart.Libs.Races.Races[sRaceName]
			fEconomicModifier = GetConfigValue("GetWarSimConfig").EconomicModifier
			pRaceObj.AddFunds(pRaceObj.GetTotalEconomyProduction()*fEconomicModifier)  

			# NOW CHECK IF RACE WILL ATTACK / manage ships
			if IsBattleHappening() == 0 and self.__RAFcalled == 0:
				if self.__timeSinceLastBattle == -1.0:
					self.__timeSinceLastBattle = time.clock()
				fMinimalAttackFunds = GetRandomInRange(300000.0, 600000.0)
				fSecsSinceLastBattle = time.clock() - self.__timeSinceLastBattle
				fSecsTimeBarrier = GetRandomInRange(180.0, 600.0)
				fPeaceValue = pRaceObj.GetPeaceValue()
				fChance = (100.0 - (fPeaceValue * 100))
				iRaceSystems = len(pRaceObj.GetSystems())
				if iRaceSystems == 0:
					fChance = 0
				fRAFModifier = GetConfigValue("GetWarSimConfig").RAFModifier
				if fRAFModifier != 0.0:
					fChance = fChance / (100.0/fRAFModifier)
					fSecsTimeBarrier = fSecsTimeBarrier * (100.0/fRAFModifier)
					fMinimalAttackFunds = fMinimalAttackFunds * (100.0/fRAFModifier)
				else:
					# if fRAFModifier is 0, no RAFs can happen. Instead or resetting all 3 values, just nullify the fChance since that will 
					# already cancel the RAF check.
					fChance = -10.0
				if pRaceObj.GetTotalFunds() >= fMinimalAttackFunds and App.g_kSystemWrapper.GetRandomNumber(100) <= fChance and fSecsSinceLastBattle > fSecsTimeBarrier:
					sPlayerRace = GetShipRaceByWarSim( pPlayer )
					sTargetRace = lAllRaces[   App.g_kSystemWrapper.GetRandomNumber( len(lAllRaces) )   ]
					pTargetRace = Custom.QBautostart.Libs.Races.Races[sTargetRace]
					bPlayerHasRaceCommand = GetConfigValue("GetWarSimConfig").PlayerHasRaceCommand
					if sTargetRace != sRaceName and pTargetRace != None:
						if (sRaceName == sPlayerRace and bPlayerHasRaceCommand != 1) or AreRacesAllied(sRaceName, sPlayerRace) == 1:
							# player or allied race
							if AreRacesEnemies(sRaceName, sTargetRace) == 1 and AreRacesEnemies(sPlayerRace, sTargetRace) == 1:
								# target race is enemy to both. Now put a RAF up her ass.. ops, territory. =P
								# now choose with region to attack, and don't forget to call the player to join the fun.
								pTargetRegion = self.__acquireTargetRegion(pRaceObj, pTargetRace)
								if pTargetRegion != None:
									if pTargetRegion.RegionBattle.CallRAFofRace(sRaceName) == 1:
										# RAF was started succesfully
										if sRaceName == sPlayerRace:
											sMsgTxt = "Our forces are going to attack "+pTargetRegion.GetName()+". We must assist them Captain."
										else:
											sMsgTxt = sRaceName+" forces are going to attack "+pTargetRegion.GetName()+". They are asking our assistance Captain."
										#self.AddNewsItem("Region", sRaceName+" forces are going to attack "+pTargetRegion.GetName()+"("+sTargetRace+" territory)")
										ShowTextBanner(sMsgTxt, 0.5, 0.4, 5.0, 13, 1, 0)
										self.__timeSinceLastBattle = -1.0
										self.__RAFcalled = 1
						elif AreRacesEnemies(sRaceName, sPlayerRace) == 1:
							# enemy to the player race
							if (AreRacesAllied(sPlayerRace, sTargetRace) == 1 or sPlayerRace == sTargetRace) and AreRacesEnemies(sRaceName, sTargetRace) == 1:
								# target race is allied to the player, and enemy to this race. RAF her up.
								pTargetRegion = self.__acquireTargetRegion(pRaceObj, pTargetRace)
								if pTargetRegion != None:
									if pTargetRegion.RegionBattle.CallRAFofRace(sRaceName) == 1:
										if sTargetRace == sPlayerRace:
											sMsgTxt = "Incoming "+sRaceName+" attack on our "+pTargetRegion.GetName()+" system! We must assist them Captain."
										else:
											sMsgTxt = "Incoming "+sRaceName+" attack on allied "+pTargetRegion.GetName()+" system! They are asking our assistance Captain."
										#self.AddNewsItem("Region", sRaceName+" forces are going to attack "+pTargetRegion.GetName()+"("+sTargetRace+" territory)")
										ShowTextBanner(sMsgTxt, 0.5, 0.4, 5.0, 13, 1, 0)
										# RAF was started succesfully
										self.__timeSinceLastBattle = -1.0
										self.__RAFcalled = 1
			elif IsBattleHappening() == 1:
				self.__timeSinceLastBattle = time.clock()
				self.__RAFcalled = 0

		if pPlayer != None:
			pSet = pPlayer.GetContainingSet()
			if pSet != None and pSet.GetRegionModule() == "Custom.GalaxyCharts.TravelerSystems.Nebula System":
				# check distance of player to Nebula
				if pPlayer.GetWorldLocation().Length() <= ConvertKMtoGU(120.0):
					#player is in the distance to spawn clone army.  LOL WOW COOL
					if self.__iActiveClones < 3:
						#create next clone ship.
						if (self.__iCloneNum % 10) == 0:
							ShowTextBanner("LOL WOW COOL!!!", 0.5, 0.4, 4.0, 13, 1, 1)
						self.__iCloneNum = self.__iCloneNum + 1
						sCloneName = "Clone "+str(self.__iCloneNum)
						pWSClone = WSShip(sCloneName, "Nebula System", 0)
						WarSimulator.dShips[sCloneName] = pWSClone
						pWSClone.Race = WSShip.pNebCloneRace
						pNebDef = GetShipDefByScript( "Nebula" )
						pClone = CreateShip(pNebDef, pSet, sCloneName, "Enemy")
						fPowerScale = (self.__iCloneNum / 10) + 1    # /10 and not /10.0 because I want the clone bonus after each 10 kills.
						if fPowerScale > 1:
							pClone.SetScale( 1 + (fPowerScale/10.0) )
							#improve shields and phasers by fPowerScale
							pShields = pClone.GetShields()
							if pShields:
								pShiProp = pShields.GetProperty()
								for i in range(6):
									pShiProp.SetMaxShields(i, pShiProp.GetMaxShields(i)*fPowerScale)
									pShiProp.SetShieldChargePerSecond(i, pShiProp.GetShieldChargePerSecond(i)+fPowerScale)
									pShields.SetCurShields(i, pShields.GetMaxShields(i))
							pPhasers = pClone.GetPhaserSystem()
							if pPhasers:
								iChildren = pPhasers.GetNumChildSubsystems()
								for iIndex in range(iChildren):
									pChild = App.EnergyWeapon_Cast(pPhasers.GetChildSubsystem(iIndex))
									pProp = pChild.GetProperty()
									pProp.SetMaxCharge(pProp.GetMaxCharge() * fPowerScale)
									pProp.SetMaxDamage(pProp.GetMaxDamage() * fPowerScale)
						self.__iActiveClones = self.__iActiveClones + 1
						pSensors = pPlayer.GetSensorSubsystem()
						if pSensors:
							pSensors.ForceObjectIdentified(pClone)


		# now send our custom event
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(ET_WAR_SIM_UPDATE)
		pEvent.SetDestination(self.pEventHandler)
		App.g_kEventManager.AddEvent(pEvent)
	def PlayerChangedHandler(self, pEvent):
		#print "PCH: mark 1"
		debug(__name__ + ", PlayerChangedHandler")
		if self.__initialized == 0:
			return
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer == None:
			return
		#print "PCH: player: ", pPlayer, "  (", pPlayer.GetName(), ")"
		sPlaName = pPlayer.GetName()
		#print "PCH: old ship: ", self.sPlayerName
		if self.sPlayerName == "":
			self.sPlayerName = sPlaName
			#print "PCH: mark 2"
		elif self.sPlayerName != sPlaName:
			#print "PCH: mark 3"
			CreateMethodTimer(self.pEventHandler, "_updatePlayerShipsAndFleets", App.g_kUtopiaModule.GetGameTime()+3.0)
	def _updatePlayerShipsAndFleets(self, pEvent = None):
		debug(__name__ + ", _updatePlayerShipsAndFleets")
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer == None:
			return
		#print "PCH: player: update player ships and fleets"
		sPlaName = pPlayer.GetName()
		pShip = App.ShipClass_Cast(App.ObjectClass_GetObject( None, self.sPlayerName ))
		if pShip != None:
			pShipFleet = FleetManager.GetFleetOfShip(pShip)
			pPlaFleet = FleetManager.GetFleetOfShip(pPlayer)
			pShipFleet.UpdateFleetLeadShip()
			if pShipFleet.GetName() != pPlaFleet.GetName():
				pPlaFleet.UpdateFleetLeadShip()
			pPlaFleet.ChangeShipStatusTo(pPlayer, pPlaFleet.ACTIVE)
			ResetShipAI(pShip)
			self.sPlayerName = sPlaName
	def ObjectCreatedHandler(self, pEvent):
		debug(__name__ + ", ObjectCreatedHandler")
		if self.__initialized == 0:
			return
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip != None:
			if SavingSystem.IsLoading() == 1 or pShip.GetName() in SavingSystem.lIgnoreObjCreated:
				SavingSystem.lIgnoreObjCreated.remove(pShip.GetName())
				return
			pSet = pShip.GetContainingSet()
			if pSet == None:
				return
			pRegion = pSet.GetRegion()
			if pRegion == None:
				return
			pSetPluObj = pRegion.GetSetByModule(pSet.GetRegionModule())
			if pSetPluObj != None:
				if pShip.GetName() in pSetPluObj.GetNativeShipNamesList():
					#ignoring ships native to a set.
					return
			# create WSShip instance, add her to the according race list and deduct her fund cost from the race.
			sRegionName = pRegion.GetName()
			sEmpire = pRegion.GetControllingEmpire()
			iOrder = IsShipEnemyOfRace(pShip, sEmpire)
			if self.dShips.has_key(pShip.GetName()) == 1:
				pShipObj = self.dShips[pShip.GetName()]
				# dunno if the following updates are needed, but it is best to do them until proved/tested otherwise...
				#pShipObj.Race = GetRaceClassObj( GetShipRaceByWarSim(pShip) )  #no need to update race since it would set the same value.
				pShipObj.Ship = pShip
				pShipObj.SetOrder(iOrder)
				pShipObj.SetRegionAssignedTo(sRegionName)
			else:
				pShipObj = WSShip(pShip, sRegionName, iOrder)
				self.dShips[pShip.GetName()] = pShipObj
			pShipObj.StartEventHandlers()
			if pShipObj.Race != None and pShipObj.Race.GetRaceName() != "Nebula Clone Army":
				# CHECK HERE: if race doesn't have enough funds, try to delete the ship :P because she can't be created.
				self.dStats["TotalShipsMade"] = self.dStats["TotalShipsMade"] + 1
				if pShip.GetName() == "Starbase 12" and self.__createdSB12 == 0:
					pShipObj.Race.AddWSShip(pShipObj)
					self.__createdSB12 = 1
					self.AddNewsItem("Ship", pShipObj.Race.GetRaceName()+" commissioned ship "+pShipObj.GetShipName()+" (class: "+pShipObj.GetShipClass()+")")
				elif IsPlayer(pShip) == 1 or pShipObj.GetTotalCost(0) <= pShipObj.Race.GetTotalFunds():
					pShipObj.Race.DeductFunds( pShipObj.GetTotalCost(0) )
					pShipObj.Race.AddWSShip(pShipObj)
					self.AddNewsItem("Ship", pShipObj.Race.GetRaceName()+" commissioned ship "+pShipObj.GetShipName()+" (class: "+pShipObj.GetShipClass()+")")
					if IsPlayer(pShip) == 1 and self.sPlayerName == "":
						self.sPlayerName = pShip.GetName()
				else:
					#print pShipObj.Race.GetRaceName(), "doesn\'t have enough funds to create ship", pShip.GetName(), ". Ship is being deleted."
					pSet.DeleteObjectFromSet(pShip.GetName())
					self.DeleteWSShip(pShipObj)				
			elif pShipObj.Race != None and pShipObj.Race.GetRaceName() == "Nebula Clone Army":
				self.AddNewsItem("Ship", "Nebula Clone Army has commissioned ship "+pShip.GetName()+"!!")
			#print "Created WSShip obj for ship", pShip.GetName()
			# finally send our ship added event
			pEvent = App.TGEvent_Create()
			pEvent.SetEventType(ET_WAR_SIM_SHIP_ADDED)
			pEvent.SetDestination(pShip)
			App.g_kEventManager.AddEvent(pEvent)
	def ObjectDestroyedHandler(self, pEvent):
		debug(__name__ + ", ObjectDestroyedHandler")
		if self.__initialized == 0:
			return
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip != None:
			if SavingSystem.IsLoading() == 1 or pShip.GetName() in SavingSystem.lIgnoreObjDestroyed:
				SavingSystem.lIgnoreObjDestroyed.remove(pShip.GetName())
				return
			pWSShip = self.GetWSShipObjForShip(pShip)
			if pWSShip == None:
				return
			self.DeleteWSShip(pWSShip)
	def WeaponHitHandler(self, pEvent):
		debug(__name__ + ", WeaponHitHandler")
		if self.__initialized == 0 or pEvent.IsHullHit() != 1:
			return
		pTargetShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pTargetShip == None:
			return
		pFiringShip = App.ShipClass_Cast(pEvent.GetFiringObject())
		if pFiringShip == None:
			return
		fDmg = pEvent.GetDamage()
		#dShipDamages dict should be <target name string, (dict<firing ship name string, damage float>) >
		if not self.dShipDamages.has_key(pTargetShip.GetName()):
			self.dShipDamages[pTargetShip.GetName()] = {}
		if not self.dShipDamages[pTargetShip.GetName()].has_key(pFiringShip.GetName()):
			self.dShipDamages[pTargetShip.GetName()][pFiringShip.GetName()] = 0
		self.dShipDamages[pTargetShip.GetName()][pFiringShip.GetName()] = self.dShipDamages[pTargetShip.GetName()][pFiringShip.GetName()] + fDmg
	def LifeSup_ShipDead_Handler(self, pEvent):
		#Ship lost all crew, AI is killed and is removed from the friendly\enemy group to prevent ships from attacking it further
		debug(__name__ + ", LifeSup_ShipDead_Handler")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip != None:
			Galaxy.Logger.LogString("WarSim:  LifeSupport - Ship Dead: "+str(pShip.GetName()))
			pSet = pShip.GetContainingSet()
			WarSimulator.AddNewsItem("Ship", pShip.GetName()+" has lost all crew, and is adrift in space at the set "+pSet.GetName()+"...")
			pWSShip = self.GetWSShipObjForShip(pShip)
			self.DeleteWSShip(pWSShip)  #lets hope this works right LOL :P
	def LifeSup_ShipReactivated_Handler(self, pEvent):
		#Ship reactivated, new AI is assigned and is added to the friendly group
		debug(__name__ + ", LifeSup_ShipReactivated_Handler")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())  # the ship that was taken over.
		pCapturer = App.ShipClass_Cast(pEvent.GetSource())  # the ship that captured the other one.
		if pShip != None and pCapturer != None:
			Galaxy.Logger.LogString("WarSim:  LifeSupport - Ship Reactivated: "+str(pShip.GetName()))
			WarSimulator.AddNewsItem("Ship", pShip.GetName()+" has been recrewed and reactivated.")

			pSet = pShip.GetContainingSet()
			if pSet == None:
				return
			pRegion = pSet.GetRegion()
			if pRegion == None:
				return

			# create WSShip instance, add her to the according race list and deduct her fund cost from the race.
			sRegionName = pRegion.GetName()
			sEmpire = pRegion.GetControllingEmpire()
			iOrder = IsShipEnemyOfRace(pShip, sEmpire)

			pShipObj = self.dShips[pShip.GetName()]
			pCapturerObj = self.dShips[pCapturer.GetName()]
			# dunno if the following updates are needed, but it is best to do them until proved/tested otherwise...
			pShipObj.Race = pCapturerObj.Race
			pShipObj.Ship = pShip
			pShipObj.SetOrder(iOrder)
			pShipObj.SetRegionAssignedTo(sRegionName)

			pShipObj.StartEventHandlers()
			if pShipObj.Race != None:
				self.dStats["TotalShipsMade"] = self.dStats["TotalShipsMade"] + 1
				pShipObj.Race.AddWSShip(pShipObj)

				pShipObj.UpdateShipAllegiance()

				pFleet = FleetManager.GetFleetOfShip(pShip)
				if pFleet == None:
					# ship doesn't have a fleet, probably has just been created. Find one or create one for it.
					pFleet = FleetManager.FindFleetToEnterIn(pRegion.GetName(), pShipObj.Race.GetRaceName() )
					if pFleet == None:
						FleetManager.CreateFleet(pShip)
					else:
						pFleet.AddShip(pShip)
				elif pFleet != None:
					# ship already has a fleet. If we're leading and we have another allied fleet in the region, try to merge fleets together.
					if pFleet.GetLeadShipName() == pShip.GetName():
						lAlliedFleets = FleetManager.GetAlliedFleetsInRegion(pRegion.GetName(), pShipObj.Race.GetRaceName() )
						if pFleet.GetFleetRegion() != None:
							if pFleet.GetFleetRegion().GetName() != pRegion.GetName():
								lAlliedFleets.append(pFleet)
						if len(lAlliedFleets) >= 2:
							# HERE!  TRY TO MERGE FLEETS TOGETHER
							FleetManager.TryToMergeFleets(lAlliedFleets)
				pRegion.RegionBattle.AddShipToBattle(pShip)
				
			# finally send our ship added event
			pEvent = App.TGEvent_Create()
			pEvent.SetEventType(ET_WAR_SIM_SHIP_ADDED)
			pEvent.SetDestination(pShip)
			App.g_kEventManager.AddEvent(pEvent)
	def LifeSup_ShipTaken_Handler(self, pEvent):
		#Ship taken over, friendly AI is assigned and group changed from enemy to friendly
		debug(__name__ + ", LifeSup_ShipTaken_Handler")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())  # the ship that was taken over.
		pCapturer = App.ShipClass_Cast(pEvent.GetSource())  # the ship that captured the other one.
		if pShip != None and pCapturer != None:
			Galaxy.Logger.LogString("WarSim:  LifeSupport - Ship Taken: "+str(pShip.GetName()))
			WarSimulator.AddNewsItem("Ship", pShip.GetName()+" has been taken over by another species.")
			pSet = pShip.GetContainingSet()
			if pSet == None:
				return
			pRegion = pSet.GetRegion()
			if pRegion == None:
				return

			# create WSShip instance, add her to the according race list and deduct her fund cost from the race.
			sRegionName = pRegion.GetName()
			sEmpire = pRegion.GetControllingEmpire()
			iOrder = IsShipEnemyOfRace(pShip, sEmpire)

			pShipObj = self.dShips[pShip.GetName()]
			pCapturerObj = self.dShips[pCapturer.GetName()]
			# dunno if the following updates are needed, but it is best to do them until proved/tested otherwise...
			pShipObj.Race = pCapturerObj.Race
			pShipObj.Ship = pShip
			pShipObj.SetOrder(iOrder)
			pShipObj.SetRegionAssignedTo(sRegionName)

			pShipObj.StartEventHandlers()
			if pShipObj.Race != None:
				self.dStats["TotalShipsMade"] = self.dStats["TotalShipsMade"] + 1
				pShipObj.Race.AddWSShip(pShipObj)

				pShipObj.UpdateShipAllegiance()

				pFleet = FleetManager.GetFleetOfShip(pShip)
				if pFleet == None:
					# ship doesn't have a fleet, probably has just been created. Find one or create one for it.
					pFleet = FleetManager.FindFleetToEnterIn(pRegion.GetName(), pShipObj.Race.GetRaceName() )
					if pFleet == None:
						FleetManager.CreateFleet(pShip)
					else:
						pFleet.AddShip(pShip)
				elif pFleet != None:
					# ship already has a fleet. If we're leading and we have another allied fleet in the region, try to merge fleets together.
					if pFleet.GetLeadShipName() == pShip.GetName():
						lAlliedFleets = FleetManager.GetAlliedFleetsInRegion(pRegion.GetName(), pShipObj.Race.GetRaceName() )
						if pFleet.GetFleetRegion() != None:
							if pFleet.GetFleetRegion().GetName() != pRegion.GetName():
								lAlliedFleets.append(pFleet)
						if len(lAlliedFleets) >= 2:
							# HERE!  TRY TO MERGE FLEETS TOGETHER
							FleetManager.TryToMergeFleets(lAlliedFleets)
				pRegion.RegionBattle.AddShipToBattle(pShip)
				
			# finally send our ship added event
			pEvent = App.TGEvent_Create()
			pEvent.SetEventType(ET_WAR_SIM_SHIP_ADDED)
			pEvent.SetDestination(pShip)
			App.g_kEventManager.AddEvent(pEvent)
	def ChangeRegionToRace(self, pRegion, sNewRaceName):
		# USE this to change a region's controlling empire to the given one. Used when a system is conquered.
		# change the region's controlling empire and add a new line in her description telling "Taken by <empire> at <time stamp>" or something like
		# that
		debug(__name__ + ", ChangeRegionToRace")
		if self.__initialized == 0:
			return
		sOldRaceName = pRegion.ControllingEmpire
		###
		# check if its the race's last system. Gain a little prize if it is ;)
		pLoserRaceObj = GetRaceClassObj(sOldRaceName)
		pWinnerRaceObj = GetRaceClassObj(sNewRaceName)
		fFundsStolen = 0.0
		if pLoserRaceObj != None and pWinnerRaceObj != None and len(pLoserRaceObj.GetSystems()) <= 1:
			fFundsStolen = pLoserRaceObj.GetTotalFunds() * 0.7
			pLoserRaceObj.DeductFunds(fFundsStolen)
			pWinnerRaceObj.AddFunds(fFundsStolen)
		###
		pRegion.Description = pRegion.Description + "\n-" + sNewRaceName + " conquered this system from " + pRegion.ControllingEmpire + " at " + self.GetTime()
		if fFundsStolen != 0.0:
			self.AddNewsItem("Region", sNewRaceName + " conquered "+pRegion.GetName()+" from " + pRegion.ControllingEmpire + ", acquiring "+GetStrFromFloat(fFundsStolen, 2)+" funds in the process.")
		else:
			self.AddNewsItem("Region", sNewRaceName + " conquered "+pRegion.GetName()+" from " + pRegion.ControllingEmpire)
		pRegion.ControllingEmpire = sNewRaceName
		pRegion.RegionBattle.SwitchShipSides()
		#####################################
		# update the Galaxy Map GUI, the player may be using it, so we need to update it in
		# real time
		GalaxyMapGUI.UpdateGUI()
		SystemAnalysisGUI.UpdateSystemAnalysis()
		#####################################
		#print "Changed", pRegion.GetName(), "controlling empire from", sOldRaceName, "to", sNewRaceName
		#now send our custom event
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_REGION_CONQUERED)
		pEvent.SetDestination(pRegion.RegionBattle.pEventHandler)
		pEvent.SetString(sOldRaceName)
		App.g_kEventManager.AddEvent(pEvent)
	def GetWSShipObjForShip(self, pShip):
		debug(__name__ + ", GetWSShipObjForShip")
		if pShip == None:
			return None
		if self.dShips.has_key(pShip.GetName()):
			return self.dShips[pShip.GetName()]
	def GetWSShipObjForName(self, sShipName):
		debug(__name__ + ", GetWSShipObjForName")
		if self.dShips.has_key(sShipName):
			return self.dShips[sShipName]
	def GetFirstIdleShipClassOfRace(self, sShipClass, sRace):
		debug(__name__ + ", GetFirstIdleShipClassOfRace")
		for pWSShip in self.dShips.values():
			if pWSShip.Race != None:
				if pWSShip.Race.GetRaceName() == sRace:
					if pWSShip.GetShipClass() == sShipClass:
						if pWSShip.GetOrder() == pWSShip.O_NOTHING:
							return pWSShip
		return None
	def DeleteWSShip(self, pWSShip):
		# USE this to delete a WSShip instance from the game. deleting it from every possible place she might be lol
		# total possible lists so far:  race obj ship list, war simulation ship list, region battle ship list
		# lists left to delete from:   none...
		#print "DeleteWSShip start"
		debug(__name__ + ", DeleteWSShip")
		if self.__initialized == 0 or SavingSystem.IsLoading() == 1:
			return
		if pWSShip.GetOrder() == pWSShip.O_DESTROYED:
			return
		if IsPlayer(pWSShip.Ship) != 1:
			pWSShip.ClearEventHandlers()
		# send our ship deleted event
		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(ET_WAR_SIM_SHIP_DELETED)
		pEvent.SetDestination(pWSShip.Ship)
		App.g_kEventManager.AddEvent(pEvent)
		###
		pFleet = FleetManager.GetFleetOfShip(pWSShip.Ship)
		if pFleet != None:
			pFleet.RemoveShip(pWSShip.Ship)
		pWSPla = None
		if pWSShip.Race != None:
			#########################
			# little easter egg stat
			sShipClass = GetShipType(pWSShip.Ship)
			if sShipClass == "Nebula" and pWSShip.Ship.GetName()[0:5] == "Clone":
				self.__iActiveClones = self.__iActiveClones - 1
			pShipDef = GetShipDefByScript(sShipClass)
			if string.count(sShipClass, "nebula") + string.count(sShipClass, "Nebula") + string.count(pShipDef.name, "nebula") + string.count(pShipDef.name, "Nebula") >= 1:
				self.dStats["NebulasDestroyed"] = self.dStats["NebulasDestroyed"] + 1
			########################
			pWSShip.Race.DeleteWSShip(pWSShip)
			if IsPlayer(pWSShip.Ship) == 1:
				pWSShip.Race.DeductFunds( pWSShip.GetTotalCost(0) / 2.0 )
				self.dStats["Deaths"] = self.dStats["Deaths"] + 1
			elif self.dShips.has_key(self.sPlayerName): 
				#this else part is only needed to check if a friendly ship was killed to update the war stats.
				pWSPla = self.dShips[self.sPlayerName]
				if pWSPla.Race == None:
					pass
				elif pWSPla.Race.GetRaceName() == pWSShip.Race.GetRaceName() or IsShipFriendlyOfRace(pWSShip.Ship, pWSPla.Race.GetRaceName()) == 1:
					self.dStats["TotalFriendlyShipDeaths"] = self.dStats["TotalFriendlyShipDeaths"] + 1
		###
		# try to check which ship destroyed this one
		sDestroyedBy = ""
		if self.dShipDamages.has_key(pWSShip.Ship.GetName()):
			dAttackers = self.dShipDamages[pWSShip.Ship.GetName()]
			fBiggestDamage = 0
			for sAttacker in dAttackers.keys():
				if dAttackers[sAttacker] > fBiggestDamage:
					sDestroyedBy = sAttacker
					fBiggestDamage = dAttackers[sAttacker]
			pWSAttacker = self.GetWSShipObjForName(sDestroyedBy)
			if not pWSPla:
				pWSPla = self.GetWSShipObjForShip(App.Game_GetCurrentPlayer())
			if pWSPla == None or pWSAttacker == None:
				#strange, but may be possible without necessarily something bad happening...
				pass
			elif pWSPla.GetShipName() == pWSAttacker.GetShipName():
				# player kill
				self.dStats["Kills"] = self.dStats["Kills"] + 1
			elif pWSPla.Race == None or pWSAttacker.Race == None:
				# something bad happened...
				pass
			elif pWSPla.Race.GetRaceName() == pWSAttacker.Race.GetRaceName() or AreRacesAllied(pWSAttacker.Race.GetRaceName(), pWSPla.Race.GetRaceName()) == 1:
				# friendly kill
				self.dStats["TotalFriendlyShipKills"] = self.dStats["TotalFriendlyShipKills"] + 1
			sDestroyedBy = " (by "+sDestroyedBy+")"
			del self.dShipDamages[pWSShip.Ship.GetName()]
		###
		pRegion = App.g_kRegionManager.GetRegion(pWSShip.GetRegionAssignedTo())
		if pRegion != None:
			pRegion.RegionBattle.RemoveShipFromBattle(pWSShip.Ship)
		pWSShip.SetOrder(pWSShip.O_DESTROYED)
		pWSShip.SetRegionAssignedTo( "None" )
		pWSShip.Ship = None
		sRaceName = ""
		if pWSShip.Race != None:
			sRaceName = pWSShip.Race.GetRaceName()
		self.AddNewsItem("Ship", sRaceName+" ship "+pWSShip.GetShipName()+" was destroyed"+sDestroyedBy+".")
		#del self.dShips[pWSShip.GetShipName()]
		#print "Deleted WSShip obj for ship", pWSShip.GetShipName(), ".  Destroyed by:", sDestroyedBy
		self.dStats["TotalShipDeaths"] = self.dStats["TotalShipDeaths"] + 1
	def AddNewsItem(self, sType, sData):
		debug(__name__ + ", AddNewsItem")
		sTimeStamp = self.GetTime()
		self.lNews.insert(0, [sTimeStamp, sType, sData] )
	def GetNewsList(self, sType = ""):
		debug(__name__ + ", GetNewsList")
		lNewsList = []
		sLastDate = ""
		for lNewsItem in self.lNews:
			#time stamp example:    23:30:58.042 of 28/April/2008, Monday
			sTimeStamp = lNewsItem[0]
			sNewsType = lNewsItem[1]
			sNewsData = lNewsItem[2]
			lTimeElements = string.split(string.split(sTimeStamp, ",")[0], " ")
			sTime = string.split(lTimeElements[0], ".")[0]
			sDate = lTimeElements[2]
			if sType == "" or sType == sNewsType:
				if sLastDate != sDate:
					lNewsList.append("")
					lNewsList.append("DATE - "+sDate+":")
					sLastDate = sDate
				lNewsList.append("   >"+sTime+": "+sNewsData)
		return lNewsList
	def GetStatsList(self):
		debug(__name__ + ", GetStatsList")
		lStatsList = []
		lStatsList.append("Player Stats:")
		lStatsList.append("   >Ships Killed: "+str(self.dStats["Kills"]))
		lStatsList.append("   >Times Docked in Starbases: "+str(self.dStats["StarbaseDocks"]))
		lStatsList.append("   >Times Died: "+str(self.dStats["Deaths"]))
		lStatsList.append("   >Times Traveled: "+str(self.dStats["TimesTraveled"]))
		lStatsList.append("   >Battles Participated In: "+str(self.dStats["BattlesParticipated"]))
		lStatsList.append("")
		lStatsList.append("")
		lStatsList.append("Player Race Stats:")
		lStatsList.append("   >Funds Acquired: "+str(self.dStats["FundsAcquired"]))
		lStatsList.append("   >Funds Spent: "+str(self.dStats["FundsSpent"]))
		lStatsList.append("   >Total Friendly Ship Kills: "+str(self.dStats["TotalFriendlyShipKills"]))
		lStatsList.append("   >Total Friendly Ship Deaths: "+str(self.dStats["TotalFriendlyShipDeaths"]))
		lStatsList.append("   >Systems Conquered: "+str(self.dStats["SystemsConquered"]))
		lStatsList.append("   >Systems Defended: "+str(self.dStats["SystemsDefended"]))
		lStatsList.append("   >Races Defeated: "+str(self.dStats["RacesDefeated"]))
		lStatsList.append("")
		lStatsList.append("")
		lStatsList.append("General Stats:")
		lStatsList.append("   >Time Playing: "+ GalaxyMapGUI.GetTimeStrings( self.dStats["PlayTime"] , 0)  )
		lStatsList.append("   >Times the Game was saved: "+str(self.dStats["TimesSaved"]))
		lStatsList.append("   >Total Ships Created: "+str(self.dStats["TotalShipsMade"]))
		lStatsList.append("   >Total Ships Destroyed: "+str(self.dStats["TotalShipDeaths"]))
		lStatsList.append("   >Total Battles Occured: "+str(self.dStats["TotalBattlesOccured"]))
		lStatsList.append("")
		lStatsList.append("")
		lStatsList.append("Nebulas Annihilated: "+str(self.dStats["NebulasDestroyed"]))
		return lStatsList
	def PlayerDockedWithStarbaseHandler(self, pEvent):
		# event fired by UndockFromStarbase CompoundAI -> when player undocks with a starbase.
		debug(__name__ + ", PlayerDockedWithStarbaseHandler")
		pShip = App.ShipClass_Cast(pEvent.GetSource())
		#GetDestination is the Starbase from which he undocked
		#GetBool -> probably would mean if he's docking or undocking with the base... but since this event is only fired from the UndockFromStarbase
		#           in one particular case....  still, UndockFromStarbase makes it Bool = 0
		if pShip != None and pEvent.GetBool() == 0:
			#player undocked
			self.dStats["StarbaseDocks"] = self.dStats["StarbaseDocks"] + 1
	def GetNewsTypes(self):
		debug(__name__ + ", GetNewsTypes")
		lNewsTypes = []
		for lNewsItem in self.lNews:
			sNewsType = lNewsItem[1]
			if not sNewsType in lNewsTypes:
				lNewsTypes.append(sNewsType)
		return lNewsTypes
	def PlayBattleEndedSound(self):
		debug(__name__ + ", PlayBattleEndedSound")
		self.BattleEndedSound.Play()
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def PrintStats(self):
		debug(__name__ + ", PrintStats")
		print "_________________________________________"
		print "WAR SIMULATION STATS:"
		print ">>> Ship Classes Cost Table:"
		for sShipClass in self.dShipClassesCost.keys():
			print "   -"+sShipClass+":", self.dShipClassesCost[sShipClass]
		###
		print ">>> Race Stats:"
		fEconomicModifier = GetConfigValue("GetWarSimConfig").EconomicModifier
		for sRaceName in Custom.QBautostart.Libs.Races.Races.keys():
			print "   >->"+sRaceName+":"
			pRaceObj = Custom.QBautostart.Libs.Races.Races[sRaceName]
			print "        -Economic Production:", pRaceObj.GetTotalEconomyProduction(), " ("+str(pRaceObj.GetTotalEconomyProduction()*fEconomicModifier)+")"
			print "        -Total Funds:", pRaceObj.GetTotalFunds()
			print "        -Total Defence Value:", pRaceObj.GetTotalDefenceValue()
			print "        -Ships:"
			for sShipName in pRaceObj.dWSShips.keys():
				print "            -"+sShipName, "("+pRaceObj.dWSShips[sShipName].GetShipClass()+")"
			print "        -Systems ("+str(len(pRaceObj.GetSystems()))+"):"
			for pRegion in pRaceObj.GetSystems():
				print "            -"+pRegion.GetName()
		print "_________________________________________"
	def GetTime(self):
		debug(__name__ + ", GetTime")
		try:
			Time = __import__('Custom.Autoload.TimeMeasurement')
			return Time.Clock.GetTimeString()
		except:
			return time.asctime(time.localtime(time.time()))
	# this function tries to acquire a good region from pTargetRace as a target for an attack of pRaceObj
	def __acquireTargetRegion(self, pRaceObj, pTargetRace):
		debug(__name__ + ", __acquireTargetRegion")
		lRaceRegions = pRaceObj.GetSystems()
		lTargetRegions = pTargetRace.GetSystems()
		lTargetProps = [1000000.0, None, None]  # attack value factor, region to attack, region to attack from(dunno, might be usefull)
		for pTargReg in lTargetRegions:
			vTargPos = pTargReg.GetLocation()
			for pReg in lRaceRegions:
				# ADDITIONAL:  any additional checks to decide which region to attack should probably be added here.
				# for now, we're only using distance as parameter. The Enemy/Allied region pair that has the smallest distance will be the target.
				vRegPos = pReg.GetLocation()
				vDist = App.NiPoint2(vRegPos.x - vTargPos.x, vRegPos.y - vTargPos.y)
				fDist = vDist.Length()
				if fDist < lTargetProps[0]:
					lTargetProps = [fDist, pTargReg, pReg]
		return lTargetProps[1]
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+str(self.__ID)+">"

WarSimulator = WarSimulatorClass()

# Class to manage/handle ShipFleet instances. 
class FleetManagerClass:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.CLASS = "Fleet Manager"
		self.__ID = GetUniqueID("FleetManager")
		self.dRaceFleets = {}   # "race" = [fleet name list]
		self.dFleetIDs = {}     # fleetname = shipfleet
	def CreateFleet(self, pInitialShip):
		debug(__name__ + ", CreateFleet")
		if IsStation(pInitialShip) == 1:
			return None
		sShipRace = GetShipRaceByWarSim(pInitialShip)
		if GetRaceClassObj(sShipRace) == None:
			return None
		pFleet = ShipFleet(sShipRace)
		WarSimulator.AddNewsItem("Fleet", pFleet.GetName() + " has been created.")
		if not self.dRaceFleets.has_key(sShipRace):
			self.dRaceFleets[sShipRace] = []
		self.dRaceFleets[sShipRace].append(pFleet.GetName())
		self.dFleetIDs[pFleet.GetName()] = pFleet
		pFleet.AddShip(pInitialShip)
		###
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_FLEET_CREATED)
		pEvent.SetDestination(WarSimulator.pEventHandler)
		pEvent.SetString(pFleet.GetName())
		App.g_kEventManager.AddEvent(pEvent)
		###
		return pFleet
	def DeleteFleet(self, pFleet):
		debug(__name__ + ", DeleteFleet")
		if pFleet.GetFleetRegion() == None:
			pFleet.Logger.LogString("Fleet is being deleted...")
			WarSimulator.AddNewsItem("Fleet", pFleet.GetName() + " has been destroyed.")
			self.dRaceFleets[pFleet.GetMainRace()].remove(pFleet.GetName())
			del self.dFleetIDs[pFleet.GetName()]
			###
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(ET_FLEET_DELETED)
			pEvent.SetDestination(WarSimulator.pEventHandler)
			pEvent.SetString(pFleet.GetName())
			App.g_kEventManager.AddEvent(pEvent)
			###
			del pFleet
	def TryToMergeFleets(self, lFleets):
		#try to merge given list of fleets together, so that there is less but more powerfull fleets.
		#for example, passing in 2 fleets, one with 4 ships and other with 5 ships, it will merge these fleets together, forming a fleet with 9 ships.
		#It will take out the ships from the fleets and add them all in a single fleet.
		###
		# start by checking if the fleets are allied.
		debug(__name__ + ", TryToMergeFleets")
		sLastFleetRace = ""
		lFleetNames = []
		for pFleet in lFleets:
			lFleetNames.append(pFleet.GetName())
			if sLastFleetRace == "":
				sLastFleetRace = pFleet.GetMainRace()
			if sLastFleetRace != pFleet.GetMainRace() and AreRacesAllied(sLastFleetRace, pFleet.GetMainRace()) != 1:
				#fleets not allied. break function.
				return 0
		# proceed with the merging process. Acquire which fleets we can merge with which fleets.
		iMaxNumFleets = self.GetMaxNumOfMergedFleets(lFleets)
		lNewFleetList = []   #list of strings containing the names of fleets to merge.
		lNames2 = lFleetNames
		lUseds = []
		while len(lNewFleetList) <= iMaxNumFleets:
			for sName1 in lFleetNames:
				if not sName1 in lUseds:
					pFleet1 = self.dFleetIDs[sName1]
					iTotalShipCount = pFleet1.GetShipCount()
					lNamesToMerge = [sName1]
					for sName2 in lNames2:
						if sName2 != sName1 and not sName2 in lUseds:
							pFleet2 = self.dFleetIDs[sName2]
							iF2Count = pFleet2.GetShipCount()
							if (iTotalShipCount + iF2Count) <= ShipFleet.iMaxShipsPerFleet:
								# ok juntar essas
								lNamesToMerge.append(sName2)
								iTotalShipCount = iTotalShipCount + iF2Count
					sToMerge = ""
					for sFleetName in lNamesToMerge:
						sToMerge = sToMerge + sFleetName + "+"
						#lUseds.append(sFleetName)
						lNames2.remove(sFleetName)
					sToMerge = sToMerge[0:len(sToMerge)-1]
					lNewFleetList.append(sToMerge)
			if len(lNewFleetList) == iMaxNumFleets:
				break
		# Ok now we know which fleets we need to merge, lets merge them.
		for sFleetMergingNames in lNewFleetList:
			lFMN = string.split(sFleetMergingNames, "+")
			if len(lFMN) >= 2:
				# okay we need to merge these fleets.
				pMergedFleet = None
				for sFleetName in lFMN:
					pFleet = self.dFleetIDs[sFleetName]
					if pMergedFleet == None:
						pMergedFleet = pFleet
					if pFleet.GetName() != pMergedFleet.GetName():
						pFleet.Logger.LogString("MARK: Merging with fleet: "+pMergedFleet.GetName())
						lShips = pFleet.GetShipObjList()
						for pShip in lShips:
							pFleet.RemoveShip(pShip)
							pMergedFleet.AddShip(pShip)
		return 1
	def GetMaxNumOfMergedFleets(self, fleetlist):
		debug(__name__ + ", GetMaxNumOfMergedFleets")
		i = 0
		for f in fleetlist:
			i = i + f.GetShipCount()
		ret = i/20.0
		if int(ret) == ret:
			return int(ret)
		return int(ret) + 1
	def GetAllFleets(self):
		debug(__name__ + ", GetAllFleets")
		return self.dFleetIDs.values()
	def GetAllFleetsOfRace(self, sRaceName):
		debug(__name__ + ", GetAllFleetsOfRace")
		lFleets = []
		if not self.dRaceFleets.has_key(sRaceName):
			return None
		lRaceFleetNames = self.dRaceFleets[sRaceName]
		for sFleetName in lRaceFleetNames:
			lFleets.append( self.dFleetIDs[sFleetName] )
		return lFleets
	def GetAlliedFleetsOfRace(self, sRaceName):
		debug(__name__ + ", GetAlliedFleetsOfRace")
		lFleets = []
		for pFleet in self.dFleetIDs.values():
			if sRaceName == pFleet.GetMainRace() or AreRacesAllied(sRaceName, pFleet.GetMainRace()) == 1:
				lFleets.append(pFleet)
		return lFleets
	def GetFleetByName(self, sName):
		debug(__name__ + ", GetFleetByName")
		if self.dFleetIDs.has_key(sName):
			return self.dFleetIDs[sName]
		return None
	def GetFleetOfShip(self, pShip):
		debug(__name__ + ", GetFleetOfShip")
		for pFleet in self.dFleetIDs.values():
			if pFleet.IsShipInFleet(pShip):
				return pFleet
	def GetFleetOfShipName(self, sShipName):
		debug(__name__ + ", GetFleetOfShipName")
		for pFleet in self.dFleetIDs.values():
			if pFleet.IsShipNameInFleet(sShipName):
				return pFleet
	def GetAlliedFleetsInRegion(self, sRegionName, sRaceName):
		debug(__name__ + ", GetAlliedFleetsInRegion")
		lFleets = []
		for pFleet in self.dFleetIDs.values():
			pRegion = pFleet.GetFleetRegion()
			if pRegion != None and pRegion.GetName() == sRegionName:
				if sRaceName == pFleet.GetMainRace() or AreRacesAllied(sRaceName, pFleet.GetMainRace()) == 1:
					lFleets.append(pFleet)
		return lFleets
	def FindFleetToEnterIn(self, sRegion, sRace):
		debug(__name__ + ", FindFleetToEnterIn")
		lPossibleFleets = self.GetAlliedFleetsInRegion(sRegion, sRace)
		for pFleet in lPossibleFleets:
			if pFleet.GetUnusedShipSlotsNumber() >= 1:
				return pFleet
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+str(self.__ID)+">"

FleetManager = FleetManagerClass()

# Class to hold info about a ship fleet. 
class ShipFleet:
	iMaxShipsPerFleet = 20
	dRacesIndexValues = {}

	IDLE = 0       # Enumaration to mark the status of a ship in the fleet, or the status of the fleet as a whole.
	ACTIVE = 1     #

	def __init__(self, sRace, dShipFleetData = None):
		debug(__name__ + ", __init__")
		self.CLASS = "Ship Fleet"
		if sRace == None and type(dShipFleetData) == type({}) and SavingSystem.IsLoading() == 1:
			for sAttr in dShipFleetData.keys():
				self.__dict__[sAttr] = dShipFleetData[sAttr]
		else:
			if not ShipFleet.dRacesIndexValues.has_key(sRace):
				ShipFleet.dRacesIndexValues[sRace] = 1
			iIndex = ShipFleet.dRacesIndexValues[sRace]
			if iIndex == 1:
				sSuffix = "st"
			if iIndex == 2:
				sSuffix = "nd"
			if iIndex == 3:
				sSuffix = "rd"
			if iIndex >= 4:
				sSuffix = "th"
			self.__fleetNum = iIndex
			self.__shortName = str(iIndex) + sSuffix + " Fleet"
			sName = sRace + " " + self.__shortName
			ShipFleet.dRacesIndexValues[sRace] = ShipFleet.dRacesIndexValues[sRace] + 1
			self.__ID = GetUniqueID(sName)
			self.__name = sName
			self.__race = sRace
			self.leadShip = ""
			self.lShips = []
			self.dShipsStatus = {} # "shipname" = status
		##########
		self.Logger = Custom.GravityFX.Logger.LogCreator(self.__name+" Logger", "scripts\Custom\GalaxyCharts\Logs\WarAIFleet_"+self.__name+"_LOG.txt")
		self.Logger.LogString("Ship Fleet created, Logger Initialized.")
		self.Logger.LogString("SELF = "+self.__repr__())
	def GetName(self):
		debug(__name__ + ", GetName")
		return self.__name
	def GetShortName(self):
		debug(__name__ + ", GetShortName")
		return self.__shortName
	def GetFleetNumber(self):
		debug(__name__ + ", GetFleetNumber")
		return self.__fleetNum
	def GetMainRace(self):
		debug(__name__ + ", GetMainRace")
		return self.__race
	def GetUnusedShipSlotsNumber(self):
		debug(__name__ + ", GetUnusedShipSlotsNumber")
		iSlots = ShipFleet.iMaxShipsPerFleet - len(self.lShips)
		if iSlots < 0:
			# O_o really strange...
			iSlots = 0
		return iSlots
	def GetShipCount(self):
		debug(__name__ + ", GetShipCount")
		return len(self.lShips)
	def GetShipNameList(self):
		debug(__name__ + ", GetShipNameList")
		return self.dShipsStatus.keys()
	def GetShipObjList(self):
		debug(__name__ + ", GetShipObjList")
		lObjs = []
		for sShipName in self.lShips:
			pShip = MissionLib.GetShip(sShipName, None, 1)
			if pShip != None:
				lObjs.append(pShip)
		return lObjs
	def GetLeadShipName(self):
		debug(__name__ + ", GetLeadShipName")
		return self.leadShip
	def GetLeadShipObj(self):
		debug(__name__ + ", GetLeadShipObj")
		return MissionLib.GetShip(self.leadShip, None, 1)
	def GetFleetTotalCost(self):
		debug(__name__ + ", GetFleetTotalCost")
		fTotalCost = 0.0
		for sShipName in self.dShipsStatus.keys():
			pWSShip = WarSimulator.GetWSShipObjForName(sShipName)
			fTotalCost = fTotalCost + pWSShip.GetTotalCost()
		return fTotalCost
	def IsFleetInNeedOfRepairAndResupply(self):
		debug(__name__ + ", IsFleetInNeedOfRepairAndResupply")
		for sShipName in self.dShipsStatus.keys():
			pWSShip = WarSimulator.GetWSShipObjForName(sShipName)
			if pWSShip.IsShipInNeedOfRepairAndResupply() == 1:
				return 1
		return 0
	def UpdateFleetLeadShip(self):
		debug(__name__ + ", UpdateFleetLeadShip")
		sChosenShip = ""
		fShipCost = 0.0
		pPlayer = App.Game_GetCurrentPlayer()
		bPlayerHasRaceCommand = GetConfigValue("GetWarSimConfig").PlayerHasRaceCommand
		for sShipName in self.lShips:
			pWSShip = WarSimulator.GetWSShipObjForName(sShipName)
			if pWSShip != None:
				fCost = pWSShip.GetTotalCost()
				if pPlayer and pWSShip.Ship and pPlayer.GetObjID() == pWSShip.Ship.GetObjID(): #and bPlayerHasRaceCommand == 1:
					sChosenShip = pPlayer.GetName()
					break
				elif fCost > fShipCost:
					sChosenShip = sShipName
					fShipCost = fCost
		self.leadShip = sChosenShip
		self.Logger.LogString("Lead Ship updated to: "+self.leadShip)
		#####
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_FLEET_UPDATED_LEAD)
		pEvent.SetDestination(WarSimulator.pEventHandler)
		pEvent.SetString(self.GetName())
		App.g_kEventManager.AddEvent(pEvent)
		####
		return
	def AddShip(self, pShip):
		debug(__name__ + ", AddShip")
		if pShip.GetName() in self.lShips:
			return
		if len(self.lShips) >= ShipFleet.iMaxShipsPerFleet:
			return
		if IsStation(pShip) == 1:
			# we dont wanna no stations in the fleet. i think its pretty obvious why...
			return
		sShipRace = GetShipRaceByWarSim(pShip)
		if sShipRace == self.__race or AreRacesAllied(sShipRace, self.__race) == 1:
			self.lShips.append( pShip.GetName() )
			self.dShipsStatus[pShip.GetName()] = ShipFleet.ACTIVE
			self.Logger.LogString("Ship added to the fleet: "+pShip.GetName() +"  (SlotsUsed:"+str(self.GetUnusedShipSlotsNumber())+")" )
			self.UpdateFleetLeadShip()
			if IsPlayer(pShip) == 0:
				ResetShipAI(pShip)
			WarSimulator.AddNewsItem("Fleet", "Ship "+pShip.GetName()+" has joined "+self.GetName())
			#####
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(ET_FLEET_SHIP_ADDED)
			pEvent.SetDestination(pShip)
			pEvent.SetString(self.GetName())
			App.g_kEventManager.AddEvent(pEvent)
			####
			return 1
	def RemoveShip(self, pShip):
		debug(__name__ + ", RemoveShip")
		if pShip.GetName() in self.lShips:
			self.lShips.remove( pShip.GetName() )
			del self.dShipsStatus[pShip.GetName()]
			self.Logger.LogString("Ship removed from the fleet: "+pShip.GetName()+"  (SlotsUsed:"+str(self.GetUnusedShipSlotsNumber())+")")
			self.UpdateFleetLeadShip()
			if not pShip.IsDying() and not pShip.IsDead() and IsPlayer(pShip) == 0:
				ResetShipAI(pShip)
			WarSimulator.AddNewsItem("Fleet", "Ship "+pShip.GetName()+" has left from the "+self.GetName())
			#####
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(ET_FLEET_SHIP_REMOVED)
			pEvent.SetDestination(pShip)
			pEvent.SetString(self.GetName())
			App.g_kEventManager.AddEvent(pEvent)
			####
			if self.GetFleetRegion() == None:
				FleetManager.DeleteFleet(self)
			return 1
	def IsShipInFleet(self, pShip):
		#debug(__name__ + ", IsShipInFleet")
		if not pShip:
			return 0
		return self.IsShipNameInFleet(pShip.GetName())
	def IsShipNameInFleet(self, sShipName):
		#debug(__name__ + ", IsShipNameInFleet")
		if sShipName in self.lShips:
			return 1
		return 0
	def ChangeShipStatusTo(self, pShip, iStatus):
		debug(__name__ + ", ChangeShipStatusTo")
		if pShip.GetName() in self.lShips:
			self.dShipsStatus[pShip.GetName()] = iStatus
			self.Logger.LogString("Ship "+pShip.GetName()+" Status has changed to: "+str(iStatus))
	def ChangeShipNameStatusTo(self, sName, iStatus):
		debug(__name__ + ", ChangeShipNameStatusTo")
		if sName in self.lShips:
			self.dShipsStatus[sName] = iStatus
			self.Logger.LogString("Ship "+sName+" Status has changed to: "+str(iStatus))
	def GetShipStatus(self, pShip):
		debug(__name__ + ", GetShipStatus")
		if self.dShipsStatus.has_key(pShip.GetName()):
			return self.dShipsStatus[pShip.GetName()]
	def GetFleetStatus(self):
		debug(__name__ + ", GetFleetStatus")
		for stat in self.dShipsStatus.values():
			if stat == ShipFleet.ACTIVE:
				return ShipFleet.ACTIVE
		return ShipFleet.IDLE
	def GetFleetRegion(self):
		debug(__name__ + ", GetFleetRegion")
		pWSShip = WarSimulator.GetWSShipObjForName(self.leadShip)
		pRegion = None
		if pWSShip != None:
			pRegion = App.g_kRegionManager.GetRegion( pWSShip.GetRegionAssignedTo() )
		return pRegion
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+str(self.__ID)+">"

# This class handles a ship in the war. She holds values about a ship which matters to make the war simulation, such as region assigned to, orders, 
# total fund cost, race, and more.
class WSShip:
	O_DESTROYED = -5
	O_NOTHING = -1
	O_DEFEND = 0
	O_ATTACK = 1

	pNebCloneRace = None

	def __init__(self, pShip, sRegionName, iOrder):
		debug(__name__ + ", __init__")
		self.CLASS = "WS Ship"
		# ship name is very important for this class since the actual Ship Class instance may change, but the name may remain the same, and if it does
		# it means it is the same ship that has reapered.
		if SavingSystem.IsLoading() == 1:
			self.__ID = GetUniqueID("WSShip_LOADING")
			self.__shipName = ""
			self.__shipClass = ""
			self.Race = None
			self.Ship = None
		elif str(type(pShip)) == str(type("")) and (pShip == "Nebula" or pShip[0:5] == "Clone"):
			self.__ID = GetUniqueID("WSShip_"+pShip)
			self.__shipName = pShip
			self.__shipClass = "Nebula"
			if pShip == "Nebula":
				self.Race = None
			else:
				if WSShip.pNebCloneRace == None:
					import Custom.QBautostart.Libs.Racesclass
					WSShip.pNebCloneRace = Custom.QBautostart.Libs.Racesclass.RaceInfo("Nebula Clone Army")
				self.Race = WSShip.pNebCloneRace
			self.Ship = None
		else:
			self.__ID = GetUniqueID("WSShip_"+pShip.GetName())
			self.__shipName = pShip.GetName()
			self.__shipClass = GetShipType(pShip)
			self.Race = GetRaceClassObj( GetShipRace(pShip) )
			self.Ship = pShip
		self.__order = iOrder
		self.__assignedTo = sRegionName
		self.__isDockedInBase = ""
		self.__occupiedShipName = ""
		self.__stat = "None"
		self.__ISINORR = 0
		self.__startedHandlers = 0
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		self.StartEventHandlers()
	def StartEventHandlers(self):
		debug(__name__ + ", StartEventHandlers")
		if self.__startedHandlers == 1:
			return
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipEnteredSet")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_EXITED_SET, self.pEventHandler, "ShipExitedSet")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(ET_SHIP_NEEDS_REPAIR_AND_RESUPPLY, self.pEventHandler, "ShipISINORRHandler")
		self.__startedHandlers = 1
	def GetShipName(self):
		debug(__name__ + ", GetShipName")
		return self.__shipName
	def GetShipClass(self):
		debug(__name__ + ", GetShipClass")
		return self.__shipClass
	def GetTotalCost(self, bIncludeEscorts = 1):
		# try to make a cost value based on everything. From shields/hull strength/size, to weapons amount/power and maybe some special tech, and
		# possibly allow for external custom functions to be set to modify the cost value.
		# also try to limit the value, something along the lines of 100 (minimum value) to 1,000,000 (maximum)
		# for now only base it on radius
		debug(__name__ + ", GetTotalCost")
		return GetShipFundCost(self.Ship, bIncludeEscorts)
	def SetOrder(self, iOrder):
		# probably needs to do some other checks to see if this can be set as the ship's orders.
		debug(__name__ + ", SetOrder")
		iOldOrder = self.__order
		self.__order = iOrder
		#print "WSShip obj", self.GetShipName(), "order set to", iOrder, "from", iOldOrder
		# send the event
		pEvent = App.TGIntEvent_Create()
		pEvent.SetEventType(ET_SHIP_SET_ORDER)
		pEvent.SetDestination(self.Ship)
		pEvent.SetInt(iOldOrder)
		App.g_kEventManager.AddEvent(pEvent)
	def GetOrder(self):	return self.__order
	def GetRegionAssignedTo(self):	return self.__assignedTo
	def SetRegionAssignedTo(self, sRegionName):
		# probably needs to do some other checks to see if this can be set as the ship's assigned to system, and change apropriate values.
		debug(__name__ + ", SetRegionAssignedTo")
		sOldAssignedTo = self.__assignedTo
		self.__assignedTo = sRegionName
		#print "WSShip obj", self.GetShipName(), "region assigned to set to", sRegionName, "from", sOldAssignedTo
		# send assigned to event
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_SHIP_SET_ASSIGNED_TO_REGION)
		pEvent.SetDestination(self.Ship)
		pEvent.SetString(sOldAssignedTo)
		App.g_kEventManager.AddEvent(pEvent)
	def IsDestroyed(self):
		debug(__name__ + ", IsDestroyed")
		if self.__order == self.O_DESTROYED:
			return 1
		else:
			return 0
	def IsBase(self):
		debug(__name__ + ", IsBase")
		if self.Race == None or self.Ship == None:
			return 0
		lBaseClasses = self.Race.GetBases()
		if self.__shipClass in lBaseClasses:
			return 1
		elif self.Ship.GetShipProperty().IsStationary() == 1:
			return 1
		return 0
	def IsBaseOccupied(self):
		debug(__name__ + ", IsBaseOccupied")
		if self.__occupiedShipName != "":
			return 1
		return 0
	def GetOccupyingShipName(self):
		 debug(__name__ + ", GetOccupyingShipName")
		 return self.__occupiedShipName
	def SetBaseOccupiedByShip(self, pShip):
		debug(__name__ + ", SetBaseOccupiedByShip")
		if self.IsBase() == 0:
			return
		if pShip == None:
			sShipName = self.__occupiedShipName
			self.__occupiedShipName = ""
			if sShipName != "":
				pWSShip = WarSimulator.GetWSShipObjForName(sShipName)
				pWSShip.SetShipDockingInStarbase(None)
			return
		if pShip.GetName() == self.__occupiedShipName:
			return
		pWSShip = WarSimulator.GetWSShipObjForShip(pShip)
		if pWSShip == None:
			return
		if pWSShip.IsBase() == 1:
			return
		self.__occupiedShipName = pShip.GetName()
		pWSShip.SetShipDockingInStarbase(self.Ship)
	def IsShipDocking(self):
		debug(__name__ + ", IsShipDocking")
		if self.__isDockedInBase != "":
			return 1
		return 0
	def GetDockingBaseName(self):
		debug(__name__ + ", GetDockingBaseName")
		return self.__isDockedInBase
	def SetShipDockingInStarbase(self, pStarbase):
		debug(__name__ + ", SetShipDockingInStarbase")
		if self.IsBase() == 1:
			return
		if pStarbase == None:
			sBaseName = self.__isDockedInBase
			self.__isDockedInBase = ""
			if sBaseName != "":
				pWSBase = WarSimulator.GetWSShipObjForName(sBaseName)
				pWSBase.SetBaseOccupiedByShip(None)
			return
		if pStarbase.GetName() == self.__isDockedInBase:
			return
		pWSBase = WarSimulator.GetWSShipObjForShip(pStarbase)
		if pWSBase == None:
			return
		if pWSBase.IsBase() == 0:
			return
		self.__isDockedInBase = pStarbase.GetName()
		pWSBase.SetBaseOccupiedByShip(self.Ship)
	def GetStatusStr(self):
		debug(__name__ + ", GetStatusStr")
		return self.__stat
	def SetStatusStr(self, sMsg):
		debug(__name__ + ", SetStatusStr")
		self.__stat = sMsg
	def IsShipInNeedOfRepairAndResupply(self):
		debug(__name__ + ", IsShipInNeedOfRepairAndResupply")
		return self.__ISINORR

	# CHECK: Entered/Exited Set Handlers probably needs to check if ship is/was travelling...
	def ShipEnteredSet(self, pEvent):
		debug(__name__ + ", ShipEnteredSet")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip == None:
			return
		if pShip.GetName() != self.GetShipName():
			return
		# right ship, do the thing(s)...
		if SavingSystem.IsLoading() == 1 or pShip.GetName() in SavingSystem.lIgnoreEnteredSet:
			SavingSystem.lIgnoreEnteredSet.remove(pShip.GetName())
			return
		if App.g_kTravelManager.IsShipTravelling(pShip) == 1:
			return
		pSet = pShip.GetContainingSet()
		if pSet == None:
			return
		pRegion = pSet.GetRegion()
		if pRegion == None:
			return
		self.UpdateShipAllegiance()
		if self.Race != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet == None:
				# ship doesn't have a fleet, probably has just been created. Find one or create one for it.
				pFleet = FleetManager.FindFleetToEnterIn(pRegion.GetName(), self.Race.GetRaceName() )
				if pFleet == None:
					FleetManager.CreateFleet(pShip)
				else:
					pFleet.AddShip(pShip)
			elif pFleet != None:
				# ship already has a fleet. If we're leading and we have another allied fleet in the region, try to merge fleets together.
				if pFleet.GetLeadShipName() == self.GetShipName():
					lAlliedFleets = FleetManager.GetAlliedFleetsInRegion(pRegion.GetName(), self.Race.GetRaceName() )
					if pFleet.GetFleetRegion() != None:
						if pFleet.GetFleetRegion().GetName() != pRegion.GetName():
							lAlliedFleets.append(pFleet)
					if len(lAlliedFleets) >= 2:
						# HERE!  TRY TO MERGE FLEETS TOGETHER
						FleetManager.TryToMergeFleets(lAlliedFleets)
			pRegion.RegionBattle.AddShipToBattle(pShip)
	def ShipExitedSet(self, pEvent):
		debug(__name__ + ", ShipExitedSet")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip == None:
			return
		if pShip.GetName() != self.GetShipName():
			return
		# right ship, do the thing(s)...
		if SavingSystem.IsLoading() == 1 or pShip.GetName() in SavingSystem.lIgnoreExitedSet:
			SavingSystem.lIgnoreExitedSet.remove(pShip.GetName())
			return
		sExitedSetName = pEvent.GetCString()
		pSet = App.g_kSetManager.GetSet(sExitedSetName)
		if pSet == None:
			return
		pRegion = pSet.GetRegion()
		if pRegion == None:
			return
		pRegion.RegionBattle.RemoveShipFromBattle(pShip)
	def ShipISINORRHandler(self, pEvent):
		debug(__name__ + ", ShipISINORRHandler")
		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip == None:
			return
		if pShip.GetName() != self.GetShipName():
			return
		self.__ISINORR = pEvent.GetInt()

	def UpdateShipAllegiance(self):
		#check if we need to update this ship's allegiance (based on race relative to player), and if we do, do it and reset her AI.
		debug(__name__ + ", UpdateShipAllegiance")
		sPlayerRace = GetShipRaceByWarSim( App.Game_GetCurrentPlayer() )
		if GetRaceClassObj(sPlayerRace) == None or self.Ship == None or self.Race == None:
			return
		pFriendlies = MissionLib.GetFriendlyGroup()
		pNeutrals = MissionLib.GetNeutralGroup()
		pEnemies = MissionLib.GetEnemyGroup()

		bResetAI = 1
		if AreRacesAllied(sPlayerRace, self.Race.GetRaceName()) == 1 or sPlayerRace == self.Race.GetRaceName():
			sNewAllegiance = "Friendly"
		elif AreRacesEnemies(sPlayerRace, self.Race.GetRaceName()) == 1:
			sNewAllegiance = "Enemy"
		else:
			sNewAllegiance = "Neutral"

		if pEnemies.IsNameInGroup(self.Ship.GetName()):
			if sNewAllegiance != "Enemy":
				pEnemies.RemoveName(self.Ship.GetName())
			else:
				bResetAI = 0
		elif pFriendlies.IsNameInGroup(self.Ship.GetName()):
			if sNewAllegiance != "Friendly":
				pFriendlies.RemoveName(self.Ship.GetName())
			else:
				bResetAI = 0
		elif pNeutrals.IsNameInGroup(self.Ship.GetName()):
			if sNewAllegiance != "Neutral":
				pNeutrals.RemoveName(self.Ship.GetName())
			else:
				bResetAI = 0

		if bResetAI == 1:
			if sNewAllegiance == "Friendly":
				pFriendlies.AddName(self.Ship.GetName())
			elif sNewAllegiance == "Enemy":
				pEnemies.AddName(self.Ship.GetName())
			elif sNewAllegiance == "Neutral":
				pNeutrals.AddName(self.Ship.GetName())
			#print "Reseted Ship", self.Ship.GetName(), "allegiance to", sNewAllegiance
			ResetShipAI(self.Ship)
	def ClearEventHandlers(self):
		debug(__name__ + ", ClearEventHandlers")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_ENTERED_SET, self.pEventHandler, "ShipEnteredSet")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_EXITED_SET, self.pEventHandler, "ShipExitedSet")
		App.g_kEventManager.RemoveBroadcastHandler(ET_SHIP_NEEDS_REPAIR_AND_RESUPPLY, self.pEventHandler, "ShipISINORRHandler")
		self.__startedHandlers = 0
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+str(self.__ID)+">"

# this class handles the battle in a region. The attack/defence forces and etc...
# she's the one which checks which side wins, and update the game accordingly.
class RegionBattle:
	lBattleList = []
	iRDF_ReinShipLimit = 15

	NOT_IN_BATTLE = 0
	DEFENCE_FORCE = 1
	ATTACK_FORCE = 2

	def __init__(self, pRegion):
		debug(__name__ + ", __init__")
		self.CLASS = "Region Battle"
		self.__ID = GetUniqueID("RegionBattle_"+pRegion.GetName())
		self.__region = pRegion
		self.__RDF = None
		self.__RAF = None
		self.__battleOn = 0
		# both of the below dicts are "ship name" = WSShip
		self.__defenceForce = {}
		self.__attackForce = {}
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		self.__conquerTimer = None
		RegionBattle.lBattleList.append(self)
	def GetRegionName(self):
		debug(__name__ + ", GetRegionName")
		return self.__region.GetName()
	def GetRegionID(self):
		debug(__name__ + ", GetRegionID")
		return self.__region.GetObjID()
	def IsBattleOn(self):
		debug(__name__ + ", IsBattleOn")
		return self.__battleOn
	def IsConquerTimerOn(self):
		debug(__name__ + ", IsConquerTimerOn")
		if self.__conquerTimer != None:
			return 1
		return 0
	def CanShipJoinBattle(self, pShip):
		debug(__name__ + ", CanShipJoinBattle")
		sEmpire = self.__region.GetControllingEmpire()
		if sEmpire == "Unknown" or sEmpire == "None":
			return 0
		if GetShipRaceByWarSim(pShip) == sEmpire:
			return 1
		elif IsShipEnemyOfRace(pShip, sEmpire) == 1:
			return 1
		elif IsShipFriendlyOfRace(pShip, sEmpire) == 1:
			return 1
		else:
			return 0
	def IsShipInBattle(self, pShip):
		debug(__name__ + ", IsShipInBattle")
		if self.__defenceForce.has_key(pShip.GetName()):
			return self.DEFENCE_FORCE
		if self.__attackForce.has_key(pShip.GetName()):
			return self.ATTACK_FORCE
		return self.NOT_IN_BATTLE
	def IsShipInAttackForce(self, pShip):
		debug(__name__ + ", IsShipInAttackForce")
		if self.__attackForce.has_key(pShip.GetName()):
			return 1
		return 0
	def IsShipInDefenceForce(self, pShip):
		debug(__name__ + ", IsShipInDefenceForce")
		if self.__defenceForce.has_key(pShip.GetName()):
			return 1
		return 0
	def GetAllShipsInAttackForce(self):
		debug(__name__ + ", GetAllShipsInAttackForce")
		return self.__attackForce.keys()
	def GetAllShipsInDefenceForce(self):
		debug(__name__ + ", GetAllShipsInDefenceForce")
		return self.__defenceForce.keys()
	def GetTimeLeftForTimer(self):
		debug(__name__ + ", GetTimeLeftForTimer")
		if self.__conquerTimer != None:
			fCurrentTime = time.clock()
			fStart = self.__conquerTimer.GetTimerStart()
			return fStart - fCurrentTime
		return 0.0
	def AddShipToBattle(self, pShip):
		debug(__name__ + ", AddShipToBattle")
		pWSShip = WarSimulator.GetWSShipObjForShip(pShip)
		if pWSShip == None or self.IsShipInBattle(pShip) != self.NOT_IN_BATTLE:
			return
		if self.CanShipJoinBattle(pShip) == 0:
			pWSShip.SetOrder(pWSShip.O_NOTHING)
			pWSShip.SetRegionAssignedTo( self.__region.GetName() )
			return
		
		bShipEntered = 0
		sEmpire = self.__region.GetControllingEmpire()
		if IsShipEnemyOfRace(pShip, sEmpire) == 1:
			self.__attackForce[pShip.GetName()] = pWSShip
			bShipEntered = 1
			pWSShip.SetOrder(pWSShip.O_ATTACK)
			pWSShip.SetRegionAssignedTo( self.__region.GetName() )
			if IsPlayer(pShip) == 1:
				ShowTextBanner("Entered "+self.__region.GetName()+"\'s Attack Force", 0.5, 0.72, 5.0, 14, 1, 0)
			#print "Ship", pShip.GetName(), "entered the attack force of system", self.__region.GetName()
			WarSimulator.AddNewsItem("Region", "Ship "+pWSShip.GetShipName()+" entered "+self.__region.GetName()+" attack force.")
			if self.__battleOn == 0:
				self.__battleOn = 1
				WarSimulator.AddNewsItem("Region", "A battle at "+self.__region.GetName()+" has started.")
				self.__callRDF()
				if len(self.__defenceForce.keys()) <= 0:
					# wait 2.0 minutes for defence forces...
					self.__conquerTimer = CreateMethodTimer(self.pEventHandler, "_conquerTimerVictory", App.g_kUtopiaModule.GetGameTime()+120.0)
					#print "Conquer timer of system", self.__region.GetName(), "has been initiated."
				### text banner for the player...
				pPlayer = App.Game_GetCurrentPlayer()
				if IsPlayer(pShip) == 1:
					if WarSimulator.GetPlayerLeadsAttack() == 1:
						self.CallRAFofRace(GetShipRaceByWarSim(pPlayer), 0.01)
				if pPlayer != None:
					bPlayerIsAllied = 0
					if GetShipRaceByWarSim(pPlayer) == sEmpire or IsShipFriendlyOfRace(pPlayer, sEmpire) == 1:
						bPlayerIsAllied = 1
					##
					if self.__defenceForce.has_key(pPlayer.GetName()) == 0 and bPlayerIsAllied == 1:
						ShowTextBanner(self.__region.GetName()+" is under attack Captain! They need your help!", 0.5, 0.2, 5.0, 14, 1, 0)
					elif self.__defenceForce.has_key(pPlayer.GetName()) == 1 and bPlayerIsAllied == 1:
						ShowTextBanner("Defend this system Captain!", 0.5, 0.2, 5.0, 14, 1, 0)
					elif self.__attackForce.has_key(pPlayer.GetName()) == 1 and bPlayerIsAllied == 0:
						ShowTextBanner("Battle stations! We are going to fight for this system!!", 0.5, 0.2, 5.0, 13, 1, 0)
					elif self.__attackForce.has_key(pPlayer.GetName()) == 0 and bPlayerIsAllied == 0:
						ShowTextBanner("Enemy system "+self.__region.GetName()+" is under attack Captain!", 0.5, 0.2, 5.0, 13, 1, 0)
				### send battle started event
				pEvent = App.TGStringEvent_Create()
				pEvent.SetEventType(ET_BATTLE_STARTED)
				pEvent.SetDestination(self.pEventHandler)
				pEvent.SetString(pShip.GetName())
				App.g_kEventManager.AddEvent(pEvent)
				WarSimulator.dStats["TotalBattlesOccured"] = WarSimulator.dStats["TotalBattlesOccured"] + 1
				#####
		elif IsShipFriendlyOfRace(pShip, sEmpire) == 1 or GetShipRaceByWarSim(pShip) == sEmpire:
			self.__defenceForce[pShip.GetName()] = pWSShip
			bShipEntered = 1
			pWSShip.SetOrder(pWSShip.O_DEFEND)
			pWSShip.SetRegionAssignedTo( self.__region.GetName() )
			if IsPlayer(pShip) == 1:
				ShowTextBanner("Entered "+self.__region.GetName()+"\'s Defence Force", 0.5, 0.72, 5.0, 14, 1, 0)
			#print "Ship", pShip.GetName(), "entered the defence force of system", self.__region.GetName()
			WarSimulator.AddNewsItem("Region", "Ship "+pWSShip.GetShipName()+" entered "+self.__region.GetName()+" defence force.")
			if self.__battleOn == 1 and self.__conquerTimer != None:
				try:
					App.g_kTimerManager.DeleteTimer(self.__conquerTimer.GetObjID())
				except AttributeError:
					pass
				self.__conquerTimer = None
				#print "Conquer timer of system", self.__region.GetName(), "has been cancelled."
		if bShipEntered == 1:
			# if ship entered, send the event saying so
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(ET_BATTLE_SHIP_ADDED)
			pEvent.SetDestination(self.pEventHandler)
			pEvent.SetString(pShip.GetName())
			App.g_kEventManager.AddEvent(pEvent)
			pPlayer = App.Game_GetCurrentPlayer()
			if pPlayer != None and pPlayer.GetObjID() == pShip.GetObjID() and self.__battleOn == 1 and self.IsShipInBattle(pPlayer) != self.NOT_IN_BATTLE:
				WarSimulator.dStats["BattlesParticipated"] = WarSimulator.dStats["BattlesParticipated"] + 1
	def RemoveShipFromBattle(self, pShip):
		debug(__name__ + ", RemoveShipFromBattle")
		pWSShip = WarSimulator.GetWSShipObjForShip(pShip)
		if pWSShip == None:
			return
		if self.IsShipInBattle(pShip) == self.NOT_IN_BATTLE:
			return
		if self.__defenceForce.has_key(pShip.GetName()):
			del self.__defenceForce[pShip.GetName()]
			if IsPlayer(pShip) == 1:
				ShowTextBanner("Left "+self.__region.GetName()+"\'s Defence Force...", 0.5, 0.7, 5.0, 14, 1, 0)
		if self.__attackForce.has_key(pShip.GetName()):
			del self.__attackForce[pShip.GetName()]
			if IsPlayer(pShip) == 1:
				ShowTextBanner("Left "+self.__region.GetName()+"\'s Attack Force...", 0.5, 0.7, 5.0, 14, 1, 0)
		
		pWSShip.SetOrder(pWSShip.O_NOTHING)
		pWSShip.SetRegionAssignedTo( "None" )
		#print "Ship", pShip.GetName(), "has been removed from battle of system", self.__region.GetName()
		WarSimulator.AddNewsItem("Region", "Ship "+pWSShip.GetShipName()+" has left the battle at "+self.__region.GetName()+".")
		###
		# send our ship removed event
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_BATTLE_SHIP_REMOVED)
		pEvent.SetDestination(self.pEventHandler)
		pEvent.SetString(pShip.GetName())
		App.g_kEventManager.AddEvent(pEvent)
		#####
		if len(self.__defenceForce.keys()) <= 0 and len(self.__attackForce.keys()) >= 1 and self.__battleOn == 1:
			# ATTACK FORCE VICTORY!
			self.__attackForceVictory()
		if len(self.__attackForce.keys()) <= 0 and len(self.__defenceForce.keys()) >= 1 and self.__battleOn == 1:
			# DEFENCE FORCE STANDS!
			self.__defenceForceVictory()
	def SwitchShipSides(self):
		# use this function when the attacking force has stood victorious and conquered the region. This funcion will then update this class instance,
		# turning those used-to-be-attacking-ships into the defending force of the newly-conquered system.
		debug(__name__ + ", SwitchShipSides")
		if len(self.__defenceForce.keys()) <= 0 and len(self.__attackForce.keys()) >= 1 and self.__battleOn == 1:
			self.__defenceForce = {}
			for pWSShip in self.__attackForce.values():
				self.__defenceForce[pWSShip.GetShipName()] = pWSShip
				pWSShip.SetOrder(pWSShip.O_DEFEND)
				pWSShip.SetRegionAssignedTo( self.__region.GetName() )
			self.__attackForce = {}
			#print "Ship sides of system", self.__region.GetName(), "have been switched"
	def _conquerTimerVictory(self, pEvent = None):
		debug(__name__ + ", _conquerTimerVictory")
		if self.__battleOn == 1 and len(self.__defenceForce.keys()) <= 0 and len(self.__attackForce.keys()) >= 1:
			#print "Conquer timer victory in system", self.__region.GetName()
			self.__attackForceVictory()
	def __attackForceVictory(self, pEvent = None):
		debug(__name__ + ", __attackForceVictory")
		sOldRace = self.__region.GetControllingEmpire()
		pFleet = None
		for pWSShip in self.__attackForce.values():
			pFleet = FleetManager.GetFleetOfShip(pWSShip.Ship)
			if pFleet != None:
				break
		if pFleet != None:
			sNewRaceName = pFleet.GetMainRace()		
		else:
			sNewRaceName = GetShipRaceByWarSim(self.__attackForce.values()[0])
		###
		# before changing the controllimg empire, just warn the player.
		pPlayer = App.Game_GetCurrentPlayer()

		pEnemyRaceObj = GetRaceClassObj(sOldRace)


		if pPlayer != None:
			if self.__attackForce.has_key(pPlayer.GetName()):
				ShowTextBanner( self.__getRandomPlaVictStr(), 0.5, 0.23, 5.0, 14, 1, 0)
				WarSimulator.PlayBattleEndedSound()
				WarSimulator.dStats["SystemsConquered"] = WarSimulator.dStats["SystemsConquered"] + 1
				if pEnemyRaceObj != None and len(pEnemyRaceObj.GetSystems()) <= 1:
					WarSimulator.dStats["RacesDefeated"] = WarSimulator.dStats["RacesDefeated"] + 1
			elif GetShipRaceByWarSim(pPlayer) == sNewRaceName:
				ShowTextBanner("Our forces have conquered "+self.__region.GetName()+"!", 0.5, 0.23, 5.0, 13, 1, 0)
				WarSimulator.dStats["SystemsConquered"] = WarSimulator.dStats["SystemsConquered"] + 1
				if pEnemyRaceObj != None and len(pEnemyRaceObj.GetSystems()) <= 1:
					WarSimulator.dStats["RacesDefeated"] = WarSimulator.dStats["RacesDefeated"] + 1
			else:
				if IsShipFriendlyOfRace(pPlayer, sNewRaceName) == 1:
					ShowTextBanner("Allied "+sNewRaceName+" forces have conquered "+self.__region.GetName()+"!", 0.5, 0.23, 5.0, 13, 1, 0)
				elif IsShipEnemyOfRace(pPlayer, sNewRaceName) == 1:
					ShowTextBanner("Hostile "+sNewRaceName+" forces have conquered "+self.__region.GetName()+"!", 0.5, 0.23, 5.0, 13, 1, 0)
		###
		WarSimulator.ChangeRegionToRace(self.__region, sNewRaceName)
		self.__conquerTimer = None
		#print "Attacking force victory in system ", self.__region.GetName()
		# close and cancel the RAF, but just delete the RDF so that any late defence ships can still come in as a counterattack.
		self.__RDF = None
		if self.__RAF != None:
			self.__RAF.CancelRDF()
			self.__RAF = None
		self.__battleOn = 0
		###
		# send our attack victory event
		pEvent = App.TGStringEvent_Create()
		pEvent.SetEventType(ET_BATTLE_ATTACK_VICTORY)
		pEvent.SetDestination(self.pEventHandler)
		pEvent.SetString(sOldRace)
		App.g_kEventManager.AddEvent(pEvent)
	def __defenceForceVictory(self, pEvent = None):
		debug(__name__ + ", __defenceForceVictory")
		fRecoverFunds = 0.0
		for pWSShip in self.__defenceForce.values():
			fRecoverFunds = fRecoverFunds + pWSShip.GetTotalCost()
		if fRecoverFunds > 0.0:
			fRecoverFunds = fRecoverFunds / len(self.__defenceForce.keys())
			pRaceObj = GetRaceClassObj( self.__region.GetControllingEmpire() )
			if pRaceObj != None:
				pRaceObj.AddFunds( fRecoverFunds )
				#print pRaceObj.GetRaceName(), "has recovered", fRecoverFunds, "funds by defending system", self.__region.GetName()
		self.__region.Description = self.__region.Description + "\n-" + self.__region.ControllingEmpire + " successfully defended this region, recovering "+ GetStrFromFloat(fRecoverFunds, 2) + " funds at" + WarSimulator.GetTime()
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			if self.__defenceForce.has_key(pPlayer.GetName()):
				ShowTextBanner( self.__getRandomPlaDefStr(), 0.5, 0.26, 5.0, 14, 1, 0)
				WarSimulator.PlayBattleEndedSound()
				WarSimulator.dStats["SystemsDefended"] = WarSimulator.dStats["SystemsDefended"] + 1
			elif GetShipRaceByWarSim(pPlayer) == self.__region.GetControllingEmpire():
				ShowTextBanner(self.__region.GetName()+" defence stands victorious!", 0.5, 0.26, 5.0, 13, 1, 0)
				WarSimulator.dStats["SystemsDefended"] = WarSimulator.dStats["SystemsDefended"] + 1
			else:
				sEmpire = self.__region.GetControllingEmpire()
				if IsShipFriendlyOfRace(pPlayer, sEmpire) == 1:
					ShowTextBanner("Allied "+sEmpire+" forces have defended "+self.__region.GetName()+"!", 0.5, 0.26, 5.0, 13, 1, 0)
				elif IsShipEnemyOfRace(pPlayer, sEmpire) == 1:
					ShowTextBanner("Hostile "+sEmpire+" forces have defended "+self.__region.GetName()+"!", 0.5, 0.26, 5.0, 13, 1, 0)
		# close and cancel possible existing RDF, and just delete the RAF, so that any late attacking ships can still come in.
		if self.__RDF != None:
			self.__RDF.CancelRDF()
			self.__RDF = None
		self.__RAF = None
		self.__battleOn = 0
		#print "Defence force victory in system ", self.__region.GetName()
		WarSimulator.AddNewsItem("Region", self.__region.GetName()+" was succesfully defended.")
		###
		# send our defence victory event
		pEvent = App.TGFloatEvent_Create()
		pEvent.SetEventType(ET_BATTLE_DEFENCE_VICTORY)
		pEvent.SetDestination(self.pEventHandler)
		pEvent.SetFloat(fRecoverFunds)
		App.g_kEventManager.AddEvent(pEvent)
	###########################################################################################
	# callRDF / callRAF :
	# both functions use pratically the same principle and formulas to calculate their stuff. So any changes in one, should be checked to change on
	# the other one.
	def __callRDF(self):
		debug(__name__ + ", __callRDF")
		if self.__RDF != None:
			return
		sEmpire = self.__region.GetControllingEmpire()
		if not self.__region.BorderSet:
			return
		pSet = self.__region.BorderSet.GetSetObj()
		if pSet == None:
			return
		# first we make some checks and maths to see how many ships (or perhaps funds?) this region should receive to defend itself from an attack.
		# they should be divided into 2 parts:
		#   1º:  the initial, default defence, ships. Which should one way or another be there to battle.
		#   2º:  the reinforcements the region will receive from the race's command.
		# note: the 'importance' values are meant to imply importance in the funds unit of measurement :P
		iNumShips = self.__region.GetNumDefensiveShips()
		iMaxNumShips = int(round(GetConfigValue("GetWarSimConfig").MaxInitShips))  #self.__region.iDefShipLimit
		fDefence = self.__region.GetTotalDefaultDefence()
		fInitialImportance = fDefence * 10000.0
		fMaxInitImportance = self.__region.fDefaultDefenceLimit * 10000.0
		if iNumShips > iMaxNumShips:
			iNumShips = iMaxNumShips

		fEconomy = self.__region.GetTotalEconomy()
		fStrategic = self.__region.GetTotalStrategicValue()
		fReinImportance = ( (fEconomy * 9000.0) + (fStrategic * 11000.0) )
		fMaxReinImportance = ( (self.__region.fEconomyLimit * 9000.0) + (self.__region.fStrategicLimit * 11000.0) )
		iMaxReinShips = int(round(GetConfigValue("GetWarSimConfig").MaxReinShips))  #RegionBattle.iRDF_ReinShipLimit
		iNumReinShips = 0
		if fMaxReinImportance > 0.0 and fReinImportance > 0.0:
			# (20*iMaxReinShips)/3.0)  =  (iMaxReinShips - (iMaxReinShips/3)) * 10
			iNumReinShips = int(round(  ((20*iMaxReinShips)/3.0) / (fMaxReinImportance/fReinImportance)  ))
			if iNumReinShips > iMaxReinShips:
				iNumReinShips = iMaxReinShips
		
		# stablish minimal number of ships to come to defend
		if (iNumShips + iNumReinShips) <= 0:
			if App.g_kSystemWrapper.GetRandomNumber(2) == 1:
				iNumShips = App.g_kSystemWrapper.GetRandomNumber(3) + 1
				fInitialImportance = 50000.0 * iNumShips
			else:
				iNumReinShips = App.g_kSystemWrapper.GetRandomNumber(3) + 1
				fReinImportance = 50000.0 * iNumReinShips

		# now we just do a simple check to see if we REALLY gonna need all these ships, in case the system already has some defending ships.
		iCurrentNumShips = len(self.__defenceForce.keys())
		iNumShips = iNumShips - iCurrentNumShips
		if iNumShips <= 0:
			iNumReinShips = iNumReinShips + iNumShips
			iNumShips = 0
			if iNumReinShips <= 0:
				# we got a lot more ships than what we need... no need to call a RDF
				return

		# now we calculate how many reinforcement waves the RDF should have and the time to they appear.
		# The RDF class will take care of choosing appropriate ship types/names based on funds/ships classes/ship names available
		if iNumReinShips >= 1:
			iShipsPerReinWave = self.__getSPWNfor(iNumReinShips)
			iNumOfReins = iNumReinShips/iShipsPerReinWave
		else:
			iShipsPerReinWave = 0
			iNumOfReins = 0

		# Calculate the time the waves will take to arrive. 
		# time for the initial wave (the default defence ships) to arrive should be pretty much very low. So that it seems that those ships were there
		# before the attackers arrive.
		fTimeToEnter = 0.0001
		fTimeToRein = GetRandomFloat() * 105
		
		# make a simple check/decision to see if we'll have allied help.
		bAddAlliedShips = 0
		pRaceObj = GetRaceClassObj(sEmpire)
		if pRaceObj != None:
			if pRaceObj.GetTotalFunds() > 0.0:
				fChance = (-100.0 * (pRaceObj.GetTotalFunds() - (fInitialImportance + fReinImportance))) / pRaceObj.GetTotalFunds()
			else:
				fChance = 200.0
			if App.g_kSystemWrapper.GetRandomNumber(100) <= fChance:
				bAddAlliedShips = 1
		
		# yes include god ships since they'll probably be very expensive to be used :)
		bIncludeGodShips = 1
		# and of course include escorts.
		bIncludeEscorts = 1

		# check for idle allied fleets. Try to get the one that best fits our defence requirements. (perhaps include distance checking)
		# if we can get a fleet, make her warp to our system.
		lAlliedFleets = FleetManager.GetAlliedFleetsOfRace( sEmpire )
		pFleetToCall = None
		sTravelTypeToUse = ""
		fFleetETA = -1.0
		for pFleet in lAlliedFleets:
			if pFleet.GetFleetRegion() == None or pFleet.GetFleetRegion().GetName() == self.__region.GetName():
				#fleet is already on our system, skip it.
				continue
			if pFleet.GetFleetStatus() == ShipFleet.ACTIVE:
				#fleet is active, don't bother it.
				continue
			if pFleet.GetShipCount() > ((iShipsPerReinWave * iNumOfReins) + iNumShips):
				#too many ships for our RDF... Skip this fleet
				continue
			if pFleet.GetFleetTotalCost() > (fInitialImportance + fReinImportance):
				#fleet is too expensive for our RDF... Skip it.
				continue
		
			# check for more things (ETA perhaps)
			# update pFleetToCall if we have a go and break for loop
			pTravel = App.g_kTravelManager.GetTravel( pFleet.GetLeadShipObj() )
			if pTravel != None:
				vWasLoc = pFleet.GetFleetRegion().GetLocation()
				vGoLoc = self.__region.GetLocation()
				vDist = App.NiPoint2(vGoLoc.x - vWasLoc.x, vGoLoc.y - vWasLoc.y)
				iDist = vDist.Length()
				tTTandSpeed = pTravel.GetFastestTTAvailable(1)
				fSpeed = tTTandSpeed[1]
				dWarpValues = Galaxy.GetWarpValues(iDist, fSpeed)	
				fETA = dWarpValues['Time']
				if fETA > 110.0:
					#fleet is going to take to long to arrive, forget it.
					continue

				fFleetETA = fETA
				sTravelTypeToUse = tTTandSpeed[0]
				pFleetToCall = pFleet
				break

		if pFleetToCall != None:
			# make lead ship of fleet travel to this system. deduct cost/ship numbers/etc from RDF settings.
			# if there are no more need for a RDF, don't even call it (the RDF, meaning, finish this method here).
			# -start by engaging travel of lead ship
			pLeadShip = pFleetToCall.GetLeadShipObj()
			pTravel = App.g_kTravelManager.GetTravel(pLeadShip)
			pTravel.SetTravelType( sTravelTypeToUse )
			pTravel.SetSpeed( pTravel.GetActualCruiseSpeed() )
			pTravel.SetDestination( pSet.GetRegionModule() )
			pTravel.Travel()
			WarSimulator.AddNewsItem("Fleet", pFleetToCall.GetName()+" awnsered "+self.__region.GetName()+"\'s distress call (ETA: "+str(fFleetETA)+" secs).")

			#now we deduct cost/shipnumbers/etc and check if we call a RDF or not after all
			iFleetShipNum = pFleetToCall.GetShipCount()
			if iFleetShipNum >= iNumOfReins * iShipsPerReinWave:
				iFleetShipNum = iFleetShipNum - (iNumOfReins * iShipsPerReinWave)
				iNumReinShips = iNumOfReins = iShipsPerReinWave = 0
			else:
				iNumReinShips = iNumOfReins * iShipsPerReinWave
				iNumReinShips = iNumReinShips - iFleetShipNum
				iFleetShipNum = 0
				iShipsPerReinWave = self.__getSPWNfor(iNumReinShips)
				iNumOfReins = iNumReinShips/iShipsPerReinWave
			if iFleetShipNum >= 1:
				iNumShips = iNumShips - iFleetShipNum
				iFleetShipNum = 0

			if (iNumShips + iNumReinShips) <= 0:
				# fleet ship count beats our RDF ship count... don't need to continue with the RDF.
				#print self.__region.GetName(), " called full fleet instead of RDF (by ship count)"
				return
		
			#deduct cost and check if we call a RDF or not after all
			fFleetCost = pFleetToCall.GetFleetTotalCost()
			if fReinImportance > 0:
				fReinImportance = fReinImportance - fFleetCost
				fFleetCost = 0
				if fReinImportance < 0:
					fFleetCost = -fReinImportance
					fReinImportance = 0
			fInitialImportance = fInitialImportance - fFleetCost
			#stablishing 50000.0 as the minimal funds to continue with the RDF. Since chances are, the race(s) won't have many combat ships
			#that cheap, and if the RDF can't find a ship class to create, which normally happens because of cost limitations, problems may occur.
			if (fInitialImportance + fReinImportance) <= 50000.0:  
				# total fleet cost beats our RDF cost... don't need to continue with the RDF.
				#print self.__region.GetName(), " called full fleet instead of RDF (by fleet cost)"
				return

		#print self.__region.GetName(), " called RDF Stats:"
		#print " -Empire:", sEmpire
		#print " -Initial Ship Number:", iNumShips
		#print " -Ships Per Rein Wave:", iShipsPerReinWave
		#print " -Number of Rein Waves:", iNumOfReins
		#print " -Time for a Rein wave:", fTimeToRein
		#print " -Total Rein Ship:", iShipsPerReinWave * iNumOfReins
		#print " -Total Amount of Ships:", (iShipsPerReinWave * iNumOfReins) + iNumShips
		#print " -Add Allied Ships:", bAddAlliedShips
		#print " -Funds for initial ships:", fInitialImportance
		#print " -Funds for reinforcement ships:", fReinImportance
		#print " -Total funds:", fInitialImportance + fReinImportance
		########
		self.__RDF = RandomDefenceForce(sEmpire, iNumShips, iShipsPerReinWave, iNumOfReins, pSet, fTimeToEnter, fTimeToRein, bIncludeGodShips, bIncludeEscorts)
		self.__RDF.SetAsWarSimRDF(fInitialImportance, fReinImportance, bAddAlliedShips)
		WarSimulator.AddNewsItem("Region", self.__region.GetName()+" called a random defence force.")
	def CallRAFofRace(self, sRace, fTimeToStart = -1.0):
		# Just a mask to call our private RAF function. The War Simulator needs this.
		# ADDITIONAL: any kind of checks to see if a RAF can be called here should be done here.
		debug(__name__ + ", CallRAFofRace")
		if sRace != "Unknown" and sRace != "None":
			return self.__callRAFofRace(sRace, fTimeToStart)
		return
	def __callRAFofRace(self, sEmpire, fTimeToStart = -1.0):
		debug(__name__ + ", __callRAFofRace")
		if self.__RAF != None:
			#print "cancelling", sEmpire, "RAF on", self.__region.GetName(), ": RAF already exists"
			return 0
		pSet = self.__region.BorderSet.GetSetObj()
		if pSet == None:
			try:
				pSetModule = __import__(self.__region.BorderSet.GetScriptFile())
				pSetModule.Initialize()
				pSet = pSetModule.GetSet()
			except:
				Galaxy.LogError("RegionBattle_CallRAF: couldn't acquire border set obj")
			if pSet == None:
				#print "cancelling", sEmpire, "RAF on", self.__region.GetName(), ": no border set"
				return 0
		if AreRacesEnemies(sEmpire, self.__region.GetControllingEmpire()) != 1:
			#print "cancelling", sEmpire, "RAF on", self.__region.GetName(), ": races not enemies"
			return 0
		# first we make some checks and maths to see how many ships (and funds) the race should gather up to attack this region 
		# they should be divided into 2 parts:
		#   1º:  the initial attack force ships. Which should be the first ones to arrive in group.
		#   2º:  the reinforcements the attack frce will receive from the race's command.
		# note: the 'importance' values are meant to imply importance in the funds unit of measurement :P
		iNumShips = self.__region.GetNumDefensiveShips()
		iMaxNumShips = int(round(GetConfigValue("GetWarSimConfig").MaxInitShips))  #self.__region.iDefShipLimit
		fDefence = self.__region.GetTotalDefaultDefence()
		fInitialImportance = fDefence * 10000.0
		fMaxInitImportance = self.__region.fDefaultDefenceLimit * 10000.0
		if iNumShips > iMaxNumShips:
			iNumShips = iMaxNumShips

		fEconomy = self.__region.GetTotalEconomy()
		fStrategic = self.__region.GetTotalStrategicValue()
		fReinImportance = ( (fEconomy * 9000.0) + (fStrategic * 11000.0) )
		fMaxReinImportance = ( (self.__region.fEconomyLimit * 9000.0) + (self.__region.fStrategicLimit * 11000.0) )
		iMaxReinShips = int(round(GetConfigValue("GetWarSimConfig").MaxReinShips))  #RegionBattle.iRDF_ReinShipLimit
		iNumReinShips = 0
		if fMaxReinImportance > 0.0 and fReinImportance > 0.0:
			# (20*iMaxReinShips)/3.0)  =  (iMaxReinShips - (iMaxReinShips/3)) * 10
			iNumReinShips = int(round(  ((20*iMaxReinShips)/3.0) / (fMaxReinImportance/fReinImportance)  ))
			if iNumReinShips > iMaxReinShips:
				iNumReinShips = iMaxReinShips
		
		# stablish minimal number of ships to come in the attack
		if (iNumShips + iNumReinShips) <= 0:
			iNumShips = App.g_kSystemWrapper.GetRandomNumber(3) + 1
			fInitialImportance = 50000.0 * iNumShips

		# now we just do a simple check to see if we REALLY gonna need all these ships, in case the system already has some defending ships.
		iCurrentNumShips = len(self.__attackForce.keys())
		iNumShips = iNumShips - iCurrentNumShips
		if iNumShips <= 0:
			iNumReinShips = iNumReinShips + iNumShips
			iNumShips = 0
			if iNumReinShips <= 0:
				# we got a lot more ships than what we need... no need to call a RAF
				#print "cancelling", sEmpire, "RAF on", self.__region.GetName(), ": more ships than what's needed"
				return 0

		# now we calculate how many reinforcement waves the RAF should have and the time to they appear.
		# The RAF class will take care of choosing appropriate ship types/names based on funds/ships classes/ship names available
		if iNumReinShips >= 1:
			iShipsPerReinWave = self.__getSPWNfor(iNumReinShips)
			iNumOfReins = iNumReinShips/iShipsPerReinWave
		else:
			iShipsPerReinWave = 0
			iNumOfReins = 0

		# Calculate the time the waves will take to arrive.
		if fTimeToStart == -1.0:
			fTimeToEnter = GetRandomInRange(60.0, 300.0)
		else:
			fTimeToEnter = fTimeToStart
		fTimeToRein = GetRandomFloat() * 105
		
		# make a simple check/decision to see if we'll have allied help.
		bAddAlliedShips = 0
		pRaceObj = GetRaceClassObj(sEmpire)
		if pRaceObj != None:
			if pRaceObj.GetTotalFunds() > 0.0:
				fChance = (-100.0 * (pRaceObj.GetTotalFunds() - (fInitialImportance + fReinImportance))) / pRaceObj.GetTotalFunds()
			else:
				fChance = 200.0
			if App.g_kSystemWrapper.GetRandomNumber(100) <= fChance:
				bAddAlliedShips = 1
		
		# yes include god ships since they'll probably be very expensive to be used :)
		bIncludeGodShips = 1
		# and of course include escorts.
		bIncludeEscorts = 1

		# check for idle allied fleets. Try to get the one that best fits our attack requirements. (perhaps include distance checking)
		# if we can get a fleet, make her warp to our system.
		lAlliedFleets = FleetManager.GetAlliedFleetsOfRace( sEmpire )
		pFleetToCall = None
		sTravelTypeToUse = ""
		fFleetETA = -1.0
		for pFleet in lAlliedFleets:
			if pFleet.GetFleetRegion() == None or pFleet.GetFleetRegion().GetName() == self.__region.GetName():
				#fleet is already on our system, skip it.
				continue
			if pFleet.GetFleetStatus() == ShipFleet.ACTIVE:
				#fleet is active, don't bother it.
				continue
			if pFleet.GetShipCount() > ((iShipsPerReinWave * iNumOfReins) + iNumShips):
				#too many ships for our RAF... Skip this fleet
				continue
			if pFleet.GetFleetTotalCost() > (fInitialImportance + fReinImportance):
				#fleet is too expensive for our RAF... Skip it.
				continue
		
			# check for more things (ETA perhaps)
			# update pFleetToCall if we have a go and break for loop
			pTravel = App.g_kTravelManager.GetTravel( pFleet.GetLeadShipObj() )
			if pTravel != None:
				vWasLoc = pFleet.GetFleetRegion().GetLocation()
				vGoLoc = self.__region.GetLocation()
				vDist = App.NiPoint2(vGoLoc.x - vWasLoc.x, vGoLoc.y - vWasLoc.y)
				iDist = vDist.Length()
				tTTandSpeed = pTravel.GetFastestTTAvailable(1)
				fSpeed = tTTandSpeed[1]
				dWarpValues = Galaxy.GetWarpValues(iDist, fSpeed)	
				fETA = dWarpValues['Time']
				if fETA > fTimeToEnter:
					#fleet is going to take to long to arrive, forget it.
					continue

				fFleetETA = fETA
				sTravelTypeToUse = tTTandSpeed[0]
				pFleetToCall = pFleet
				break

		if pFleetToCall != None:
			# make lead ship of fleet travel to this system. deduct cost/ship numbers/etc from RAF settings.
			# if there are no more need for a RAF, don't even call it (the RAF, meaning, finish this method here).
			# -start by engaging travel of lead ship
			pLeadShip = pFleetToCall.GetLeadShipObj()
			pTravel = App.g_kTravelManager.GetTravel(pLeadShip)
			pTravel.SetTravelType( sTravelTypeToUse )
			pTravel.SetSpeed( pTravel.GetActualCruiseSpeed() )
			pTravel.SetDestination( pSet.GetRegionModule() )
			pTravel.Travel()
			WarSimulator.AddNewsItem("Fleet", pFleetToCall.GetName()+" received order to attack "+self.__region.GetName()+" (ETA: "+str(fFleetETA)+" secs).")

			#now we deduct cost/shipnumbers/etc and check if we call a RAF or not after all
			iFleetShipNum = pFleetToCall.GetShipCount()
			if iFleetShipNum >= iNumOfReins * iShipsPerReinWave:
				iFleetShipNum = iFleetShipNum - (iNumOfReins * iShipsPerReinWave)
				iNumReinShips = iNumOfReins = iShipsPerReinWave = 0
			else:
				iNumReinShips = iNumOfReins * iShipsPerReinWave
				iNumReinShips = iNumReinShips - iFleetShipNum
				iFleetShipNum = 0
				iShipsPerReinWave = self.__getSPWNfor(iNumReinShips)
				iNumOfReins = iNumReinShips/iShipsPerReinWave
			if iFleetShipNum >= 1:
				iNumShips = iNumShips - iFleetShipNum
				iFleetShipNum = 0

			if (iNumShips + iNumReinShips) <= 0:
				# fleet ship count beats our RAF ship count... don't need to continue with the RAF.
				#print self.__region.GetName(), " called full fleet instead of RAF (by ship count)"
				return
		
			#deduct cost and check if we call a RAF or not after all
			fFleetCost = pFleetToCall.GetFleetTotalCost()
			if fReinImportance > 0:
				fReinImportance = fReinImportance - fFleetCost
				fFleetCost = 0
				if fReinImportance < 0:
					fFleetCost = -fReinImportance
					fReinImportance = 0
			fInitialImportance = fInitialImportance - fFleetCost
			#stablishing 50000.0 as the minimal funds to continue with the RAF. Since chances are, the race(s) won't have many combat ships
			#that cheap, and if the RAF can't find a ship class to create, which normally happens because of cost limitations, problems may occur.
			if (fInitialImportance + fReinImportance) <= 50000.0:  
				# total fleet cost beats our RAF cost... don't need to continue with the RAF.
				#print self.__region.GetName(), " called full fleet instead of RAF (by fleet cost)"
				return

		#print self.__region.GetName(), " called RAF Stats:"
		#print " -Empire:", sEmpire
		#print " -Initial Ship Number:", iNumShips
		#print " -Ships Per Rein Wave:", iShipsPerReinWave
		#print " -Number of Rein Waves:", iNumOfReins
		#print " -Time for initial attack:", fTimeToEnter
		#print " -Time for a Rein wave:", fTimeToRein
		#print " -Total Rein Ship:", iShipsPerReinWave * iNumOfReins
		#print " -Total Amount of Ships:", (iShipsPerReinWave * iNumOfReins) + iNumShips
		#print " -Add Allied Ships:", bAddAlliedShips
		#print " -Funds for initial ships:", fInitialImportance
		#print " -Funds for reinforcement ships:", fReinImportance
		#print " -Total funds:", fInitialImportance + fReinImportance
		########
		self.__RAF = RandomDefenceForce(sEmpire, iNumShips, iShipsPerReinWave, iNumOfReins, pSet, fTimeToEnter, fTimeToRein, bIncludeGodShips, bIncludeEscorts)
		self.__RAF.SetAsWarSimRDF(fInitialImportance, fReinImportance, bAddAlliedShips)
		WarSimulator.AddNewsItem("Region", sEmpire+" forces are going to attack "+self.__region.GetName()+" ("+self.__region.GetControllingEmpire()+" territory), in approx. "+str(int(fTimeToEnter))+" seconds.")
		return 1
	#############################################################################
	# SPWN = ship-per-wave-number
	# SPWNL =  list of the above
	def __getSPWNfor(self, iNumReinShips, spwnl = [1,2,3,4,5,7]):
		debug(__name__ + ", __getSPWNfor")
		l = []
		if type(spwnl) != type([]):
			spwnl = [1, 2, 3, 4, 5, 7]
			#print "SPWNL was set again..."
		#print "SPWN Num Rein Ships:", iNumReinShips
		for iShipsPerWave in spwnl:
			#print "SPWN  ShipPerWave:", iShipsPerWave,  "(", float(iShipsPerWave),")"
			fFac = iNumReinShips/float(iShipsPerWave)
			iNumOfReins = int(round(fFac+0.4))
			iShipDiff = int( (iNumReinShips * (iNumOfReins - fFac))+0.4 )
	
			iTotal = (iNumOfReins*iShipsPerWave)-iShipDiff
			if iTotal == iNumReinShips:
				l.append( iShipsPerWave )
		index = l[int(len(l)/2)]
		return index
	def __getRandomPlaVictStr(self):
		debug(__name__ + ", __getRandomPlaVictStr")
		lStrList = ["We conquered this system!",
			"This system is ours!",
			"Another territory for the empire!",
			"We achieved victory!",
			"Unstoppable onslaught!",
			"Region conquered!",
			"Superb fight Captain!",
			"This was not our day to die!",
			"Hoorah!",
			"They didn't stand a chance!",
			"We did it again!",
			"We got'em good!",
			"Jackpot!!"]
		index = App.g_kSystemWrapper.GetRandomNumber( len(lStrList) )
		return lStrList[index]
	def __getRandomPlaDefStr(self):
		debug(__name__ + ", __getRandomPlaDefStr")
		lStrList = ["Our defence stands victorious!",
			"They can't beat us!",
			"THIS. IS. SPARTA!",
			"We succesfully defended this system.",
			"This system is saved, for now.",
			"Unbreakable defence!",
			"Now they'll think twice before doing that!",
			"Our hope and guns prevails!",
			"This system is still ours!",
			"Great work Captain!",
			"We retained this region in our control!",
			"We pushed them away from here!"]
		index = App.g_kSystemWrapper.GetRandomNumber( len(lStrList) )
		return lStrList[index]
	def IsPlayerInBattle(self):
		debug(__name__ + ", IsPlayerInBattle")
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			return self.IsShipInBattle(pPlayer)
		return self.NOT_IN_BATTLE
	def GetObjID(self):
		debug(__name__ + ", GetObjID")
		l = string.split(self.__ID, "_")
		return l[len(l)-1]
	def __repr__(self):
		debug(__name__ + ", __repr__")
		return "<"+str(self.__ID)+">"


###############################################
# HELPERS  FUNCTIONS
##############################################
def IsPlayer(pShip):
	debug(__name__ + ", IsPlayer")
	pPlayer = App.Game_GetCurrentPlayer()
	if pPlayer != None and pShip != None:
		if pPlayer.GetObjID() == pShip.GetObjID():
			return 1
	return 0

def GetRegionDestination(pDest):
	debug(__name__ + ", GetRegionDestination")
	for pRegion in App.g_kRegionManager.GetAllRegions():
		if pRegion.RegionBattle.pEventHandler.GetObjID() == pDest.GetObjID():
			return pRegion

def GetRegionBattleDestination(pDest):
	debug(__name__ + ", GetRegionBattleDestination")
	for pRegion in App.g_kRegionManager.GetAllRegions():
		if pRegion.RegionBattle.pEventHandler.GetObjID() == pDest.GetObjID():
			return pRegion.RegionBattle

def GetWarSimulatorDestination(pDest):
	debug(__name__ + ", GetWarSimulatorDestination")
	if WarSimulator.pEventHandler != None:
		if pWarSimulator.pEventHandler.GetObjID() == pDest.GetObjID():
			return WarSimulator

def GetRealDestinationObj(pDest):
	debug(__name__ + ", GetRealDestinationObj")
	if GetRegionDestination(pDest) != None:
		return GetRegionDestination(pDest)
	if GetRegionBattleDestination(pDest) != None:
		return GetRegionBattleDestination(pDest)
	if GetWarSimulatorDestination(pDest) != None:
		return GetWarSimulatorDestination(pDest)

def IsBattleHappening():
	debug(__name__ + ", IsBattleHappening")
	for pRB in RegionBattle.lBattleList:
		if pRB.__dict__["_RegionBattle__battleOn"] == 1:
			return 1
	return 0

#override: ShipDestroyed function from QuickBattle.py
import QuickBattle.QuickBattle
QBShipDestroyed_Original = QuickBattle.QuickBattle.ShipDestroyed
def QBShipDestroyed_Override(pObject, pEvent):
	debug(__name__ + ", QBShipDestroyed_Override")
	pPlayer = App.Game_GetCurrentGame().GetPlayer()
	pShip = App.ShipClass_Cast(pEvent.GetDestination())
	if pShip == None:
		return
	#let QB handle Ship Destroyed events as usual, unless it is the player being destroyed and War Sim is on
	#in that case, we'll let the War Sim do its specific stuff to handle the player's death.
	if pPlayer and pShip.GetName() == pPlayer.GetName() and WarSimulator.IsInitialized() == 1:
		#player was destroyed and WarSim is on. Override QB handling here, and our own consequences.
		#print "GC WarSim: overriding QB ship destroyed handler: Player was destroyed"
		sPlaName = pPlayer.GetName()
		pWSPla = WarSimulator.GetWSShipObjForShip(pPlayer)

		pSet = pPlayer.GetContainingSet()
		pPlayer.SetDead()
		pCurrentRegion = None
		if pSet:
			pSet.DeleteObjectFromSet(sPlaName)
			pCurrentRegion = pSet.GetRegion()

		# If we are not in a battle, recreate the player in the same set. Otherwise, recreate it in the closest allied set or closest neutral set
		# incase we have no allied sets.
		if pCurrentRegion != None and pCurrentRegion.RegionBattle.IsBattleOn() == 0:
			pass
		else:
			fClosestDist = 1e+10
			pClosestRegion = None
			iClosestAllegiance = 0
			lRegions = App.g_kRegionManager.GetAllRegions()
			for pRegion in lRegions:
				sEmpire = pRegion.GetControllingEmpire()
				sPlaRace = pWSPla.Race.GetRaceName()
				if sEmpire == "Unknown" or sEmpire == "None" or sPlaRace == "Unknown" or sPlaRace == "None":
					iAllegiance = 1 #Neutral
				elif sPlaRace == sEmpire or AreRacesAllied(sPlaRace, sEmpire) == 1:
					iAllegiance = 2 #Friendly
				elif AreRacesEnemies(sPlaRace, sEmpire) == 1:
					iAllegiance = 0 #Hostile
				else:
					iAllegiance = 1 #Neutral
				if pCurrentRegion != None and pRegion.GetName() != pCurrentRegion.GetName():
					if iAllegiance > iClosestAllegiance or iAllegiance == 2:
						vInLoc = pCurrentRegion.GetLocation()
						vGoLoc = pRegion.GetLocation()
						fDist = 1e+10
						if vInLoc != "DEFAULT" and vGoLoc != "DEFAULT":
							vDist = App.NiPoint2(vGoLoc.x - vInLoc.x, vGoLoc.y - vInLoc.y)
							fDist = vDist.Length()
						if fDist < fClosestDist:
							#closer region acquired, update 'closest' variables.
							fClosestDist = fDist
							pClosestRegion = pRegion
							iClosestAllegiance = iAllegiance
				elif pCurrentRegion == None:
					if iAllegiance > iClosestAllegiance or iAllegiance == 2:
						#just grab any neutral or allied system... without the region the player died, we can't do much here...
						pClosestRegion = pRegion
						iClosestAllegiance = iAllegiance
			if pClosestRegion != None:
				pBorderSet = pClosestRegion.GetBorderSet()
				pSet = pBorderSet.GetSetObj(1)

		pNewPlayer = MissionLib.CreatePlayerShip(pWSPla.GetShipClass(), pSet, sPlaName, "")
		if not pNewPlayer:
			pNewPlayer = MissionLib.GetShip(sPlaName)
			if not pNewPlayer:
				#print "QuickBattle RecreatePlayer (at GC War Sim): Something bad happened"
				return

		# Reposition the ship...
		iRandomValue = 500
		kLocation = App.TGPoint3()
		X = GetRandomInRange(-iRandomValue, iRandomValue)
		Y = GetRandomInRange(-iRandomValue, iRandomValue)
		Z = GetRandomInRange(-iRandomValue, iRandomValue)
		kLocation.SetXYZ(X, Y, Z)
		i = 0
		while ( pSet.IsLocationEmptyTG(kLocation, pNewPlayer.GetRadius()*2, 1) == 0):
			X = GetRandomInRange(-iRandomValue, iRandomValue)
			Y = GetRandomInRange(-iRandomValue, iRandomValue)
			Z = GetRandomInRange(-iRandomValue, iRandomValue)
			kLocation.SetXYZ(X, Y, Z)
			i = i + 1
			if i == 10:
				i = 0
				iRandomValue = iRandomValue + 500
		pNewPlayer.SetTranslate(kLocation)

		# Update the ship with its new positional information...
		pNewPlayer.UpdateNodeOnly()

		# update the proximity manager with this object's new position.
		pProximityManager = pSet.GetProximityManager()
		if pProximityManager:
			pProximityManager.UpdateObject (pNewPlayer)

		pTopWindow = App.TopWindow_GetTopWindow()
		pTopWindow.ForceBridgeVisible()
		# Need to reset interactive mode, otherwise you'll get stuck if you go
		# to this mode.
		pCinematic = App.CinematicWindow_Cast(pTopWindow.FindMainWindow(App.MWT_CINEMATIC))
		if pCinematic:
			pCinematic.SetInteractive(1)
		pNewPlayer.SetTarget(None)
		#print "GC WarSim: finished handling Player ship destroyed event"
	else:
		try:
			QBShipDestroyed_Original(pObject, pEvent)
		except:
			Galaxy.LogError("QBShipDestroyed_Override")
