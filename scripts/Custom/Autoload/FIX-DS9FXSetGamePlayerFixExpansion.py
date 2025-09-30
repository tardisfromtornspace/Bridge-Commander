# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# This file is an unofficial patch made by CharaToLoki (Alex SL Gato) for DS9FX that is ALL Rights Reserved by USS Sovereign, with the aim of this patch meant to extend the "SetGamePlayerFix" DS9FXLib file in order to extend "Transporter fix" functionality to also cover certain transporter issues.
# The only code I own from this patch would fall under the LGPL license, but excluding the patch itself and patch conditions and fixes, the rest of the code is pretty much Sovereign's, so as always, ask permission first!
# 30th September 2025
# By Alex SL Gato, with permission from Sov

import App
from bcdebug import debug
import traceback

needUpdate = 0
patchDone = 0
scriptToPatch = None
sDS9FXVersionSignature = None
sDS9FXSavedConfig = None
toPatchPath = "Custom.DS9FX"
DS9FXVersionPath = "DS9FXVersionSignature"
DS9FXMutFuncPath = "DS9FXMutatorFunctions"
DS9FXFileToPatch = "DS9FXLib.SetGamePlayerFix"
DS9FXSavedConfigPath = "Custom.UnifiedMainMenu.ConfigModules.Options.SavedConfigs.DS9FXSavedConfig"
sepPath = "."

VERSION = 20250930
try:
	try:
		sDS9FXVersionSignature = __import__(toPatchPath + sepPath + DS9FXVersionPath)
	except:
		sDS9FXVersionSignature = None
		traceback.print_exc()

	if sDS9FXVersionSignature:
		if hasattr(sDS9FXVersionSignature,"DS9FXVersionNumber"): # Newer versions of DS9FX
			if sDS9FXVersionSignature.DS9FXVersionNumber == "1.0" or sDS9FXVersionSignature.DS9FXVersionNumber == "1.1":
				needUpdate = 1
			else :
				needUpdate = 0

		else: # Older versions of DS9FX f.ex. 1.0 may not have a version number (i.e. the one on KM, "Xtended")
			if hasattr(sDS9FXVersionSignature, "DS9FXVersion"):
				needUpdate = 1
			else :
				needUpdate = 0 # I don't know what kind of script you have, but it's probably not any DS9FX we know of...

	try:
		scriptToPatch = __import__(toPatchPath + sepPath + DS9FXFileToPatch)
	except:
		scriptToPatch = None
		traceback.print_exc()
except:
	traceback.print_exc()


if needUpdate and scriptToPatch and hasattr(scriptToPatch, "Fix") and hasattr(scriptToPatch, "FixTransportingBug") and hasattr(scriptToPatch, "ResetList") and hasattr(scriptToPatch, "bEnabled") and hasattr(scriptToPatch, "lPlayerIDs"): # We check that those vital functions we modify exist...

	try:
		# Old functions
		origFix = scriptToPatch.Fix
		origFixTransportingBug = scriptToPatch.FixTransportingBug
		origResetList = scriptToPatch.ResetList

		# Extra imports
		import MissionLib

		try:
			sDS9FXSavedConfig = __import__(DS9FXSavedConfigPath)
		except:
			sDS9FXSavedConfig = None
			traceback.print_exc()

		# Vars
		#scriptToPatch.bEnabled = 1
		#scriptToPatch.lPlayerIDs = []
		g_pID = None # New global variable
		g_pSet = None # New global variable


		# Events
		#ET_DUMMY = App.UtopiaModule_GetNextEventType()

		# Functions
		def NewFix(pAction, mustFixBad = 0, pPlayer = None): # This script got modified in multiple points to provide the fix and better error detection.

			if mustFixBad:
				pPlayer = quicklyReAddMissingSetting(None, None, 1)

			try:
				origFix(pAction)
			except:
				# If we are here, it means we somehow got an issue from pTacWeaponsCtrl, which prevented us from calling oPlayerChecking... so we must do that
				print __name__, " NewFix: we somehow got an issue while calling origFix"
				traceback.print_exc()
				try:
					# Fake an event
					if pPlayer == None:
						pPlayer = MissionLib.GetPlayer()
					pEvent = App.TGEvent_Create()
					pEvent.SetEventType(scriptToPatch.ET_DUMMY)
					pEvent.SetDestination(pPlayer)
					App.g_kEventManager.AddEvent(pEvent)		
					from Custom.Autoload import ReSet
					if ReSet.mode.IsEnabled():
						ReSet.oPlayerChecking.__call__(None, pEvent)
				except:
					print __name__, " NewFix: Error while faking an event"
					traceback.print_exc()

			return 0

		#def ResetList(): 
		#	#global scriptToPatch.lPlayerIDs
		#	scriptToPatch.lPlayerIDs = []


		def isInList(item, list=None): # Made the calls a bit more abstracted from the list
			result = 0
			if list != None:
				result = (item in list)
			else:
				result = (item in scriptToPatch.lPlayerIDs)
			return result


		def appendOtherShips(liShipIDs): # Made the calls a bit more abstracted from the list
			for iShipID in liShipIDs:
				if iShipID != None and iShipID != App.NULL_ID:
					scriptToPatch.lPlayerIDs.append(iShipID)


		def killOtherShips(liShipIDs, pcName): # This function works mostly for single-player campaign, to clear the other pShips in a way that works for us... basically kill'em.
			if not App.g_kUtopiaModule.IsMultiplayer():
				for iShipID in scriptToPatch.lPlayerIDs:
					if iShipID != None and not isInList(iShipID, liShipIDs):
						try:
							pSacrifice = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), iShipID)
							if pSacrifice:
								pSet = pSacrifice.GetContainingSet()
								pSacrifice.SetDead()
								myName = pSacrifice.GetName()
								if pSet and pcName != pSacrifice.GetName(): # Because curiously enough it is in fact possible to have two ships with same name on certain circumstances
									pSet.DeleteObjectFromSet(myName)
						except:
							traceback.print_exc()

				scriptToPatch.ResetList()
				appendOtherShips(liShipIDs)

			return 0


		def quicklyReAddMissingSetting(pShip, pSet, itsPlayerTime = 0): # New function to execute most of the call fixes
			myPlayer = None
			try:
				if itsPlayerTime:
					import QuickBattle.QuickBattle
					pPlayer = QuickBattle.QuickBattle.RecreatePlayer()
					if pPlayer and hasattr(pPlayer, "GetObjID") and hasattr(pPlayer, "GetName"): # In theory the above should be enough...
						pID = pPlayer.GetObjID()
						pcName = pPlayer.GetName()
						if pID != None and pID != App.NULL_ID:
							pGame = App.Game_GetCurrentGame()
							if pGame:
								pEpisode = pGame.GetCurrentEpisode()
								if pEpisode:
									pMission = pEpisode.GetCurrentMission()
									if pcName != None and pMission:
										pFriendlies = pMission.GetFriendlyGroup() 
										pEnemies = pMission.GetEnemyGroup() 
										pNeutrals = pMission.GetNeutralGroup()
										pTractors = pMission.GetTractorGroup()	
										pNeutrals2 = App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pNeutrals2")

										if pEnemies and pEnemies.IsNameInGroup(pcName):
											pEnemies.RemoveName(pcName)
										if pNeutrals and pNeutrals.IsNameInGroup(pcName):
											pNeutrals.RemoveName(pcName)
										if pNeutrals2 and pNeutrals2.IsNameInGroup(pcName):
											pNeutrals2.RemoveName(pcName)
										if pTractors and pTractors.IsNameInGroup(pcName):
											pTractors.RemoveName(pcName)
										if pFriendlies:
											if pFriendlies.IsNameInGroup(pcName):
												pFriendlies.RemoveName(pcName)
											pFriendlies.AddName(pcName)

										pPlayer.UpdateNodeOnly()

								if not App.g_kUtopiaModule.IsMultiplayer():
									pGame.SetPlayer(pPlayer)

							pPlayer.UpdateNodeOnly()

							killOtherShips([pID], pcName)
				
							global g_pID
							g_pID = pID
				else:
					if not pSet:
						try:
							pModule = None
							if App.g_kSetManager.GetSet("Belaruz4"):
								pModule = App.g_kSetManager.GetSet("Belaruz4")
							else:
								# Import the dest set & initialize it		
								import Systems.Belaruz.Belaruz4
								Systems.Belaruz.Belaruz4.Initialize()	
								pModule = App.g_kSetManager.GetSet("Belaruz4")	

							pSet = pModule

						except:
							pSet = None
							traceback.print_exc()

					if pSet and pShip and hasattr(pShip, "GetName") and hasattr(pShip, "GetObjID"):
						sID = pShip.GetObjID()
						sObjectName = pShip.GetName()
						if sObjectName != None:
							pSet.AddObjectToSet(pShip, sObjectName)
							proxManager = pSet.GetProximityManager() 
							if (proxManager):
								try:
									proxManager.UpdateObject(pShip)
								except:
									print __name__, ": Error:"
									traceback.print_exc()
			
			except:
				traceback.print_exc()

			return myPlayer


		def ExitSetToCheck(pObject, pEvent): # When a player ship exists a set, we need to update the set used
			if not pEvent:
				return 0

			pShip = App.ShipClass_Cast(pEvent.GetDestination())
			if not pShip:
				return 0

			iShipID = pShip.GetObjID()
			if not iShipID or iShipID == App.NULL_ID:
				return 0

			pShip = App.ShipClass_GetObjectByID(None, iShipID)
			if not pShip:
				return 0
	
			localToGlobalSet(pShip)
	
			return 0


		def localToGlobalSet(pShip): # Just handling the global set tracing I decided to keep
			pSet = pShip.GetContainingSet()
			if not pSet:
				return 0

			proxManager = pSet.GetProximityManager() 
			if (proxManager):
				isID = pShip.GetObjID()
				if g_pID != None and g_pID != App.NULL_ID and g_pID == isID:
					global g_pSet
					g_pSet = pSet
			return 0

		def NewFixTransportingBug(pObject, pEvent, param = None):
			global g_pID

			reload(sDS9FXSavedConfig)
			if sDS9FXSavedConfig and sDS9FXSavedConfig.TransporterFix == 1:
				scriptToPatch.bEnabled = 1
			else:
				scriptToPatch.bEnabled = 0

			pPlayer = MissionLib.GetPlayer()

			pID = None
			pShip = None
			mustFixBad = 0
			if param == "PlayerCreated": # Modifications done: as a way to detect when the Transporter bug happens, when it fails to find a Destination and a Set. Also for efficiency.
				pShipAux = App.ShipClass_Cast(pEvent.GetDestination())

				if pShipAux and hasattr(pShipAux, "GetObjID"):
					pID = pShipAux.GetObjID()
					pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pID)

				if (pID == None or pID == App.NULL_ID or not pShip) and pPlayer:
					pShip = pPlayer
					pID = pShip.GetObjID()
					pSet = pShip.GetContainingSet()
					if not pSet:
						mustFixBad = 1
						pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetToCheck") # This is required to prevent other scripts from derping out while the fix is being applied
						pShipA = quicklyReAddMissingSetting(pShip, g_pSet, 0)
						if pShipA:
							pShip = pShipA
							#pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetToCheck")

				if pID != None and pID != App.NULL_ID and not isInList(pID, scriptToPatch.lPlayerIDs):
					appendOtherShips([pID]) 
		
			elif param == "SetPlayer": # Changes done to make it more efficient, to update g_pID and to listen for when a ship exits a set.
				if pPlayer:
					pShip = pPlayer
					pID = pPlayer.GetObjID()

				if pID != None and pID != App.NULL_ID:
					if not isInList(pID, scriptToPatch.lPlayerIDs):
						appendOtherShips([pID])

					g_pID = pID
					localToGlobalSet(pShip)
					pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetToCheck")
					pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetToCheck")

					gerson = App.ShipClass_Cast(pEvent.GetSource())
					if gerson:
						oldManID = gerson.GetObjID()
						if oldManID != None and oldManID != App.NULL_ID:
							gerson = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), oldManID)
							if gerson and not oldManID == pID:
								gerson.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSetToCheck")

			elif param == "ObjectKilled":
				pShip = App.ShipClass_Cast(pEvent.GetDestination())
				if not pShip:
					return 0
				pID = pShip.GetObjID()
				if isInList(pID, scriptToPatch.lPlayerIDs): # Abstracting
					pass
				else:
					return 0
			else:
				return 0

			if scriptToPatch.bEnabled and pShip:
				if param != "ObjectKilled" and mustFixBad == 0:
					NewFix(None)
				else:
					secs = 7.0
					if mustFixBad == 1:
						secs = 1.0
					pSequence = App.TGSequence_Create()
					pAction = App.TGScriptAction_Create(__name__, "NewFix", mustFixBad)
					pSequence.AddAction(pAction, None, secs)
					pSequence.Play()

			return 0

		scriptToPatch.Fix = NewFix
		scriptToPatch.FixTransportingBug = NewFixTransportingBug

	except: # In case any unknown error happens, so we know it!
		traceback.print_exc()