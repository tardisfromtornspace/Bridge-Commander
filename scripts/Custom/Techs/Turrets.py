#         Turrets
#         18th February 2024
#         Based strongly on SubModels.py by USS Defiant and their team, and AutoTargeting.py by USS Frontier.
#         Also based very slightly on the Borg Technology from Alex SL Gato, and ConditionInLineOfSight by the original STBC team
#################################################################################################################
# This tech gives a ship the ability to have working turrets, not merely props added - that is, the turrets aim and fire and that turn is visible.
# Please notice, that you must make turret script/Custom/Ships, scripts/ships and scripts/Ships/Hardpoints files for each turret. This tech will make it so, upon firing, all turrets with the same weapon subsystem name as the fired weapon will fire. 

# the scheme is that:
# 1. add normal model
# 2. replace model with body + turrets
# 3. move the turrets + consider original turret size re-escale (via the "SetScale" property; else there's a default smaller than the size)
# 4. replace body if necessary, but keep turrets moving around

# NOTE: THIS IS A VERY EXPERIMENTAL WORK-IN-PROGRESS, EXPECT BUGS
# KNOWN BUGS/UNINTENDED EFFECTS (By order of priority):
# - Turrets support AutoTargeting and MultiTargeting, but it is wonky (including random spinning and turrets aiming at each other). Behaviour may turn out even weirder if multiple parent ship weapons are assigned to the same turret (with each one aiming at a different target)
# --- IMPORTANT NOTE: In order to reduce issues, if your ships has AutoTargeting already, assign one SINGLE parent ship weapon per turret, and then just make the turret harpoint have the desired number of weapons of the same type (beam, torpedo, pulse or tractor).
# - Turrets when firing may hit and damage the parent ship shields and subsystems with their weaponry. # TO-DO possible fix would be to add an extra hardpoint that later moves and aligns with the subShip hardpoints?
# - Sometimes after reloading, turrets may not appear.
# - Sometimes a turret will keep firing even if the parent ship stopped firing.
# - At the moment turrets are invulnerable and can work as an effective physical shield for the subsystems underneath.
# - The presence of a model makes AI act evasive due to detecting for a moment "a collision course" with the turrets, despite being uncollidable.
# - Weapon intensity for phaser turrets is not currently being modulated - it is set to default #TO-DO MAYBE LOOK ADVANCED POWER CONTROL TO REGULATE POWER OF THE FIRED SUBSYSTEM?
# - For some reason, turrets are always bigger than the model... strange. Anyways, to help fix that, we've given a SetScale option to customize their size... albeit the turret hardpoint may need to be adjusted accordingly
# THINGS YET TO TEST FULLY
# - Trying to warp away.
# - Trying to cloak/decloak.

"""

Sample Setup:

Foundation.ShipDef.VasKholhr.dTechs = { 'Turret': {
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
                },
                "SetScale": 1.0
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
                },
                "SetScale": 1.0
        ],
}}



"""
from bcdebug import debug
import traceback

import App
import FoundationTech
import loadspacehelper
import math
import MissionLib


MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.7",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }


REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

globalTurretTimer = None
bOverflow = 0
#eTurretTime = App.Mission_GetNextEventType()
defaultSlice = 0.1 # In seconds

# This class does control the attach and detach of the Models
class Turrets(FoundationTech.TechDef):
        def __init__(self, name):
                debug(__name__ + ", Initiated Turrets counter")
                FoundationTech.TechDef.__init__(self, name)
                self.pTimer = None
                self.bBattleTurretListener = {}

        def countdown(self):
                debug(__name__ + ", Initiated Turret counter countdown")
                if not self.pTimer:
                        global defaultSlice
                        self.pTimer = App.PythonMethodProcess()
                        self.pTimer.SetInstance(self)
                        self.pTimer.SetFunction("aimingAtTarget")
                        self.pTimer.SetDelay(defaultSlice)
                        self.pTimer.SetPriority(App.TimeSliceProcess.LOW)        
                        self.pTimer.SetDelayUsesGameTime(1)

        def aimingAtTarget(self, fTime):
                debug(__name__ + ", Reality Bomb Counter lookclosershipsEveryone")
                for itemList in self.bBattleTurretListener.keys():
                        pShipID = self.bBattleTurretListener[itemList][0].GetObjID()
                        pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))

                        if pShip:
                                if self.bBattleTurretListener[itemList][-1] == 1:
                                        self.bBattleTurretListener[itemList][-1] = 0 # We are active in battle, but doing an action
                                        PartsForWeaponTurretState(pShip)
                        else:
                                del self.bBattleTurretListener[itemList]

        #TO-DO maybe add a getbBattleTurretListener for targeting things

        def SetBattleTurretListenerTo(self, pShip, value):
                debug(__name__ + ", ArePartsAttached")
                if not pShip:
                        return 0
                itemList = repr(pShip)
                if self.bBattleTurretListener.has_key(itemList):
                        self.bBattleTurretListener[itemList][-1] = value
                return 0

        # called by FoundationTech when a ship is created
        # Prepares the ship for moving its sub parts
        def AttachShip(self, pShip, pInstance):
                debug(__name__ + ", AttachShip")
                print "Ship %s with Turrets support added" % pShip.GetName()

                sNamePrefix = repr(pShip) + "_"
                pInstance.__dict__["OptionsList"] = [] # save options to this list, so we can access them later
                self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once
                self.bAddedAlertListener = {}

                ModelList = pInstance.__dict__["Turret"]
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
                                dOptions["AlertLevel"][repr(pShip)] = 0
                                dOptions["GenMoveID"][repr(pShip)] = 0
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
                        dOptions["currentRotation"][repr(pShip)] = [0, 0, 0] # those two lists are updated with every move
                        dOptions["currentPosition"][repr(pShip)] = [0, 0, 0]
                        dOptions["curMovID"][repr(pShip)] = 0
                        if not dOptions.has_key("Position"):
                                dOptions["Position"] = [0, 0, 0]
                        dOptions["currentPosition"][repr(pShip)] = dOptions["Position"] # set current Position
                        
                        if not dOptions.has_key("Rotation"):
                                dOptions["Rotation"] = [0, 0, 0]
                        dOptions["currentRotation"][repr(pShip)] = dOptions["Rotation"] # set current Rotation
                        
                        # event listener
                        if not self.bAddedWarpListener.has_key(repr(pShip)) and (dOptions.has_key("WarpRotation") or dOptions.has_key("WarpPosition")):
                                pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                                # ET_EXITED_WARP handler doesn't seem to work, so use ET_EXITED_SET instead
                                pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                                self.bAddedWarpListener[repr(pShip)] = 1
                        if not self.bAddedAlertListener.has_key(repr(pShip)) and (dOptions.has_key("AttackRotation") or dOptions.has_key("AttackPosition")):
                                pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertStateChanged")
                                # Alert change handler doesn't work for AI ships, so use subsystem changed instead
                                pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")

                                # TO-DO see why these 2 lines may break some of the code
                                pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

                                #Weapon Control
                                pShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                                # There's not good tolerance for torpedoes at the moment, potential TO-DO
                                pShip.AddPythonFuncHandlerForInstance(App.ET_TORPEDO_FIRED, __name__ + ".WeaponFiredStopAction")
    
                                self.bAddedAlertListener[repr(pShip)] = 1
                                AlertListener = 1
                                self.bBattleTurretListener[repr(pShip)] = [pShip, -1] # That means we are not active in battle
                                self.countdown()
                
                # Make sure the Ship is correctly set
                # because we don't get the first ET_SUBSYSTEM_STATE_CHANGED event for Ai ships
                if AlertListener:
                        PartsForWeaponState(pShip)

        # Called by FoundationTech when a Ship is removed from set (eg destruction)
        def DetachShip(self, iShipID, pInstance):
                # get our Ship
                debug(__name__ + ", DetachShip")
                pShip = App.ShipClass_GetObjectByID(None, iShipID)

                self.DetachParts(pShip, pInstance)

                if pShip:
                        # remove the listeners
                        if self.bAddedWarpListener.has_key(repr(pShip)):
                                pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
                                pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                                pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                                del self.bAddedWarpListener[repr(pShip)]
                        if self.bAddedAlertListener.has_key(repr(pShip)):
                                pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
                                pShip.RemoveHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertStateChanged")

                                pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
                                pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
                                pShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
                                pShip.RemoveHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                                pShip.RemoveHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                                pShip.RemoveHandlerForInstance(App.ET_TORPEDO_FIRED, __name__ + ".WeaponFiredStopAction")
                                del self.bAddedAlertListener[repr(pShip)]
                                del self.bBattleTurretListener[repr(pShip)]
                        
                        if hasattr(pInstance, "OptionsList"):
                                for item in pInstance.OptionsList:
                                        if item[0] == "Setup":
                                                del item[1]["AlertLevel"][repr(pShip)]
                                        else:
                                                del item[1]["currentRotation"][repr(pShip)]
                                                del item[1]["currentPosition"][repr(pShip)]
                                
                if hasattr(pInstance, "TurretList"):
                        del pInstance.TurretList

        # Attaches the SubParts to the Body Model
        def AttachParts(self, pShip, pInstance):
                debug(__name__ + ", AttachParts")
                pSet = pShip.GetContainingSet()
                pInstance.__dict__["TurretList"] = []
                ModelList = pInstance.__dict__["Turret"]
                sNamePrefix = repr(pShip) + "_"
                TurretList = pInstance.TurretList

                pProxManager = pSet.GetProximityManager()
                # iteeeerate over every Turret
                for sNameSuffix in ModelList.keys():
                        if sNameSuffix == "Setup":
                                continue

                        sFile = ModelList[sNameSuffix][0]
                        sShipName = sNamePrefix + sNameSuffix
                        
                        # check if the ship does exist first, before create it
                        pSubShip = MissionLib.GetShip(sShipName)
                        if not pSubShip:
                                pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "")
                        TurretList.append(pSubShip)
                        if len(ModelList[sNameSuffix]) > 1:
                                dOptions = ModelList[sNameSuffix][1]

                        # set current positions
                        pSubShip.SetTranslateXYZ(dOptions["currentPosition"][repr(pShip)][0],dOptions["currentPosition"][repr(pShip)][1],dOptions["currentPosition"][repr(pShip)][2])
                        iNorm = math.sqrt(dOptions["currentRotation"][repr(pShip)][0] ** 2 + dOptions["currentRotation"][repr(pShip)][1] ** 2 + dOptions["currentRotation"][repr(pShip)][2] ** 2)
                        pSubShip.SetAngleAxisRotation(1.0,dOptions["currentRotation"][repr(pShip)][0],dOptions["currentRotation"][repr(pShip)][1],dOptions["currentRotation"][repr(pShip)][2])
                        #pSubShip.SetScale(-iNorm + 1.85)
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
                        pSubShip.SetCollisionsOn(0)
                        pSubShip.GetShipProperty().SetMass(0.000001)
                        pSubShip.GetShipProperty().SetRotationalInertia(1.0e+25)
                        pSubShip.GetShipProperty().SetStationary(1)
                        pSubShip.SetHailable(0)
                        if pSubShip.GetShields():
                                pSubShip.GetShields().TurnOff()
            
                        pShip.EnableCollisionsWith(pSubShip, 0)
                        pSubShip.EnableCollisionsWith(pShip, 0)
                        MultiPlayerEnableCollisionWith(pShip, pSubShip, 0)
                        MultiPlayerEnableCollisionWith(pSubShip, pShip, 0)
                        for pSubShip2 in TurretList:
                                if pSubShip.GetObjID() != pSubShip2.GetObjID():
                                        pSubShip.EnableCollisionsWith(pSubShip2, 0)
                                        pSubShip2.EnableCollisionsWith(pSubShip, 0)
                                        MultiPlayerEnableCollisionWith(pSubShip, pSubShip2, 0)
                                        MultiPlayerEnableCollisionWith(pSubShip2, pSubShip, 0)

                        # pSubShip.DisableCollisionDamage()
                        # pSubShip.CanCollide(0)

                        #pProxManager = pSet.GetProximityManager()
                        #if pProxManager:
                        #    kIterator = pProxManager.GetNearObjects(pShip.GetWorldLocation(), 0.0, 0) #pProxManager.GetNearObjects(pShip.GetWorldLocation(), 50.0, 1)
                        #    intAux = 0
                        #    while(1):
                        #        pProximityCheck = pProxManager.GetNextObject(kIterator)
                        #        print "intAux = ", intAux
                        #        if not pProximityCheck:
                        #            print "we break"
                        #            break
                        #        try:
                        #            pProximityCheck.RemoveObjectFromCheckListByID(pSubShip.GetObjID())
                        #        except:
                        #            print "Failed to remove object from proximityCheck"
                        #            traceback.print_exc()
                        #        intAux = intAux + 1

                        #    pProxManager.EndObjectIteration(kIterator)

                        #pSubShip.SetCollisionFlags(App.ObjectClass.CFB_NO_COLLISIONS) # This does not help and funnily enough makes the game crash when the phaser hits the parent ship shield. Interesting...
                        #print pSubShip.GetCollisionFlags()

                        pSubShip.UpdateNodeOnly()
                        pShip.AttachObject(pSubShip)

        # check if parts are attached
        def ArePartsAttached(self, pShip, pInstance):
                debug(__name__ + ", ArePartsAttached")
                if hasattr(pInstance, "TurretList"):
                        return 1
                return 0

        # Detaches the parts
        def DetachParts(self, pShip, pInstance):
                debug(__name__ + ", DetachParts")
                if hasattr(pInstance, "TurretList"):
                        for pSubShip in pInstance.TurretList:
                                pSet = pSubShip.GetContainingSet()
                                pShip.DetachObject(pSubShip)
                                DeleteObjectFromSet(pSet, pSubShip.GetName())
                        del pInstance.TurretList
                
oTurrets = Turrets("Turret")


# The class does the moving of the parts
# with every move the part continues to move
class MovingEvent:
        # prepare fore move...
        def __init__(self, pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints):
                debug(__name__ + ", __init__")
                
                self.iNacelleID = item[0].GetObjID()
                self.iThisMovID = item[1]["curMovID"][repr(pShip)]
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
                                print "Turret Error: Unable to find Hardpoint %s" % sHP
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
        def __call__(self, pShip, pTarget=None):
                # if the move ID doesn't match then this move is outdated
                debug(__name__ + ", __call__")
                if self.iThisMovID != self.dOptionsList["curMovID"][repr(self.pShip)]:
                        print "Moving Error: Move no longer active"
                        return 1
                
                # this makes sure the game does not crash when trying to access a deleted element
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        #print "Moving Error: Lost part"
                        return 0
                        
                # set new Rotation values
                if pTarget == None:
                    if self.dOptionsList.has_key("TARGET"):
                        if self.dOptionsList["TARGET"].has_key(repr(pShip)):
                            #print "Custom one: ", self.dOptionsList["TARGET"]
                            pTarget = self.dOptionsList["TARGET"][repr(pShip)]
                            if pTarget:
                                pTarget = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
                            if not pTarget or pTarget.IsDead() or pTarget.IsDying() or pTarget.GetObjID() == self.iNacelleID:
                                pTarget = pShip.GetTarget()
                        else:
                            pTarget = pShip.GetTarget()
                    else:
                        pTarget = pShip.GetTarget()
                else:
                        self.dOptionsList["TARGET"] = pTarget

                while pTarget and (pTarget.GetObjID() == self.iNacelleID): # another safety feature for doofus AutoTargeting scripts
                    pTarget = pShip.GetNextTarget()

                if pTarget:
                        kNacelleLocation = pNacelle.GetWorldLocation()
                        kTargetLocation = pTarget.GetWorldLocation()
                        kShipLocation = pShip.GetWorldLocation()

                        kNewUpReal = pShip.GetWorldUpTG() # pShip.GetWorldForwardTG()
                        #kNewUp = pShip.GetWorldUpTG()
                        kNewForward = pShip.GetWorldForwardTG()

                        kTargetLocation.Subtract(kNacelleLocation)

                        kFwd = kTargetLocation
                        kFwd.Unitize()

                        #kNewUpAux = kNewUpReal.Perpendicular()

                        kNewUp = App.TGPoint3()
                        kNewUp.SetXYZ(kNewUpReal.x, kNewUpReal.y, kNewUpReal.z)

                        kPerp = kFwd.Perpendicular()
                        kPerp2 = App.TGPoint3()
                        kPerp2.SetXYZ(kPerp.x, kPerp.y, kPerp.z)

                        #kFwd.Perpendicular() ... would it give us any perpendicular in particular? If so, maybe another manual option would be better, we want the perpendicular parallel to the kNewUp
                        # Step 1: a x b, with a and b being the kFwd and the kNewUp
                        vAuxVx, vAuxVy, vAuxVz = MatrixMult(kFwd, kNewUp)

                        if vAuxVx == 0.0 and vAuxVy == 0.0 and vAuxVz == 0.0: # No other option, we share the same rect
                            pNacelle.AlignToVectors(kFwd, kPerp2) # Aims correctly but gives a weird clockwise or counterclockwise turn if the ship rotates
                        else:
                            kVect1 = App.TGPoint3()
                            kVect1.SetXYZ(vAuxVx, vAuxVy, vAuxVz)
                            #pNacelle.AlignToVectors(kFwd, kVect1)

                            #Now that we got a x b, we want to get (a x b) x a = kVect1 x a, to get the perpendicular we really want
                            vAuxVx, vAuxVy, vAuxVz = MatrixMult(kVect1, kFwd)


                            kVect2 = App.TGPoint3()
                            kVect2.SetXYZ(vAuxVx, vAuxVy, vAuxVz)
                            kVect2.Unitize()

                            pNacelle.AlignToVectors(kFwd, kVect2)

                        if self.dOptionsList.has_key("SetScale"):
                            pNacelle.SetScale(dOptionsList["SetScale"])
                        else:
                            pNacelle.SetScale(0.5)
            
                        #pNacelle.AlignToVectors(kFwd, kNewUp) # aims without clockwise or counterclockwise turn, but no turn-up
                        #pNacelle.AlignToVectors(kFwd, kPerp2) # Aims correctly but gives a weird clockwise or counterclockwise turn if the ship rotates

                        #tNewY = pShip.GetWorldForwardTG() 
                        #tNewZ = pShip.GetWorldForwardTG()

                        #vScalar = kFwd.x * kNewUp.x + kFwd.y * kNewUp.y + kFwd.z * kNewUp.z 
                        #angleUp = math.acos(vScalar)

                        #uniMatrix = pNacelle.GetWorldRotation()
                        #uniMatrix.MakeXRotation(angleUp)
                        #pNacelle.Rotate(uniMatrix) # Trying to rotate it this way or by pNacelle.SetAngleAxisRotation(1.0, kPerp.x, kPerp.y, kPerp.z) causes a ton of resize problems


                #self.iCurRotX = self.iCurRotX + self.iRotStepX
                #self.iCurRotY = self.iCurRotY + self.iRotStepY
                #self.iCurRotZ = self.iCurRotZ + self.iRotStepZ
                #iNorm = math.sqrt(self.iCurRotX ** 2 + self.iCurRotY ** 2 + self.iCurRotZ ** 2)
                # set Rotation
                #pNacelle.SetAngleAxisRotation(1.0, self.iCurRotX, self.iCurRotY, self.iCurRotZ)
                #pNacelle.SetScale(1.0)

                # set new Translation values
                self.iCurTransX = self.iCurTransX + self.iTransStepX
                self.iCurTransY = self.iCurTransY + self.iTransStepY
                self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
                # set Translation
                pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)
                
                self.dOptionsList["currentRotation"][repr(self.pShip)] = [self.iCurRotX, self.iCurRotY, self.iCurRotZ]
                self.dOptionsList["currentPosition"][repr(self.pShip)] = [self.iCurTransX, self.iCurTransY, self.iCurTransZ]
                
                # Hardpoints
                for sHP in self.dCurHPs.keys():
                        self.dCurHPs[sHP][0] = self.dCurHPs[sHP][0] + self.dHPSteps[sHP][0]
                        self.dCurHPs[sHP][1] = self.dCurHPs[sHP][1] + self.dHPSteps[sHP][1]
                        self.dCurHPs[sHP][2] = self.dCurHPs[sHP][2] + self.dHPSteps[sHP][2]
                        UpdateHardpointPositionsTo(self.pShip, sHP, self.dCurHPs[sHP])
                
                pNacelle.UpdateNodeOnly()
                return 0

        def isCloaking(self, pShip):
                # if the move ID doesn't match then this move is outdated
                debug(__name__ + ", __call__")
                if self.iThisMovID != self.dOptionsList["curMovID"][repr(self.pShip)]:
                        print "Moving Error: Move no longer active"
                        return 1
                
                # this makes sure the game does not crash when trying to access a deleted element
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        #print "Moving Error: Lost part"
                        return 0

                pCloak = pNacelle.GetCloakingSubsystem()
                if pCloak:
                        pCloak.StartCloaking()

        def isDecloaking(self, pShip):
                # if the move ID doesn't match then this move is outdated
                debug(__name__ + ", __call__")
                if self.iThisMovID != self.dOptionsList["curMovID"][repr(self.pShip)]:
                        print "Moving Error: Move no longer active"
                        return 1
                
                # this makes sure the game does not crash when trying to access a deleted element
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        #print "Moving Error: Lost part"
                        return 0

                pCloak = pNacelle.GetCloakingSubsystem()
                if pCloak:
                        pCloak.InstantDecloak()

def MatrixMult(kFwd, kNewUp):
    vAuxVx = kFwd.y * kNewUp.z - kNewUp.y * kFwd.z
    vAuxVy = kNewUp.x * kFwd.z - kFwd.x * kNewUp.z
    vAuxVz = kFwd.x * kNewUp.y - kNewUp.x * kFwd.y
    return vAuxVx, vAuxVy, vAuxVz

# calls the MovingEvent class and returns its return value
def MovingAction(pAction, oMovingEvent, pShip):
        debug(__name__ + ", MovingAction")
        return oMovingEvent(pShip)


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
# cause this is possibly also an alert event
def SubsystemStateChanged(pObject, pEvent):
        debug(__name__ + ", SubsystemStateChanged")

        pShip = App.ShipClass_Cast(pObject)
        pSubsystem = pEvent.GetSource()
        #print "pSubsystem: ", pSubsystem
        # if the subsystem that changes its power is a weapon
        if not pSubsystem:
                pObject.CallNextHandler(pEvent)
                return

        wpnActiveState = pEvent.GetBool()

        if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM): # in theory this should be enough, in practice...
                #print "pSubsystem is a weapon system "
                # set turrets for this alert state
                PartsForWeaponState(pShip, wpnActiveState)
        else:
                #print "pSubsystem is NOT a weapon system "
                try:
                        pParent = pSubsystem.GetParentSubsystem()
                        if pParent and (pParent.IsTypeOf(App.CT_WEAPON_SYSTEM) or pParent.IsTypeOf(App.CT_PHASER_SYSTEM) or pSubsystem.IsTypeOf(App.CT_PULSE_WEAPON_SYSTEM) or pSubsystem.IsTypeOf(App.CT_TORPEDO_SYSTEM)):
                                PartsForWeaponState(pShip, wpnActiveState)
                except:
                        pass

        pObject.CallNextHandler(pEvent)
        return

def CloakHandler(pObject, pEvent):
        pInstance = FoundationTech.dShips[pObject.GetName()]

        pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

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
        
        # update alert state
        dGenShipDict["AlertLevel"][repr(pShip)] = iType
        IncCurrentMoveID(pShip, pInstance)

        # iterate over every Turret

        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        # attack or cruise modus?
                        dHardpoints = {}
                        if iType == 2 and item[1].has_key("AttackHardpoints"):
                                dHardpoints = item[1]["AttackHardpoints"]
                        elif iType != 2 and item[1].has_key("Hardpoints"):
                                dHardpoints = item[1]["Hardpoints"]
                        
                        # setup is not a Turret
                        continue

                # set the id for this move
                iThisMovID = item[1]["curMovID"][repr(pShip)] + 1
                item[1]["curMovID"][repr(pShip)] = iThisMovID
        
                fDuration = 1000.0
                #if item[1].has_key("AttackDuration"):
                #        fDuration = item[1]["AttackDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][repr(pShip)]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("AttackRotation") and iType == 2:
                        lStoppingRotation = item[1]["AttackRotation"]
                else:
                        lStoppingRotation = item[1]["Rotation"]
                
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][repr(pShip)]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and iType == 2:
                        lStoppingTranslation = item[1]["AttackPosition"]
                else:
                        lStoppingTranslation = item[1]["Position"]
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
                oMovingEvent.isCloaking(pShip)

        pObject.CallNextHandler(pEvent)

def DecloakHandler(pObject, pEvent):
        pInstance = FoundationTech.dShips[pObject.GetName()]

        pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

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
        
        # update alert state
        dGenShipDict["AlertLevel"][repr(pShip)] = iType
        IncCurrentMoveID(pShip, pInstance)

        # iterate over every Turret

        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        # attack or cruise modus?
                        dHardpoints = {}
                        if iType == 2 and item[1].has_key("AttackHardpoints"):
                                dHardpoints = item[1]["AttackHardpoints"]
                        elif iType != 2 and item[1].has_key("Hardpoints"):
                                dHardpoints = item[1]["Hardpoints"]
                        
                        # setup is not a Turret
                        continue

                # set the id for this move
                iThisMovID = item[1]["curMovID"][repr(pShip)] + 1
                item[1]["curMovID"][repr(pShip)] = iThisMovID
        
                fDuration = 1000.0
                #if item[1].has_key("AttackDuration"):
                #        fDuration = item[1]["AttackDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][repr(pShip)]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("AttackRotation") and iType == 2:
                        lStoppingRotation = item[1]["AttackRotation"]
                else:
                        lStoppingRotation = item[1]["Rotation"]
                
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][repr(pShip)]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and iType == 2:
                        lStoppingTranslation = item[1]["AttackPosition"]
                else:
                        lStoppingTranslation = item[1]["Position"]
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
                oMovingEvent.isDecloaking(pShip)

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
        if not oTurrets.ArePartsAttached(pShip, pInstance):
                ReplaceModel(pShip, pInstance.__dict__["Turret"]["Setup"]["Body"])
                oTurrets.AttachParts(pShip, pInstance)


def IncCurrentMoveID(pShip, pInstance):
        debug(__name__ + ", IncCurrentMoveID")
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        item[1]["GenMoveID"][repr(pShip)] = item[1]["GenMoveID"][repr(pShip)] + 1


def GetCurrentMoveID(pShip, pInstance):
        debug(__name__ + ", GetCurrentMoveID")
        iGenMoveID = 0
        
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        iGenMoveID = item[1]["GenMoveID"][repr(pShip)]
        return iGenMoveID
                        

def MoveFinishMatchId(pShip, pInstance, iThisMovID):
        debug(__name__ + ", MoveFinishMatchId")
        if GetCurrentMoveID(pShip, pInstance) == iThisMovID:
                return 1
        return 0
        
def findShipInstance(pShip):
        pInstance = None
        try:
                if not pShip:
                        return pInstance
                pInstance = FoundationTech.dShips[pShip.GetName()]
                if pInstance == None:
                        print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
                
        except:
                print "Error while looking for pInstance for Turret technology:"
                traceback.print_exc()
                
        #finally:
        return pInstance

def CheckLOS(pObject1, pObject2, pObjectInBetween, pSet):
	debug(__name__ + ", CheckLOS")
	bBlockedLOS = 0

	# Get the proximity manager...
	pProxManager = pSet.GetProximityManager()

	if pProxManager:
		# Get a list of objects between pObject1 and pObject2
		kIter = pProxManager.GetLineIntersectObjects(pObject1.GetWorldLocation(), pObject2.GetWorldLocation(), 0)
		pObject = pProxManager.GetNextObject(kIter)
		while (pObject != None):
			# Is this object the object we're looking for?
			if repr(pObject) == repr(pObjectInBetween):
				# Yep.  We're now true.
				bBlockedLOS = 1
				break
			pObject = pProxManager.GetNextObject(kIter)
		pProxManager.EndObjectIteration(kIter)

	return bBlockedLOS

def WeaponFiredStopAction(pObject, pEvent):
        debug(__name__ + ", AlertStateChanged")

        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WeaponFiredStopActionAux", pObject, pEvent), 0.1)
        pSeq.Play()

def WeaponFiredStopActionAux(pAction, pObject, pEvent):
        WeaponFiredStop(pObject, pEvent)

def WeaponFiredStop(pObject, pEvent, stoppedFiring=None):
        #TO-DO  .... MERGE WITH WEAPONFIRED
        debug(__name__ + ", WeaponFired")

        #print "The pEvent destination of stopped fire is ", pEvent.GetDestination()

        pShip = App.ShipClass_Cast(pObject)
        pInstance = None
        if pShip:
                #print "Found ship: ", pShip.GetName()
                pInstance = findShipInstance(pShip)

        if pInstance and pInstance.__dict__.has_key("Turret"):
                pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
                if pWeaponFired == None:
                        print "no weapon stopped fired obj..."
                        return

                pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
                if not pTarget:
                    pTarget = pShip.GetTarget()

                pParentFired = pWeaponFired.GetParentSubsystem()
                if pParentFired == None:
                        print "no weapon stop-fire parent subsystem obj..."
                        pObject.CallNextHandler(pEvent)
                        return

                weaponParentName = pParentFired.GetName()
                weaponName = pWeaponFired.GetName()

                lTurretsToFire = {}
                #lDoNotAttackYourself = []
                if hasattr(pInstance, "TurretList"):
                        for pSubShip in pInstance.TurretList:
                                #lDoNotAttackYourself.append(pSubShip) # Because some versions of AutoTargeting are wonky, they may target non-enemies, meaning the turret could have aimed at another friendly turret of themselves
                                mySubsystem = MissionLib.GetSubsystemByName(pSubShip, weaponName)
                                if mySubsystem != None:
                                        mySubsWep = App.Weapon_Cast(mySubsystem)
                                        thisParent = mySubsWep.GetParentSubsystem()
                                        for item in pInstance.OptionsList:
                                            if item[0] != "Setup" and item[0].GetObjID() == pSubShip.GetObjID():
                                                lTurretsToFire[repr(pSubShip)] = [pSubShip, mySubsystem, item, thisParent]
                                                break

                if lTurretsToFire:

                        #for turret in lTurretsToFire:
                        for turret in lTurretsToFire.keys():
                                print "TURRET TO STOP ", lTurretsToFire[turret][0].GetName()

                                wpnSystem = App.WeaponSystem_Cast(lTurretsToFire[turret][-1])

                                if wpnSystem != None:
                                        print "STOP FIRING BATTERIES!!!"
                                        for anotherTurret in pInstance.TurretList:
                                            wpnSystem.StopFiringAtTarget(anotherTurret) # NOTE: see if they have accidentally attacked themselves... it could be possible with other scripts!!!   

                                        #lTurretsToFire[turret][-2][1]["TARGET"][repr(pShip)] = None # In theory unnecessary but it should help with some rotational wonky behaviour
                                        if pTarget:
                                            wpnSystem.StopFiringAtTarget(pTarget)
                                        #else: # We decided to remove these to ensure that when we ask a turret to stop firing a certain type of weapon, it stops firing that weapon.
                                        wpnSystem.StopFiring()
                         

                                        wpnSystem.SetForceUpdate(1)
                                #else:
                                #        print "We have gone so far, what do you mean you don't have the system to fire???"
                        
        pObject.CallNextHandler(pEvent)


def WeaponFired(pObject, pEvent, stoppedFiring=None):
        #TO-DO  ....
        debug(__name__ + ", WeaponFired")

        pShip = App.ShipClass_Cast(pObject)
        pInstance = None
        if pShip:
                pInstance = findShipInstance(pShip)

        if pInstance and pInstance.__dict__.has_key("Turret"):
                pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
                if pWeaponFired == None:
                        print "no weapon fired obj..."
                        return

                pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
                if not pTarget:
                    pTarget = pShip.GetTarget()
                    while pTarget in pInstance.TurretList: # another safety feature for doofus AutoTargeting scripts
                        pTarget = pShip.GetNextTarget()

                pParentFired = pWeaponFired.GetParentSubsystem()
                if pParentFired == None:
                        pObject.CallNextHandler(pEvent)
                        return

                weaponParentName = pParentFired.GetName()
                weaponName = pWeaponFired.GetName()

                lTurretsToFire = {}
                if hasattr(pInstance, "TurretList"):
                        for pSubShip in pInstance.TurretList:
                                mySubsystem = MissionLib.GetSubsystemByName(pSubShip, weaponName)
                                if mySubsystem != None:
                                        mySubsWep = App.Weapon_Cast(mySubsystem)
                                        thisParent = mySubsWep.GetParentSubsystem()
                                        for item in pInstance.OptionsList:
                                            if item[0] != "Setup" and item[0].GetObjID() == pSubShip.GetObjID():
                                                lTurretsToFire[repr(pSubShip)] = [pSubShip, mySubsystem, item, thisParent]
                                                break

                shouldWeTakeMeasuresToAvoidGettingHit = (pTarget in pInstance.TurretList) # Because some versions of AutoTargeting are wonky, they may target non-enemies, meaning the turret could have aimed at another friendly turret of themselves
                if lTurretsToFire:

                        #for turret in lTurretsToFire:
                        for turret in lTurretsToFire.keys():
                                print "TURRET ", lTurretsToFire[turret][0].GetName()

                                wpnSystem = App.WeaponSystem_Cast(lTurretsToFire[turret][-1])

                                if wpnSystem != None:
                                        print "FIRING BATTERIES!!!"

                                        if pTarget and not shouldWeTakeMeasuresToAvoidGettingHit: # Just a safety precaution for some AutoTargeting scripts deciding to attack its own turret
                                            if not lTurretsToFire[turret][-2][1].has_key("TARGET"):
                                                lTurretsToFire[turret][-2][1]["TARGET"] = {}
                                            lTurretsToFire[turret][-2][1]["TARGET"][repr(pShip)] = pTarget #item[1]["TARGET"][repr(pShip)] = pTarget
                                            #lTurretsToFire[turret][0].SetTarget(pTarget)
                                            pSet = lTurretsToFire[turret][0].GetContainingSet()
                                            mothershipBlock = CheckLOS(pTarget, lTurretsToFire[turret][0], pShip, pSet) # TO-DO check why this is not preventing the turrets from firing through the parent ship
                                            if mothershipBlock:
                                                wpnSystem.StopFiring()
                                            else:
                                                wpnSystem.StopFiring() # TO-DO Safety check for strays due to multi-targeting
                                                wpnSystem.StartFiring(pTarget)
                                        else:
                                            if not lTurretsToFire[turret][-2][1].has_key("TARGET"):
                                                lTurretsToFire[turret][-2][1]["TARGET"] = {}
                                            lTurretsToFire[turret][-2][1]["TARGET"][repr(pShip)] = pShip.GetTarget()# TO-DO check if AI can decide to target this for no reason

                                        for anotherTurret in pInstance.TurretList:
                                            wpnSystem.StopFiringAtTarget(anotherTurret) # NOTE: see if they have accidentally attacked themselves... it could be possible with other scripts!!!

                                        wpnSystem.SetForceUpdate(1)
                                        #wpnSystem.StopFiringAtTarget(pTarget)
                                #else:
                                #        print "We have gone so far, what do you mean you don't have the system to fire???"
                        
        pObject.CallNextHandler(pEvent)

# called after the Alert move action
# Remove the attached parts and use the attack or normal model now
def AlertMoveFinishTemporarilyAction(pAction, pShip, pInstance, iThisMovID, iType=None):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", AlertMoveFinishTemporarilyAction")

        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
#TO-DO AQUÍ SIGUES
        # Ok so here we add the main ship to a timer list

        #if iType == None:
        #    iType = pShip.GetAlertLevel()
        #iType = pShip.GetAlertLevel()
       
        if pShip.GetAlertLevel() == 2 or iType == 2:
                if oTurrets.ArePartsAttached(pShip, pInstance):
                        oTurrets.SetBattleTurretListenerTo(pShip, 1)
                #sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["AttackModel"]
        else:
                if oTurrets.ArePartsAttached(pShip, pInstance):
                        oTurrets.SetBattleTurretListenerTo(pShip, -1) # Not combat mode
                sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["NormalModel"]
                oTurrets.DetachParts(pShip, pInstance) # we hide turrets when not in alert mode, else we keep them

        # For some reason this line below leads to the ship getting dark until you fire
        #ReplaceModel(pShip, sNewShipScript)
### 
        return 0

# called after the Alert move action
# Remove the attached parts and use the attack or normal model now
def AlertMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", AlertMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
        
        oTurrets.DetachParts(pShip, pInstance)
        if pShip.GetAlertLevel() == 2:
                sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["AttackModel"]
        else:
                sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["NormalModel"]
        ReplaceModel(pShip, sNewShipScript)
        
        return 0


# called after the warp-start move action
# Remove the attached parts and use the warp model now
def WarpStartMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", WarpStartMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
                
        oTurrets.DetachParts(pShip, pInstance)
        sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["WarpModel"]
        ReplaceModel(pShip, sNewShipScript)
        return 0


# called after the warp-exit move action
# Remove the attached parts and use the attack or normal model now
def WarpExitMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", WarpExitMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1
                
        oTurrets.DetachParts(pShip, pInstance)
        if pInstance.__dict__["Turret"]["Setup"].has_key("AttackModel") and pShip.GetAlertLevel() == 2:
                sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["AttackModel"]
        else:
                sNewShipScript = pInstance.__dict__["Turret"]["Setup"]["NormalModel"]
        ReplaceModel(pShip, sNewShipScript)
        return 0
        

# called after a move, sets the current Rotation/Translation values to the final ones
def UpdateState(pAction, pShip, item, lStoppingRotation, lStoppingTranslation):
        debug(__name__ + ", UpdateState")
        item[1]["currentRotation"][repr(pShip)] = lStoppingRotation
        item[1]["currentPosition"][repr(pShip)] = lStoppingTranslation
        item[1]["curMovID"][repr(pShip)] = 0
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
                print "Turret Error: Unable to find Hardpoint %s" % sHP
        pShip.UpdateNodeOnly()


def UpdateHardpointPositions(pAction, pShip, dHardpoints):
        debug(__name__ + ", UpdateHardpointPositions")

        for sHP in dHardpoints.keys():
                UpdateHardpointPositionsTo(pShip, sHP, dHardpoints[sHP])
        return 0


# Set the parts to the correct alert state
def PartsForWeaponState(pShip, weaponsActive=None):        
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
        # TO-DO VERIFY THIS SEMAPHORE WORKS
        oTurrets.SetBattleTurretListenerTo(pShip, 0)
        
        # try to get the last alert level
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        dGenShipDict = item[1]
                        break

        # update alert state
        auxLevel = None
        if weaponsActive == 1 or iType == 2: 
            auxLevel = 2
        else:
            auxLevel = iType

        # check if the alert state has really changed since the last time
        if dGenShipDict["AlertLevel"][repr(pShip)] == auxLevel:
                return

        dGenShipDict["AlertLevel"][repr(pShip)] = auxLevel
        
        MovingProcess(pShip, pInstance, auxLevel, iLongestTime, dHardpoints, dGenShipDict)

# Set things for turret aiming when not in alert switch
def PartsForWeaponTurretState(pShip):        
        debug(__name__ + ", PartsForWeaponState")
        
        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return
        
        pInstance = FoundationTech.dShips[pShip.GetName()]
        #iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        dHardpoints = {}
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        # TO-DO VERIFY THIS SEMAPHORE WORKS
        oTurrets.SetBattleTurretListenerTo(pShip, 0)

        # try to get the last alert level
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        dGenShipDict = item[1]
                        break
        
        # update alert state
        #dGenShipDict["AlertLevel"][repr(pShip)] = iType
        iType = dGenShipDict["AlertLevel"][repr(pShip)]
        
        MovingProcess(pShip, pInstance, iType, iLongestTime, dHardpoints, dGenShipDict)


def MovingProcess(pShip, pInstance, iType, iLongestTime, dHardpoints, dGenShipDict):
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        IncCurrentMoveID(pShip, pInstance)
        
        # start with replacing the Models
        PrepareShipForMove(pShip, pInstance)

        # iterate over every Turret
        for item in pInstance.OptionsList:
                if item[0] == "Setup":
                        # attack or cruise modus?
                        dHardpoints = {}
                        if iType == 2 and item[1].has_key("AttackHardpoints"):
                                dHardpoints = item[1]["AttackHardpoints"]
                        elif iType != 2 and item[1].has_key("Hardpoints"):
                                dHardpoints = item[1]["Hardpoints"]
                        
                        # setup is not a Turret
                        continue
        
                # set the id for this move
                iThisMovID = item[1]["curMovID"][repr(pShip)] + 1
                item[1]["curMovID"][repr(pShip)] = iThisMovID

                #TO-DO Revise if necessary to add the item target here again?
        
                fDuration = 200.0
                if item[1].has_key("AttackDuration"):
                        fDuration = item[1]["AttackDuration"]

                # Rotation
                lStartingRotation = item[1]["currentRotation"][repr(pShip)]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("AttackRotation") and iType == 2:
                        lStoppingRotation = item[1]["AttackRotation"]
                else:
                        lStoppingRotation = item[1]["Rotation"]
                
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][repr(pShip)]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and iType == 2:
                        lStoppingTranslation = item[1]["AttackPosition"]
                else:
                        lStoppingTranslation = item[1]["Position"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingRotation, lStoppingRotation, lStartingTranslation, lStoppingTranslation, dHardpoints)
# TO-DO EXTRA ADDITION HOPEFULLY TO REPLACE THE HANDLERS WHICH SEEM TO CAUSE AN ISSUE AS WELL

                pCloak = pShip.GetCloakingSubsystem()
                if pCloak:
                        if pCloak.IsCloaking():
                                oMovingEvent.isCloaking(pShip)
                        else:
                                if pCloak.IsDecloaking():
                                        oMovingEvent.isDecloaking(pShip)
                pSeq = App.TGSequence_Create()
                
                # do the move
                while(iTime < fDuration):
                        if iTime == 0.0:
                                iWait = 0.02 # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent, pShip), iWait)
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + 1
                pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingRotation, lStoppingTranslation))
                pSeq.Play()
                
                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = iTimeNeededTotal
                
        # finally detach?

        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints), iLongestTime)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "AlertMoveFinishTemporarilyAction", pShip, pInstance, GetCurrentMoveID(pShip, pInstance), iType), iLongestTime) #, iType #TO-DO WHY ADDING THAT CAUSES THE LOCK TO STOP WORKING, FIX
        pSeq.Play()

        return 0


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
                # setup is not a Turret
                if item[0] == "Setup":
                        if item[1].has_key("WarpHardpoints"):
                                dHardpoints = item[1]["WarpHardpoints"]
                        continue
        
                # set the id for this move
                iThisMovID = item[1]["curMovID"][repr(pShip)] + 1
                item[1]["curMovID"][repr(pShip)] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("WarpDuration"):
                        fDuration = item[1]["WarpDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][repr(pShip)]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("WarpRotation"):
                        lStoppingRotation = item[1]["WarpRotation"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][repr(pShip)]
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
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent, pShip), iWait)
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
                # setup is not a Turret
                if item[0] == "Setup":
                        dHardpoints = {}
                        if item[1].has_key("WarpHardpoints"):
                                dHardpoints = item[1]["WarpHardpoints"]
                        continue
        
                # set the id for this move
                iThisMovID = item[1]["curMovID"][repr(pShip)] + 1
                item[1]["curMovID"][repr(pShip)] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("WarpDuration"):
                        fDuration = item[1]["WarpDuration"]
                    
                # Rotation
                lStartingRotation = item[1]["currentRotation"][repr(pShip)]
                lStoppingRotation = lStartingRotation
                if item[1].has_key("AttackRotation") and pShip.GetAlertLevel() == 2:
                                lStoppingRotation = item[1]["AttackRotation"]
                else:
                        lStoppingRotation = item[1]["Rotation"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"][repr(pShip)]
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
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent, pShip), iWait)
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
                pMessage.SetGuaranteed(1)                # Yes, this is a guaranteed packet
                        
                # Setup the stream.
                kStream = App.TGBufferStream()                # Allocate a local buffer stream.
                kStream.OpenBuffer(256)                                # Open the buffer stream with a 256 byte buffer.
        
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
