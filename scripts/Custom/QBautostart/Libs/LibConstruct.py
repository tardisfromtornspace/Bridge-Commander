import App
import loadspacehelper
import AI.Player.FlyForward
from Races import Races
from LibQBautostart import *
import math

lBlockConstructingShip = []

MP_CONSTRUCT_MSG = 207


class Construct:
        def __init__(self, pConstructingShip, sConstructingRace, lShipsToConstruct, sConstructionLocation, iIncConstructionPower, iNumParallelConstructions = 1, bIsShip = 0, bUseRaceNames = 1):
		self.pConstructingShip = pConstructingShip
                self.iConstructingShipID = pConstructingShip.GetObjID()
                self.sConstructingRace = sConstructingRace
                self.lShipsToConstruct = lShipsToConstruct
                self.iBuildShipID = 0
                self.sConstructionLocation = sConstructionLocation
                self.iIncConstructionPower = iIncConstructionPower
                self.iNumParallelConstructions = iNumParallelConstructions
                self.iCurShipStatus = -20
		self.lBuildQueue = []
                self.sMode = "Construct"
                self.sNewMode = self.sMode
		self.MPClient = 0
		self.bIsShip = bIsShip
		self.bUseRaceNames = bUseRaceNames
		self.lBuildShipShieldMaxConditions = [0, 0, 0, 0, 0, 0]
		self.iProtectionShieldPowerPerSecond = 0
		self.iOnlyUndockWhenNeeded = 0
		self.PerMissionToStart = 0
		self.Waypoint = None
		self.iBuildShipIsStationary = 0

		if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
			self.MPClient = 1
		if not self.MPClient:
                	self.pTimerProcess = None
                	self.SetupTimer()
		
	def SetPerMissionToStart(self, i):
		self.PerMissionToStart = i
	def GetPerMissionToStart(self):
		return self.PerMissionToStart
	def ForceStart(self):
		if self.iCurShipStatus == 1:
			self.iCurShipStatus = 1.5

        def SetMode(self, sNewMode):
                if sNewMode == "Repair":
                        self.sNewMode = sNewMode
                else:
                        self.sNewMode = "Construct"
		if App.g_kUtopiaModule.IsMultiplayer():
			SendMPNewMode(self.iConstructingShipID, sNewMode)
        
        def GetMode(self):
		if self:
                	return self.sMode

        def GetConstructingShip(self):
		if self:
                	return App.ShipClass_GetObjectByID(None, self.iConstructingShipID)
        
        def GetBuildShip(self):
		if self:
                	return App.ShipClass_GetObjectByID(None, self.iBuildShipID)

        def SetupTimer(self):
                if self.pTimerProcess:
                        # We already have a timer.
                        return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(1.0)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)

        def Update(self, dTimeAvailable):
		if self.iCurShipStatus < 0:
                        self.sMode = self.sNewMode
                        self.iCurShipStatus = self.iCurShipStatus + 1
                        return
                        
                # check if the Object doesn't exist anymore
                if not self.GetConstructingShip() or not self.GetConstructingShip().GetContainingSet() or self.GetConstructingShip().GetName() == "MvamTemp":
                        # delete our timer
                        self.pTimerProcess = None
                        # remove our build ship if it exits
                        if self.GetBuildShip():
                                self.GetBuildShip().DestroySystem(self.GetBuildShip().GetHull())
				self.GetBuildShip().GetContainingSet().RemoveObjectFromSet(self.GetBuildShip().GetName())
				return
                # only do anything if our Hull is > 50%
                elif self.GetConstructingShip().GetHull().GetConditionPercentage() > 0.5:
                        self.ContinueConstruction()
		
		# make sure it looks like we are constructing
		if self.GetBuildShip() and self.bIsShip:
			self.GetConstructingShip().SetAI(CreateOrbitAI(self.GetConstructingShip(),  self.GetBuildShip()))
        
        def ContinueConstruction(self):
                if not self.GetBuildShip():
                        self.iCurShipStatus = 0
			# if we have the BuildID still set, then our ship probably exploded
			# in this case set the Status very low so we do not imediately start construction
			# process for a new ship, but in something like 10 minutes
			if self.iBuildShipID != 0:
				self.iCurShipStatus = -60;
			
                # set new mode
                if self.iCurShipStatus == 0 and self.sMode != self.sNewMode:
                        self.sMode = self.sNewMode
			if App.g_kUtopiaModule.IsMultiplayer():
				SendMPNewModeSet(self.iConstructingShipID, self.sMode)
                        
                if self.iCurShipStatus == 0 and self.sMode == "Construct":
                        self.CreateNewShip()
                elif self.iCurShipStatus == 1:
                        self.SetShipSystems(iIncC = self.iIncConstructionPower)
		elif self.iCurShipStatus == 1.5:
			self.ForcedEngineRepair()
                elif self.iCurShipStatus == 2:
                        self.ShipLeaveDock()
		elif self.iCurShipStatus == 2.5:
			self.CheckIfShipLeftDock()
                elif self.iCurShipStatus == 30:
                        self.ShipFinished()
                        self.iCurShipStatus = 31
                elif self.iCurShipStatus == 60:
                        self.iCurShipStatus = 0
                else:
                        self.iCurShipStatus = self.iCurShipStatus + 1

	def CheckIfShipLeftDock(self):
		if not self.GetConstructingShip():
			BlockConstructingShip(self.iConstructingShipID, 0)
			if self.iBuildShipID != 0:
				self.iCurShipStatus = -60;
		vConstructingShipPos    = self.GetConstructingShip().GetWorldLocation()
		vBuildShipPos           = self.GetBuildShip().GetWorldLocation()
		iConstructingShipPosX   = vConstructingShipPos.GetX()
		iConstructingShipPosY   = vConstructingShipPos.GetY()
		iConstructingShipPosZ   = vConstructingShipPos.GetZ()
		iBuildShipPosX          = vBuildShipPos.GetX()
		iBuildShipPosY          = vBuildShipPos.GetY()
		iBuildShipPosZ          = vBuildShipPos.GetZ()
		iXDif                   = iBuildShipPosX - iConstructingShipPosX
		iYDif                   = iBuildShipPosY - iConstructingShipPosY
		iZDif                   = iBuildShipPosZ - iConstructingShipPosZ
		iDist                   = math.sqrt((iXDif * iXDif) + (iYDif * iYDif) + (iZDif * iZDif))
		iConstructingShipRadius = self.GetConstructingShip().GetRadius()
		if iDist > iConstructingShipRadius:
			BlockConstructingShip(self.iConstructingShipID, 0)
			self.ShipFinished()
			self.iCurShipStatus = -5



        def ForcedEngineRepair(self):
		parentfull = 1
		allfull = 1
		pShip = self.GetBuildShip()
		Engines = pShip.GetImpulseEngineSubsystem()
		iTotalRepairPoints = self.iIncConstructionPower * self.iNumParallelConstructions
		iNum = Engines.GetNumChildSubsystems()
		if Engines.GetConditionPercentage() < 1:
			parentfull = 0
			allfull = 0
		iRepairPointsPerSystem = iTotalRepairPoints / (iNum + parentfull)
		for i in range(iNum):
			if Engines.GetChildSubsystem(i).GetConditionPercentage() < 1:
				Engines.GetChildSubsystem(i).SetCondition(Engines.GetChildSubsystem(i).GetCondition() + iRepairPointsPerSystem)
				allfull = 0
		if parentfull == 0:
			Engines.SetCondition(Engines.GetCondition() + iRepairPointsPerSystem)
		if allfull and Engines.IsOn():
			self.iCurShipStatus = 2


        def CreateNewShip(self):
                sShipType = self.GetNextShipToConstruct()
                if sShipType:
                        pSet = self.GetConstructingShip().GetContainingSet()
			if self.bUseRaceNames:
                        	sShipName = Races[self.sConstructingRace].GetRandomName()
			else:
				i = 1
				sShipName = sShipType + " " + str(i)
				while(MissionLib.GetShip(sShipName)):
					i = i + 1
					sShipName = sShipType + " " + str(i)
                        pNewShip = loadspacehelper.CreateShip(sShipType, pSet, sShipName, self.sConstructionLocation)
                        if not pNewShip:
                                return
			if not self.sConstructionLocation:
				kPos = FindGoodLocation(pSet, pNewShip.GetRadius() * 5)
				pNewShip.SetTranslate(kPos)
                        self.GetConstructingShip().EnableCollisionsWith(pNewShip, 0)
                        self.iBuildShipID = pNewShip.GetObjID()
                        self.iCurShipStatus = 1
                        self.SetShipSystems(iToValue = 0.00000001)
			if pNewShip.IsDead():
				return
			pNewShip.DisableGlowAlphaMaps()
                        # Make it stationary, so it doesn't move on gun fire
			self.iBuildShipIsStationary = pNewShip.GetShipProperty().IsStationary()
                        pNewShip.GetShipProperty().SetStationary(1)

################################################# Setup the Protectionshield ##############################################
			if self.iProtectionShieldPowerPerSecond > 0:
				pBuildShip = self.GetBuildShip()
				if not pBuildShip:
					return
				BuildShipShieldSystem = pBuildShip.GetShields()
				if not BuildShipShieldSystem:
					return
				BuildShipShieldSystem.SetCondition(BuildShipShieldSystem.GetMaxCondition())
				iCounter = 0
				for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
					self.lBuildShipShieldMaxConditions[iCounter] = BuildShipShieldSystem.GetMaxShields(ShieldDir)
					BuildShipShieldSystem.GetProperty().SetMaxShields(ShieldDir, self.iProtectionShieldPowerPerSecond * 1000)
					BuildShipShieldSystem.SetCurShields(ShieldDir, BuildShipShieldSystem.GetMaxShields(ShieldDir))
					iCounter = iCounter + 1

###########################################################################################################################
        
	def GetNextShipToConstruct(self):
		# if empty, add random ship to list
		if not self.lBuildQueue:
			ship = self.GetRandomShip()
			if not ship:
				return
			self.AddShipToConstructQueue(ship)
		if App.g_kUtopiaModule.IsMultiplayer():
			SendMPRemoveFromQueue(self.iConstructingShipID, 0)
		return self.lBuildQueue.pop(0)
	
	def AddShipToConstructQueue(self, sShipType, bSendNoMessage=0):
		if App.g_kUtopiaModule.IsMultiplayer() and not bSendNoMessage:
			SendMPAppendToQueue(self.iConstructingShipID, sShipType)
		return self.lBuildQueue.append(sShipType)
	
	def GetConstructQueue(self):
		return self.lBuildQueue
	
	def RemoveShipFromQueue(self, iPos, bSendNoMessage=0):
		if App.g_kUtopiaModule.IsMultiplayer() and not bSendNoMessage:
			SendMPRemoveFromQueue(self.iConstructingShipID, iPos)
		if self.lBuildQueue and len(self.lBuildQueue) > iPos:
			del self.lBuildQueue[iPos]
			return 0
		return -1

        def GetRandomShip(self):
		if self.lShipsToConstruct > 0:
                	iRandTypeNum = App.g_kSystemWrapper.GetRandomNumber(len(self.lShipsToConstruct))
                	return self.lShipsToConstruct[iRandTypeNum]
		return None

        def SetShipSystems(self, iToValue=0, iIncC=0):
                pShip = self.GetBuildShip()
                if not pShip:
                        self.iCurShipStatus = 0
                        return
                # disable glow every time, to make sure it hasn't been enabled
		if pShip.IsDead():
			return
                pShip.DisableGlowAlphaMaps()
                pPropSet = pShip.GetPropertySet()
                pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
                iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
                iNumConstructs = 0

                pShipSubSystemPropInstanceList.TGBeginIteration()
                for i in range(iNumItems):
                        pInstance = pShipSubSystemPropInstanceList.TGGetNext()
                        pProperty = pShip.GetSubsystemByProperty(App.SubsystemProperty_Cast(pInstance.GetProperty()))
                        if iToValue:
                                pProperty.SetCondition(iToValue)
                        elif iIncC:
                                # break here if we have done enough for this turn
                                if iNumConstructs >= self.iNumParallelConstructions:
                                        break
                                
                                iCurCondition = pProperty.GetCondition()
                                iNewCondition = iCurCondition + iIncC
                        
                                # count number of builds
                                if iCurCondition != pProperty.GetMaxCondition():
                                        iNumConstructs = iNumConstructs + 1
                                        
                                if iCurCondition + iIncC > pProperty.GetMaxCondition():
                                        iNewCondition = pProperty.GetMaxCondition()
                                pProperty.SetCondition(iNewCondition)
                
                pShipSubSystemPropInstanceList.TGDoneIterating()

		if self.iProtectionShieldPowerPerSecond > 0:
			ShieldsFull = 1
			self.TransferShieldPower()
		else:
			ShieldsFull = self.ChargeShields(iIncC)
                ReadyToLeaveDock = self.CheckReadyToLeaveDock()
                # if iNumConstructs is zero, then we are done with this ship
                if iIncC and iNumConstructs == 0 and ShieldsFull == 1 and ReadyToLeaveDock == 1:
                        self.iCurShipStatus = 2

###########################################################################################################################

	def TransferShieldPower(self):
		pBuildShip = self.GetBuildShip()
		if not pBuildShip:
			return
		BuildShipShieldSystem = pBuildShip.GetShields()
		if not BuildShipShieldSystem:
			return
		iCur = 0
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			iCur = iCur + BuildShipShieldSystem.GetCurShields(ShieldDir)
		iCur = iCur + (self.iProtectionShieldPowerPerSecond * 6)
		iCur = iCur / 6
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			if iCur <= BuildShipShieldSystem.GetMaxShields(ShieldDir):
				BuildShipShieldSystem.SetCurShields(ShieldDir, iCur)
			if iCur > BuildShipShieldSystem.GetMaxShields(ShieldDir):
				BuildShipShieldSystem.SetCurShields(ShieldDir, BuildShipShieldSystem.GetMaxShields(ShieldDir))

	def ChargeShields(self, iIncC = 0):
		pShip = self.GetBuildShip()
		if not pShip or iIncC == 0:
			return 1
		ShieldSystem = pShip.GetShields()
		if not ShieldSystem:
			return 1
		AllShieldsFull = 1
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
			shield = ShieldSystem.GetCurShields(ShieldDir) / (ShieldSystem.GetMaxShields(ShieldDir) + 0.00001)
			if shield < 1:
				AllShieldsFull = 0
				if ShieldSystem.GetCurShields(ShieldDir) + iIncC > ShieldSystem.GetMaxShields(ShieldDir):
					ShieldSystem.SetCurShields(ShieldDir, ShieldSystem.GetMaxShields(ShieldDir))
				elif ShieldSystem.GetCurShields(ShieldDir) + iIncC <= ShieldSystem.GetMaxShields(ShieldDir):
					ShieldSystem.SetCurShields(ShieldDir, ShieldSystem.GetCurShields(ShieldDir) + iIncC)
		if AllShieldsFull == 0:
			return 0
		return 1

	def CheckReadyToLeaveDock(self):
		if self.iOnlyUndockWhenNeeded == 0:
			return 1
		if self.PerMissionToStart == 0:
			return 0
		pEnemyGroup     = MissionLib.GetEnemyGroup()
		pFriendlyGroup     = MissionLib.GetFriendlyGroup()
		pSet		= self.pConstructingShip.GetContainingSet()
		lpEnemys        = pEnemyGroup.GetActiveObjectTupleInSet(pSet)
		lpFriendlys        = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
		countEnemy	= 0
		countFriendly	= 0
		sMyGroup = None

		# Count enemy Ships in System.
		for pEnemy in lpEnemys:
			# If it is a Base, add 5 points
			ShipType = GetShipType(pEnemy)
			if pEnemy.GetShipProperty().IsStationary():
				countEnemy = countEnemy + 5
			else:
				countEnemy = countEnemy + 1
		# Count friendly Ships in System.
		for pFriendly in lpFriendlys:
			# If it is a Base, add 5 points
			ShipType = GetShipType(pFriendly)
			if pFriendly.GetShipProperty().IsStationary():
				countFriendly = countFriendly + 5
			else:
				countFriendly = countFriendly + 1
		if checkaffliction(self.pConstructingShip) == 'friendly':
			if self.pConstructingShip.GetShipProperty().IsStationary():
				countFriendly = countFriendly - 5
			else:
				countFriendly = countFriendly - 1
			if countEnemy > self.iOnlyUndockWhenNeeded * countFriendly:
				return 1
		elif checkaffliction(self.pConstructingShip) == 'enemy':
			if self.pConstructingShip.GetShipProperty().IsStationary():
				countEnemy = countEnemy - 5
			else:
				countEnemy = countEnemy - 1
			if countFriendly > self.iOnlyUndockWhenNeeded * countEnemy:
				return 1
		return 0

###########################################################################################################################

        def ShipLeaveDock(self):
		if GetBlockedConstructionShip(self.iConstructingShipID) == 1:
			return

                # enable Glow
                if App.g_kLODModelManager.AreGlowMapsEnabled() == 1 and App.g_kLODModelManager.GetDropLODLevel() == 0: # else the game will crash on not high graphics
                        App.g_kLODModelManager.SetGlowMapsEnabled(0)
                        App.g_kLODModelManager.SetGlowMapsEnabled(1)
                
################################################# Reset the ships Shieldsystem ############################################
		if self.iProtectionShieldPowerPerSecond > 0:
			pBuildShip = self.GetBuildShip()
			if not pBuildShip:
				return
			BuildShipShieldSystem = pBuildShip.GetShields()
			if not BuildShipShieldSystem:
				return
			iCounter = 0
			for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
				BuildShipShieldSystem.GetProperty().SetMaxShields(ShieldDir, self.lBuildShipShieldMaxConditions[iCounter])
				BuildShipShieldSystem.SetCurShields(ShieldDir, BuildShipShieldSystem.GetMaxShields(ShieldDir))
				iCounter = iCounter + 1


###########################################################################################################################

               
		if self.iBuildShipIsStationary == 1:
			addShipToGroup(self.GetBuildShip().GetName(), getGroupFromShip(self.GetConstructingShip().GetName()))
			self.ShipFinished()
			self.iCurShipStatus = -10
			return

                # unset stationary
                self.GetBuildShip().GetShipProperty().SetStationary(0)

                # add it to the group
                addShipToGroup(self.GetBuildShip().GetName(), getGroupFromShip(self.GetConstructingShip().GetName()))
                # set its AI if we have a fixed build location
		if self.sConstructionLocation:
			if self.Waypoint == None:
	                	self.GetBuildShip().SetAI(AI.Player.FlyForward.CreatePlain(self.GetBuildShip(), 0.1))
				self.iCurShipStatus = 3
			elif self.Waypoint != None:
				BlockConstructingShip(self.iConstructingShipID, 1)
				self.GetBuildShip().SetAI(CreateAI(self.GetBuildShip(), self.Waypoint))
				self.iCurShipStatus = 2.5
				
		

        def ShipFinished(self):
		autoAI(self.GetBuildShip())
                self.iBuildShipID = 0
                if self.GetConstructingShip():
                        self.GetConstructingShip().EnableCollisionsWith(self.GetBuildShip(), 1)

def BlockConstructingShip(pConstructingShipID, bValue):
	global lBlockConstructingShip
	if bValue == 1:
		for i in range(len(lBlockConstructingShip)):
			if lBlockConstructingShip[i] == pConstructingShipID:
				return
		lBlockConstructingShip[len(lBlockConstructingShip) : len(lBlockConstructingShip)] = [pConstructingShipID]
	if bValue == 0:
		while pConstructingShipID in lBlockConstructingShip:
			lBlockConstructingShip.remove(pConstructingShipID)

def GetBlockedConstructionShip(pConstructingShipID):
	if pConstructingShipID in lBlockConstructingShip:
		return 1
	return 0


def CreateAI(pShip,pcWaypoint):
	#########################################
	# Creating PlainAI Scripted at (50, 50)
	pScripted = App.PlainAI_Create(pShip, "Scripted")
	pScripted.SetScriptModule("FollowWaypoints")
	pScripted.SetInterruptable(0)
	pScript = pScripted.GetScriptInstance()
	pScript.SetTargetWaypointName(pcWaypoint)
	# Done creating PlainAI Scripted
	#########################################
	return pScripted



def checkaffliction(pTargetShip):
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
	pFriendlies = pMission.GetFriendlyGroup()
        pEnemies = pMission.GetEnemyGroup()
        pNeutrals = pMission.GetNeutralGroup()
        if pFriendlies.IsNameInGroup(pTargetShip.GetName()):
                return 'friendly'
        if pEnemies.IsNameInGroup(pTargetShip.GetName()):
                return 'enemy'
        if pNeutrals.IsNameInGroup(pTargetShip.GetName()):
                return 'neutral'



def CreateMessageStream():
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage = App.TGMessage_Create()
	pMessage.SetGuaranteed(1)
	kStream = App.TGBufferStream()
	kStream.OpenBuffer(256)
	kStream.WriteChar(chr(MP_CONSTRUCT_MSG))
	return pMessage, kStream


def SendMessageToEveryone(pMessage, kStream):
	pNetwork = App.g_kUtopiaModule.GetNetwork()
	pMessage.SetDataFromStream(kStream)
	if not App.IsNull(pNetwork):
		if App.g_kUtopiaModule.IsHost():
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)
		else:
			pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage) # Host has to forward for us
	kStream.CloseBuffer()


def SendMPNewMode(iShipID, sNewMode):
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(1)
	kStream.WriteInt(iShipID)
	iLen = len(sNewMode)
	kStream.WriteShort(iLen)
	kStream.Write(sNewMode, iLen)
	SendMessageToEveryone(pMessage, kStream)


def SendMPNewModeSet(iShipID, sMode):
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(2)
	kStream.WriteInt(iShipID)
	iLen = len(sMode)
	kStream.WriteShort(iLen)
	kStream.Write(sMode, iLen)
	SendMessageToEveryone(pMessage, kStream)


def SendMPAppendToQueue(iShipID, sShipType):
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(3)
	kStream.WriteInt(iShipID)
	iLen = len(sShipType)
	kStream.WriteShort(iLen)
	kStream.Write(sShipType, iLen)
	SendMessageToEveryone(pMessage, kStream)


def SendMPRemoveFromQueue(iShipID, iPos):
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(4)
	kStream.WriteInt(iShipID)
	kStream.WriteInt(iPos)
	SendMessageToEveryone(pMessage, kStream)


def SendMPShipInConstructQueue(iShipID, sShipType):
	pMessage, kStream = CreateMessageStream()
	kStream.WriteInt(5)
	kStream.WriteInt(iShipID)
	iLen = len(sShipType)
	kStream.WriteShort(iLen)
	kStream.Write(sShipType, iLen)
	SendMessageToEveryone(pMessage, kStream)


def FindGoodLocation (pSet, fRadius):
	kPos = App.TGPoint3 ()
	# first try to find a location that's centered around (0,0,0)
	iCount = 0
	while (iCount < 50):
		x = App.g_kSystemWrapper.GetRandomNumber (200)
		x = x - 100;
		y = App.g_kSystemWrapper.GetRandomNumber (200)
		y = y - 100;
		z = App.g_kSystemWrapper.GetRandomNumber (200)
		z = z - 100;

		kPos.SetXYZ (x, y, z)

		if (pSet.IsLocationEmptyTG (kPos, fRadius, 1)):
			# Okay, found a good location.  Place it here.
			return kPos

		iCount = iCount + 1
	
	# if we're here, we failed to find a good location.  Do the offset method instead.

	# generate random offset direction.
	kOffset = App.TGPoint3 ()
	while (1):
		x = App.g_kSystemWrapper.GetRandomNumber (200) - 100
		y = App.g_kSystemWrapper.GetRandomNumber (200) - 100
		z = App.g_kSystemWrapper.GetRandomNumber (200) - 100
		x = float(x) / 10.0
		y = float(y) / 10.0
		z = float(z) / 10.0

		kOffset.SetXYZ (x, y, z)

		# make sure offset is not zero length
		if (kOffset.Length () > 1.0):
			# good.
			break

	# now add offset to kPos until we find an empty spot
	while pSet.IsLocationEmptyTG(kPos, fRadius, 1) == 0:
		kPos.Add (kOffset)

	# okay, now we've found an empty spot.
	return kPos





def CreateOrbitAI(pShip, pPlanet):
	#########################################
	# Creating PlainAI StartingOrbitScript at (241, 52)
	pStartingOrbitScript = App.PlainAI_Create(pShip, "StartingOrbitScript")
	pStartingOrbitScript.SetScriptModule("RunScript")
	pStartingOrbitScript.SetInterruptable(1)
	pScript = pStartingOrbitScript.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StartingOrbit")
	pScript.SetArguments(pShip, pPlanet)
	# Done creating PlainAI StartingOrbitScript
	#########################################
	#########################################
	# Creating PlainAI CirclePlanet at (353, 55)
	pCirclePlanet = App.PlainAI_Create(pShip, "CirclePlanet")
	pCirclePlanet.SetScriptModule("CircleObject")
	pCirclePlanet.SetInterruptable(1)
	pScript = pCirclePlanet.GetScriptInstance()
	pScript.SetFollowObjectName(pPlanet.GetName())
	pScript.SetNearFacingVector(App.TGPoint3_GetModelLeft())
	pScript.SetRoughDistances(pPlanet.GetRadius() + 10, pPlanet.GetRadius() + 10)
	# Done creating PlainAI CirclePlanet
	#########################################
	#########################################
	# Creating SequenceAI Sequence at (201, 111)
	pSequence = App.SequenceAI_Create(pShip, "Sequence")
	pSequence.SetInterruptable(1)
	pSequence.SetLoopCount(1)
	pSequence.SetResetIfInterrupted(1)
	pSequence.SetDoubleCheckAllDone(0)
	pSequence.SetSkipDormant(0)
	# SeqBlock is at (301, 127)
	pSequence.AddAI(pStartingOrbitScript)
	pSequence.AddAI(pCirclePlanet)
	# Done creating SequenceAI Sequence
	#########################################
	#########################################
	# Creating ConditionalAI CloseEnough at (210, 167)
	## Conditions:
	#### Condition InRange
	pInRange = App.ConditionScript_Create("Conditions.ConditionInRange", "ConditionInRange", 200.0 + pPlanet.GetRadius(),  pShip.GetName(), pPlanet.GetName())
	## Evaluation function:
	def EvalFunc(bInRange):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInRange:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pCloseEnough = App.ConditionalAI_Create(pShip, "CloseEnough")
	pCloseEnough.SetInterruptable(1)
	pCloseEnough.SetContainedAI(pSequence)
	pCloseEnough.AddCondition(pInRange)
	pCloseEnough.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI CloseEnough
	#########################################
	#########################################
	# Creating PlainAI FlyToPlanet at (328, 183)
	pFlyToPlanet = App.PlainAI_Create(pShip, "FlyToPlanet")
	pFlyToPlanet.SetScriptModule("Intercept")
	pFlyToPlanet.SetInterruptable(1)
	pScript = pFlyToPlanet.GetScriptInstance()
	pScript.SetTargetObjectName(pPlanet.GetName())
	pScript.SetInterceptDistance(0.0)
	pScript.SetAddObjectRadius(1)
	# Done creating PlainAI FlyToPlanet
	#########################################
	#########################################
	# Creating PriorityListAI OrbitPriorityList at (156, 227)
	pOrbitPriorityList = App.PriorityListAI_Create(pShip, "OrbitPriorityList")
	pOrbitPriorityList.SetInterruptable(1)
	# SeqBlock is at (272, 228)
	pOrbitPriorityList.AddAI(pCloseEnough, 1)
	pOrbitPriorityList.AddAI(pFlyToPlanet, 2)
	# Done creating PriorityListAI OrbitPriorityList
	#########################################
	#########################################
	# Creating PreprocessingAI OrbitAvoidObstacles at (128, 289)
	## Setup:
	import AI.Preprocessors
	pScript = AI.Preprocessors.AvoidObstacles()
	## The PreprocessingAI:
	pOrbitAvoidObstacles = App.PreprocessingAI_Create(pShip, "OrbitAvoidObstacles")
	pOrbitAvoidObstacles.SetInterruptable(1)
	pOrbitAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pOrbitAvoidObstacles.SetContainedAI(pOrbitPriorityList)
	# Done creating PreprocessingAI OrbitAvoidObstacles
	#########################################
	return pOrbitAvoidObstacles
