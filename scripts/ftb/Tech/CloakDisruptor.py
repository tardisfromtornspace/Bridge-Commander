from bcdebug import debug
import App

import FoundationTech
import MissionLib
import Foundation
import ATPFunctions

from DisablerYields import *
from math import *

#########################################################################################################################
##	YieldType:													#
##			SensorDisable:		Sensors disabled for SensorDisabledTime seconds			#
##			ShieldDisruptor		Target shields are disrupted for ShieldDisabledTime seconds		#
##			EngineJammer:		Target Engines are disabled for EngineDisabledTime seconds		#
##			Ion Cannon:		Random Subtarget disabled for IonCannonDisabledTime seconds		#
##						    with a 1 on IonCannonMiss to have no effect				#
##			CloakBurn:		Target CloakingSys is disabled for CloakDisabledTime seconds	#
#########################################################################################################################

g_count = 1


# One difference:  if the target is missing, call the contained event

# I had to overwrite the __init__ to make it work, reason: self didn't had pTorpID... -MLeoDaalder
class CloakDisruptorEvent(FoundationTech.FTBEvent):
	def __init__(self, source, when, pTorpID):
		debug(__name__ + ", __init__")
		self.pTorpID = pTorpID
		FoundationTech.FTBEvent.__init__(self, source, when)

	def __call__(self, now):

		debug(__name__ + ", __call__")
		print 'Disrupting Cloaks'

		pTorp = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(self.pTorpID))
		if not pTorp:
			return

		kTorp = pTorp.GetWorldLocation()

		lShips = ATPFunctions.MakeEnemyShipList(pTorp.GetContainingSet()) + ATPFunctions.MakeFriendShipList(pTorp.GetContainingSet())
		for i in lShips:
			pTempShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(i))
			if not pTempShip.IsCloaked():
				continue
			print pTempShip.GetName(), 'is being decloaked'
			kTempShip = pTempShip.GetWorldLocation()
			kTempShip.Subtract(kTorp)
			
			if kTempShip.Length() < 1000.0:
				pInstance = FoundationTech.dShips[pTempShip.GetName()]
				oCloakDisable.OnYield(pTempShip, pInstance, self, pTorp, 10)

		global g_count
		g_count = g_count + 1
		return g_count % 4


class CloakDisruptor(FoundationTech.TechDef):
	def __init__(self, name, dict):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.__dict__.update(dict)

	def OnFire(self, pEvent, pTorp):
		debug(__name__ + ", OnFire")
		pShipID = pTorp.GetParentID()
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		pInstance = FoundationTech.dShips[pShip.GetName()]
		
		print 'CloakDisruptor.OnFire'
		pTorpID = pTorp.GetObjID()
		e = CloakDisruptorEvent(pInstance, 1, pTorpID)
		FoundationTech.oEventQueue.Queue(e)

print 'Cloak Disruptor loaded'
