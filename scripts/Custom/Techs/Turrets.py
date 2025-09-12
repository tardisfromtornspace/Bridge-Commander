"""
#         Turrets
#         11th September 2025
#         Based strongly on SubModels.py by USS Defiant and their team, and AutoTargeting.py by USS Frontier.
#         Also based slightly on AdvancedTorpedoManagement.py from BCSTB Team, the Borg Technology from Alex SL Gato, and ConditionInLineOfSight by the original STBC team
#         Special thanks to USS Sovereign and Gizmo_3.
#################################################################################################################
# This tech gives a ship the ability to have working turrets, not merely props added - that is, the turrets aim and fire and that turn is visible.
# - Please notice, that you must make turret script/Custom/Ships, scripts/ships and scripts/Ships/Hardpoints files for each turret. This tech will make it so, upon firing, all turrets with the same weapon subsystem name as the 
# fired weapon will fire. 
# - Depending on the hardpoint and weapon used, the turrets can be fully functional and really fire for themselves, or be aesthethic and only aim at where the weapon they are tied to is aiming (f.ex by needing a higher charge 
# to fire than the max, not having torpedoes, etc.). Aesthethic turrets are possible because those subShips are removed from the ProximityManager, they become ghosts that can fire on other ships without risking getting hit by ships
# or weapons. Aesthethic turrets however may be only necessary for beams.
# -- IMPORTANT NOTE: Due to the Proximity Manager thing, the parent ship can fire through, meaning that, in a functional turret, it may be sometimes preferable to replace the parent weapon with a super-thin/small/not noticeable and
#    almost harmless weapon (like a very small/thin transparent torpedo/pulse or beam).
# -- When several turrets are created, it is strongly recommended to create a generic Hardpoint template with everything available, including cloak, engines and alternative measures of travel, and then import such template for other
#    turrets, overwriting the "ShipProperty_" imported to have a unique name, and adding the appropiate weapon to track. This also allows to add a type of turret desired for the job, so f.ex. the parent fires 1 weapon, but the turret 
#    fires 7 weapons at the same time, or another weapon type... even a tractor turret! That would be funny to watch, not gonna lie!
# --- If you make a tractor turret, please notice that a functional tractor turret will not fire tractor beams if they are under the parent shield, but if there's no shield they will fire and grab anything in their line, so if the 
#     parent has a piece of them between tractor and target, you can actually tractor the parent in place! This could be useful in a niche amount of cases, but in other cases, I recommend using something similar to phasers, 
#     "SimulatedTractor" to 1.
# --- IMPORTANT NOTE: In order to reduce issues, if your ship has AutoTargeting already, assign one SINGLE parent ship weapon per turret, and then just make the turret hardpoint have the desired number of weapons of the same type 
#     (beam, torpedo, pulse or tractor). Also, for the sake of STABILITY and not having wonky behaviour, do not create turrets for turrets without extreme caution nor add the AutoTargeting to the turret itself (the latter is already taken care of by the parent)!!!
# --- From version 0.9993, "Tactical.Projectiles.AutomaticSystemRepairDummy" and "ftb.Tech.ATPFunctions" are required as dependencies.

# The scheme is that: # TO-DO SEE IF BY NOT DETACHING THE PARTS WE CAN GET SOMETHING ELSE... IF THAT WORKS THEN CHANGE THE SYSTEM BEHAVIOUR
# 1. add normal model
# 2. replace model with body + turrets if red alert or weapons are activated
# 3. move the turrets + consider original turret size re-escale (for some reason, turrets are always bigger than the model... strange. Anyways, to help fix that, we've given the "SetScale" property; else there's a default 0.5 times
# smaller than the "inflated" size... albeit the turret hardpoint may need to be adjusted accordingly).
# 4. replace body if necessary, but keep turrets moving around
# 5. if red alert is cancelled or it is not red alert but the weapons are deactivated, or the ship warps away, pull back the turrets.
# 6. When parent ship fires, we aim, and maybe fire as well.
# 6a. OPTIONAL - CANCELLED: if "SyncTorpType" is set to 1 for a turret, upon changing torpedo types, it will change them as well for that turret only.
## REASON OF CANCEL - SEE LIMITATION 3.

# Please note that there's a field in Setup "ShieldOption", if it doesn't exist or is set to 0, shields will work normally - else shields will drop when turrets are active - this is useful for some functional turrets that are inside
# the shield grid, or for lore reasons!

# NOTE: If the versioning being below 1.0 did not give you a hint, this is an experimental work-in-progress, it may be possible to find far more bugs
# KNOWN UNINTENDED EFFECTS, BUGS, LIMITATIONS and other TO-DOs (By order of priority):

# 1. Functional turrets when firing may hit and damage the parent ship shields and subsystems with their phaser weaponry. Originally that also included torps and pulses if they required multiple fires too fast and if they were very big
# and their spawn location was inside the parent ship model, but that got fixed for most cases. However, it is known it may sometimes still happen for torpedoes, and to a lesser degree, disruptors. Obviously if using aesthethic turrets
# that will not happen.
#    -- If facing issues with a functional turret accidentally hitting a subsystem, adjust turret and parent hardpoints so the weapon area is lesser than the amplitude needed to hit the parent ship (if it's a turret-side beam) or so 
#       the turret torpedo launcher is not inside the parent ship (if it's a torpedo one). 
#    --- IMPORTANT NOTE: If you need to use a functional phaser turret whose phasers may be/end up inside the parent ship's shields, or suffer similar hit issues with own-turrets torps and pulses, make sure either:
#    ---- The "ShieldOption" is set to 1.
#    ---- The ship has shields at 0 or less than 10%.
#    ---- Removing the main ship from the Proximitymanager **does the trick for turret original beams, which are the only issue**... but for every ship and weapon, IT MAKES THE SHIP A GHOST WITH BITE! If your ship uses a tech that works
#         like that, then that's another option. However, since for this tech we only want to remove collision from our turret weapons to our parent shields, this tech will not do that for the parent ship.
#    ---- Phaser turrets can be simulated in two ways:
#    ----- Option A: Just place a normal aesthethic turret that never fires above a phaser or phaser group. This option is preferable if there is only 1 phaser per turret and model/scalability issues do not make the following option
#          feasible.
#    ----- Option B: Create auxiliar parent ship hardpoint properties, identical to the turret ship phaser to imitate if that phaser worked, but with their name ending on a " T" (space included, f.ex. if weapon was "Quantom 10", then it
#          would be called "Quantom10 T") but with a max charge identical but on the negatives and a recharge rate greater than twice its max charge, and the firing arcs and direction of the parent , non-T hardpoint. Then the script 
#          will make sure that upon firing a "non-T" parent phaser bank, the fire and charge of those associated "T" hardpoint properties becomes the opposite value, and when a "non- T" stops firing, all the associated T siblings' max
#          charge will be sent to the negatives. Additionally, these auxiliar hardpoint properties will attempt to move to fit the turret sibling one.
#          -- Remember that the functional turret hardpoint positions and the ones with this function may not totally match (f.ex. a phaser at 0.5 forward on the turret end may actually end on the middle because the game had adjusted 
#             the hardpoint position to somehing valid according to the turret model).
#          -- If this is done, you cannot use the same exact hardpoint for phaser turrets (since the common phaser name could cause a conflict which on the other case would not be).
#          -- If this is done, it is also extremely recommended to set those " T" hardpoints as non-targetable, since some visible damage shenanigans can all of a sudden decide to destroy the systems for being separated.
#          -- Additionally, the option of "SimulatedPhaser" needs to be set to 1, that is because this faithful option is more expensive and it's better to reduce its use if the turrets do not need it.
# 2. Weapon intensity for turret-side phasers is not currently being totally modulated to the user - it uses the main weapon control subsystem for that, not advanced power control.
#    -- However, naturally, phasers using the "SimulatedPhaser" will work with advanced power control because those are actually the parent ship beams.
# 3. Torpedo change-type and spread-type support is non-existant at the moment
#    -- The reason for this is because, for some unexplainable reason, trying to change the ammo for a torpedo will work fine, but then when a turret torpedo of the new type collides or despawns, it causes a virtual call function error.
# 4. For some unknown reason, when a ship gets out of warp, if the turret "WarpPosition" is too, too far, turrets might become invisible - something similar happens sometimes with GC warp stretchiness - this does not affect the turret functionality at all, it can still fire and do actions.
# 5. Turrets support AutoTargeting and MultiTargeting fine, but for some cases it may be a tiny bit wonky (including very rarely having a turret aiming at a target for a millisecond, to later on aim and fire at another). 
#    ***Behaviour may turn out even weirder if multiple parent ship weapons are assigned to the same turret (with each one aiming at a different target)***
# 6. For functional turrets:
# -- Turret fire range may not totally overlap the parent ship beam range that they are covering, specially when aiming totally upwards. They cover a slighly smaller area inside the parent coverage area.
# -- Turret fire may be very slightly delayed.
# 7. Setup load/unload times for ships with turrets can be noticeably longer. This is because naturally, every small turret is technically a ship, so a ship with 20 turrets would need to load an extra 20 ships. Please be patient. Also the simpler the turret hardpoint and the turret model, the least impact.

"""
"""

Sample Setup:

Foundation.ShipDef.VasKholhr.dTechs = { 'Turret': {
        "Setup":        {
                "Body":                 "VasKholhr_Body", # If this field is present, it will change the main part model to this one upon activating weaponry.
                #"NormalModel":          shipFile,
                #"WarpModel":          "VasKholhr_WingUp",
                #"AttackModel":          "VasKholhr_WingDown",
                "ShieldOption": 0,
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
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.03],
                "WarpPosition":       [0, 0, 0.02],
                "WarpDuration":       150.0,
                "SyncTorpType": 1,
                "SimulatedPhaser": 1,
                "SimulatedTractor": 1,
                "SetScale": 1.0,
                }
        ],
        
        "Starboard Wing":     ["VasKholhr_Starboardwing", {
                "Position":             [0, 0, 0],
                "AttackDuration":         200.0, # Value is 1/100 of a second
                "AttackPosition":         [0, 0, 0.03],
                "WarpPosition":       [0, 0, 0.02],
                "WarpDuration":       150.0,
                "SyncTorpType": 1,
                "SimulatedPhaser": 1,
                "SimulatedTractor": 1,
                "SetScale": 1.0,
                }
        ],
}}



"""
#################################################################################################################
from bcdebug import debug
import traceback

import App
import FoundationTech
import loadspacehelper
import math
import MissionLib



#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.9996",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################



REMOVE_POINTER_FROM_SET = 190
NO_COLLISION_MESSAGE = 192
REPLACE_MODEL_MSG = 208
SET_TARGETABLE_MSG = 209

globalTurretTimer = None
bOverflow = 0
sinTurretbOverflow = 0
defaultSlice = 0.01 # In seconds

# A Reverse dictionary class for easier management
# 0.992 version saw optimizing this to only have the ship IDs
class SingleTurret:
    def __init__(self):
        global sinTurretbOverflow
        self.bOverflow = 1
        sinTurretbOverflow = 1
        self.pShips = {}

    def addShip(self, pShipID, pTurretID):
        self.pShips[pTurretID] = pShipID

    def removeShip(self, pTurretID):
        if self.pShips.has_key(pTurretID):
            del self.pShips[pTurretID]

    def removeTurretsforShip(self, pShipID):
        auxShipKeys = self.pShips.keys()
        for turretElement in auxShipKeys:
            if self.pShips[turretElement] == pShipID:
                del self.pShips[turretElement]

    def getDict(self):
        return self.pShips

    def getDictEntry(self, pTurretID):
        if self.pShips.has_key(pTurretID):
            return self.pShips[pTurretID]
        else:
            return None            
        
    def getShipForTurret(self, pTurretID): #oInvertedTurretList.getShipForTurret(pTurret)
        if self.getDictEntry(pTurretID) != None:
            return self.pShips[pTurretID]
        else:
            return None

    def isTurretHere(self, pTurret):
        if hasattr(pTurret, "GetObjID") and self.getDictEntry(pTurret.GetObjID()) != None:
            return 1
        else:
            return 0

oInvertedTurretList = SingleTurret()

# This class does control the attach and detach of the Models
class Turrets(FoundationTech.TechDef):
        def __init__(self, name):
                debug(__name__ + ", Initiated Turrets counter")
                FoundationTech.TechDef.__init__(self, name)

                self.pEventHandler = App.TGPythonInstanceWrapper()
                self.pEventHandler.SetPyWrapper(self)

                self.pTimer = None
                self.bBattleTurretListener = {}
                self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once
                self.bAddedAlertListener = {}

        def countdown(self):
                debug(__name__ + ", Initiated Turret counter countdown")
                if not self.pTimer:
                        global bOverflow
                        bOverflow = 1
                        global defaultSlice
                        self.pTimer = App.PythonMethodProcess()
                        self.pTimer.SetInstance(self)
                        self.pTimer.SetFunction("aimingAtTarget")
                        self.pTimer.SetDelay(defaultSlice)
                        self.pTimer.SetPriority(App.TimeSliceProcess.LOW)        
                        self.pTimer.SetDelayUsesGameTime(1)

        def checkWell(self, fTime, myShipID, pInstanceO):
                pShip = GetShipFromID(myShipID)
                if pShip and not pShip.IsDead():
                        pInstance = findShipInstance(pShip)
                        if pInstance != None:
                                pInstanceShipID = getShipIDfromInstance(pInstance)
                                if pInstanceShipID != myShipID: # Weird but can happen for the player - trying to make this as player-agnostic as possible, in case this ever gets implemented for multiplayer
                                        self.trueDetach(pInstanceO, myShipID)
                                pInstanceDict = pInstance.__dict__
                                if pInstanceDict.has_key(self.name):
                                        atta = self.ArePartsAttached(pShip, pInstance)
                                        if atta:
                                                PartsForWeaponTurretState(pInstance, pShip, myShipID)
                                else:
                                        try:
                                                print __name__ , " checkWell: cancelling, the ship", pShip.GetName(), " has no '", self.name, "'"
                                                self.trueDetach(pInstance, myShipID)
                                                self.extraCleanup(myShipID)
                                        except:
                                                print __name__ , " error when calling checkWell:"
                                                traceback.print_exc()
                        else:
                                try:
                                        self.trueDetach(pInstanceO, myShipID)
                                        self.extraCleanup(myShipID)
                                except:
                                        print __name__ , "error when calling checkWell:"
                                        traceback.print_exc()
                else:
                        try:
                                self.trueDetach(pInstanceO, myShipID)
                                self.extraCleanup(myShipID)
                        except:
                                print __name__ , "error when calling checkWell:"
                                traceback.print_exc()

        def extraCleanup(self, iShipID):
                try:
                    # Extra memory cleanup
                    try:
                         App.g_kLODModelManager.Purge()
                    except:
                         traceback.print_exc()

                    try:
                         App.g_kModelManager.Purge()
                    except:
                         traceback.print_exc()
                except:
                    traceback.print_exc()

        def aimingAtTarget(self, fTime):
                debug(__name__ + ", aimingAtTarget")
                #print "self.bAddedAlertListener: ", self.bAddedAlertListener
                if len(self.bAddedAlertListener) == 0:
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpEnteredSet")
                        #App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpEnteredSet")

                auxBattleTurretListenerKeys = self.bBattleTurretListener.keys()
                for itemList in auxBattleTurretListenerKeys:
                        if itemList != None and self.bBattleTurretListener[itemList] != None:
                                self.checkWell(fTime, itemList, self.bBattleTurretListener[itemList][0])


        def SetBattleTurretListenerTo(self, pShip, value, otherValue = -1):
                debug(__name__ + ", SetBattleTurretListenerTo")
                if not pShip:
                        return 0
                itemList = pShip.GetObjID()
                if itemList != None and self.bBattleTurretListener.has_key(itemList):
                        self.bBattleTurretListener[itemList][otherValue] = value
                return 0

        def GetBattleTurretListenerEntry(self, iShipID):
               if iShipID != None and self.bBattleTurretListener.has_key(iShipID) and self.bBattleTurretListener[iShipID] != None:
                       return self.bBattleTurretListener[iShipID]
               else:
                       return None

        def Attach(self, pInstance):
                pInstance.lTechs.append(self)

        # called by FoundationTech when a ship is created
        # Prepares the ship for moving its sub parts
        def AttachShip(self, pShip, pInstance):
                debug(__name__ + ", AttachShip")
                #print "Ship %s with Turrets support added" % pShip.GetName()

                sNamePrefix = str(pShip.GetObjID()) + "_"
                pInstance.__dict__["TurretSystemOptionsList"] = [] # save options to this list, so we can access them later
                #self.bAddedWarpListener = {} # this variable will make sure we add our event handlers only once
                #self.bAddedAlertListener = {}

                ModelList = pInstance.__dict__[self.name]
                AlertListener = 0
                
                if not ModelList.has_key("Setup"):
                        print __name__, ": Error: Cannot find Setup for Moving Parts"
                        return
                
                # Iterate over every item

                for sNameSuffix in ModelList.keys():
                        # if this is the setup, do the things for the whole ship 
                        #we have to remember, like alert state
                        if sNameSuffix == "Setup":
                                dOptions = ModelList[sNameSuffix]

                                dOptions1 = {}
                                # we start with green alert
                                if not dOptions1.has_key("AlertLevel"):
                                        dOptions1["AlertLevel"] = 0
                                if not dOptions1.has_key("GenMoveID"):
                                        dOptions1["GenMoveID"] = 0

                                for key in dOptions.keys():
                                    dOptions1[key] = dOptions[key]
                                pInstance.TurretSystemOptionsList.append("Setup", dOptions1)

                                continue # nothing more to do here
                        #
                        # the following stuff is only for the objects that move
                        
                        if len(ModelList[sNameSuffix]) > 1:
                                dOptions = ModelList[sNameSuffix][1]
                        sFile = ModelList[sNameSuffix][0]
                        loadspacehelper.PreloadShip(sFile, 1)

                        dofShip = [None, None]
                        dofShip[0] = sNameSuffix
                        
                        # save the shipfile for later use, this would be on "item[1]"
                        dOptions2 = {}
                        dOptions2["sShipFile"] = sFile
                        
                        # set current position values
                        if not dOptions2.has_key("currentPosition"):
                                dOptions2["currentPosition"] = [0, 0, 0]
                        if not dOptions2.has_key("curMovID"):
                                dOptions2["curMovID"] = 0

                        if not dOptions.has_key("Position"):
                                dOptions["Position"] = [0, 0, 0]
                        dOptions2["currentPosition"] = dOptions["Position"]
                        for key in dOptions.keys():
                            dOptions2[key] = dOptions[key]

                        dofShip[1] = dOptions2
                        pInstance.TurretSystemOptionsList.append(dofShip)

                        # event listener

                        pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
                        pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                        pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                        pShip.RemoveHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")

                        pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp") # It seems something about ET_START_WARP or ET_START_WARP_NOTIFY causes issues TO-DO CHECK
                        pShip.AddPythonFuncHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                        # ET_EXITED_WARP handler doesn't seem to work, so use ET_EXITED_SET instead
                        pShip.AddPythonFuncHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                        pShip.AddPythonFuncHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")

                        self.bAddedWarpListener[pShip.GetObjID()] = 1

                        # Extra thing
                        App.g_kEventManager.RemoveBroadcastHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpEnteredSet")
                        App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_TORPEDO_ENTERED_SET, self.pEventHandler, "TorpEnteredSet")

                        if not self.bAddedAlertListener.has_key(pShip.GetObjID()) and dOptions.has_key("AttackPosition"):

                                pShip.AddPythonFuncHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertStateChanged")
                                # Alert change handler doesn't work for AI ships, so use subsystem changed instead
                                pShip.AddPythonFuncHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")

                                pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

                                #Weapon Control
                                pShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                                pShip.AddPythonFuncHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")

                                # There's not such a good tolerance for torpedoes compared with phasers, if a problem arises due to this, it may be a potential TO-DO
                                pShip.AddPythonFuncHandlerForInstance(App.ET_TORPEDO_FIRED, __name__ + ".WeaponFiredStopAction")

                                self.bAddedAlertListener[pShip.GetObjID()] = 1
                                AlertListener = 1

                        self.bBattleTurretListener[pShip.GetObjID()] = [pInstance, 0, -1] # That means the ship pShip with shields inactive at 0 is not active in battle (-1)

                global bOverflow
                if bOverflow == 0:
                    bOverflow = 1
                    self.countdown()

                # Make sure the Ship is correctly set
                # because we don't get the first ET_SUBSYSTEM_STATE_CHANGED event for Ai ships
                if AlertListener:
                        PartsForWeaponState(pShip)

        def DetachShip(self, iShipID, pInstance):
                debug(__name__ + ", DetachShip")

                pShip = App.ShipClass_GetObjectByID(None, iShipID)

                if pShip:
                        # remove the listeners
                        try:
                            pShip.RemoveHandlerForInstance(App.ET_START_WARP, __name__ + ".StartingWarp")
                            pShip.RemoveHandlerForInstance(App.ET_START_WARP_NOTIFY, __name__ + ".StartingWarp")
                            pShip.RemoveHandlerForInstance(App.ET_EXITED_SET, __name__ + ".ExitSet")
                            pShip.RemoveHandlerForInstance(App.ET_ENTERED_SET, __name__ + ".EnterSet")
                        
                            pShip.RemoveHandlerForInstance(App.ET_SUBSYSTEM_STATE_CHANGED, __name__ + ".SubsystemStateChanged")
                            pShip.RemoveHandlerForInstance(App.ET_SET_ALERT_LEVEL, __name__ + ".AlertStateChanged")

                            pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
                            pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
                            pShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
                            pShip.RemoveHandlerForInstance(App.ET_PHASER_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                            pShip.RemoveHandlerForInstance(App.ET_TRACTOR_BEAM_STOPPED_FIRING, __name__ + ".WeaponFiredStop")
                            pShip.RemoveHandlerForInstance(App.ET_TORPEDO_FIRED, __name__ + ".WeaponFiredStopAction")
                        except:
                            traceback.print_exc()

                try:
                        #print "calling DetachShip --> Detach Parts"
                        self.DetachParts(pShip, pInstance, 1, iShipID)
                except:
                        traceback.print_exc()
   
                if hasattr(pInstance, "TurretSystemOptionsList"):
                        for item in pInstance.TurretSystemOptionsList:
                            if item[0] == "Setup":
                                if item[1].has_key("AlertLevel"):
                                    del item[1]["AlertLevel"]
                                if item[1].has_key("GenMoveID"):
                                    del item[1]["GenMoveID"]
                            else:
                                if item[1].has_key("currentPosition"):
                                    del item[1]["currentPosition"]
                                if item[1].has_key("curMovID"):
                                    del item[1]["curMovID"]
                                if item[1].has_key("TARGET"):
                                    del item[1]["TARGET"]

                        del pInstance.TurretSystemOptionsList

        # Called by FoundationTech when a Ship is removed from set (eg destruction)
        def Detach(self, pInstance):
                debug(__name__ + ", Detach")
                #print "calling Detach ---> trueDetach"
                self.trueDetach(pInstance)

        def trueDetach(self, pInstance, iShipID = None):
                debug(__name__ + ", trueDetach")

                if iShipID == None:
                        auxShipID = getShipIDfromInstance(pInstance)
                        if auxShipID != None:
                                iShipID = auxShipID
                if iShipID != None:
                        if self.bBattleTurretListener.has_key(iShipID):
                                del self.bBattleTurretListener[iShipID]
                        else:
                                #print "I did not find the key so I'm done with that one"
                                return
                else:
                        #print __name__ , ", trueDetach: Error: the pInstance has no pShipID attribute?"
                        return
                try:
                    if self.bAddedWarpListener.has_key(iShipID):
                        del self.bAddedWarpListener[iShipID]
                except:
                    traceback.print_exc()

                try:
                    if self.bAddedAlertListener.has_key(iShipID):
                        del self.bAddedAlertListener[iShipID]
                except:
                    traceback.print_exc()

                try:
                    #print "calling trueDetach ---> DetachShip"
                    self.DetachShip(iShipID, pInstance)
                except:
                    print __name__, ": Error while calling trueDetach:"
                    traceback.print_exc()

                oInvertedTurretList.removeTurretsforShip(iShipID)

                try:
                    if pInstance != None:
                        pInstance.lTechs.remove(self)
                except:
                    traceback.print_exc()

        # Attaches the SubParts to the Body Model
        def AttachParts(self, pShip, pInstance):
                debug(__name__ + ", AttachParts")
                pSet = pShip.GetContainingSet()
                if not pSet:
                    return 0

                if not pInstance.__dict__.has_key("TurretList"):
                    pInstance.__dict__["TurretList"] = []
                ModelList = pInstance.__dict__[self.name]
                sNamePrefix = str(pShip.GetObjID()) + "_"
                TurretList = pInstance.TurretList

                # Because for some reason the turret spawned is sometimes considered a friendly or an enemy so the other side targets them or Saffi gets angry at you
                pMission        = MissionLib.GetMission()

                pFriendlies     = None
                pEnemies        = None
                pNeutrals       = None
                pTractors       = None
                if pMission:
                        pFriendlies     = pMission.GetFriendlyGroup() 
                        pEnemies        = pMission.GetEnemyGroup() 
                        pNeutrals       = pMission.GetNeutralGroup()
                        pTractors       = pMission.GetTractorGroup()

                # To avoid AI and multiple processes from constantly trying to avoid the turrets
                pProxManager = pSet.GetProximityManager()

                pShields = pShip.GetShields()
                if pInstance.__dict__.has_key(self.name) and pInstance.__dict__[self.name].has_key("Setup") and  pInstance.__dict__[self.name]["Setup"].has_key("ShieldOption") and pInstance.__dict__[self.name]["Setup"]["ShieldOption"] == 1 and pShields.IsOn(): # If shields are active with ShieldOption = 1, drop shields
                    pShields.TurnOff()

                pShields = pShip.GetShields()
                if pInstance.__dict__.has_key(self.name) and pInstance.__dict__[self.name].has_key("Setup") and  pInstance.__dict__[self.name]["Setup"].has_key("ShieldOption") and pInstance.__dict__[self.name]["Setup"]["ShieldOption"] == 1 and pShields.IsOn(): # If shields are active with ShieldOption = 1, drop shields
                    pShields.TurnOff()

                #pProxManager.RemoveObject(pShip) # This, funnily enough, allows our weapons to bypass our shields... as well as pretty much everyone not being able to hit us

                pCloak = pShip.GetCloakingSubsystem()
                shipIsCloaking = 0
                shipIsDecloaking = 0
                if pCloak:
                        shipIsCloaking = pCloak.IsCloaking() or pCloak.IsCloaked() 
                        shipIsDecloaking = pCloak.IsDecloaking() or not pCloak.IsCloaked()
                # iteeeerate over every Turret, this version is O(N) and more efficient, but if you find any issues, I've also left the previous O(N^2) version commented just in case
                for lList in pInstance.TurretSystemOptionsList:
                        if lList != None and len(lList) > 0 and lList[0] != None and lList[0] != "Setup":
                                sFile = None
                                sShipName = None
                                pSubShip = None
                                found = 0
                                if hasattr(lList[0], "GetObjID"):
                                        # It means it is a ship
                                        piNacelle = App.ShipClass_GetObjectByID(None, lList[0].GetObjID())
                                        if piNacelle:
                                                pSubShip = piNacelle
                                                found = 1
                                else: # it is a string
                                        sNameSuffix = lList[0]
                                        sShipName = sNamePrefix + sNameSuffix
                                        pSubShip = MissionLib.GetShip(sShipName, None, 1)
                                        if len(lList) > 1 and lList[1].has_key("sShipFile"):
                                                sFile = lList[1]["sShipFile"]
                                        if not pSubShip and sFile != None:
                                                pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "")

                                if pSubShip == None:
                                        print __name__, ": Error - missing SubShip Turret during AttachParts ", sShipName, " of sFile ", sFile
                                        continue
                                else:
                                        lList[0] = pSubShip
                                        iSaveDone = 1
                                        dOptions = lList[1]

                                        TurretList.append(pSubShip)
                        
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
                                        pSubShip.SetScannable(0)
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

                                        # set current positions
                                        pSubShip.SetTranslateXYZ(dOptions["currentPosition"][0],dOptions["currentPosition"][1],dOptions["currentPosition"][2])
                                        pSubShip.UpdateNodeOnly()

                                        if pCloak:
                                                pSubShipID = pSubShip.GetObjID()
                                                if shipIsCloaking:
                                                        CloakShip(pSubShipID, -1)
                                                elif shipIsDecloaking:
                                                        CloakShip(pSubShipID, 1)

                                        # Because for some reason the turret spawned is sometimes considered a friendly or an enemy so the other side targets them or Saffi gets angry at you
                                        if pMission:
                                                pFriendlies.RemoveName(pSubShip.GetName())
                                                pEnemies.RemoveName(pSubShip.GetName())
                                                pNeutrals.RemoveName(pSubShip.GetName())
                                                pTractors.RemoveName(pSubShip.GetName())
                                                pTractors.AddName(pSubShip.GetName())

                                        if pProxManager:
                                                pProxManager.RemoveObject(pSubShip) # This removes the Subship from the proximity manager without causing a crash when a ship dies or changes set

                                        # For some reason, App.ET_TORPEDO_FIRED only worked for torpedoes fired from torp tubes, and only as a broadcast - so we do it another way...
                                        oInvertedTurretList.addShip(pShip.GetObjID(), pSubShip.GetObjID())

                                        pSubShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".TorpedoTurretFiredTest")
                                        pSubShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".TorpedoTurretFiredTest") 

                                        pSubShip.UpdateNodeOnly()
                                        pShip.AttachObject(pSubShip)

                """
                # iteeeerate over every Turret
                for sNameSuffix in ModelList.keys(): # I know this O(N^2) is inefficient and on an ideal world we could just use pInstance.TurretSystemOptionsList and then make this O(N)... but with all the techs around...
                        if sNameSuffix == "Setup":
                                continue

                        sFile = ModelList[sNameSuffix][0]
                        sShipName = sNamePrefix + sNameSuffix
                        
                        # check if the ship does exist first, before create it
                        pSubShip = MissionLib.GetShip(sShipName, None, 1)


                        # save the options list
                        iSaveDone = 0
                        dOptions = None
                        # this is here to check if we already have the entry
                        for lList in pInstance.TurretSystemOptionsList:
                                if lList[0] != "Setup":
                                        proceed = 0
                                        if lList[0] == sNameSuffix:
                                                proceed = 1
                                        else:
                                                if (lList[0] != None):
                                                        if hasattr(lList[0], "GetObjID") and (lList[0].GetName() == sShipName):
                                                                proceed = 1
                                                                piNacelle = App.ShipClass_GetObjectByID(None, lList[0].GetObjID())
                                                                if piNacelle:
                                                                        if not pSubShip:
                                                                                pSubShip = piNacelle

                                        if proceed > 0 and lList[1]["sShipFile"] == sFile:
                                                if not pSubShip:
                                                        pSubShip = loadspacehelper.CreateShip(sFile, pSet, sShipName, "")
                                                lList[0] = pSubShip
                                                iSaveDone = 1
                                                dOptions = lList[1]
                                                break
                        
                        if not iSaveDone:
                            if len(ModelList[sNameSuffix]) > 1:
                                dOptionsSingle = ModelList[sNameSuffix][1]

                            loadspacehelper.PreloadShip(sFile, 1)
                        
                            # save the shipfile for later use, this would be on "item[1]"
                            dOptions2 = {}
                            dOptions2["sShipFile"] = sFile
                        
                            # set current position values
                            if not dOptions2.has_key("currentPosition"):
                                dOptions2["currentPosition"] = [0, 0, 0]
                            if not dOptions2.has_key("curMovID"):
                                dOptions2["curMovID"] = 0
                            if not dOptionsSingle.has_key("Position"):
                                dOptionsSingle["Position"] = [0, 0, 0]
                            dOptions2["currentPosition"] = dOptionsSingle["Position"]
                            for key in dOptionsSingle.keys():
                                dOptions2[key] = dOptionsSingle[key]

                            pInstance.TurretSystemOptionsList.append([pSubShip, dOptions2])
                            dOptions = dOptions2

                        if pSubShip == None:
                                print __name__, ": Error - missing SubShip during AttachParts "
                                continue

                        TurretList.append(pSubShip)
                        
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
                        pSubShip.SetScannable(0)
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

                        # set current positions
                        pSubShip.SetTranslateXYZ(dOptions["currentPosition"][0],dOptions["currentPosition"][1],dOptions["currentPosition"][2])
                        pSubShip.UpdateNodeOnly()


                        if pCloak:
                                pSubShipID = pSubShip.GetObjID()
                                if shipIsCloaking:
                                    CloakShip(pSubShipID, -1)
                                elif shipIsDecloaking:
                                    CloakShip(pSubShipID, 1)

                        # Because for some reason the turret spawned is sometimes considered a friendly or an enemy so the other side targets them or Saffi gets angry at you
                        if pMission:
                            pFriendlies.RemoveName(pSubShip.GetName())
                            pEnemies.RemoveName(pSubShip.GetName())
                            pNeutrals.RemoveName(pSubShip.GetName())
                            pTractors.RemoveName(pSubShip.GetName())
                            pTractors.AddName(pSubShip.GetName())


                        ##### EXPERIMENTAL AREA
                        " " "
                        # CANCELLED TO-DO (See Limitation 3), no matter where we add it, changing the torpedo type is successfull in both SetTorpedoScriipt and SetAmmoType ways, 
                        # but removal of the new torpedo fired will cause a virtual function call crash when the new torpedo despawns or dies
                        parentTorpSys = pShip.GetTorpedoSystem()
                        turTrpSys = pSubShip.GetTorpedoSystem()
                        if parentTorpSys:
                            if turTrpSys and pInstance.__dict__[self.name][sNameSuffix][1].has_key("SyncTorpType") and pInstance.__dict__[self.name][sNameSuffix][1]["SyncTorpType"] > 0:
                                turTrpSys.SetAmmoType(1, 0.1) # First parameter is the iType, first, second, third, fourth torpedo. Second parameter is the time to reload, in minutes
                                #pParentFiredSystemProperty = App.TorpedoSystemProperty_Cast(parentTorpSys.GetProperty())
                                #if pInstance.__dict__[self.name][sNameSuffix][1]["SyncTorpType"] == 1: # We sync types
                                #    #print "Ok so torp slot sync"
                                #    ammoNum = parentTorpSys.GetCurrentAmmoTypeNumber() # TO-DO if this works, move them above to avoid getting too much loop
                                #    pTorpedoType = parentTorpSys.GetAmmoType(ammoNum)
                                #    pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()

                                #    curTurammoNum = turTrpSys.GetCurrentAmmoTypeNumber()
                                #    curTurammoType = turTrpSys.GetAmmoType(curTurammoNum)
                                #    curTurammoTypeScript = curTurammoType.GetTorpedoScript()
                                #    #print curTurammoTypeScript ," vs ", pTorpedoTypeScript
                                #    if curTurammoTypeScript != pTorpedoTypeScript:
                                #        #print "Updating to another torp type, please wait..."
                                #        curTurammoType.SetTorpedoScript(pTorpedoTypeScript)
                        " " "
                        ##### END EXPERIMENTAL AREA




                        if pProxManager:
                            pProxManager.RemoveObject(pSubShip) # This removes the Subship from the proximity manager without causing a crash when a ship dies or changes set

                        # For some reason, App.ET_TORPEDO_FIRED only worked for torpedoes fired from torp tubes, and only as a broadcast - so we do it another way...
                        oInvertedTurretList.addShip(pShip.GetObjID(), pSubShip.GetObjID())
                        pSubShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".TorpedoTurretFiredTest")
                        pSubShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".TorpedoTurretFiredTest") 

                        pSubShip.UpdateNodeOnly()
                        pShip.AttachObject(pSubShip)
                """

        # check if parts are attached
        def ArePartsAttached(self, pShip, pInstance):
                debug(__name__ + ", ArePartsAttached")
                if hasattr(pInstance, "TurretList") and pInstance.TurretList != None and len(pInstance.TurretList) > 0:
                        return 1
                return 0

        # Detaches the parts
        def DetachParts(self, pShip, pInstance, fromSet=0, pShipID = None):
                debug(__name__ + ", DetachParts")
                try:
                    if pShipID == None:
                        pShipID = pShip.GetObjID()
                    iShipID = getShipIDfromInstance(pInstance)
                    pShip = App.ShipClass_GetObjectByID(None, pShipID)

                    if hasattr(pInstance, "TurretList"):
                        for pSubShip in pInstance.TurretList:
                            if hasattr(pSubShip, "__class__") and pSubShip.__class__ == App.ShipClass:
                                pSubShip = App.ShipClass_GetObjectByID(None, pSubShip.GetObjID())
                                if pSubShip:
                                    pSubShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".TorpedoTurretFiredTest") # Addition that makes torps and pulses at least work
                                    oInvertedTurretList.removeShip(pSubShip.GetObjID())
                                    if pShip:
                                        try:
                                            pShip.DetachObject(pSubShip)
                                        except:
                                            traceback.print_exc()

                                    pSet = pSubShip.GetContainingSet()
                                    DeleteObjectFromSet(pSet, pSubShip.GetName())
                                    if fromSet == 1:
                                        pSubShip.SetDeleteMe(1)
                                    pSubShip.UpdateNodeOnly()
                        del pInstance.TurretList

                    if pShip:
                        pShields = pShip.GetShields()
                        if pInstance and hasattr(pInstance, "__dict__"):
                            pInsDict = pInstance.__dict__
                            if pInsDict.has_key(self.name) and pInsDict[self.name].has_key("Setup") and pInsDict[self.name]["Setup"].has_key("ShieldOption") and pInsDict[self.name]["Setup"]["ShieldOption"] == 1 and pShields and pShip.GetAlertLevel() > 0: # If yellow alert or more, shields up
                                pShields.TurnOn()

                    if pShipID != None:
                        oInvertedTurretList.removeTurretsforShip(pShipID)
                except:
                    traceback.print_exc()

        def TorpEnteredSet(self, pEvent):
                debug(__name__ + ", TorpEnteredSet")
                pTorp=App.Torpedo_Cast(pEvent.GetDestination())
                if (pTorp==None):
                        return
                global oInvertedTurretList
                pShipID = oInvertedTurretList.getShipForTurret(pTorp.GetParentID())
                if pShipID != None:
                        pShip = App.ShipClass_GetObjectByID(None, pShipID)
                        if pShip: 
                                pTorp.SetParent(pShipID)
                                pTorp.UpdateNodeOnly()


oTurrets = Turrets("Turret")

# The class does the moving of the parts
# with every move the part continues to move
class MovingEvent:
        # prepare fore move...
        def __init__(self, pShip, item, fDuration, lStartingTranslation, lStoppingTranslation, dHardpoints):
                debug(__name__ + ", __init__")
                
                pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
                if not pShip:
                        return

                if not item or not len(item) > 1:
                        return

                item0 = None
                if hasattr(item[0], "GetObjID"):
                        item0 = App.ShipClass_GetObjectByID(None, item[0].GetObjID())

                if not item0:
                        return

                self.iNacelleID = item[0].GetObjID()
                self.iThisMovID = item[1]["curMovID"]
                self.dTurretSystemOptionsList = item[1]
                self.pShip = pShip
                        
                fDurationMul = 0.95 # make us a little bit faster to avoid bad timing
                
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
                                print __name__, ": Error: Unable to find Hardpoint %s" % sHP
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


                if self.dTurretSystemOptionsList.has_key("SetScale") and self.dTurretSystemOptionsList["SetScale"] != 0.0:
                    item[0].SetScale(self.dTurretSystemOptionsList["SetScale"])
                else:
                    item[0].SetScale(0.5)
                
        # adjust planned move
        def __call__(self, pShip, pTarget=None):
                # if the move ID doesn't match then this move is outdated
                debug(__name__ + ", __call__")

                # these make sure the game does not crash when trying to access a deleted element
                pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
                if not pShip:
                        return 0

                if not hasattr(self, "iNacelleID"):
                        return 0
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        return 0

                if (not self.dTurretSystemOptionsList.has_key("curMovID")) or self.iThisMovID != self.dTurretSystemOptionsList["curMovID"]: # Move no longer active
                        return 1

                # set new Translation values
                self.iCurTransX = self.iCurTransX + self.iTransStepX
                self.iCurTransY = self.iCurTransY + self.iTransStepY
                self.iCurTransZ = self.iCurTransZ + self.iTransStepZ
                # set Translation
                # pNacelle.SetTranslateXYZ(self.iCurTransX, self.iCurTransY, self.iCurTransZ)
                
                self.dTurretSystemOptionsList["currentPosition"] = [self.iCurTransX, self.iCurTransY, self.iCurTransZ]
                
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
                debug(__name__ + ", isCloaking")
                if self.iThisMovID != self.dTurretSystemOptionsList["curMovID"]: # "Moving Error: Move no longer active"
                        return 1
                
                # this makes sure the game does not crash when trying to access a deleted element
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        return 0

                pCloak = pNacelle.GetCloakingSubsystem()
                if pCloak:
                        pCloak.StartCloaking()

        def isDecloaking(self, pShip):
                # if the move ID doesn't match then this move is outdated
                debug(__name__ + ", isDecloaking")
                if self.iThisMovID != self.dTurretSystemOptionsList["curMovID"]: # "Moving Error: Move no longer active"
                        return 1
                
                # this makes sure the game does not crash when trying to access a deleted element
                pNacelle = App.ShipClass_GetObjectByID(None, self.iNacelleID)
                if not pNacelle:
                        return 0

                pCloak = pNacelle.GetCloakingSubsystem()
                if pCloak:
                        pCloak.InstantDecloak()

# move!
def partTranslate(item, iShipID, lStoppingTranslation, warpDirty, usualMove = 0):

        #pShip = GetShipFromID(iShipID)
        #if not pShip:
        #        print __name__, ": Transloc Error: Lost MAIN part"
        #        return 0

        iNacelleID = None
        if item[0] != None and hasattr(item[0], "GetObjID"):
                iNacelleID = item[0].GetObjID()

        if iNacelleID == None or iNacelleID == App.NULL_ID:
                #print __name__, ": Transloc Error: Lost Nacelle ID"
                return 0

        pNacelle = GetShipFromID(iNacelleID)
        if not pNacelle:
               #print __name__, ": Transloc Error: Lost Nacelle ship"
               return 0

        dTurretSystemOptionsList = item[1]

        pNacelle.SetTranslateXYZ(lStoppingTranslation[0], lStoppingTranslation[1], lStoppingTranslation[2])

        if usualMove == 0: # Not a usual move, thus we need to update the current position on the dictionary
                dTurretSystemOptionsList["currentPosition"] = [lStoppingTranslation[0], lStoppingTranslation[1], lStoppingTranslation[2]]
                
        pNacelle.UpdateNodeOnly()

        if warpDirty:
                model = item[1]["sShipFile"]
                if model:
                        ReplaceModel(pNacelle, model)
                pNacelle.SetHidden(0)
                pNacelle.UpdateNodeOnly()
                checkingReCloak(pNacelle)
        return 0

# aim!
def aim1Item(item, iShipID, pTarget=None, pShip = None): #(item, iShipID, pTarget=None):

        if not pShip:
                pShip = GetShipFromID(iShipID)

        if not pShip:
                print __name__, ": Rotating Error: Lost MAIN part"
                return 0

        iNacelleID = None
        if item[0] != None and hasattr(item[0], "GetObjID"):
                iNacelleID = item[0].GetObjID()

        if iNacelleID == None or iNacelleID == App.NULL_ID:
                #print __name__, ": Rotating Error: Lost Nacelle ID"
                return 0

        pNacelle = GetShipFromID(iNacelleID)
        if not pNacelle:
               #print __name__, ": Rotating Error: Lost Nacelle ship"
               return 0

        dTurretSystemOptionsList = item[1]

        # Reminder because sometimes a ship may accidentally fire on the parent and then the game automatically switches it to enemy
        pMission = MissionLib.GetMission()
        if pMission:
               pFriendlies     = pMission.GetFriendlyGroup() 
               pEnemies        = pMission.GetEnemyGroup() 
               pNeutrals       = pMission.GetNeutralGroup()
               pTractors       = pMission.GetTractorGroup()
               pFriendlies.RemoveName(pNacelle.GetName())
               pEnemies.RemoveName(pNacelle.GetName())
               pNeutrals.RemoveName(pNacelle.GetName())
               pTractors.RemoveName(pNacelle.GetName())
               pTractors.AddName(pNacelle.GetName())
                        
        # set new Rotation values
        if pTarget == None:
                if dTurretSystemOptionsList.has_key("TARGET"):
                        pTarget = dTurretSystemOptionsList["TARGET"]
                        if pTarget:
                                pTarget = GetShipFromID(pTarget.GetObjID())
                        if not pTarget or pTarget.IsDead() or pTarget.IsDying() or pTarget.GetObjID() == iNacelleID:
                                pTarget = pShip.GetTarget()
                else:
                        pTarget = pShip.GetTarget()
        else:
                dTurretSystemOptionsList["TARGET"] = pTarget

        ### If we leave the scale to regular warp and alert then we can comment this
        ###if dTurretSystemOptionsList.has_key("SetScale") and dTurretSystemOptionsList["SetScale"] != 0.0:
        ###    pNacelle.SetScale(dTurretSystemOptionsList["SetScale"])
        ###else:
        ###    pNacelle.SetScale(0.5)

        while pTarget and (pTarget.GetObjID() == iNacelleID): # another safety feature for doofus AutoTargeting scripts
                pTarget = pShip.GetNextTarget()

        if pTarget: 
                        kNacelleLocation = pNacelle.GetWorldLocation()
                        kTargetLocation = pTarget.GetWorldLocation()

                        kNewUpReal = pShip.GetWorldUpTG()

                        kTargetLocation.Subtract(kNacelleLocation)

                        kFwd = kTargetLocation
                        kFwd.Unitize()

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

                            #Now that we got a x b, we want to get (a x b) x a = kVect1 x a, to get the perpendicular we really want
                            vAuxVx, vAuxVy, vAuxVz = MatrixMult(kVect1, kFwd)


                            kVect2 = App.TGPoint3()
                            kVect2.SetXYZ(vAuxVx, vAuxVy, vAuxVz)
                            kVect2.Unitize()

                            pNacelle.AlignToVectors(kFwd, kVect2)

                        if dTurretSystemOptionsList.has_key("SimulatedPhaser") and dTurretSystemOptionsList["SimulatedPhaser"] == 1:
                            turPhsSys = pNacelle.GetPhaserSystem()
                            if turPhsSys:
                                lookandUpdateSiblingTPhasers(turPhsSys, pShip, pNacelle, 2, 1)

                        if dTurretSystemOptionsList.has_key("SimulatedTractor") and dTurretSystemOptionsList["SimulatedTractor"] == 1:
                            turTbpSys = pNacelle.GetTractorBeamSystem()
                            if turTbpSys:
                                lookandUpdateSiblingTPhasers(turTbpSys, pShip, pNacelle, 2, 0)               
                
        pNacelle.UpdateNodeOnly()
        return 0

def MatrixMult(kFwd, kNewUp):
    debug(__name__ + ", MatrixMult")
    vAuxVx = kFwd.y * kNewUp.z - kNewUp.y * kFwd.z
    vAuxVy = kNewUp.x * kFwd.z - kFwd.x * kNewUp.z
    vAuxVz = kFwd.x * kNewUp.y - kNewUp.x * kFwd.y
    return vAuxVx, vAuxVy, vAuxVz


def MatrixDet(matrix):
    debug(__name__ + ", MatrixDet")
    secondRow = {"x": matrix[3], "y": matrix[4], "z": matrix[5]}
    ThirdRow = {"x": matrix[3], "y": matrix[4], "z": matrix[5]}
    vAuxVx, vAuxVy, vAuxVz = MatrixMult(secondRow, ThirdRow)
    return vAuxVx * matrix[0] + vAuxVy * matrix[1] + vAuxVz * matrix[2]

def GetShipFromID(pShipID):
        debug(__name__ + ", GetShipFromID")
        pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
        return pShip

def GetWellShipFromID(pShipID):
        debug(__name__ + ", GetWellShipFromID")
        pShip = GetShipFromID(pShipID)
        if not pShip or pShip.IsDead() or pShip.IsDying():
                return None
        return pShip

def findShipInstance(pShip):
        debug(__name__ + ", findShipInstance")
        pInstance = None
        try:
                if not pShip:
                        return pInstance
                if FoundationTech.dShips.has_key(pShip.GetName()):
                        pInstance = FoundationTech.dShips[pShip.GetName()]
        except:
                pass
        return pInstance

def getShipIDfromInstance(pInstance):
        pShipID = None
        if pInstance != None and hasattr(pInstance, "pShipID"):
                pShipID = pInstance.pShipID
        return pShipID

# calls the MovingEvent class and returns its return value
def MovingAction(pAction, oMovingEvent, pShip):
        debug(__name__ + ", MovingAction")
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if pShip:
            pInstance = findShipInstance(pShip)
            if pInstance:
                return oMovingEvent(pShip)
        return 0


def AlertStateChanged(pObject, pEvent):
        debug(__name__ + ", AlertStateChanged")
        pObject.CallNextHandler(pEvent)
        pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
        if pShip:
                pShields = pShip.GetShields()
                if pShields and pShields.IsOn() and not pShields.IsDisabled():
                    pInstance = findShipInstance(pShip)
                    if pInstance and pInstance.__dict__.has_key(oTurrets.name) and pInstance.__dict__[oTurrets.name].has_key("Setup") and  pInstance.__dict__[oTurrets.name]["Setup"].has_key("ShieldOption") and pInstance.__dict__[oTurrets.name]["Setup"]["ShieldOption"] == 1: # and pShields.IsOn(): # If shields are active with ShieldOption = 1, drop shields
                        if oTurrets.ArePartsAttached(pShip, pInstance):
                            pShields.TurnOff()
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

        pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
        pSubsystem = pEvent.GetSource()
        # if the subsystem that changes its power is a weapon
        if not pSubsystem:
                pObject.CallNextHandler(pEvent)
                return
        if hasattr(pEvent, "GetBool"):
                wpnActiveState = pEvent.GetBool()

                if pSubsystem.IsTypeOf(App.CT_WEAPON_SYSTEM) or pSubsystem.IsTypeOf(App.CT_PHASER_SYSTEM) or pSubsystem.IsTypeOf(App.CT_PULSE_WEAPON_SYSTEM) or pSubsystem.IsTypeOf(App.CT_TORPEDO_SYSTEM): # in theory this should be enough, in practice...
                        # set turrets for this alert state
                        PartsForWeaponState(pShip, wpnActiveState)
                elif pSubsystem.IsTypeOf(App.CT_SHIELD_SUBSYSTEM):
                        pShields = pShip.GetShields()
                        if pShields and pShields.IsOn() and not pShields.IsDisabled():
                            pInstance = findShipInstance(pShip)
                            if pInstance and pInstance.__dict__.has_key(oTurrets.name) and pInstance.__dict__[oTurrets.name].has_key("Setup") and  pInstance.__dict__[oTurrets.name]["Setup"].has_key("ShieldOption") and pInstance.__dict__[oTurrets.name]["Setup"]["ShieldOption"] == 1: # and pShields.IsOn(): # If shields are active with ShieldOption = 1, drop shields
                                if oTurrets.ArePartsAttached(pShip, pInstance):
                                    pShields.TurnOff()
                else:
                        try:
                                pParent = pSubsystem.GetParentSubsystem()
                                if pParent and (pParent.IsTypeOf(App.CT_WEAPON_SYSTEM) or pParent.IsTypeOf(App.CT_PHASER_SYSTEM) or pParent.IsTypeOf(App.CT_PULSE_WEAPON_SYSTEM) or pParent.IsTypeOf(App.CT_TORPEDO_SYSTEM)):
                                        PartsForWeaponState(pShip, wpnActiveState)
                        except:
                                traceback.print_exc()

                pObject.CallNextHandler(pEvent)
                return

def CloakShip(pNacelleID, decloak=0):
    debug(__name__ + ", CloakShip")
    pNacelle = App.ShipClass_GetObjectByID(None, pNacelleID)
    if not pNacelle:
        return 0

    pCloak = pNacelle.GetCloakingSubsystem()
    if pCloak:
        if decloak == 0:
            pCloak.StartCloaking()
        elif decloak == 1:
            pCloak.InstantDecloak()
        elif decloak == -1:
            pCloak.InstantCloak()


def CloakHandler(pObject, pEvent):
        debug(__name__ + ", CloakHandler")
        pInstance = findShipInstance(pObject)

        pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID) # App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

        iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        # iterate over every Turret
        pCloak = pShip.GetCloakingSubsystem()
        if pCloak and hasattr(pInstance, "TurretList"):
            shipIsCloaking = pCloak.IsCloaking()
            shipIsDecloaking = pCloak.IsDecloaking()
            for pSubShip in pInstance.TurretList:
                if hasattr(pSubShip, "__class__") and pSubShip.__class__ == App.ShipClass:
                    iSubShipID = pSubShip.GetObjID()
                    if shipIsCloaking:
                        CloakShip(iSubShipID, 0)
                    elif shipIsDecloaking:
                        CloakShip(iSubShipID, 1)

        pObject.CallNextHandler(pEvent)

def DecloakHandler(pObject, pEvent):
        debug(__name__ + ", DecloakHandler")
        pInstance = findShipInstance(pObject)

        pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID) #App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))

        iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        # iterate over every Turret
        pCloak = pShip.GetCloakingSubsystem()
        if pCloak and hasattr(pInstance, "TurretList"):
            shipIsCloaking = pCloak.IsCloaking()
            shipIsDecloaking = pCloak.IsDecloaking()
            for pSubShip in pInstance.TurretList:
                if hasattr(pSubShip, "__class__") and pSubShip.__class__ == App.ShipClass:
                    iSubShipID = pSubShip.GetObjID()
                    if shipIsCloaking:
                        CloakShip(iSubShipID, 0)
                    elif shipIsDecloaking:
                        CloakShip(iSubShipID, 1)

        pObject.CallNextHandler(pEvent)


# called when a ship enters a Set.
def EnterSet(pObject, pEvent):
        debug(__name__ + ", EnterSet")

        pShip   = App.ShipClass_Cast(pEvent.GetDestination())
        try:
            pShip =  App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        except:
            pShip = None
            traceback.print_exc()

        if pShip:
            myShipID = pShip.GetObjID()
            pEntry = oTurrets.GetBattleTurretListenerEntry(myShipID)
            if pEntry != None:
                pInstanceA = findShipInstance(pShip)
                pInstanceShipID = getShipIDfromInstance(pInstanceA)
                pInstanceO = pEntry[0]
                if pInstanceShipID != myShipID: # Weird but can happen for the player - trying to make this as player-agnostic as possible, in case this ever gets implemented for multiplayer
                    #print "calling EnterSet --> trueDetach"
                    oTurrets.trueDetach(pInstanceO, myShipID) # TO-DO MAYBE NOT ADD THE TRUE DETACH CALL HERE?
                else:
                    if pInstanceA != None:
                        #print "calling EnterSet --> Detach Parts"
                        oTurrets.DetachParts(pShip, pInstanceA) # This would not only ensure that the proximity manager stops complaining, but also cleans any possible turrets left behind

# called when a ship exits a Set. Replacement for WARP_END Handler.
def ExitSet(pObject, pEvent):
        debug(__name__ + ", ExitSet")
        pShip   = App.ShipClass_Cast(pEvent.GetDestination())
        try:
            pShip =  App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        except:
            pShip = None
            traceback.print_exc()

        sSetName = pEvent.GetCString()

        if pShip:
            myShipID = pShip.GetObjID()
            pEntry = oTurrets.GetBattleTurretListenerEntry(myShipID)
            if pEntry != None:
                pInstanceA = findShipInstance(pShip)
                pInstanceShipID = getShipIDfromInstance(pInstanceA)
                pInstanceO = pEntry[0]
                if pInstanceShipID != myShipID: # Weird but can happen for the player - trying to make this as player-agnostic as possible, in case this ever gets implemented for multiplayer
                    #print "calling EnterSet --> trueDetach"
                    oTurrets.trueDetach(pInstanceO, myShipID) # TO-DO MAYBE NOT ADD THE TRUE DETACH CALL HERE?
                else:
                    if pInstanceA != None:
                        #print "calling EnterSet --> Detach Parts"
                        oTurrets.DetachParts(pShip, pInstanceA) # This would not only ensure that the proximity manager stops complaining, but also cleans any possible turrets left behind

                    # if the system we come from is the warp system, then we exitwarp, right?
                    if sSetName == "warp":
                        # call ExitingWarp in a few seconds
                        pSeq = App.TGSequence_Create()
                        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "ExitingWarp", pShip), 4.0)
                        pSeq.Play()
                    else:
                        if pInstanceA and not oTurrets.ArePartsAttached(pShip, pInstanceA):
                            # try to get the last alert level
                            for item in pInstanceA.TurretSystemOptionsList:
                                    if item[0] == "Setup":
                                            dGenShipDict = item[1]
                                            break
        
                            # update alert state
                            if (not dGenShipDict.has_key("AlertLevel")) or dGenShipDict["AlertLevel"] == None:
                                dGenShipDict["AlertLevel"] = pShip.GetAlertLevel()
                            iType = dGenShipDict["AlertLevel"]

                            pInstanceAdict = pInstanceA.__dict__
                            if pInstanceAdict[oTurrets.name]["Setup"].has_key("AttackModel") and iType == 2:
                                    oTurrets.AttachParts(pShip, pInstanceA)
                                    if pInstanceAdict[oTurrets.name]["Setup"].has_key("AttackModel"):
                                            sNewShipScript = pInstanceAdict[oTurrets.name]["Setup"]["AttackModel"]
                                            ReplaceModel(pShip, sNewShipScript)
                                            checkingReCloak(pShip)

                                    oTurrets.SetBattleTurretListenerTo(pShip, 1) # Combat mode

                            else:
                                    if pInstanceAdict[oTurrets.name]["Setup"].has_key("NormalModel"):
                                            sNewShipScript = pInstanceAdict[oTurrets.name]["Setup"]["NormalModel"]
                                            ReplaceModel(pShip, sNewShipScript)
                                            checkingReCloak(pShip)

                                    oTurrets.SetBattleTurretListenerTo(pShip, -1) # Not combat mode
    
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

        # Because hiding and unhiding the ship does not seem to do the job of fixing the weird lack of lights, but something like this dumb thing below does :/
        from ftb.Tech.ATPFunctions import *

        point = pShip.GetWorldLocation()
        pHitPoint = App.TGPoint3()
        pHitPoint.SetXYZ(point.x, point.y, point.z)

        pVec = pShip.GetVelocityTG()
        pVec.Scale(0.001)
        pHitPoint.Add(pVec)

        mod = "Tactical.Projectiles.AutomaticSystemRepairDummy" 
        try:
                pTempTorp = FireTorpFromPointWithVector(pHitPoint, pVec, mod, pShip.GetObjID(), pShip.GetObjID(), __import__(mod).GetLaunchSpeed())
                if pTempTorp:
                        pTempTorp.SetHidden(1)
                        pTempTorp.SetLifetime(0.0)
        except:
                print __name__, ": You are missing '", mod, "' torpedo on your install, without that a weird black-texture-until-firing-or-fired bug may happen"
                traceback.print_exc()

        if App.g_kUtopiaModule.IsMultiplayer():
                MPSentReplaceModelMessage(pShip, sNewShipScript)



def checkingReCloak(pShip):
	try:
		pShipID = pShip.GetObjID()
		if pShipID:
			pShip = App.ShipClass_GetObjectByID(None, pShipID)
		if pShip:
			pCloak = pShip.GetCloakingSubsystem()
			if pCloak:
				shipIsCloaking = pCloak.IsCloaking() or pCloak.IsCloaked() 
				shipIsDecloaking = pCloak.IsDecloaking() or not pCloak.IsCloaked()
				if shipIsCloaking:
					CloakShip(pShipID, -1)
				#elif shipIsDecloaking:
				#	CloakShip(pShipID, 1)

	except:
		traceback.print_exc()

	return 0

# Prepares a ship to move: Replaces the current Model with the move Model and attaches its sub Models
def PrepareShipForMove(pShip, pInstance):
        debug(__name__ + ", PrepareShipForMove")
        if not oTurrets.ArePartsAttached(pShip, pInstance):
                if pInstance.__dict__[oTurrets.name]["Setup"].has_key("Body"):
                        ReplaceModel(pShip, pInstance.__dict__[oTurrets.name]["Setup"]["Body"])
                oTurrets.AttachParts(pShip, pInstance)

                checkingReCloak(pShip)


def IncCurrentMoveID(pShip, pInstance):
        debug(__name__ + ", IncCurrentMoveID")
        if hasattr(pInstance, "TurretSystemOptionsList"):
            for item in pInstance.TurretSystemOptionsList:
                if len(item) > 1 and item[0] == "Setup" and item[1].has_key("GenMoveID"):
                    item[1]["GenMoveID"] = item[1]["GenMoveID"] + 1


def GetCurrentMoveID(pShip, pInstance):
        debug(__name__ + ", GetCurrentMoveID")
        iGenMoveID = -1
        
        if hasattr(pInstance, "TurretSystemOptionsList"):
            for item in pInstance.TurretSystemOptionsList:
                if len(item) > 1 and item[0] == "Setup" and item[1].has_key("GenMoveID"):
                    iGenMoveID = item[1]["GenMoveID"]
        return iGenMoveID
                        

def MoveFinishMatchId(pShip, pInstance, iThisMovID):
        debug(__name__ + ", MoveFinishMatchId")
        if GetCurrentMoveID(pShip, pInstance) == iThisMovID:
                return 1
        return 0

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
                        if pObject.GetObjID() == pObjectInBetween.GetObjID() and pObject.GetObjID() != pObject2.GetObjID() and pObject.GetObjID() != pObject1.GetObjID():
                                # not firing because parent ship is between us. Yep. We're now true.
                                bBlockedLOS = 1
                                break
                        pObject = pProxManager.GetNextObject(kIter)
                pProxManager.EndObjectIteration(kIter)

        return bBlockedLOS

def WeaponSystemFiredStopAction(pShip, pSystem, pTarget=None):
        debug(__name__ + ", WeaponSystemFiredStopAction")
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WeaponSystemFiredStopActionAux", pShip, pSystem, pTarget), 0.1) # 0.1 works
        pSeq.Play()

def WeaponSystemFiredStopActionAux(pAction, pShip, pSystem, pTarget):
       debug(__name__ + ", WeaponSystemFiredStopActionAux")
       pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
       if pShip:
           pTargetI =  App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
           if pTargetI:
               pSystem.StopFiringAtTarget(pTargetI)
           else:
               pSystem.StopFiring()

       return 0

def WeaponFiredStopAction(pObject, pEvent):
        debug(__name__ + ", WeaponFiredStopAction")

        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WeaponFiredStopActionAux", pObject, pEvent), 0.1)
        pSeq.Play()

def WeaponFiredStopActionAux(pAction, pObject, pEvent):
        debug(__name__ + ", WeaponFiredStopActionAux")
        WeaponFiredStop(pObject, pEvent)

def WeaponFiredStop(pObject, pEvent, stoppedFiring=None):
        debug(__name__ + ", WeaponFiredStop")
        #Potential TO-DO .... maybe merge with WeaponFired

        pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
        pInstance = None
        if pShip:
                pInstance = findShipInstance(pShip)

        if pInstance and pInstance.__dict__.has_key(oTurrets.name) and hasattr(pInstance, "TurretList"):
                pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
                if pWeaponFired == None:
                        #print __name__, ": no weapon stopped fired obj..."
                        return

                pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
                if pTarget:
                    pTarget = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
                if not pTarget:
                    pTarget = pShip.GetTarget()

                pParentFired = pWeaponFired.GetParentSubsystem()
                if pParentFired == None:
                        #print __name__, ": no weapon stop-fire parent subsystem obj..."
                        pObject.CallNextHandler(pEvent)
                        return

                weaponParentName = pParentFired.GetName()
                weaponName = pWeaponFired.GetName()

                lTurretsToFire = {}
                #lDoNotAttackYourself = []

                if hasattr(pInstance, "TurretList"):
                        # Reminder because sometimes a ship may accidentally fire on the parent and then the game automatically switches it to enemy
                        pMission        = MissionLib.GetMission()
                        pFriendlies     = None
                        pEnemies        = None 
                        pNeutrals       = None
                        pTractors       = None
                        if pMission:
                            pFriendlies     = pMission.GetFriendlyGroup() 
                            pEnemies        = pMission.GetEnemyGroup() 
                            pNeutrals       = pMission.GetNeutralGroup()
                            pTractors       = pMission.GetTractorGroup()
                        for pSubShip in pInstance.TurretList:
                            if pMission:
                                pFriendlies.RemoveName(pSubShip.GetName())
                                pEnemies.RemoveName(pSubShip.GetName())
                                pNeutrals.RemoveName(pSubShip.GetName())
                                pTractors.RemoveName(pSubShip.GetName())
                                pTractors.AddName(pSubShip.GetName())
                                mySubsystem = MissionLib.GetSubsystemByName(pSubShip, weaponName)
                                if mySubsystem != None:
                                        mySubsWep = App.Weapon_Cast(mySubsystem)
                                        thisParent = mySubsWep.GetParentSubsystem()
                                        for item in pInstance.TurretSystemOptionsList:
                                            if item[0] != "Setup" and item[0].GetObjID() == pSubShip.GetObjID():
                                                lTurretsToFire[pSubShip.GetObjID()] = [pSubShip, mySubsystem, item, thisParent]
                                                break

                if lTurretsToFire:

                        for turret in lTurretsToFire.keys():
                                #print "TURRET TO STOP ", lTurretsToFire[turret][0].GetName()

                                wpnSystem = App.WeaponSystem_Cast(lTurretsToFire[turret][-1])

                                if wpnSystem != None:
                                        for anotherTurret in pInstance.TurretList:
                                            wpnSystem.StopFiringAtTarget(anotherTurret) # NOTE: see if they have accidentally attacked themselves... it could be possible with other scripts!!!   

                                        if pTarget:
                                            wpnSystem.StopFiringAtTarget(pTarget)

                                        if lTurretsToFire[turret][-2][1].has_key("SimulatedPhaser") and lTurretsToFire[turret][-2][1]["SimulatedPhaser"] == 1:
                                            turPhsSys = lTurretsToFire[turret][0].GetPhaserSystem()
                                            isPhaserFire = turPhsSys and wpnSystem.GetName() == turPhsSys.GetName()
                                            if isPhaserFire:
                                                lookandUpdateSiblingTPhasers(wpnSystem, pShip, lTurretsToFire[turret][0], 1, 1)
                                        if lTurretsToFire[turret][-2][1].has_key("SimulatedTractor") and lTurretsToFire[turret][-2][1]["SimulatedTractor"] == 1:
                                            turTbpSys = lTurretsToFire[turret][0].GetTractorBeamSystem()
                                            isTrBPFire = turTbpSys and wpnSystem.GetName() == turTbpSys.GetName()
                                            if isTrBPFire:
                                                lookandUpdateSiblingTPhasers(wpnSystem, pShip, lTurretsToFire[turret][0], 1, 0)

                                        wpnSystem.StopFiring()
                         

                                        wpnSystem.SetForceUpdate(1)
                                #else:
                                #        print "We have gone so far, what do you mean you don't have the system to fire???"
                        
        pObject.CallNextHandler(pEvent)


def WeaponFired(pObject, pEvent, stoppedFiring=None):
        debug(__name__ + ", WeaponFired")
        #Potential TO-DO  .... maybe merge with WeaponFiredStop

        pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
        pInstance = None
        if pShip:
                pInstance = findShipInstance(pShip)

        if pInstance and pInstance.__dict__.has_key(oTurrets.name) and hasattr(pInstance, "TurretList"):
                pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
                if pWeaponFired == None:
                        #print __name__, ": no weapon fired obj..."
                        return
                

                pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pWeaponFired.GetTargetID()))
                if pTarget:
                    pTarget = App.ShipClass_GetObjectByID(None, pTarget.GetObjID())
                if not pTarget:
                    pTarget = pShip.GetTarget()
                    while pTarget in pInstance.TurretList: # another safety feature for doofus AutoTargeting scripts
                        pTarget = pShip.GetNextTarget()

                pParentFired = pWeaponFired.GetParentSubsystem()
                if pParentFired == None:
                        #print __name__, ": We could not find the parent fired? what?"
                        pObject.CallNextHandler(pEvent)
                        return

                weaponParentName = pParentFired.GetName()
                weaponName = pWeaponFired.GetName()

                phsrDmgControl = App.PhaserSystem_Cast(pParentFired)
                phsrLvl = None
                if phsrDmgControl and hasattr(phsrDmgControl, "GetPowerLevel") and phsrDmgControl.GetPowerLevel() != None:
                    phsrLvl = phsrDmgControl.GetPowerLevel()

                lTurretsToFire = {}
                if hasattr(pInstance, "TurretList"):
                        # Reminder because sometimes a ship may accidentally fire on the parent and then the game automatically switches it to enemy
                        pMission        = MissionLib.GetMission()
                        pFriendlies     = None
                        pEnemies        = None 
                        pNeutrals       = None
                        pTractors       = None
                        if pMission:
                            pFriendlies     = pMission.GetFriendlyGroup() 
                            pEnemies        = pMission.GetEnemyGroup() 
                            pNeutrals       = pMission.GetNeutralGroup()
                            pTractors       = pMission.GetTractorGroup()

                        for pSubShip in pInstance.TurretList:
                            if pMission:
                                pFriendlies.RemoveName(pSubShip.GetName())
                                pEnemies.RemoveName(pSubShip.GetName())
                                pNeutrals.RemoveName(pSubShip.GetName())
                                pTractors.RemoveName(pSubShip.GetName())
                                pTractors.AddName(pSubShip.GetName())

                                mySubsystem = MissionLib.GetSubsystemByName(pSubShip, weaponName)

                                if mySubsystem:
                                        mySubsWep = App.Weapon_Cast(mySubsystem)
                                        thisParent = mySubsWep.GetParentSubsystem()
                                        for item in pInstance.TurretSystemOptionsList:
                                            if item[0] != "Setup" and item[0].GetObjID() == pSubShip.GetObjID():
                                                lTurretsToFire[pSubShip.GetObjID()] = [pSubShip, mySubsystem, item, thisParent]
                                                break

                shouldWeTakeMeasuresToAvoidGettingHit = (pTarget and (pTarget in pInstance.TurretList)) # Because some versions of AutoTargeting are wonky, they may target non-enemies, or some mods can make neutrals or tractor teams to switch, meaning the turret could have aimed at another friendly turret of themselves
                if lTurretsToFire:

                        #for turret in lTurretsToFire:
                        for turret in lTurretsToFire.keys():
                                #print "TURRET ", lTurretsToFire[turret][0].GetName()

                                wpnSystem = App.WeaponSystem_Cast(lTurretsToFire[turret][-1])

                                if wpnSystem != None:
                                        if pTarget and not shouldWeTakeMeasuresToAvoidGettingHit: # Just a safety precaution
                                            lTurretsToFire[turret][-2][1]["TARGET"] = pTarget #item[1]["TARGET"] = pTarget
                                            pSet = lTurretsToFire[turret][0].GetContainingSet()
                                            mothershipBlock = 0 # 0.991 change, after optimizing this is so effective that no turret can ever fire if it Checks Line of Sight
                                            # mothershipBlock = CheckLOS(pTarget, lTurretsToFire[turret][0], pShip, pSet) # This prevents turrets from firing most of the time since technically the turrets are inside.
                                            if mothershipBlock:
                                                #print "parent is between us, stopping..."
                                                wpnSystem.StopFiring()
                                            else:
                                                #print "firing the weapon"

                                                if phsrLvl:
                                                    wpnSystemButPhaser = App.PhaserSystem_Cast(wpnSystem)
                                                    if wpnSystemButPhaser and hasattr(wpnSystemButPhaser, "GetPowerLevel") and wpnSystemButPhaser.GetPowerLevel() != None: # GetPowerLevel#SetPowerLevel
                                                        wpnSystemButPhaser.SetPowerLevel(phsrLvl)

                                                # Fix for disruptors, we only fire when we want to... once!
                                                turPulSys = lTurretsToFire[turret][0].GetPulseWeaponSystem()
                                                turTrpSys = lTurretsToFire[turret][0].GetTorpedoSystem()
                                                isPulseFire = turPulSys and wpnSystem.GetName() == turPulSys.GetName()
                                                isTorpFire = turTrpSys and wpnSystem.GetName() == turTrpSys.GetName()
                                                if (isPulseFire) or (isTorpFire):
                                                    """
                                                    ## *** SORRY BUT DOING THIS, WHILE IT WORKS, MAKES THE TORPEDO FIRED REACH A VIRTUAL CALL WHEN DISAPPEARING FROM THE SET FOR SOME UNKNOWN REASON ***
                                                    if isTorpFire and lTurretsToFire[turret][-2][1].has_key("SyncTorpType") and lTurretsToFire[turret][-2][1]["SyncTorpType"] > 0:
                                                        pParentFiredSystem = App.TorpedoSystem_Cast(pParentFired)
                                                        if pParentFiredSystem:
                                                            pParentFiredSystemProperty = App.TorpedoSystemProperty_Cast(pParentFiredSystem.GetProperty())

                                                            # ammoType= pParentFiredSystem.GetCurrentAmmoType() # this is a C TorpedoAmmoType instance - maybe useful for phasers later... if it's possible?
                                                            #ammoType= pParentFiredSystem.GetCurrentAmmoType().GetTorpedoScript() # this is a C TorpedoAmmoType instance
                                                            #print ammoType
                                                            if lTurretsToFire[turret][-2][1]["SyncTorpType"] == 1: # We sync slots with slots
                                                                #print "Ok so torp slot sync"
                                                                ammoNum = pParentFiredSystem.GetCurrentAmmoTypeNumber()
                                                                # Version 2, it is a delayed sync, when the ammo gets changed and the ship fires, it will look for that
                                                                maxTurAmmo = turTrpSys.GetNumAmmoTypes()
                                                                #print maxTurAmmo
                                                                if maxTurAmmo > 0: # *** IMPORTANT ***
                                                                    ammoNumAppropiate = ammoNum % maxTurAmmo

                                                                    curTurammoNum = turTrpSys.GetCurrentAmmoTypeNumber()
                                                                    #print ammoNumAppropiate, " ammoNumAppropiate vs curTurammoNum ", curTurammoNum
                                                                    #If this works (it didn't) add also an event for player changing torp types if necessary... or do a dirty thing and check it in movement... that could work
                                                                    if curTurammoNum != ammoNumAppropiate:
                                                                        #print "changing ammo types"
                                                                        #turTrpSys.LoadAmmoType(ammoNumAppropiate, 1000)
                                                                        turTrpSys.SetAmmoType(ammoNumAppropiate)
                                                                        wpnSystem = turTrpSys # I was pointed here as for the potential virtual call issue but testing did not indicate this was at the very least the cause of the issue.

                                                            elif lTurretsToFire[turret][-2][1]["SyncTorpType"] == 2: # We sync types with types, if no type is found, then no change
                                                                #print "Ok so torp type sync"

                                                                #pTurretSystemProperty = App.TorpedoSystemProperty_Cast(turTrpSys.GetProperty())
                                                                #pTurretSystemProperty.SetTorpedoScript(App.AT_ONE, ammoType)

                                                                # POSSIBLE SOLUTION: Special thanks to USS Sovereign for giving me tips towards looking for AdvancedTorpedoManagement.py
                                                                # LEAVING THIS AS UNTOUCHED AS POSSIBLE TO SHOW WHAT I MEAN WITH SAME THING NOT WORKING
                                                                Storage = []

                                                                pPTorpedoType = pParentFiredSystem.GetAmmoType(ammoNum)
                                                                ammoTypeScript = pPTorpedoType.GetTorpedoScript()
                                                                torpName = pPTorpedoType.GetAmmoName()
                                                                avail = 1000 # pParentFiredSystem.GetNumAvailableTorpsToType(App.AT_ONE)
                                                                Storage[0 : 2] = [ammoTypeScript, torpName, avail]
                                                                slot = App.AT_ONE
                                                                defaultslot = App.AT_ONE

                                                                # This below also causes a crash :(
                                                                pTorpedoType = turTrpSys.GetAmmoType(App.AT_ONE)


                                                                pTorpedoTypeName = pTorpedoType.GetAmmoName()
                                                                pTorpedoTypeScript = pTorpedoType.GetTorpedoScript()
                                                                Storage[3 : 5] = [pTorpedoTypeScript, pTorpedoTypeName, avail]

                                                                pTorpedoTypeScript = Storage[0 * 3]
                                                                pTorpedoTypeAvailable = Storage[(0 * 3) + 2]
                                                                Storage[(0 * 3) + 2] = 0

                                                                hugo = pTorpedoType.SetTorpedoScript(pTorpedoTypeScript)
                                                                hansi = pTorpedoType.SetMaxTorpedoes(int(pTorpedoTypeAvailable))
                                                                turTrpSys.LoadAmmoType(defaultslot, int(pTorpedoTypeAvailable))

                                                                #turTrpSys2 = lTurretsToFire[turret][0].GetTorpedoSystem()
                                                                #turTrpSys2.SetAmmoType(defaultslot)

                                                    """
                                                    WeaponSystemFiredStopAction(pShip, wpnSystem, pTarget)

                                                else:
                                                    if lTurretsToFire[turret][-2][1].has_key("SimulatedPhaser") and lTurretsToFire[turret][-2][1]["SimulatedPhaser"] == 1:
                                                        turPhsSys = lTurretsToFire[turret][0].GetPhaserSystem()
                                                        isPhaserFire = turPhsSys and wpnSystem.GetName() == turPhsSys.GetName()
                                                        if isPhaserFire:
                                                            lookandUpdateSiblingTPhasers(wpnSystem, pShip, lTurretsToFire[turret][0], 0, 1)

                                                    if lTurretsToFire[turret][-2][1].has_key("SimulatedTractor") and lTurretsToFire[turret][-2][1]["SimulatedTractor"] == 1:
                                                        turTbpSys = lTurretsToFire[turret][0].GetTractorBeamSystem()
                                                        isTrBPFire = turTbpSys and wpnSystem.GetName() == turTbpSys.GetName()
                                                        if isTrBPFire:
                                                            lookandUpdateSiblingTPhasers(wpnSystem, pShip, lTurretsToFire[turret][0], 0, 0)


                                                ####### XPERIMENTAL AREA, TO SEE KCS' IDEA ABOUT CHANGING A TRACTOR BEAM COLOR AND TEXTURE
                                                #tractorQ = pShip.GetImpulseEngineSubsystem().GetTractorBeamSystem()
                                                #if tractorQ:
                                                #        print "Wait, there's a tractor on the impulse engine?"
                                                #        for i in range(tractorQ.GetNumChildSubsystems()):
                                                #            pChild = tractorQ.GetChildSubsystem(i)
                                                #            print "pChild is of type", pChild.GetObjType()
                                                #            pChildProperty = App.TractorBeamProperty_Cast(pChild.GetProperty())
                                                #            #print "pChild is of type", pChild.GetObjType()
                                                #            # subsystems TractorBeamProjector -> TractorBeamProperty
                                                #
                                                #            kColor = App.TGColorA()
                                                #            kColor.SetRGBA(0.900000, 0.400000, 0.000000, 1.000000)
                                                #            pChildProperty.SetOuterShellColor(kColor)
                                                #            kColor.SetRGBA(0.900000, 0.400000, 0.000000, 1.000000)
                                                #            pChildProperty.SetInnerShellColor(kColor)
                                                #            kColor.SetRGBA(0.900000, 0.400000, 0.000000, 1.000000)
                                                #            pChildProperty.SetOuterCoreColor(kColor)
                                                #            kColor.SetRGBA(0.900000, 0.400000, 0.000000, 1.000000)
                                                #            pChildProperty.SetInnerCoreColor(kColor)
                                                #            pChildProperty.SetTextureName("data/coiledTwistBeam1.tga")
                                                #            tractorQ.SetForceUpdate(1)
                                                #
                                                ####### XPERIMENTAL AREA, TO SEE KCS' idea 

                                                wpnSystem.StopFiring() # Safety check for strays due to multi-targeting
                                                wpnSystem.StartFiring(pTarget)
                                                
                                        else:
                                            lTurretsToFire[turret][-2][1]["TARGET"] = pShip.GetTarget()

                                        for anotherTurret in pInstance.TurretList:
                                            wpnSystem.StopFiringAtTarget(anotherTurret) # NOTE: see if they have accidentally attacked themselves... it could be possible with other scripts!!!

                                        wpnSystem.SetForceUpdate(1)
                                #else:
                                #        print "We have gone so far, what do you mean you don't have the system to fire???"
                        
        pObject.CallNextHandler(pEvent)

# Phasers maybe we cannot fix, but torps? Surely we can... right?
def TorpedoTurretFiredTest(pObject, pEvent):
    debug(__name__ + ", TorpedoTurretFiredTest")
    # Ok, so, since for some reason, firing a torpedo is not recognized unless it is a broadcast handler, and only for torpedoes and not pulses, we'll have to do this the hard and slow way...
    # Recommended to upgrade several of those for-loops into iterators if possible...
    pTurret = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
    if not pTurret:
        pObject.CallNextHandler(pEvent)
        return

    pSet = pTurret.GetContainingSet()
    if not pSet:
        pObject.CallNextHandler(pEvent)
        return
    """    
    # This section got commented, there is a more effective way to prevent torps and pulses from damaging the parent ship
    mineTorps= []

    
    # Option A, look for all torps in set, this takes a long time, try to find a better option.
    # For some reason this is the only one which, when a lot of ships are firing torps or disruptors, works well 99% of times.
    for aObject in pSet.GetClassObjectList(App.CT_TORPEDO):
        aTorp = App.Torpedo_GetObjectByID(None, aObject.GetObjID())
        if aTorp and aTorp.GetParentID() == pTurret.GetObjID():
            mineTorps.append(aTorp)

    pShipID = oInvertedTurretList.getShipForTurret(pTurret.GetObjID())
    if pShipID != None:
        pShip = App.ShipClass_GetObjectByID(None, pShipID)
        if pShip: 
            for pTorp in mineTorps:
                pTorp.SetParent(pShipID)
                pTorp.UpdateNodeOnly()
    """
    """
    #Option B, search around 5 times the radious of the turret we are part of (OUTDATED). This still causes problems

    pProx = pSet.GetProximityManager()

    kIter = pProx.GetNearObjects(pTurret.GetWorldLocation(), pTurret.GetRadius() * 5 + 10, 1) 
    while 1:
        pdObject = pProx.GetNextObject(kIter)
        if not pdObject:
            break

        if pdObject.IsTypeOf(App.CT_TORPEDO):
            # Torpedo scanning would just work like normal, with no buffs
            pTorp = App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(pdObject.GetObjID()))
            if pTorp and pTorp.GetParentID() == pTurret.GetObjID():
                mineTorps.append(pTorp)	

    pProx.EndObjectIteration(kIter)
    # Removed dry lava
    """
    """
    #Option C, search around 2 times the radius of the main ship we are part of (OUTDATED). This still gives problems!!!???
    # Removed dry lava
    """

    pWeaponFired = App.Weapon_Cast(pEvent.GetSource())
    if pWeaponFired == None:
        #print "no weapon subshipfire fired obj..."
        pObject.CallNextHandler(pEvent)
        return

    pParentFired = pWeaponFired.GetParentSubsystem()
    if pParentFired == None:
        #print "no weapon subshipfire parent subsystem obj..."
        pObject.CallNextHandler(pEvent)
        return      

    phsrCtrl = pTurret.GetPhaserSystem()
    trpCtrl = pTurret.GetTorpedoSystem()

    if trpCtrl and pParentFired.GetName() == trpCtrl.GetName(): #if it's a torp one, recharges its torpedoes and max of torps ready, to allow full control from parent ship!!!

        # Find proper torps..
        iNumTypes = trpCtrl.GetNumAmmoTypes()
        for iType in range(iNumTypes):
            trpCtrl.LoadAmmoType(iType, 1000) # In theory, we are not going to have any turret fire more than 1000 torps at the same time... right?
            #trpCtrl.SetAmmoType(iType, 0)
            #pTorpType = trpCtrl.GetAmmoType(iType)
            #trpCtrl.UpdateNodeOnly()

        #print "pTurret property list: ", pTurret.GetPropertySet.GetPropertyList()

        pTorpTube = App.TorpedoTube_Cast(pWeaponFired)

        #### **** TO-DO **** #### Gizmo_3: reading your script i think it's probably getting angry because you're doing things in a way that desyncs the torpedo system's state and the script it expects to have or something. 
        ## i'm not sure what's desyncing, but it might be smart to try to unload all the torpedo tubes on the ship before you modify what scripts are being used by the ammo of your torpedo system TorpedoTube.UnloadTorpedo
        # Maybe look for the torp tubes with App.CT_TORPEDO_TUBE?
        #### setting the script of the ammo type also might not set the script in the property object, might want to check that, could be that your torpedosystem and its torpedosystemproperty are having different scripts
        ##   when you do that, this probably isn't happenning, but i guess it's possible
        ## As for events, App.ET_TORPEDO_RELOAD and then checking if the torpedo slot selected matches the turrets
        ## trpCtrl.SetAmmoType(1, 0) # Tested the suggestion above for swapping torpedoes, still crashes :(

        #pTurretSystemProperty = App.TorpedoSystemProperty_Cast(trpCtrl.GetProperty())
        #pTurretSystemProperty.SetNumAmmoTypes(3)
        #pTurretSystemProperty.SetTorpedoScript(2, "Tactical.Projectiles.PhotonTorpedo")
        #trpCtrl.SetAmmoType(1, 0) # Causes crash
        #pTorpTube.UnloadTorpedo()

        #trpCtrl.SetAmmoType(1)
        #pTorpTube.UnloadTorpedo()
        #pTorpTube.ReloadTorpedo()
        pTorpTube.SetNumReady(pTorpTube.GetMaxReady())

    pObject.CallNextHandler(pEvent)
    return 0

def lookandUpdateSiblingTPhasers(wpnSystem, pShip, pTurret, discharge=0, phaser=1):
    debug(__name__ + ", lookandUpdateSiblingTPhasers")

    wpnSystemButPhaser = App.PhaserSystem_Cast(wpnSystem)
    itsTractor = 0
    if not wpnSystemButPhaser:
        itsTractor = 1
        wpnSystemButPhaser = App.TractorBeamSystem_Cast(wpnSystem)

    pShipNode = pShip.GetNiObject()
    pTurretNode = pTurret.GetNiObject()
    
    # 0.99 Innovation - Optimization from O(N^2) or more to 0(3N)
    """
    # Old 0.98 code
    for i in range(wpnSystem.GetNumChildSubsystems()):
        pChild = wpnSystem.GetChildSubsystem(i)
        if (pChild != None):
            parentSibling = MissionLib.GetSubsystemByName(pShip, pChild.GetName() + " T")
            if parentSibling:
                childPos = pChild.GetWorldLocation()
                pTurretNode = pTurret.GetNiObject()
                newPosition = App.TGModelUtils_WorldToLocalPoint(pShipNode, childPos)

                subsystemProperty = parentSibling.GetProperty()
                oldPosition = subsystemProperty.GetPosition()
                subsystemProperty.SetPosition(newPosition.x/100.0, newPosition.y/100.0, newPosition.z/100.0)
                
                if not itsTractor and discharge != 2:
                    parentSiblingBank = App.EnergyWeaponProperty_Cast(subsystemProperty)
                    if discharge:
                        parentSiblingBank.SetMaxCharge(-abs(parentSiblingBank.GetMaxCharge()))
                    else:
                        parentSiblingBank.SetMaxCharge(abs(parentSiblingBank.GetMaxCharge()))
    """

    systemsToChoose = {}

    for i in range(wpnSystem.GetNumChildSubsystems()):
        pChild = wpnSystem.GetChildSubsystem(i)
        if (pChild != None):
            newName = pChild.GetName() + " T"
            systemsToChoose[newName] = [pChild, None]

    lTurretSys = systemsToChoose.keys()

    # We are only interested on phasers or tractors, we can do this even faster
    pEnergyWeaponSubsystem = None
    if phaser:
        pEnergyWeaponSubsystem = pShip.GetPhaserSystem()
    else:
        pEnergyWeaponSubsystem = pShip.GetTractorBeamSystem()

    if pEnergyWeaponSubsystem:
        for i in range(pEnergyWeaponSubsystem.GetNumChildSubsystems()):
            pChildM = pEnergyWeaponSubsystem.GetChildSubsystem(i)
            if pChildM.GetName() in lTurretSys:
                systemsToChoose[pChildM.GetName()][-1] = pChildM

    for i in lTurretSys:
        if systemsToChoose[i][-1] != None:
            childPos = systemsToChoose[i][0].GetWorldLocation()
            newPosition = App.TGModelUtils_WorldToLocalPoint(pShipNode, childPos)

            subsystemProperty = systemsToChoose[i][-1].GetProperty()
            oldPosition = subsystemProperty.GetPosition()
            subsystemProperty.SetPosition(newPosition.x/100.0, newPosition.y/100.0, newPosition.z/100.0)
                
            if not itsTractor and discharge != 2:
                parentSiblingBank = App.EnergyWeaponProperty_Cast(subsystemProperty)
                if discharge:
                    parentSiblingBank.SetMaxCharge(-abs(parentSiblingBank.GetMaxCharge()))
                else:
                    parentSiblingBank.SetMaxCharge(abs(parentSiblingBank.GetMaxCharge()))


# called after the Alert move action
# Remove the attached parts and use the attack or normal model now
def AlertMoveFinishTemporarilyAction(pAction, pShip, pInstance, iThisMovID, iType=None):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", AlertMoveFinishTemporarilyAction")

        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1

        dGenShipDict = None
        for item in pInstance.TurretSystemOptionsList:
            if len(item) > 1 and item[0] == "Setup":
                dGenShipDict = item[1]
                break

        if dGenShipDict == None:
            return 1

        if not dGenShipDict.has_key("AlertLevel") or dGenShipDict["AlertLevel"] == None:
            if not iType:
               dGenShipDict["AlertLevel"] = pShip.GetAlertLevel()
            else:
               dGenShipDict["AlertLevel"] = iType

        iType = dGenShipDict["AlertLevel"]
        inCombatM = (iType == 2)

        if inCombatM:
                sNewShipScript = None
                if pInstance.__dict__[oTurrets.name]["Setup"].has_key("AttackModel"):
                        sNewShipScript = pInstance.__dict__[oTurrets.name]["Setup"]["AttackModel"]

                elif pInstance.__dict__[oTurrets.name]["Setup"].has_key("NormalModel"):
                        sNewShipScript = pInstance.__dict__[oTurrets.name]["Setup"]["NormalModel"]

                if sNewShipScript != None:
                        ReplaceModel(pShip, sNewShipScript)
                        checkingReCloak(pShip)
        else:
                if pInstance.__dict__[oTurrets.name]["Setup"].has_key("NormalModel"):
                        sNewShipScript = pInstance.__dict__[oTurrets.name]["Setup"]["NormalModel"]
                        ReplaceModel(pShip, sNewShipScript)
                        checkingReCloak(pShip)

                oTurrets.DetachParts(pShip, pInstance) # we hide turrets when not in alert mode, else we keep them

        turretTranslocation(pInstance, pShip.GetObjID(), iType)

        if inCombatM:
                oTurrets.SetBattleTurretListenerTo(pShip, 1)
        else:
                oTurrets.SetBattleTurretListenerTo(pShip, -1) # Not combat mode
        return 0

# called after the warp-start move action
# Do not remove the attached parts, and use the warp model now
def WarpStartMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", WarpStartMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1

        # We may have finished the start of warp, but that doesn't mean we have ended yet - turrets will remain in position and then probably hide
        oTurrets.DetachParts(pShip, pInstance)
        return 0


# called after the warp-exit move action
# Remove the attached parts and use the attack or normal model now
def WarpExitMoveFinishAction(pAction, pShip, pInstance, iThisMovID):
        # Don't switch Models back when the ID does not match
        debug(__name__ + ", WarpExitMoveFinishAction")
        if not MoveFinishMatchId(pShip, pInstance, iThisMovID):
                return 1

        #If the system was totally concurrent, this line below would be totally necessary
        oTurrets.SetBattleTurretListenerTo(pShip, -1) # Not combat mode    

        # try to get the last alert level
        dGenShipDict = None
        for item in pInstance.TurretSystemOptionsList:
            if len(item) > 1 and item[0] == "Setup":
                dGenShipDict = item[1]
                break

        if dGenShipDict == None:
            return 1
        
        # update alert state

        if not dGenShipDict.has_key("AlertLevel") or dGenShipDict["AlertLevel"] == None:
            dGenShipDict["AlertLevel"] = pShip.GetAlertLevel()
        iType = dGenShipDict["AlertLevel"]

        inCombatM = (iType == 2)

        if inCombatM:
                sNewShipScript = None
                if pInstance.__dict__[oTurrets.name]["Setup"].has_key("AttackModel"):
                        sNewShipScript = pInstance.__dict__[oTurrets.name]["Setup"]["AttackModel"]

                elif pInstance.__dict__[oTurrets.name]["Setup"].has_key("NormalModel"):
                        sNewShipScript = pInstance.__dict__[oTurrets.name]["Setup"]["NormalModel"]

                if sNewShipScript != None:
                        ReplaceModel(pShip, sNewShipScript)
                        checkingReCloak(pShip)

        else:

                if pInstance.__dict__[oTurrets.name]["Setup"].has_key("NormalModel"):
                        sNewShipScript = pInstance.__dict__[oTurrets.name]["Setup"]["NormalModel"]
                        ReplaceModel(pShip, sNewShipScript)
                        checkingReCloak(pShip)

                #print "calling AlertMoveFinishTemporarilyAction --> Detach Parts"
                oTurrets.DetachParts(pShip, pInstance) # we hide turrets when not in alert mode, else we keep them

        turretTranslocation(pInstance, pShip.GetObjID(), iType)

        if inCombatM:
                oTurrets.SetBattleTurretListenerTo(pShip, 1) # Combat mode
        else:
                oTurrets.SetBattleTurretListenerTo(pShip, -1) # Not combat mode

        return 0
        

# called after a move, sets the current Rotation/Translation values to the final ones
def UpdateState(pAction, pShip, item, lStoppingTranslation):
        debug(__name__ + ", UpdateState")
        item[1]["currentPosition"] = lStoppingTranslation
        item[1]["curMovID"] = 0
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
                        pInstanceList.TGDoneIterating()
                        pInstanceList.TGDestroy()
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
                print __name__, " Error: Unable to find Hardpoint %s" % sHP
        pShip.UpdateNodeOnly()


def UpdateHardpointPositions(pAction, pShip, dHardpoints, iThisMovID):
        debug(__name__ + ", UpdateHardpointPositions")

	pInstance = findShipInstance(pShip)
	if not pInstance or not MoveFinishMatchId(pShip, pInstance, iThisMovID):
		return 0

        for sHP in dHardpoints.keys():
                UpdateHardpointPositionsTo(pShip, sHP, dHardpoints[sHP])
        return 0


# Set the parts to the correct alert state
def PartsForWeaponState(pShip, weaponsActive=None):        
        debug(__name__ + ", PartsForWeaponState")
        
        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return
        
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        pInstance = findShipInstance(pShip)
        iType = pShip.GetAlertLevel()
        iLongestTime = 0.0
        dHardpoints = {}

        oTurrets.SetBattleTurretListenerTo(pShip, 0)
        
        # try to get the last alert level
        for item in pInstance.TurretSystemOptionsList:
                if item[0] == "Setup":
                        dGenShipDict = item[1]
                        break

        # update alert state
        auxLevel = None
        if weaponsActive == 1 or iType == 2: 
            auxLevel = 2
        else:
            auxLevel = iType

        pSubsystem = pShip.GetShields()
        if pSubsystem and auxLevel > 0 and not pSubsystem.IsDisabled() and pSubsystem.IsOn():
            oTurrets.SetBattleTurretListenerTo(pShip, 1, -2)
        else:
            oTurrets.SetBattleTurretListenerTo(pShip, 0, -2)

        # check if the alert state has really changed since the last time
        if dGenShipDict["AlertLevel"] == auxLevel:
                return

        dGenShipDict["AlertLevel"] = auxLevel
        
        MovingProcess(pShip, pInstance, auxLevel, iLongestTime, dHardpoints, dGenShipDict)

# Set things for turret aiming when not in alert switch
def PartsForWeaponTurretState(pInstance, pShip, iShipID):        
        debug(__name__ + ", PartsForWeaponTurretState")
        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return

        pShip2 = GetShipFromID(iShipID)
        if not pShip2:
                #print __name__, ": TranslocRotating Error: Lost MAIN part"
                return 0

        for item in pInstance.TurretSystemOptionsList:
                if len(item) > 1 and item[0] == "Setup":
                        dGenShipDict = item[1]
                        break

        if dGenShipDict == None:
                return 1
        
        # update alert state

        if not dGenShipDict.has_key("AlertLevel") or dGenShipDict["AlertLevel"] == None:
                dGenShipDict["AlertLevel"] = pShip.GetAlertLevel()
        iType = dGenShipDict["AlertLevel"]

        inCombatM = (iType == 2)

        for item in pInstance.TurretSystemOptionsList:
                try:
                        if hasattr(item[0], "__class__") and item[0].__class__ == App.ShipClass:
                                aim1Item(item, iShipID, pShip=pShip2)
                                turretTranslocation(pInstance, iShipID, iType, warpDirty = 0, usualMove = 1, alreadyChecked = 1)
                except:
                        traceback.print_exc()


def turretTranslocation(pInstance, iShipID, iType, warpDirty=0, usualMove = 0, alreadyChecked = 0):
        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return

        if alreadyChecked == 0:
                pShip = GetShipFromID(iShipID)
                if not pShip:
                        #print __name__, ": Transloc Error: Lost MAIN part"
                        return 0

        for item in pInstance.TurretSystemOptionsList:
                try:
                        if hasattr(item[0], "__class__") and item[0].__class__ == App.ShipClass:

                                lStoppingTranslation = None
                                if usualMove and item[1].has_key("currentPosition"):
                                        lStoppingTranslation = item[1]["currentPosition"]
                                elif item[1].has_key("AttackPosition") and iType == 2:
                                        lStoppingTranslation = item[1]["AttackPosition"]
                                else:
                                        lStoppingTranslation = item[1]["Position"]

                                partTranslate(item, iShipID, lStoppingTranslation, warpDirty, usualMove)
                except:
                        traceback.print_exc()
        return 0

def JointAlertMoveFinishAction(pAction, pShip, pInstance, dHardpoints, iThisMovID, iType):
	UpdateHardpointPositions(pAction, pShip, dHardpoints, iThisMovID) 
	AlertMoveFinishTemporarilyAction(pAction, pShip, pInstance, iThisMovID, iType)
	return 0


def MovingProcess(pShip, pInstance, iType, iLongestTime, dHardpoints, dGenShipDict):
        # check if ship still exits
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        IncCurrentMoveID(pShip, pInstance)
        
        # start with replacing the Models
        PrepareShipForMove(pShip, pInstance)

        warpDirty = 0
        if pInstance.__dict__[oTurrets.name]["Setup"].has_key("WarpReload") and pInstance.__dict__[oTurrets.name]["Setup"]["WarpReload"] == 1:
            pInstance.__dict__[oTurrets.name]["Setup"]["WarpReload"] = 0
            warpDirty = 1

        thisMoveCurrentID = GetCurrentMoveID(pShip, pInstance)
        # iterate over every Turret
        for item in pInstance.TurretSystemOptionsList:
                if item[0] == "Setup":
                        # attack or cruise modus?
                        dHardpoints = {}
                        if iType == 2 and item[1].has_key("AttackHardpoints"):
                                dHardpoints = item[1]["AttackHardpoints"]
                        elif iType != 2 and item[1].has_key("Hardpoints"):
                                dHardpoints = item[1]["Hardpoints"]
                        
                        # setup is not a Turret
                        continue

                #This is a thing for warp changes, for some reason warp changes make the models not visible, so better reload them
                if warpDirty:
                    model = item[1]["sShipFile"]
                    if model:
                        ReplaceModel(item[0], model)
                    item[0].SetHidden(0)

                # set the id for this move
                iThisMovID = item[1]["curMovID"] + 1
                item[1]["curMovID"] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("AttackDuration"):
                        fDuration = item[1]["AttackDuration"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and iType == 2:
                        lStoppingTranslation = item[1]["AttackPosition"]
                else:
                        lStoppingTranslation = item[1]["Position"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingTranslation, lStoppingTranslation, dHardpoints)

                pSeq = App.TGSequence_Create()
                
                # do the move
                initialWait = 0.01 # In seconds (so 10 centiseconds)
                while(iTime < (fDuration + initialWait)):
                        if iTime == 0.0:
                                iWait = initialWait # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        theScriptToPerform = App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent, pShip)
                        if theScriptToPerform != None:
                                pSeq.AppendAction(theScriptToPerform, iWait)
                        else:
                                print __name__, ": failed to create script action for MovingProcess ", iTimeNeededTotal, iTime, iWait
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + round(iWait * 100.0)

                finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingTranslation)
                if finalLocalScriptAct:
                        pSeq.AppendAction(finalLocalScriptAct, 0.01)
                        pSeq.Play()
                else:
                        print __name__, ": Error while trying to perform final local action for MovingProcess"

                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = round(iTimeNeededTotal, 2)
                
        # finally detach?
        pShip = App.ShipClass_GetObjectByID(None, pShip.GetObjID())
        if not pShip:
                return

        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "JointAlertMoveFinishAction", pShip, pInstance, dHardpoints, thisMoveCurrentID, iType), iLongestTime + 0.01)
        pSeq.Play()

        return 0


# Set the parts for Warp state
def StartingWarp(pObject, pEvent):
        debug(__name__ + ", StartingWarp")
        
        if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                pObject.CallNextHandler(pEvent)
                return
        
        pShip = App.ShipClass_GetObjectByID(None, pObject.GetObjID())
        pInstance = findShipInstance(pShip)
        iLongestTime = 0.0
        oTurrets.SetBattleTurretListenerTo(pShip, 0)
        IncCurrentMoveID(pShip, pInstance)
        dHardpoints = {}


        # first replace the Models
        PrepareShipForMove(pShip, pInstance)
        
        warpDirty = 0
        if pInstance.__dict__[oTurrets.name]["Setup"].has_key("WarpReload") and pInstance.__dict__[oTurrets.name]["Setup"]["WarpReload"] == 1:
            #pInstance.__dict__[oTurrets.name]["Setup"]["WarpReload"] = 0
            warpDirty = 1

        thisMoveCurrentID = GetCurrentMoveID(pShip, pInstance)

        for item in pInstance.TurretSystemOptionsList:
                # setup is not a Turret
                if item[0] == "Setup":
                        if item[1].has_key("WarpHardpoints"):
                                dHardpoints = item[1]["WarpHardpoints"]
                        continue

                # The warp changes thing
                if warpDirty:
                    model = item[1]["sShipFile"]
                    if model:
                        ReplaceModel(item[0], model)
                    item[0].SetHidden(0)

                # set the id for this move
                iThisMovID = item[1]["curMovID"] + 1
                item[1]["curMovID"] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("WarpDuration"):
                        fDuration = item[1]["WarpDuration"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("WarpPosition"):
                        lStoppingTranslation = item[1]["WarpPosition"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingTranslation, lStoppingTranslation, {})
                pSeq = App.TGSequence_Create()
                
                # do the move
                initialWait = 0.1 # In seconds (so 10 centiseconds)
                while(iTime < (fDuration + initialWait)):
                        if iTime == 0.0:
                                iWait = initialWait # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        theScriptToPerform = App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent, pShip)
                        if theScriptToPerform != None:
                                pSeq.AppendAction(theScriptToPerform, iWait)
                        else:
                                print __name__, ": failed to create script action for StartingWarp ", iTimeNeededTotal, iTime, iWait
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + round(iWait * 100.0)

                finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingTranslation)
                if finalLocalScriptAct:
                        pSeq.AppendAction(finalLocalScriptAct, 0.01)
                        pSeq.Play()
                else:
                        print __name__, ": Error while trying to perform final local action for StartingWarp"

                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = round(iTimeNeededTotal, 2)
                
        # finally detach
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints, thisMoveCurrentID), iLongestTime)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WarpStartMoveFinishAction", pShip, pInstance, thisMoveCurrentID), 2.0)
        pSeq.Play()

        pObject.CallNextHandler(pEvent)


def GetStartWarpNacellePositions(pShip):
        ret = []
        dHardpoints = {}
        
        if not FoundationTech.dShips.has_key(pShip.GetName()):
                return []
        
        pInstance = findShipInstance(pShip)
        if hasattr(pInstance, "TurretSystemOptionsList"):
                for item in pInstance.TurretSystemOptionsList:
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
        
        pInstance = findShipInstance(pShip)
        iLongestTime = 0.0

        oTurrets.SetBattleTurretListenerTo(pShip, 0) # We clearly indicate we are in combat mode, but doing a thing
        IncCurrentMoveID(pShip, pInstance)
        dHardpoints = {}
        
        # first replace the Models
        PrepareShipForMove(pShip, pInstance)
        
        warpDirty = 0
        if pInstance.__dict__[oTurrets.name]["Setup"].has_key("WarpReload") and pInstance.__dict__[oTurrets.name]["Setup"]["WarpReload"] == 1:
            #pInstance.__dict__[oTurrets.name]["Setup"]["WarpReload"] = 0
            warpDirty = 1

        thisMoveCurrentID = GetCurrentMoveID(pShip, pInstance)

        dGenShipDict = None
        iType = pShip.GetAlertLevel()
        
        # try to get the last alert level
        for item in pInstance.TurretSystemOptionsList:
                if len(item) > 1 and item[0] == "Setup":
                        dGenShipDict = item[1]
                        break

        if dGenShipDict != None and dGenShipDict.has_key("AlertLevel") and dGenShipDict["AlertLevel"] != None:
                iType = dGenShipDict["AlertLevel"]

        for item in pInstance.TurretSystemOptionsList:
                # setup is not a Turret
                if item[0] == "Setup":
                        dHardpoints = {}
                        if item[1].has_key("WarpHardpoints"):
                                dHardpoints = item[1]["WarpHardpoints"]
                        continue

                #The warp changes thing
                if warpDirty:
                    model = item[1]["sShipFile"]
                    if model:
                        ReplaceModel(item[0], model)
                    item[0].SetHidden(0)


                # set the id for this move
                iThisMovID = item[1]["curMovID"] + 1
                item[1]["curMovID"] = iThisMovID
        
                fDuration = 200.0
                if item[1].has_key("WarpDuration"):
                        fDuration = item[1]["WarpDuration"]
                
                # Translation
                lStartingTranslation = item[1]["currentPosition"]
                lStoppingTranslation = lStartingTranslation
                if item[1].has_key("AttackPosition") and iType == 2:
                                lStoppingTranslation = item[1]["AttackPosition"]
                else:
                        lStoppingTranslation = item[1]["Position"]
        
                iTime = 0.0
                iTimeNeededTotal = 0.0
                oMovingEvent = MovingEvent(pShip, item, fDuration, lStartingTranslation, lStoppingTranslation, dHardpoints)
                pSeq = App.TGSequence_Create()
                
                # do the move
                initialWait = 0.1 # In seconds (so 10 centiseconds)
                while(iTime < (fDuration + initialWait)):
                        if iTime == 0.0:
                                iWait = initialWait # we wait for the first run
                        else:
                                iWait = 0.01 # normal step
                        theScriptToPerform = App.TGScriptAction_Create(__name__, "MovingAction", oMovingEvent, pShip)
                        if theScriptToPerform != None:
                                pSeq.AppendAction(theScriptToPerform, iWait)
                        else:
                                print __name__, ": failed to create script action for ExistingWarp ", iTimeNeededTotal, iTime, iWait
                        iTimeNeededTotal = iTimeNeededTotal + iWait
                        iTime = iTime + round(iWait * 100.0)

                finalLocalScriptAct = App.TGScriptAction_Create(__name__, "UpdateState", pShip, item, lStoppingTranslation)
                if finalLocalScriptAct:
                        pSeq.AppendAction(finalLocalScriptAct, 0.01)
                        pSeq.Play()
                else:
                        print __name__, ": Error while trying to perform final local action for ExitingWarp"

                # iLongestTime is for the part that needs the longest time...
                if iTimeNeededTotal > iLongestTime:
                        iLongestTime = round(iTimeNeededTotal, 2)
                
        # finally detach
        pSeq = App.TGSequence_Create()
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "UpdateHardpointPositions", pShip, dHardpoints, thisMoveCurrentID), iLongestTime)
        pSeq.AppendAction(App.TGScriptAction_Create(__name__, "WarpExitMoveFinishAction", pShip, pInstance, thisMoveCurrentID), 2.0)
        pSeq.Play()
        
        return 0


def DeleteObjectFromSet(pSet, sObjectName):
        if not MissionLib.GetShip(sObjectName, None, 1):
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
