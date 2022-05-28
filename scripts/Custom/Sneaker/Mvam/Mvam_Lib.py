from bcdebug import debug
import App
import Camera
import loadspacehelper
import MissionLib
import nt
import QuickBattle.QuickBattle
import string


#####################################
#     The QB Simulation Script      #
#####################################
def SneakerStartSimulation2(pObject, pEvent):
	debug(__name__ + ", SneakerStartSimulation2")
	MissionLib.EndLoadingText (None, None)
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.AllowKeyboardInput(1)
	pTopWindow.AllowMouseInput(1)
	QuickBattle.QuickBattle.EnableStopMenu() 	# Reset friendly fire warning points so that friendly fire will be enabled again.
	App.g_kUtopiaModule.SetCurrentFriendlyFire(0)		# Call this when you re-create the ship, too
	#global QuickBattle.QuickBattle.bInSimulation
	QuickBattle.QuickBattle.bInSimulation = 1 	# Suppress win/loss message during startup
	#global QuickBattle.QuickBattle.bWonOrLost
	QuickBattle.QuickBattle.bWonOrLost = 1 	# Lower Saffi's Menu
	App.CharacterAction_Create(QuickBattle.QuickBattle.g_pXO, App.CharacterAction.AT_MENU_DOWN).Play()

	QuickBattle.QuickBattle.RecreatePlayer()

	# Generate the necessary ships
	QuickBattle.QuickBattle.GenerateShips()

	# If pEnemies has no names in it, just make one up.
	if not QuickBattle.QuickBattle.pEnemies.GetNameTuple():
		QuickBattle.QuickBattle.pEnemies.AddName("This ship probably wont exist")

	# Change the region appropriately
	QuickBattle.QuickBattle.ChangeRegion()

	# Begin the simulation. Take each ship in the global ship mapping, and
	# assign its AI.
	#global QuickBattle.QuickBattle.g_kShips
	for kShip in QuickBattle.QuickBattle.g_kShips.items():
		iShipID, kTuple = kShip

		pcWhichAI, pcDestroyedSound, sWhichSide, sAINumber = kTuple

		#global QuickBattle.QuickBattle.g_iCurrentAILevel
		QuickBattle.QuickBattle.g_iCurrentAILevel = sAINumber

		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))
		if (pShip != None) and (pcWhichAI != None):
	#############################################################sneaker edit
			if (DetermineMvamAi(pShip) == 1):
				pAIModule = __import__("Custom.Sneaker.Mvam.MvamAI")
				pShip.SetAI(pAIModule.CreateAI(pShip), 0, 0)
			else:
	#########################################################end sneaker edit
				pAIModule = __import__("QuickBattle." + pcWhichAI)
				pShip.SetAI(pAIModule.CreateAI(pShip), 0, 0)

	# Force tactical view
	pTopWindow = App.TopWindow_GetTopWindow()
	pTopWindow.ForceBridgeVisible()	# Hack. Doing this somehow prevents the
							# occasionally tendancy of the game to
							# stop drawing frames at this point.
	pTopWindow.ForceTacticalVisible()

	# Switch us to red alert
	#pAlertEvent = App.TGIntEvent_Create()
	#pAlertEvent.SetDestination(App.Game_GetCurrentGame().GetPlayer())
	#pAlertEvent.SetEventType(App.ET_SET_ALERT_LEVEL)
	#pAlertEvent.SetInt(App.Game_GetCurrentGame().GetPlayer().RED_ALERT)
	#App.g_kEventManager.AddEvent(pAlertEvent)

	# Change text of start button to restart
	pStartButton = QuickBattle.QuickBattle.g_pXOMenu.GetButtonW(QuickBattle.QuickBattle.g_pMissionDatabase.GetString("Start Simulation"))
	if (pStartButton):
		pStartButton.SetName(QuickBattle.QuickBattle.g_pMissionDatabase.GetString("Restart Simulation"))

	App.g_kLODModelManager.Purge()

	# Reset flag after startup for win/loss message only if there is an enemy ship.
	if (len (QuickBattle.QuickBattle.g_kEnemyList) > 0):
		QuickBattle.QuickBattle.bWonOrLost = 0

	pObject.CallNextHandler(pEvent)



#####################################
#     The Determine AI Script       #
#####################################
#use this to determine wether we're going to use the MvamAI or not...
def DetermineMvamAi(pShip):
	#go through every new Mvam item in the Custom/Autoload/Mvam folder. Create new icons in the mvam menu
	debug(__name__ + ", DetermineMvamAi")
	straMvamList = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

	#okay, we need a mock go through.. just so it'll spawn a pyc
	snkMockModule = []
	for t in range(len(straMvamList)):
		#mock mock mock mock
		straTempName = string.split(straMvamList[t], ".")
		snkMockModule.append(__import__ ("Custom.Autoload.Mvam." + straTempName[0]))

	#save some memory
	del snkMockModule

	#reload the list after the mock. Create new icons in the mvam menu
	straMvamList = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

	#time to go through every mvam item. set up an int so i can modify it
	intListNum = len(straMvamList)

	#now that all pyc's are in place, lets do the real deal
	for i in range(intListNum):
		#okayyyy, make sure it's a pyc file, and make sure its not the init
		straTempName = string.split(straMvamList[i], ".")
		if ((straMvamList[i] == "__init__.pyc") or (straTempName[-1] == "py")):
			#bad file alert. redo the for loop and lower the counter
			i = i - 1
			intListNum = intListNum - 1

		# we succeeded! good file, so lets go
		else:
			straTempName = string.split(straMvamList[i], ".pyc")
			snkMvamModule = __import__ ("Custom.Autoload.Mvam." + straTempName[0])
			
			#alright, so determine if we're using the MvamAI or not...
			if (pShip.GetScript() == "ships." + snkMvamModule.ReturnMvamShips()[0]):
				return 1
				
	return 0



#####################################
#     The Return Module Script      #
#####################################
#now this is for returning the module... i hate making this in so many areas
def ReturnMvamModule(pShip):
	#go through every new Mvam item in the Custom/Autoload/Mvam folder. Create new icons in the mvam menu
	debug(__name__ + ", ReturnMvamModule")
	straMvamList = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

	#okay, we need a mock go through.. just so it'll spawn a pyc
	snkMockModule = []
	for t in range(len(straMvamList)):
		#mock mock mock mock
		straTempName = string.split(straMvamList[t], ".")
		snkMockModule.append(__import__ ("Custom.Autoload.Mvam." + straTempName[0]))

	#save some memory
	del snkMockModule

	#reload the list after the mock. Create new icons in the mvam menu
	straMvamList = nt.listdir("scripts\\Custom\\Autoload\\Mvam\\")

	#time to go through every mvam item. set up an int so i can modify it
	intListNum = len(straMvamList)

	#now that all pyc's are in place, lets do the real deal
	for i in range(intListNum):
		#okayyyy, make sure it's a pyc file, and make sure its not the init
		straTempName = string.split(straMvamList[i], ".")
		if ((straMvamList[i] == "__init__.pyc") or (straTempName[-1] == "py")):
			#bad file alert. redo the for loop and lower the counter
			i = i - 1
			intListNum = intListNum - 1

		# we succeeded! good file, so lets go
		else:
			straTempName = string.split(straMvamList[i], ".pyc")
			snkMvamModule = __import__ ("Custom.Autoload.Mvam." + straTempName[0])
			
			#alright, so check to see if this module has the pShip in it...
			if (pShip.GetScript() == "ships." + snkMvamModule.ReturnMvamShips()[0]):
				return snkMvamModule
				
	return 0



#####################################
#     The Create Player Script      #
#####################################
def CreatePlayerShip(sShipClass, pSet, pcName, sWaypoint, bUnloadShip = 0):
	debug(__name__ + ", CreatePlayerShip")
	pGame = App.Game_GetCurrentGame()

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
			# Player isn't dead.
			# Remove any old menus/handlers before setting up the new ship
			MissionLib.DetachCrewMenus()

			pOldSet.DeleteObjectFromSet(pPlayer.GetName())

		else:
			if (pOldSet != None):
				# Remove any old menus/handlers before setting up the new ship
				MissionLib.DetachCrewMenus()

				pOldSet.DeleteObjectFromSet(pPlayer.GetName())

	# If the ships aren't the same (or no previous ship), create the new one
	if (bCreateNewShip == 1):
		#pShipMod = __import__("ships." + sShipClass)
		import Foundation
		pShipMod = Foundation.FolderManager('ship', sShipClass)
#		kShipStats = pShipMod.GetShipStats()
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
			App.Game_SetPlayerHardpointFileName(pShipMod.GetShipStats()["HardpointFile"])
			loadspacehelper.AdjustShipForDifficulty(pPlayer, App.Game_GetPlayerHardpointFileName())
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

	#reload the menu
	import Custom.Sneaker.Mvam.SneakerXOMenuHandlers
	if pPlayer:
		Custom.Sneaker.Mvam.SneakerXOMenuHandlers.SneakerCreateMenu(pPlayer.GetScript())

	#the fix: thank MLeo for this one. I appreciate the time saver :)
	import Foundation 
	if(Foundation.__dict__.has_key("FolderDef") or Foundation.__dict__.has_key("FolderManager")): 
		pEvent = App.TGEvent_Create() 
		pEvent.SetEventType(Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP) 
		pEvent.SetDestination(pPlayer) 
		App.g_kEventManager.AddEvent(pEvent)

	return (pPlayer)



##############################
#     The Camera Script      #
##############################
def SneakerWatchShip(pAction, sSet, sObjectName, snkMvamModule, sCamera = "CutsceneCam"):
	debug(__name__ + ", SneakerWatchShip")
	pSet = App.g_kSetManager.GetSet(sSet)

	if not pSet:
		return 0

	pCamera = App.CameraObjectClass_GetObject(pSet, sCamera)

	if not pCamera:
		return 0

	dblCameraValues = snkMvamModule.ReturnCameraValues()

	pAction = App.TGScriptAction_Create("Actions.CameraScriptActions", "DropAndWatch", sSet, sObjectName)

	pAction.Play()

	pMode = pCamera.GetCurrentCameraMode()
	if not pMode:
		return 0

	pMode.SetAttrFloat("AwayDistance", dblCameraValues[0])
	pMode.SetAttrFloat("ForwardOffset", dblCameraValues[1])
	pMode.SetAttrFloat("SideOffset", dblCameraValues[2])
	pMode.SetAttrFloat("RangeAngle1", dblCameraValues[3])
	pMode.SetAttrFloat("RangeAngle2", dblCameraValues[4])
	pMode.SetAttrFloat("RangeAngle3", dblCameraValues[5])
	pMode.SetAttrFloat("RangeAngle4", dblCameraValues[6])
	pMode.Update()
	pMode.SetAttrFloat("AwayDistance", dblCameraValues[7])

	return 0
