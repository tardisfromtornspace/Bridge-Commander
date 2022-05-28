#!/usr/bin/python

# Dock script (Return Shuttles Addon) by Defiant <mail@defiant.homedns.org>
MODINFO = {     "Author": "\"Defiant\" mail@defiant.homedns.org",
                "License": "GPL",
                "needBridge": 0
            }

# Imports
import App
import MissionLib
import Lib.LibEngineering
from Libs.LibQBautostart import *

# Vars
g_pGeblePodTargets = None
DockVersion = 2 # may be 1 or 2

def ShuttlesDock(pObject, pEvent):
        global DockVersion
	#print("Docking...")

        if (DockVersion == 2):
                import ReturnShuttles
                ReturnShuttles.ReturnWithoutTractor(pObject, pEvent, NotHost = 1)
                return

	pGame = App.Game_GetCurrentGame()
	pEpisode = pGame.GetCurrentEpisode()
	pMission = pEpisode.GetCurrentMission()
	pFriendlies = pMission.GetFriendlyGroup()
	pPlayer = MissionLib.GetPlayer()
        pTarget = pPlayer.GetTarget()

	if not pTarget:
		print("No Target - No Docking")
		return
        if App.ShipClass_Cast(pTarget).GetNetPlayerID() > 0:
                print("Not Docking to a Player")
                return
	
	if (pFriendlies.IsNameInGroup(pPlayer.GetTarget().GetName()) != 1):
		print("Target is Enemy")
		return
	else:
		print("Target is Friendly...Going on")
	
	
	pTarget = MissionLib.GetShip(pPlayer.GetTarget().GetName())
	g_pGeblePodTargets = App.ObjectGroup()
	g_pGeblePodTargets.AddName(pPlayer.GetName())
	
	Getg_pGeblePodTargets()
	
	if not pTarget:
		print("Error in Target")
		return
	
	AIModule = __import__("AI.Compound.TractorTarget")
	pTarget.SetAI(AIModule.CreateAI(pTarget, App.ObjectGroup_FromModule("Custom.QBautostart.Dock", "g_pGeblePodTargets")))


def Getg_pGeblePodTargets():
	global g_pGeblePodTargets
	pPlayer = MissionLib.GetPlayer()
	
	g_pGeblePodTargets = None
	g_pGeblePodTargets = App.ObjectGroup()
	g_pGeblePodTargets.AddName(pPlayer.GetName())


def init():
	if not IsMultiplayerHostAlone():
		return
        if not Lib.LibEngineering.CheckActiveMutator("New Technology System"):
                return
                
        Lib.LibEngineering.CreateMenuButton("Land on Target", "Helm", __name__ + ".ShuttlesDock")
