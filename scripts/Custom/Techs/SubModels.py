from bcdebug import debug
import App
import FoundationTech
import loadspacehelper
import math
import MissionLib

# code is broken and needs rewrite, sorry, but we did a 90° turn while programming -Defiant
# the scheme is that:
# 1. add normal model
# 2. replace model with body + wings
# 3. move the wings
# 4. replace body + parts with attack model

"""

Sample Setup:

Foundation.ShipDef.VasKholhr.dTechs = { 'SubModel': {
        "Setup":        {
                "Body":                 "VasKholhr_Body",
                "NormalModel":          shipFile,
                "WarpModel":          "VasKholhr_WingUp",
                "AttackModel":          "VasKholhr_WingDown",
                "Hardpoints":       {
                        "Port Cannon":  [-0.677745, 0.514529, -0.229285],
                        "Star Cannon":  [0.663027, 0.511252, -0.240265],
                        "Port Cannon 1":  [-0.323324, 0.240263, -0.115398],
                        "Star Cannon 1":  [0.319566, 0.242142, -0.11861],
                },
                "AttackHardpoints":       {
                        "Port Cannon":  [-0.503543, 0.524792, -0.47761],
                        "Star Cannon":  [0.486256, 0.527008, -0.483889],
                        "Port Cannon 1":  [-0.244469, 0.228191, -0.19762],
                        "Star Cannon 1":  [0.243789, 0.243208, -0.201933],
                },
        },
                
        "Port Wing":     ["VasKholhr_Portwing", {
                "Position":             [0, 0, 0],
                "Rotation":             [0, 0, 0], # normal Rotation used if not Red Alert and if not Warp
                "AttackRotation":         [0, -0.6, 0],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.03],
                "WarpRotation":       [0, 0.349, 0],
                "WarpPosition":       [0, 0, 0.02],
                "WarpDuration":       150.0,
                }
        ],
        
        "Starboard Wing":     ["VasKholhr_Starboardwing", {
                "Position":             [0, 0, 0],
                "Rotation":             [0, 0, 0],
                "AttackRotation":         [0, 0.6, 0],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.03],
                "WarpRotation":       [0, -0.349, 0],
                "WarpPosition":       [0, 0, 0.02],
                "WarpDuration":       150.0,
                }
        ],
}}



"""

REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

# This class does control the attach and detach of the Models
class SubModels(FoundationTech.TechDef):
	
	# called by FoundationTech when a ship is created
	# Prepares the ship for moving its sub parts
        def AttachShip(self, pShip, pInstance):
                debug(__name__ + ", AttachShip")
                print "Ship %s with SubModels support added" % pShip.GetName()

                sNamePrefix = pShip.GetName() + "_"
                pInstance.__dict__["OptionsList"] = [] # save options to this list, so we can access them later
                self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once
                self.bAddedAlertListener = {}
                ModelList = pInstance.__dict__["SubModel"]
		AlertListener = 0
                
                if not ModelList.has_key("Setup"):
                        print "Error: Cannot find Setup for Moving Parts"
                        return
                
		# Interate over every item
                for sNameSuffix in ModelList.keys():
			# if this is the setup, do the thinks for the whole ship 
			#we have to remember, like alert state
                        if sNameSuffix == "Setup":
                                dOptions = ModelList[sNameSuffix]
                                # we start with green alert
                                if not dOptions.has_key("AlertLevel"):
                                        dOptions["AlertLevel"] = {}
                                if not dOptions.has_key("GenMoveID"):
                                        dOptions["GenMoveID"] = {}
                                dOptions["AlertLevel"][pShip.GetName()] = 0
                                dOptions["GenMoveID"][pShip.GetName()] = 0
                                pInstance.OptionsList.append("Setup", dOptions)
                                continue # nothing more todo here
                        #
                        # the following stuff is only for the objects that moves
                        
                        if len(ModelList[sNameSuffix]) > 1:
                                dOptions = ModelList[sNameSuffix][1]
                        sFile = ModelList[sNameSuffix][0]
                        loadspacehelper.PreloadShip(sFile, 1)
                        
			# save the shipfile for later use
                        dOptions["sShipFile"] = sFile
                        
                        # set current rotation/position values
                        if not dOptions.has_key("currentRotation"):
                                dOptions["currentRotation"] = {}
                        if not dOptions.has_key("currentPosition"):
                                dOptions["currentPosition"] = {}
                        if not dOptions.has_key("curMovID"):
                                dOptions["curMovID"] = {}
                        dOptions["currentRotation"][pShip.GetName()] = [0, 0, 0] # those two lists are updated with every move
                        dOptions["currentPosition"][pShip.GetName()] = [0, 0, 0]
                        dOptions["curMovID"][pShip.GetName()] = 0
                        if not dOptions.has_key("Position"):
                                dOptions["Position"] = [0, 0, 0]
                        dOptions["currentPosition"][pShip.GetName()] = dOptions["Position"] # set current Position
                        
                        if not dOptions.has_key("Rotation"):
                                dOptions["Rotation"] = [0, 0, 0]
                        dOptions["currentRotation"][pShip.GetName()] = dOptions["Rotation"] # set current Rotation
                        
                        # event listener
                        if not self.bAddedWarpListener.has_key(pShip.GetName()) and (dOptions.has_key("WarpRotation") or dOptions.has_key("WarpPosition")):
                                pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
				pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                                # ET_EXITED_WARP handler doesn't seem to work, so use ET_EXITED_SET instead
                                pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                                self.bAddedWarpListener[pShip.GetName()] = 1
                        if not self.bAddedAlertListener.has_key(pShip.GetName()) and (dOptions.has_key("AttackRotation") or dOptions.has_key("AttackPosition")):
				pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertStateChanged")
                                # Alert change handler doesn't work for AI ships, so use subsystem changed instead
                                pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
                                self.bAddedAlertListener[pShip.GetName()] = 1
				AlertListener = 1
                
                # Make sure the Ship is correctly set
                # because we don't get the first ET_SUBSYSTEM_STATE_CHANGED event for Ai ships
		if AlertListener:
                	PartsForWeaponState(pShip)

	# Called by FoundationTech when a Ship is removed from set (eg destruction)
        def DetachShip(self, iShipID, pInstance):
		# get our Ship
                debug(__name__ + ", DetachShip")
                pShip = App.ShipClass_GetObjectByID(None, iShipID)
                if pShip:
			# remove the listeners
                        if self.bAddedWarpListener.has_key(pShip.GetName()):
                                pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
				pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                                pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                                del self.bAddedWarpListener[pShip.GetName()]
                        if self.bAddedAlertListener.has_key(pShip.GetName()):
                                pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
				pShip.RemoveHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertStateChanged")
                                del self.bAddedAlertListener[pShip.GetName()]
			
                        if hasattr(pInstance, "OptionsList"):
                                for item in pInstance.OptionsList:
                                        if item[0] == "Setup":
                                                del item[1]["AlertLevel"][pShip.GetName()]
                                        else:
                                                del item[1]["currentRotation"][pShip.GetName()]
                                                del item[1]["currentPosition"][pShip.GetName()]
                                
                if hasattr(pInstance, "SubModelList"):
                        del pInstance.SubModelList

	# Attaches the SubParts to the Body Model
        def AttachParts(self, pShip, pInstance):
                debug(__name__ + ", AttachParts")
                pSet = pShip.GetContainingSet()
                pInstance.__dict__["SubModelList"] = []
                ModelList = pInstance.__dict__["SubModel"]
                sNamePrefix = pShip.GetName() + "_"
                SubModelList = pInstance.SubModelList

		# iteeeerate over every SubModel
                for sNameSuffix in ModelList.keys():
                        if sNameSuffix == "Setup":
                                continue

                        sFile = ModelList[sNameSuffix][0]
                        sShipName = sNamePrefix + sNameSuffix
                        
                        # check if the ship does exist first, before create it
                        pSubShip = MissionLib.GetShip(sShipName)
                        if not pSubShip:
                                pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "")
                        SubModelList.append(pSubShip)
                        if len(ModelList[sNameSuffix]) > 1:
                                dOptions = ModelList[sNameSuffix][1]

                        # set current positions
                        pSubShip.SetTranslateXYZ(dOptions["currentPosition"][pShip.GetName()][0],dOptions["currentPosition"][pShip.GetName()][1],dOptions["currentPosition"][pShip.GetName()][2])
                        iNorm = math.sqrt(dOptions["currentRotation"][pShip.GetName()][0] ** 2 + dOptions["currentRotation"][pShip.GetName()][1] ** 2 + dOptions["currentRotation"][pShip.GetName()][2] ** 2)
                        pSubShip.SetAngleAxisRotation(1.0,dOptions["currentRotation"][pShip.GetName()][0],dOptions["currentRotation"][pShip.GetName()][1],dOptions["currentRotation"][pShip.GetName()][2])
			pSubShip.SetScale(-iNorm + 1.85)
			pSubShip.UpdateNodeOnly()

                        # save the options list
                        iSaveDone = 0
                        # this is here to check if we already have the entry
                        for lList in pInstance.OptionsList:
                                if lList[0] != "Setup":
                                        if lList[1]["sShipFile"] == sFile:
                                                lList[0] = pSubShip
                                                iSaveDone = 1
                                                break
                        
                        if not iSaveDone:
                                pInstance.OptionsList.append([pSubShip, dOptions])
			
                        pSubShip.SetUsePhysics(0)
                        pSubShip.SetTargetable(0)
			mp_send_settargetable(pSubShip.GetObjID(), 0)
                        pSubShip.SetInvincible(1)
                        pSubShip.SetHurtable(0)
                        #pSubShip.GetShipProperty().SetMass(1.0e+25)
                        #pSubShip.GetShipProperty().SetRotationalInertia(1.0e+25)
                        #pSubShip.GetShipProperty().SetStationary(1)
                        pSubShip.SetHailable(0)
                        if pSubShip.GetShields():
                                pSubShip.GetShields().TurnOff()
            
                        pShip.EnableCollisionsWith(pSubShip, 0)
                        pSubShip.EnableCollisionsWith(pShip, 0)
			MultiPlayerEnableCollisionWith(pShip, pSubShip, 0)
                        for pSubShip2 in SubModelList:
				if pSubShip.GetObjID() != pSubShip2.GetObjID():
                                	pSubShip.EnableCollisionsWith(pSubShip2, 0)
                                	pSubShip2.EnableCollisionsWith(pSubShip, 0)
					MultiPlayerEnableCollisionWith(pSubShip, pSubShip2, 0)
                        
                        pShip.AttachObject(pSubShip)

	# check if parts are attached
        def ArePartsAttached(self, pShip, pInstance):
                debug(__name__ + ", ArePartsAttached")
                if hasattr(pInstance, "SubModelList"):
                        return 1
                return 0

	# Detaches the parts
        def DetachParts(self, pShip, pInstance):
                debug(__name__ + ", DetachParts")
                if hasattr(pInstance, "SubModelList"):
                        for pSubShip in pInstance.SubModelList:
                                pSet = pSubShip.GetContainingSet()
                                pShip.DetachObject(pSubShip)
				DeleteObjectFromSet(pSet, pSubShip.GetName())
                        del pInstance.SubModelList
                
oSubModels = SubModels("SubModel")


# The class does the moving of the parts
# with every move the part continues to move
class MovingEvent:
	# prepare fore move...
        def __init__(self, pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints):
                debug(__name__ + ", __init__")
		
                self.iNacelleID = item[0].GetObjID()
                self.iThisMovID = item[1]["curMovID"][pShip.GetName()]
                self.dOptionsList = item[1]
                self.pShip = pShip
			
		fDurationMul = 0.95 # make us a little bit faster to avoid bad timing
	
                # rotation values
                self.iCurRotX = lStartingRotation[0]
                self.iCurRotY = lStartingRotation[1]
                self.iCurRotZ = lStartingRotation[2]
		if fDuration > 0:
			self.iRotStepX = (lStoppingRotation[0] - lStartingRotation[0]) / (fDuration * fDurationMul)
			self.iRotStepY = (lStoppingRotation[1] - lStartingRotation[1]) / (fDuration * fDurationMul)
			self.iRotStepZ = (lStoppingRotation[2] - lStartingRotation[2]) / (fDuration * fDurationMul)
		else:
			self.iRotStepX = (lStoppingRotation[0] - lStartingRotation[0])
			self.iRotStepY = (lStoppingRotation[1] - lStartingRotation[1])
			self.iRotStepZ = (lStoppingRotation[2] - lStartingRotation[2])
                
                # translation values
                self.iCurTransX = lStartingTranslation[0]
                self.iCurTransY = lStartingTranslation[1]
                self.iCurTransZ = lStartingTranslation[2]
		if fDuration > 0:
			self.iTransStepX = (lStoppingTranslation[0] - lStartingTranslation[0]) / (fDuration * fDurationMul)
			self.iTransStepY = (lStoppingTranslation[1] - lStartingTranslation[1]) / (fDuration * fDurationMul)
			self.iTransStepZ = (lStoppingTranslation[2] - lStartingTranslation[2]) / (fDuration * fDurationMul)
		else:
			self.iTransStepX = (lStoppingTranslation[0] - lStartingTranslation[0])
			self.iTransStepY = (lStoppingTranslation[1] - lStartingTranslation[1])
			self.iTransStepZ = (lStoppingTranslation[2] - lStartingTranslation[2])
		
		self.dStopHardpoints = dHardpoints
		self.dStartHardpoints = {}
		self.dCurHPs = {}
		for sHP in self.dStopHardpoints.keys():
			lPos = None
			pHP = MissionLib.GetSubsystemByName(pShip, sHP)
			pPOP = GetPositionOrientationPropertyByName(pShip, sHP)
			if pHP:
				NiPoint3 = pHP.GetPosition()
				lPos = [NiPoint3.x, NiPoint3.y, NiPoint3.z]
			elif pPOP:
				TGPoint3 = pPOP.GetPosition()
				lPos = [TGPoint3.x, TGPoint3.y, TGPoint3.z]
			else:
				print "Submodel Error: Unable to find Hardpoint %s" % sHP
			if lPos:
				self.dStartHardpoints[sHP] = lPos
				self.dCurHPs[sHP] = lPos

		self.dHPSteps = {}
		for sHP in self.dStartHardpoints.keys():
			self.dHPSteps[sHP] = [0, 0, 0]
			
			if fDuration > 0:
				self.dHPSteps[sHP][0] = (self.dStopHardpoints[sHP][0] - self.dStartHardpoints[sHP][0]) / (fDuration * fDurationMul)
				self.dHPSteps[sHP][1] = (self.dStopHardpoints[sHP][1] - self.dStartHardpoints[sHP][1]) / (fDuration * fDurationMul)
				self.dHPSteps[sHP][2] = (self.dStopHardpoints[sHP][2] - self.dStartHardpoints[sHP][2]) / (fDuration * fDurationMul)
			else:
				self.dHPSteps[sHP][0] = (self.dStopHardpoints[sHP][0] - self.dStartHardpoints[sHP][0])
				self.dHPSteps[sHP][1] = (self.dStopHardpoints[sHP][1] - self.dStartHardpoints[sHP][1])
				self.dHPSteps[sHP][2] = (self.dStopHardpoints[sHP][2] - self.dStartHardpoints[sHP][2])
		
	# move!
        def __call__(self):
		# if the move ID doesn't match then this move is outdated
                debug(__name__ + ", __call__")
                if self.iThisMovID != self.dOptionsList["curMovID"][self.pShip.GetName()]:
                        print "Moving Error: Move no longer active"
                        return 1
                
                # this makes sure the game does not crash when trying to access a deleted element
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        #print "Moving Error: Lost part"
                        return 0
                        
                # set new Rotation values
                self.iCurRotX = self.iCurRotX + self.iRotStepX
                self.iCurRotY = self.iCurRotY + self.iRotStepY
                self.iCurRotZ = self.iCurRotZ + self.iRotStepZ
                iNorm = math.sqrt(self.iCurRotX ** 2 + self.iCurRotY ** 2 + self.iCurRotZ ** 2)
                # set Rotation
                pNacelle.SetAngleAxisRotation(1.0, self.iCurRotX, self.iCurRotY, self.iCurRotZ)
		pNacelle.SetScale(-iNorm + 1.85)

                # set new Translation values
                self.iCurTransX = self.iCurTransX + self.iTransStepX
                self.iCurTransY = self.iCurTransY + self.iTransStepY
                self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
                # set Translation
                pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)
                
                self.dOptionsList["currentRotation"][self.pShip.GetName()] = [self.iCurRotX, self.iCurRotY, self.iCurRotZ]
                self.dOptionsList["currentPosition"][self.pShip.GetName()] = [self.iCurTransX, self.iCurTransY, self.iCurTransZ]
                
		# Hardpoints
		for sHP in self.dCurHPs.keys():
			self.dCurHPs[sHP][0] = self.dCurHPs[sHP][0] + self.dHPSteps[sHP][0]
			self.dCurHPs[sHP][1] = self.dCurHPs[sHP][1] + self.dHPSteps[sHP][1]
			self.dCurHPs[sHP][2] = self.dCurHPs[sHP][2] + self.dHPSteps[sHP][2]
			UpdateHardpointPositionsTo(self.pShip, sHP, self.dCurHPs[sHP])
		
		pNacelle.UpdateNodeOnly()
                return 0


# calls the MovingEvent class and returns its return value
def MovingAction(pAction, oMovingEvent):
        debug(__name__ + ", MovingAction")
        return oMovingEvent()


def AlertStateChanged(pObject, pEvent):
	debug(__name__ + ", AlertStateChanged")
	pObject.CallNextHandler(pEvent)
	pShip = App.ShipClass_Cast(pObject)
	
	pSeq = App.TGSequence_Create()
	pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AlertStateChangedAction", pShip), 0.1)
	pSeq.Play()


def AlertStateChangedAction(pAction, pShip):
	debug(__name__ + ", AlertStateChangedAction")
	PartsForWeaponState(pShip)
	return 0


# called when a ship changes Power of one of its subsystems
# cause this is possible also an alert event
def SubsystemStateChanged(pObject, pEvent):
        debug(__name__ + ", SubsystemStateChanged")
        pShip = App.ShipClass_Cast(pObject)
        pSubsystem = pEvent.GetSource()

	# if the subsystem that changes its power is a weapon
        if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM):
		# set wings for this alert state
                PartsForWeaponState(pShip)
		
        pObject.CallNextHandler(pEvent)
        

# called when a ship exits a Set. Replacement for WARP_END Handler.
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


# Replaces the Model of pShip
def ReplaceModel(pShip, sNewShipScript):
        debug(__name__ + ", ReplaceModel")
	
	pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
	if not pShip:
		return
	
        ShipScript = __import__('ships.' + sNewShipScript)
        ShipScript.LoadModel()
        kStats = ShipScript.GetShipStats()
        pShip.SetupModel(kStats['Name'])
	if App.g_kUtopiaModule.IsMultiplayer():
		MPSentReplaceModelMessage(pShip, sNewShipScript)


# Prepares a ship to move: Replaces the current Model with the move Model and attaches its sub Models
def PrepareShipForMove(pShip, pInstance):
        debug(__name__ + ", PrepareShipForMove")
        if not oSubModels.ArePartsAttached(pShip, pInstance):
                ReplaceModel(pShip, pInstance.__dict__["SubModel"]["Setup"]["Body"])
                oSubModels.AttachParts(pShip, pInstance)


def IncCurrentMoveID(pShip, pInstance):
        debug(__name__ + ", IncCurrentMoveID")
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        item[1]["GenMoveID"][pShip.GetName()] = item[1]["GenMoveID"][pShip.GetName()] + 1


def GetCurrentMoveID(pShip, pInstance):
        debug(__name__ + ", GetCurrentMoveID")
        iGenMoveID = 0
        
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        iGenMoveID = item[1]["GenMoveID"][pShip.GetName()]
        return iGenMoveID
                        

def MoveFinishMatchId(pShip, pInstance, iThisMovID):
        debug(__name__ + ", MoveFinishMatchId")
        if GetCurrentMoveID(pShip, pInstance) == iThisMovID:
                return 1
        return 0
        
        
# called after the Alert move action
# Remove the attached parts and use the attack or normal model now
def AlertMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", AlertMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
        
        oSubModels.DetachParts(pShip, pInstance)
        if pShip.GetAlertLevel() == 2:
                sNewShipScript = pInstance.__dict__["SubModel"]["Setup"]["AttackModel"]
        else:
                sNewShipScript = pInstance.__dict__["SubModel"]["Setup"]["NormalModel"]
        ReplaceModel(pShip, sNewShipScript)
        
        return 0


# called after the warp-start move action
# Remove the attached parts and use the warp model now
def WarpStartMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", WarpStartMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
                
        oSubModels.DetachParts(pShip, pInstance)
        sNewShipScript = pInstance.__dict__["SubModel"]["Setup"]["WarpModel"]
        ReplaceModel(pShip, sNewShipScript)
        return 0


# called after the warp-exit move action
# Remove the attached parts and use the attack or normal model now
def WarpExitMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", WarpExitMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
                
        oSubModels.DetachParts(pShip, pInstance)
        if pInstance.__dict__["SubModel"]["Setup"].has_key("AttackModel") and pShip.GetAlertLevel() == 2:
                sNewShipScript = pInstance.__dict__["SubModel"]["Setup"]["AttackModel"]
        else:
                sNewShipScript = pInstance.__dict__["SubModel"]["Setup"]["NormalModel"]
        ReplaceModel(pShip, sNewShipScript)
        return 0
        

# called after a move, sets the current Rotation/Translation values to the final ones
def UpdateState(pAction, pShip, item, lStoppingRotation, lStoppingTranslation):
        debug(__name__ + ", UpdateState")
        item[1]["currentRotation"][pShip.GetName()] = lStoppingRotation
        item[1]["currentPosition"][pShip.GetName()] = lStoppingTranslation
        item[1]["curMovID"][pShip.GetName()] = 0
        return 0
        
        
def GetPositionOrientationPropertyByName(pShip, pcSubsystemName):
	debug(__name__ + ", GetPositionOrientationPropertyByName")
	pPropSet = pShip.GetPropertySet()
	pInstanceList = pPropSet.GetPropertiesByType(App.CT_POSITION_ORIENTATION_PROPERTY)

	pInstanceList.TGBeginIteration()
	iNumItems = pInstanceList.TGGetNumItems()

	for i in range(iNumItems):
		pInstance = pInstanceList.TGGetNext()
		pProperty = App.PositionOrientationProperty_Cast(pInstance.GetProperty())
		
		if pProperty.GetName().GetCString() == pcSubsystemName:
			return pProperty

	pInstanceList.TGDoneIterating()
	pInstanceList.TGDestroy()
	
	return None


def UpdateHardpointPositionsTo(pShip, sHP, lPos):
        debug(__name__ + ", UpdateHardpointPositionsTo")

	pHP = MissionLib.GetSubsystemByName(pShip, sHP)
	pPOP = GetPositionOrientationPropertyByName(pShip, sHP)
	if pHP:
		pHPprob = pHP.GetProperty()
		pHPprob.SetPosition(lPos[0], lPos[1], lPos[2])
	elif pPOP:
		pPosition = App.TGPoint3()
		pPosition.SetXYZ(lPos[0], lPos[1], lPos[2])
		pPOP.SetPosition(pPosition)
	else:
		print "Submodel Error: Unable to find Hardpoint %s" % sHP
	pShip.UpdateNodeOnly()


def UpdateHardpointPositions(pAction, pShip, dHardpoints):
        debug(__name__ + ", UpdateHardpointPositions")

	for sHP in dHardpoints.keys():
		UpdateHardpointPositionsTo(pShip, sHP, dHardpoints[sHP])
	return 0


# Set the parts to the correct alert state
def PartsForWeaponState(pShip):	
        debug(__name__ + ", PartsForWeaponState")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		return
	
        pInstance = FoundationTech.dShips[pShip.GetName()]
        iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        dHardpoints = {}
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return
        
        # try to get the last alert level
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        dGenShipDict = item[1]
                        break
	
	# check if the alert state has really chanced since the last time
        if dGenShipDict["AlertLevel"][pShip.GetName()] == iType:
                return
	# update alert state
        dGenShipDict["AlertLevel"][pShip.GetName()] = iType
        IncCurrentMoveID(pShip, pInstance)
        
        # start with replacing the Models
        PrepareShipForMove(pShip, pInstance)
        
	# iterate over every submodel
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        # attack or cruise modus?
			dHardpoints = {}
                        if iType == 2 and item[1].has_key("AttackHardpoints"):
                                dHardpoints = item[1]["AttackHardpoints"]
                        elif iType != 2 and item[1].has_key("Hardpoints"):
                                dHardpoints = item[1]["Hardpoints"]
                        
                        # setup is not a submodel
                        continue
        
		# set the id for this move
                iThisMovID = item[1]["curMovID"][pShip.GetName()] + 1
                item[1]["curMovID"][pShip.GetName()] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("AttackDuration"):
                        fDuration = item[1]["AttackDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][pShip.GetName()]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("AttackRotation") and iType == 2:
                        lStoppingRotation = item[1]["AttackRotation"]
		else:
			lStoppingRotation = item[1]["Rotation"]
                
		
                # Translation
                lStartingTranslation = item[1]["currentPosition"][pShip.GetName()]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and iType == 2:
                        lStoppingTranslation = item[1]["AttackPosition"]
		else:
			lStoppingTranslation = item[1]["Position"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
                pSeq = App.TGSequence_Create()
                
		# do the move
                while(iTime < fDuration):
                        if iTime == 0.0:
                                iWait = 0.5 # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent), iWait)
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + 1
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
                pSeq.Play()
                
                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = iTimeNeededTotal
                
        # finally detach
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AlertMoveFinishAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance)), 2.0)
        pSeq.Play()


# Set the parts for Warp state
def StartingWarp(pObject, pEvent):
        debug(__name__ + ", StartingWarp")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		pObject.CallNextHandler(pEvent)
		return
	
        pShip = App.ShipClass_Cast(pObject)
        pInstance = FoundationTech.dShips[pShip.GetName()]
        iLongestTime = 0.0
        IncCurrentMoveID(pShip, pInstance)
        dHardpoints = {}
        
        # first replace the Models
        PrepareShipForMove(pShip, pInstance)
        
        for item in pInstance.OptionsList:
		# setup is not a submodel
                if item[0] == "Setup":
                        if item[1].has_key("WarpHardpoints"):
                                dHardpoints = item[1]["WarpHardpoints"]
                        continue
        
		# set the id for this move
                iThisMovID = item[1]["curMovID"][pShip.GetName()] + 1
                item[1]["curMovID"][pShip.GetName()] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("WarpDuration"):
                        fDuration = item[1]["WarpDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][pShip.GetName()]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("WarpRotation"):
                        lStoppingRotation = item[1]["WarpRotation"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][pShip.GetName()]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("WarpPosition"):
                        lStoppingTranslation = item[1]["WarpPosition"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, {})
                pSeq = App.TGSequence_Create()
                
		# do the move
                while(iTime < fDuration):
                        if iTime == 0.0:
                                iWait = 0.5 # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent), iWait)
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + 1
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
                pSeq.Play()
                
                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = iTimeNeededTotal
                
        # finally detach
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WarpStartMoveFinishAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance)), 2.0)
        pSeq.Play()

        pObject.CallNextHandler(pEvent)


def GetStartWarpNacellePositions(pShip):
	ret = []
	dHardpoints = {}
	
	if not FoundationTech.dShips.has_key(pShip.GetName()):
		return []
	
	pInstance = FoundationTech.dShips[pShip.GetName()]
	if hasattr(pInstance, "OptionsList"):
		for item in pInstance.OptionsList:
			if item[0] == "Setup":
                        	if item[1].has_key("WarpHardpoints"):
                                	dHardpoints = item[1]["WarpHardpoints"]
                        	continue

	pWarpSystem  = pShip.GetWarpEngineSubsystem()
	if pWarpSystem:
		for i in range(pWarpSystem.GetNumChildSubsystems()):
			pChild = pWarpSystem.GetChildSubsystem(i)
			
			if dHardpoints.has_key(pChild.GetName()):
				ret.append(App.NiPoint3(dHardpoints[pChild.GetName()][0], dHardpoints[pChild.GetName()][1], dHardpoints[pChild.GetName()][2]))
			else:
				ret.append(pChild.GetPosition())

	return ret
		

def ExitingWarp(pAction, pShip):
        debug(__name__ + ", ExitingWarp")
	
	if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
		debug(__name__ + ", ExitingWarp Return not host")
		return 0
	
        pInstance = FoundationTech.dShips[pShip.GetName()]
        iLongestTime = 0.0
        IncCurrentMoveID(pShip, pInstance)
        dHardpoints = {}
        
        # first replace the Models
        PrepareShipForMove(pShip, pInstance)
        
        for item in pInstance.OptionsList:
		# setup is not a submodel
                if item[0] == "Setup":
			dHardpoints = {}
                        if item[1].has_key("WarpHardpoints"):
                                dHardpoints = item[1]["WarpHardpoints"]
                        continue
        
		# set the id for this move
                iThisMovID = item[1]["curMovID"][pShip.GetName()] + 1
                item[1]["curMovID"][pShip.GetName()] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("WarpDuration"):
                        fDuration = item[1]["WarpDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][pShip.GetName()]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("AttackRotation") and pShip.GetAlertLevel() == 2:
                                lStoppingRotation = item[1]["AttackRotation"]
		else:
			lStoppingRotation = item[1]["Rotation"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][pShip.GetName()]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and pShip.GetAlertLevel() == 2:
                                lStoppingTranslation = item[1]["AttackPosition"]
		else:
			lStoppingTranslation = item[1]["Position"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
                pSeq = App.TGSequence_Create()
                
		# do the move
                while(iTime < fDuration):
                        if iTime == 0.0:
                                iWait = 0.5 # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent), iWait)
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + 1
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
                pSeq.Play()
                
                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = iTimeNeededTotal
                
        # finally detach
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WarpExitMoveFinishAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance)), 2.0)
        pSeq.Play()
        
        return 0


def DeleteObjectFromSet(pSet, sObjectName):
	if not MissionLib.GetShip(sObjectName):
		return
        pSet.DeleteObjectFromSet(sObjectName)
	
	# send clients to remove this object
        if App.g_kUtopiaModule.IsMultiplayer():
                # Now send a message to everybody else that the score was updated.
                # allocate the message.
                pMessage = App.TGMessage_Create()
                pMessage.SetGuaranteed(1)		# Yes, this is a guaranteed packet
                        
                # Setup the stream.
                kStream = App.TGBufferStream()		# Allocate a local buffer stream.
                kStream.OpenBuffer(256)				# Open the buffer stream with a 256 byte buffer.
	
                # Write relevant data to the stream.
                # First write message type.
                kStream.WriteChar(chr(REMOVE_POINTER_FROM_SET))

                # Write the name of killed ship
                for i in range(len(sObjectName)):
                        kStream.WriteChar(sObjectName[i])
                # set the last char:
                kStream.WriteChar('\0')

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
        return 0


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
        # TODO: Send it to asking client only
        pNetwork = App.g_kUtopiaModule.GetNetwork()
        if not App.IsNull(pNetwork):
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def MPSentReplaceModelMessage(pShip, sNewShipScript):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", MPSentReplaceModelMessage")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(REPLACE_MODEL_MSG))

	try:
		from Multiplayer.Episode.Mission4.Mission4 import dReplaceModel
		dReplaceModel[pShip.GetObjID()] = sNewShipScript
	except ImportError:
		pass

	# send Message
	kStream.WriteInt(pShip.GetObjID())
	iLen = len(sNewShipScript)
	kStream.WriteShort(iLen)
	kStream.Write(sNewShipScript, iLen)

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
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()


def mp_send_settargetable(iShipID, iMode):
        # Setup the stream.
        # Allocate a local buffer stream.
        debug(__name__ + ", mp_send_settargetable")
        kStream = App.TGBufferStream()
        # Open the buffer stream with a 256 byte buffer.
        kStream.OpenBuffer(256)
        # Write relevant data to the stream.
        # First write message type.
        kStream.WriteChar(chr(SET_TARGETABLE_MSG))

	# send Message
	kStream.WriteInt(iShipID)
	kStream.WriteInt(iMode)

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
                if App.g_kUtopiaModule.IsHost():
                        pNetwork.SendTGMessageToGroup("NoMe", pMessage)
                else:
                        pNetwork.SendTGMessage(pNetwork.GetHostID(), pMessage)
        # We're done.  Close the buffer.
        kStream.CloseBuffer()
