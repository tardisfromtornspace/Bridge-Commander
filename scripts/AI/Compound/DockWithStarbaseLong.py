from bcdebug import debug
import App
import MissionLib
import Actions.CameraScriptActions
import Actions.ShipScriptActions
import Camera
import Lib.LibEngineering

#NonSerializedObjects = ( "debug", )

#debug = App.CPyDebug(__name__).Print
#debug("Loading " + __name__ + " AI module...")

# Info for the AI editor:
# AIFlag(NoRepair) OnOff
# AIFlag(FadeEnd) OnOff
g_kRestoreTranslateDict = {}
g_dRestoreScaleDict = {}
g_bPlayerDockedOnce = 0
NO_COLLISION_MESSAGE = 192
SUBSYSTEM_SET_CONDITION = 194
SET_SHIELD_CONDITION = 199

def MultiPlayerEnableCollisionWith(pObject1, pObject2, CollisionOnOff):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", MultiPlayerEnableCollisionWith")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(NO_COLLISION_MESSAGE))
        
        # send Message
        kStream.WriteInt(pObject1.GetObjID())
        kStream.WriteInt(pObject2.GetObjID())
        kStream.WriteInt(CollisionOnOff)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def MPSendSubsystemCondition(iShipObjID, sSubsystenName, iNewCondition):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", MPSendSubsystemCondition")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SUBSYSTEM_SET_CONDITION))
        
        # send Message
        kStream.WriteInt(iShipObjID)
        for i in range(len(sSubsystenName)):
                kStream.WriteChar(sSubsystenName[i])
        # set the last char:
        kStream.WriteChar('\0')
        kStream.WriteInt(iNewCondition)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()
        

def MPSendShieldCondition(iShipObjID, iShield, iNewCondition):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", MPSendShieldCondition")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SET_SHIELD_CONDITION))
        
        # send Message
        kStream.WriteInt(iShipObjID)
        kStream.WriteInt(iShield)
        kStream.WriteInt(iNewCondition)

        pMessage = App.TGMessage_Create()
        # Yes, this is a guaranteed packet
        pMessage.SetGuaranteed(1)
        # Okay, now set the data from the buffer stream to the message
        pMessage.SetDataFromStream(kStream)
        # Send the message to everybody but me.  Use the NoMe group, which
        # is set up by the multiplayer game.
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def InStarbaseRange(pShip, pStarbase):
        debug(__name__ + ", InStarbaseRange")
        vDifference = pStarbase.GetWorldLocation()
        vDifference.Subtract(pShip.GetWorldLocation())
        if vDifference.Length() < pStarbase.GetRadius():
                return 1
        return 0
        
        
def RepairSubsystem(pAction, pShip, pSubsystem, pStarbase):
        debug(__name__ + ", RepairSubsystem")
        iShipObjID = pShip.GetObjID()
        
        # check if the ship does still exist
        pShip = App.ShipClass_GetObjectByID(None, iShipObjID)
        if not pShip:
                return 1
        if not InStarbaseRange(pShip, pStarbase):
                print "Ship not inside Starbase - bye"
                return 1
        
        if pSubsystem.GetCondition() + 1000 <= pSubsystem.GetMaxCondition():
                iNewCondition = pSubsystem.GetCondition() + 1000
        else:

                iNewCondition = pSubsystem.GetMaxCondition()
                
        if not App.g_kUtopiaModule.IsHost():
                MPSendSubsystemCondition(iShipObjID, pSubsystem.GetName(), iNewCondition)
        else:
                pSubsystem.SetCondition(iNewCondition)
                
        return 0
        
        
###############################################################################
#	RepairSubsystemFully(pAction, iSubsystemID)
#	
#	Repairs a subsystem, and all of its children, fully.
#	
#	Args:	pAction			- the script action, passed in automatically
#			iSubsystemID	- the ID of the subsystem being affected
#	
#	Return:	zero for end.
###############################################################################
def RepairSubsystemFully(pShip, iSubsystemID, pStarbase):
	debug(__name__ + ", RepairSubsystemFully")
	"Repairs a single subsystem and its children fully."
        pSeq = App.TGSequence_Create()

	pSubsystem = App.ShipSubsystem_Cast(App.TGObject_GetTGObjectPtr(iSubsystemID))

	if (pSubsystem == None):
		return pSeq

        points = pSubsystem.GetRepairPointsNeeded()
        timeNeeded = 2
        while(points > 0):
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RepairSubsystem", pShip, pSubsystem, pStarbase), timeNeeded)
                points = points - 1000
	iChildren = pSubsystem.GetNumChildSubsystems()

	if (iChildren > 0):
		# Fix all child subsystems.
		for iIndex in range(iChildren):
			pChild = pSubsystem.GetChildSubsystem(iIndex)
                        points = pChild.GetRepairPointsNeeded()
                        while(points > 0):
                                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "RepairSubsystem", pShip, pChild, pStarbase), timeNeeded)
                                points = points - 1000
                                
	return pSeq


###############################################################################
#	RepairShipFully(pAction, iShipID)
#	
#	Repairs a ship fully. All subsystems are restored to full health.
#	
#	Args:	pAction			- the script action, passed in automatically
#			iShipID			- the ID of the ship being affected
#	
#	Return:	zero for end.
###############################################################################
def RepairShipFully(iShipID, pStarbase):
	debug(__name__ + ", RepairShipFully")
	"Repairs a ship fully. Every subsystem is restored to full health."
        pSeq = App.TGSequence_Create()

	pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(iShipID))

	if(pShip is None):
		return pSeq

	# Iterate over all the subsystems of the ship.
	pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
	pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

	while (pSubsystem != None):
		pSeq.AppendAction(RepairSubsystemFully(pShip, pSubsystem.GetObjID(), pStarbase))
		pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

	pShip.EndGetSubsystemMatch(pIterator)

	# Set all of ship's shields to max.
	pShields = pShip.GetShields()

	if (pShields != None):
		for ShieldDir in range(App.ShieldClass.NUM_SHIELDS):
                        if App.g_kUtopiaModule.IsHost():
			        pShields.SetCurShields(ShieldDir, pShields.GetMaxShields(ShieldDir))
                        else:
                                MPSendShieldCondition(iShipID, ShieldDir, pShields.GetMaxShields(ShieldDir))

	# Set the power of the ship to max.
	pPower = pShip.GetPowerSubsystem()
	if (pPower != None):
		pPower.SetMainBatteryPower(pPower.GetMainBatteryLimit())
		pPower.SetBackupBatteryPower(pPower.GetBackupBatteryLimit())

	# Fix visible damage.
	pShip.RemoveVisibleDamage()

	# Replenish probe supply.
	pSensors = pShip.GetSensorSubsystem()
	if pSensors:
		pProp = pSensors.GetProperty()
		if pProp:
			pSensors.SetNumProbes(pProp.GetMaxProbes())

	return pSeq


def DockStarbase(pAction, pShip, pStarbase, pGraffAction = None, bNoRepair = 0, bFadeEnd = 1):
	# Get Player
	debug(__name__ + ", DockStarbase")
	pPlayer = MissionLib.GetPlayer()
	if pPlayer is None:
		return 0

	# Take down Helm menu and turn character back.
	pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet("bridge"))
	pHelm = App.CharacterClass_GetObject (pBridgeSet, "Helm")
	if pHelm and pPlayer.GetObjID() == pShip.GetObjID():
	        pHelm.MenuDown()
	        pHelm.TurnBack()

	# Setup a sequence for Graff's stuff.
	pSequence = App.TGSequence_Create()

	# Make sure the rendered set is the Bridge.
        if pBridgeSet and pPlayer.GetObjID() == pShip.GetObjID():
	        sOldSet = App.g_kSetManager.GetRenderedSet().GetName()
	        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", "bridge"))

	        # Set the viewscreen to watch Graff.
	        pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "ViewscreenOn", "FedOutpostSet_Graff", "Graff"))

	# Have Graff say his greeting.
        if pBridgeSet and pPlayer.GetObjID() == pShip.GetObjID():
	        if pGraffAction is None:
		        pSequence.AppendAction(App.TGScriptAction_Create("Bridge.Characters.Graff", "SayGreeting"))
	        else:
                        # debug("Triggering custom Graff action.")
		        pSequence.AppendAction(pGraffAction)
	
	# Fade out...  Something else will fade us back in later.
	#if bFadeEnd:
	#	pSequence.AppendAction( App.TGScriptAction_Create("MissionLib", "FadeOut") )

	# Turn off the viewscreen.
        if pBridgeSet and pPlayer.GetObjID() == pShip.GetObjID():
	        pSequence.AppendAction(App.TGScriptAction_Create("MissionLib", "ViewscreenOff"))

	        # Change the rendered set back to whatever it used to be.
	        pSequence.AppendAction(App.TGScriptAction_Create("Actions.CameraScriptActions", "ChangeRenderedSet", sOldSet), 0.5)

	# Automatically reload & repair the player's ship.
	if not bNoRepair:
		pSequence.AppendAction(RepairShipFully(pShip.GetObjID(), pStarbase))
	pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "ReloadShip", pShip.GetObjID()), 5)

	# pAction is done when pSequence is done.
	pDoneEvent = App.TGObjPtrEvent_Create()
	pDoneEvent.SetEventType(App.ET_ACTION_COMPLETED)
	pDoneEvent.SetDestination(App.g_kTGActionManager)
	pDoneEvent.SetObjPtr(pAction)
	pSequence.AddCompletedEvent(pDoneEvent)

	pSequence.Play()

	return 1


def SetupCutscene(pShip, sStarbase):
	debug(__name__ + ", SetupCutscene")
	pSet = pShip.GetContainingSet()
	pStarbase = App.ShipClass_GetObject(pSet, sStarbase)
	if not pStarbase:
#		debug("No starbase %s in set %s" % (sStarbase, pSet.GetName()))
		return

	# Change to a cinematic camera, and watch the ship fly in.
	MissionLib.StartCutscene(None)
	Actions.CameraScriptActions.CutsceneCameraBegin(None, pSet.GetName(), "DockingCam")

	# Switch to the cinematic window.
	pTopWindow = App.TopWindow_GetTopWindow()
	pFocus = pTopWindow.GetFocus()
	pCinematic = pTopWindow.FindMainWindow(App.MWT_CINEMATIC)
	if (not pFocus)  or  (pFocus.GetObjID() != pCinematic.GetObjID()):
		# Cinematic window isn't in focus yet.
		pTopWindow.ToggleCinematicWindow()

	pFirstCameraWaypoint = SetupCameraSweepWaypoints(pStarbase, "DockingCameraSweep")
	if pFirstCameraWaypoint:
		Camera.Placement(pFirstCameraWaypoint.GetName(), pShip.GetName(), pSet.GetName())

	App.g_kSetManager.MakeRenderedSet(pSet.GetName())

	# Disable collisions between the ship and the starbase.
	#pShip.EnableCollisionsWith(pStarbase, 0)

	if pShip.GetRadius() > 4.0:
		# Ship's too big to fit through the doors.  Shrink it.
		g_dRestoreScaleDict[pShip.GetObjID()] = pShip.GetScale()
		pShip.SetScale( pShip.GetScale() * 4.0 / pShip.GetRadius() )

def SetupDockPositions(pShip, sStarbase):
	# Move the ship to the "Docking Entry" waypoint.
	debug(__name__ + ", SetupDockPositions")
	pSet = pShip.GetContainingSet()
	pStarbase = App.ShipClass_GetObject(pSet, sStarbase)
	if not pStarbase:
#		debug("No starbase %s in set %s" % (sStarbase, pSet.GetName()))
		return

	pDockingEntry = App.PlacementObject_GetObject(pSet, "Docking Entry")

	vZero = App.TGPoint3()
	vZero.SetXYZ(0, 0, 0)
	pShip.SetVelocity(vZero)
	pShip.SetAngularVelocity(vZero, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)
	pShip.PlaceObjectByName("Docking Entry")
	pShip.UpdateNodeOnly()

	# Make sure no other ships are nearby.
	pProx = pSet.GetProximityManager()
	pIter = pProx.GetNearObjects(pDockingEntry.GetWorldLocation(), 300.0)
	pObject = pProx.GetNextObject(pIter)

	global g_kRestoreTranslateDict
	kRestoreDict = {}
	g_kRestoreTranslateDict [pShip.GetObjID ()] = kRestoreDict

	while pObject:
		if pObject.GetObjID() not in (pShip.GetObjID(), pStarbase.GetObjID()):
			# It's not the ship and it's not the starbase.  Move it away.
#			debug("Moving object %s away from docking zone." % pObject.GetName())

			vDiff = pObject.GetWorldLocation()

			# If this object is inside the starbase, store off the object's original
			# position so it can be restored when docking is complete
			if IsInViewOfInsidePoints(pObject, pStarbase):
				# It's inside the starbase.  Remember its position for later.
				kRestoreDict [pObject.GetObjID ()] = pObject.GetWorldLocation()

			# now find a new location to put the ship so it's out of the way
			vDiff.Subtract(pDockingEntry.GetWorldLocation())
			vDiff.Unitize()
			if vDiff.SqrLength < 0.5:
				vDiff.SetXYZ(1, 0, 0)

			# Find a distance that's clear of other hazards.
			fMoveDistance = 300.0
			while 1:
				vDiff.Scale(fMoveDistance / vDiff.Length())
				vNewLocation = pDockingEntry.GetWorldLocation()
				vNewLocation.Add(vDiff)
				if pSet.IsLocationEmptyTG(vNewLocation, pObject.GetRadius()):
					break
				fMoveDistance = fMoveDistance + 100.0

			pObject.SetTranslate(vNewLocation)

		# Look at the next object..
		pObject = pProx.GetNextObject(pIter)
	pProx.EndObjectIteration(pIter)

	# Fix the ship's impulse engines and power supply, if they need fixing.
	pImpulse = pShip.GetImpulseEngineSubsystem()
	if pImpulse:
		Actions.ShipScriptActions.RepairSubsystemFully(None, pImpulse.GetObjID())

		# And set them to full power.
		pImpulse.TurnOn()
		pImpulse.SetPowerPercentageWanted(1.0)

	# Fix the power system...
	pPower = pShip.GetPowerSubsystem()
	if pPower:
		Actions.ShipScriptActions.RepairSubsystemFully(None, pPower.GetObjID())

		# Set the power of the ship to max.
		pPower.SetMainBatteryPower(pPower.GetMainBatteryLimit())
		pPower.SetBackupBatteryPower(pPower.GetBackupBatteryLimit())

def StopShip(pShip):
	# Hard stop, so the ship doesn't drift while being repaired.
	debug(__name__ + ", StopShip")
	vZero = App.TGPoint3()
	vZero.SetXYZ(0, 0, 0)
	pShip.SetVelocity(vZero)
	pShip.SetSpeed(0, App.TGPoint3_GetModelForward(), App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

def CreatePlayerDockAction(pShip, pStarbase, pGraffAction, bNoRepair, bFade):
	# The player is docking.  Make sure Graff's set exists.
        debug(__name__ + ", CreatePlayerDockAction")
        try:
	        import Systems.Starbase12.Starbase12_S
	        Systems.Starbase12.Starbase12_S.SetupGraffSet()
        except:
                pass

	# Return the sequence to hail the starbase.
	return App.TGScriptAction_Create(__name__, "DockStarbase", pShip, pStarbase, pGraffAction, bNoRepair, bFade)

def NonPlayerDocked(pShip, sStarbase):
	# Circle the camera around the starbase, hinting at the passage of time.
	# Need to get a bunch of waypoints from the starbase model, to do this.
	debug(__name__ + ", NonPlayerDocked")
	pSet = pShip.GetContainingSet()
	if not pSet:
		return

	pStarbase = App.ShipClass_GetObject(pSet, sStarbase)
	#if pStarbase:
	#	pFirstWaypoint = SetupCameraSweepWaypoints(pStarbase, "DockedCameraSweep")

		# All the waypoints for the camera sweep have been created and hooked together.
		# Have the camera sweep along them.
	#	if pFirstWaypoint:
        #		Camera.Placement(pFirstWaypoint.GetName(), pShip.GetName(), pSet.GetName())
        #
	# Repair and reload the ship.
        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(RepairShipFully(pShip.GetObjID(), pStarbase))
        pSequence.Play()
	Actions.ShipScriptActions.ReloadShip(None, pShip.GetObjID())

def SetupCameraSweepWaypoints(pStarbase, sHardpointRoot):
	debug(__name__ + ", SetupCameraSweepWaypoints")
	pSet = pStarbase.GetContainingSet()
	pFirstWaypoint = None
	pPreviousWaypoint = None
	iWaypoint = 1
	while 1:
		# Get hardpoint info from the model.
		sHardpointName = sHardpointRoot + str(iWaypoint)
		vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, sHardpointName)
		iWaypoint = iWaypoint + 1
		if None in (vPos, vFwd, vUp):
			break

		pWaypoint = App.Waypoint_Cast( App.PlacementObject_GetObject(pSet, sHardpointName) )
		if not pWaypoint:
			pWaypoint = App.Waypoint_Create(sHardpointName, pSet.GetName(), None)
			if pPreviousWaypoint:
				pPreviousWaypoint.InsertAfterObj(pWaypoint)

		# Position the waypoint based on the hardpoint info.
		PositionObjectFromLocalInfo(pWaypoint, pStarbase, vPos, vFwd, vUp)

		if not pFirstWaypoint:
			pFirstWaypoint = pWaypoint

#	if not pFirstWaypoint:
#		debug("Unable to find hardpoints %s## on model for %s" % (sHardpointRoot, pStarbase.GetName()))

	return pFirstWaypoint #

def PrepareUndock(pShip, sStarbase, bFade):
	debug(__name__ + ", PrepareUndock")
	pSet = pShip.GetContainingSet()
	if not pSet:
		return

	pStarbase = App.ShipClass_GetObject(pSet, sStarbase)
	if not pStarbase:
		return

        # only player for camera
        pPlayer = MissionLib.GetPlayer()
        if pPlayer.GetObjID() != pShip.GetObjID():
                return

	# Change to a cinematic camera, and watch the ship fly out.
	import DockWithStarbase
	pStartWaypoint = DockWithStarbase.SetupCameraSweepWaypoints(pStarbase, "UndockingCameraSweep")
	if pStartWaypoint:
		Camera.Placement(pStartWaypoint.GetName(), pShip.GetName(), pSet.GetName())

#	debug("Fade is %s" % bFade)
	#if bFade:
		# The screen has faded out...  Fade it back in.
	#	App.TGScriptAction_Create("MissionLib", "FadeIn").Play()


def ReEnableCollisionWithStarbase(pAction, pStarbase, pShip):
        debug(__name__ + ", ReEnableCollisionWithStarbase")
        pStarbase.EnableCollisionsWith(pShip, 1)
        if App.g_kUtopiaModule.IsMultiplayer():
                MultiPlayerEnableCollisionWith(pStarbase, pShip, 1)
        return 0


def FinishedUndocking(pShip, sStarbase, bBridge, bTactical):
        debug(__name__ + ", FinishedUndocking")
        pPlayer = MissionLib.GetPlayer()
        if pPlayer.GetObjID() != pShip.GetObjID():
                return

	# Restore all ships that were moved out of the way to their original position.
	global g_kRestoreTranslateDict
	if (g_kRestoreTranslateDict.has_key (pShip.GetObjID ())):
		kRestoreDict = g_kRestoreTranslateDict [pShip.GetObjID ()]
		if (kRestoreDict):
			for iObjID in kRestoreDict.keys ():
				# Get the world translate of this object
				vWorldPos = kRestoreDict [iObjID]
				# Get the object itself.
				pObject = App.ObjectClass_GetObjectByID (None, iObjID)
				if (pObject):
					pObject.SetTranslate (vWorldPos)

		# We're done.  Delete the restore dict to free up memory.
		del g_kRestoreTranslateDict [pShip.GetObjID ()]

	# Restore the object size, if it was modified.
	if g_dRestoreScaleDict.has_key(pShip.GetObjID()):
		pShip.SetScale( g_dRestoreScaleDict[pShip.GetObjID()] )
		del g_dRestoreScaleDict[pShip.GetObjID()]

	# Push the object forward a bit, so people stop complaining about camera clipping.
	vLocation = pShip.GetWorldForwardTG()
	vLocation.Scale(17.5)
	vLocation.Add( pShip.GetWorldLocation() )
	pShip.SetTranslate( vLocation )
	pShip.UpdateNodeOnly()

	# Exit out of cinematic mode.
	MissionLib.EndCutscene(None)

	# Reenable collisions with the starbase.
	pSet = pShip.GetContainingSet()
	if pSet:
		pStarbase = App.ShipClass_GetObject(pSet, sStarbase)
		if pStarbase:
                        pSeq = App.TGSequence_Create()
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ReEnableCollisionWithStarbase", pStarbase, pShip), 5)
                        pSeq.Play()

	# Make the rendered set either the bridge or the player's set, depending
	# on whether the bridge or tactical is up.
	pTop = App.TopWindow_GetTopWindow()
	if bBridge:
		pTop.ForceBridgeVisible()
	elif bTactical:
		pTop.ForceTacticalVisible()

		import Tactical.Interface.TacticalControlWindow
		Tactical.Interface.TacticalControlWindow.Refresh()

	pSet = pShip.GetContainingSet()
	if pSet:
		Actions.CameraScriptActions.CutsceneCameraEnd(None, pSet.GetName(), "DockingCam")

	# If this ship is the player, set our flag that says the player
	# has docked at least once.
	if pShip.IsPlayerShip():
		global g_bPlayerDockedOnce
		g_bPlayerDockedOnce = 1

		# And set the ship to coast out at impulse 2, replacing this AI.
		# Note that, with the AvoidObstacles in this AI, there's a good
		# chance the ship will take off a lot faster than impulse 2 at
		# the start, as it tries to get away from the starbase...
		import AI.Player.FlyForward
		MissionLib.SetPlayerAI("Helm", AI.Player.FlyForward.CreateWithAvoid(pShip, 2.0 / 9.0))
                
                if not App.g_kSetManager.GetSet("bridge"):
                        MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ForceTacticalVisible", App.g_kUtopiaModule.GetGameTime() + 5, 0, 0)
                        MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".ForceTacticalVisible", App.g_kUtopiaModule.GetGameTime() + 7, 0, 0)


def ForceTacticalVisible(pObject, pEvent):
        debug(__name__ + ", ForceTacticalVisible")
        pTopWindow = App.TopWindow_GetTopWindow()
        pTopWindow.ToggleCinematicWindow()


def MakeWaypoints(pStarbase):
	# Waypoints will be named "Docking Entry" and "Docking Entry End".
	# Get these waypoints if they exist, or create them if they don't.
	debug(__name__ + ", MakeWaypoints")
	pWaypointStart = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), "Docking Entry") )
	if not pWaypointStart:
		pWaypointStart = App.Waypoint_Create("Docking Entry", pStarbase.GetContainingSet().GetName(), None)
		pWaypointStart.SetSpeed(5.0)

	pWaypointEnd = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), "Docking Entry End") )
	if not pWaypointEnd:
		pWaypointEnd = App.Waypoint_Create("Docking Entry End", pStarbase.GetContainingSet().GetName(), None)
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
		PositionObjectFromLocalInfo(pWaypoint, pStarbase, vPos, vFwd, vUp)

def PositionObjectFromLocalInfo(pObject, pLocalInfoObject, vPos, vFwd, vUp):
	debug(__name__ + ", PositionObjectFromLocalInfo")
	vWorldPos = pLocalInfoObject.GetWorldLocation()
	mWorldRot = pLocalInfoObject.GetWorldRotation()

	vPos.MultMatrixLeft( mWorldRot )
	vPos.Add(vWorldPos)
	vFwd.MultMatrixLeft( mWorldRot )
	vUp.MultMatrixLeft( mWorldRot )

	# Move the waypoint to this position/orientation.
	pObject.SetTranslate(vPos)
	pObject.AlignToVectors(vFwd, vUp)
	pObject.UpdateNodeOnly()

def ShowInsidePoints(sStarbase = "Starbase 12"):
	debug(__name__ + ", ShowInsidePoints")
	pStarbase = App.ShipClass_GetObject(None, sStarbase)
	if not pStarbase:
		return

	iPoint = 0
	while 1:
		iPoint = iPoint + 1
		sName = "Inside Visibility " + str(iPoint)
		vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, sName)
		if not vPos:
			break

		# Get these waypoints if they exist, or create them if they don't.
		pPlacement = App.Waypoint_Cast( App.PlacementObject_GetObject(pStarbase.GetContainingSet(), sName) )
		if not pPlacement:
			pPlacement = App.Waypoint_Create(sName, pStarbase.GetContainingSet().GetName(), None)
			pPlacement.SetSpeed(5.0)

		# Position the waypoint based on info in the model.
		PositionObjectFromLocalInfo(pPlacement, pStarbase, vPos, vFwd, vUp)

def IsInViewOfInsidePoints(pShip, pStarbase):
	# False, unless set True below.
	debug(__name__ + ", IsInViewOfInsidePoints")
	bInView = 0

	# Get visibility points from the starbase model.
	iPoint = 0
	while 1:
		iPoint = iPoint + 1
		vPos, vFwd, vUp = MissionLib.GetPositionOrientationFromProperty(pStarbase, "Inside Visibility " + str(iPoint))
		if vPos is None:
			break

		# Move the position into worldspace, for the comparison.
		vPos.MultMatrixLeft( pStarbase.GetWorldRotation() )
		vPos.Add( pStarbase.GetWorldLocation() )

		# Got an inside visibility point.  Test if the ship can see that point.
		if not pStarbase.LineCollides( vPos, pShip.GetWorldLocation() ):
			# This point is visible to the ship.  The condition is True.
			bInView = 1
			break

	return bInView

def CreateAI(pShip, pStarbase, pGraffAction = None, **dFlags):
	# Find the docking point on the starbase, in the
	# model space of the starbase.
	debug(__name__ + ", CreateAI")
	global vBayCenter, vBayDirection, vBayUp
	vBayCenter = None
	vBayDirection = None
	vBayUp = None

	# Check if this ship is the player's ship.
	pPlayer = App.Game_GetCurrentPlayer()
	bFadeEnd = 1
	if pPlayer  and  (pShip.GetObjID() == pPlayer.GetObjID()):
		dFlags["IsPlayer"] = 1
		# If it's the player, we might fade at the end of Graff's sequence.
		if dFlags.has_key("FadeEnd"):
			bFadeEnd = dFlags["FadeEnd"]
	else:
		dFlags["IsPlayer"] = 0

	# Test whether the ship is in view of the Inside Visibility points in the starbase.
	dFlags["InViewOfInsidePoints"] = IsInViewOfInsidePoints(pShip, pStarbase)

	if dFlags.has_key("NoRepair"):
		bNoRepair = dFlags["NoRepair"]
	else:
		bNoRepair = 0

	# Make waypoints for the docking entry positions..
	MakeWaypoints(pStarbase)

	if pStarbase:
                pStarbase.EnableCollisionsWith(pShip, 0)
                if App.g_kUtopiaModule.IsMultiplayer():
                        MultiPlayerEnableCollisionWith(pStarbase, pShip, 0)
                
		pSet = pStarbase.GetContainingSet()
		if pSet:
			pBayWaypoint = App.Waypoint_Cast( App.PlacementObject_GetObject(pSet, "Docking Entry") )
			if pBayWaypoint:
				mInv = pStarbase.GetWorldRotation()

				# Determine the center of the docking
				# bay, in the starbase's model space.
				vBayCenter = pBayWaypoint.GetWorldLocation()
				vBayCenter.Subtract(pStarbase.GetWorldLocation())
				vBayCenter.MultMatrixLeft(mInv)
				vBayCenter.Scale( 1.0 / pStarbase.GetScale() )

				# Determine orientation.
				vBayDirection = pBayWaypoint.GetWorldForwardTG()
				vBayDirection.Scale(-1.0)
				vBayDirection.MultMatrixLeft(mInv)

				vBayUp = pBayWaypoint.GetWorldUpTG()
				vBayUp.MultMatrixLeft(mInv)

	if not (vBayCenter and vBayDirection and vBayUp):
		# Starbase doesn't have a docking point.  We can't
		# dock with it.
#		debug("Tried to dock with a starbase with no docking point: " + str(pStarbase.GetName()))
		return None

	# Check if the Bridge or Tactical is visible...
	pTop = App.TopWindow_GetTopWindow()
	bBridgeVisible = pTop.IsBridgeVisible()
	bTacticalVisible = pTop.IsTacticalVisible()




	#########################################
	# Creating PlainAI EnterStarbase at (99, 75)
	pEnterStarbase = App.PlainAI_Create(pShip, "EnterStarbase")
	pEnterStarbase.SetScriptModule("FollowWaypoints")
	pEnterStarbase.SetInterruptable(1)
	pScript = pEnterStarbase.GetScriptInstance()
	pScript.SetTargetWaypointName("Docking Entry")
	# Done creating PlainAI EnterStarbase
	#########################################
	#########################################
	# Creating PlainAI StopShip at (153, 38)
	pStopShip = App.PlainAI_Create(pShip, "StopShip")
	pStopShip.SetScriptModule("RunScript")
	pStopShip.SetInterruptable(1)
	pScript = pStopShip.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("StopShip")
	pScript.SetArguments(pShip)
	# Done creating PlainAI StopShip
	#########################################
	#########################################
	# Creating SequenceAI FlyInSequence at (31, 148)
	pFlyInSequence = App.SequenceAI_Create(pShip, "FlyInSequence")
	pFlyInSequence.SetInterruptable(1)
	pFlyInSequence.SetLoopCount(1)
	pFlyInSequence.SetResetIfInterrupted(1)
	pFlyInSequence.SetDoubleCheckAllDone(0)
	pFlyInSequence.SetSkipDormant(0)
	# SeqBlock is at (143, 155)
	pFlyInSequence.AddAI(pEnterStarbase)
	pFlyInSequence.AddAI(pStopShip)
	# Done creating SequenceAI FlyInSequence
	#########################################
	#########################################
	# Creating ConditionalAI NotInViewOfInsidePoints at (39, 198)
	## Conditions:
	#### Condition InView
	pInView = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "InViewOfInsidePoints", dFlags)
	## Evaluation function:
	def EvalFunc(bInView):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bInView:
			return DONE
		return ACTIVE
	## The ConditionalAI:
	pNotInViewOfInsidePoints = App.ConditionalAI_Create(pShip, "NotInViewOfInsidePoints")
	pNotInViewOfInsidePoints.SetInterruptable(1)
	pNotInViewOfInsidePoints.SetContainedAI(pFlyInSequence)
	pNotInViewOfInsidePoints.AddCondition(pInView)
	pNotInViewOfInsidePoints.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI NotInViewOfInsidePoints
	#########################################
	#########################################
	# Creating PlainAI PlayerDocked at (252, 43)
	pPlayerDocked = App.PlainAI_Create(pShip, "PlayerDocked")
	pPlayerDocked.SetScriptModule("RunAction")
	pPlayerDocked.SetInterruptable(1)
	pScript = pPlayerDocked.GetScriptInstance()
	pScript.SetAction(CreatePlayerDockAction(pShip, pStarbase, pGraffAction, bNoRepair, bFadeEnd))
	# Done creating PlainAI PlayerDocked
	#########################################
	#########################################
	# Creating ConditionalAI IsPlayerShip at (237, 118)
	## Conditions:
	#### Condition IsPlayer
	pIsPlayer = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "IsPlayer", dFlags)
	## Evaluation function:
	def EvalFunc(bIsPlayer):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIsPlayer:
			return ACTIVE
		return DONE
	## The ConditionalAI:
	pIsPlayerShip = App.ConditionalAI_Create(pShip, "IsPlayerShip")
	pIsPlayerShip.SetInterruptable(1)
	pIsPlayerShip.SetContainedAI(pPlayerDocked)
	pIsPlayerShip.AddCondition(pIsPlayer)
	pIsPlayerShip.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI IsPlayerShip
	#########################################
	#########################################
	# Creating PlainAI NonPlayerDocked at (438, 55)
	pNonPlayerDocked = App.PlainAI_Create(pShip, "NonPlayerDocked")
	pNonPlayerDocked.SetScriptModule("RunScript")
	pNonPlayerDocked.SetInterruptable(1)
	pScript = pNonPlayerDocked.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("NonPlayerDocked")
	pScript.SetArguments(pShip, pStarbase.GetName())
	# Done creating PlainAI NonPlayerDocked
	#########################################
	#########################################
	# Creating ConditionalAI NotPlayerShip at (397, 115)
	## Conditions:
	#### Condition IsPlayer
	pIsPlayer = App.ConditionScript_Create("Conditions.ConditionFlagSet", "ConditionFlagSet", "IsPlayer", dFlags)
	## Evaluation function:
	def EvalFunc(bIsPlayer):
		debug(__name__ + ", EvalFunc")
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bIsPlayer:
			return DONE
		return ACTIVE
	## The ConditionalAI:
	pNotPlayerShip = App.ConditionalAI_Create(pShip, "NotPlayerShip")
	pNotPlayerShip.SetInterruptable(1)
	pNotPlayerShip.SetContainedAI(pNonPlayerDocked)
	pNotPlayerShip.AddCondition(pIsPlayer)
	pNotPlayerShip.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI NotPlayerShip
	#########################################
	#########################################
	# Creating PriorityListAI PriorityList at (249, 188)
	pPriorityList = App.PriorityListAI_Create(pShip, "PriorityList")
	pPriorityList.SetInterruptable(1)
	# SeqBlock is at (342, 148)
	pPriorityList.AddAI(pIsPlayerShip, 1)
	pPriorityList.AddAI(pNotPlayerShip, 2)
	# Done creating PriorityListAI PriorityList
	#########################################
	#########################################
	# Creating PlainAI PrepareUndock at (306, 252)
	pPrepareUndock = App.PlainAI_Create(pShip, "PrepareUndock")
	pPrepareUndock.SetScriptModule("RunScript")
	pPrepareUndock.SetInterruptable(1)
	pScript = pPrepareUndock.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("PrepareUndock")
	pScript.SetArguments(pShip, pStarbase.GetName(), bFadeEnd)
	# Done creating PlainAI PrepareUndock
	#########################################
	#########################################
	# Creating CompoundAI Undock at (308, 303)
	import AI.Compound.UndockFromStarbase
	pUndock = AI.Compound.UndockFromStarbase.CreateAI(pShip, pStarbase)
	# Done creating CompoundAI Undock
	#########################################
	#########################################
	# Creating PlainAI FinishedUndocking at (325, 353)
	pFinishedUndocking = App.PlainAI_Create(pShip, "FinishedUndocking")
	pFinishedUndocking.SetScriptModule("RunScript")
	pFinishedUndocking.SetInterruptable(1)
	pScript = pFinishedUndocking.GetScriptInstance()
	pScript.SetScriptModule(__name__)
	pScript.SetFunction("FinishedUndocking")
	pScript.SetArguments(pShip, pStarbase.GetName(), bBridgeVisible, bTacticalVisible)
	# Done creating PlainAI FinishedUndocking
	#########################################
	#########################################
	# Creating SequenceAI DockingSequence at (23, 350)
	pDockingSequence = App.SequenceAI_Create(pShip, "DockingSequence")
	pDockingSequence.SetInterruptable(0)
	pDockingSequence.SetLoopCount(1)
	pDockingSequence.SetResetIfInterrupted(1)
	pDockingSequence.SetDoubleCheckAllDone(0)
	pDockingSequence.SetSkipDormant(0)
	# SeqBlock is at (220, 360)
	pDockingSequence.AddAI(pNotInViewOfInsidePoints)
	pDockingSequence.AddAI(pPriorityList)
	pDockingSequence.AddAI(pPrepareUndock)
	pDockingSequence.AddAI(pUndock)
	pDockingSequence.AddAI(pFinishedUndocking)
	# Done creating SequenceAI DockingSequence
	#########################################
	return pDockingSequence
