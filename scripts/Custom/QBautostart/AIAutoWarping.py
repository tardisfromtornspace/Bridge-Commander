from bcdebug import debug
import App
import MissionLib
import Libs.LibEngineering
from Libs.LibQBautostart import *
from Libs.Races import Races

MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }

sMutatorName = "AI auto Warping"
g_pAIWarpTimer = None
g_dOverrideAIs = {}

NonSerializedObjects = (
"g_pAIWarpTimer"
"g_dOverrideAIs"
)

class AIWarpTimer:
	def __init__(self):
		debug(__name__ + ", __init__")
		self.pTimerProcess = None
		self.SetupTimer()

        def SetupTimer(self):
                debug(__name__ + ", SetupTimer")
                if self.pTimerProcess:
                        # We already have a timer.
                        return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)
		self.SetDelay()
		
	def SetDelay(self):
		debug(__name__ + ", SetDelay")
		self.pTimerProcess.SetDelay(App.g_kSystemWrapper.GetRandomNumber(60) + 600)
	
	def Update(self, dTimeAvailable):
		debug(__name__ + ", Update")
		self.SetDelay()
		pPlayer = MissionLib.GetPlayer()
		
		dSets = {}
		for pSet in App.g_kSetManager.GetAllSets():
			if GetSystemShortName(pSet):
				dSets[GetSystemShortName(pSet)] = pSet.GetRegionModule()
		
		lShipsDone = []
		for pSet in App.g_kSetManager.GetAllSets():
			lShips = pSet.GetClassObjectList(App.CT_SHIP)
			for pObject in lShips:
				pShip = App.ShipClass_Cast(pObject)
				pSet = pShip.GetContainingSet()
				sRace = GetRaceFromShip(pShip)
				sGroup = getGroupFromShip(pShip.GetName())
				sOppositeGroup = getOppositeGroup(sGroup)
				if pShip.GetObjID() == pPlayer.GetObjID() or pShip.GetNetPlayerID() > 0 or pSet.GetName() == "warp" or not sRace or not sGroup or not sOppositeGroup and (not pShip.GetWarpEngineSubsystem() or pShip.GetWarpEngineSubsystem().IsDisabled()) or pShip.GetObjID() in lShipsDone:
					continue
				
				pGroup = getGroup(sGroup)
				pOppositeGroup = getGroup(sOppositeGroup)
				
				lpGroup = pGroup.GetActiveObjectTupleInSet(pSet)
				lpOppositeGroup = pOppositeGroup.GetActiveObjectTupleInSet(pSet)
				
				# still enemy ships to fight here
				if len(lpOppositeGroup) > 0:
					continue
				
				# group warp or single warp
				if len(lpGroup) < 5:
					# single warp, defence own systems
					iNumSystems = len(Races[sRace].Systems)
					if iNumSystems > 0:
						sSystem = Races[sRace].Systems[App.g_kSystemWrapper.GetRandomNumber(iNumSystems)]
						sDestination = ""
						if dSets.has_key(sSystem):
							sDestination = dSets[sSystem]
						if sDestination and pSet.GetRegionModule() != sDestination:
							OverrideAIInternal(pShip, CreateAI(pShip, sDestination))
							lShipsDone.append(pShip.GetObjID())
				else:
					# move the fleet as s task force to an enemy system
					lEnemySystems = getSystems(pOppositeGroup)
					iNumSystems = len(lEnemySystems)
					if iNumSystems > 0:
						sSystem = lEnemySystems[App.g_kSystemWrapper.GetRandomNumber(iNumSystems)]
						sDestination = ""
						if dSets.has_key(sSystem):
							sDestination = dSets[sSystem]
						if sDestination and pSet.GetRegionModule() != sDestination and pSet.GetName() != "warp":
							for ship in lpGroup:
								pShip = App.ShipClass_Cast(ship)
								if (pShip.GetObjID() == pPlayer.GetObjID() or pShip.GetNetPlayerID() > 0) and (not pShip.GetWarpEngineSubsystem() or pShip.GetWarpEngineSubsystem().IsDisabled()) or pShip.GetObjID() in lShipsDone:
									continue
								pShip.SetAI(CreateAI(pShip, sDestination))
								OverrideAIInternal(pShip, CreateAI(pShip, sDestination))
								lShipsDone.append(pShip.GetObjID())


def getSystems(pGroup):
	debug(__name__ + ", getSystems")
	lRet = []
	
	for pSet in App.g_kSetManager.GetAllSets():
		lpGroup = pGroup.GetActiveObjectTupleInSet(pSet)
		for ship in lpGroup:
			pShip = App.ShipClass_Cast(ship)
			sRace = GetRaceFromShip(pShip)
			if pShip and sRace:
				for sSystem in Races[sRace].Systems:
					if not sSystem in lRet:
						lRet.append(sSystem)
	
	return lRet


def CreateAI(pShip, sDestinationSet):
	#########################################
	debug(__name__ + ", CreateAI")
	pWarpToPlacement = App.PlainAI_Create(pShip, "WarpToPlacement")
	pWarpToPlacement.SetScriptModule("Warp")
	pWarpToPlacement.SetInterruptable(1)
	pScript = pWarpToPlacement.GetScriptInstance()
	pScript.SetDestinationSetName(sDestinationSet)
	pScript.SetWarpDuration(5)
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (235, 212)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pWarpToPlacement)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	return pAvoidObstacles


def OverrideAIInternal(pShip, pNewAI):
	# Check for an old AI.
	debug(__name__ + ", OverrideAIInternal")
	global g_dOverrideAIs
	pOldAI = pShip.GetAI()
	pOverrideAI = None
	if pOldAI:
		if g_dOverrideAIs.has_key(pShip.GetObjID()):
			# Already have an override AI for this ship.  Check if
			# that AI is still in place.
			pOverrideAI = App.ArtificialIntelligence_GetAIByID(g_dOverrideAIs[pShip.GetObjID()])
			if (not pOverrideAI)  or  (pOverrideAI.GetID() != pOldAI.GetID()):
				# It's not in place.  Gotta make a new one.
				pOverrideAI = None
			else:
				# It's still in place.  Remove whatever was in
				# the priority 1 slot (whatever the player told
				# this ship to do before).
				pOverrideAI.RemoveAIByPriority(1)

	if not pOverrideAI:
		# Make a new Override AI.
		pOverrideAI = App.PriorityListAI_Create(pShip, "FleetCommandOverrideAI")
		pOverrideAI.SetInterruptable(1)

		# Second AI in the list is the current AI.
		if pOldAI:
			pOverrideAI.AddAI(pOldAI, 2)

	# First AI in the list is the AI to override the old one.
	pOverrideAI.AddAI(pNewAI, 1)

	# Replace the ship's AI with the override AI.  The 0 here
	# tells the game not to delete the old AI.
	pShip.ClearAI(0, pOldAI)
	pShip.SetAI(pOverrideAI)

	# Save info about this override AI.
	g_dOverrideAIs[pShip.GetObjID()] = pOverrideAI.GetID()


def StopOverridingAI(pShip):
	debug(__name__ + ", StopOverridingAI")
	global g_dOverrideAIs
	pOldAI = pShip.GetAI()
	pOverrideAI = None
	if pOldAI:
		if g_dOverrideAIs.has_key(pShip.GetObjID()):
			# Have an override AI for this ship.  Check if
			# that AI is still in place.
			pOverrideAI = App.ArtificialIntelligence_GetAIByID(g_dOverrideAIs[pShip.GetObjID()])
			if pOverrideAI  and  (pOverrideAI.GetID() == pOldAI.GetID()):
				# It's still in place.  Remove whatever was in
				# the priority 1 slot (whatever the player told
				# this ship to do before).
				pOverrideAI.RemoveAIByPriority(1)


def ExitingWarp(pAction, pShip):
	debug(__name__ + ", ExitingWarp")
	if pShip:
		StopOverridingAI(pShip)
	return 0


def ExitSet(pObject, pEvent):
	debug(__name__ + ", ExitSet")
	pShip   = App.ShipClass_Cast(pEvent.GetDestination())
	sSetName = pEvent.GetCString()
	# if the system we come from is the warp system, then we exitwarp, right?
	if sSetName == "warp":
		# call ExitingWarp in a few seconds
		pSeq = App.TGSequence_Create()
		pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ExitingWarp", pShip), 4.0)
		pSeq.Play()
		
	pObject.CallNextHandler(pEvent)


def init():
	debug(__name__ + ", init")
	global g_pAIWarpTimer

	# No need to start in SP
	pGame = App.Game_GetCurrentGame()
	if not pGame or pGame.GetScript() == "Maelstrom.Maelstrom":
		return
	elif not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		if Libs.LibEngineering.CheckActiveMutator(sMutatorName):
			g_pAIWarpTimer = AIWarpTimer()
		App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_EXITED_SET, MissionLib.GetMission(), __name__ + ".ExitSet")
