#################################################################################################################
#         FiveSecsGodPhaser
#                          by USS Frontier
#################################################################################################################
# Little simple tech. Any ships with phasers and equipped with this will have a nasty weapon at their disposal.
# With this equipped, any beam weapons of the ship that hit their target for 5 seconds, continuously, will instantly destroy the target.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"FiveSecsGodPhaser": 1
	}
}
"""
#######################################################################
import App
import FoundationTech
from ftb.Tech.ATPFunctions import *
import time
import string

class FiveSecsGodPhaser(FoundationTech.TechDef):
	def __init__(self, name):
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_STARTED_HITTING, self.pEventHandler, "PhaserStartedHitting")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_PHASER_STOPPED_HITTING, self.pEventHandler, "PhaserStoppedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PHASER_STARTED_HITTING, self.pEventHandler, "PhaserStartedHitting")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_PHASER_STOPPED_HITTING, self.pEventHandler, "PhaserStoppedHitting")
		#print "Initialized FiveSecsGodPhaser"

	def Attach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			pInstance.__dict__['FiveSecsGodPhaser'] = {}
			dMasterDict = pInstance.__dict__['FiveSecsGodPhaser']
		else:
			pass
			#print "FiveSecsGodPhaser Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
		pInstance.lTechs.append(self)
		print "FSGP: attached to ship:", pShip.GetName()
	def Detach(self, pInstance):
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			dMasterDict = pInstance.__dict__['FiveSecsGodPhaser']
		else:
			#print "FiveSecsGodPhaser Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
			pass
		pInstance.lTechs.remove(self)
		print "FSGP: detached from ship:", pShip.GetName()


	def PhaserStartedHitting(self, pEvent):
		pPhaser = App.Weapon_Cast(pEvent.GetSource())
		#print "FSGP: phasers started hitting"
		if pPhaser == None:
			#print "FSGP: cancelling... no phaser weapon"
			return
		pShip = pPhaser.GetParentShip()
		try:
			pInstance = FoundationTech.dShips[pShip.GetName()]
			if pInstance == None:
				#print "FSGP: cancelling, no FTech Ship Instance obj"
				return
		except:
			#print "FSGP: cancelling, error in try found..."
			return
		if not pInstance.__dict__.has_key("FiveSecsGodPhaser"):
			#print "FSGP: cancelling, ship does not have FSGP equipped..."
			return
		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		if pTarget == None:
			#print "FSGP: cancelling, no target..."
			return
		sTargetName = pTarget.GetName()
		#print "FSGP: Mark 1, Target is:", sTargetName
		if not pInstance.__dict__['FiveSecsGodPhaser'].has_key(sTargetName):
			pInstance.__dict__['FiveSecsGodPhaser'][sTargetName] = {"HittingNames": [], "Target": pTarget}

			pGame = App.Game_GetCurrentGame()
			pEpisode = pGame.GetCurrentEpisode()
			pMission = pEpisode.GetCurrentMission()
			eType = App.Mission_GetNextEventType()
			App.g_kEventManager.AddBroadcastPythonMethodHandler(eType, self.pEventHandler, "HandleInstaKill")
			pEvent = App.TGStringEvent_Create()
			pEvent.SetEventType(eType)
			pEvent.SetDestination(pMission)
			pEvent.SetString(pShip.GetName()+">|<"+sTargetName)
			pTimer = App.TGTimer_Create()
			pTimer.SetTimerStart( App.g_kUtopiaModule.GetGameTime()+5.0 )
			pTimer.SetDelay(0)
			pTimer.SetDuration(0)
			pTimer.SetEvent(pEvent)
			App.g_kTimerManager.AddTimer(pTimer)

			pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['Timer'] = pTimer
			#print "FSGP: first time hitting target, setting up data."

		#however we still need to store their names so that the events are properly handled
		if not pPhaser.GetName() in pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['HittingNames']:
			pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['HittingNames'].append( pPhaser.GetName() )
			#print "FSGP: adding phaser", pPhaser.GetName(), "to Target hitting list."
	def PhaserStoppedHitting(self, pEvent):
		pPhaser = App.Weapon_Cast(pEvent.GetSource())
		if pPhaser == None:
			#print "FSGP (Stop): cancelling, no phaser..."
			return
		pShip = pPhaser.GetParentShip()
		try:
			pInstance = FoundationTech.dShips[pShip.GetName()]
			if pInstance == None:
				#print "FSGP (Stop): cancelling, no FTech Ship Instance obj"
				return
		except:
			#print "FSGP (Stop): cancelling, error in try found."
			return
		if not pInstance.__dict__.has_key("FiveSecsGodPhaser"):
			#print "FSGP (Stop): ship does not have FSGP equipped."
			return	
		pTarget = App.ShipClass_Cast(pEvent.GetDestination())
		if pTarget == None:
			#print "FSGP (Stop): cancelling, no target"
			return
		sTargetName = pTarget.GetName()
		#print "FSGP (Stop): Mark 1, target is:", sTargetName
		if not pInstance.__dict__['FiveSecsGodPhaser'].has_key(sTargetName):
			#most likely scenario, and hopefully the only one, for this if:  ship was just destroyed by this phaser fire, thus her entry deleted
			#from our data dict, but phaser was still hitting her and stopped after the destruction. So we simply return here...
			return
		if pPhaser.GetName() in pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['HittingNames']:
			pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['HittingNames'].remove( pPhaser.GetName() )
			#print "FSGP (Stop): removing phaser", pPhaser.GetName(), "from target hitting list."

		if len(pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['HittingNames']) <= 0:
			#5-secs hitting sequence aborted... cancel it.
			App.g_kTimerManager.DeleteTimer(pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['Timer'].GetObjID())
			pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['Timer'] = None
			del pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]
			#print "FSGP (Stop): 5-sec hitting sequence aborted..."

	def HandleInstaKill(self, pEvent):
		sMasterStr = pEvent.GetCString()
		lStrs = string.split(sMasterStr, ">|<")
		sShipName = lStrs[0]
		sTargetName = lStrs[1]
		#print "FSGP (HIK): Handle Instant Kill called..."
		#print "FSGP (HIK): Ship:", sShipName, " ||Target:", sTargetName
		try:
			pInstance = FoundationTech.dShips[sShipName]
			if pInstance == None:
				#print "FSGP (HIK): cancelling, no FTech Ship Instance obj"
				return
		except:
			#print "FSGP (HIK): cancelling, error at try found..."
			return
		if not pInstance.__dict__.has_key("FiveSecsGodPhaser"):
			#print "FSGP (HIK): cancelling, ship is not equipped with FSGP..."
			return
		if pInstance.__dict__['FiveSecsGodPhaser'].has_key(sTargetName):
			#okydokey, we did it. Blow up the ship. then delete our data about it.
			pTarget = pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['Target']
			pTarget.DestroySystem(pTarget.GetHull())
			App.g_kTimerManager.DeleteTimer(pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['Timer'].GetObjID())
			pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]['Timer'] = None
			del pInstance.__dict__['FiveSecsGodPhaser'][sTargetName]
			#print "FSGP (HIK): 5-sec hitting sequence completed, destroying target."

	#Note for me: if needed, check other FTech scripts/plugins to get some insight/examples on using Yield event for beam weapons.
		
oFiveSecsGodPhaser = FiveSecsGodPhaser("FiveSecsGodPhaser")