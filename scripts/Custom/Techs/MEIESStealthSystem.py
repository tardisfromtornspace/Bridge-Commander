# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# MEIESStealthSystem.py
# 18th December 2024, by Alex SL Gato (CharaToLoki)
#         Partially based on PhaseCloak by MLeo Daalder, which was based on Apollo's Phase Cloak.
#
# Requirements:
#	Foundation Technologies (Version 20050510 or later)
#
# Installation:
#	Place this file in scripts\Custom\Techs
#
# How does this tech work?
# Basically this tech is a roundabout way to make the IES stealth system from Mass Effect. What it does is to basically act when a ship with this tech is cloaking or decloaking, so they are immediately decloaked but their team is temporarily swapped to tractor when cloaking so the regular AI cannot target them, but specialized AI or a player performing "visual scans" totally can. When one of those ships is fired upon, it will switch back to the team it was from last time it cloaked. And thanks to specific scripts used when a ship is from the regular neutral team, that ship managing to hurt its target will also make it again switch team properly, as weapons fire would pretty much reveal a ship using this stealth.
# While a ship is using its stealth, it also performs radio silence, so they will not be commandable, albeit they will still follow orders sent previously and their AIs will still behave as if they were still from the same team, unless you shoot them down, that is.
# Fields:
# "ME IES Stealth System": only field required for this tech. Its value assigns a time penalty in seconds which indicates the amount of seconds that the cloak is disabled when it is active and the ship is hit by a weapon
"""
#Sample Setup: replace "USSProtostar" for the appropiate abbrev
Foundation.ShipDef.USSProtostar.dTechs = {
	"ME IES Stealth System": 0,
}
"""
#################################################################################################################
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.3",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#################################################################################################################

import App
from bcdebug import debug
import Foundation
import FoundationTech
import MissionLib

class MEIESStealth(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		if not pEvent.IsHullHit():
			return
		if pInstance.__dict__['ME IES Stealth System'] <= 0:
			return
		
		pCloak = pShip.GetCloakingSubsystem()
		if not pCloak:
			return

		#if not (pCloak.IsCloaked() or pCloak.IsTryingToCloak() or pCloak.IsCloaking() or pCloak.IsDecloaking()):
		#	#print pShip.GetName(), "is not cloaked and is not trying to cloak and is not cloaking", pCloak
		#	return

		# Now, decloak for a sec or 2...
		#	Depends on the setting in the Phase Cloak tuple...
		pInstance.Disable(pShip, pCloak, pInstance.__dict__["ME IES Stealth System"])
		StateMachine(pShip, pEvent, 1)

	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		if pInstance.__dict__["ME IES Stealth System"] > 0:
			pInstance.lTorpDefense.append(self)
			pInstance.lPulseDefense.append(self)
			pInstance.lBeamDefense.append(self)

		pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)
		if pShip:
			# I can't decide between ET_CLOAK_BEGINNING and ET_CLOAK_COMPLETED
			#	Same for the decloaking part...
			pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
			pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
			pShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
			pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
			pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
			pShip.AddPythonFuncHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")

	def Detach(self, pInstance):
		debug(__name__ + ", Detach")	
		pInstance.lTechs.remove(self)
		if pInstance.__dict__["ME IES Stealth System"] > 0:
			pInstance.lTorpDefense.remove(self)
			pInstance.lPulseDefense.remove(self)
			pInstance.lBeamDefense.remove(self)
		
		pShip = App.ShipClass_GetObjectByID(None, pInstance.pShipID)
		if pShip:
			pShip.RemoveHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
			pShip.RemoveHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")
			pShip.RemoveHandlerForInstance(App.ET_WEAPON_FIRED, __name__ + ".WeaponFired")
			if hasattr(pInstance, "MEIESStealthSystemGroup"):
				del pInstance.MEIESStealthSystemGroup
			if hasattr(pInstance, "MEIESStealthSystemCount"):
				del pInstance.MEIESStealthSystemCount

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTractorDefense(self, pShip, pInstance, oYield, pEvent):
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

oMEIESStealth = MEIESStealth("ME IES Stealth System")

def findShipInstance(pShip):
        debug(__name__ + ", findShipInstance")
        pInstance = None
        try:
            if not pShip:
                return pInstance
            if FoundationTech.dShips.has_key(pShip.GetName()):
                pInstance = FoundationTech.dShips[pShip.GetName()]
            #if pInstance == None:
            #        print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
        except:
            pass

        return pInstance

def grabTeamsQB(pShipID, encloak=0):
	debug(__name__ + ", grabTeamsQB")
	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return None

	pInstance = findShipInstance(pShip)
	if not pInstance:
		return None

	pMission        = MissionLib.GetMission()

	pFriendlies     = None
	pEnemies        = None
	pNeutrals       = None
	pTractors       = None
	myGroup = None
	if pMission:
		pcName = pShip.GetName()
		pFriendlies     = pMission.GetFriendlyGroup() 
		pEnemies        = pMission.GetEnemyGroup() 
		pNeutrals       = pMission.GetNeutralGroup()
		pTractors       = pMission.GetTractorGroup()	
		pNeutrals2      = App.ObjectGroup_FromModule("Custom.QuickBattleGame.QuickBattle", "pNeutrals2")
	
		if encloak == 1:
			careful = 0
			chose1 = "F"
			if pFriendlies and pFriendlies.IsNameInGroup(pcName):
				myGroup = pFriendlies
				chose1 = "F"
				pFriendlies.RemoveName(pcName)
			if pEnemies and pEnemies.IsNameInGroup(pcName):
				myGroup = pEnemies
				chose1 = "E"
				pEnemies.RemoveName(pcName)
			if pNeutrals and pNeutrals.IsNameInGroup(pcName):
				myGroup = pNeutrals
				chose1 = "N"
				pNeutrals.RemoveName(pcName)
			if pNeutrals2 and pNeutrals2.IsNameInGroup(pcName):
				myGroup = pNeutrals2
				pNeutrals2.RemoveName(pcName)
			if pTractors and pTractors.IsNameInGroup(pcName):
				myGroup = pTractors
				careful = 1
				print "careful"
				pTractors.RemoveName(pcName)

			if careful == 0 or not hasattr(pInstance, "MEIESStealthSystemGroup"):
				#pInstance.MEIESStealthSystemGroup = myGroup
				if myGroup:
					pInstance.MEIESStealthSystemGroup = myGroup
					if pTractors and not pTractors.IsNameInGroup(pcName):
						pTractors.AddName(pcName)
					#if chose1 == "F":
					#	if pTractors and not pTractors.IsNameInGroup(pcName):
					#		pTractors.AddName(pcName)
					#else:
					#	if pNeutrals and not pNeutrals.IsNameInGroup(pcName):
					#		pNeutrals.AddName(pcName)

			elif careful == 1 and hasattr(pInstance, "MEIESStealthSystemGroup"):
				if hasattr(pInstance.MEIESStealthSystemGroup, "IsNameInGroup") and not pInstance.MEIESStealthSystemGroup.IsNameInGroup(pcName):
					pInstance.MEIESStealthSystemGroup.AddName(pcName)
					myGroup = "ERROR"

		else:
			if hasattr(pInstance, "MEIESStealthSystemGroup"):
				if pTractors and pTractors.IsNameInGroup(pcName):
					pTractors.RemoveName(pcName)
				#if pNeutrals and pNeutrals.IsNameInGroup(pcName):
				#	pNeutrals.RemoveName(pcName)
				if not pInstance.MEIESStealthSystemGroup.IsNameInGroup(pcName):
					pInstance.MEIESStealthSystemGroup.AddName(pcName)

	return myGroup

def WeaponFired(pObject, pEvent):
	myState = StateMachine(pObject, pEvent, 1)
	return 0

def CloakHandler(pObject, pEvent):
	myState, pShip = StateMachine(pObject, pEvent, 0)

	if myState != None and pShip != None and (myState == 0 or myState == 2):
		pCloak = pShip.GetCloakingSubsystem()
		if pCloak:
			shipIsCloaking = pCloak.IsCloaking() or pCloak.IsCloaked()
			if shipIsCloaking:
				pCloak.StopCloaking()

	#pObject.CallNextHandler(pEvent)
	return None

def DecloakHandler(pObject, pEvent, fromDamage=0):
	StateMachine(pObject, pEvent, fromDamage)
	#pObject.CallNextHandler(pEvent)
	return None


def StateMachine(pObject, pEvent, fromDamage=0):
	currentState = None
	if not pObject or not hasattr(pObject, "GetObjID"):
		return currentState, None

	pShipID = pObject.GetObjID()
	if not pShipID:
		return currentState, None

	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return currentState, None

	pInstance = findShipInstance(pShip)
	if not pInstance:
		return currentState, pShip

	myTeam = None
	if fromDamage == 0:
		if not hasattr(pInstance, "MEIESStealthSystemCount"):
			pInstance.MEIESStealthSystemCount = 0

		currentState = pInstance.MEIESStealthSystemCount
		if pInstance.MEIESStealthSystemCount == 1:
			myTeam = grabTeamsQB(pShipID, 1)

		elif pInstance.MEIESStealthSystemCount == 3:
			myTeam = grabTeamsQB(pShipID, 0)

		# Ok so, first time, we cloak, we are really cloaking, the second is product of us decloaking so we cannot do that
		pInstance.MEIESStealthSystemCount = (pInstance.MEIESStealthSystemCount + 1) % 4 # mod 4, so only 0, 1, 2 and 3

	else:
		currentState = 3
		pInstance.MEIESStealthSystemCount = 0
		myTeam = grabTeamsQB(pShipID, 0)

	if myTeam == "ERROR":
		currentState = 0
		pInstance.MEIESStealthSystemCount = 0
		myTeam = grabTeamsQB(pShipID, 0)

	pShip.UpdateNodeOnly()

	return currentState, pShip

