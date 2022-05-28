from bcdebug import debug
## WalkFX KM Edition
## BCS:TNG 2006
## Current Maintiner John Hardy (Lost_Jedi)
################################################################################
#   WalkFX -- v0.3.5
#
#   Last Review:    Nominated for BCF Mod of the Year 2005 (v0.0.2)
#
#   Lets the Captain walk round the bridge, like a true Bridge Commander.
#                                          
#   Created by BCS:TNG for a HUGE secret upcoming mod                          
#       v0.0.1 -- Lost_Jedi aka John Hardy 09/10/2005                           
#           ~Works fine for me.                                                 
#
#       v0.0.2 -- Lost_Jedi aka John Hardy 15/10/2005                           
#           ~Added:                                                             
#                   - Easier to access key events                               
#                   - SeatBelt Button                                           
#                       - Free Float Mode                                       
#                       - Walking Mode                                          
#                   - Sinusoidal Walking Movment                                
#                   - Run Factor for easy access to speeds                      
#                   - Sounds as the player walks                                
#                   - Spelling of Handlers corrected ;)                         
#                                                                               
#	v0.0.2.5 -- USS Sovereign -- 27/10/2005			         	
#                   - Galaxy Bridge fix inserted differently 			 
#	            - It transfer's you to so called Engineering (DBridge)       
#                   - Vent Plasma Conflict Fixed                                 
#
#       v0.0.2.5a -- Lost_Jedi -- 17/11/2005                                     
#                   - Wowbaggers Hight Fix Implemented                               
#                   - FreeFloat Issue Fixed (thanks for the bug reps guys!)      
#
#       v0.3 -- Wowbagger
#               - Ramp issues worked out.
#               - A burning hatred for bridge models develops.
#               - Minor sound/sinusoidal movement alterations.
#               - Minor cleanup.
#               - Known Bugs:
#                       -Sinusoidal movement got really choppy as soon as altitude
#                       correction started working.  I'm at a loss to fix it.
#   
#       v0.0.3.1 -- USS Sovereign 22/12/2005
#               - restored proper history of the mod, as l_j originally did that
#                 and we have to respect his wishes
#               - gal bridge fix forgotten and now included
#               - sounds which were fixed in 0.0.2.5 are now again included
#               - People that had CTD's could also now have it - FIXED again
#               Note to myself: wowbagger must have worked on an older version
#
#       v0.0.3.2 -- USS Sovereign 04/01/2006 (corrected the date :) )
#               - fixed a bug where the game would crash if you got into a wall
#               or for me the game would just freeze
#               - also if you run into a wall you cannot walk through it, clipping
#               effect disabled or to be more precise it seems like you're hitting
#               it
#               Note: Wowbagger did a hell of a job
#
#       v0.0.3.3 -- USS Sovereign  19/1/2006
#               - Reworked the menu
#               - You now run by pressing the V key
#               - Fixed the double menu QBR bug
#               - Added a new option called 'Sit Down' which gets you back to your
#               starting location
#               NOTE: This version was done to show how to do real scripting job!
#
#       v0.0.4 -- USS Sovereign 20/1/2006
#               - Got tired of using 4 nubmers to name one version
#               - Fixed a conflict when using the V key to run
#               - You now run using the 'L' key by looking at the default key
#               config it's free to be used.
#               - Improved collision detection further for custom bridges
#
#       v0.1 -- USS Sovereign 21/1/2006
#               - Fixed ET_OBJECT_CREATED bug
#               - Added QBR restart handler
#               - Fixed one additional QBR bug I found while testing
#               - Fixed the galaxy bridge bug when starting a new game
#               you were obviously standing at the begining of it
#               - Tested this version in many different conditions and
#               with different mods, tested with Bridge Plugin too.
#
#       v0.1.1 -- Wowbagger 1/29/2006
#               - Tested and complimented Sovvy's work.  Noted general
#               excellence of clipping fix.
#               - Changed ET_OBJECT_CREATED to ET_SET_PLAYER.  I kept getting
#               teleported back to my chair in the middle of battle, every
#               time a new object was created.
#               - Adjusted sinsoidal movement code for greater smoothness.
#               - Noted and repaired tiny conflict between NanoFX, WFX, and BP.
#
#       v0.1.2 -- USS Sovereign 01/02/2006
#               - Changed back ET_OBJECT_CREATED but added a new listener that
#               only activates the sequence after the player enters the set.
#               - WOWBAGGER NOTES: This works much better and is acceptable for
#               release with TB.  However, certain combinations of clicks in the
#               Tactical Window can still result in position reset (falling 
#               through the Magical Space Holes back to your chair).  It is rare
#               in this version, but will have to be fixed to be used in the
#               Immersion Framwork.
#
#       v0.1.3 -- Lost_Jedi aka John Hardy 06/02/2006 
#               - <Rant>
#                   Ok since TG *forgot* to include an event type for a new bridge
#                   loading, amongst alot of things... actually going offtopic i think this
#                   game was gonna orig. be called "Star Trek: Commander" cos there
#                   is VERY limited support for bridge stuff. it all seems so slapped on
#                   at the end. Like that whole "galaxy bridge captin" thing. Whats with that?...  anyway
#                   like i was saying there is no event for the awapping of bridges
#                   and in order to get anywhere close we'd have to do what Sovvie and Wowie
#                   have been doing for the last 5 versions of this mod and check every time
#                   the engine creates an object.  Now this can range from "missions" to "torpedos"
#                   so as you can imagine its quite alot of work to check, and will cause alot alot
#                   of sloooow down.
#                   So how did you get round it? Well credit goes to MLeo for his wonderful
#                   scripting job on the Bridge Plugin.  It allows a class __call__ function to be
#                   run every time a bridge switches, which is *PERFECT* for doing what we want.
#                   But not everyone has the Bridge Plugin, so thereofre it would have to become a
#                   requirement.  Not true.  I've done it so it tries to use the bridge plugin, if then it
#                   can't find it it will then not create the "sit down" button.  If however it does find
#                   BP present then it will use it and swap a boolean saying that its ok to create
#                   button and run the function.
#               - </Rant>
#               - So after that short and unnecessay outburst - here's the change list:
#                   - Sit Down dependant on BP
#                   - Removed all the un necessary code
#                   - Now uses an array rather than a dictionary
#                   - Camera looks at view screen when u sit down
#                   - Error protection
#               - A point of interest.  On my FBCMP install i noticed that part of MLeo's
#                   ReSet.py (detail fixing mod) to do with the power sliders was getting
#                   called when you press L.  This was filling the console with errors
#                   so for now i changed it back to a capital N pending further inviestigation.
#
#
#       v0.1.4 -- Wowbagger 2/13/2006:
#               - Shiny new options!
#               - Added proximity check to sit down -- you now must be within
#               a few game units of the camera starting position (the captain's
#               chair) in order to sit down.
#               - Sit Down has been changed from a button in Saffi's menu to
#               a keyboard command.
#               - Still not QBR-compatible.
#               - Minor re-ordering of functions in this file, for organiz-
#               ational purposes.
#               - Moved Run key to the comma.
#               - Moved Sit Down key to the period.
#
#       v0.2 -- USS Sovereign 07/03/2006
#               <Rant Mode>
#               Well Lj said that ET_OBJECT_CREATED can cause slowdowns, it's not true
#               especially if it calls only for a listener that activates a sequence, only
#               if the players ship is recreated the sequence is activated! I know this,
#               as a fact, if somebody doesn't believe me then I don't care! :P
#               <End Rant Mode>
#
#               - Skipped few numbers 
#               - You sit down using the S key now
#               - QBR compatible
#               - QBR restart handlers included
#               - No longer Sit Down function is Bridge Plugin dependant
#               - SitDown no longer screws up Bridge Restarting positions as it
#               did in older versions, pre 0.1.3
#               - Re-fixed Galaxy Bridge Height starting position (It appeared
#               that you were standing!)
#               - Character collision detection system implemented, needs further
#               testing
#               - Implemented character collisions only for 5 main characters,
#               other characters seem to cause a lot of problems to walkfx
#               module. It sees collisions that are not there, it may be cause
#               of the fact that these extra characters are hidden and then
#               spawned into the game. So walkfx code detects them and detects
#               collisions with them :(, still working on a way to fix this
#               if it's possible
#               UPDATE NOTES 10/03/2006
#               - Improved character collision and used new math, well minimal
#               changes but better results. This WalkFX is ready for beta testing
#               now!

#       v0.3 -- Wowbagger 03/09/06
#               - Unreleased.  Error Code Number 2: Piece of Crap.
#
#       v0.3.1 -- Wowbagger 03/10/06
#               - Nice job, Sov.  Very clever ET_OBJECT_CREATED workaround.
#               Hopefully not much system resource cost.
#               - Tightened code in character collision detection system.
#               - Used KeyFoundation for WFX key config; MLeo's file will
#               have to be included in future installs, but now the PLAYER
#               has control of key assignments.
#               - Went back and tightened up a ton of loose code in AdjustHeight().
#               It's still Sovvy's system, but it uses a set of variables that
#               enable it to do all the same checks in about 1/5th the code.
#               - Updated 0.2.2 with Sovvy's final mods to the Beta release of
#               0.2.
#               - I *think* I found the source of the weird errors with checking
#               extras.  They were still on the bridge, but "hidden."  If we add
#               a check for "hidden" characters in addition to casting for
#               pCharacter, the problem seems to go away.
#               - Final concern: the last released version was called v0.0.2.
#               Should the one in TB just be called v0.3, to keep people from
#               mixing up v0.0.2 with v0.2.2 and/or v0.2.0?
#                   On the other hand, you could read the history of this mod
#               in this order, and I think it makes more sense that way!
#                   [list deleted]
#                   Actually, why don't I just make a thread on it?  Ignore this
#               random spiel.
#
#       v0.3.2 -- USS Sovereign 15/03/2006
#               - Minor tweak to character collision detection system, my baby
#               evolved thanks to Wowbagger ;)
#               - Fixed the bug so height is no more a preset on every bridge,
#               before height was a preset for all bridges Z value was presumed
#               to be 65 now we interact with the currently assigned bridge HP
#               and get the Z value and add 8.5 units to it
#               - Modified default commands, they're the same in every version
#               and wowbagger sometimes loves to change them to his liking
#               - You have to be in bridge view in order to walk now
#
#       v0.3.3 -- Wowbagger 3/16/06
#               - Worked on z-coordinate checking in Char. Col. Det. Sys. (or
#               CCDS) to compensate for some missed checks on Defiant bridges. I
#               ended up just adding a second test.  The in-game effects are
#               extremely minor, but will be important in Immersion.
#               - Added bridge view check to SitDown().
#               - Killed the PosX - 1 if the CCDS returned TRUE.  It was causing
#               some problems where I could get pulled into a "character vortex"
#               and be unable to move until I got spit out the other side.
#               Sometimes I was even trapped between a character and a wall.
#               - KeyFoundation now re-binds every time SDHandler resets,
#               ensuring that players will have their control scheme active the
#               FIRST time they program it.
#
#       v0.3.4 -- Wowbagger 3/17/06
#               - Wow.  After Cackad's post, I downloaded every available
#               complete bridge, just so I covered every base.  I found some
#               interesting stuff, but for you non-programmers out there who
#               don't really care about the version history: there are a lot
#               of really excellent pieces of bridge work out there.  Go get
#               'em.
#               - Minor disaster with Sovvy's iHeight fix.  I had to revert it.
#               The details of this sad event are in AdjustHeight().  I couldn't
#               stand to delete the code, though.  It's just commented out.
#               - Some bridges are really, really cramped.  The CCDS settings
#               were just too restrictive.  I gave our Captain a lot more
#               latitude to move around by reducing the a check from 42 to 21.
#               - Killed one of my old stray print command that was flooding the
#               console.
#
#       v0.3.5 -- Lost_Jedi 12/15/06
#               - Almost 9 months have passed and nobody has had to look at WFX
#                   since, that is pretty good :)
#               - This is a KM edition.  KM 1.0 is a requirement (or to be more accurate Mleo's Keyfoundation and the Bridge Plugin are)
#               - Uses the Bridge Plugin like in v0.1.3 woo!
#               - Tightended code up and made it conform to a naming scheme
#                   - To make a point, i've cut over 300+ lines of unnecessary code from it :P hehe
#               - Yea, it's just better :) woo
################################################################################


## Imports
import App
import Foundation
from math import sin, sqrt

## Tools
dSoundCache = {}
def LoadSound(sFileName, sSoundID):
    debug(__name__ + ", LoadSound")
    pSound = App.TGSound_Create(sFileName, sSoundID, 0)
    pSound.SetSFX(0)
    pSound.SetInterface(1)
    dSoundCache[sFileName] = pSound
    return sSoundID

  
def GetBridgeCamera():
    debug(__name__ + ", GetBridgeCamera")
    pSet = App.g_kSetManager.GetSet ("bridge")
    if not pSet:
        return None
    pCamera = App.CameraObjectClass_GetObject(pSet, "maincamera")
    return pCamera

## Constants
bFreeFloatEnabled   = 0
WALKSPEED           = 3.0
RUNFACTOR           = 2.00

RUN_FORWARD         = 0x00000064
WALK_FORWARD        = 0x00000065
WALK_BACKWARD       = 0x00000066
SIT_DOWN            = 0x00000067

# These are the names of the positions we will check.
CHARACTER_NAMES = ["Engineer", "Tactical", "XO", "Science", "Helm", "FemaleExtra1", "FemaleExtra2", "FemaleExtra3", "MaleExtra1", "MaleExtra2", "MaleExtra3"]

## Globals
global mode, dWalkFX, pSeatLocation, fStepsTaken
mode            = Foundation.MutatorDef("BCS:TNG WalkFX KM Edition")
dWalkFX         = {"modes": [mode]}
pSeatLocation   = None
fStepsTaken     = 0

## Events
ET_WALKFX       = App.UtopiaModule_GetNextEventType()


## Setup Key Bindings
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Walk Forward",   "Walk Forward",     ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_FORWARD,     "General", dict = {"modes": [mode]}))
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Walk Backward",  "Walk Backward",    ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_BACKWARD,    "General", dict = {"modes": [mode]}))
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Run Forward",    "Run Forward",      ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, RUN_FORWARD,      "General", dict = {"modes": [mode]}))
Foundation.g_kKeyBucket.AddKeyConfig(Foundation.KeyConfig("Sit Down",       "Sit Down",         ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, SIT_DOWN,         "General", dict = {"modes": [mode]}))


def KeyConfigReload(pObject = None, pEvent = None):
    ## Takes our KeyFoundation-determined Key Bindings and resets them for KS_NORMAL.
    ## Get the key bindings
    debug(__name__ + ", KeyConfigReload")
    iForward    = App.g_kKeyboardBinding.FindKey(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_FORWARD)
    iBackward   = App.g_kKeyboardBinding.FindKey(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_BACKWARD)
    iRun        = App.g_kKeyboardBinding.FindKey(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, RUN_FORWARD)
    iSitDown    = App.g_kKeyboardBinding.FindKey(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, SIT_DOWN)
    ## Clear old bindings for KEY_UP
    App.g_kKeyboardBinding.ClearBinding(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_FORWARD)
    App.g_kKeyboardBinding.ClearBinding(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_BACKWARD)
    App.g_kKeyboardBinding.ClearBinding(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, RUN_FORWARD)
    App.g_kKeyboardBinding.ClearBinding(ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, SIT_DOWN)
    ## Do new bindings for KEY_UP
    App.g_kKeyboardBinding.BindKey(iForward,    App.TGKeyboardEvent.KS_NORMAL, ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_FORWARD)
    App.g_kKeyboardBinding.BindKey(iBackward,   App.TGKeyboardEvent.KS_NORMAL, ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, WALK_BACKWARD)
    App.g_kKeyboardBinding.BindKey(iRun,        App.TGKeyboardEvent.KS_NORMAL, ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, RUN_FORWARD)
    App.g_kKeyboardBinding.BindKey(iSitDown,    App.TGKeyboardEvent.KS_NORMAL, ET_WALKFX, App.KeyboardBinding.GET_INT_EVENT, SIT_DOWN)


## Setup Walking Sounds
global lStepSounds, iStepNumber, fPlaySoundCounter
iStepNumber         = 0
fPlaySoundCounter   = 0.00
lStepSounds = [
    LoadSound("sfx/Custom/WalkFX/steps/step1.wav", "Step1"),
    LoadSound("sfx/Custom/WalkFX/steps/step2.wav", "Step2"),
    LoadSound("sfx/Custom/WalkFX/steps/step3.wav", "Step3"),
    LoadSound("sfx/Custom/WalkFX/steps/step4.wav", "Step4")
    ]


## Walking Class
########################################################
class WalkFX(Foundation.TriggerDef):
    
    def __init__(self, dict = {}):

        ## Instantiate the base class
        debug(__name__ + ", __init__")
        Foundation.TriggerDef.__init__(self, "WalkFX", ET_WALKFX, dict = {})

        ## Add a function handler so everytime we access the pause menu, we do a reload.
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_BACKGROUND_MENU, None, __name__ + ".KeyConfigReload")

    def __call__(self, pObject, pEvent):

        ## Get the integer from the event
        debug(__name__ + ", __call__")
        iWalkAction = pEvent.GetInt()

        ## Select the appropriate action
        
        if (iWalkAction == RUN_FORWARD):
            MoveForward(RUNFACTOR*WALKSPEED, 1)

        elif (iWalkAction == WALK_FORWARD):
            MoveForward(WALKSPEED)

        elif (iWalkAction == WALK_BACKWARD):
            MoveForward(-WALKSPEED)
            
        elif (iWalkAction == SIT_DOWN):
            SitDown()

        return 0

## WalkFX: Functions
def GetSinusoidalHeightFromStepNumber(bRunning):
    debug(__name__ + ", GetSinusoidalHeightFromStepNumber")
    global fStepsTaken
    
    fStepsTaken = fStepsTaken + 0.5               
    if (fStepsTaken == 99999):   # <--- So I 'worked round'/bodged it with this
        fStepsTaken = 0          #       to prevent step overflow
        
    fHeight = 0.0000
    fHeight = sin(fStepsTaken/2)

    # If we're at about -0.77 on the sine curve, our foot is just hitting the ground.
    # Note: if the line "sHeight = sin(StepsTaken/2)" is changed, this MUST be changed
    # proportionately.
    if fHeight <= -0.75 or fHeight >= -0.97:
        PlayStepSound(bRunning)
    return fHeight


def PlayStepSound(bRunning = 0):
    debug(__name__ + ", PlayStepSound")
    global lStepSounds, iStepNumber, fPlaySoundCounter

    ## Increment the floating threshold for the step player
    if (bRunning == 1):
        fPlaySoundCounter = fPlaySoundCounter + (RUNFACTOR / 10)
    else:
        fPlaySoundCounter = fPlaySoundCounter + 0.1

    ## If we have exceded this threshold and are ready to reset then
    if(fPlaySoundCounter >= 2):
        fPlaySoundCounter = 0

        ## Rotate the sound buffer and play head
        lStepSounds.append(lStepSounds.pop(0))
        App.g_kSoundManager.PlaySound(lStepSounds[0])


# Adjusts camera height depending on altitude by detecting distance from the bridge model.
# This def over the time has grown to be a monster .
def AdjustHeight(x, y, z):
                debug(__name__ + ", AdjustHeight")
                vCameraX    = x
                vCameraY    = y
                vCameraZ    = z

                # We need this now.
                pCamera     = GetBridgeCamera()
                kForward    = pCamera.GetWorldForwardTG()
                kPos        = pCamera.GetWorldLocation()

                # Before we really get started, let's just find out if we're
                # about to try to occupy character space:
                if FindCharPositions(x, y, z) == 1:
                        x = kPos.GetX() # I encountered some "character black holes", and was forced to cut the -1.  Which is too bad.  The -1 was really nifty.
                        y = kPos.GetY()
                        z = kPos.GetZ()
                        return x, y, z

##                # well I'm sick of height being given manually now we fix this
##                # on nebula bridge your height is way too low so we use the new code to interact with
##                # currently assigned bridge hp and get z coordinate + 15 units
##                pBridgeSet = App.BridgeSet_Cast(App.g_kSetManager.GetSet('bridge'))
##                BridgeConfig = pBridgeSet.GetConfig()
##                pBridge = __import__("Bridge." + BridgeConfig)
##                BasePos = pBridge.GetBaseCameraPosition()
##
##                # x and y are not used but might be useful in the future who knows
##                BaseX = BasePos[0]
##                BaseY = BasePos[1]
##                BaseZ = BasePos[2]
##
##                # There have been problems with the Defiant bridge on this.
##                # If we're *really* low, just set our height to a nice 6.5 feet.
##                if BaseZ < 50:
##                        BaseZ = 65 - 8.5
##                
##                # Finds how far we are from the bridge floor by using two points, then auto-corrects so we reach a proper height.
##                # now this baby is checking for current z coordinates and adds 8.5 units so you really are standing ;)
##                # we've turned out BC into a great game now :)
##                iHeight = BaseZ + 8.5 

                #   Wow.  Some things you just don't notice until a Beta tester
                # points them out to you.  After a *really* freaky test run with
                # v0.3.3 on the BoP Bridge, I was totally baffled.  Why wouldn't
                # my character go down to the floor?
                #   Then it suddenly occurred to me: **iHeight is a function of
                # the captain's height, NOT the distance from z-coordinate 0!**
                # Therefore, when we used Sovvy's config file method, we weren't
                # adjusting our captain's position for the different bridge
                # sets, as we both thought we were; we were changing his height
                # so that he was anywhere from 10 GU (about half of a meter)
                # tall on the Defiant to 138.5 GU (a good bit over 5 meters) tall 
                # on the Bird of Prey!
                #   So the original code worked better after all.  I only regret
                # killing such a nice piece of coding on Sovereign's part.  I am
                # reverting to a reasonable 65 GU, which appears to be about 6
                # feet, 3 inches in the Imperial system, and a bit over 2 meters
                # in metric.
                iHeight         = 65
                iDeepTest       = iHeight + 1
                iShallowTest    = iHeight - 1
                iRange          = iDeepTest - iShallowTest

                # Grab our bridge object.
          	pSet            = App.g_kSetManager.GetSet("bridge")
                pBridgeObject   = App.BridgeObjectClass_GetObject(pSet, "bridge")

                # Deep points.
                kTestPoint1     = App.TGPoint3()
        	kTestPoint1.SetXYZ(vCameraX, vCameraY, vCameraZ - iDeepTest)
                kTestPoint1a    = App.TGPoint3()
        	kTestPoint1a.SetXYZ(vCameraX, vCameraY, vCameraZ - iDeepTest + 0.1)

                # Shallow points.
                kTestPoint2     = App.TGPoint3()
        	kTestPoint2.SetXYZ(vCameraX, vCameraY, vCameraZ - iShallowTest + 0.1)
                kTestPoint2a    = App.TGPoint3()
        	kTestPoint2a.SetXYZ(vCameraX, vCameraY, vCameraZ - iShallowTest)

                #       The following two boolean checks test for collision types "Big" and "A2".  They are 
                # exact opposites; the weird names are simply holdovers from the testing phase, where many, 
                # many collision types were checked for usefulness.
                #       The test checks to see whether kTestPoint1 or kTestPoint2 are on the bridge set; the
                # secondary points are simply a place to which to draw the line and are intentionally
                # kept very close to their parent points.  Incidentally, testing shows that the arguments
                # for each boolean check MUST be in the given order; the deep point test must have the secondary
                # go first (the secondary being above the parent in both TestPoints), and the shallow point test
                # must have the parent go before the secondary.  We have no earthly idea why.  It's TG's fault,
                # as per usual. *recalls Sleight42's rant about windowing toolkits in the ATP GUI file*  *waxes nostalgic*
                bBig    = pBridgeObject.LineCollides(kTestPoint1a, kTestPoint1)
                bA2     = pBridgeObject.LineCollides(kTestPoint2, kTestPoint2a)

                bLittle = pBridgeObject.LineCollides(kTestPoint2a, kTestPoint2)
                bA1     = pBridgeObject.LineCollides(kTestPoint1, kTestPoint1a)
                bB2     = pBridgeObject.LineCollides(kPos, kTestPoint2)
                bB1     = pBridgeObject.LineCollides(kPos, kTestPoint1)
                bC2     = pBridgeObject.LineCollides(kTestPoint2, kPos)
                bC1     = pBridgeObject.LineCollides(kTestPoint1, kPos)

                # If nothing is colliding, we are either way far away from the
                # bridge or attempting to walk through the wall.  Stop it.
                if (bBig == 0) and (bA2 == 0) and (bA1 == 0):
                        x = kPos.GetX()
                        y = kPos.GetY()
                        z = kPos.GetZ()
                        return x, y, z
                    
                # If both Big and A2 are colliding, we're too shallow.
                elif (bBig == 1) and (bA2 == 1):
                        x, y, z = AdjustHeight(x,y,z - iRange/2)

                # If neither is colliding, we're too deep.
                elif (bBig == 0) and (bA2 == 0):
                        x, y, z = AdjustHeight(x,y,z + iRange/2)
      
                # Apparently, the correct ones are in the correct locations.  We're done.
                # If we have a loop going, send these values back through.
                return x, y, z


# Find all characters on the set and their coordinates.
# Mental Note: I hate math!!!
# Extra note: This is one big def :O not as big as Adjust height but when I tried adding those extra characters it was
# big I tell you, for extra characters we need to think of something different, cause the way game uses them is most confusing
# for walkfx module
# Wowie's Note: Not anymore.  Mwahahahahaha!  Still no compatibility with extras
# though.  Working on it.  Sovvy's right; it does cause some weird errors.  My
# theory is that a character not on the bridge still exists there, somewhere,
# but is invisible.  I am testing that theory now.  EDIT: It seems to work now.
def FindCharPositions(x, y, z):
        # If anything collides, the condition is TRUE.
        debug(__name__ + ", FindCharPositions")
        for sChar in CHARACTER_NAMES:
                if FetchIndividualCharPos(x, y, z, sChar) == 1:
                    return 1

        # And in the end if we're not colliding with anything then just return
        # false and you can walk. 
        return 0


# I (Wowbagger) was messing around with WFX late tonight and decided to see if
# we could modularize (is that a word?) Sovv's system of character collision
# detection.  As it turns out, we can.  This is just Sovv's code almost exactly,
# only compressed into a loop and with the camera system slightly altered.  By
# the way, props to Sovereign for Overwhelming Cleverness.
def FetchIndividualCharPos(fCameraX, fCameraY, fCameraZ, sCharacter):

    ## Get the Bridge Set and Character 
    debug(__name__ + ", FetchIndividualCharPos")
    pSet = App.g_kSetManager.GetSet("bridge")
    pCharacter = App.CharacterClass_Cast(pSet.GetObject(sCharacter))

    ## Check we have a character
    if pCharacter and not pCharacter.IsHidden():
        pLocation = pCharacter.GetWorldLocation()
        fCharX = pLocation.GetX()
        fCharY = pLocation.GetY()
        fCharZ = pLocation.GetZ()

        # I would of never thought of this, wowbagger set up the basis to get character collision detection system working
        # without even realizing that ;)
        a = sqrt(pow((fCameraX - fCharX), 2) + pow((fCameraY - fCharY), 2) + pow((fCameraZ - fCharZ), 2))

        # Secondary test that specifically deals with z-coordinate problems.
        b = sqrt(pow((fCameraX - fCharX), 2) + pow((fCameraY - fCharY), 2))
        c = sqrt(pow((fCameraZ - fCharZ), 2))

        # 0.3.4: Decreased "a" even more to compensate for
        # Ambassador/Nebula/Prometheus bridge cramps.
        if a <= 21 or ((b <= 10) and (c <= 100)):
                return 1
        
    # and in the end if we're not colliding with anything then just return false and you can walk 
    return 0


# This baby does most of the work around here.  It is called directly from the WalkFX class.
# And, yes, standard BC scripting format does suggest a separate document for classes.  Admire our flexibility.
def MoveForward(mUnits, bRunning = 0):
    debug(__name__ + ", MoveForward")
    global bFreeFloatEnabled
    # Move the Camera Forward in the direction its facing    

    # If we're not in bridge view return false
    if not (App.TopWindow_GetTopWindow().IsBridgeVisible()):
        return

    # Find the camera.
    pCamera = GetBridgeCamera()
    if not pCamera:
        return

    # Find the camera's position.
    kForward    = pCamera.GetWorldForwardTG()
    kPos        = pCamera.GetWorldLocation()                            

    # Find new positions.
    x = (kPos.GetX() + (kForward.GetX() * mUnits))
    y = (kPos.GetY() + (kForward.GetY() * mUnits))
    z = (kPos.GetZ())

    # If free-floating camera is on, find a Z-position, too.
    if(bFreeFloatEnabled == 1):
            z = (kPos.GetZ() + (kForward.GetZ() * mUnits))

    # Otherwise, maintain our Z... except an elevation check.
    # Also, adjust for sinusoidal movement.
    if (bFreeFloatEnabled == 0):
        x, y, z = AdjustHeight(x, y, z)

        if(bRunning == 1):
            z = (z + GetSinusoidalHeightFromStepNumber(bRunning))
        else:
            z = (z + GetSinusoidalHeightFromStepNumber(bRunning) / RUNFACTOR)

    # Finally, move the camera.
    pCamera.SetTranslateXYZ(x,y,z) 
     

## Sit Down Class
########################################################
class SitDownManager(Foundation.BridgePluginDef):

    bBridgePluginInstalled = 1
       
    def __call__(self, Plug, pBridgeSet, oBridgeInfo):

        ## Reload the Key Config
        debug(__name__ + ", __call__")
        KeyConfigReload()
        
        ## Get the name of the new bridge
        sBridgeName = pBridgeSet.GetConfig()

        ## Then the module
        pBridgeSet  = App.BridgeSet_Cast(App.g_kSetManager.GetSet('bridge'))
        pyModule    = __import__("Bridge." + pBridgeSet.GetConfig())
        if (pyModule):
            ## Then set the position to start from
            global pSeatLocation
            tBridgePos = pyModule.GetBaseCameraPosition()
            pSeatLocation = App.TGPoint3()
            pSeatLocation.SetX(tBridgePos[0])
            pSeatLocation.SetY(tBridgePos[1])
            pSeatLocation.SetZ(tBridgePos[2])


## Are we close enough to sit down
def IsCloseEnoughToSit(pCamera):
    debug(__name__ + ", IsCloseEnoughToSit")
    global pSeatLocation
    # Find the camera's position.
    pPos        = pCamera.GetWorldLocation()
    # Find the camera's position from the seat.
    fDistance   = sqrt(pow((pPos.GetX() - pSeatLocation.GetX()), 2) + pow((pPos.GetY() - pSeatLocation.GetY()), 2) + pow((pPos.GetZ() - pSeatLocation.GetZ()), 2))
    if fDistance <= 50:
        return 1
    return 0

# Function to jump the player back to his starting position.
def SitDown(pObject = None, pEvent = None):
    debug(__name__ + ", SitDown")
    global pSeatLocation
    
    # If we're not in bridge view return false
    if not (App.TopWindow_GetTopWindow().IsBridgeVisible()):
        return

    ## Check we were loaded with the bridge plugin
    if SitDownManager.bBridgePluginInstalled == 0:
        return

    ## Get the Bridge Camera
    pCamera = GetBridgeCamera()
    if not pCamera:
        return
    
    ## If we are close enough to sit then do so
    if IsCloseEnoughToSit(pCamera) and pSeatLocation:
        pCamera.SetTranslate(pSeatLocation)
        App.ZoomCameraObjectClass_Cast(pCamera).LookForward()


## Graphical User Interface
########################################################
class Seatbelt(Foundation.TriggerDef):

    pWalkModeButton     = None
    pFreeFloatButton    = None
    pSitDownButton      = None
    
    def __init__(self, name, eventKey, dict = {}):
        debug(__name__ + ", __init__")
        Foundation.TriggerDef.__init__(self, name, eventKey, dict)

    def __call__(self, pObject, pEvent, dict = {}):
        # we call this function first to delete any clone buttons that appear in QBR
        debug(__name__ + ", __call__")
        RemoveMenu()
        BuildWalkFXMenu()


        
## Build the UI menu
def BuildWalkFXMenu():    
    debug(__name__ + ", BuildWalkFXMenu")
    pMenu                       = CreateMenu("Seatbelt", "XO")
    Seatbelt.pFreeFloatButton   = CreateButton("Free Float",    "XO", __name__ + ".StartFREEFLOAT",  "Seatbelt")
    Seatbelt.pWalkModeButton    = CreateButton("Walk Mode",     "XO", __name__ + ".StartWALKMODE",   "Seatbelt")
    if SitDownManager.bBridgePluginInstalled == 1:
        Seatbelt.pSitDownButton = CreateButton("Sit Down",     "XO", __name__ + ".SitDown",         "Seatbelt")

    # Start with Free Float OFF
    StartWALKMODE()

  
# Turn Free Float Mode on 
def StartFREEFLOAT(pObject = None, pEvent = None):
    debug(__name__ + ", StartFREEFLOAT")
    global bFreeFloatEnabled
    Seatbelt.pWalkModeButton.SetEnabled()
    Seatbelt.pFreeFloatButton.SetDisabled()
    if Seatbelt.pSitDownButton:
        Seatbelt.pSitDownButton.SetEnabled()
    bFreeFloatEnabled = 1


# Turn WalkMode On
def StartWALKMODE(pObject = None, pEvent = None):
    debug(__name__ + ", StartWALKMODE")
    global bFreeFloatEnabled
    Seatbelt.pWalkModeButton.SetDisabled()
    Seatbelt.pFreeFloatButton.SetEnabled()
    if Seatbelt.pSitDownButton:
        Seatbelt.pSitDownButton.SetEnabled()
    bFreeFloatEnabled = 0


# my solution for ESR problem, reworked -- USS Sovereign
# it's badly needed for hardcore QBR fans like myself :)
def RemoveMenu():
    debug(__name__ + ", RemoveMenu")
    g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/WFXmenustring.tgl")
    pBridge     = App.g_kSetManager.GetSet("bridge")
    if not pBridge:
	    return
    g_pXO	= App.CharacterClass_GetObject(pBridge, "XO")
    if not g_pXO:
	    return
    pXOMenu     = g_pXO.GetMenu()
    if not(pXOMenu is None):
        pButton = pXOMenu.GetSubmenu("Seatbelt")
        if not(pButton is None):
            pXOMenu.DeleteChild(pButton)

# Get a bridge menu by name
def GetBridgeMenu(menuName):
    debug(__name__ + ", GetBridgeMenu")
    pTactCtrlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
    pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Menus.tgl")
    if(pDatabase is None):
            return
    App.g_kLocalizationManager.Unload(pDatabase)
    return pTactCtrlWindow.FindMenu(pDatabase.GetString(menuName))


# Create a menu
def CreateMenu(sNewMenuName, sBridgeMenuName):
    debug(__name__ + ", CreateMenu")
    pMenu = GetBridgeMenu(sBridgeMenuName)
    pNewMenu = App.STMenu_Create(sNewMenuName)
    pMenu.PrependChild(pNewMenu)
    return pNewMenu

# Create a button
def CreateButton(sButtonName, sMenuName, Function, sToButton = None, EventInt = 0):        
    debug(__name__ + ", CreateButton")
    pMenu = GetBridgeMenu(sMenuName)
    if sToButton:
        pToButton = pMenu.GetSubmenu(sToButton)
    ET_EVENT = App.Mission_GetNextEventType()
    pMenu.AddPythonFuncHandlerForInstance(ET_EVENT, Function)
    pEvent = App.TGIntEvent_Create()
    pEvent.SetEventType(ET_EVENT)
    pEvent.SetDestination(pMenu)
    pEvent.SetInt(EventInt)
    pButton = App.STButton_CreateW(App.TGString(sButtonName), pEvent)
    if not pToButton:
        pMenu.PrependChild(pButton)
    else:
        pToButton.PrependChild(pButton)
    return pButton

## Instantiate Abstract Classes
########################################################
WalkFX(dict = dWalkFX)
SitDownManager("WalkFX Sitdown Manager",    dict = dWalkFX)
Seatbelt('WalkFX Seatbelt Interface',       App.ET_MISSION_START, dict = dWalkFX)

## Overrides (this particular one fixes the whole 'not being able to walk on the DBridge)
########################################################
Foundation.OverrideDef('GalBridgeFix', 'Bridge.GalaxyBridge.CreateBridgeModel', 'Custom.Autoload.WalkFXfiles.GalaxyBridgeFix.GalBridgeFix', dict = dWalkFX)

