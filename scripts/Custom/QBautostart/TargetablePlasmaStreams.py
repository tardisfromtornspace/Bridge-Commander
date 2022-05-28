from bcdebug import debug
###################################################################
# Targetable Plasma Streams                             
#   Allows you to ignite a plasma trail                 
#                                                       
#       Created by BCS:TNG                              
#               v0.0.1 Lost_Jedi                        
#                   - First Gen Tracking Engine             
#                   - NanoFX Plasma.py Modded               
#                   - Dynamic Class Creation                
#               v0.0.2 Lost_Jedi                        
#                   - Bug Fixed Tracking Engine             
#                   - Arrays fixed                          
#                   - NanoFX Explosion Code Created         
#                   - Tracking Engine Handles Multiple      
#                       objects                             
#                   - Basic Ignition System                 
#               v0.0.3 Lost_Jedi                        
#                   - Game Doesn't Crash after explosion    
#                   - Firepoints Removed on death           
#                   - Bug Fixed Tracker some more           
#                   - Basic Ignition System *Removed*       
#                   - Started testing different methods     
#                       of ingition systems                 
#               v0.0.4 Lost_Jedi                        
#                   - FirePointBomb Class Created           
#                   - Total Redesign of Ignition System     
#                   - Get a girlfriend....              
#               v0.0.5 Lost_Jedi
#                   - Complety different ignition system   
#                   - Wow...Talk about optimised ;)         
#                   - Code actually works                   
#                   - Little to no slowdown now :D
#               v0.0.6 Lost_Jedi
#                   - Random Throw put on model when stream hits engine
#               v0.0.7 by USS Sovereign
#                   - Fixed the bug where the game crashed
#                   - Made an foundation override of NanoFX's plasma.py
#                   - Made an foundation override over NanoFX's explosions.py
#                   - Added a mutator to the mod
#                   - Even with the fix to the ExpFX.py the game crashed so
#                     a new bugfix is also involved by increasing radius of the probes
#               v0.0.8 Lost_Jedi
#                   - Textures now NOT loaded by NanoFX
#                   - Flicker added to ship when explosion hits
#                   - Changed the way the EXPFX overrides work to leave functionality
#                       NanoFX2 *not working but code is there*
#                   - Dynamically sized streams (not based on ship size but on how long they have been igniting)
#                   - More realistic ignition duration times
#                   - Size increases as it goes up the stream
#                   - Found a way to stop the plasma from venting on that nacelle
#               v0.0.9 Lost_Jedi
#                   - New Explosion on Nacelle
#                   - Debris connected to set, sparks connected to ship
#                   - Random Non Model damage applied to engine
#                   - Stop Player Streams function (for external usage)
#                   - Added option ro toggle visible damage on/off
#                   - ooo yea and visible damage added ;)
#               v0.1.0 Lost_Jedi
#                   - Different randomised levels of damage
#                   - Better *scorch mark* damage effects
#               v0.1.1 Lost_Jedi
#                   - Mini Ruptures
#               v0.1.2 Lost_Jedi
#                   - AI goes after plasma streams *Basic* Thanks for the idea Spanner and
#                       thanks to MLeo for the neutral group fix.
#                   - A few damage fixes to prevent the ship from getting destroyed by application of visible damage alone
#                   - ZeroError Division fixed (thanks MLeo for the error report)
#
#               v1.3 Wowbagger
#                   - Unalaterally changed version numbering system.
#                   - Unalaterally added a space between versions in the version history.
#                   - Unalaterally invaded the sovereign (no pun intended) nation of Iraq.
#                   - Theoretically fixed wandering firepoints.
#                   - Fixed plasma level carryover problem when player changes ships.
#                   - Corrected spelling of "Vacuum Cleaner" in source code.
#                   - Reminded self to ask LJ about the use of MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet() when self.LocalFirePoint.GetContainingSet().RemoveObjectFromSet() looks like it would be more efficient.
#                   - Unalaterally raised the probability for serious damage (from 2.5/10 to 5.5./10).  I hope no one minds.  If you go to all the work of blowing open a plasma vent, I would hope for serious payoff.  :evilgrin: Is that okay?
#
# TODO:     -Fix the new override system *sorry sovvie :( * -- LJ *think this is done now*
#		-Do Mini Streams properly
#               v1.4 -- USS Sovereign
#                    - updated it so that it doesn't use probe.py anymore
#                                                       
###################################################################

import App
import MissionLib
import Foundation
import loadspacehelper
import Libs.LibEngineering
import math     # <--- Oooooo!

import Custom.NanoFXv2.ExplosionFX.ExpFX
import Custom.NanoFXv2.NanoFX_ScriptActions
import Custom.NanoFXv2.NanoFX_Lib

# Mod Info Block.  Used for MP loading.
MODINFO = {     "Author": "\"BCS:TNG\" <http://bcscripterstng.forumsplace.com/>",
                "Version": "1.3",
                "License": "GPL",
                "Description": "Targetable Plasma Streams",
                "needBridge": 0
            }
    
# Setup Constants
FALSE = 0
TRUE = 1

######################################################################################
DAMAGESHIP = TRUE                   # Turn off visible damage like broken nacelles etc (just for Phaser) ;-)
DEBUGMODE = FALSE                   # Debug?
MAX_EXPLOSION_PLUMES = 100          # Tracking Resolution
UPDATE_TIME = 0.2                  # Timer Resuolution
AI_ATTACK_STREAMS = TRUE            # Should the AI go after your plasms streams TRUE or FALSE
SET_STREAM_TO_PARENT_TARGET = TRUE  # When you blow up a stream, do you want the target to be set to the parent ship
GFX_FOLDER = 'scripts/Custom/QBautostart/TPSDATA/Gfx/'    # Path to the GFX
REMOVE_POINTER_FROM_SET = 190
FIREPOINT_SHIP = "BigFirepoint"
######################################################################################

# cout debug function.  Helps to make the console tidy.
def cout(sData):
    debug(__name__ + ", cout")
    if DEBUGMODE == TRUE:
        print "TPS" + str(sData)
    return TRUE

# Load the Script
def init():

    # as we all agreed, disable these mods in MP to prevent cheating ;) -- USS Sovereign
    debug(__name__ + ", init")
    if App.g_kUtopiaModule.IsMultiplayer() and not App.g_kUtopiaModule.IsHost():
                return
    # by USS Sovereign, checks if the mutator is active if it isn't it won't load and execute :)
    if not Libs.LibEngineering.CheckActiveMutator("BCS:TB: Targetable Plasma Streams"):
                return
            
    # Load the new GFX
    LoadTPSGfx()
    # Start the timer! With another timer!
    ScanTimeTimer = MissionLib.CreateTimer(ScanTimeEvent, __name__ + ".UpdateArray", App.g_kUtopiaModule.GetGameTime() + 0.2, 0, 0)
    return


class PlasmaTrail:
    def __init__(self):
                    debug(__name__ + ", __init__")
                    self.pExplosionPoints = []                  #  Create an array to hold the points
                    
                    self.ParentEmittingObject = None
                    self.pEngineToTrack = None                  #  Create the variable
                    self.iMaxTimetoTrack = 0.00                 #  Maximum time before class stops tracking (i.e the vent seals)

                    self.LocalFirePointName = None              #  Local FirePoint Name
                    self.LocalFirePoint = None                  #  Local FirePoint Object

                    self.Explosion = FirePointBomb()            #  Explosion

                    self.bActive = FALSE                        #  Has the class finished
                    self.bIgniting = FALSE                      #  Is the stream blowing up?
                    self.bTracking = FALSE                      #  Is the stream tracking
                    self.bTakenOver = FALSE                     #  Has this class been taken over?

                    self.iBlown = 0                             #  Number to reduce distance by
                    self.fSpeedCounter = 0.00

                    self.pPlasmaSequence = None                 #  Plasma Sequence created by NanoByte's code

                    self.pEventHandler = App.TGPythonInstanceWrapper()  # Setup for using class-based event handlers
                    self.pEventHandler.SetPyWrapper(self)               # Sets class-based handlers to look within this class instance for the relevant function.

                    return
                
    def SetSequence(self,pSequence):
                    debug(__name__ + ", SetSequence")
                    self.pPlasmaSequence = pSequence
                    return

    def SetTrackingObject(self, pEmittingObject, iLifeTime, pParent):
                    debug(__name__ + ", SetTrackingObject")
                    global iPlasmaArray 
                    # Sets the class to track an object...
                    self.ParentEmittingObject = pParent         # Set the emitting ship
                    self.pEngineToTrack = pEmittingObject       # Set the emitting object on that ship
                    self.iMaxTimetoTrack = iLifeTime            # How long is it to vent for?
                    
                    self.bActive = TRUE                         # The Class is being used so don't delete
                    self.bIgniting = FALSE                      # The Class is not blowing up yet
                    self.bTracking = TRUE                       # Enable Tracking


                    # Setup the firepoint to target the stream
                    self.LocalFirePointName = "Plasma Stream Firepoint" + str(iPlasmaArray) + "_t"      #  Create the next avb Firepoint Name
                    self.LocalFirePoint = MissionLib.GetShip(self.LocalFirePointName)   #  Try to see if it already exists

                    if not self.LocalFirePoint:                                         #  If it doesn't exist already then
                            cout("Creating Classed Plasma Firepoint")                       
                            pSet = self.ParentEmittingObject.GetContainingSet()             # Get the set of the parent object and then create the firepoint
                            self.LocalFirePoint = loadspacehelper.CreateShip(FIREPOINT_SHIP, pSet, self.LocalFirePointName, None)   #Firepoint    # Probe
                            ### Make the fp friendly so the enemy can target it
                            if AI_ATTACK_STREAMS == TRUE:
                                ### Make the AI go after the streams
                                AddtoTeam(self.LocalFirePoint,self.ParentEmittingObject)
                           
                            self.LocalFirePoint.SetTargetable(1)                                    # let people shoot sh*t out of this one!
                            self.LocalFirePoint.EnableCollisionsWith(self.ParentEmittingObject, 0)  # Don't destroy me on vent!
                            App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_OBJECT_EXPLODING, self.pEventHandler, "KillClass", self.ParentEmittingObject)    # If the parent is destroyed, kill the firepoint.  (self.ParentEmittingObject is the argument for App.OBJECT_EXPLODING.)

                    # Build the array
                    for iTemp in range(MAX_EXPLOSION_PLUMES + 1):
                            cout("Buliding array ... " + str(iTemp))
                            self.pExplosionPoints.append(App.TGPoint3())
                            self.pExplosionPoints[iTemp] = self.pEngineToTrack.GetWorldLocation()   # Put all points to the pos of the engine

                    self.pExplosionPoints[0] = App.TGPoint3()                                   # Do the 0 point
                    self.pExplosionPoints[0] = self.pEngineToTrack.GetWorldLocation()

                    # Timer Stuff
                    self.iMaxTimetoTrack = App.g_kUtopiaModule.GetGameTime() + iLifeTime        # Set the kill time when it finishes venting
                    return TRUE
                
    def TrackObject(self, pBufferVar = None):   # Gave it a buffer because the timer kept giving it an extra variable?!      
                    # Track the object
                    
                    if(self.bActive == FALSE):              # This class instance should not be tracking
                            return

                    if self.ParentEmittingObject.IsDead() == TRUE or self.ParentEmittingObject.IsDying() == TRUE:
                            debug(__name__ + ", TrackObject")
                            cout("Parent Ship/Object is dead so stop tracking")
                            self.KillClass()                    # If the object is dead,  therefore an object anymore, put this here to prevent crashes
                            return

                    if self.bTracking == TRUE:                                                                  #  Is the stream tracking
                            self.ShufflePoints()                                                                    #  Carry on trekking...oo..i mean tracking
                            if self.LocalFirePoint.IsDead() == FALSE:                                               #  Cos the FP is dead don't bother to move it
                                self.LocalFirePoint.SetTranslate(self.pExplosionPoints[MAX_EXPLOSION_PLUMES - 5])   #  Move the tracking firepoint          

                    if self.bIgniting == TRUE:
                            self.IgnitePlasma()                 # We are blowing up

                    return TRUE
        
    def ShufflePoints(self):
                    # Shuffles the array along one and enters a new point passed through the function as nPointValue
                    debug(__name__ + ", ShufflePoints")
                    iPointer = MAX_EXPLOSION_PLUMES
                    while(iPointer > 0):
                        self.SwapValues((iPointer-1),iPointer)
                        iPointer = iPointer -1
                    
                    # As MLeo says, "Premature Optimisation is the root of all evil."
                    if self.pEngineToTrack:
                        self.pExplosionPoints[0].SetXYZ(self.pEngineToTrack.GetWorldLocation().GetX(),self.pEngineToTrack.GetWorldLocation().GetY(),self.pEngineToTrack.GetWorldLocation().GetZ())#
                    debug(__name__ + ", ShufflePoints Done")
                    return TRUE

    def SwapValues(self, x, y):
                    # Swaps two TGPoint3 array values
                    vTemp = App.TGPoint3()
                    vTemp.SetXYZ(self.pExplosionPoints[x].GetX(),self.pExplosionPoints[x].GetY(),self.pExplosionPoints[x].GetZ())
                    self.pExplosionPoints[x].SetXYZ(self.pExplosionPoints[y].GetX(),self.pExplosionPoints[y].GetY(),self.pExplosionPoints[y].GetZ())
                    self.pExplosionPoints[y].SetXYZ(vTemp.GetX(),vTemp.GetY(),vTemp.GetZ())
                    return TRUE

    def TakeOverTracker(self):
                    # Takes over the firepoint
                    # This is called when the other firepoint has been destroyed.
                    # Tracking has NOT stopped.
                        debug(__name__ + ", TakeOverTracker")
                        if self.bTakenOver == FALSE:
                            # Set the player target to be the ship
                            pPlayer = MissionLib.GetPlayer()
                            if pPlayer:
                                if pPlayer == self.ParentEmittingObject:
                                    # don't target myself
                                    cout("Trying to target myself??!")
                                else:
                                    # ok target the ship
                                    if SET_STREAM_TO_PARENT_TARGET == TRUE:
                                        ### Set the target to the parent ship
					debug(__name__ + ", TakeOverTracker SetTarget")
                                        pPlayer.SetTarget(self.ParentEmittingObject.GetName())
                                        cout("Target set to player")
                                
                        # Now do the **real** stuff :P
                        self.bTakenOver = TRUE
                        self.bIgniting = TRUE
                        self.Explosion.Create(self.ParentEmittingObject)
                        self.Explosion.Move(self.pExplosionPoints[MAX_EXPLOSION_PLUMES - 5])    # Move the tracking firepoint
                        self.ShufflePoints()                                                    # Carry on trekking...oo..i mean tracking  

    def IgnitePlasma(self):
                    # This ignites the plasma for that ship
                    
                    # Get the explosion class
                    debug(__name__ + ", IgnitePlasma")
                    if not self.Explosion:                                  # Error protection .. oooo
                        self.Explosion = FirePointBomb()                    # Reccreate if necessary
                        self.Explosion.Create(self.ParentEmittingObject)    # Setup

                    fExpSize = self.fSpeedCounter + 1
                    self.Explosion.Move(self.pExplosionPoints[MAX_EXPLOSION_PLUMES - int(round(self.iBlown,0))],fExpSize)       # Move the tracking firepoint
                    self.ShufflePoints()                                    #  Carry on trekking...oo..i mean tracking   

                    ### Control Explosion size
                    if self.fSpeedCounter < 1.25:                         # 100 / limit which in this case is 80
                        self.fSpeedCounter = self.fSpeedCounter + 0.05
                        
                    ### Carry on counting down the array
                    self.iBlown = self.iBlown + 0.3 + self.fSpeedCounter

                    ### EVENT FOR PLASMA REACHING ENGINE
                    if MAX_EXPLOSION_PLUMES - self.iBlown < 0:  
                        cout("Done Exploding now - i.e. its hit the engine")
                        self.bIgniting = FALSE
                        self.bActive = FALSE                        # Remove firepoint flag
                        self.Explosion.Destroy()                    # Remove the explosion

                        ### Create a sequence ###
                        pSequence = App.TGSequence_Create ()
                        self.LocalFirePoint.SetTargetable(0)        # Hide the firepoint
                        
                        ### Warp Engine Stuff ###
                        # Stop the plasma venting on that engine
                        #if self.pPlasmaSequence:
                        #    self.pPlasmaSequence.Abort()            # Abort the sequence
                        #    cout("NanoBytes sequence stopped")
                            
                        # Make a large engine explosion on the engine
                        LargeEngineExplode(self.ParentEmittingObject, self.pEngineToTrack)
                        # Throw the ship forward and tilt it down some CRAZY!!!!!1111oneoneone
                        SetCrazyRotation(self.ParentEmittingObject)
                        # Flicker the glows
                        pSequence.AddAction(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(self.ParentEmittingObject, 2.50), App.TGAction_CreateNull(), 1.0)
                            
                        pSequence.Play()
                        return      
                    
                    return TRUE

    def KillClass(self, bKillSequence = FALSE):
                    # Try to remove the firepoints
                    debug(__name__ + ", KillClass")
                    print "killing the player class instance"
                    try:
                        MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet(self.LocalFirePointName)
			MPDeleteFirePoint(self.LocalFirePointName)
                        #self.Explosion.Destroy()
                    except:
                        cout("Could not Kill Plasma stream tracker")
                        
                    # Kill the class
                    self.pExplosionPoints = []                  #  Create an array to hold the points
                    
                    self.ParentEmittingObject = None
                    self.pEngineToTrack = None                  #  Create the variable
                    self.iMaxTimetoTrack = 0.00                 #  Maximum time before class stops tracking (i.e the vent seals)

                    self.LocalFirePointName = None              #  Local FirePoint Name
                    self.LocalFirePoint = None                  #  Local FirePoint Object

                    #self.Explosion = FirePointBomb()            #  Explosion

                    self.bActive = FALSE                        #  Has the class finished
                    self.bIgniting = FALSE                      #  Is the stream blowing up?
                    self.bTracking = FALSE                      #  Is the stream tracking
                    self.bTakenOver = FALSE                     #  Has this class been taken over?

                    self.iBlown = 0                             #  Number to reduce distance by
                    self.fSpeedCounter = 0.00
                    
                    #if bKillSequence == TRUE:
                        #if self.pPlasmaSequence:
                            #self.pPlasmaSequence.Abort()        # This kills the actual stream    
                    
                    return TRUE

# The end of the class

###########################################################################################################

global aPlasmaArray, iPlasmaArray   # Array of plasma tracking things
aPlasmaArray = []                   # Array
iPlasmaArray = -1                   # Counter

global ScanTimeTimer, ScanTimeEvent # Timers
ScanTimeTimer = None                # Object
ScanTimeEvent = Libs.LibEngineering.GetEngineeringNextEventType()    # Event


# Appends the list with a new tracer
def AppendPlasmaTracker(pEmittingObject = None, iLifeTime = None, pParent = None, pSequence = None):
                debug(__name__ + ", AppendPlasmaTracker")
                if not Libs.LibEngineering.CheckActiveMutator("BCS:TB: Targetable Plasma Streams"):
                    return
                global aPlasmaArray, iPlasmaArray
                if pParent == None:
                    cout("No parent ship passed")                           # No parent ship passed
                    return
                if pParent.IsDead() == TRUE or pParent.IsDying() == TRUE:
                    cout("Didn't create tracker as object is dead(ing).")   # Because the ship is dying(dead) don't track cos it doesn't exist
                    return
                iPlasmaArray = iPlasmaArray + 1                                                     # Increment pointer
                aPlasmaArray.append(PlasmaTrail())                                                  # Create
                aPlasmaArray[iPlasmaArray].SetTrackingObject(pEmittingObject, iLifeTime, pParent)   # Setup
                aPlasmaArray[iPlasmaArray].SetSequence(pSequence)                                   # Set sequence

                cout("Created Tracking Class")
                return TRUE

def UpdateArray(pObject = None, pEvent = None):
                debug(__name__ + ", UpdateArray")
                global aPlasmaArray, iPlasmaArray
                # DO THE TRACKING
                #######################
                ilTime = App.g_kUtopiaModule.GetGameTime()      # Only do this once to make the script faster
                for iCount in range(len(aPlasmaArray)):
                    if(aPlasmaArray[iCount].bActive == TRUE):   # The time out has not been triggered
                        if aPlasmaArray[iCount].LocalFirePoint.IsDead() == TRUE or aPlasmaArray[iCount].LocalFirePoint.IsDying() == TRUE and aPlasmaArray[iCount].bTakenOver == FALSE:
                            # Ignite plasma
                            #aPlasmaArray[iCount].IgnitePlasma()
                            #aPlasmaArray[iCount].TrackObject()
                            aPlasmaArray[iCount].TakeOverTracker()
                            aPlasmaArray[iCount].TrackObject()
                        else:
                            # Continue to track
                             aPlasmaArray[iCount].TrackObject()

                # DO MESSAGES
                #######################
                # Loops through all the elements
                for iCount in range(len(aPlasmaArray)):
                    if(aPlasmaArray[iCount].bActive == TRUE):                       # The time out has not been triggered
                        if(ilTime >= aPlasmaArray[iCount].iMaxTimetoTrack):         # Check to see if this index needs to be removed
                            cout("Remove Plasma Firepoint")
                            aPlasmaArray[iCount].bActive = FALSE                    # Remove the class
                            RemoveObject(iCount)
                            aPlasmaArray[iCount].KillClass()
                
                ScanTimeTimer = MissionLib.CreateTimer(ScanTimeEvent, __name__ + ".UpdateArray", App.g_kUtopiaModule.GetGameTime() + UPDATE_TIME, 0, 0)
		debug(__name__ + ", UpdateArray Done")
                return TRUE

### Remove a firepoint
def RemoveObject(iIndex = -1):
                debug(__name__ + ", RemoveObject")
                global aPlasmaArray
                # Unselect the ship from being tracked
                cout("Removing Plasma firepoint")
                if iIndex == -1:
                    cout("RemoveObject not passed an index")
                    return FALSE
                if not MissionLib.GetPlayer():
                    return
                try:
                    MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet(aPlasmaArray[iIndex].LocalFirePointName)   # Remove the firepoint
		    MPDeleteFirePoint(aPlasmaArray[iIndex].LocalFirePointName)
                except:
                    pass
                
                return TRUE

### This stops the player from venting plasma...
def StopPlayerStreams():
                debug(__name__ + ", StopPlayerStreams")
                global aPlasmaArray
                # Stops any streams that are venting from the player
                pPlayer = App.Game_GetCurrentPlayer()
                for iCount in range(len(aPlasmaArray)):
                    if(aPlasmaArray[iCount].bActive == TRUE):
                        #print str(iCount) + " Active"
                        ## This next line is offically my worst line of code ever :D - but it works! :P
                        if str(aPlasmaArray[iCount].ParentEmittingObject) == str(pPlayer):
                            #print str(iCount) + " Active and same as player"
                            aPlasmaArray[iCount].KillClass(TRUE)
                            #print str(iCount) + " Dead now sow whats the problem?"
                return
                                

###########################################################################################################
global iExplosionFirePointNameCounterThing
iExplosionFirePointNameCounterThing = -1        # Counter to give unique names

class FirePointBomb:
    def __init__(self):
        debug(__name__ + ", __init__")
        self.fp1 = None         # Firepoint 1
        self.fp1Name = None     # Firepoint 1 Name
        self.pParent = None     # Parent Ship AGAIN! (this is here to get the right colour for the trail really)
        
    # Creates the firepoints
    def Create(self, pParent):
        debug(__name__ + ", Create")
        global iExplosionFirePointNameCounterThing
        iExplosionFirePointNameCounterThing = iExplosionFirePointNameCounterThing +1

        pSet = pParent.GetContainingSet()
        
        self.fp1Name = "EFP Firepoint" + str(iExplosionFirePointNameCounterThing) + "_t"
        self.fp1 = MissionLib.GetShip(self.fp1Name)
        if not self.fp1:
            # Not already created so create it
            # so that we don't have to overwrite probe.py 
            self.fp1 = loadspacehelper.CreateShip(FIREPOINT_SHIP, pSet, self.fp1Name, None)   #Firepoint
            self.fp1.SetTargetable(0)                                   # Hide it from view
            self.fp1.EnableCollisionsWith(pParent, 0)                   # Don't destroy parent (but keep other ships getting hurt)
            self.pParent = pParent 
        return
    
    # Remove the firepoints
    def Destroy(self):
        debug(__name__ + ", Destroy")
        try:
            # .SetDeleteMe(1)
            MissionLib.GetPlayer().GetContainingSet().RemoveObjectFromSet(self.fp1Name)   # Remove the firepoint
	    MPDeleteFirePoint(self.fp1Name)
            self.fp1 = None
        except:
            pass
            cout("Error on removal of explosion firepoints")
        return
    
    # move the firepoints
    def Move(self,vPoint, fExpSize = 2):
        # move the firepoints
        debug(__name__ + ", Move")
	self.fp1 = App.ShipClass_GetObjectByID(None, self.fp1.GetObjID())
	if self.fp1:
        	self.fp1.SetTranslate(vPoint)
        	CreateTrailExp(self.fp1,self.pParent,fExpSize)
        return

    def JustMove(self,vPoint):
        # move the firepoint
        debug(__name__ + ", JustMove")
	self.fp1 = App.ShipClass_GetObjectByID(None, self.fp1.GetObjID())
	if self.fp1:
        	self.fp1.SetTranslate(vPoint)
        return
    
    def JustExplodeLarge(self):
        # blow up the firepoint
        debug(__name__ + ", JustExplodeLarge")
        CreateTrailExp(self.fp1,self.pParent,5)
        return

################################################################################### 
# Add a ship to your team 
def AddtoTeam(pNewShip,pTeamedShip): 
    ### Add pNewShip to the team of pTeamedShip 
    debug(__name__ + ", AddtoTeam")
    pMission = MissionLib.GetMission() 
    pFriendlies = pMission.GetFriendlyGroup() 
    pEnemies = pMission.GetEnemyGroup() 
    pGroup = pMission.GetNeutralGroup()             #<<<< 
    ### Set the pGroup to which ever side our pTeamedShip is on 
    if pFriendlies.IsNameInGroup(pTeamedShip.GetName()): 
            ### We are a friendly group so set the group to friendlys 
            pGroup = pMission.GetFriendlyGroup() 
    if pEnemies.IsNameInGroup(pTeamedShip.GetName()): 
            ### We are a friendly group so set the group to enemys 
            pGroup = pMission.GetEnemyGroup() 

    ### If the pGroup exists then 
    if pGroup: 
        ### Add the ship to the group 
        pGroup.AddName(pNewShip.GetName()) 
        return TRUE 
    return FALSE
    
###################################################################################
# Create a NanoFX Explosion on the point
def CreateTrailExp(pPoint, pShip, fExpRadius = 1.0):  
    debug(__name__ + ", CreateTrailExp")
    fPlasmaColor = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "PlasmaFX")   # Get the nice colours for the correct plasma
    if fPlasmaColor == None:
        sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)                    # Can't find so default
        fPlasmaColor = Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)

    fRed2    = fPlasmaColor[0]  # R
    fGreen2  = fPlasmaColor[1]  # G
    fBlue2   = fPlasmaColor[2]  # B

    pSet = pPoint.GetContainingSet()                                    # Get the set for the probe					
    pSequence = App.TGSequence_Create()                                 # Create a scene .. hehehe
    pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pPoint.GetNode())   # Cast the probe to a temp object
    if not pSet:
	    return FALSE
    pAttachTo = pSet.GetEffectRoot()                                    # Set the explosion object to be part of the grid
    
    vEmitPos = App.NiPoint3(0, 0, 0)
    vEmitDir = App.NiPoint3(1, 1, 1)
    fSize     = fExpRadius              # Explosion Radius 1.5 is about right :)
    sFile     = ChooseRandomTexture()
    
    if not sFile:
        return FALSE
    
    pSound = Custom.NanoFXv2.ExplosionFX.ExpFX.CreateNanoSoundSeq(pPoint, "ExpMedSfx")
    pSequence.AddAction(pSound)
    
    pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pAttachTo, fSize,fLifeTime = 1.0, fRed = fRed2, fGreen = fGreen2, fBlue = fBlue2)
    pSequence.AddAction(pExplosion)
    
    pSequence.Play()    # PLAY!!
    return TRUE

###################################################################################
# Create a Large explosion with all the trimmings on this ships engine (Customised NanoFX2 code)
def LargeEngineExplode(pShip, pWarpEngine):
        debug(__name__ + ", LargeEngineExplode")
        pShip.SetInvincible(1)
        
        pSequence = App.TGSequence_Create()
        ### Setup for Effect ###
        pSet = pShip.GetContainingSet()
        pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
        pShipNode = pShip.GetNode()
        pAttachTo = pSet.GetEffectRoot() 
        vEmitPos  = pWarpEngine.GetPosition()
        vEmitDir  = App.NiPoint3(1, 1, 1)
        fSize     = pShip.GetRadius() * 0.50
	###
        pSound = Custom.NanoFXv2.ExplosionFX.ExpFX.CreateNanoSoundSeq(pShip, "ExpMedSfx")
        pSequence.AddAction(pSound)
        
        # little Defiant fix: just don't crash with small objects, please. -- Sweet work with that Defiant, LJ
        if pShip.GetRadius() < 0.1:
                return pSequence

        ### Create 4 explosions of sparks, particles and textures 
        for i in range(4):
            ### Get a different texture for each itteration of the exlosion
            sFile     = Custom.NanoFXv2.ExplosionFX.ExpFX.GetNanoGfxFile("ExplosionGfx", "scripts/Custom/NanoFXv2/ExplosionFX/Gfx/Explosions/")
            ### Create a visble explsion that hangs round the warp engine (attached to pShipNode)
            pExplosion = Custom.NanoFXv2.NanoFX_ScriptActions.CreateControllerFX(sFile, pEmitFrom, pShipNode, fSize + (i* 0.3) , vEmitPos, fLifeTime = 1.0)
            pSequence.AddAction(pExplosion)
            ### Create sparks that come off it (attached to pShipNode)
            pSparks = Custom.NanoFXv2.ExplosionFX.ExpFX.CreateExpSparkSeq(fSize, pEmitFrom, pShipNode, vEmitPos, vEmitDir)
            pSequence.AddAction(pSparks, App.TGAction_CreateNull(), 0.5)
            ### Create debris (attached to the set root so it looks more real)
            pDebris = Custom.NanoFXv2.ExplosionFX.ExpFX.CreateNanoDebrisSeq(fSize, pEmitFrom, pSet.GetEffectRoot(), vEmitPos, vEmitDir)
            pSequence.AddAction(pDebris, App.TGAction_CreateNull(), 0.5)
        ###

        ##############################################################
        #  IF THIS SECTION OF CODE WERE A VACUUM CLEANER IT WOULD BE #
        #  A DYSON.  WHY?   BECAUSE IT SUCKS!                        #
        ##############################################################
            
        ### Do the visible damage
        WorldLoc = pWarpEngine.GetWorldLocation()
        LocalLoc = App.TGModelUtils_WorldToLocalPoint(pShip.GetNiObject(),WorldLoc)
        #print "X = " + str(LocalLoc.x) + "Y = " +  str(LocalLoc.y) + "Z = " + str(LocalLoc.z)  #  The scaling is /100!
        
        ### Do some random stuff
        fRand = App.g_kSystemWrapper.GetRandomNumber(10)+ 0.000001      # prevent overflow if i use it somewhere
        #fRand = 10
        cout(str(fRand))
        if fRand > 4.5:
            ### Do some serious damage -- blow off the hull plating baby!
            if DAMAGESHIP == TRUE:
                pShip.AddObjectDamageVolume((LocalLoc.x/100), (LocalLoc.y/100),(LocalLoc.z/100), (pWarpEngine.GetRadius() * 1.3)+0.1, 800.000000)

            ### Destroy the engine
            pShip.SetInvincible(0)
            pWarpEngine.SetCondition((pWarpEngine.GetCondition()-pWarpEngine.GetCondition()))

            ### I would put some code here to destroy the nacelle,  but it isn't really necessary
            pWarpSys = pShip.GetWarpEngineSubsystem()
            if pWarpSys:
                    # determine how many warp subsystems
                    iNumWarp = pWarpSys.GetNumChildSubsystems()
                    # for each warp engine on the ship make it vent plasma
                    for iEng in range(iNumWarp):
                            qWarpChild = pWarpSys.GetChildSubsystem(iEng)
                            if qWarpChild:
                                if str(qWarpChild) != str(pWarpEngine):
                                    ### balance this later
                                    if PointInSphere(qWarpChild.GetWorldLocation(), (pWarpEngine.GetRadius() * 90.0)+0.1, pWarpEngine.GetWorldLocation()) == TRUE:
                                        VentMiniPlasma(qWarpChild, pShip)
            
        else:
            ### Let them get away lightly -- scorch marks
            if DAMAGESHIP == TRUE:
                pShip.AddObjectDamageVolume((LocalLoc.x/100), (LocalLoc.y/100),(LocalLoc.z/100), (pWarpEngine.GetRadius() * 1.3)+0.1, 300.000000)

            ### but how much should we Damage the engine by?!
            iRand = float(App.g_kSystemWrapper.GetRandomNumber(5)+1)
            pShip.SetInvincible(0)
            try:
                pWarpEngine.SetCondition((pWarpEngine.GetCondition()/iRand))
            except:
                ## destroy it
                pWarpEngine.SetCondition((pWarpEngine.GetCondition()- pWarpEngine.GetCondition()))

            
            pWarpSys = pShip.GetWarpEngineSubsystem()
            if pWarpSys:
                    # determine how many warp subsystems
                    iNumWarp = pWarpSys.GetNumChildSubsystems()
                    # for each warp engine on the ship make it vent plasma
                    for iEng in range(iNumWarp):
                            qWarpChild = pWarpSys.GetChildSubsystem(iEng)
                            if qWarpChild:
                                if str(qWarpChild) != str(pWarpEngine):
                                    ### balance this later
                                    if PointInSphere(qWarpChild.GetWorldLocation(), (pWarpEngine.GetRadius() * 90.0)+0.1, pWarpEngine.GetWorldLocation()) == TRUE:
                                        VentMiniPlasma(qWarpChild, pShip)
            
                
        ### Play the sequence
        pSequence.Play()

### Note - I love nanobytes style of ### comments! I am gonna use from now on!
###################################################################################
# Maths functions! oooo!
def SQ(num):
    # Squares a number
    # Not done in the BC engine as its alot of data flow
    # when it can be done localy quicker (IMO)
    debug(__name__ + ", SQ")
    return num*num

def Get2VectorLength(v1, v2):
    # Get the distance between two vectors
    debug(__name__ + ", Get2VectorLength")
    return math.sqrt(SQ(v2.GetX() - v1.GetX()) + SQ(v2.GetY() - v1.GetY()) + SQ(v2.GetZ() - v1.GetZ()))

def PointInSphere(Point, SphereRadius, SphereCenter):
    # Determine if a point is within a sphere
    debug(__name__ + ", PointInSphere")
    if Get2VectorLength(SphereCenter, Point) >= SphereRadius:
        return FALSE
    else:
        return TRUE

###################################################################################
# Based of NanoFX2/Stock code to set a rotation for the ship
def SetCrazyRotation(pShip):
    debug(__name__ + ", SetCrazyRotation")
    vNewVelocity = App.TGPoint3()                                                           # We will need a new veolcity
    vNewVelocity.SetX((App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 1000.0)       # Randomly Gen the angular acc
    vNewVelocity.SetY((App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 1000.0)
    vNewVelocity.SetZ((App.g_kSystemWrapper.GetRandomNumber(20001) - 10000) / 1000.0)
    vCurVelocity = pShip.GetAngularVelocityTG()                                             # Add New Velocity to Current Velocity
    vCurVelocity.Add(vNewVelocity)
    vCurVelocity.Unitize()                                                              
    pShip.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)    # Annnd done!
    return 0

###################################################################################
# Loads a texture set into the game engine
def ChooseRandomTexture():
    # Chooses a random texture from the folder where they are
    debug(__name__ + ", ChooseRandomTexture")
    ilen = len(Foundation.GetFileNames(GFX_FOLDER, 'tga'))
    if ilen > 0:
    	iRandom = App.g_kSystemWrapper.GetRandomNumber(ilen)
    	strFile = GFX_FOLDER + "TPS" + str(iRandom) + ".tga"
    	return strFile
    return None

def LoadTPSGfx():       # based of NanoFX2 code to load them
    
    # Load the textures and their frames into the BC engine
    iNumXFrames = 8                                             # Number of X frames to index the image by
    iNumYFrames = 4                                             # Number of X frames to index the image by
    
    sFolder = GFX_FOLDER                                        # Folder to the Gfx
    sFileNames = Foundation.GetFileNames(sFolder, 'tga')        # get a list of the files in the dir

    for loadIndex in sFileNames:
            debug(__name__ + ", LoadTPSGfx")
            strFile = sFolder + str(loadIndex)
            #cout("Loading " + strFile)
            fX = 0.0
            fY = 0.0

            pContainer = App.g_kTextureAnimManager.AddContainer(strFile)    # Set the "primary key" in the texture database
            # Load a Normal X * Y Frame Explosion Effect
            pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
            for index in range(iNumXFrames * iNumYFrames):
                    pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
                    fX = fX + (1.0 / iNumXFrames)

                    if (fX == 1.0):
                            fX = 0.0
                            fY = fY + (1.0 / iNumYFrames)
    cout("Texture Loading Complete")
    
###################################################################################
# Create mini plasma streams *built from the ground up!*
def VentMiniPlasma(pWarpChild = None, pShip = None):
    #vEmitPos      = pShip.GetWorldForwardTG()
    #vEmitDir      = pShip.GetWorldUpTG()
    debug(__name__ + ", VentMiniPlasma")
    pSet          = pShip.GetContainingSet()
    pAttachTo     = pShip.GetNode() #pSet.GetEffectRoot()
    pEmitFrom     = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
    fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetOverrideColor(pShip, "PlasmaFX")
    if (fPlasmaColor == None):
            sRace	      = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pShip)
            fPlasmaColor  = Custom.NanoFXv2.NanoFX_Lib.GetRaceTextureColor(sRace)
    Seq = App.TGSequence_Create()

    for iMiniS in range(round(App.g_kSystemWrapper.GetRandomNumber(3) + 1)):
        # for each potential rupture
        if pWarpChild:
            ### Get X
            c = App.g_kSystemWrapper.GetRandomNumber(180) + 1 /180
            if c > 1:
                c = -1
            else:
                c = 1
            x = c * 4
            x = App.g_kSystemWrapper.GetRandomNumber(x + 1)
            
            # Get Y
            c = App.g_kSystemWrapper.GetRandomNumber(180) + 1 /180
            if c > 1:
                c = -1
            else:
                c = 1
            y = c * 4
            y = App.g_kSystemWrapper.GetRandomNumber(y + 1)
            ### Get X
            c = App.g_kSystemWrapper.GetRandomNumber(180) + 1 /180
            if c > 1:
                c = -1
            else:
                c = 1
            z = c * 4
            z = App.g_kSystemWrapper.GetRandomNumber(z + 1)

            ###

            ### Set Dir
            vEmitDir = App.TGPoint3()
            vEmitDir.SetXYZ(x,y,z)
            ### Set Pos
            vEmitPos = pWarpChild.GetPosition()

                
            fSize = pShip.GetRadius() * 0.01
            pPlasma = CreateMiniPlasmaEffect(pEmitFrom,
                            
                                          pAttachTo,
                                          fSize,
                                          vEmitPos,
                                          vEmitDir,
                                          fVelocity = 0.2,
                                          fRed = fPlasmaColor[0],
                                          fGreen = fPlasmaColor[1],
                                          fBlue = fPlasmaColor[2],
                                          fBrightness = 0.10, fLen = pWarpChild.GetRadius())
            Seq.AddAction(pPlasma)

            fSize = pShip.GetRadius() * 0.005
            pPlasma = CreateMiniPlasmaEffect(pEmitFrom,
                            
                                          pAttachTo,
                                          fSize,
                                          vEmitPos,
                                          vEmitDir,
                                          fVelocity = 0.2,
                                          fRed = fPlasmaColor[0],
                                          fGreen = fPlasmaColor[1],
                                          fBlue = fPlasmaColor[2],
                                          fBrightness = 0.6, fLen = pWarpChild.GetRadius())
            Seq.AddAction(pPlasma)
    Seq.Play()                       

def CreateMiniPlasmaEffect(pEmitFrom,pAttachTo,fSize, kEmitPos, kEmitDir, fVelocity, fRed = 255.0, fGreen = 255.0,fBlue = 255.0, fBrightness = 0.6, fLen = 1.4):
	#iTimingId  = App.TGProfilingInfo_StartTiming("Effects::CreateSmokeHigh")
	debug(__name__ + ", CreateMiniPlasmaEffect")
	pMiniPlasma = App.AnimTSParticleController_Create()
        ### Do the colours and alpha     
        pMiniPlasma.AddColorKey(0.1, 1.0, 1.0, 1.0)
        pMiniPlasma.AddColorKey(fBrightness, fRed / 255, fGreen / 255, fBlue / 255)
        pMiniPlasma.AddColorKey(1.0, 0.0, 0.0, 0.0)
        ### Alpha
        pMiniPlasma.AddAlphaKey(0.0, 1.0)
        pMiniPlasma.AddAlphaKey(0.7, 0.5)
        pMiniPlasma.AddAlphaKey(1.0, 0.0)   
        ### Setup Sizes
	pMiniPlasma.AddSizeKey(0.0, 0.2 * fSize)
	pMiniPlasma.AddSizeKey(0.6, 1.0 * fSize)
	pMiniPlasma.AddSizeKey(0.9, 2.0 * fSize)
        ### Setup properties
	pMiniPlasma.SetEmitVelocity(fVelocity)
	pMiniPlasma.SetAngleVariance(1.0)#(60.0)
	### we might want to varry this with the velocity 
	### so the puffs are not so far from each other	
	fFrequency = 0.01
	pMiniPlasma.SetEmitLife(fLen)
	pMiniPlasma.SetEmitFrequency(fFrequency)
	pMiniPlasma.SetEffectLifeTime(App.g_kSystemWrapper.GetRandomNumber(10) + 5.0) #(5.3)
	#pMiniPlasma.SetEmitVelocity(0.10)
	#pMiniPlasma.SetDrawOldToNew(0)
        sFile = "scripts/Custom/NanoFXv2/SpecialFX/Gfx/Plasma/Plasma.tga"
	pMiniPlasma.CreateTarget(sFile)
	pMiniPlasma.SetEmitFromObject(pEmitFrom)
	pMiniPlasma.SetEmitPositionAndDirection(kEmitPos, kEmitDir)
	#pMiniPlasma.SetInheritsVelocity(1)	# share the ships velocity
	pMiniPlasma.AttachEffect(pAttachTo)	
	# Make it blend closer to white than black
	pMiniPlasma.SetTargetAlphaBlendModes(0, 0)
	#App.TGProfilingInfo_StopTiming(iTimingId)
	return App.EffectAction_Create(pMiniPlasma)


def MPDeleteFirePoint(myFirePointName):                        
	# send clients to remove this object
	debug(__name__ + ", MPDeleteFirePoint")
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
		for i in range(len(myFirePointName)):
			kStream.WriteChar(myFirePointName[i])
		# set the last char:
		kStream.WriteChar('\0')

		# Okay, now set the data from the buffer stream to the message
		pMessage.SetDataFromStream(kStream)

		# Send the message to everybody but me.  Use the NoMe group, which
		# is set up by the multiplayer game.
		pNetwork = App.g_kUtopiaModule.GetNetwork()
		if not App.IsNull(pNetwork):
			pNetwork.SendTGMessageToGroup("NoMe", pMessage)

		# We're done.  Close the buffer.
		kStream.CloseBuffer()
	return 0
