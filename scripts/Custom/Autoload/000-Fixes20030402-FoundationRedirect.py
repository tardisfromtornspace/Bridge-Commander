# Foundation Triggers Extension 20030305 for Bridge Commander
# Written March 5, 2003 by Daniel B. Rollings AKA Dasher42, all rights reserved.


import Foundation
import Actions.EffectScriptActions ### Tisk tisk Dash, STOP Forgetting to import modules :P ###
								   # Baby why you gotta make me hitchoo?! ;)  -Dash
import App

Foundation.TriggerDef.ET_FND_CREATE_SHIP = App.UtopiaModule_GetNextEventType()
Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP = App.UtopiaModule_GetNextEventType()
bInitialized = 0

if int(Foundation.version[0:8]) < 20030402:
	print 'Outdated Foundation, installing FolderManager'



	def PreloadShip(sModelName, iNumToLoad = 0):
		# Mark the model for preloading.
		pMod = Foundation.FolderManager('ship', sModelName)
		# pMod = __import__("ships.%s" % sModelName)
		pMod.PreLoadModel()

		# Before the mission is initialized, we'll want to create a
		# bunch of these ships.
		if iNumToLoad > 0:
			import MissionLib
			pMission = MissionLib.GetMission()
			if not pMission:
	#			debug("No mission in PreloadShip.  Can't precreate ships (but models will be preloaded)")
				return

			pMission.AddPrecreatedShip(sModelName, iNumToLoad)


	def AdjustShipForDifficulty(pShip, pcHardpointFile):
		if (pShip == None):
			return
		if (pcHardpointFile == None):
			return

		fOFactor = App.Game_GetOffensiveDifficultyMultiplier()
		fDFactor = App.Game_GetDefensiveDifficultyMultiplier()
	#	debug("Adjusting ship, o factor: " + str(fOFactor) + ", d factor: " + str(fDFactor))

		pShipSet = pShip.GetPropertySet()
		pNewSet = App.TGModelPropertySet()
		# Load hardpoints.
		mod = Foundation.FolderManager('hp', pcHardpointFile)
		if not mod:
			return
		# try:
		# 	mod = __import__("ships.Hardpoints." + pcHardpointFile)
		# except ImportError:
	#		debug("Tried to load hardpoint file ships.Hardpoints." + pcHardpointFile + " and failed miserably")
		# 	return

		reload (mod)
		mod.LoadPropertySet(pNewSet)

		# Modify all subsystem strengths.
		pShipList = pShipSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
		pNewList = pNewSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)

		pShipList.TGBeginIteration()
		pNewList.TGBeginIteration()

		for i in range(pShipList.TGGetNumItems()):
			pShipProperty = App.SubsystemProperty_Cast(pShipList.TGGetNext().GetProperty())
			pNewProperty = App.SubsystemProperty_Cast(pNewList.TGGetNext().GetProperty())

			pSubsystem = pShip.GetSubsystemByProperty(pShipProperty)

			if (pSubsystem != None):
				import loadspacehelper
				loadspacehelper.ProcessSubsystemForDifficulty(pSubsystem, pShipProperty, pNewProperty)

		pShipList.TGDoneIterating()
		pNewList.TGDoneIterating()
		pShipList.TGDestroy()
		pNewList.TGDestroy()



	def CreateShip(pcScript, pSet, pcIdentifier, pcLocationName, iWarpFlash = 0, bGrabPreloaded = 1, shipDef = None):
		import App
		# Creates a new ship

		# Check if a ship of this type has been pre-created for us.
		pShip = None
		if bGrabPreloaded:
			import MissionLib
			pMission = MissionLib.GetMission()
			if pMission:
				pShip = pMission.GetPrecreatedShip(pcScript)

		if not pShip:
			# FIX ME:  This is back-arsewards in that the ship script is gotten from kStats
			# which was gotten from the ship script in the first place.  But this is the
			# least intrusive fix I can think of

			pModule = Foundation.FolderManager('ship', pcScript)

			pModule.LoadModel ()
			kStats = pModule.GetShipStats ()

			pShip = App.ShipClass_Create( kStats['Name'] )
			# print 'pModule name', pModule.__name__
			pShip.SetScript(pModule.__name__)

			if (kStats.has_key('DamageRadMod')):
				pShip.SetVisibleDamageRadiusModifier( kStats['DamageRadMod'] )

			if (kStats.has_key('DamageStrMod')):
				pShip.SetVisibleDamageStrengthModifier( kStats['DamageStrMod'] )

			if (kStats.has_key('SpecularCoef')):
				pShip.SetSpecularKs( kStats['SpecularCoef'] )

			pPropertySet = pShip.GetPropertySet()
			# Load hardpoints.
			mod = Foundation.FolderManager('hp', kStats['HardpointFile'])
			App.g_kModelPropertyManager.ClearLocalTemplates()
			reload(mod)
			mod.LoadPropertySet(pPropertySet)

			pShip.SetupProperties()

			if kStats.has_key('Rescale'):
				pShip.SetScale(kStats['Rescale'])

			# Set the default splash damage based on the size of the ship
			# and the strength of its hull.
			pHull = pShip.GetHull()
			if pHull:
				pShip.SetSplashDamage(pHull.GetMaxCondition() * 0.1, pShip.GetRadius() * 2.0)
				#debug("Setting splash damage for %s to (%f, %f)" % (pShip.GetName(), pShip.GetSplashDamage(), pShip.GetSplashDamageRadius()))

			pShip.SetNetType (kStats['Species'])

		if pSet:
			if not pSet.AddObjectToSet( pShip, pcIdentifier ):
	#			debug("Unable to add ship %s to set %s" % (pcIdentifier, pSet.GetName()))

				# Delete the ship.
				pDeletionEvent = App.TGEvent_Create()
				pDeletionEvent.SetEventType(App.ET_DELETE_OBJECT_PUBLIC)
				pDeletionEvent.SetDestination(pShip)
				App.g_kEventManager.AddEvent(pDeletionEvent)

				return None

			# Place the object at the specified location.
			if pcLocationName:
				pShip.PlaceObjectByName( pcLocationName )

			pShip.UpdateNodeOnly()

			if (iWarpFlash != 0):
				pWarp = pShip.GetWarpEngineSubsystem()
				if (pWarp != None) and (pcLocationName != None) and (pcLocationName != ""):
					pSequence = Actions.EffectScriptActions.CreateEndWarpSequence(pShip.GetObjID(), pcLocationName)
					pSequence.Play()
				else:
					# Just create a warp flash wherever the thing appears.
					pAction = App.TGScriptAction_Create("Actions.EffectScriptActions", "WarpFlash", pShip.GetObjID())
					pSequence = App.TGSequence_Create()
					pSequence.AddAction(pAction)
					pSequence.Play()

		# The Foundation requires that added ships select a species number that corresponds to an icon.
		# As icons are loaded, they are issued numbers by the Foundation.  This makes sure that a ship
		# has the species number that corresponds to the icon. -Dasher42

		pShipProperty = pShip.GetShipProperty()

		if pShipProperty:
			if shipDef:
				pShipProperty.SetSpecies(shipDef.GetIconNum())
			elif Foundation.shipList._keyList.has_key(pcScript):
				pShipProperty.SetSpecies(Foundation.shipList[pcScript].GetIconNum())
		else:
			print 'ERROR:  Cannot get ship property for %s, check hardpoints!' % (pcScript)

		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_SHIP)
		pEvent.SetDestination(pShip)
		App.g_kEventManager.AddEvent(pEvent)

		return pShip



	def CreatePlayerShip(sShipClass, pSet, pcName, sWaypoint, bUnloadShip = 0):
		import App
		import loadspacehelper
		pGame = App.Game_GetCurrentGame()

		#
		# Ugly, Ugly, Ugly
		#
		# Until we fix the type vs. string typing issue, we can't know if what they
		# want (string) is the same as what we have (type) without doing a big 'if'
		# check, which of course limits us.
		#

		# Don't show an entering banner this time..
		import Bridge.HelmMenuHandlers
		Bridge.HelmMenuHandlers.g_bShowEnteringBanner = 0

		bCreateNewShip = 1
		pPlayer = pGame.GetPlayer()
		if pPlayer:
			pOldSet = pPlayer.GetContainingSet()
			# Player exists...   But are they about to die?  If they're
			# Dead and they're not in a set, assume that they're about to
			# be deleted, and create a new player.
			if (not pPlayer.IsDead()):
				# Player isn't dead.  Check the player's ship to see if
				# a new one should be created.
				kSpecies = pPlayer.GetShipProperty().GetSpecies()

				if (((kSpecies == App.SPECIES_GALAXY) and (sShipClass != "Galaxy")) or
					((kSpecies == App.SPECIES_SOVEREIGN) and (sShipClass != "Sovereign"))):
					# Remove any old menus/handlers before setting up the new ship
					DetachCrewMenus()

					pOldSet.DeleteObjectFromSet(pPlayer.GetName())
				else:
					bCreateNewShip = 0
			else:
				if (pOldSet != None):
					# Remove any old menus/handlers before setting up the new ship
					DetachCrewMenus()

					pOldSet.DeleteObjectFromSet(pPlayer.GetName())

		# If the ships aren't the same (or no previous ship), create the new one
		if (bCreateNewShip == 1):
			# pShipMod = __import__("ships." + sShipClass)
			pShipMod = Foundation.FolderManager('ship', sShipClass)
			# kShipStats = pShipMod.GetShipStats()
			pPlayer = loadspacehelper.CreateShip(sShipClass, pSet, pcName, sWaypoint)

			if (pPlayer != None):
				pGame.SetPlayer(pPlayer)
				#
				# If a federation ship, give it a default NCC
				if (sShipClass == "Sovereign"):
					pPlayer.ReplaceTexture("Data/Models/Ships/Sovereign/Sovereign_glow.tga", "ID")
				elif (sShipClass == "Galaxy"):
					pPlayer.ReplaceTexture("Data/Models/SharedTextures/FedShips/Dauntless_glow.tga", "ID")
				elif (sShipClass == "Nebula"):
					pPlayer.ReplaceTexture("Data/Models/SharedTextures/FedShips/Berkeley_glow.tga", "ID")
				elif (sShipClass == "Akira"):
					pPlayer.ReplaceTexture("Data/Models/Ships/Akira/Geronimo_glow.tga", "ID")
				elif (sShipClass == "Ambassador"):
					pPlayer.ReplaceTexture("Data/Models/Ships/Ambassador/Zhukov_glow.tga", "ID")

				# Set the variable for the player's hardpoint file, so we can use
				# it later if the difficulty level is changed.
				# print 'hardpoints', pShipMod.GetShipStats()["HardpointFile"], sShipClass
				App.Game_SetPlayerHardpointFileName(pShipMod.GetShipStats()["HardpointFile"])
				# This is broken.  Fix it! - Dasher42
				# loadspacehelper.AdjustShipForDifficulty(pPlayer, App.Game_GetPlayerHardpointFileName())
				pPlayer.SetAlertLevel(App.ShipClass.GREEN_ALERT)

				pTorpSys = pPlayer.GetTorpedoSystem()
				if(pTorpSys):
					if (bUnloadShip != 0):
						# Unloads all torps, and resets the current loads to 0
						pTorpSys.SetAmmoType(0, 0)

						# Unload all other torps from the system
						iNumTypes = pTorpSys.GetNumAmmoTypes()
						for iType in range(iNumTypes):
							pTorpType = pTorpSys.GetAmmoType(iType)

							# Unload current load
							pTorpSys.LoadAmmoType(iType, -pTorpSys.GetNumAvailableTorpsToType(iType))


		pEvent = App.TGEvent_Create()
		pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP)
		pEvent.SetDestination(pPlayer)
		App.g_kEventManager.AddEvent(pEvent)
		
		return (pPlayer)


	class RedirectMutatorDef(Foundation.MutatorDef):
		def __init__(self, name = None):
			Foundation.MutatorDef.__init__(self, name)

			self.bInitialized = 0
			self.folders = {
				'ship': [ 'ships.' ],
				'hp': [ 'ships.Hardpoints.' ],
			}

		def __call__(self, type, key):
			if self.folders.has_key(type):
				for i in self.folders[type]:
					try:
						# print 'importing', type, i + key
						mod = __import__(i + key)
						# print mod
						if mod is not None:
							return mod
					except ImportError:
						pass

			return None

		def Add(self, type, folder):
			if self.folders.has_key(type):
				self.folders[type].insert(0, folder)
			else:
				self.folders[type] = [ folder ]

		def Remove(self, type, folder):
			try:
				self.folders[type].remove(folder)
			except:
				pass

		def Initialize(self):
			if not bInitialized:
				import loadspacehelper
				loadspacehelper.lCreateShipExtras = []
				loadspacehelper.lCreatePlayerShipExtras = []
				loadspacehelper.CreateShip = CreateShip
				loadspacehelper.AdjustShipForDifficulty = AdjustShipForDifficulty
				loadspacehelper.PreloadShip = PreloadShip

				import MissionLib
				MissionLib.CreatePlayerShip = CreatePlayerShip



	#########################################################
	# System-related definitions

	class FolderDef(Foundation.OverrideDef):

		def __init__(self, type, folder, dict = {}):
			Foundation.OverrideDef.__init__(self, type + folder + 'Folder', None, None, dict)
			self.type = type
			self.folder = folder

		def Activate(self):
			f = Foundation.FolderManager
			f.Initialize()
			f.Add(self.type, self.folder)

		def Deactivate(self):
			Foundation.FolderManager.Remove(self.type, self.folder)



	Foundation.FolderManager = RedirectMutatorDef()
	Foundation.FolderDef = FolderDef

	Foundation.version = '20030402'

