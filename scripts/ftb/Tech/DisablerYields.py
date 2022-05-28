from bcdebug import debug
import App

import FoundationTech
import MissionLib
import Foundation

#########################################################################################################################
##	YieldType:													#
##			SensorDisable:		Sensors disabled for SensorDisabledTime seconds			#
##			ShieldDisruptor		Target shields are disrupted for ShieldDisabledTime seconds		#
##			EngineJammer:		Target Engines are disabled for EngineDisabledTime seconds		#
##			Ion Cannon:		Random Subtarget disabled for IonCannonDisabledTime seconds		#
##						    with a 1 on IonCannonMiss to have no effect				#
##			CloakBurn:		Target CloakingSys is disabled for CloakDisabledTime seconds	#
#########################################################################################################################

NonSerializedObjects = (
"oPowerDisable",
"oSensorDisable",
"oWarpDisable",
"oImpulseDisable",
"oShieldDisable",
"oCloakDisable",
"oMultipleDisable",
"oRandomDisable",
)

class DisablerTorpDef(FoundationTech.TechDef):
	def __init__(self, name, dict):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.sSelfDisabled = None
		self.sTargetDisabled = None
		self.sEffect = None
		self.__dict__.update(dict)
		self.tDisable = 10

	def GetSubSys(self, pShip):			return

	def MakeEffects(self, pShip, pSubSys, pTorp, bTalk):
		debug(__name__ + ", MakeEffects")
		if FoundationTech.BridgeFX and bTalk:
			PID = MissionLib.GetPlayer().GetObjID()
			AID = pTorp.GetParentID()
			SID = pShip.GetObjID()

			if pSubSys.IsDisabled():
				if PID == SID and self.sSelfDisabled:
					FoundationTech.BridgeFX.MakeCharacterSay(self.sSelfDisabled[0], self.sSelfDisabled[1])
				elif PID == AID and self.sTargetDisabled:
					FoundationTech.BridgeFX.MakeCharacterSay(self.sTargetDisabled[0], self.sTargetDisabled[1])

		#if FoundationTech.EffectsLib and self.sEffect:
		#	FoundationTech.EffectsLib.CreateSpecialFXSeq(pShip, pEvent, self.sEffect)

	def OnYield(self, pShip, pInstance, pEvent, pTorp = None, time = None):
		debug(__name__ + ", OnYield")
		pSubSys = self.GetSubSys(pShip)
		if not pSubSys:
			return

		bPrevDisabled = 0
		if pSubSys.IsDisabled():
			bPrevDisabled = 1

		if time:
			# We assume that if we get a time argument,
			# another tech is in charge of effects -Dasher42
			pInstance.DisableSubSys(pShip, pSubSys, time)
		else:
			pInstance.DisableSubSys(pShip, pSubSys, self.tDisable)
			self.MakeEffects(pShip, pSubSys, pTorp, bPrevDisabled)

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()



class PowerDisableDef(DisablerTorpDef):
	def GetSubSys(self, pShip):			return pShip.GetPowerSubsystem()

oPowerDisable = PowerDisableDef('Power Disable', {
	'tDisable':			10,
	'sSelfDisabled':	('Miguel', 'SelfPowerDisabled'),
	'sTargetDisabled':	('Miguel', 'TargetPowerDisabled'),
	# 'sEffect':			''
})


class SensorDisableDef(DisablerTorpDef):
	debug(__name__ + ", GetSubSys")
	def GetSubSys(self, pShip):			return pShip.GetSensorSubsystem()

oSensorDisable = SensorDisableDef('Sensor Disable', {
	'tDisable':			10,
	'sSelfDisabled':	('Miguel', 'SelfSensorsDisabled'),
	'sTargetDisabled':	('Miguel', 'TargetSensorsDisabled'),
	# 'sEffect':			''
})


class WarpDisableDef(DisablerTorpDef):
	debug(__name__ + ", GetSubSys")
	def GetSubSys(self, pShip):			return pShip.GetWarpEngineSubsystem()

oWarpDisable = WarpDisableDef('Warp Disable', {
	'tDisable':			10,
	'sSelfDisabled':	('Miguel', 'SelfImpulseDisabled'),
	'sTargetDisabled':	('Miguel', 'TargetImpulseDisabled'),
	# 'sEffect':			''
})


class ImpulseDisableDef(DisablerTorpDef):
	debug(__name__ + ", GetSubSys")
	def GetSubSys(self, pShip):			return pShip.GetImpulseEngineSubsystem()

oImpulseDisable = ImpulseDisableDef('Impulse Disable', {
	'tDisable':			10,
	'sSelfDisabled':	('Brex', 'SelfImpulseDisabled'),
	'sTargetDisabled':	('Miguel', 'TargetImpulseDisabled'),
	# 'sEffect':			''
})


class ShieldDisableDef(DisablerTorpDef):
	debug(__name__ + ", GetSubSys")
	def GetSubSys(self, pShip):			return pShip.GetShields()

oShieldDisable = ShieldDisableDef('Shield Disable', {
	'tDisable':			10,
	'sSelfDisabled':	('Brex', 'SelfShieldsDisabled'),
	'sTargetDisabled':	('Miguel', 'TargetShieldsDisabled'),
	# 'sEffect':			''
})


class CloakDisableDef(DisablerTorpDef):
	debug(__name__ + ", GetSubSys")
	def GetSubSys(self, pShip):			return pShip.GetCloakingSubsystem()

oCloakDisable = CloakDisableDef('Cloak Disable', {
	'tDisable':			10,
})



class MultipleDisableDef(FoundationTech.TechDef):
	debug(__name__ + ", GetSubSys")
	def __init__(self, name, dict):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.lYields = []
		self.__dict__.update(dict)

	def OnYield(self, pShip, pInstance, pEvent, pTorp = None):
		debug(__name__ + ", OnYield")
		for i in self.lYields:
			i[0].OnYield(pShip, pInstance, pEvent, pTorp, i[1])

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()

oMultipleDisable = MultipleDisableDef('Multiple Disable', {
	'lYields':		[
		# TechDef Instance, Time
		(oShieldDisable, 10),
		(oSensorDisable, 10)
	]
})


class RandomDisableDef(FoundationTech.TechDef):
	def __init__(self, name, dict):
		debug(__name__ + ", __init__")
		FoundationTech.TechDef.__init__(self, name, FoundationTech.dMode)
		self.lYields = []
		self.__dict__.update(dict)

	def OnYield(self, pShip, pInstance, pEvent, pTorp = None):
		debug(__name__ + ", OnYield")
		rnd = App.g_kSystemWrapper.GetRandomNumber(100)
		for i in self.lYields:
			rnd = rnd - i[2]
			if rnd <= 0:
				return i[0].OnYield(pShip, pInstance, pEvent, pTorp)

	# def Activate(self):
	# 	FoundationTech.oWeaponHit.Start()
	# def Deactivate(self):
	# 	FoundationTech.oWeaponHit.Stop()


oRandomDisable = RandomDisableDef('Random Disable', {
	'lYields':		[
		# TechDef Instance, Time, Chance
		(oSensorDisable,  10, 20),
		(oWarpDisable,    10, 20),
		(oImpulseDisable, 10, 20),
		(oShieldDisable,  10, 20),
		(oCloakDisable,   10, 10),
		(oPowerDisable,   10, 10),
	]
})


# print 'Disabler yields loaded'
