from bcdebug import debug
import App

import FoundationTech
import MissionLib
import Foundation

from ATPFunctions import *
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


# One difference:  if the target is missing, call the contained event
class TorpDistanceEvent(FoundationTech.DistanceEvent):
	def __call__(self, now):

		debug(__name__ + ", __call__")
		print self.__dict__
		pFirst = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(self.pFirstID))
		if not pFirst:
			return

		pSecond = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(self.pSecondID))
		if not pSecond:
			self.oEvent(now)

		kDist = pFirst.GetWorldLocation()
		kDist.Subtract(pSecond.GetWorldLocation())
		distance = kDist.Length()

		if distance < self.distance:
			self.oEvent(now)
		else:
			return self.interval


class SingleMIRVEvent(FoundationTech.FTBEvent):
	def __init__(self, pTorpID, oTech, when):
		debug(__name__ + ", __init__")
		self._source = None
		self._when = when
		self.pTorpID = pTorpID
		self.oTech = oTech

	# This function is based upon Apollo's cycleSpreadType1
	def __call__(self, now):

		debug(__name__ + ", __call__")
		print self.__dict__
		pTorp = App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(self.pTorpID))
		if not pTorp:
			return

		pTargetID = pTorp.GetTargetID()
		pTarget = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(pTargetID))

		if not pTarget:
			return

		pShipID = pTorp.GetParentID()

		oTech = self.oTech

		# I have no idea what Apollo was up to here.
		#
		# if App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTorp.GetTargetID())) == None:
		# 	TargetID = pShip.GetObjID()
		# else:
		# 	TargetID = pTorp.GetTargetID()

		kVectTorp = pTorp.GetWorldLocation()
		kVelocity = CopyVector(pTorp.GetVelocityTG())
		fSpeed = kVelocity.Length()
		kVelocity.Unitize()

		kTest = App.TGPoint3()
		kTest.SetXYZ(1,0,0)
		if kVelocity.GetY() == 0.0:
			kTest.SetY(1.0)
		kX = kVelocity.Cross(kTest)
		kX.Unitize()
		kY = kX.Cross(kVelocity)

		theta = 0.0
		delta = 2.0 * pi / oTech.spreadNumber

		for k in range(oTech.spreadNumber):
			ktX = CopyVector(kX)
			ktX.Scale(cos(theta) / oTech.spreadDensity)

			ktY = CopyVector(kY)
			ktY.Scale(sin(theta) / oTech.spreadDensity)

			kZ = CopyVector(kVelocity)
			kZ.Add(ktX)
			kZ.Add(ktY)

			pTempTorp = FireTorpFromPointWithVector(kVectTorp, kZ, oTech.warheadModule, pTargetID, pShipID, fSpeed)
			pTempTorp.SetLifetime(15.0)
			theta = theta + delta

		if not oTech.shellLive:
			pTorp.SetLifetime(0.0)


class MultipleMIRVEvent(FoundationTech.FTBEvent):
	def __init__(self, pTorpID, oTech, when):
		debug(__name__ + ", __init__")
		self._source = None
		self._when = when
		self.pTorpID = pTorpID
		self.oTech = oTech

	# This function is based upon Apollo's cycleSpreadType2
	def __call__(self, now):
		debug(__name__ + ", __call__")
		pTorp = App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(self.pTorpID))
		if not pTorp:
			return

		pTargetID = pTorp.GetTargetID()
		pTarget = App.BaseObjectClass_Cast(App.TGObject_GetTGObjectPtr(pTargetID))
		if not pTarget:
			return

		pShipID = pTorp.GetParentID()
		pShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pShipID))
		if not pShip:
			return

		# TODO: We need better
		if IsEnemy(pShip):
			lShips = MakeFriendShipList(pTorp.GetContainingSet())
		elif IsFriend(pShip):
			lShips = MakeEnemyShipList(pTorp.GetContainingSet())
		else:
			lShips = MakeEnemyShipList(pTorp.GetContainingSet()) + MakeFriendShipList(pTorp.GetContainingSet())

		oTech = self.oTech


		kVect = pTorp.GetWorldLocation()
		kVelocity = CopyVector(pTorp.GetVelocityTG())
		fSpeed = kVelocity.Length()
		kVelocity.Unitize()
		lShips = DistanceSort(lShips, kVect)

		kTest = App.TGPoint3()
		kTest.SetXYZ(1,0,0)
		if kVelocity.GetY() == 0.0:
			kTest.SetY(1.0)
		kX = kVelocity.Cross(kTest)
		kX.Unitize()
		kY = kX.Cross(kVelocity)

		theta = 0.0
		delta = 2.0 * pi / oTech.spreadNumber	# Just enough to spread them out a bit.

		x = 0
		l = len(lShips)

		for k in range(oTech.spreadNumber):
			pTempShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(lShips[x]))
			kTempShip = pTempShip.GetWorldLocation()
			kTempShip.Subtract(kVect)

			if kTempShip.Length() > 500.0:
				if x == 0:
					break
				x = 0

			ktX = CopyVector(kX)
			ktX.Scale(cos(theta) / oTech.spreadDensity)

			ktY = CopyVector(kY)
			ktY.Scale(sin(theta) / oTech.spreadDensity)

			kZ = CopyVector(kVelocity)
			kZ.Add(ktX)
			kZ.Add(ktY)

			pTempTorp = FireTorpFromPointWithVector(kVect, kZ, oTech.warheadModule, lShips[x], pShipID, fSpeed)
			pTempTorp.SetLifetime(15.0)

			theta = theta + delta
			x = x + 1
			if x >= l:
				x = 0

		if not oTech.shellLive:
			pTorp.SetLifetime(0.0)


class MIRVSingleTargetTorpedo(FoundationTech.TechDef):
	def __init__(self, name, dict):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.__dict__.update(dict)

	def OnFire(self, pEvent, pTorp):
		debug(__name__ + ", OnFire")
		print 'MIRVSingleTargetTorpedo.OnFire'
		pTorpID = pTorp.GetObjID()
		FoundationTech.oEventQueue.Queue(
			TorpDistanceEvent(
				pTorpID,
				pTorp.GetTargetID(),
				SingleMIRVEvent(pTorpID, self, 0),
				100.0,
				1)
		)

	# def Activate(self):
	# 	FoundationTech.oTorpedoFired.Start()
	# def Deactivate(self):
	# 	FoundationTech.oTorpedoFired.Stop()


class MIRVMultiTargetTorpedo(FoundationTech.TechDef):
	def __init__(self, name, dict):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.__dict__.update(dict)

	def OnFire(self, pEvent, pTorp):
		debug(__name__ + ", OnFire")
		pTorpID = pTorp.GetObjID()
		print 'MIRVMultiTargetTorpedo.OnFire'
		print self.__dict__, pTorpID
		FoundationTech.oEventQueue.Queue(
			TorpDistanceEvent(
				pTorpID,
				pTorp.GetTargetID(),
				MultipleMIRVEvent(pTorpID, self, 1),
				250.0,
				1)
		)



print 'Timed Torpedoes loaded'
