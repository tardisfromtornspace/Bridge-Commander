# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 6th February 2026
# VERSION 0.1
# By Alex SL Gato
# FoundationTech.py by Dasher and the Foundation Technologies team -> ShipInstance.DefendVS* fix
#
# Changes: 
# - As of FoundationTech 20050703:
# -- ShipInstance.DefendVSBeam does not look for phasers, but for tractors. This has been corrected on this patch.
# -- These defences are not resistant to a tech breaking and making others fail. This has been patched as well.
# -- Tractor defenses were only counting the first time it could hit, and never called again - now this fixes the call event so it can keep firing as it should, and then stops when the tractor disengages.


from bcdebug import debug
import App
import FoundationTech
import Foundation
import traceback

necessaryToUpdate = 0
try:

	if hasattr(Foundation,"version"):
		if int(Foundation.version[0:8]) < 20250305: # we are gonna assume the 2025 version and previous versions lack this
			necessaryToUpdate = 1
	else:
		necessaryToUpdate = 1 # the oldest versions have a signatre, except maybe some prototypes	

except:
    print "Unable to find FoundationTech.py install"
    pass

if necessaryToUpdate:
	original1 = FoundationTech.ShipInstance.DefendVSBeam
	original2 = FoundationTech.ShipInstance.DefendVSTractor
	original3 = FoundationTech.ShipInstance.DefendVSPulse
	original4 = FoundationTech.ShipInstance.DefendVSTorp

	original5 = FoundationTech.TractorEvent.__call__

	def NDefendVSBeam(self, pShip, pEvent):
		debug(__name__ + ", DefendVSBeam")
		try:
			pEmitter = App.PhaserBank_Cast(pEvent.GetSource())
			sName = pEmitter.GetFireSound()
			oYield = FoundationTech.dYields[sName]
		except:
			oYield = None

		for i in self.lBeamDefense:
			try:
				if i.OnBeamDefense(pShip, self, oYield, pEvent):
					return
			except:
				traceback.print_exc()

		if oYield:
			oYield.OnYield(pShip, self, pEvent)

	def NDefendVSTractor(self, pShip, pEvent):
		debug(__name__ + ", DefendVSTractor")
		try:
			pProjector = App.TractorBeamProjector_Cast(pEvent.GetSource())
			sName = pProjector.GetFireSound()
			oYield = FoundationTech.dYields[sName]
		except:
			oYield = None

		for i in self.lTractorDefense:
			try:
				if i.OnTractorDefense(pShip, self, oYield, pEvent):
					return
			except:
				traceback.print_exc()
		if oYield:
			oYield.OnYield(pShip, self, pEvent)


	def NDefendVSPulse(self, pShip, pEvent, pTorp):
		debug(__name__ + ", DefendVSPulse")
		try:
			sName = pTorp.GetModuleName()
			oYield = FoundationTech.dYields[sName]
		except:
			oYield = None

		for i in self.lPulseDefense:
			try:
				if i.OnPulseDefense(pShip, self, pTorp, oYield, pEvent):
					return
			except:
				traceback.print_exc()

		if oYield:
			oYield.OnYield(pShip, self, pEvent, pTorp)

	def NDefendVSTorp(self, pShip, pEvent, pTorp):
		debug(__name__ + ", DefendVSTorp")
		try:
			sName = pTorp.GetModuleName()
			oYield = FoundationTech.dYields[sName]
		except:
			oYield = None

		for i in self.lTorpDefense:
			try:
				if i.OnTorpDefense(pShip, self, pTorp, oYield, pEvent):
					return
			except:
				traceback.print_exc()

		if oYield:
			oYield.OnYield(pShip, self, pEvent, pTorp)

	def tractorEventNewCall(self, now):
		debug(__name__ + ", __call__")
		if self._when > 0.25:
			self._when = 0.25
		try:
			if (not hasattr(self, "Ship")) or self.Ship == None or (not hasattr(self, "Event")) or self.Event == None:
				self._when = 0
			else:
				pShipT = None
				if hasattr(self.Ship, "GetObjID"):
					shipID = self.Ship.GetObjID()
					if shipID == None or shipID == App.NULL_ID:
						self._when = 0
					else:
						pShip = App.ShipClass_GetObjectByID(None, shipID)
						if pShip != None and hasattr(self, "_source") and hasattr(self._source, "DefendVSTractor"):
							self._source.DefendVSTractor(pShipT, self.Event) # self._source is on this case the pInstance
						else:
							self._when = 0
				else:
					self._when = 0
		except:
			traceback.print_exc()
			self._when = 0
		return self._when # if value is 0, it makes it stop - else it will repeat after self._when seconds


	FoundationTech.ShipInstance.DefendVSBeam = NDefendVSBeam
	FoundationTech.ShipInstance.DefendVSTractor = NDefendVSTractor
	FoundationTech.ShipInstance.DefendVSPulse = NDefendVSPulse
	FoundationTech.ShipInstance.DefendVSTorp = NDefendVSTorp
	FoundationTech.TractorEvent.__call__ = tractorEventNewCall

	print "Updated FoundationTech.ShipInstance's DefendVS* Fixes"
