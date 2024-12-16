# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# MEIESStealthSystem.py
# 16th December 2024, by Alex SL Gato (CharaToLoki)
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
	    "Version": "0.1",
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
		if hasattr(pInstance, "MEIESStealthSystemCount") and pInstance.MEIESStealthSystemCount == 1:
			DecloakHandler(pShip, pEvent)

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
			pShip.AddPythonFuncHandlerForInstance(App.ET_CLOAK_BEGINNING, __name__ + ".CloakHandler")
			pShip.AddPythonFuncHandlerForInstance(App.ET_DECLOAK_BEGINNING, __name__ + ".DecloakHandler")

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
			if pFriendlies and pFriendlies.IsNameInGroup(pcName):
				myGroup = pFriendlies
			if pFriendlies:
				pFriendlies.RemoveName(pcName)
			if pEnemies and pEnemies.IsNameInGroup(pcName):
				myGroup = pEnemies
			if pEnemies:
				pEnemies.RemoveName(pcName)
			if pNeutrals and pNeutrals.IsNameInGroup(pcName):
				myGroup = pNeutrals
			if pNeutrals:
				pNeutrals.RemoveName(pcName)
			if pNeutrals2 and pNeutrals2.IsNameInGroup(pcName):
				myGroup = pNeutrals2
			if pNeutrals2:
				pNeutrals2.RemoveName(pcName)
			if pTractors and pTractors.IsNameInGroup(pcName):
				myGroup = pTractors
			if pTractors:
				pTractors.RemoveName(pcName)

			pInstance.MEIESStealthSystemGroup = myGroup
			if myGroup:
				pInstance.MEIESStealthSystemGroup = myGroup
				if pTractors and not pTractors.IsNameInGroup(pcName):
					pTractors.AddName(pcName)
				#if pNeutrals and not pNeutrals.IsNameInGroup(pcName):
				#	pNeutrals.AddName(pcName)

		else:
			if hasattr(pInstance, "MEIESStealthSystemGroup"):
				if pTractors and pTractors.IsNameInGroup(pcName):
					pTractors.RemoveName(pcName)
				#if pNeutrals and pNeutrals.IsNameInGroup(pcName):
				#	pNeutrals.RemoveName(pcName)
				if not pInstance.MEIESStealthSystemGroup.IsNameInGroup(pcName):
					pInstance.MEIESStealthSystemGroup.AddName(pcName)

	return myGroup

def CloakHandler(pObject, pEvent):
	if not pObject or not hasattr(pObject, "GetObjID"):
		return None

	pShipID = pObject.GetObjID()
	if not pShipID:
		return None

	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return None

	pInstance = findShipInstance(pShip)
	if not pInstance:
		return None

	if hasattr(pInstance, "MEIESStealthSystemCount"): # Ok so, first time, we cloak, we are really cloaking, the second is poroduct of us decloaking so we cannot do that TO-DO CLEANUP
		pInstance.MEIESStealthSystemCount = (pInstance.MEIESStealthSystemCount + 1) % 2 # mod 2, so only 0 or 1
	else:
		pInstance.MEIESStealthSystemCount = 1

	if pInstance.MEIESStealthSystemCount == 1:
		myTeam = grabTeamsQB(pShipID, pInstance.MEIESStealthSystemCount)
	pCloak = pShip.GetCloakingSubsystem()
	if pCloak:
		pCloak.StopCloaking() #InstantDecloak()

	pShip.UpdateNodeOnly()

	return None
	#pObject.CallNextHandler(pEvent)

def DecloakHandler(pObject, pEvent, fromDamage=0):
	if not pObject or not hasattr(pObject, "GetObjID"):
		return None

	pShipID = pObject.GetObjID()
	if not pShipID:
		return None

	pShip = App.ShipClass_GetObjectByID(None, pShipID)
	if not pShip:
		return None

	pInstance = findShipInstance(pShip)
	if not pInstance:
		pObject.CallNextHandler(pEvent)
		return None
	if fromDamage == 0:
		if hasattr(pInstance, "MEIESStealthSystemCount"): # Ok so, first time, we cloak, we are really cloaking, the second is poroduct of us decloaking so we cannot do that TO-DO CLEANUP
			pInstance.MEIESStealthSystemCount = (pInstance.MEIESStealthSystemCount + 1) % 2 # mod 2, so only 0 or 1
		else:
			pInstance.MEIESStealthSystemCount = 1
	else:
		if not hasattr(pInstance, "MEIESStealthSystemCount"):
			pInstance.MEIESStealthSystemCount = 0

	if pInstance.MEIESStealthSystemCount == 1:
		myTeam = grabTeamsQB(pShipID, 1)

	pShip.UpdateNodeOnly()
	
	#pObject.CallNextHandler(pEvent)
