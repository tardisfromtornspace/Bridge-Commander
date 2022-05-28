from bcdebug import debug
import App
import BaseAI
import MissionLib
from Custom.GalaxyCharts.GalacticWarSimulator import *

import AI.PlainAI.FollowWaypoints

class IntelligentShipDocking(AI.PlainAI.FollowWaypoints.FollowWaypoints):
	DS_NONE = 0
	DS_ENTERING_BASE = 1
	DS_IN_BASE = 2
	DS_EXITING_BASE = 3
	DS_FINISHING = 4

	RS_REMOVE_DAMAGE = 0
	RS_CHARGE_SHIELDS = 1
	RS_CHARGE_BATTERIES = 2
	RS_FILL_PROBES = 3
	RS_RELOAD_ARMAMENTS = 4
	RS_DONE = 5
	def __init__(self, pCodeAI):
		# Parent class init first.
		debug(__name__ + ", __init__")
		AI.PlainAI.FollowWaypoints.FollowWaypoints.__init__(self, pCodeAI)

		# Set default values for parameters that have them.
		self.SetupDefaultParams()
		self.SetRequiredParams()
		self.SetExternalFunctions()

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)
		self.lSubsystems = None
		self.iDockingStage = self.DS_NONE
		self.iRepairStage = self.RS_REMOVE_DAMAGE
		self.pBaseToDock = None
		self.fImpDisPerc = -1 #impulse engines disabled percentage
		self.bImpStat = 1
		self.sOriginalWaypoint = ""
		self.pCondISINORR = None
		if pCodeAI != None:
			pShip = pCodeAI.GetShip()
			if pShip != None:
				self.pCondISINORR = App.ConditionScript_Create("Custom.GalaxyCharts.WarAI", "ConditionIsShipInNeedOfRepairResupply", pShip.GetName() )

	#def GetNextUpdateTime(self):
	#	# return value in seconds
	#	return 1.0

	def Update(self):
		debug(__name__ + ", Update")
		pShip = self.pCodeAI.GetShip()
		if pShip == None:
			return App.ArtificialIntelligence.US_DORMANT
		pWSShip = WarSimulator.GetWSShipObjForShip(pShip)

		pSet = pShip.GetContainingSet()
		if pSet == None:
			return App.ArtificialIntelligence.US_DORMANT
		pRegion = pSet.GetRegion()
		if pRegion == None:
			return App.ArtificialIntelligence.US_DORMANT
		if pRegion.RegionBattle.IsBattleOn() == 1 and self.iDockingStage == self.DS_NONE:
			#we can't dock if there's a fight going on. However let us continue the docking procedure if a fight started after we docked.
			return App.ArtificialIntelligence.US_DORMANT

		#print "ISD: ISINORR:", self.pCondISINORR.GetStatus(), " ||AreWeDocking:", pWSShip.IsShipDocking()
		if self.pCondISINORR.GetStatus() == 0 and pWSShip.IsShipDocking() == 0:
			return App.ArtificialIntelligence.US_DORMANT

		pStarbase = self.GetStarbaseToDock()
		if pStarbase == None and pWSShip.IsShipDocking() == 0:
			return App.ArtificialIntelligence.US_DORMANT

		fInterceptRange = App.UtopiaModule_ConvertKilometersToGameUnits(50.0)
		if self.iDockingStage == self.DS_NONE and DistanceCheck(pShip, pStarbase) > fInterceptRange:
			pWSShip.SetStatusStr("Docking - Intercepting")
			fInSystemWarpRange = App.UtopiaModule_ConvertKilometersToGameUnits(800.0)
			bWarping = pShip.InSystemWarp(pStarbase, fInSystemWarpRange)				
			if bWarping != 1:
				bIntercepting = pShip.Intercept(pStarbase, fInterceptRange)
			if bWarping == 1 or bIntercepting == 1:
				return App.ArtificialIntelligence.US_ACTIVE
						

		if self.iDockingStage == self.DS_NONE:
			self.pBaseToDock = pStarbase
			pImpEngines = pShip.GetImpulseEngineSubsystem()
			pImpProp = pImpEngines.GetProperty()
			self.fImpDisPerc = pImpProp.GetDisabledPercentage()
			pWSShip.SetShipDockingInStarbase(self.pBaseToDock)
			pShip.SetDocked(1)
			sStartName, sEndName = self.MakeDockWaypoints(self.pBaseToDock)
			self.pBaseToDock.EnableCollisionsWith(pShip, 0)
			self.SetTargetWaypointName(sStartName)
			self.iDockingStage = self.DS_ENTERING_BASE
			pWSShip.SetStatusStr("Docking - Entering")
			pEvent = App.TGIntEvent_Create()
			pEvent.SetEventType(ET_SHIP_STARTED_DOCKING)
			pEvent.SetDestination(pShip)
			pEvent.SetInt( pShip.GetObjID() )
			App.g_kEventManager.AddEvent(pEvent)
			print "ISD: ship is starting docking procedures"
		elif self.iDockingStage == self.DS_ENTERING_BASE:
			self.CheckImpulseEngine(pShip)
			iStat = AI.PlainAI.FollowWaypoints.FollowWaypoints.Update(self)
			if iStat == App.ArtificialIntelligence.US_DONE:
				print "ISD: ship entered base, starting repairs"
				pWSShip.SetStatusStr("Docking - Repairing")
				#try to call DS9FX Xtended to recrew the ship.
				try:
					from Custom.DS9FX.DS9FXEventManager import DS9FXGlobalEvents
					# DS9FX will now handle your custom repair ship code and recrew the ship fully
					DS9FXGlobalEvents.Trigger_Repair_Ship(pShip)
				except:
					Galaxy.Logger.LogString("WarAI IntelligentShipDocking: couldn't fire Xtended REPAIR_SHIP event for ship "+str(pShip.GetName()))
				self.iDockingStage = self.DS_IN_BASE
		elif self.iDockingStage == self.DS_IN_BASE:
			self.DisableImpulse()
			iStat = self.DoRepairs(pShip)
			if iStat == App.ArtificialIntelligence.US_DONE:
				sStartName, sEndName = self.MakeUndockWaypoints(self.pBaseToDock)
				self.SetTargetWaypointName(sStartName)
				print "ISD: ship repaired, changing to exit starbase"
				pWSShip.SetStatusStr("Docking - Exiting")
				self.iDockingStage = self.DS_EXITING_BASE
		elif self.iDockingStage == self.DS_EXITING_BASE:
			self.EnableImpulse()
			iStat = AI.PlainAI.FollowWaypoints.FollowWaypoints.Update(self)
			if iStat == App.ArtificialIntelligence.US_DONE:
				self.pBaseToDock.EnableCollisionsWith(pShip, 1)
				self.iDockingStage = self.DS_FINISHING
		elif self.iDockingStage == self.DS_FINISHING:
			pWSShip.SetShipDockingInStarbase(None)
			pShip.SetDocked(0)
			self.lSubsystems = None
			self.iDockingStage = self.DS_NONE
			self.iRepairStage = self.RS_REMOVE_DAMAGE
			self.pBaseToDock = None
			pEvent = App.TGIntEvent_Create()
			pEvent.SetEventType(ET_SHIP_FINISHED_DOCKING)
			pEvent.SetDestination(pShip)
			pEvent.SetInt( pShip.GetObjID() )
			App.g_kEventManager.AddEvent(pEvent)
			return App.ArtificialIntelligence.US_DORMANT
		return App.ArtificialIntelligence.US_ACTIVE

	def DoRepairs(self, pShip):
		debug(__name__ + ", DoRepairs")
		vZero = App.TGPoint3()
		vZero.SetXYZ(0, 0, 0)
		pShip.SetVelocity(vZero)
		pShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		if self.lSubsystems == None:
			self.lSubsystems = []
			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
			while (pSubsystem != None):
				self.CheckSubsystem(pSubsystem)
				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

		if len(self.lSubsystems) >= 1:
			#repair subsystems
			sSubsystem = self.lSubsystems[0]
			pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystem)
			if pSubsystem != None:
				fRepairPoints = 900.0 * self.GetNextUpdateTime()
				pSubsystem.SetCondition( pSubsystem.GetCondition() + fRepairPoints )
				if pSubsystem.GetCondition() >= pSubsystem.GetMaxCondition():
					del self.lSubsystems[0]
			else:
				del self.lSubsystems[0]
		else:
			#do other stuff
			if self.iRepairStage == self.RS_REMOVE_DAMAGE:
				#after repairing the ship, fix visual damage
				pShip.RemoveVisibleDamage()
				self.iRepairStage = self.RS_CHARGE_SHIELDS

			elif self.iRepairStage == self.RS_CHARGE_SHIELDS:
				#now we recharge the ships shields
				pShields = pShip.GetShields()
				if pShields != None:
					for i in range(App.ShieldClass.NUM_SHIELDS):
						pShields.SetCurShields(i, pShields.GetMaxShields(i))
				self.iRepairStage = self.RS_CHARGE_BATTERIES

			elif self.iRepairStage == self.RS_CHARGE_BATTERIES:
				#recharge the ships batteries
				pPower = pShip.GetPowerSubsystem()
				if pPower != None:
					pPower.SetMainBatteryPower(pPower.GetMainBatteryLimit())
					pPower.SetBackupBatteryPower(pPower.GetBackupBatteryLimit())
				self.iRepairStage = self.RS_FILL_PROBES

			elif self.iRepairStage == self.RS_FILL_PROBES:
				#replenish the ship probe supply
				pSensors = pShip.GetSensorSubsystem()
				if pSensors:
					pProp = pSensors.GetProperty()
					if pProp:
						pSensors.SetNumProbes(pProp.GetMaxProbes())
				self.iRepairStage = self.RS_RELOAD_ARMAMENTS

			elif self.iRepairStage == self.RS_RELOAD_ARMAMENTS:
				#reload the ship weapons supply and charges
				import Actions.ShipScriptActions
				Actions.ShipScriptActions.ReloadShip(None, pShip.GetObjID())
				self.iRepairStage = self.RS_DONE

			elif self.iRepairStage == self.RS_DONE:
				#we finished our docking procedure =)
				pEvent = App.TGIntEvent_Create()
				pEvent.SetEventType(ET_SHIP_REPAIRED)
				pEvent.SetDestination(pShip)
				pEvent.SetInt( pShip.GetObjID() )
				App.g_kEventManager.AddEvent(pEvent)
				return App.ArtificialIntelligence.US_DONE
				
		return App.ArtificialIntelligence.US_ACTIVE
	def CheckSubsystem(self, pSubsystem):
		debug(__name__ + ", CheckSubsystem")
		if pSubsystem.GetRepairPointsNeeded() > 0:
			self.lSubsystems.append(pSubsystem.GetName())
		iChildren = pSubsystem.GetNumChildSubsystems()
		for iIndex in range(iChildren):
			pChild = pSubsystem.GetChildSubsystem(iIndex)
			self.CheckSubsystem(pChild)

	def GetStarbaseToDock(self):
		debug(__name__ + ", GetStarbaseToDock")
		pShip = self.pCodeAI.GetShip()
		if pShip == None:
			return None
		#start by checking our current region for allied dockable bases.
		sShipRace = GetShipRaceByWarSim(pShip)
		pSet = pShip.GetContainingSet()
		if pSet == None:
			return None
		pRegion = pSet.GetRegion()
		if pRegion == None:
			return None

		lDocks = []
		if sShipRace == pRegion.GetControllingEmpire() or AreRacesAllied(sShipRace, pRegion.GetControllingEmpire()) == 1:
			#we're on a allied system, check for dockable bases.
			lDocks = GetDockableBasesOfSet(pSet)

		if len(lDocks) <= 0:
			return None
		pStarbase = None
		fDistance = 1e+20
		for pCheckBase in lDocks:
			fCBdist = DistanceCheck(pShip, pCheckBase)
			pWSBase = WarSimulator.GetWSShipObjForShip(pCheckBase)
			if pWSBase and fCBdist < fDistance and pWSBase.IsBaseOccupied() == 0:
				pStarbase = pCheckBase
				fDistance = fCBdist
		return pStarbase

	def MakeDockWaypoints(self, pStarbase):
		# Waypoints will be named "Docking Entry" and "Docking Entry End".
		# Get these waypoints if they exist, or create them if they don't.
		debug(__name__ + ", MakeDockWaypoints")
		sStartName = pStarbase.GetName()+" Dock Entry"
		sEndName = pStarbase.GetName()+" Dock Entry End"
		pWaypointStart = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), sStartName) )
		if not pWaypointStart:
			pWaypointStart = App.Waypoint_Create(sStartName, pStarbase.GetContainingSet().GetName(), None)
			pWaypointStart.SetSpeed(5.0)

		pWaypointEnd = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), sEndName) )
		if not pWaypointEnd:
			pWaypointEnd = App.Waypoint_Create(sEndName, pStarbase.GetContainingSet().GetName(), None)
			pWaypointEnd.SetSpeed(2.0)

		# Make sure the End waypoint is attached to the start waypoint.
		if (not pWaypointStart.GetNext())  or  (pWaypointStart.GetNext().GetObjID() != pWaypointEnd.GetObjID()):
			# It's not.  Attach it.
			pWaypointStart.InsertAfterObj(pWaypointEnd)

		# Position pWaypointStart at the "Docking Entry Start" position/orientation
		# on the starbase model, and pWaypointEnd at the "Docking Entry End" one.
		for pWaypoint, sHardpoint in (
			(pWaypointStart, "Docking Entry Start"),
			(pWaypointEnd, "Docking Entry End")
			):

			vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, sHardpoint)
			if None in (vPos, vFwd, vUp):
				raise AttributeError, "Object (%s) has no position/orientation property (%s)" % (pStarbase.GetName(), sHardpoint)

			# Change these values to worldspace..
			import AI.Compound.DockWithStarbase
			AI.Compound.DockWithStarbase.PositionObjectFromLocalInfo(pWaypoint, pStarbase, vPos, vFwd, vUp)
		return [sStartName, sEndName]
	def MakeUndockWaypoints(self, pStarbase):
		# Waypoints will be named "Docking Entry" and "Docking Entry End".
		# Get these waypoints if they exist, or create them if they don't.
		debug(__name__ + ", MakeUndockWaypoints")
		sStartName = pStarbase.GetName()+" Dock Exit"
		sEndName = pStarbase.GetName()+" Dock Exit End"
		pWaypointStart = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), sStartName) )
		if not pWaypointStart:
			pWaypointStart = App.Waypoint_Create(sStartName, pStarbase.GetContainingSet().GetName(), None)
			pWaypointStart.SetSpeed(1.0)

		pWaypointEnd = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), sEndName) )
		if not pWaypointEnd:
			pWaypointEnd = App.Waypoint_Create(sEndName, pStarbase.GetContainingSet().GetName(), None)
			pWaypointEnd.SetSpeed(5.0)

		# Make sure the End waypoint is attached to the start waypoint.
		if (not pWaypointStart.GetNext())  or  (pWaypointStart.GetNext().GetObjID() != pWaypointEnd.GetObjID()):
			# It's not.  Attach it.
			pWaypointStart.InsertAfterObj(pWaypointEnd)
	
		# Position pWaypointStart at the "Docking Exit Start" position/orientation
		# on the starbase model, and pWaypointEnd at the "Docking Exit End" one.
		for pWaypoint, sHardpoint in (
			(pWaypointStart, "Docking Exit Start"),
			(pWaypointEnd, "Docking Exit End")
			):

			vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, sHardpoint)
			if None in (vPos, vFwd, vUp):
				raise AttributeError, "Object (%s) has no position/orientation property (%s)" % (pStarbase.GetName(), sHardpoint)

			# Change these values to worldspace..
			import AI.Compound.DockWithStarbase
			AI.Compound.DockWithStarbase.PositionObjectFromLocalInfo(pWaypoint, pStarbase, vPos, vFwd, vUp)
		return [sStartName, sEndName]

	def CheckImpulseEngine(self, pShip):
		debug(__name__ + ", CheckImpulseEngine")
		pImpEngines = pShip.GetImpulseEngineSubsystem()
		if int(pImpEngines.IsOn() and not pImpEngines.IsDisabled()) == 1:  #check is system online
			return 1
		iChildren = pImpEngines.GetNumChildSubsystems()
		for iIndex in range(iChildren):
			pChild = pImpEngines.GetChildSubsystem(iIndex)
			if pChild and int(pChild.IsOn() and not pChild.IsDisabled()) == 0:
				fPerc = pChild.GetProperty().GetDisabledPercentage() + 0.2
				pChild.SetCondition(pChild.GetMaxCondition() * fPerc)
	def DisableImpulse(self):
		debug(__name__ + ", DisableImpulse")
		if self.bImpStat == 0:
			return
		#hard stop and disable the impulse engines of the ship so that it doesn't "run" from the starbase.
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			vZero = App.TGPoint3()
			vZero.SetXYZ(0, 0, 0)
			pShip.SetVelocity(vZero)
			pShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

			pImpEngines = pShip.GetImpulseEngineSubsystem()
			pImpProp = pImpEngines.GetProperty()
			pImpProp.SetDisabledPercentage(2.0)
			print pShip.GetName(), " - disabled engines"
			self.bImpStat = 0
	def EnableImpulse(self):
		debug(__name__ + ", EnableImpulse")
		if self.bImpStat == 1:
			return
		#re-enable impulse engines of the ship
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pImpEngines = pShip.GetImpulseEngineSubsystem()
			pImpProp = pImpEngines.GetProperty()
			pImpProp.SetDisabledPercentage(self.fImpDisPerc)
			print pShip.GetName(), " - enabled engines"
			self.bImpStat = 1

	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is checking ISD.")
			if self.pCondISINORR == None:
				self.pCondISINORR = App.ConditionScript_Create("Custom.GalaxyCharts.WarAI", "ConditionIsShipInNeedOfRepairResupply", pShip.GetName() )
	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": stopped ISD.")