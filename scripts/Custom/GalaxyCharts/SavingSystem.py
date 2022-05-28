from bcdebug import debug
########################################################################################################################
###   SavingSystem.py
###                 by Fernando Aluani, aka USS Frontier
#######################
# This script, new in Galaxy Charts v2.0, contains the routines, functions and methods to save and load the game status,
# allowing the player to continue the game he was making later, or even share his game with other people.
########################################################################################################################
import App
import nt
import string
import loadspacehelper
import MissionLib
import Galaxy
import GalaxyLIB
import GalacticWarSimulator
import Custom.QBautostart.Libs.Races
from Custom.QBautostart.Libs.Racesclass import RaceInfo

# for checking in other scripts
bIsLoading = 0
# list of ship names that should ignore those event, for use with the WarSim
lIgnoreObjDestroyed = []
lIgnoreExitedSet = []
lIgnoreObjCreated = []
lIgnoreEnteredSet = []


#################################################
# Master Functions  (LOAD NEEDS RECODING)
#######################################################
def Save(sSaveName):
	debug(__name__ + ", Save")
	if App.g_kTravelManager.IsAnyShipTravelling() == 1:
		# I know this seems like a cheap solution... But it is exactly that. It's a lot easier to wait for travelling ships to stop travelling to
		# be able to save the game than having to save the Travel attributes, and make the (complicated) routine to load them up...
		print "Couldnt save the game: at least 1 ship is travelling."
		return 0
	try:
		lData = GetSaveData()
		sSaveFile = "scripts\\Custom\\GalaxyCharts\\GameSaves\\" + sSaveName + ".py"
		file = nt.open(sSaveFile, nt.O_WRONLY|nt.O_CREAT|nt.O_TRUNC)
		for sLine in lData:
			nt.write(file, str(sLine)+ "\n")
		nt.close(file)
		print "Saved Game Stats!"
		GalacticWarSimulator.WarSimulator.dStats["TimesSaved"] = GalacticWarSimulator.WarSimulator.dStats["TimesSaved"] + 1
		return 1
	except:
		Galaxy.LogError("SavingSystem_Save: couldn't save game stats")
		return 0

def Load(sSaveName):
	debug(__name__ + ", Load")
	global bIsLoading
	bIsLoading = 1
	bLoadedOK = 0
	try:
		sSaveFile = "Custom.GalaxyCharts.GameSaves." + sSaveName
		pModule = __import__(sSaveFile)
		if LoadGameData(pModule) == 1:
			print "Loaded Game Stats!"

			pTopWin = App.TopWindow_GetTopWindow()
			if pTopWin != None:
				pTopWin.ForceTacticalVisible()

			bLoadedOK = 1
	except:
		Galaxy.LogError("SavingSystem_Load: couldn't load game stats")
	bIsLoading = 0
	return bLoadedOK

###################################################################
# General Saving Function
###################################################################
def GetSaveData():
	debug(__name__ + ", GetSaveData")
	lAllShipsDatas = []
	lData = ["Sets = ["]
	for pSet in App.g_kSetManager.GetAllSets():
		if str(pSet.GetRegionModule()) != "None":
			lSetData = GetDataListFromDict( GetSystemStats(pSet), 1 )
			for sSetDataLine in lSetData:
				lData.append(sSetDataLine)

			lShips = pSet.GetClassObjectList(App.CT_SHIP)
			for pShipObj in lShips:
				pShip = App.ShipClass_Cast(pShipObj)
				if pShip != None:
					lAllShipsDatas.append( GetDataListFromDict( GetShipStats(pShip), 1 ) )

	lData.append("]")
	lData.append("")
	lData.append("Ships = [")
	for lShipData in lAllShipsDatas:
		for sShipDataLine in lShipData:
			lData.append(sShipDataLine)
	lData.append("]")
	lData.append("")
	lData.append("WarSimulator = [")
	lWarData = GetDataListFromDict( GetWarSimStats() , 1)
	for sWarDataLine in lWarData:
		lData.append(sWarDataLine)
	lData.append("]")
	lData.append("")
	lData.append("FleetManager = [")
	lFleetData = GetDataListFromDict( GetFleetStats() , 1)
	for sFleetDataLine in lFleetData:
		lData.append(sFleetDataLine)
	lData.append("]")
	lData.append("")
	lData.append("Regions = [")
	lRegionData = GetDataListFromDict( GetRegionsStats() , 1)
	for sRegionDataLine in lRegionData:
		lData.append(sRegionDataLine)
	lData.append("]")
	lData.append("")
	lData.append("GalaxyLIB = [")
	lGCLIBData = GetDataListFromDict( GetGCLIBStats() , 1)
	for sGCLIBDataLine in lGCLIBData:
		lData.append(sGCLIBDataLine)
	lData.append("]")
	lData.append("")
	lData.append("Races = [")
	lRaceData = GetDataListFromDict( GetRaceStats() , 1)
	for sRaceDataLine in lRaceData:
		lData.append(sRaceDataLine)
	lData.append("]")
	return lData

###################################################################
# General Loading Function
###################################################################
def LoadGameData(pSaveModule):
	## while this load order may seem weird and all, and in some places not very resource friendly, like making 2 times the same FOR loop,
	## that is needed to maintain a specific load order for the objs and attributes.
	debug(__name__ + ", LoadGameData")
	lAttrs = ["Sets", "Ships", "WarSimulator", "Regions", "GalaxyLIB", "Races"]
	for sAttr in lAttrs:
		if not sAttr in pSaveModule.__dict__.keys():
			print "Couldn't load save file", pSaveModule.__name__, ". Its missing the attribute:", sAttr
			return 0

	##############
	### Load races
	for sRace in pSaveModule.Races[0].keys():
		dRaceData = pSaveModule.Races[0][sRace]
		if Custom.QBautostart.Libs.Races.Races.has_key(sRace):
			pRaceObj = Custom.QBautostart.Libs.Races.Races[sRace]
		else:
			pRaceObj = RaceInfo(sRace)
		for sAttr in dRaceData.keys():
			pRaceObj.__dict__[sAttr] = dRaceData[sAttr]

	##############
	### Load GalaxyLIB / RDFs
	GalaxyLIB.iRDFshipCreated = pSaveModule.GalaxyLIB[0]["iRDFshipCreated"]
	GalaxyLIB.CreatedIDsList = pSaveModule.GalaxyLIB[0]["CreatedIDsList"]
	dRDFs = {}
	for dRDFStats in pSaveModule.GalaxyLIB[0]["lRDFs"]:
		pRDF = GalaxyLIB.RandomDefenceForce("None", 0, 0, 0, None, 0, 0, 0, 0)
		for sAttr in dRDFStats.keys():
			pRDF.__dict__[sAttr] = dRDFStats[sAttr]
		dRDFs[pRDF.GetObjID()] = pRDF

	##############
	### Load Regions/SystemPlugins/SetPlugins/RegionBattle
	for sRegion in pSaveModule.Regions[0].keys():
		dRegData = pSaveModule.Regions[0][sRegion]
		pRegion = App.g_kRegionManager.GetRegion(sRegion)
		if pRegion != None:
			for sAttr in dRegData.keys():
				if sAttr != "Sets" and sAttr != "RegionBattle":
					if sAttr == "Location" and type(dRegData[sAttr]) == type([]):
						pRegion.SetLocation(dRegData[sAttr][0], dRegData[sAttr][1])
					elif sAttr == "Location" and type(dRegData[sAttr]) == type(""):
						pRegion.Location = None
					elif sAttr == "Description":
						pRegion.Description = string.replace(dRegData[sAttr], "<%NL%>", "\n")
					else:
						pRegion.__dict__[sAttr] = dRegData[sAttr]
			for pSet in pRegion.GetAllSets():
				if pSet.GetName() in dRegData["Sets"].keys():
					for sSetAttr in dRegData["Sets"][pSet.GetName()].keys():
						pSet.__dict__[sSetAttr] = dRegData["Sets"][pSet.GetName()][sSetAttr]
			for sRBAttr in dRegData["RegionBattle"].keys():
				if sRBAttr == "_RegionBattle__RAF" or sRBAttr == "_RegionBattle__RDF":
					if dRDFs.has_key(dRegData["RegionBattle"][sRBAttr]):
						pRegion.RegionBattle.__dict__[sRBAttr] = dRDFs[dRegData["RegionBattle"][sRBAttr]]
					else:
						pRegion.RegionBattle.__dict__[sRBAttr] = None
				else:
					pRegion.RegionBattle.__dict__[sRBAttr] = dRegData["RegionBattle"][sRBAttr]

	##############
	### Load FleetManager / ShipFleet
	dFleetManagerStats = pSaveModule.FleetManager[0]
	GalacticWarSimulator.ShipFleet.dRacesIndexValues = dFleetManagerStats["dRacesIndexValues"]
	del dFleetManagerStats["dRacesIndexValues"]
	for sFMAttr in dFleetManagerStats.keys():
		if sFMAttr == "dFleetIDs":
			for sFleetName in dFleetManagerStats["dFleetIDs"].keys():
				dFleetData = dFleetManagerStats["dFleetIDs"][sFleetName]
				pFleet = GalacticWarSimulator.ShipFleet(None, dFleetData)
				GalacticWarSimulator.FleetManager.dFleetIDs[sFleetName] = pFleet
		else:
			GalacticWarSimulator.FleetManager.__dict__[sFMAttr] = dFleetManagerStats[sFMAttr]

	##############
	### Load WarSimulator / WSShips
	dWarSimStats = pSaveModule.WarSimulator[0]
	for sWSAttr in dWarSimStats.keys():
		if sWSAttr != "dShips":
			GalacticWarSimulator.WarSimulator.__dict__[sWSAttr] = dWarSimStats[sWSAttr]
	for sShipName in dWarSimStats["dShips"].keys():
		dWSShipStats = dWarSimStats["dShips"][sShipName]
		pWSShip = GalacticWarSimulator.WSShip("LOADING", "", "")
		for sWSSAttr in dWSShipStats.keys():
			if sWSSAttr != "Race":
				pWSShip.__dict__[sWSSAttr] = dWSShipStats[sWSSAttr]
		if Custom.QBautostart.Libs.Races.Races.has_key(dWSShipStats["Race"]):
			pRaceObj = Custom.QBautostart.Libs.Races.Races[ dWSShipStats["Race"] ]
			pWSShip.Race = pRaceObj
			if pWSShip.GetOrder() != pWSShip.O_DESTROYED:
				pRaceObj.dWSShips[pWSShip.GetShipName()] = pWSShip
		pRegion = App.g_kRegionManager.GetRegion( pWSShip.GetRegionAssignedTo() )
		if pRegion != None:
			if pWSShip.GetOrder() == pWSShip.O_ATTACK:
				pRegion.RegionBattle.__dict__["_RegionBattle__attackForce"][pWSShip.GetShipName()] = pWSShip
			elif pWSShip.GetOrder() == pWSShip.O_DEFEND:
				pRegion.RegionBattle.__dict__["_RegionBattle__defenceForce"][pWSShip.GetShipName()] = pWSShip
		GalacticWarSimulator.WarSimulator.dShips[pWSShip.GetShipName()] = pWSShip

	##############
	### Recreate sets
	for dSetData in pSaveModule.Sets:
		try:
			pSetModule = __import__( dSetData["Module"] )
			if pSetModule.GetSet() == None:
				pSetModule.Initialize()
		except:
			Galaxy.LogError("SavingSystem_Load: couldn't load set: "+str(dSetData["Module"]))

	##############
	### Recreate ships  (hard part! yay! >_<)
	dShips = {}
	dShipTargets = {}
	iPlayerID = 0
	for dShipData in pSaveModule.Ships:
		pShip = CreateShip(dShipData)
		if dShipData["Is Player"] == 1:
			pGame = App.Game_GetCurrentGame()
			if pGame != None:
				pGame.SetPlayer(pShip)
				iPlayerID = pShip.GetObjID()
		pShip.SetTarget( dShipData["Target Name"] )
		dShipTargets[ dShipData["Target Name"] ] = pShip
		if dShipData["Is Cloaked"] == 1:
			pCloak = pShip.GetCloakingSubsystem()
			if pCloak != None:
				pCloak.InstantCloak()
		dShips[pShip.GetName()] = pShip
		if GalacticWarSimulator.WarSimulator.dShips.has_key(pShip.GetName()):
			GalacticWarSimulator.WarSimulator.dShips[pShip.GetName()].Ship = pShip
	# just to be sure we're setting the target correctly...
	for sTargetName in dShipTargets.keys():
		dShipTargets[sTargetName].SetTarget(sTargetName)

	##############
	### Update set objects (waypoints, projectiles and others...)
	for dSetData in pSaveModule.Sets:
		try:
			pSetModule = __import__( dSetData["Module"] )
			pSet = pSetModule.GetSet()
			lObjects = pSet.GetClassObjectList(App.CT_OBJECT)
			dWaypoints = {}
			for pObject in lObjects:
				if App.Waypoint_Cast(pObject) != None:
					dWaypoints[pObject.GetName()] = App.Waypoint_Cast(pObject)
				else:
					if not pObject.GetName() in dSetData["Objects"]:
						pSet.RemoveObjectFromSet(pObject.GetName())
			for dWayData in dSetData["Waypoints"]:
				vLoc = App.TGPoint3()
				vLoc.SetXYZ(dWayData["Location"][0], dWayData["Location"][1], dWayData["Location"][2])
				if dWaypoints.has_key(dWayData["Name"]):
					pWayp = dWaypoints[ dWayData["Name"] ]
					pWayp.SetTranslate(vLoc)
					pWayp.UpdateNodeOnly()
					# to delete waypoints that are in this set but were not saved as in this set:
					# -uncomment following line
					# -make a FOR pWay in dWaypoints.values(), delete pWay from pSet
					#dWaypoints[ dWayData["Name"] ] = None
				else:
					pWayp = GalaxyLIB.CreateNAVPoint(dWayData["Name"], pSet, vLoc)
				pWayp.SetSpeed( dWayData["Speed"] )
				pWayp.SetStatic( dWayData["IsStatic"] )
				pWayp.SetNavPoint( dWayData["IsNavPoint"] )
			
			for dProjData in dSetData["Projectiles"]:
				if dShips.has_key(dProjData["Target Name"]):
					pTarget = dShips[ dProjData["Target Name"] ]
					iTargetID = pTarget.GetObjID()
				else:
					pTarget = None
					iTargetID = App.NULL_ID
				if dShips.has_key(dProjData["Parent Name"]):
					pParent = dShips[ dProjData["Parent Name"] ]
					iParentID = pParent.GetObjID()
				else:
					pParent = None
					iParentID = App.NULL_ID

				vPos = App.TGPoint3()
				vPos.SetXYZ(dProjData["Location"][0], dProjData["Location"][1], dProjData["Location"][2] )

				pTorp = App.Torpedo_Create( dProjData["Module"], vPos)
				pTorp.UpdateNodeOnly()

				pTorp.SetTarget(iTargetID)
				pTorp.SetTargetOffset(vPos)
				pTorp.SetParent(iParentID)

				pSet.AddObjectToSet(pTorp, None)
				pTorp.UpdateNodeOnly()

				vForward = App.TGPoint3()
				vForward.SetXYZ(dProjData["Forward Vec"][0], dProjData["Forward Vec"][1], dProjData["Forward Vec"][2] )
				vUp = App.TGPoint3()
				vUp.SetXYZ(dProjData["Up Vec"][0], dProjData["Up Vec"][1], dProjData["Up Vec"][2] )
				vVelocity = App.TGPoint3()
				vVelocity.SetXYZ(dProjData["Velocity"][0], dProjData["Velocity"][1], dProjData["Velocity"][2] )
				vAngVelocity = App.TGPoint3()
				vAngVelocity.SetXYZ(dProjData["Angular Velocity"][0], dProjData["Angular Velocity"][1], dProjData["Angular Velocity"][2] )
				vAccel = App.TGPoint3()
				vAccel.SetXYZ(dProjData["Acceleration"][0], dProjData["Acceleration"][1], dProjData["Acceleration"][2] )
				vAngAccel = App.TGPoint3()
				vAngAccel.SetXYZ(dProjData["Angular Acceleration"][0], dProjData["Angular Acceleration"][1], dProjData["Angular Acceleration"][2] )

				pTorp.AlignToVectors(vForward, vUp)
				pTorp.SetVelocity(vVelocity)
				pTorp.SetAngularVelocity(vAngVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
				pTorp.SetAcceleration(vAccel)
				pTorp.SetAngularAcceleration(vAngAccel)
				pTorp.SetMaxAngularAccel( dProjData["Max Angular Accel"] )
				pTorp.SetGuidanceLifetime( dProjData["Guidance Lifetime"] )
				pTorp.SetDamage( dProjData["Damage"] )
				pTorp.SetLifetime( dProjData["Lifetime"] )

				pTorp.UpdateNodeOnly()
		except:
			Galaxy.LogError("SavingSystem_Load: couldn't update set objects: "+str(dSetData["Module"]))

	##############
	### Reset RDFs timers and Set obj.
	for dRDFStats in pSaveModule.GalaxyLIB[0]["lRDFs"]:
		oID = dRDFStats["_RandomDefenceForce__timer"]
		if dRDFs.has_key(oID):
			pRDF = dRDFs[oID]
			try:
				pSetModule = __import__( dRDFStats["pSet"] )
				pSet = pSetModule.GetSet()
			except:
				pSet = None
			pRDF.pSet = pSet

			fTimeLeft = dRDFStats["_RandomDefenceForce__timer"]
			if fTimeLeft > 0:
				pTimer = CreateMethodTimer(pRDF.pEventHandler, "CreateShips", App.g_kUtopiaModule.GetGameTime() + fTimeLeft )
			else:
				pTimer = None
			pRDF.__dict__["_RandomDefenceForce__timer"] = pTimer

	##############
	### Reset RegionBattle conquer timers
	for sRegion in pSaveModule.Regions[0].keys():
		dRegData = pSaveModule.Regions[0][sRegion]
		pRegion = App.g_kRegionManager.GetRegion(sRegion)
		if pRegion != None:
			fTimeLeft = dRegData["RegionBattle"]["_RegionBattle__conquerTimer"] 
			if fTimeLeft > 0:
				pTimer = CreateMethodTimer(pRegion.RegionBattle.pEventHandler, "_conquerTimerVictory", App.g_kUtopiaModule.GetGameTime() + fTimeLeft )
			else:
				pTimer = None
			pRegion.RegionBattle.__dict__["_RegionBattle__conquerTimer"] = pTimer

	##############
	### Reset Ship AIs
	for pShipObj in dShips.values():
		if pShipObj.GetObjID() != iPlayerID:
			GalaxyLIB.ResetShipAI(pShipObj)
	
	########
	return 1

####################################################################################
# Saving Helpers
######################################################################################
def GetSystemStats(pSet):
	debug(__name__ + ", GetSystemStats")
	dStats = {}
	dStats["Module"] = pSet.GetRegionModule()
	dStats["Objects"] = []
	lObjects = pSet.GetClassObjectList(App.CT_OBJECT)
	lWaypoints = []
	lProjectiles = []
	for pObject in lObjects:
		if App.Waypoint_Cast(pObject) != None:
			lWaypoints.append(App.Waypoint_Cast(pObject))
		elif App.Torpedo_Cast(pObject) != None:
			lProjectiles.append(App.Torpedo_Cast(pObject))
		else:
			dStats["Objects"].append(pObject.GetName())
	dStats["Waypoints"] = []
	for pWaypoint in lWaypoints:
		dWaySta = {}
		dWaySta["Name"] = pWaypoint.GetName()
		dWaySta["Location"] = Get3DCoordList(pWaypoint.GetWorldLocation())
		dWaySta["IsNavPoint"] = pWaypoint.IsNavPoint()
		dWaySta["IsStatic"] = pWaypoint.IsStatic()
		dWaySta["Speed"] = pWaypoint.GetSpeed()
		dStats["Waypoints"].append(dWaySta)
	dStats["Projectiles"] = []
	for pProj in lProjectiles:
		dProj = {}
		dProj["Module"] = pProj.GetModuleName()
		pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pProj.GetTargetID()))
		if pTarget != None:
			dProj["Target Name"] = pTarget.GetName()
		else:
			dProj["Target Name"] = "None"
		pParent = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pProj.GetParentID()))
		if pParent != None:
			dProj["Parent Name"] = pParent.GetName()
		else:
			dProj["Parent Name"] = "None"
		dProj["Damage"] = pProj.GetDamage()
		dProj["Lifetime"] = pProj.GetLifetime()
		dProj["Guidance Lifetime"] = pProj.GetGuidanceLifeTime()
		dProj["Location"] = Get3DCoordList(pProj.GetWorldLocation())
		dProj["Forward Vec"] = Get3DCoordList(pProj.GetWorldForwardTG())
		dProj["Up Vec"] = Get3DCoordList(pProj.GetWorldUpTG())
		dProj["Velocity"] = Get3DCoordList( pProj.GetVelocityTG() )
		dProj["Angular Velocity"] = Get3DCoordList( pProj.GetAngularVelocityTG() )
		dProj["Acceleration"] = Get3DCoordList( pProj.GetAccelerationTG() )
		dProj["Angular Acceleration"] = Get3DCoordList( pProj.GetAngularAccelerationTG() )
		dProj["Max Angular Accel"] = pProj.GetMaxAngularAccel()
		dStats["Projectiles"].append(dProj)
	return dStats

def GetShipStats(pShip):
	debug(__name__ + ", GetShipStats")
	pPlayer = App.Game_GetCurrentPlayer()
	bIsPlayer = 0
	if pPlayer != None:
		if pPlayer.GetObjID() == pShip.GetObjID():
			bIsPlayer = 1
	dStats = {}
	# general stats
	dStats["Ship Name"] = pShip.GetName()
	dStats["Ship Class"] = GalaxyLIB.GetShipType(pShip)
	dStats["Ship Group"] = GetShipGroup(pShip)
	dStats["Is Player"] = bIsPlayer
	dStats["Location"] = Get3DCoordList(pShip.GetWorldLocation())
	dStats["Forward Vec"] = Get3DCoordList(pShip.GetWorldForwardTG())
	dStats["Up Vec"] = Get3DCoordList(pShip.GetWorldUpTG())
	dStats["Warp Speed"] = pShip.GetWarpSpeed()  #dunno if this will be needed, if we save the Travel classes.
	dStats["Velocity"] = Get3DCoordList( pShip.GetVelocityTG() )
	dStats["Angular Velocity"] = Get3DCoordList( pShip.GetAngularVelocityTG() )
	dStats["Acceleration"] = Get3DCoordList( pShip.GetAccelerationTG() )
	dStats["Angular Acceleration"] = Get3DCoordList( pShip.GetAngularAccelerationTG() )
	pSet = pShip.GetContainingSet()
	if pSet != None:
		dStats["In System"] = pSet.GetRegionModule()
	else:
		dStats["In System"] = "None"
	if pShip.GetTarget() != None:
		dStats["Target Name"] = pShip.GetTarget().GetName()
	else:
		dStats["Target Name"] = "None"
	dStats["Is Cloaked"] = pShip.IsCloaked()
	dStats["Alert Level"] = pShip.GetAlertLevel()
	dStats["Scale"] = pShip.GetScale()
	dStats["Is Scannable"] = pShip.IsScannable()
	dStats["Is Hailable"] = pShip.IsHailable()
	dStats["Is Hidden"] = pShip.IsHidden()
	dStats["Is Static"] = pShip.IsStatic()
	dStats["Collision Flags"] = pShip.GetCollisionFlags()
	dStats["Is Targetable"] = pShip.IsTargetable()
	dStats["Is Invincible"] = pShip.IsInvincible()
	dStats["Is Hurtable"] = pShip.IsHurtable()
	
	# general subsystem stats
	dStats["Subsystems"] = {}
	pPropSet = pShip.GetPropertySet()
	pSubsystemList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
	pSubsystemList.TGBeginIteration()
	for i in range(pSubsystemList.TGGetNumItems()):
		pProperty = App.SubsystemProperty_Cast(pSubsystemList.TGGetNext().GetProperty())
		sName = pProperty.GetName().GetCString()
		pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
		if pSubsystem != None:
			dStats["Subsystems"][sName] = {}
			dStats["Subsystems"][sName]["Condition"] = pSubsystem.GetCondition()
			pPoweredSys = App.PoweredSubsystem_Cast(pSubsystem)
			if pPoweredSys != None:
				dStats["Subsystems"][sName]["Is On"] = pPoweredSys.IsOn()
				dStats["Subsystems"][sName]["Power Wanted"] = pPoweredSys.GetPowerPercentageWanted()
			pWeapon = App.EnergyWeapon_Cast(pSubsystem)
			if pWeapon != None:
				dStats["Subsystems"][sName]["Charge Level"] = pWeapon.GetChargeLevel()
			pPowerSys = App.PowerSubsystem_Cast(pSubsystem)
			if pPowerSys != None:
				dStats["Subsystems"][sName]["Available Power"] = pPowerSys.GetAvailablePower()
				dStats["Subsystems"][sName]["Main Battery Power"] = pPowerSys.GetMainBatteryPower()
				dStats["Subsystems"][sName]["Backup Battery Power"] = pPowerSys.GetBackupBatteryPower()
			pShields = App.ShieldClass_Cast(pSubsystem)
			if pShields != None:
				dStats["Subsystems"][sName]["Shield Stats"] = []
				for iShield in range(App.ShieldClass.NUM_SHIELDS):
					dStats["Subsystems"][sName]["Shield Stats"].append(pShields.GetCurShields(iShield))
			pSensors = App.SensorSubsystem_Cast(pSubsystem)
			if pSensors != None:
				dStats["Subsystems"][sName]["Probe Count"] = pSensors.GetNumProbes()
			pTractors = App.TractorBeamSystem_Cast(pSubsystem)
			if pTractors != None:
				dStats["Subsystems"][sName]["Tractor Mode"] = pTractors.GetMode()
			pTorpSys = App.TorpedoSystem_Cast(pSubsystem)
			if pTorpSys != None:
				dStats["Subsystems"][sName]["Available Ammos"] = {}
				for i in range(pTorpSys.GetNumAmmoTypes()):
					pAmmoType = pTorpSys.GetAmmoType(i)
					dStats["Subsystems"][sName]["Available Ammos"][pAmmoType.GetTorpedoScript()] = pTorpSys.GetNumAvailableTorpsToType(i)
					# to load and deduct torps:
					# before deducting, check for torpedo script/ammo type num of the ship's torp system, in case they were changed.
					# iMax = torps.GetAmmoType(i).GetMaxTorpedoes()
					# iAvailable = saved value
					# torps.LoadAmmoType(i, -(iMax - iAvailable) )
	pSubsystemList.TGDoneIterating()
	pSubsystemList.TGDestroy()

	# Now, we would save up the Traveler System stats about this ship.
	# However, since we would save it mainly so ships that are traveling will remain travelling when loaded in the Load saved game process, and since
	# the Traveler system is pretty complicated (more complex than the War Simulator by the way), i've decided that for now, we won't save it.
	# Pratically all of it's stats either don't get changed, or get changed when a ship is going to travel: thus, if she's going to travel again, 
	# they'll get updated again. Pratically eliminating the need to saving the stats.
	# And also because of this complexity of the Traveler System, loading it from a saved game would be even more complicated...
	# So my decision is to leave that (unfinished) code below, incase we do get around to make it save later, and while we're not saving it, make that
	# the game can only be saved when NO SHIPs are travelling. And make ships stop warp intercept before saving.
	#pTravel = App.g_kTravelManager.GetTravel(pShip)
	#if pTravel != None:
	#	dStats["Traveler Stats"] = {}
	#	dStats["Traveler Stats"]["Destination"] = pTravel.GetDestination()
	#	dStats["Traveler Stats"]["Travel Type"] = pTravel.GetTravelType()
	#	dStats["Traveler Stats"]["Speed"] = pTravel.GetSpeed()
	#	dStats["Traveler Stats"]["Towing Enabled"] = pTravel.EnableTowing
	#	dStats["Traveler Stats"]["Travel Blindly"] = pTravel.IsTravelBlindly()
	#	dStats["Traveler Stats"]["Travel"] = pTravel.IsTravelBlindly()
	#else:
	#	dStats["Traveler Stats"] = "None"
	return dStats

def GetWarSimStats():
	# for the War Simulator and WSShip, we pretty much return the exact copy of the obj attributes dict. However, we leave some of those values out,
	# since they are pretty much static, or are other obj instances which will be re-created and re-set anyways.
	debug(__name__ + ", GetWarSimStats")
	dWar = GalacticWarSimulator.WarSimulator.__dict__.copy()
	del dWar["CLASS"]
	del dWar["Refresher"]
	del dWar["pEventHandler"]
	del dWar["dShipClassesCost"]
	del dWar["BattleEndedSound"]
	dWar["dShips"] = {}
	for sShipName in GalacticWarSimulator.WarSimulator.dShips.keys():
		pWSShip = GalacticWarSimulator.WarSimulator.dShips[sShipName]
		dWSShipAttrs = CopyDict( pWSShip.__dict__ )
		dWar["dShips"][sShipName] = dWSShipAttrs
		del dWar["dShips"][sShipName]["CLASS"]
		del dWar["dShips"][sShipName]["_WSShip__isDockedInBase"]
		del dWar["dShips"][sShipName]["_WSShip__occupiedShipName"]
		pRace = dWar["dShips"][sShipName]["Race"]
		del dWar["dShips"][sShipName]["Race"]
		if pRace != None:
			dWar["dShips"][sShipName]["Race"] = pRace.GetRaceName()
		else:
			dWar["dShips"][sShipName]["Race"] = "None"
		del dWar["dShips"][sShipName]["Ship"]
		del dWar["dShips"][sShipName]["pEventHandler"]
		try:
			del dWar["dShips"][sShipName]["O_DESTROYED"]
			del dWar["dShips"][sShipName]["O_NOTHING"]
			del dWar["dShips"][sShipName]["O_DEFEND"]
			del dWar["dShips"][sShipName]["O_ATTACK"]
		except:
			pass
	return dWar

def GetFleetStats():
	# for the FleetManager and fleets, we get basically everything.
	# remember, the dRacesIndexValues is a static variable from ShipFleet, it gotta be the first to be "loaded"
	# and then deleted from this dict.
	debug(__name__ + ", GetFleetStats")
	dStats = GalacticWarSimulator.FleetManager.__dict__.copy()
	del dStats["CLASS"]
	dStats["dRacesIndexValues"] = CopyDict( GalacticWarSimulator.ShipFleet.dRacesIndexValues )
	dStats["dFleetIDs"] = {}   #fleet name = shipfleet
	for sFleetName in GalacticWarSimulator.FleetManager.dFleetIDs.keys():
		pFleet = GalacticWarSimulator.FleetManager.dFleetIDs[sFleetName]
		dFleetAttrs = CopyDict( pFleet.__dict__ )
		dStats["dFleetIDs"][sFleetName] = dFleetAttrs 
		del dStats["dFleetIDs"][sFleetName]["CLASS"]
		del dStats["dFleetIDs"][sFleetName]["Logger"]
		try:
			del dStats["dFleetIDs"][sFleetName]["IDLE"]
			del dStats["dFleetIDs"][sFleetName]["ACTIVE"]
		except:
			pass
	return dStats

def GetRegionsStats():
	# for the Region (System plugin + set plugins) and RegionBattle objs, we do pratically the same thing we did with the WarSim:
	# copy the obj's dict, taking out some stuff we don't wanna saved.
	# no need to store the RegionManager attributes, since the only one important are the regions, which we'll already save.
	debug(__name__ + ", GetRegionsStats")
	lRegions = App.g_kRegionManager.GetAllRegions()
	dStats = {}
	for pRegion in lRegions:
		dStats[pRegion.GetName()] = CopyDict(pRegion.__dict__)
		del dStats[pRegion.GetName()]["Menu"]
		del dStats[pRegion.GetName()]["CLASS"]
		del dStats[pRegion.GetName()]["Location"]
		oPos = pRegion.GetLocation()
		if type(oPos) == type([]) or type(oPos) == type(""):
			dStats[pRegion.GetName()]["Location"] = oPos
		else:
			dStats[pRegion.GetName()]["Location"] = Get2DCoordList(pRegion.GetLocation())
		dStats[pRegion.GetName()]["Description"] = string.replace(dStats[pRegion.GetName()]["Description"], "\n", "<%NL%>")
		del dStats[pRegion.GetName()]["BorderSet"]
		lSets = pRegion.GetAllSets()
		dStats[pRegion.GetName()]["Sets"] = {}
		for pSetPlug in lSets:
			dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()] = CopyDict(pSetPlug.__dict__)
			del dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()]["CLASS"]
			del dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()]["ParentRegion"]
			del dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()]["__name__"]
			del dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()]["__file__"]
			del dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()]["__builtins__"]
			del dStats[pRegion.GetName()]["Sets"][pSetPlug.GetName()]["__doc__"]

		pRegionBattle = dStats[pRegion.GetName()]["RegionBattle"]
		dStats[pRegion.GetName()]["RegionBattle"] = CopyDict(pRegionBattle.__dict__)
		del dStats[pRegion.GetName()]["RegionBattle"]["CLASS"]
		try:
			del dStats[pRegion.GetName()]["RegionBattle"]["NOT_IN_BATTLE"]
			del dStats[pRegion.GetName()]["RegionBattle"]["DEFENCE_FORCE"]
			del dStats[pRegion.GetName()]["RegionBattle"]["ATTACK_FORCE"]
			del dStats[pRegion.GetName()]["RegionBattle"]["lBattleList"]
		except:
			pass
		del dStats[pRegion.GetName()]["RegionBattle"]["pEventHandler"]
		del dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__region"]
		# these both dicts are "string": WSShip obj... retain only the ship's names, or don't save these dicts altogether since we can see where a 
		# ship is stationed by her order/assigned to attributes.
		#RegionBattle.__defenceForce = {}
		#RegionBattle.__attackForce = {}
		del dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__defenceForce"]
		del dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__attackForce"]

		# these following objs tho will need special care:
		# for the conquer timer (and other timers), store his start/delay/duration, and calculate time passed already of it. When loading, we'll 
		#  recreate the timer and apply these values/time left to trigger.
		# for the RDF/RAF, do the same as for other objs: copy it's attribute dict. however remember to handle with care her timer and attributes we
		#  don't wanna saved too.
		#RegionBattle.__RDF = None
		#RegionBattle.__RAF = None
		#RegionBattle.__conquerTimer = None
		pRDF = dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__RDF"]
		del dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__RDF"]
		if pRDF != None:
			dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__RDF"] = pRDF.GetObjID()
		pRAF = dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__RAF"]
		del dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__RAF"]
		if pRAF != None:
			dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__RAF"] = pRAF.GetObjID()
		fTimeLeft = pRegionBattle.GetTimeLeftForTimer()
		dStats[pRegion.GetName()]["RegionBattle"]["_RegionBattle__conquerTimer"] = fTimeLeft
	return dStats

def GetGCLIBStats():
	# just to save some global values from the GalaxyLIB script which we need saved. Most importantly, the RDFs and IDs created.
	debug(__name__ + ", GetGCLIBStats")
	dStats = {}
	dStats["iRDFshipCreated"] = GalaxyLIB.iRDFshipCreated
	dStats["CreatedIDsList"] = GalaxyLIB.CreatedIDsList
	dStats["lRDFs"] = []
	for pRDF in GalaxyLIB.lRDFs:
		dRDFStats = CopyDict(pRDF.__dict__)
		del dRDFStats["lShips"]
		del dRDFStats["pEventHandler"]
		dRDFStats["_RandomDefenceForce__timer"] = pRDF.GetTimeLeftForTimer()
		dRDFStats["pSet"] = pRDF.pSet.GetRegionModule()

		dStats["lRDFs"].append(dRDFStats)
	return dStats

def GetRaceStats():
	# in here we get the stats of each race. Much like we the Region stats: copy the dict, take out un-needed stuff.
	debug(__name__ + ", GetRaceStats")
	dStats = {}
	for sRaceName in Custom.QBautostart.Libs.Races.Races.keys():
		pRaceObj = Custom.QBautostart.Libs.Races.Races[sRaceName]
		dStats[sRaceName] = CopyDict(pRaceObj.__dict__)
		del dStats[sRaceName]["dWSShips"]
	return dStats

#######################################################################################
# Loading Helpers
#######################################################################################
def CreateShip(dShipData):
	debug(__name__ + ", CreateShip")
	global lIgnoreObjDestroyed, lIgnoreExitedSet, lIgnoreObjCreated, lIgnoreEnteredSet

	sShipName = dShipData["Ship Name"]
	sShipType = dShipData["Ship Class"]
	try:
		pSetModule = __import__( dShipData["In System"] )
		pSet = pSetModule.GetSet()
	except:
		pSet = None
	pShipDef = GalaxyLIB.GetShipDefByScript(sShipType)
	if pShipDef == None or pSet == None:
		return None

	pOldShip = MissionLib.GetShip(sShipName, bAnySet = 1)
	if pOldShip:
		pPlayer = App.Game_GetCurrentPlayer()
		if pPlayer != None:
			if pPlayer.GetObjID() == pOldShip.GetObjID():
				# I think this is needed, as MissionLib's CreatePlayerShip function does.
				MissionLib.DetachCrewMenus()
		pOldSet = pOldShip.GetContainingSet()
		lIgnoreObjDestroyed.append(pOldShip.GetName())
		lIgnoreExitedSet.append(pOldShip.GetName())
		pOldSet.RemoveObjectFromSet(pOldShip.GetName())
		pOldShip.RemoveVisibleDamage()

	lIgnoreObjCreated.append(sShipName)
	lIgnoreEnteredSet.append(sShipName)
	pShip = loadspacehelper.CreateShip(sShipType, pSet, sShipName, "", 0)
	if not pShip:
		# really strange... ship wasn't created...
		return

	vPos = App.TGPoint3()
	vPos.SetXYZ(dShipData["Location"][0], dShipData["Location"][1], dShipData["Location"][2] )
	vForward = App.TGPoint3()
	vForward.SetXYZ(dShipData["Forward Vec"][0], dShipData["Forward Vec"][1], dShipData["Forward Vec"][2] )
	vUp = App.TGPoint3()
	vUp.SetXYZ(dShipData["Up Vec"][0], dShipData["Up Vec"][1], dShipData["Up Vec"][2] )
	vVelocity = App.TGPoint3()
	vVelocity.SetXYZ(dShipData["Velocity"][0], dShipData["Velocity"][1], dShipData["Velocity"][2] )
	vAngVelocity = App.TGPoint3()
	vAngVelocity.SetXYZ(dShipData["Angular Velocity"][0], dShipData["Angular Velocity"][1], dShipData["Angular Velocity"][2] )
	vAccel = App.TGPoint3()
	vAccel.SetXYZ(dShipData["Acceleration"][0], dShipData["Acceleration"][1], dShipData["Acceleration"][2] )
	vAngAccel = App.TGPoint3()
	vAngAccel.SetXYZ(dShipData["Angular Acceleration"][0], dShipData["Angular Acceleration"][1], dShipData["Angular Acceleration"][2] )

	pShip.SetTranslate(vPos)
	pShip.AlignToVectors(vForward, vUp)
	pShip.SetVelocity(vVelocity)
	pShip.SetAngularVelocity(vAngVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
	pShip.SetAcceleration(vAccel)
	pShip.SetAngularAcceleration(vAngAccel)
	pShip.SetWarpSpeed( dShipData["Warp Speed"] )
	

	pFriendlies = MissionLib.GetFriendlyGroup()
	pEnemies = MissionLib.GetEnemyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()

	if pFriendlies and pFriendlies.IsNameInGroup(pShip.GetName()):
		pFriendlies.RemoveName(pShip.GetName())
	if pEnemies and pEnemies.IsNameInGroup(pShip.GetName()):
		pEnemies.RemoveName(pShip.GetName())
	if pNeutrals and pNeutrals.IsNameInGroup(pShip.GetName()):
		pNeutrals.RemoveName(pShip.GetName())

	sAllegiance = dShipData["Ship Group"]
	if sAllegiance == "Enemy":
		if pEnemies:
			pEnemies.AddName(pShip.GetName())
	elif sAllegiance == "Friendly":
		if pFriendlies:
			pFriendlies.AddName(pShip.GetName())
	elif sAllegiance == "Neutral":
		if pNeutrals:
			pNeutrals.AddName(pShip.GetName())

	ApplyShipSubsystemData(pShip, dShipData["Subsystems"])
	pShip.SetScale( dShipData["Scale"] )
	pShip.SetScannable( dShipData["Is Scannable"] )
	pShip.SetHailable( dShipData["Is Hailable"] )
	pShip.SetHidden( dShipData["Is Hidden"] )
	pShip.SetStatic( dShipData["Is Static"] )
	pShip.SetCollisionFlags( dShipData["Collision Flags"] )
	pShip.SetTargetable( dShipData["Is Targetable"] )
	pShip.SetInvincible( dShipData["Is Invincible"] )
	pShip.SetHurtable( dShipData["Is Hurtable"] )
	pShip.SetAlertLevel( dShipData["Alert Level"] )

	pShip.UpdateNodeOnly()
	return pShip

def ApplyShipSubsystemData(pShip, dSubsystems):
	debug(__name__ + ", ApplyShipSubsystemData")
	for sSubsystemName in dSubsystems.keys():
		dSysStats = dSubsystems[sSubsystemName]
		pSubsystem = MissionLib.GetSubsystemByName(pShip, sSubsystemName)
		if pSubsystem != None:
			pSubsystem.SetCondition( dSysStats["Condition"] )
			pPoweredSys = App.PoweredSubsystem_Cast(pSubsystem)
			if pPoweredSys != None:
				pPoweredSys.Turn(dSysStats["Is On"])
				pPoweredSys.SetPowerPercentageWanted(dSysStats["Power Wanted"])
			pWeapon = App.EnergyWeapon_Cast(pSubsystem)
			if pWeapon != None:
				pWeapon.SetChargeLevel(dSysStats["Charge Level"])
			pPowerSys = App.PowerSubsystem_Cast(pSubsystem)
			if pPowerSys != None:
				pPowerSys.SetAvailablePower(dSysStats["Available Power"])
				pPowerSys.SetMainBatteryPower(dSysStats["Main Battery Power"])
				pPowerSys.SetBackupBatteryPower(dSysStats["Backup Battery Power"])
			pShields = App.ShieldClass_Cast(pSubsystem)
			if pShields != None:
				for iShield in range(App.ShieldClass.NUM_SHIELDS):
					pShields.SetCurShields(iShield, dSysStats["Shield Stats"][iShield])
			pSensors = App.SensorSubsystem_Cast(pSubsystem)
			if pSensors != None:
				pSensors.SetNumProbes(dSysStats["Probe Count"])
			pTractors = App.TractorBeamSystem_Cast(pSubsystem)
			if pTractors != None:
				pTractors.SetMode(dSysStats["Tractor Mode"])
			pTorpSys = App.TorpedoSystem_Cast(pSubsystem)
			if pTorpSys != None:
				for i in range(pTorpSys.GetNumAmmoTypes()):
					pAmmoType = pTorpSys.GetAmmoType(i)
					sTorpScript = pAmmoType.GetTorpedoScript()
					if dSysStats["Available Ammos"].has_key(sTorpScript):
						iMaxNum = pAmmoType.GetMaxTorpedoes()
						iAvailableNum = dSysStats["Available Ammos"][sTorpScript]
						pTorpSys.LoadAmmoType(i, -(iMaxNum - iAvailableNum) )

##################################################################
# General Helpers
##################################################################
def Get3DCoordList(vPos):
	debug(__name__ + ", Get3DCoordList")
	return [vPos.x, vPos.y, vPos.z]

def Get2DCoordList(vPos):
	debug(__name__ + ", Get2DCoordList")
	return [vPos.x, vPos.y]

def GetShipGroup(pShip):
	debug(__name__ + ", GetShipGroup")
	sShipName = pShip.GetName()
	pFriendlies = MissionLib.GetFriendlyGroup()
	pEnemies = MissionLib.GetEnemyGroup()
	pNeutrals = MissionLib.GetNeutralGroup()
	if pFriendlies and pFriendlies.IsNameInGroup(sShipName):
		return "Friendly"
	elif pEnemies and pEnemies.IsNameInGroup(sShipName):
		return "Enemy"
	elif pNeutrals and pNeutrals.IsNameInGroup(sShipName):
		return "Neutral"
	return "Neutral"

def GetTabPrefix(iTabNum):
	debug(__name__ + ", GetTabPrefix")
	ret = ""
	for i in range(iTabNum):
		ret = ret + "\t"
	return ret

def GetDataListFromDict(dData, iTabNum = 0):
	debug(__name__ + ", GetDataListFromDict")
	lStrs = [GetTabPrefix(iTabNum)+"{"]
	for k in dData.keys():
		if type(k) == type(1) or type(k) == type(1.0):
			sLine = GetTabPrefix(iTabNum)+str(k)+": "
		else:
			sLine = GetTabPrefix(iTabNum)+"\""+str(k)+"\": "
		oData = dData[k]
		if type(oData) == type({}):
			lDataList = GetDataListFromDict(oData, iTabNum + 1)
			del lDataList[0]
			sLine = sLine + "{"
			lStrs.append(sLine)
			for s in lDataList:
				lStrs.append(s)
		elif type(oData) == type([]):
			sLine = sLine + "["
			for i in oData:
				if type(i) == type(1) or type(i) == type(1.0):
					sLine = sLine + str(i) + ", "
				elif type(i) == type({}):
					lDictLines = GetDataListFromDict(i, iTabNum + 1)
					for sd in lDictLines:
						sLine = sLine + "\n" + sd
				elif type(i) == type([]):
					sLine = sLine + str(i) + ", "
				else:
					sLine = sLine + "\"" + str(i) + "\", "
			sLine = sLine + "],"
			lStrs.append(sLine)
		elif type(oData) == type(1) or type(oData) == type(1.0):
			lStrs.append(sLine + str(oData) + ",")
		else:
			lStrs.append(sLine + "\"" + str(oData) + "\",")
	lStrs.append(GetTabPrefix(iTabNum)+"},")
	return lStrs

def CopyDict(dict):
	debug(__name__ + ", CopyDict")
	d = {}
	for k in dict.keys():
		d[k] = dict[k]
	return d

def IsLoading():
	debug(__name__ + ", IsLoading")
	global bIsLoading
	return bIsLoading