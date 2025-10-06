#################################################################################################################
#         AdvancedHullTech
#                          by USS Frontier
#################################################################################################################
# Purpose of this Foundation Tech plugin is to give ships that use it a different kind of advanced hull.
# Making some systems (specified in the ship plugin) "merged" with the ship's hull. Thus, they are untargetable 
# and immune to normal weapons fire, however they might still get disabled, depending on the hull's condition percentage, 
# and the system's disabled percentage value.
#############################################
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file
# but modify the values accordingly to what you want, and for actual values since the following is just a general example
"""
Foundation.ShipDef.Sovereign.dTechs = {
	"AdvancedHull": ["subsystem name", "another subsystem name" ]
	}
}
"""
#######################################################################

import App
import MissionLib
import Foundation
import FoundationTech
import string

try:
	from bcdebug import debug
except:
	def debug(s):
		pass

dHullWatchers = {}
class AdvancedHullTech(FoundationTech.TechDef):
	def Attach(self, pInstance):
		global dHullWatchers
		debug(__name__ + ", Attach")
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			lSysNames = pInstance.__dict__['AdvancedHull']
			dATH = {}
			for sName in lSysNames:
				pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
				if pSubsystem != None:
					dATH[sName] = pSubsystem.GetDisabledPercentage()
					#pSubsystem.SetInvincible(1)
					pProp = pSubsystem.GetProperty()
					pProp.SetTargetable(0)
					pProp.SetDisabledPercentage(0.0)
					#print "AdvancedHullTech (at Attach): found subsystem", sName, "in ship", pShip.GetName()
				else:
					print "AdvancedHullTech Error (at Attach): couldn't find subsystem", sName, "in ship", pShip.GetName()
			hullwat = HullWatcher(pShip, dATH)
			dHullWatchers[pShip.GetName()] = hullwat
		else:
			print "AdvancedHullTech Error (at Attach): couldn't acquire ship of id", pInstance.pShipID
		pInstance.lTechs.append(self)

	def Detach(self, pInstance):
		global dHullWatchers
		debug(__name__ + ", Detach")
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pInstance.pShipID))
		if pShip != None:
			lSysNames = pInstance.__dict__['AdvancedHull']
			for sName in lSysNames:
				pSubsystem = MissionLib.GetSubsystemByName(pShip, sName)
				if pSubsystem != None:
					#pSubsystem.SetInvincible(0)
					pProp = pSubsystem.GetProperty()
					pProp.SetTargetable(1)
				else:
					print "AdvancedHullTech Error (at Detach): couldn't find subsystem", sName, "in ship", pShip.GetName()			
			if dHullWatchers.has_key(pShip.GetName()):
				dHullWatchers[pShip.GetName()].RemoveWatchers()
		else:
			print "AdvancedHullTech Error (at Detach): couldn't acquire ship of id", pInstance.pShipID
		pInstance.lTechs.remove(self)


oAdvancedHull = AdvancedHullTech("AdvancedHull")


class HullWatcher:
	def __init__(self, pShip, dAHT):
		self.Ship = pShip
		self.AHT = dAHT  

		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		ET_HULL_WATCHER = App.UtopiaModule_GetNextEventType()
		###
		pHull = pShip.GetHull()

		pEvent = App.TGFloatEvent_Create()
		pEvent.SetEventType( ET_HULL_WATCHER )
		pEvent.SetDestination( self.pEventHandler )
		pEvent.SetSource( pHull )

		pWatcher = pHull.GetConditionWatcher()
		self.lRangeCheckIDs = []
		for i in range(100):
			i = i/100.0
			iRangeID = pWatcher.AddRangeCheck( i, App.FloatRangeWatcher.FRW_BOTH, pEvent )
			self.lRangeCheckIDs.append(iRangeID)

		###
		self.lastFraction = -1.0
		self.pEventHandler.AddPythonMethodHandlerForInstance( ET_HULL_WATCHER, "SystemEvent" )

	def RemoveWatchers(self):
		if (not hasattr(self, "Ship")) or self.Ship == None:
			return
		if hasattr(self, "RangeCheck") and self.RangeCheck is not None:
			pWatcher = pShip.GetHull().GetConditionWatcher()
			for iRangeCheckID in self.lRangeCheckIDs:
				pWatcher.RemoveRangeCheck( iRangeCheckID )
			self.lRangeCheckIDs = []

	def SystemEvent(self, pFloatEvent):
		# Check if our system is now above or below the fraction...
		fFraction = pFloatEvent.GetFloat()
		if fFraction != self.lastFraction:
			#print "HullWatcher event for", self.Ship.GetName(), ": fraction =", fFraction
			lNames = self.AHT.keys()
			for sName in lNames:
				pSubsystem = MissionLib.GetSubsystemByName(self.Ship, sName)
				#print "HW: checking subsystem:", sName, " Obj:", pSubsystem
				if pSubsystem != None:
					if fFraction >= self.AHT[sName]:
						#system is OK
						pSubsystem.GetProperty().SetDisabledPercentage(0.0)
						#print "HW: is OK"
					else:
						#system is disabled
						pSubsystem.GetProperty().SetDisabledPercentage(100)
						#print "HW: disabled"
			self.lastFraction = fFraction
		self.pEventHandler.CallNextHandler(pFloatEvent)
###
