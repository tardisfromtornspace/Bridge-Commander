from bcdebug import debug
################################################################
#   SB12_DryDock_LoadFix
########
#  This script will fix the loading procedure of the Starbase 12 and DryDock systems
# so that when using the Galaxy Charts mod, they will still be working correctly, with those stations being dockable.
###################################################################
import App
import Foundation
import MissionLib
import loadspacehelper
try:
	import Custom.GalaxyCharts.GalaxyLIB
	bIsOK = 1
except:
	print "SB12_DryDock_LoadFix cancelling... Galaxy Charts isn't installed."
	bIsOK = 0


NonSerializedObjects = (
"oLoadFixTrigger",
)

class LoadFixTrigger(Foundation.TriggerDef):
	def __init__(self, name, eventKey, dict = {}):
		debug(__name__ + ", __init__")
		Foundation.TriggerDef.__init__(self, name, eventKey, dict)
		self.bCreatedSB12Ships = 0
		self.bCreatedDryDockShips = 0
	def __call__(self, pObject, pEvent, dict = {}):
		debug(__name__ + ", __call__")
		global bIsOK
		if bIsOK == 0:
			return

		pShip = App.ShipClass_Cast(pEvent.GetDestination())
		if pShip == None:
			return
		pSet = pShip.GetContainingSet()
		if pSet == None:
			return

		pFriendlies = MissionLib.GetFriendlyGroup()
		pEnemies = MissionLib.GetEnemyGroup()
		if pFriendlies == None or pEnemies == None:
			return

		if pSet.GetName() == "Starbase12":
			import Maelstrom.Episode1.E1M1.E1M1_Starbase12_P
			Maelstrom.Episode1.E1M1.E1M1_Starbase12_P.LoadPlacements(pSet.GetName())

			bCreatedStarbaseNow = 0
			pStarbase = self.GetSB12Ships(pSet)
			if pStarbase == None and self.bCreatedSB12Ships == 0:
				pStarbase	= loadspacehelper.CreateShip("FedStarbase", pSet, "Starbase 12", "Starbase12 Location")			
				bCreatedStarbaseNow = 1

			if pStarbase != None:
				self.bCreatedSB12Ships = 1

				if bCreatedStarbaseNow == 1:
					sAllegiance = self.SetShipAllegiance(pStarbase)
					if sAllegiance == "Enemy":
						pStarbase.SetAI(CreateStarbaseAI(pStarbase, pFriendlies))
					elif sAllegiance == "Friendly":
						pStarbase.SetAI(CreateStarbaseAI(pStarbase, pEnemies))
	

		elif pSet.GetName() == "DryDock":
			import Maelstrom.Episode1.E1M1.Dock_P
			Maelstrom.Episode1.E1M1.Dock_P.LoadPlacements(pSet.GetName())
	
			bShipsExist = self.GetDryDockShips(pSet)
			if bShipsExist == 0 and self.bCreatedDryDockShips == 0:
				pDryDock	= loadspacehelper.CreateShip("DryDock", pSet, "Dry Dock", "DryDock Start")
				pDryDock1	= loadspacehelper.CreateShip("DryDock", pSet, "Dry Dock2", "DryDock2")
				pDryDock2	= loadspacehelper.CreateShip("DryDock", pSet, "Dry Dock3", "DryDock3")
				pStation	= loadspacehelper.CreateShip("SpaceFacility", pSet, "Station", "StationPlacement")
				for pObject in [ pDryDock, pDryDock1, pDryDock2, pStation ]:
					pObject.SetStatic(1)
					pObject.SetAI(CreateStayAI(pObject))
				self.bCreatedDryDockShips = 1
			elif bShipsExist == 1:
				self.bCreatedDryDockShips = 1
				pDryDock	= MissionLib.GetShip("Dry Dock", pSet)
				pDryDock1	= MissionLib.GetShip("Dry Dock2", pSet)
				pDryDock2	= MissionLib.GetShip("Dry Dock3", pSet)
				pStation	= MissionLib.GetShip("Station", pSet)
			
			if pDryDock != None:
				self.SetShipAllegiance(pDryDock)
			if pDryDock1 != None:
				self.SetShipAllegiance(pDryDock1)
			if pDryDock2 != None:
				self.SetShipAllegiance(pDryDock2)
			if pStation != None:
				self.SetShipAllegiance(pStation)

	def GetDryDockShips(self, pSet):
		debug(__name__ + ", GetDryDockShips")
		pDryDock	= MissionLib.GetShip("Dry Dock", pSet)
		pDryDock1	= MissionLib.GetShip("Dry Dock2", pSet)
		pDryDock2	= MissionLib.GetShip("Dry Dock3", pSet)
		pStation	= MissionLib.GetShip("Station", pSet)
		if pDryDock != None and pDryDock1 != None and pDryDock2 != None and pStation != None:
			return 1
		else:
			return 0
	def GetSB12Ships(self, pSet):
		debug(__name__ + ", GetSB12Ships")
		pStarbase	= MissionLib.GetShip("Starbase 12", pSet)
		return pStarbase
	def SetShipAllegiance(self, pShip):
		debug(__name__ + ", SetShipAllegiance")
		pFriendlies = MissionLib.GetFriendlyGroup()
		pEnemies = MissionLib.GetEnemyGroup()
		pPlayer = App.Game_GetCurrentPlayer()
		if pShip == None or pPlayer == None or pFriendlies == None or pEnemies == None:
			return
		pSet = pShip.GetContainingSet()
		if pSet == None:
			return
		pRegion = pSet.GetRegion()
		if pRegion == None:
			return
		sEmpire = pRegion.GetControllingEmpire()
		pRaceObj = Custom.GalaxyCharts.GalaxyLIB.GetRaceClassObj(sEmpire)
		if sEmpire != "Unknown" and sEmpire != "None" and pRaceObj != None:
			if Custom.GalaxyCharts.GalaxyLIB.IsShipEnemyOfRace(pShip, sEmpire) == 1 and pEnemies.IsNameInGroup(pShip.GetName()) == 0:
				pEnemies.AddName(pShip.GetName())
				return "Enemy"
			elif Custom.GalaxyCharts.GalaxyLIB.IsShipFriendlyOfRace(pShip, sEmpire) == 1 and pFriendlies.IsNameInGroup(pShip.GetName()) == 0:
				pFriendlies.AddName(pShip.GetName())		
				return "Friendly"

oLoadFixTrigger = LoadFixTrigger('SB12_DryDock LoadFix Trigger', App.ET_ENTERED_SET)


#######################################################
# HELPER FUNCTIONS
######################################
def CreateStayAI(pShip):
	#########################################
	# Creating PlainAI DontMove at (50, 50)
	debug(__name__ + ", CreateStayAI")
	pDontMove = App.PlainAI_Create(pShip, "DontMove")
	pDontMove.SetScriptModule("Stay")
	pDontMove.SetInterruptable(1)
	# Done creating PlainAI DontMove
	#########################################
	#########################################
	# Creating PreprocessingAI GreenAlert at (49, 109)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AlertLevel(App.ShipClass.GREEN_ALERT)
	## The PreprocessingAI:
	pGreenAlert = App.PreprocessingAI_Create(pShip, "GreenAlert")
	pGreenAlert.SetInterruptable(1)
	pGreenAlert.SetPreprocessingMethod(pScript, "Update")
	pGreenAlert.SetContainedAI(pDontMove)
	# Done creating PreprocessingAI GreenAlert
	#########################################
	return pGreenAlert

def CreateStarbaseAI(pShip, pEnemyShipGroup):
	#########################################
	# Creating CompoundAI StarbaseAttack at (194, 57)
	debug(__name__ + ", CreateStarbaseAI")
	import AI.Compound.StarbaseAttack
	pStarbaseAttack = AI.Compound.StarbaseAttack.CreateAI(pShip, pEnemyShipGroup)
	# Done creating CompoundAI StarbaseAttack
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (83, 155)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pStarbaseAttack)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################
	return pWait
