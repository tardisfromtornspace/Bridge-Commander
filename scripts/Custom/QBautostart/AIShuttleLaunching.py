import App
import Libs.LibEngineering
import ftb.ShipManager
import ftb.FTB_MissionLib
from Libs.LibQBautostart import *


MODINFO = {     "Author": "\"Defiant\" erik@bckobayashimaru.de",
                "needBridge": 0
            }

sMutatorName = "AI Shuttle Launching"
sTechMutatorName = "New Technology System"
iShipDisabledChance = 20 # percent
iShipOutnumberdChance = 20
iTotalLaunchChance = 20
iChanceMoreThenOneLaunchPerRound = 50
g_pAILaunchingTimer = None

NonSerializedObjects = (
"g_pAILaunchingTimer"
)

class AILaunchingTimer:
	def __init__(self):
		self.pTimerProcess = None
		self.SetupTimer()

        def SetupTimer(self):
                if self.pTimerProcess:
                        # We already have a timer.
                        return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)
		self.SetDelay()
		
	def SetDelay(self):
		self.pTimerProcess.SetDelay(App.g_kSystemWrapper.GetRandomNumber(10))
	
	def Update(self, dTimeAvailable):
		self.SetDelay()
		lShips = self.GetShuttleLaunchingShips()
		iLaunchCounts = 0
	
		for pShip in lShips:
			if self.ShipDisabled(pShip) and chance(iShipDisabledChance):
				iLaunchCounts = iLaunchCounts + 1
			if pShip.GetHull().GetConditionPercentage() < 0.25 and chance(iShipDisabledChance):
				iLaunchCounts = iLaunchCounts + 1
			if self.NumShipsTargetting(pShip.GetObjID()) > 2 and chance(iShipOutnumberdChance):
				iLaunchCounts = iLaunchCounts + 1
			if chance(iTotalLaunchChance * iLaunchCounts):
				self.SelectLaunchType(pShip)
				self.LaunchShip(pShip)
				if not chance(iChanceMoreThenOneLaunchPerRound):
					break
	
	def SelectLaunchType(self, pLaunchShip):
		pFTBCarrier = ftb.ShipManager.GetShip(pLaunchShip)
		if not pFTBCarrier or not hasattr(pFTBCarrier, "GetLaunchers"):
			return
		pFTBLauncher = pFTBCarrier.GetLaunchers()
		numTypes = len(pFTBLauncher)
		for i in range(App.g_kSystemWrapper.GetRandomNumber(10)):
			for index in range(numTypes):
				launchType = pFTBLauncher[index].NextLaunchType()
	
	def LaunchShip(self, pShip):
		ftb.FTB_MissionLib.LaunchShip(pShip)
	
	def NumShipsTargetting(self, iShipID):
		iNumShips = 0
		for pSet in App.g_kSetManager.GetAllSets():
			lShips = pSet.GetClassObjectList(App.CT_SHIP)
			for pObject in lShips:
				pShip = App.ShipClass_Cast(pObject)
				pTarget = pShip.GetTarget()
				if pTarget:
					iTargetID = pTarget.GetObjID()
					if iTargetID == iShipID:
						iNumShips = iNumShips + 1
		return iNumShips
	
	def ShipDisabled(self, pShip):
		iCountDisabledSystems = 0
		if pShip.GetImpulseEngineSubsystem() and pShip.GetImpulseEngineSubsystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 3
		if pShip.GetWarpEngineSubsystem() and pShip.GetWarpEngineSubsystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 1
		if pShip.GetShields() and pShip.GetShields().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 10
		if pShip.GetPowerSubsystem() and pShip.GetPowerSubsystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 5
		if pShip.GetSensorSubsystem() and pShip.GetSensorSubsystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 10
		if pShip.GetTorpedoSystem() and pShip.GetTorpedoSystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 3
		if pShip.GetPhaserSystem() and pShip.GetPhaserSystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 3
		if pShip.GetPulseWeaponSystem() and pShip.GetPulseWeaponSystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 3
		if pShip.GetCloakingSubsystem() and pShip.GetCloakingSubsystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 1
		if pShip.GetRepairSubsystem() and pShip.GetRepairSubsystem().IsDisabled():
			iCountDisabledSystems = iCountDisabledSystems + 2
		
		if iCountDisabledSystems > 20:
			return 1
		return 0
		
	def GetShuttleLaunchingShips(self):
		lRet = []
		for pSet in App.g_kSetManager.GetAllSets():
			lShips = pSet.GetClassObjectList(App.CT_SHIP)
			for pObject in lShips:
				pShip = App.ShipClass_Cast(pObject)
				pFTBCarrier = ftb.ShipManager.GetShip(pShip)
				if pFTBCarrier and not pShip.IsDead() and not pShip.IsDying() and pShip.GetAI() and not pShip.IsPlayerShip():
					if hasattr(pFTBCarrier, "GetLaunchers"):
						lRet.append(pShip)
		return lRet
		

def init():
	global g_pAILaunchingTimer
	
	if not App.g_kUtopiaModule.IsMultiplayer() or App.g_kUtopiaModule.IsHost():
		if Libs.LibEngineering.CheckActiveMutator(sMutatorName) and Libs.LibEngineering.CheckActiveMutator(sTechMutatorName):
			g_pAILaunchingTimer = AILaunchingTimer()
