from bcdebug import debug
import App
from Custom.QBautostart.Libs.Races import Races
from Custom.QBautostart.Libs.LibConstruct import Construct

CONSTRUCT_SHIP = "ships.CN_FedStarbase"
RACE = "Federation"

dConstructors = {}

def RemoveFromList(lList, toRemove):
        debug(__name__ + ", RemoveFromList")
        if toRemove in lList:
                lList.remove(toRemove)
        
#def PositionObjectFromLocalInfo(pObject, pLocalInfoObject, vPos, vFwd, vUp):
#	vWorldPos = pLocalInfoObject.GetWorldLocation()
#	mWorldRot = pLocalInfoObject.GetWorldRotation()
#
#	vPos.MultMatrixLeft( mWorldRot )
#	vPos.Add(vWorldPos)
#	vFwd.MultMatrixLeft( mWorldRot )
#	vUp.MultMatrixLeft( mWorldRot )
#
#	# Move the waypoint to this position/orientation.
#	pObject.SetTranslate(vPos)
#	pObject.AlignToVectors(vFwd, vUp)
#	pObject.UpdateNodeOnly()

# 1. Create a new Ship (race of construction ship, random ship), Place it inside and set its Hardpoints to 0 + Epsilon
# 2. Create Loops(class-loop!) set increases the ships HP points
# 3. When all Hardpoints are at 100%, let the ship fly out of the dock, set AI
# 4. Build a new ship
def StartConstruction(pConstructionShip):
##############################################Ships #####################################################

	debug(__name__ + ", StartConstruction")
	lShipsToConstructLargeDock = Races[RACE].GetShips()
	RemoveFromList(lShipsToConstructLargeDock, "pulsemine")
	RemoveFromList(lShipsToConstructLargeDock, "torpedomine")
	RemoveFromList(lShipsToConstructLargeDock, "ExcaliburCarrier")
	RemoveFromList(lShipsToConstructLargeDock, "MvamPrometheusVentral")
	RemoveFromList(lShipsToConstructLargeDock, "MvamPrometheusDorsal")
	RemoveFromList(lShipsToConstructLargeDock, "MvamPrometheusSaucer")
	RemoveFromList(lShipsToConstructLargeDock, "GalaxySaucer")
	RemoveFromList(lShipsToConstructLargeDock, "GalaxyStardrive")
	RemoveFromList(lShipsToConstructLargeDock, "Shuttle")
	RemoveFromList(lShipsToConstructLargeDock, "type9")
	RemoveFromList(lShipsToConstructLargeDock, "Type11")
	RemoveFromList(lShipsToConstructLargeDock, "deltaflyer")
	RemoveFromList(lShipsToConstructLargeDock, "sovereignyacht")
	RemoveFromList(lShipsToConstructLargeDock, "sovereignyachtwarp")
	RemoveFromList(lShipsToConstructLargeDock, "DanubemkI")
	RemoveFromList(lShipsToConstructLargeDock, "DanubemkII")
	RemoveFromList(lShipsToConstructLargeDock, "VentureScout")
	RemoveFromList(lShipsToConstructLargeDock, "ZZSaratogaPod2")
	RemoveFromList(lShipsToConstructLargeDock, "PeragrineF1")
	RemoveFromList(lShipsToConstructLargeDock, "FedConst")
	RemoveFromList(lShipsToConstructLargeDock, "FedConstOpen")

	iOnlyUndockWhenNeeded = 1
	iProtectionShieldPowerPerSecond = 0
########if EnemyShipsOnPlayerSet / FriendlyShipsOnPlayerSet > iOnlyUndockWhenNeeded: UnDockShip  --==No Code==--

        global dConstructors
        sSetName = pConstructionShip.GetContainingSet().GetName()

##############################################Dock 1#####################################################
	DockNumber = 1
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" : 0.0,  "PosY" : -90.0,  "PosZ" : 10.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : -50.0,  "PosZ" : 16.0, "FwdX" : 1.0,  "FwdY" : 0.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : -43.3,  "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : -25.0,  "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : -0.5, "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 2#####################################################
	DockNumber = 2
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" : 45.0, "PosY" : -77.9,  "PosZ" : 10.0, "FwdX" : -0.5, "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : -43.3,  "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : -25.0,  "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : -0.5, "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 3#####################################################
	DockNumber = 3
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" : 77.9, "PosY" : -45.0,  "PosZ" : 10.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : -25.0,  "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : -0.5, "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 4#####################################################
	DockNumber = 4
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" : 90.0, "PosY" : 0.0,    "PosZ" : 10.0, "FwdX" : -1.0, "FwdY" : 0.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : -0.5, "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 5#####################################################
	DockNumber = 5
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" : 77.9, "PosY" : 45.0,   "PosZ" : 10.0, "FwdX" : -0.87,"FwdY" : -0.5,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : -0.5, "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 6#####################################################
	DockNumber = 6
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" : 45.0, "PosY" : 77.9,   "PosZ" : 10.0, "FwdX" : -0.5, "FwdY" :-0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : -0.87,"FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 7#####################################################
	DockNumber = 7
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" :-45.0, "PosY" : -77.9,  "PosZ" : 10.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-25.0, "PosY" : -43.3,  "PosZ" : 16.0, "FwdX" :-0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-43.3, "PosY" : -25.0,  "PosZ" : 16.0, "FwdX" :-0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 8#####################################################
	DockNumber = 8
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" :-77.9, "PosY" : -45.0,  "PosZ" : 10.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-43.3, "PosY" : -25.0,  "PosZ" : 16.0, "FwdX" :-0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock 9#####################################################
	DockNumber = 9
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" :-90.0, "PosY" : 0.0,    "PosZ" : 10.0, "FwdX" : 1.0,  "FwdY" : 0.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-50.0, "PosY" : 0.0,    "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock10#####################################################
	DockNumber = 10
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" :-77.8, "PosY" : 45.0,   "PosZ" : 10.0, "FwdX" : 0.87, "FwdY" :-0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-43.3, "PosY" : 25.0,   "PosZ" : 16.0, "FwdX" : 0.5,  "FwdY" : 0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()

##############################################Dock11#####################################################
	DockNumber = 11
        lShipsToConstruct = lShipsToConstructLargeDock
	Waypoints = [
		{"PosX" :-45.0, "PosY" : 77.9,   "PosZ" : 10.0, "FwdX" : 0.5,  "FwdY" :-0.87,"FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" :-25.0, "PosY" : 43.3,   "PosZ" : 16.0, "FwdX" : 0.87, "FwdY" : 0.5, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 70.0,   "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
		{"PosX" : 0.0,  "PosY" : 290.0,  "PosZ" : 16.0, "FwdX" : 0.0,  "FwdY" : 1.0, "FwdZ" : 0.0, "UpX" : 0.0, "UpY" : 0.0, "UpZ" : 1.0},
	]

	vWorldPos = pConstructionShip.GetWorldLocation()
	mWorldRot = pConstructionShip.GetWorldRotation()


	Waypoint = []
	
	for i in range(len(Waypoints)):
		vPos = App.TGPoint3()
		vFwd = App.TGPoint3()
		vUp  = App.TGPoint3()
		vPos.SetXYZ(Waypoints[i]["PosX"], Waypoints[i]["PosY"], Waypoints[i]["PosZ"])
		vFwd.SetXYZ(Waypoints[i]["FwdX"], Waypoints[i]["FwdY"], Waypoints[i]["FwdZ"])
		vUp.SetXYZ( Waypoints[i]["UpX"] , Waypoints[i]["UpY"] , Waypoints[i]["UpZ"] )

		vPos.MultMatrixLeft( mWorldRot )
		vPos.Add(vWorldPos)
		vFwd.MultMatrixLeft( mWorldRot )
		vUp.MultMatrixLeft( mWorldRot )
		if i > 0:
			Waypoint[len(Waypoint) : len(Waypoint)] = [App.Waypoint_Create(pConstructionShip.GetName() + " Leave Dock" + str(DockNumber) + " Wp" + str(i), sSetName, None)]
			Waypoint[i - 1].SetSpeed(5.0)
			Waypoint[i - 1].SetNavPoint(1)
			if i > 1:
				Waypoint[i - 2].InsertAfterObj(Waypoint[i - 1])
			Waypoint[i - 1].SetTranslate(vPos)
			Waypoint[i - 1].AlignToVectors(vFwd, vUp)
			Waypoint[i - 1].UpdateNodeOnly()
		else:
			        sConstructionLocation = pConstructionShip.GetName() + " Constructing Location" + str(DockNumber)
	      
			        # Position
			        kThis = App.Waypoint_Create(sConstructionLocation, sSetName, None)
			        kThis.SetStatic(1)
			        kThis.SetNavPoint(0)
			        kThis.SetTranslate(vPos)
			        kThis.AlignToVectors(vFwd, vUp)
			        kThis.Update(0)

			
	
        # go
        dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)] = Construct(pConstructionShip, RACE, lShipsToConstruct, sConstructionLocation, iIncConstructionPower = 40, iNumParallelConstructions = 8, bIsShip = 0, bUseRaceNames = 1)
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iOnlyUndockWhenNeeded = iOnlyUndockWhenNeeded
	dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].iProtectionShieldPowerPerSecond = iProtectionShieldPowerPerSecond
	if len(Waypoint) > 0:
		dConstructors[pConstructionShip.GetName() + 'Dock' + str(DockNumber)].Waypoint = Waypoint[0].GetName()
