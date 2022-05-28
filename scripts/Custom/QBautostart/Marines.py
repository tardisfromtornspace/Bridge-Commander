from bcdebug import debug
#!/usr/bin/python1.5
# Capturing Enemy Ships
#
# Version:
# 0.8 (beta; all functions implemented, but maybe buggy)
#
# TODO:
# -clean up code :P
#
# HISTORY:
# 06.02.2005:
#       -no more Bridge needed
# 07.11.2004:
#	-released as Version 0.8
#	-capture chance now much higher
#	-fixed asteroids
# 31.10.2004:
# Defiant:      -finally fixed Science Display! :)
# 01.08.2004:
# Defiant:      -check for active NTS Mutator.
# 08.05.2004:
# Defiant:      -renamed 'Marines'-Button to 'Away Team'
# 05.05.2004:
# Defiant:      -added some cloak checks
# 01.05.2004:
# Defiant:      -Fix crashing Bug while creating the scan window
#               -Shuttle Launching Framework is _not_ required for this anymore, but still needed for configuration (say optional)
# 04.04.2004:
# Defiant:      -Reworked Scan window
#               -Added Position of Ships and weapon status to the scan window
# 31.03.2004:
# Defiant:      -Added support for QBautostart (Engineering) Extension >= 0.5
# 24.02.2004
# Defiant:	     Some minor changes :)
# 31.01.2004:
# Defiant:      -The Crew Number will also change the Ship Repairpoints now.
# 30.01.2004:
# Defiant:      -got user output (without sound of course :( -using a dummy .wav file. Maybe we can have a better version in the future)
# 29.01.2004:
# Defiant:      -some fixes and addons for the Scan output. It also has a timer now.
#               -fixed Troops recall function
# 18.01.2004:
# Defiant:	-writing this history :)
#		-finished Scan Button
# 17.01.2004
# Defiant:	-Starting work on scan-buttons
#		-writing Rescue()
#
# older Stuff:
# 5. Defiant (Marines v0.4): Complete Rewrote: A new Marine Model.			 	        # Mod Liscense: GPL
#     code left from others:
#	- Banbury: Distance()
# 4. Defiant (Marines v0.3):		Merge Code from latest Transporter.py to Marines.py
# 3. Lord_Apophis (Marines v0-1 - v0.2):	Rewrote: Allow Beaming to Enemys (Marines.py)		# Mod Liscense: GPL
# 2. Defiant (Engineering Extension 0.1): 	Rewrote for Engineering Mod, will Transport to Target	# Mod Liscense: GPL
# 1. Banbury (QBR 2.2):		wrote the first Emergency Transporter for his QBR		        # Mod Liscense: GPL
#
# This script is using some code from the ReturnShuttles Mod (Liscense: GNU/GPL), Selft Destruct Countdown (SDK Liscense)
# and Shuttle Launching Framework(GPL)
#
# for the GNU GPL see http://www.gnu.org/copyleft
# and LGPL: http://www.gnu.org/copyleft/lesser.html
#
# current Maintainer:
# Defiant <mail@defiant.homedns.org>
# For updates see http://defiant.homedns.org/~erik/STBC/Marines/
#

import App
import MissionLib
import Lib.LibEngineering
import Foundation
import string
from Libs.LibQBautostart import *

# chech for proper ftb Install
useFTB = -1

for i in Foundation.mutatorList._arrayList:
        fdtnMode = Foundation.mutatorList._keyList[i]
        if fdtnMode.IsEnabled() and (fdtnMode.name == "New Technology System"):
                useFTB = 1
                break

if (useFTB == 1):
        try:
                import ftb.ShipManager
        except:
                useFTB = 0

pBridge = None
g_pBrex = None
pBrexMenu = None
g_pScience = None
pScienceMenu = None
#MARINES_FIGHT_TIMER	= Lib.LibEngineering.GetEngineeringNextEventType()
TRANSFER_SHIELDON_TIMER = Lib.LibEngineering.GetEngineeringNextEventType()
SCAN_TIMER              = Lib.LibEngineering.GetEngineeringNextEventType()
EVENT_SCAN_TARGET       = None
pSound = App.TGSound_Create("sfx/Interface/new_game3.wav", "Beam_Sound", 0) # the Beam Sound
pSound.SetSFX(0)
pSound.SetInterface(1)
g_pDatabase = App.g_kLocalizationManager.Load("data/TGL/Bridge Crew General.tgl")
c_pTroops = 0
p_MaxTroops = 0
p_ActiveTroops = 0
ShieldTurnOnShip = 0
dist = 300 # Max Beam Distance
pGame_old = str(App.Game_GetCurrentGame()) # we need that one in restart()
dict_Marines = {} # dictionaries
dict_Battles = {}
pScienceScanWindow = None
MarinesDatabase = App.g_kLocalizationManager.Load("data/TGL/Marines.tgl")
dict_Warp = {}

MODINFO = { "Author": "\"Defiant\" mail@defiant.homedns.org",
            "Download": "http://defiant.homedns.org/~erik/STBC/Marines/",
            "Version": "0.9",
            "License": "GPL",
            "Description": "This script allows you to beam Troops over to another Ship",
            "needBridge": 0
            }

NonSerializedObjects = (
"pScienceScanWindow",
)

def TransferTroops(pObject, pEvent):
        debug(__name__ + ", TransferTroops")
        global dist, dict_Marines, p_ActiveTroops, g_pDatabase, TRANSFER_SHIELDON_TIMER, ShieldTurnOnShip
        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
        pFriendlies = pMission.GetFriendlyGroup()
        
        # Test if we have a Target
        if not pTarget:
                MarinesSay("BrexNoTarget")
                return

        # Test Distance
        if (Distance(pTarget) > 300):
                MarinesSay("TargetTooFar")
                return

        # Test if our Target is friendly
        if not pFriendlies.IsNameInGroup(pTarget.GetName()):
                MarinesSay("NoTransfer")
                return
        
        if (p_ActiveTroops == 0):
                MarinesSay("NoTroopsSelected")
                return
                
        if pPlayer.IsCloaked():
                MarinesSay("cloaked")
                return
                
        if not dict_Marines.has_key(str(pTarget)): # test if we already have this ship as Object
                dict_Marines[str(pTarget)] = Marineclass(pTarget)
        if not dict_Marines.has_key(str(pPlayer)): # same test for Player
                dict_Marines[str(pPlayer)] = Marineclass(pPlayer)
        
        if (dict_Marines[str(pTarget)].GetPeople() == 0):
                # This Ship does not have a crew, give it one.
                dict_Marines[str(pTarget)].SetPeople(p_ActiveTroops)
                # and set friendly AI:
                MarinesSetFriendlyAI(pTarget)
        else:
                dict_Marines[str(pTarget)].SetMarines(dict_Marines[str(pTarget)].GetMarines() + p_ActiveTroops)
        dict_Marines[str(pPlayer)].SetMarines(dict_Marines[str(pPlayer)].GetMarines() - p_ActiveTroops)
        
        # Play the sound and flicker Shields
        ftime1 = int(round(p_ActiveTroops / (pPlayer.GetHull().GetRadius() * 10)))
        ftime2 = int(round(p_ActiveTroops / (pTarget.GetHull().GetRadius() * 10)))
        if (ftime1 > ftime2): # We need the longer Interval
            ftime = ftime1
        else:
            ftime = ftime2

        if ( pPlayer.GetShields().IsOn() == 1 ):
                pSequence = App.TGSequence_Create()
                global g_pBrex
                pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)) # Brex
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, ftime)) # old Ship
                pSequence.Play()
        
        if ( pTarget.GetShields().IsOn() == 1 ):
                ShieldTurnOnShip = str(pTarget.GetName())
                pTarget.GetShields().TurnOff()
    
                # Timer from Self Destruct:
                # Create an event - it's a thing that will call this function
                pTimerEvent = App.TGEvent_Create()
                pTimerEvent.SetEventType(TRANSFER_SHIELDON_TIMER)
                pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

                # Create a timer - it's a thing that will wait for a given time,then do something
                pTimer = App.TGTimer_Create()
                pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + ftime + 2)
                pTimer.SetDelay(0)
                pTimer.SetDuration(0)
                pTimer.SetEvent(pTimerEvent)
                App.g_kTimerManager.AddTimer(pTimer)
        App.g_kSoundManager.PlaySound("Beam_Sound")

        # reset the Troops Button:
        resetTroopsButton(dict_Marines[str(pPlayer)].GetMarines(), p_ActiveTroops)


def Rescue(pObject, pEvent):
        debug(__name__ + ", Rescue")
        global dist, dict_Marines, p_ActiveTroops, g_pDatabase
        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
        pFriendlies = pMission.GetFriendlyGroup()
    
        # Test if we have a Target
        if not pTarget:
                MarinesSay("BrexNoTarget")
                return

        # Test Distance
        if (Distance(pTarget) > 300):
                MarinesSay("TargetTooFar")
                return

        # Test if our Target is friendly
        if not pFriendlies.IsNameInGroup(pTarget.GetName()):
                MarinesSay("NoTransfer")
                return
        
        # Test if our Target is really that damaged:
        if (pTarget.GetHull().GetConditionPercentage() > 0.3 and pTarget.GetPowerSubsystem().GetConditionPercentage() > 0.4) and (pTarget.GetHull().GetMaxCondition() > 2000):
                MarinesSay("NoRescue")
                return

        if pPlayer.IsCloaked():
                MarinesSay("cloaked")
                return
                
        if not dict_Marines.has_key(str(pTarget)): # test if we already have this ship as Object
                dict_Marines[str(pTarget)] = Marineclass(pTarget)
        if not dict_Marines.has_key(str(pPlayer)): # same test for Player
                dict_Marines[str(pPlayer)] = Marineclass(pPlayer)
        
        # Get the Beam time
        ftime = int(round((dict_Marines[str(pTarget)].GetMarines() + dict_Marines[str(pTarget)].GetPeople()) / (pPlayer.GetHull().GetRadius() * 10)))
   
        dict_Marines[str(pPlayer)].SetMarines(dict_Marines[str(pPlayer)].GetMarines() + dict_Marines[str(pTarget)].GetMarines())
        dict_Marines[str(pTarget)].SetMarines(0)
        dict_Marines[str(pPlayer)].SetPeople(dict_Marines[str(pPlayer)].GetPeople() + dict_Marines[str(pTarget)].GetPeople())
        dict_Marines[str(pTarget)].SetPeople(0)
        
        if ( pPlayer.GetShields().IsOn() == 1 ):
                pSequence = App.TGSequence_Create()
                global g_pBrex
                pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)) # Brex
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, ftime)) # old Ship
                pSequence.Play()
        
        if ( pTarget.GetShields().IsOn() == 1 ):
                ShieldTurnOnShip = str(pTarget.GetName())
                pTarget.GetShields().TurnOff()
                # No, we don't turn the Shields on again
        App.g_kSoundManager.PlaySound("Beam_Sound")

        # No one on board:
        import AI.Player.Stay
        pTarget.SetAI(AI.Player.Stay.CreateAI(pTarget))
        
        # reset the Troops Button:
        resetTroopsButton(dict_Marines[str(pPlayer)].GetMarines(), p_ActiveTroops)


def TransferGet(pObject, pEvent):
        debug(__name__ + ", TransferGet")
        global dist, dict_Marines, p_ActiveTroops, g_pDatabase
        
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pPlayer = MissionLib.GetPlayer()
        pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
        pFriendlies = pMission.GetFriendlyGroup()
    
        # Test if we have a Target
        if not pTarget:
                MarinesSay("BrexNoTarget")
                return

        # Test Distance
        if (Distance(pTarget) > 300):
                MarinesSay("TargetTooFar")
                return

        # Test if our Target is friendly
        if not pFriendlies.IsNameInGroup(pTarget.GetName()):
                MarinesSay("NoTransfer")
                return

        if pPlayer.IsCloaked():
                MarinesSay("cloaked")
                return
                
        if not dict_Marines.has_key(str(pTarget)): # test if we already have this ship as an Object
                dict_Marines[str(pTarget)] = Marineclass(pTarget)
        if not dict_Marines.has_key(str(pPlayer)): # same test for Player
                dict_Marines[str(pPlayer)] = Marineclass(pPlayer)
        
        MarinesFromOtherShip = int(dict_Marines[str(pTarget)].GetMarines() * (float(2)/3)) # can give us 2/3 of total Marines
        dict_Marines[str(pPlayer)].SetMarines(dict_Marines[str(pPlayer)].GetMarines() + MarinesFromOtherShip)
        dict_Marines[str(pTarget)].SetMarines(dict_Marines[str(pTarget)].GetMarines() - MarinesFromOtherShip)
        
        
        # Play the sound and flicker Shields
        ftime1 = int(round(MarinesFromOtherShip / (pPlayer.GetHull().GetRadius() * 10)))
        ftime2 = int(round(MarinesFromOtherShip / (pTarget.GetHull().GetRadius() * 10)))
        if (ftime1 > ftime2): # We need the longer Interval
            ftime = ftime1
        else:
            ftime = ftime2
        
        if ( pPlayer.GetShields().IsOn() == 1 ):
                pSequence = App.TGSequence_Create()
                global g_pBrex
                pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)) # Brex
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, ftime)) # old Ship
                pSequence.Play()
        
        if ( pTarget.GetShields().IsOn() == 1 ):
                ShieldTurnOnShip = str(pTarget.GetName())
                pTarget.GetShields().TurnOff()
    
                # Timer from Self Destruct:
                # Create an event - it's a thing that will call this function
                pTimerEvent = App.TGEvent_Create()
                pTimerEvent.SetEventType(TRANSFER_SHIELDON_TIMER)
                pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

                # Create a timer - it's a thing that will wait for a given time,then do something
                pTimer = App.TGTimer_Create()
                pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + ftime + 2)
                pTimer.SetDelay(0)
                pTimer.SetDuration(0)
                pTimer.SetEvent(pTimerEvent)
                App.g_kTimerManager.AddTimer(pTimer)
        App.g_kSoundManager.PlaySound("Beam_Sound")

        # reset the Troops Button:
        resetTroopsButton(dict_Marines[str(pPlayer)].GetMarines(), p_ActiveTroops)


def TransferShieldsOn(pObject, pEvent):
    debug(__name__ + ", TransferShieldsOn")
    global ShieldTurnOnShip
    
    pPlayer = MissionLib.GetPlayer()
    pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
    
    if pTarget:
        if (ShieldTurnOnShip == str(pTarget.GetName()) and pTarget.GetShields().IsOn() != 1):
            pTarget.GetShields().TurnOn()


def RecallTroops(pObject, pEvent):
        debug(__name__ + ", RecallTroops")
        global dict_Marines, dist, pSound, dict_Battles, g_pDatabase
        
        pPlayer = MissionLib.GetPlayer()
        pTarget = App.ShipClass_Cast(pPlayer.GetTarget())
        
        if not pTarget:
                MarinesSay("BrexNoTarget")
                return
                
        if (Distance(pTarget) > dist):
                MarinesSay("TargetTooFar")
                return

        if pPlayer.IsCloaked():
                MarinesSay("cloaked")
                return
                
        # try to find an offline Shield
        OfflineShield = -1        
        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                if (pTarget.GetShields().GetCurShields(Shield) < 200):
                        OfflineShield = Shield
        if (OfflineShield == -1):
                        MarinesSay("NoOfflineShield")
                        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                            print (Shield, pTarget.GetShields().GetCurShields(Shield))
                        return
                        
        if not dict_Marines.has_key(str(pTarget)): # test if we already have this ship as Object
                dict_Marines[str(pTarget)] = Marineclass(pTarget)
        
        OurMarinesOnShip = dict_Marines[str(pTarget)].GetEnemyMarinesOnShip()
        if OurMarinesOnShip == 0 or not dict_Battles.has_key(pTarget.GetObjID()):
            MarinesSay("NoMarinesOnTarget")
            return
        
        # else Beaming:
        dict_Marines[str(pPlayer)].SetMarines(dict_Marines[str(pPlayer)].GetMarines() + OurMarinesOnShip)
        # and 0 friendly Marines on enemy Ship:
        dict_Marines[str(pTarget)].SetEnemyMarinesOnShip(0)

	# Delete old Attack
	for pBattle in dict_Battles[pTarget.GetObjID()]:
		pBattle.pTimerProcess = None
	del dict_Battles[pTarget.GetObjID()]

        
        # Play the sound and flicker Shields
        ftime = (OurMarinesOnShip / (pPlayer.GetHull().GetRadius() * 10))
        print ("Troops need seconds:", ftime)

        if ( pPlayer.GetShields().IsOn() == 1 ):
                pSequence = App.TGSequence_Create()
                pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)) # Brex
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, ftime)) # old Ship
                pSequence.Play()
        App.g_kSoundManager.PlaySound("Beam_Sound")

        # rest the Troops Button:
        resetTroopsButton(dict_Marines[str(pPlayer)].GetMarines(), 0)


def Capture(pObject, pEvent):
        debug(__name__ + ", Capture")
        global p_ActiveTroops, dist, pSound, g_pDatabase, dict_Battles

        pPlayer = MissionLib.GetPlayer()
        pTarget = pPlayer.GetTarget()
        pSet = pPlayer.GetContainingSet()
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pEnemies = MissionLib.GetEnemyGroup()
        pFriendlies = pMission.GetFriendlyGroup()
        pClosest = None
        lpEnemies = pEnemies.GetActiveObjectTupleInSet(pSet)
        pTargetattr = App.ShipClass_Cast(pTarget)
        
        if not pTarget:
                MarinesSay("BrexNoTarget")
                return
                
        if (Distance(pTarget) > dist):
                MarinesSay("TargetTooFar")
                return

        if (pFriendlies.IsNameInGroup(pTarget.GetName()) == 1):
                MarinesSay("BrexTargetFriendly")
                return
        
        if (p_ActiveTroops == 0):
                MarinesSay("NoTroopsSelected")
                return

        if pPlayer.IsCloaked():
                MarinesSay("cloaked")
                return
                
        # try to find an offline Shield
        OfflineShield = -1        
        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                if (pTargetattr.GetShields().GetCurShields(Shield) < 200):
                        OfflineShield = Shield
        if (OfflineShield == -1):
                        MarinesSay("NoOfflineShield")
                        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                            print (Shield, pTargetattr.GetShields().GetCurShields(Shield))
                        return
                  
        EnemyPeople = GetNumPeople(pTargetattr)
        EnemyPeople = EnemyPeople + GetNumMarines(pTargetattr) # do it in two steps, else would create the Object two times
        pTargetSubsystem = pPlayer.GetTargetSubsystem()
                
        # Play the sound and flicker Shields
        ftime = (p_ActiveTroops / (pPlayer.GetHull().GetRadius() * 10))
        MarinesSay("ShieldDowntime", ftime)
        
        pSequence = App.TGSequence_Create()
        if ( pPlayer.GetShields().IsOn() == 1 ):
                pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)) # Brex
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, ftime)) # old Ship
        pSequence.Play()
        App.g_kSoundManager.PlaySound("Beam_Sound")
        
	if (dict_Marines[str(pPlayer)].GetMarines() < p_ActiveTroops):
		p_ActiveTroops = dict_Marines[str(pPlayer)].GetMarines()
	
        # Fight here
	if not dict_Battles.has_key(pTarget.GetObjID()):
		dict_Battles[pTarget.GetObjID()] = []
        dict_Battles[pTarget.GetObjID()].append(FightBattle(pPlayer, p_ActiveTroops, EnemyPeople, App.ShipClass_Cast(pTarget), pTargetSubsystem))


class FightBattle:
	def __init__(self, pShip, iNumPlayerMarines, iNumEnemyMarines, pTarget, pTargetSubsystem):
		debug(__name__ + ", __init__")
		self.pShip = pShip
		self.iNumPlayerMarines = iNumPlayerMarines
		self.iNumEnemyMarines = iNumEnemyMarines
		self.pTarget = pTarget
		self.pTargetSubsystem = pTargetSubsystem
		self.pTimerProcess = None
		self.SetupTimer()

		# 1. decrease Players Marine Number:
		dict_Marines[str(pShip)].SetMarines(dict_Marines[str(pShip)].GetMarines()- iNumPlayerMarines)
			
		# 2. Marines arrived:
		dict_Marines[str(pTarget)].SetEnemyMarinesOnShip(dict_Marines[str(pTarget)].GetEnemyMarinesOnShip() + iNumPlayerMarines)

		# reset the Troops Button:
		resetTroopsButton(dict_Marines[str(pShip)].GetMarines(), iNumPlayerMarines)

		if pTargetSubsystem.GetName() == pTarget.GetHull().GetName():
			# If we are trying to capture, we need at least 40s and up to 2min
			self.iCounterTime = 30 + App.g_kSystemWrapper.GetRandomNumber(80)
			self.PreCalculateCapture()
		else:
			# something between 10 and 20 seconds
			self.iCounterTime = 10 + App.g_kSystemWrapper.GetRandomNumber(10)
		print "Troops need %d seconds" % (self.iCounterTime)

	def SetupTimer(self):
		debug(__name__ + ", SetupTimer")
		if self.pTimerProcess:
			# We already have a timer.
			return

		self.pTimerProcess = App.PythonMethodProcess()
		self.pTimerProcess.SetInstance(self)
		self.pTimerProcess.SetFunction("Update")
		self.pTimerProcess.SetDelay(1.0)
		self.pTimerProcess.SetPriority(App.TimeSliceProcess.LOW)

	def Update(self, dTimeAvailable):
		debug(__name__ + ", Update")
		pFriendlies = MissionLib.GetFriendlyGroup()
		iOldNumMarines = self.iNumPlayerMarines
		
		# Make sure that Target is still not friendly
		if pFriendlies.IsNameInGroup(self.pTarget.GetName()):
			print("Attack was stopped")
			# Stop the Attack
			self.pTimerProcess = None
			# Add our attack crew to the Ship ones.
			dict_Marines[str(self.pTarget)].SetMarines(self.iNumPlayerMarines)
		elif self.pTargetSubsystem.GetName() == self.pTarget.GetHull().GetName():
			self.CaptureProcess()
		else:
			self.DamageSubsystem()

		if self.iCounterTime == 0:
			self.pTimerProcess = None
		self.iCounterTime = self.iCounterTime - 1
		
		iNewNumMarines = self.iNumPlayerMarines
		if iOldNumMarines != iNewNumMarines:
			iNumMarinesDiff = iOldNumMarines - iNewNumMarines
			dict_Marines[str(self.pTarget)].SetEnemyMarinesOnShip(dict_Marines[str(self.pTarget)].GetEnemyMarinesOnShip() - iNumMarinesDiff)

	def PreCalculateCapture(self):
		debug(__name__ + ", PreCalculateCapture")
		iNumDefenders = dict_Marines[str(self.pTarget)].GetPeople()
		if iNumDefenders > 0:
			fChance = float(self.iNumPlayerMarines) / iNumDefenders
		else:
			fChance = 1.0
		if fChance > 1.0:
			fChance = 1.0
		iChance = int(fChance*100)
		
		if chance(iChance):
			self.iCaptureWin = 1
		else:
			self.iCaptureWin = 0
		
		iNumPlayerMarinesLoosing = int((1-fChance)*100)
		if iNumPlayerMarinesLoosing > 0:
			iNumPlayerMarinesLoosing = int(self.iNumPlayerMarines * App.g_kSystemWrapper.GetRandomNumber(iNumPlayerMarinesLoosing) / 100.0)
		else:
			iNumPlayerMarinesLoosing = 0
		self.iPlayerMarinesLoosingPerSecond = iNumPlayerMarinesLoosing/self.iCounterTime
		
		iNumPeopleLoosing = int((fChance)*100)
		if iNumPeopleLoosing > 0:
			iNumPeopleLoosing = int(iNumDefenders * App.g_kSystemWrapper.GetRandomNumber(iNumPeopleLoosing) / 100.0)
		else:
			iNumPeopleLoosing = 0
		self.iNumPeopleLoosingPerSecond = iNumPeopleLoosing/self.iCounterTime
		print "%d vs %d" % (self.iNumPlayerMarines, iNumDefenders)
		print "Player will loose %d/round" % self.iPlayerMarinesLoosingPerSecond
		print "Enemy will loose %d/round" % self.iNumPeopleLoosingPerSecond
		
	def CaptureProcess(self):
		# Trying to capture the Ship
		debug(__name__ + ", CaptureProcess")
		pFriendlies = MissionLib.GetFriendlyGroup()
		pEnemies = MissionLib.GetEnemyGroup()

		if self.iCounterTime == 0:
			if self.iCaptureWin == 0:
				MarinesSay("MarinesLostCapture", "Felix")
				return
			MarinesSay("MarinesWonCapture", "Felix")
			# so we won the fight - make Target friendly:
			if pEnemies.IsNameInGroup(self.pTarget.GetName()):
				RemoveNameFromGroup(pEnemies, self.pTarget.GetName())
			# If this was the last Ship, there can be a Problem with the Enemy Group, so add a dummy
			if not pEnemies.GetNameTuple():
				pEnemies.AddName("This ship probably wont exist")
			# Finaly captured!
			pFriendlies.AddName(self.pTarget.GetName())
			autoAI(self.pTarget)

			dict_Marines[str(self.pTarget)].SetMarines(0) # they don't have any Marines
			dict_Marines[str(self.pTarget)].SetPeople(self.iNumPlayerMarines) # and the capturing Marines are the crew now
		# we will loose people by fighting
		else:
			self.iNumPlayerMarines = self.iNumPlayerMarines - self.iPlayerMarinesLoosingPerSecond
			dict_Marines[str(self.pTarget)].SetPeople(dict_Marines[str(self.pTarget)].GetPeople()-self.iNumPeopleLoosingPerSecond)

	def DamageSubsystem(self):
		# Target is a subsystem...trying to damage:
		debug(__name__ + ", DamageSubsystem")
		iNumPeopleInSubsystem = int(self.pTargetSubsystem.GetRadius() * 100 * self.pTargetSubsystem.GetConditionPercentage())
		if iNumPeopleInSubsystem > 0:
			fChance = float(self.iNumPlayerMarines) / iNumPeopleInSubsystem
		else:
			fChance = 1.0
		if fChance > 1.0:
			fChance = 1.0
		
		iChance = int(fChance*100)
		iDamage = 0
		if iChance > 0:
			iDamage = App.g_kSystemWrapper.GetRandomNumber(iChance)
		self.pTargetSubsystem.SetConditionPercentage(self.pTargetSubsystem.GetConditionPercentage()-iDamage/100.0)
		iNumPlayerMarinesLoosing = int((1-fChance)*100)
		if iNumPlayerMarinesLoosing > 0:
			iNumPlayerMarinesLoosing = int(self.iNumPlayerMarines * App.g_kSystemWrapper.GetRandomNumber(iNumPlayerMarinesLoosing) / 100.0)
		else:
			iNumPlayerMarinesLoosing = 0
		self.iNumPlayerMarines = self.iNumPlayerMarines - iNumPlayerMarinesLoosing

		if self.pTargetSubsystem.GetCondition() < 0.01 or self.iCounterTime == 0:
			self.pTarget.DestroySystem(self.pTargetSubsystem)
			BeamBack(self.iNumPlayerMarines, self.pTarget)
			self.pTimerProcess = None
			return
		elif self.iNumPlayerMarines == 0:
			MarinesSay("MarinesLostCapture", "Felix")
			self.pTimerProcess = None
			return


#def FightBattle(pShip, PlayerMarines, EnemyMarines, pTarget, pTargetSubsystem):
#        global dict_Marines, p_ActiveTroops, MARINES_FIGHT_TIMER, dict_Battles
#
#        if not dict_Marines.has_key(str(pShip)):
#                dict_Marines[str(pShip)] = Marineclass(pShip)
#        # 1. decrease Players Marine Number:
#        dict_Marines[str(pShip)].SetMarines(dict_Marines[str(pShip)].GetMarines()- PlayerMarines)
#        if (dict_Marines[str(pShip)].GetMarines() <= p_ActiveTroops):
#                p_ActiveTroops = dict_Marines[str(pShip)].GetMarines()
#        
#        # 2. Marines arrived:
#        dict_Marines[str(pTarget)].SetEnemyMarinesOnShip(dict_Marines[str(pTarget)].GetEnemyMarinesOnShip() + p_ActiveTroops)
#        
#        # rest the Troops Button:
#        resetTroopsButton(dict_Marines[str(pShip)].GetMarines(), p_ActiveTroops)
#        
#	# Create an event - it's a thing that will call this function
#	pTimerEvent = App.TGEvent_Create()
#	pTimerEvent.SetEventType(MARINES_FIGHT_TIMER)
#	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())
#
#        if (pTargetSubsystem.GetName() == pTarget.GetHull().GetName()):
#                # If we are trying to capture, we need at least 40s and up to 2min
#                CounterTime = 30 + App.g_kSystemWrapper.GetRandomNumber(80)
#        else:
#                # something between 10 and 20 seconds
#                CounterTime = 10 + App.g_kSystemWrapper.GetRandomNumber(10)
#        
#        print ("Troops need seconds:", CounterTime)
#        
#        EndBattleTime = App.g_kUtopiaModule.GetGameTime() + CounterTime
#
#	# Create a timer - it's a thing that will wait for a given time,then do something
#	pTimer = App.TGTimer_Create()
#	pTimer.SetTimerStart(EndBattleTime)
#	pTimer.SetDelay(0)
#	pTimer.SetDuration(0)
#	pTimer.SetEvent(pTimerEvent)
#	App.g_kTimerManager.AddTimer(pTimer)
#
#       dict_Battles[str(pTimerEvent)] = (pShip, PlayerMarines, EnemyMarines, pTarget, pTargetSubsystem)


pButtonSelectTroops = None

def resetTroopsButton(max_Marines, p_ActiveTroops2):
        debug(__name__ + ", resetTroopsButton")
        global pButtonSelectTroops, p_ActiveTroops
        p_ActiveTroops = p_ActiveTroops2
        if (p_ActiveTroops > max_Marines):
            p_ActiveTroops = 0
        pButtonSelectTroops.SetName(App.TGString('Troops(Max:' + str(max_Marines) + '): ' + str(p_ActiveTroops)))

    
def EndBattle(pObject, pEvent):
        debug(__name__ + ", EndBattle")
        global dict_Marines, p_ActiveTroops, dict_Battles
            
        if not dict_Battles.has_key(str(pEvent)):
            print("Attack was stopped")
            return
        pShip                   = dict_Battles[str(pEvent)][0]
        PlayerMarines           = dict_Battles[str(pEvent)][1]
        EnemyMarines            = dict_Battles[str(pEvent)][2]
        pTarget                 = dict_Battles[str(pEvent)][3]
        pTargetSubsystem        = dict_Battles[str(pEvent)][4]

        if not pTarget: # Make sure the ship still exists
            print("Attack was stopped")
            return
        pGame = App.Game_GetCurrentGame()
        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pFriendlies = pMission.GetFriendlyGroup()
        pEnemies = MissionLib.GetEnemyGroup()
        pTargetattr = pTarget # it is already a shipclass cast!

        # Make sure that Target is really enemy
        if not pEnemies.IsNameInGroup(pTarget.GetName()):
                print("Attack was stopped")
                # Stop the Attack
                i = 0
                list = dict_Battles.values()
                while (i != len(dict_Battles)):
                        if (str(list[i][3]) == str(pTarget)): # we are trying to find our attack Groups by comparing the Target field with our Target
                                dict_Battles[dict_Battles.keys()[i]] = (0, 0, 0, 0, 0)
                        i = i + 1
                # Add our attack crew to the Ship ones.
                dict_Marines[str(pTarget)].SetMarines(PlayerMarines)
                return
            
        
        if (pTargetSubsystem.GetName() == pTargetattr.GetHull().GetName()):
                #print("Trying to capture the Ship")
                cWin    = int(float(PlayerMarines) / EnemyMarines * 100) # One Number has to be float, result int
		cRandom = App.g_kSystemWrapper.GetRandomNumber(100)
		if cWin < 1:
			if (cRandom > cWin):
				MarinesSay("MarinesLostCapture", "Felix")
				return
		else:
			if (cRandom > 95 + cWin):
				MarinesSay("MarinesLostCapture", "Felix")
				return
                        MarinesSay("MarinesWonCapture", "Felix")
                        # so we won the fight - make Target friendly:
                        if pEnemies.IsNameInGroup(pTarget.GetName()):
                                RemoveNameFromGroup(pEnemies, pTarget.GetName())
                        # If this is the last Ship, there can be a Problem with the Enemy Group, so add a dummy
                        if not pEnemies.GetNameTuple():
                                pEnemies.AddName("nothing")
                        # Finaly captured!
                        pFriendlies.AddName(pTarget.GetName())
                        MarinesSetFriendlyAI(pTarget)
			if (cWin < 100):
				value = PlayerMarines * (cRandom / 125)
			else:
				value = PlayerMarines * (cRandom / 500)
			PlayerMarinesLoosing = int(value)
                        # But they don't have any Marines
                        dict_Marines[str(pTarget)].SetMarines(0)
                        dict_Marines[str(pTarget)].SetPeople(PlayerMarines - PlayerMarinesLoosing) # and the capturing Marines are the crew now
        else:
		#print("Target is a subsystem...trying to damage:")
		PeopleInSubsystem = int(pTargetSubsystem.GetRadius() * 100 * (pTargetSubsystem.GetMaxCondition() / pTargetSubsystem.GetCondition()))
		cWin    = int(float(PlayerMarines) / PeopleInSubsystem * 100) # One Number has to be float, result int
		cRandom = App.g_kSystemWrapper.GetRandomNumber(100)
		if cWin < 1:
			if (cRandom > cWin):
				MarinesSay("MarinesLostCapture", "Felix")
				return
			else:
				value = float(cRandom - cWin) / 100
		else:
			value = float(cWin - cRandom) / 100
		# some calculations...
		tDamage = pTargetSubsystem.GetConditionPercentage() - value
		if (tDamage < 0.01): # Protection: We don't want a System with HP <0
			pTarget.DestroySystem(pTargetSubsystem)
		else:
			pTargetSubsystem.SetConditionPercentage(tDamage)
		if (cWin < 100):
			value = PlayerMarines * (cRandom / 125)
		else:
			value = PlayerMarines * (cRandom / 500)
		PlayerMarinesLoosing = int(value)
		BeamBack(PlayerMarines - PlayerMarinesLoosing, pTarget)

                Value = cRandom - cWin
                if Value < 0:
                        Value = cWin - cRandom
		EnemyMarinesLoosing = int(PeopleInSubsystem * App.g_kSystemWrapper.GetRandomNumber(Value + 1)) / 100
		EnemyPeopleLoosing = int(float(dict_Marines[str(pTargetattr)].GetPeople()) / dict_Marines[str(pTargetattr)].GetMarines() * EnemyMarinesLoosing)
		dict_Marines[str(pTargetattr)].SetMarines(dict_Marines[str(pTargetattr)].GetMarines() - EnemyMarinesLoosing)
		dict_Marines[str(pTargetattr)].SetPeople(dict_Marines[str(pTargetattr)].GetPeople() - EnemyPeopleLoosing)


def BeamBack(PlayerMarines, pTarget):
        debug(__name__ + ", BeamBack")
        global dict_Marines, dist, pSound, g_pDatabase
        pPlayer = MissionLib.GetPlayer()
        pTargetattr = pTarget # yes - it is the same
        
        # Shields have to be still offline
        OfflineShield = -1        
        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                if (pTargetattr.GetShields().GetCurShields(Shield) < 200):
                        OfflineShield = Shield
        if (OfflineShield == -1 or Distance(pTarget) > dist):
                        print ("No offline Shield or Distance to high: can't save Troops...Troops are now trying to capture Ship")
                        for Shield in range(App.ShieldClass.NUM_SHIELDS):
                            print (Shield, pTargetattr.GetShields().GetCurShields(Shield))
                            EnemyPeople = GetNumPeople(pTarget) + GetNumMarines(pTarget)
                            FightBattle(pPlayer, PlayerMarines, EnemyPeople, pTarget, pTarget.GetHull())
                        return
                
        ftime = (PlayerMarines / (pPlayer.GetHull().GetRadius() * 10))
        pSequence = App.TGSequence_Create()
        if ( pPlayer.GetShields().IsOn() == 1 ):
                pSequence.AppendAction(App.CharacterAction_Create(g_pBrex, App.CharacterAction.AT_SAY_LINE, "LoweringShields", None, 0, g_pDatabase)) # Brex
                pSequence.AppendAction(App.TGScriptAction_Create("Actions.ShipScriptActions", "FlickerShields", 0, ftime)) # old Ship
        pSequence.Play()
        App.g_kSoundManager.PlaySound("Beam_Sound")
        
        # increase our Marines number
        dict_Marines[str(pPlayer)].SetMarines(dict_Marines[str(pPlayer)].GetMarines()+ PlayerMarines)
        # and 0 friendly Marines on enemy Ship:
        dict_Marines[str(pTarget)].SetEnemyMarinesOnShip(0)
    

# captuered..reset AI
def MarinesSetFriendlyAI(pTarget):
        debug(__name__ + ", MarinesSetFriendlyAI")
        pTargetattr = pTarget # same here - pTarget is already a cast
        # set AI
	if (pTargetattr.GetShipProperty().IsStationary() == 1):
		# its a Station
		pTargetattr.SetAI(Lib.LibEngineering.CreateStarbaseFriendlyAI(pTargetattr))
	else:
		pTargetattr.SetAI(Lib.LibEngineering.CreateFriendlyAI(pTargetattr))


# change the Button
def SelectTroops(pObject, pEvent):
    debug(__name__ + ", SelectTroops")
    global pButtonSelectTroops, c_pTroops, p_MaxTroops, p_ActiveTroops, dict_Marines
    
    pPlayer = MissionLib.GetPlayer()
    
    if not dict_Marines.has_key(str(pPlayer)):
        dict_Marines[str(pPlayer)] = Marineclass(pPlayer)
    p_MaxTroops = dict_Marines[str(pPlayer)].GetMarines()
    
    # If we start clicking from 0
    if (p_ActiveTroops == p_MaxTroops):
        p_ActiveTroops = 0
    elif (p_ActiveTroops + 5 > p_MaxTroops):
        p_ActiveTroops = p_MaxTroops
    elif (p_ActiveTroops < 5):
        p_ActiveTroops = 5
    else:
        p_ActiveTroops = p_ActiveTroops + 5
    
    pButtonSelectTroops.SetName(App.TGString('Troops(Max:' + str(p_MaxTroops) + '): ' + str(p_ActiveTroops)))
    

# Get the Distance between the Player and pObject - made by Banbury for QBR
def Distance(pObject):
	debug(__name__ + ", Distance")
	pPlayer = App.Game_GetCurrentPlayer()
	vDifference = pObject.GetWorldLocation()
	vDifference.Subtract(pPlayer.GetWorldLocation())

	return vDifference.Length()


# Actually from ReturnShuttles
def GetNumMarines(pShip):
        debug(__name__ + ", GetNumMarines")
        global dict_Marines
        
        if not dict_Marines.has_key(str(pShip)):
            dict_Marines[str(pShip)] = Marineclass(pShip)
        return dict_Marines[str(pShip)].GetMarines()


# same... from ReturnShuttles
def GetNumPeople(pShip):
        debug(__name__ + ", GetNumPeople")
        global dict_Marines
        
        if not dict_Marines.has_key(str(pShip)):
            dict_Marines[str(pShip)] = Marineclass(pShip)
        return dict_Marines[str(pShip)].GetPeople()


# Restart is called by Engineering Extension on ...well restart
def Restart():
    debug(__name__ + ", Restart")
    global pGame_old, dict_Marines, pButtonSelectTroops, p_ActiveTroops, dict_Battles
    pGame = App.Game_GetCurrentGame()

    # test if the restart is only Called by ftb!
    if (str(pGame) == pGame_old):
        #print("Game havn't changed - return.")
        return
    pGame_old = str(pGame)
    
    pPlayer = App.Game_GetCurrentPlayer()
    dict_Marines = {}
    dict_Battles = {}
    p_ActiveTroops = 0
    if not dict_Marines.has_key(str(pPlayer)):
            dict_Marines[str(pPlayer)] = Marineclass(pPlayer)
    if pButtonSelectTroops:
            pButtonSelectTroops.SetName(App.TGString('Troops(Max:' + str(dict_Marines[str(pPlayer)].GetMarines()) + '): ' + str(p_ActiveTroops)))

    # clear the Science Pane
    if pScienceScanWindow:
        pScienceScanWindow.KillChildren()


def ScanInit(pObject, pEvent):
        debug(__name__ + ", ScanInit")
        global SCAN_TIMER, EVENT_SCAN_TARGET, pScienceScanWindow
                
        EVENT_SCAN_TARGET = pEvent.GetInt()

	# call first
        pObject.CallNextHandler(pEvent)
        
        # clear the Science Pane
        if not pScienceScanWindow:
                CreateSciencePane()
        else:
                pScienceScanWindow.KillChildren()
        
        # Create an event - it's a thing that will call this function
	pTimerEvent = App.TGEvent_Create()
	pTimerEvent.SetEventType(SCAN_TIMER)
	pTimerEvent.SetDestination(App.TopWindow_GetTopWindow())

	CounterTime = 10.0
	
	# Create a timer - it's a thing that will wait for a given time,then do something
	pTimer = App.TGTimer_Create()
	pTimer.SetTimerStart(App.g_kUtopiaModule.GetGameTime() + CounterTime)
	pTimer.SetDelay(0)
	pTimer.SetDuration(0)
	pTimer.SetEvent(pTimerEvent)
	App.g_kTimerManager.AddTimer(pTimer)


def GetShipType(pShip):
        debug(__name__ + ", GetShipType")
        if pShip.GetScript():
                return string.split(pShip.GetScript(), '.')[-1]
        return None


def MarinesScan(pObject, pEvent):
        debug(__name__ + ", MarinesScan")
        global dict_Marines, pScienceScanWindow, EVENT_SCAN_TARGET
    
        iType = EVENT_SCAN_TARGET

        pPlayer         = MissionLib.GetPlayer()
        if not pPlayer:
                return
        pGame           = App.Game_GetCurrentGame()
        pSensors        = pPlayer.GetSensorSubsystem()
        pTarget         = App.ShipClass_Cast(pPlayer.GetTarget())
        pSet            = pPlayer.GetContainingSet()
        pEpisode	= pGame.GetCurrentEpisode()
        pMission	= pEpisode.GetCurrentMission()
        pEnemyGroup     = MissionLib.GetEnemyGroup()
        lpEnemys        = pEnemyGroup.GetActiveObjectTupleInSet(pSet)
        pFriendlyGroup  = MissionLib.GetFriendlyGroup()
        lpFriendlies    = pFriendlyGroup.GetActiveObjectTupleInSet(pSet)
        x2              = 0.2
        x3              = 0.4
        countWeapons    = 0
        
        # check sensors
        if not pSensors or pSensors.IsDisabled():
                print "No sensors. Not Scanning."
                return

        if not pScienceScanWindow:
                CreateSciencePane()
        else:
                pScienceScanWindow.KillChildren()

        if (pEvent.GetSource()):
                if (App.ObjectClass_Cast(pEvent.GetSource())):
                        pTarget = App.ObjectClass_Cast(pEvent.GetSource())
        
        if (iType == App.CharacterClass.EST_SCAN_OBJECT):
                if (pTarget):
                        pTractorText = App.TGParagraph_CreateW(App.TGString("Scanning Target:"))
                        pScienceScanWindow.AddChild(pTractorText, 0, 0, 0)
                        y = 0.02
			# Check roids:
                        if pTarget and pTarget.GetScript() and (string.find(pTarget.GetScript(), 'Asteroid') != -1 or string.find(pTarget.GetScript(), 'Comet') != -1):
                                randall = 0
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Nicle:")), 0, y, 0)
                                rand = App.g_kSystemWrapper.GetRandomNumber(25)
                                randall = randall + rand
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(rand) + "%")), x2, y, 0)
				y = y + 0.02
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Duranium:")), 0, y, 0)
                                rand = App.g_kSystemWrapper.GetRandomNumber(25)
                                randall = randall + rand
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(rand) + "%")), x2, y, 0)
				y = y + 0.02
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Iron:")), 0, y, 0)
                                rand = App.g_kSystemWrapper.GetRandomNumber(25)
                                randall = randall + rand
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(rand) + "%")), x2, y, 0)
				y = y + 0.02
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Ice:")), 0, y, 0)
                                rand = App.g_kSystemWrapper.GetRandomNumber(25)
                                randall = randall + rand
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(rand) + "%")), x2, y, 0)
				y = y + 0.02
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Misc:")), 0, y, 0)
                                rand = 100 - randall
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(rand) + "%")), x2, y, 0)
				y = y + 0.02
			else:
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Shipname:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(pTarget.GetName()))), x2, y, 0)
				y = y + 0.02
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Shiptype:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(GetShipType(pTarget)))), x2, y, 0)
				y = y + 0.02
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Target:")), 0, y, 0)
				if pTarget.GetTarget():
					pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(pTarget.GetTarget().GetName()))), x2, y, 0)
				else:
					pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("None")), x2, y, 0)
				y = y + 0.02
		
				# print critical Status
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Hull Strength:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("%0.f" % pTarget.GetHull().GetCondition())), x2, y, 0)
				y = y + 0.02
				
				if not dict_Marines.has_key(str(pTarget)): # test if we already have this ship as Object
					dict_Marines[str(pTarget)] = Marineclass(pTarget)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("total Crew:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(dict_Marines[str(pTarget)].GetPeople() + dict_Marines[str(pTarget)].GetMarines()))), x2, y, 0)
				y = y + 0.02
				# Cycle through the subsystems:
				averageStatus = 0
				criticalStatus = 0
				count_critical = 0
				WeaponsOnOff = 0
				pPropSet = pTarget.GetPropertySet()
				pShipSubSystemPropInstanceList = pPropSet.GetPropertiesByType(App.CT_SUBSYSTEM_PROPERTY)
				iNumItems = pShipSubSystemPropInstanceList.TGGetNumItems()
				pShipSubSystemPropInstanceList.TGBeginIteration()
				for i in range(iNumItems):
					pInstance = pShipSubSystemPropInstanceList.TGGetNext()
					pProperty = pTarget.GetSubsystemByProperty(App.SubsystemProperty_Cast(pInstance.GetProperty()))
					# 1. Get Average Status of All Systems
					averageStatus = averageStatus + pProperty.GetConditionPercentage()
					# 2. Find critical Systems and get their Average
					if pProperty.IsCritical():
						criticalStatus = criticalStatus + pProperty.GetConditionPercentage()
						count_critical = count_critical + 1
					
					
				pShipSubSystemPropInstanceList.TGDoneIterating()
				pShipSubSystemPropInstanceList.TGDestroy()
				
				# print System Status
				averageStatus = int((averageStatus / iNumItems)*100)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("average Status:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(averageStatus) + "%")), x2, y, 0)
				y = y + 0.02
				
				# print critical Status
				criticalStatus = int((criticalStatus / count_critical)*100)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("avg critival Status:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(criticalStatus) + "%")), x2, y, 0)
				y = y + 0.02
				
				# 3. The Weapons:
				if pTarget.GetPhaserSystem():
					WeaponStatus1 = pTarget.GetPhaserSystem().GetCombinedConditionPercentage()
					countWeapons = countWeapons + 1
					if pTarget.GetPhaserSystem().IsOn():
					        WeaponsOnOff = 1
				else:
					WeaponStatus1 = 0
				if pTarget.GetTorpedoSystem():
					WeaponStatus2 = pTarget.GetTorpedoSystem().GetCombinedConditionPercentage()
					countWeapons = countWeapons + 1
					if pTarget.GetTorpedoSystem().IsOn():
						WeaponsOnOff = 1
				else:
					WeaponStatus2 = 0
				if pTarget.GetPulseWeaponSystem():
					WeaponStatus3 = pTarget.GetPulseWeaponSystem().GetCombinedConditionPercentage()
					countWeapons = countWeapons + 1
					if pTarget.GetPulseWeaponSystem().IsOn():
					        WeaponsOnOff = 1
				else:
					WeaponStatus3 = 0
				
				if (countWeapons == 0):
					WeaponStatus = 0
				else:
					WeaponStatus = int(((WeaponStatus1 + WeaponStatus2 + WeaponStatus3) / countWeapons)*100)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("avg Weapon Status:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(WeaponStatus) + "%")), x2, y, 0)
				y = y + 0.02
				
				# 4. Shields:
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Shield Status:")), 0, y, 0)
				if pTarget.GetShields():
					for Shield in range(App.ShieldClass.NUM_SHIELDS):
						pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(pTarget.GetShields().GetCurShields(Shield)))), x2, y, 0)
						y = y + 0.02
				else:
					pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("None")), x2, y, 0)
					y = y + 0.02
	
				# Torpedos
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Torpedo counts:")), 0, y, 0)
				if pTarget.GetTorpedoSystem():
					TorpSubSys = pTarget.GetTorpedoSystem()
					iNumTorpTypes = TorpSubSys.GetNumAmmoTypes()
					for iType in range(iNumTorpTypes):
						pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(TorpSubSys.GetAmmoType(iType).GetAmmoName()) + ': ' + str(TorpSubSys.GetNumAvailableTorpsToType(iType)))), x2, y, 0)
						y = y + 0.02
				else:
					pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("None")), x2, y, 0)
					y = y + 0.02
				# Position
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Position:")), 0, y, 0)
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(pTarget.GetWorldLocation().GetX()) + ", " + str(pTarget.GetWorldLocation().GetY()) + ", " + str(pTarget.GetWorldLocation().GetZ()))), x2, y, 0)
				y = y + 0.02
				# Weapons on/offline
				pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Weapon status:")), 0, y, 0)
				if (WeaponsOnOff == 1):
					pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("online")), x2, y, 0)
				else:
					pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("offline")), x2, y, 0)
				y = y + 0.02                        

        if (iType == App.CharacterClass.EST_SCAN_AREA):
                pText = App.TGParagraph_CreateW(App.TGString("Scanning Area:"))
                pScienceScanWindow.AddChild(pText, 0, 0, 0)
                y = 0.02
                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("System name: " + str(pPlayer.GetContainingSet().GetName()))), 0, y, 0)
                y = y + 0.02
                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Shipname:")), 0, y, 0)
                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Target:")), x2, y, 0)
                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Position:")), x3, y, 0)
                for pObject in pSet.GetClassObjectList(App.CT_SHIP):
			pShip = App.ShipClass_Cast(pObject)
			if not pShip:
				continue
                        if not pFriendlyGroup.IsNameInGroup(pShip.GetName()) and ((pShip.IsCloaked() or not pShip.IsTargetable()) and App.g_kSystemWrapper.GetRandomNumber(100) > 10): # Small chance to see cloaked ships
                                continue
                        y = y + 0.02
                        pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(pShip.GetName()) + ": ")), 0, y, 0)
                        
                        if pShip.IsCloaked():
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("cloaked")), x2, y, 0)
                        elif pShip.GetTarget():
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(pShip.GetTarget().GetName()))), x2, y, 0)
                        else:
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("None")), x2, y, 0)
                        pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(str(int(round(pShip.GetWorldLocation().GetX(), 2))) + ", " + str(int(round(pShip.GetWorldLocation().GetY(), 2))) + ", " + str(int(round(pShip.GetWorldLocation().GetZ(), 2))))), x3, y, 0)
                y = y + 0.04
                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString("Warp signatures:")), 0, y, 0)
                for key in dict_Warp.keys():
                        # only Warp signatures from this Set and maximum of 60 seconds ago:
                        if pSet.GetName() == dict_Warp[key][1] and App.g_kUtopiaModule.GetGameTime() <= dict_Warp[key][3] + 60:
                                y = y + 0.02
                                SystemNameList = string.split(dict_Warp[key][2], ".")
                                SystemName = SystemNameList[-1:][0]
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(dict_Warp[key][0])), 0, y, 0)
                                pScienceScanWindow.AddChild(App.TGParagraph_CreateW(App.TGString(SystemName)), x2, y, 0)
        
        pScienceScanWindow.InteriorChangedSize()
        # rebuild Pane
        if pScienceScanWindow.IsVisible():
            #pScienceScanWindow.SetFixedSize(0.6, 0.5)
            #pScienceScanWindow.Resize(pScienceScanWindow.GetMaximumWidth(), pScienceScanWindow.GetMaximumHeight())
            pScienceScanWindow.Layout()


def exit():
        debug(__name__ + ", exit")
        global pScienceScanWindow
        
        if pScienceScanWindow: # can someone tell me why this doesn't work?
                # reloading is still crashing the game :(
                pScienceScanWindow.KillChildren()
                pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
                pTacticalControlWindow.DeleteChild(pScienceScanWindow)
	pScienceScanWindow = None


def CreateSciencePane(pObject=None, pEvent=None):
        debug(__name__ + ", CreateSciencePane")
        global pScienceScanWindow
        
        # Create the Scan output Window:
        pScienceScanWindow = App.STStylizedWindow_CreateW("StylizedWindow", "NormalStyle", App.TGString("Scan output"), 0.0, 0.0, None, 1, 0.6, 0.5)
        pScienceScanWindow.SetUseScrolling(1)
        
	pTacticalControlWindow = App.TacticalControlWindow_GetTacticalControlWindow()
        pTacticalControlWindow.AddChild(pScienceScanWindow, 0.4, 0.0)
        
        pScienceScanWindow.SetNotVisible()


def HandleScanMenuEvent(pObject, pEvent):
        debug(__name__ + ", HandleScanMenuEvent")
        global pScienceScanWindow
                
        if pScienceScanWindow:
            if (pEvent.GetBool() == 1): # Boolean: On 1 we open him, on 0 we close
                pScienceScanWindow.SetVisible()
            else:
                pScienceScanWindow.SetNotVisible()
        #else:
                 #CreateSciencePane()

	# All done, call the next handler
	pObject.CallNextHandler(pEvent)


def ShowScanWindow(pObject, pEvent):
        debug(__name__ + ", ShowScanWindow")
        global pScienceScanWindow
        
        if pScienceScanWindow:
                if not pScienceScanWindow.IsVisible():
                        pScienceScanWindow.SetVisible()
                else:
                        pScienceScanWindow.SetNotVisible()
        


def MarinesSay(SayString, Person = "Brex"):
        debug(__name__ + ", MarinesSay")
        global MarinesDatabase, g_pBrex, pBridge
        g_pFelix = App.CharacterClass_GetObject(pBridge, "Tactical") 

        if (Person == "Felix"):
            Person = g_pFelix
        else:
            Person = g_pBrex
        pSequence = App.TGSequence_Create()
        pSequence.AppendAction(App.CharacterAction_Create(Person, App.CharacterAction.AT_SAY_LINE, SayString, None, 0, MarinesDatabase))
        pSequence.Play()    


def StartWarpHandler(pObject, pEvent):
        debug(__name__ + ", StartWarpHandler")
        global dict_Warp
        
        pPlayer = MissionLib.GetPlayer()
        if not pPlayer:
                return
        
        # Get the ship doing the warping.
        pShip = App.ShipClass_Cast(pEvent.GetDestination())
        # Okay, we've got the player's ship.  Now check where he's going.
	if hasattr(pEvent, "GetDestinationSetName"):
		pcDestinationSetName = pEvent.GetDestinationSetName()
	else:
		pTravel = App.g_kTravelManager.GetTravel(pShip)
		if not pTravel or not pTravel.DestSet:
			return
		pcDestinationSetName = pTravel.DestSet.GetName()

        # our current Set:
        pSet = pPlayer.GetContainingSet()
        
        if pShip and pcDestinationSetName and pSet:
		if pShip and pSet:
                	key = pSet.GetName() + pShip.GetName()
                	dict_Warp[key] = [pShip.GetName(), pSet.GetName(), pcDestinationSetName, App.g_kUtopiaModule.GetGameTime()]
        
        pObject.CallNextHandler(pEvent)


def TractorTargetDocked(pObject, pEvent):
	debug(__name__ + ", TractorTargetDocked")
	pObject.CallNextHandler(pEvent)
	
	# Get the object that was docked and it's name
	pShip	= App.ShipClass_Cast(pEvent.GetObjPtr())
	pDockingShip	= App.ShipClass_Cast(pEvent.GetDestination())
	if not pShip or not pDockingShip:
		return
	
	if not IsSameGroup(pShip, pDockingShip) and not IsSameRace(pShip, pDockingShip) and string.find(pShip.GetScript(), "EscapePod") == -1:
		return
	
	if not dict_Marines.has_key(str(pDockingShip)):
		dict_Marines[str(pDockingShip)] = Marineclass(pDockingShip)
	
	iShipMarines = 0
	if dict_Marines.has_key(str(pShip)):
		iShipMarines = dict_Marines[str(pShip)].GetMarines() + dict_Marines[str(pShip)].GetPeople()
	elif string.find(pShip.GetScript(), 'Pod') != -1:
		iShipMarines = App.g_kSystemWrapper.GetRandomNumber(pShip.GetHull().GetRadius() * 1000 + 10)
	
	print "Adding %d extra Marines" % iShipMarines
	dict_Marines[str(pDockingShip)].SetMarines(dict_Marines[str(pDockingShip)].GetMarines() + iShipMarines)


# init() - QBautostart Extension >= 0.5
def init():
        debug(__name__ + ", init")
        global pBrexMenu, g_pBrex, pScienceMenu, g_pScience, pButtonSelectTroops, useFTB, pBridge
        
        pBridge = App.g_kSetManager.GetSet('bridge')
        g_pBrex = App.CharacterClass_GetObject(pBridge, 'Engineer')
        pBrexMenu = Lib.LibEngineering.GetBridgeMenu("Engineer")
        g_pScience = App.CharacterClass_GetObject(pBridge, "Science") 
        pScienceMenu = Lib.LibEngineering.GetBridgeMenu("Science")
        pMission = MissionLib.GetMission()

	# Marines disabled. Crews now by DS9FX
        #if (useFTB != -1) and not App.g_kUtopiaModule.IsMultiplayer():
        #        # oh found it - here we create the Buttons :)
        #        pMasterButtonMarines = App.STCharacterMenu_CreateW(App.TGString("Away Team"))
        #        
        #        pMasterButtonTransfer = App.STCharacterMenu_CreateW(App.TGString("Transfer"))
        #        
        #        Lib.LibEngineering.CreateMenuButton("Capture", "Engineer", __name__ + ".Capture", 0, pMasterButtonMarines)

        #        pButtonSelectTroops = Lib.LibEngineering.CreateMenuButton('Troops: ' + str(p_ActiveTroops), "Engineer", __name__ + ".SelectTroops", 0, pMasterButtonMarines)

        #        Lib.LibEngineering.CreateMenuButton("Recall Troops", "Engineer", __name__ + ".RecallTroops", 0, pMasterButtonMarines)
        #
        #        Lib.LibEngineering.CreateMenuButton("Get", "Engineer", __name__ + ".TransferGet", 0, pMasterButtonTransfer)

        #        Lib.LibEngineering.CreateMenuButton("Donate", "Engineer", __name__ + ".TransferTroops", 0, pMasterButtonTransfer)
        #
        #        Lib.LibEngineering.CreateMenuButton("Rescue", "Engineer", __name__ + ".Rescue", 0, pMasterButtonTransfer)

        #        # This Event Handler is for our Timer, how long the Troops will fight
        #        #App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(MARINES_FIGHT_TIMER, __name__ + ".EndBattle")
        #        # And this is the for the Timer how long until turning Shields back on for Transfer
        #        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(TRANSFER_SHIELDON_TIMER, __name__ + ".TransferShieldsOn")
        #        
        #        # add it here, not earlier, so we don't break the engineering menu with Borg Ships?!?
        #        pMasterButtonMarines.PrependChild(pMasterButtonTransfer)
        #        pBrexMenu.AddChild(pMasterButtonMarines)
	#	
	#	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_TRACTOR_TARGET_DOCKED, pMission, __name__+ ".TractorTargetDocked")
                
        # Scan Timer:
        App.TopWindow_GetTopWindow().AddPythonFuncHandlerForInstance(SCAN_TIMER, __name__ + ".MarinesScan")
        # Warp
        App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_START_WARP, pMission, __name__ + ".StartWarpHandler")
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_START_WARP_NOTIFY, pMission, __name__ + ".StartWarpHandler")

        if pScienceMenu:
                # When Player is scanning....
                pScienceMenu.AddPythonFuncHandlerForInstance(App.ET_SCAN, __name__ + ".ScanInit")

                # finally create the Pane - we don't create it later like in previous Version, cause that can cause crashes
                # creating it here can crash the game - damm!
                #CreateSciencePane()
                # bad, really bad work around!
                MissionLib.CreateTimer(Lib.LibEngineering.GetEngineeringNextEventType(), __name__ + ".CreateSciencePane", App.g_kUtopiaModule.GetGameTime() + 2, 0, 0)
        
        if g_pScience:
                # Menu
                g_pScience.AddPythonFuncHandlerForInstance(App.ET_CHARACTER_MENU, __name__ + ".HandleScanMenuEvent")
        elif App.g_kUtopiaModule.IsMultiplayer():
                Lib.LibEngineering.CreateMenuButton("Scan Window", "Science",  __name__ + ".ShowScanWindow")



# Finally the Marine class
class Marineclass:
    def __init__(self, pShip):
        debug(__name__ + ", __init__")
        global useFTB
        
        self.pShip = pShip
        self.NumEnemy = 0
        
        if (useFTB == 1): # only if ftb is installed
            pCarrier = ftb.ShipManager.GetShip(self.pShip)
        else:
            pCarrier = None
        if useFTB and hasattr(pCarrier, "GetNumMarines"):
            self.NumMarines = pCarrier.GetNumMarines()
        else:
            self.NumMarines = int(round(self.pShip.GetHull().GetRadius() * 30, 0))

        if hasattr(pCarrier, "GetNumPeople"):
            self.NumPeople = pCarrier.GetNumPeople()
        else:
            self.NumPeople = int(round(pShip.GetHull().GetRadius() * 50, 0))
        self.MaxCrew  = float(self.NumPeople + self.NumMarines)
        if self.pShip.GetRepairSubsystem():
                self.NormRepairPoints = self.pShip.GetRepairSubsystem().GetProperty().GetMaxRepairPoints()        
        
    def GetMarines(self):
        debug(__name__ + ", GetMarines")
        return self.NumMarines

    def SetMarines(self, NumMarines):
        debug(__name__ + ", SetMarines")
        self.NumMarines = NumMarines
        # reset RepairPoints
        if self.pShip.GetRepairSubsystem():
                mySet = self.NormRepairPoints * ((self.NumPeople + self.NumMarines)/ self.MaxCrew)
                self.pShip.GetRepairSubsystem().GetProperty().SetMaxRepairPoints(mySet)
        
    def GetPeople(self):
        debug(__name__ + ", GetPeople")
        return self.NumPeople
    
    def SetPeople(self, NumPeople):
        debug(__name__ + ", SetPeople")
        self.NumPeople = NumPeople
        # reset RepairPoints
        if self.pShip.GetRepairSubsystem():
                mySet = self.NormRepairPoints * (self.NumPeople + self.NumMarines) / self.MaxCrew
                self.pShip.GetRepairSubsystem().GetProperty().SetMaxRepairPoints(mySet)
        if (self.NumPeople == 0): # No one on board?
            #then reset AI:
            import AI.Player.Stay
            self.pShip.SetAI(AI.Player.Stay.CreateAI(self.pShip))

    def GetEnemyMarinesOnShip(self):
        debug(__name__ + ", GetEnemyMarinesOnShip")
        return self.NumEnemy
    
    def SetEnemyMarinesOnShip(self, NumEnemy):
        debug(__name__ + ", SetEnemyMarinesOnShip")
        self.NumEnemy = NumEnemy
