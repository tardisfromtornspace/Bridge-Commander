# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE FOUNDATION LGPL LICENSE AS WELL
# TimedTorpedoesExpansion.py
# 20th February 2026, by Alex SL Gato, based and depending on TimedTorpedoes (by the ftb team; scripts/ftb/Techs/TimedTorpedoes or scripts/Custom/Techs/TimedTorpedoes) to work
# This script depends on Alex SL Gato's updated SolidProjectiles (by the ftb team; scripts/ftb/Techs/SolidProjectiles or scripts/Custom/Techs/SolidProjectiles) to work fully
#################################################################################################################
# This script:
# 1st if the proper SolidProjectiles is patched, allows MIRV torpedoes to work from separate phases, pulses and even phased cloak.
# 2nd gives more customization parameters to the MIRV:
# ---- 'multipleTargetSelect': if it selects 1 or multiple targets when splitting ('multipleTargetSelect': 0 or 'multipleTargetSelect': 1). Default 0 (always choose the same target).
# ---- 'splitProx': minimum distance that the parent projectile about to split ("shell") needs to be from the target to split, default is 100 (if 'multipleTargetSelect': 0) or 250 (any other value of 'multipleTargetSelect'). Seems to use in-game units, not km.  Can also be used to get something inside alternateClassCall1,... on that case the structure would be "splitProx": {"splitProx": 1, "extras": {}}
# ---- 'chkInterval': check how often the distance is verified, in seconds. Default is 1. Can also be used as a timer.
# ---- 'chkInterval2': same as checkInterval, but for the actual effect event. Default is 0 (if 'multipleTargetSelect': 0) or 1 (any other value of 'multipleTargetSelect').
# ---- 'alternateClassCall2': in case you don't want the function/class that the alternateFTBEvent/TorpDistanceEvent handles to be the regular SingleMIRVEvent or MultipleMIRVEvent, but another. To add extra parameters to this one, consider adding them like normal.
# --------- 'CustomFunction2': a function (see below "@SECTION B") that allows you to change stuff when the alternateClassCall2 event is called. It has as input parameters "self" (from where you can get the oTech itself for anything extra you may need), "now" (see FTB Queue stuff), "oTech" (to access stuff from your tech easier) and a fourth variable (trpE) which indicates if the torp exists or not. This function must return trpE unless you want to actually change that to handle errors or because you want to perform some weird delayed effect if the torp is gone. In case of doubt, it is preferable to return 0 since at least that will prevent the script from cluttering things with those queued events.
# --------- 'maxIntervalLax2': a function (see below "@SECTION A"), allows you to change the interval between parts to a degree. Only uses "self", "now" and "oTech"
# --------- 'OnlyWhenTheTorpStoppedExisting2' interesting value to call if you want this to only happen after the torp stopped existing
# ---- 'alternateClassCall1': in case you don't want the default TorpDistanceEvent to do most of the initial calculations, but another class of FTBEvent. When a new function is called, if you also have a 'alternateClassCall1Extras' set to 1, the distance parameters are changed to fit inside the Tech, so any classes for this one would need to have that taken into account. It uses the same parameters as alternateClassCall2 but without the "2" ('maxIntervalLax', 'CustomFunction')
# -- Since this tech inherits from TimedTorpedoes, it also uses the following parameters (TimedTorpedoes does not seem to have default for these, but this techs adds defaults for itself):
# ---- 'spreadNumber': number of torpedoes the shell splits into. Default is 1.
# ---- 'spreadDensity': how packed together the new torps will be, regarding their directions. The higher its value, the more similar their initial directions will look like to the shell's. Default is 1.
# ---- 'shellLive': if set to 0 the shell will have its lifetime cut to 0 when splitting, effectively despawning the shell. Default is 0.
# -- Since this tech inherits from TimedTorpedoes, it also uses the following parameters:
# ---- 'warheadModule': the actual path to the new projectile file.
# HOW-TO- ADD
# At the bottom of your torpedo projectile file add this (Between the """ and """) and adjust its contents to your preferences:
# OPTION A: Example with regular default TimedTorpedoes classes
"""
import traceback
try:
	import FoundationTech
	import ftb.Tech.TimedTorpedoesExpansion
	oFire = ftb.Tech.TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2(
		'MIRVMultiSingleTargetTorpedoFire2', {
		'multipleTargetSelect': 0,
		'spreadNumber': 3,
		'spreadDensity': 358.0,
		'warheadModule': "Tactical.Projectiles.B5ThirdspaceTeleAttack",
		'shellLive': 0,
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()
"""
# OPTION B: Create your own classes and functions
# Below is an example of adding techs in such a way that both functions are replaced - please take note that ideally for adding such functions you should NEVER add them on the projectile, particularly for that size... (SEE OPTION C) 
"""
## def GetDamage():
##	return 1000.0

import traceback
try:
	import FoundationTech
	import ftb.Tech.TimedTorpedoesExpansion

	thisWouldBeTheClass1 = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassDLoop
	def newCustomFunctionFor1(self, now, oTech, trpE): # Skip things, call the other event now
		if trpE:
			#trpE = 0 <-- uncomment this and it will only do the event ONCE
			self.oEvent(now)
		return trpE

	thisWouldBeTheClass2 = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassLoop
	def newCustomFunctionFor2(self, now, oTech, trpE):
		damageChanged = 0
		if trpE:
			pTorp = App.Torpedo_GetObjectByID(None, self.pTorpID)
			if pTorp and hasattr(pTorp, "GetDamage") and hasattr(pTorp, "SetDamage"):
				getDmg = pTorp.GetDamage()
				if getDmg > 0:
					if hasattr(oTech, 'LOOK_CUSTOM_INI_DMG'):
						valueIni = oTech.LOOK_CUSTOM_INI_DMG
						typeValueIni = type(valueIni)
						if (type(1) == typeValueIni or type(1.0) == typeValueIni) and hasattr(oTech, 'LOOK_CUSTOM_XTRA_DMG'):
							valuePlus = oTech.LOOK_CUSTOM_XTRA_DMG
							typeValuePlus = type(valuePlus)
							if type(1) == typeValuePlus or type(1.0) == typeValuePlus:
								newValue = getDmg + (valueIni * valuePlus)
								if hasattr(oTech, 'LOOK_CUSTOM_MAX_DMG'):
									valueMax = oTech.LOOK_CUSTOM_MAX_DMG
									typevalueMax = type(valueMax)
									if type(1) == typevalueMax or type(1.0) == typevalueMax:
										if newValue > valueMax:
											newValue == valueMax
								if newValue < 0.00001:
									newValue = 0.00001
									trpE = 0
								pTorp.SetDamage(newValue)
								damageChanged = 1
		if not damageChanged:
			trpE = 0

		return trpE

	oFire = ftb.Tech.TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2(
		'MIRVMultiSingleTargetTorpedoFire2', {
		'alternateClassCall1': thisWouldBeTheClass1,
		'alternateClassCall2': thisWouldBeTheClass2,
		'alternateClassCall1Extras': 1,
		'multipleTargetSelect': 1,
		'spreadNumber': 3,
		'spreadDensity': 4.5,
		'warheadModule': "Tactical.Projectiles.ZZSpread2",
		'shellLive': 0,
		'CustomFunction': newCustomFunctionFor1,
		'CustomFunction2': newCustomFunctionFor2,
		'LOOK_CUSTOM_XTRA_DMG': 0.1,
		'LOOK_CUSTOM_MAX_DMG': GetDamage() * 9, # GetDamage() from the projectile script
		'LOOK_CUSTOM_INI_DMG': GetDamage(),
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()

"""
# OPTION C: Create your own classes and functions and keep them on a separate file. This one is the best option if you need complex stuff! then you just ahve to import such functions! On my case since these functions are quite useful and I made them myself for this example, I will leave them functional inside this file!!!
# Please note that these can be optimized even more. For example with the functions I called some of the parameters became superfluous and could be omitted.
"""
import traceback
try:
	import FoundationTech
	import ftb.Tech.TimedTorpedoesExpansion

	# You would need to add another import for each different file you are importing a function from.
	# import ftb.Tech.TimedTorpedoesExpansion
	repeatClass = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassDLoop
	newFuncRepeat = ftb.Tech.TimedTorpedoesExpansion.newCustomFunctionFor1           # <--- and you would change that, too

	ActClass = ftb.Tech.TimedTorpedoesExpansion.TorpedoActionClassLoop
	newFuncAct = ftb.Tech.TimedTorpedoesExpansion.newCustomFunctionFor2              # <--- and you would change that, too

	oFire = ftb.Tech.TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2(
		'MIRVMultiSingleTargetTorpedoFire2', {
		'alternateClassCall1': repeatClass,
		'alternateClassCall2': ActClass,
		'alternateClassCall1Extras': 1,
		'multipleTargetSelect': 1,
		'spreadNumber': 3,
		'spreadDensity': 4.5,
		'warheadModule': "Tactical.Projectiles.ZZSpread2",
		'shellLive': 0,
		'CustomFunction': newFuncRepeat,
		'CustomFunction2': newFuncAct,
		'LOOK_CUSTOM_XTRA_DMG': 0.1,
		'LOOK_CUSTOM_MAX_DMG': GetDamage() * 9, # GetDamage() from the projectile script
		'LOOK_CUSTOM_INI_DMG': GetDamage(),
	})
	FoundationTech.dOnFires[__name__] = oFire
except:
	print "Something went wrong with TimedTorpedoesExpansion"
	traceback.print_exc()
"""

##################################
#
MODINFO = { "Author": "\"ftb Team\", \"Apollo\", \"Greystar\", \"Alex SL Gato\" (andromedavirgoa@gmail.com)",
	    "Version": "0.16",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#
import App
from bcdebug import debug
import traceback

import Foundation
import FoundationTech

SCRIPT_INHERITED = None
SCRIPT_DEPENDENCY = None

S_F_PATH = ["ftb.Tech.TimedTorpedoes", "Custom.Techs.TimedTorpedoes"] # FUTURE TO-DO update some code below if these change, too
S_F_PATH_DEPENDENCY = ["ftb.Tech.SolidProjectiles", "Custom.Techs.SolidProjectiles"] # FUTURE TO-DO update some code below if these change, too

ATTEMPT_TIMED_TORP = None
ATTEMPT_SOLID_PROJ = None

DEPENDENCY_PATCHED = None

def getScriptToInherit(firstPath=S_F_PATH[0], backupPath=S_F_PATH[1]):
	fndScriptS = None
	attempts = -1
	try:
		fndScriptS = __import__(firstPath)
		attempts = 0
	except:
		try:
			if backupPath != None:
				fndScriptS = __import__(backupPath)
			attempts = 1
		except:
			fndScriptS = None
			attempts = -1
	return attempts, fndScriptS

def isSolidProjectilesPatched(scriptOne, listi, notDone):
	isPatched = 0
	if scriptOne != None and hasattr(scriptOne, "MODINFO") and scriptOne.MODINFO.has_key("Version") and scriptOne.MODINFO["Version"] >= 0.4:
		if hasattr(scriptOne, "AuxInitiater") and hasattr(scriptOne.AuxInitiater, "TorpedoEnteredSet"):
			isPatched = 1

	if isPatched and notDone:
		if listi == 0: # FUTURE TO-DO Update this if folders change
			import ftb.Tech.SolidProjectiles
		elif listi == 1: # FUTURE TO-DO Update this if folders change
			import Custom.Techs.SolidProjectiles

	return isPatched


def newCustomFunctionFor1(self, now, oTech, trpE): # Skip things, call the other event now
	if trpE:
		#trpE = 0 <-- uncomment this and it will only do the event ONCE
		self.oEvent(now)
	return trpE

def newCustomFunctionFor2(self, now, oTech, trpE):
	damageChanged = 0
	if trpE:
		pTorp = App.Torpedo_GetObjectByID(None, self.pTorpID)
		if pTorp and hasattr(pTorp, "GetDamage") and hasattr(pTorp, "SetDamage"):
			getDmg = pTorp.GetDamage()
			if getDmg > 0:
				if hasattr(oTech, 'LOOK_CUSTOM_INI_DMG'):
					valueIni = oTech.LOOK_CUSTOM_INI_DMG
					typeValueIni = type(valueIni)
					if (type(1) == typeValueIni or type(1.0) == typeValueIni) and hasattr(oTech, 'LOOK_CUSTOM_XTRA_DMG'):
						valuePlus = oTech.LOOK_CUSTOM_XTRA_DMG
						typeValuePlus = type(valuePlus)
						if type(1) == typeValuePlus or type(1.0) == typeValuePlus:
							newValue = getDmg + (valueIni * valuePlus)
							if hasattr(oTech, 'LOOK_CUSTOM_MAX_DMG'):
								valueMax = oTech.LOOK_CUSTOM_MAX_DMG
								typevalueMax = type(valueMax)
								if type(1) == typevalueMax or type(1.0) == typevalueMax:
									if newValue > valueMax:
										newValue == valueMax
							if newValue < 0.00001:
								newValue = 0.00001
								trpE = 0
							pTorp.SetDamage(newValue)
							damageChanged = 1
	if not damageChanged:
		trpE = 0

	return trpE


class TorpedoActionClassLoop(FoundationTech.FTBEvent): # Example of an 'alternateClassCall2' For the inner class replacement

	def __init__(self, pTorpID, oTech, when): # On this one we can just add a function from the oTech
		debug(__name__ + ", TorpedoActionClassLoop.__init__")
		self._source = None
		self._when = when
		self.interval = when
		self.pTorpID = pTorpID
		self.oTech = oTech
		self.smyPeriodFunc = "maxIntervalLax2" # @SECTION A
		self.smyCustomFunction = "CustomFunction2" # @SECTION B
		self.sTorpWhenNo = "OnlyWhenTheTorpStoppedExisting2" # @SECTION C

	def __call__(self, now): # we are in a loop, we will be forcing them to have a repeatable equal loop
		debug(__name__ + ", TorpedoActionClassLoop.OnFire")
		self.keepPeriodsEqual(now)
		trpE = self.safeOurTorpExists(now)
		trpE2 = self.safeCustomFunction(now, trpE)

		if not trpE2:
			self._when = 0
		return self._when

	def keepPeriodsEqual(self, now): # Yup, allowing people to inherit and change the effects!
		multiplier = 1.0

		if hasattr(self, "oTech") and self.oTech != None and hasattr(self.oTech, self.smyPeriodFunc): # @SECTION A
			newMult = None
			try:
				leFunction = getattr(self.oTech, self.smyPeriodFunc)
				if leFunction != None:
					newMult = leFunction(self, now, self.oTech)  # @SECTION A
					if newMult < 0.0:
						newMult = 0.0
			except:
				traceback.print_exc()
				newMult = None

			if newMult != None:
				multiplier = newMult

		if self._when > self.interval * multiplier:	
			self._when = self.interval * multiplier

	def safeCustomFunction(self, now, trpE):
		try:
			if hasattr(self, "oTech") and self.oTech != None and (trpE or (hasattr(self.oTech, self.sTorpWhenNo) and getattr(self.oTech, self.sTorpWhenNo) == 1)) and hasattr(self.oTech, self.smyCustomFunction): # @SECTION B
				leFunction = getattr(self.oTech, self.smyCustomFunction)
				if leFunction != None:
					trpE = leFunction(self, now, self.oTech, trpE) # @SECTION B
		except:
			traceback.print_exc()
			trpE = 0

		return trpE


	def safeOurTorpExists(self, now):
		trpE = 0
		try:
			trpE = self.ourTorpExists(now)
		except:
			traceback.print_exc()
			trpE = 0
		return trpE

	def ourTorpExists(self, now):
		ourTrpE = 0
		if hasattr(self, "pTorpID") and self.pTorpID != None and self.pTorpID != App.NULL_ID:
			pTorp = App.Torpedo_GetObjectByID(None, self.pTorpID)
			if pTorp:
				ourTrpE = 1
		return ourTrpE



class TorpedoActionClassDLoop(TorpedoActionClassLoop): # Example of an 'alternateClassCall1' For distance replacement
	def __init__(self, pFirstID, pSecondID, oEvent, distance, when):
		debug(__name__ + ", __init__")
		self._source = None
		self._when = when
		self.interval = when
		self.pTorpID = pFirstID
		self.pSecondID = pSecondID
		self.oEvent = oEvent

		distanceTime = 100.0
		techAux = None

		try:
			if distance != None:
				typedistance = type(distance)
				if (type(1) == typedistance or type(1.0) == typedistance):
					distanceTime = distance
				elif type([]) == typedistance:
					if len(distance) > 0:
						if (type(1) == distance[0] or type(1.0) == distance[0]):
							distanceTime = distance[0]
						if len(distance) > 1:
							techAux = distance[1]
				elif type({}) == typedistance:
					if distance.has_key("splitProx") and distance["splitProx"] != None:
						typedistancechkInterval2 = type(distance["splitProx"])
						if (type(1) == typedistancechkInterval2 or type(1.0) == typedistancechkInterval2) and not distance["splitProx"] < 0.0:
							distanceTime = distance["splitProx"]

					if distance.has_key("extras") and distance["extras"] != None:
						techAux = distance["extras"]
		except:
			traceback.print_exc()
			whenTime = 1.0
			extrasAdded = 0

		self.oTech = techAux
		self.distance = distanceTime

		self.smyPeriodFunc = "maxIntervalLax" # @SECTION A
		self.smyCustomFunction = "CustomFunction" # @SECTION B
		self.sTorpWhenNo = "OnlyWhenTheTorpStoppedExisting" # @SECTION C


ATTEMPT_TIMED_TORP, SCRIPT_INHERITED = getScriptToInherit()

if SCRIPT_INHERITED != None and hasattr(SCRIPT_INHERITED, "MIRVMultiTargetTorpedo") and hasattr(SCRIPT_INHERITED, "SingleMIRVEvent") and hasattr(SCRIPT_INHERITED, "MultipleMIRVEvent") and hasattr(SCRIPT_INHERITED, "TorpDistanceEvent"):

	class MIRVMultiSingleTargetTorpedoFire2(SCRIPT_INHERITED.MIRVMultiTargetTorpedo):
		def __init__(self, name, dict):
			SCRIPT_INHERITED.MIRVMultiTargetTorpedo.__init__(self, name, dict)
			self.checkIfAScriptIsPatched()

		def scriptFilePatch(self):
			return S_F_PATH_DEPENDENCY[0]

		def scriptFilePatchAlternate(self):
			return S_F_PATH_DEPENDENCY[1]

		def IwannaBeWithPulsesToo(self):
			return 1

		def OnFire2(self, pEvent, pTorp):
			debug(__name__ + ", OnFire2")
			try:
				if pTorp != None:
					pTorpID = pTorp.GetObjID()
					if pTorpID != None and pTorpID != App.NULL_ID:

						hasMultTrgt = hasattr(self, "multipleTargetSelect")
						if not hasMultTrgt:
							self.multipleTargetSelect = 0

						hasalternateClassCall1 = hasattr(self, "alternateClassCall1")
						if not hasalternateClassCall1:
							self.alternateClassCall1 = SCRIPT_INHERITED.TorpDistanceEvent

						myClassCall = None
						hasalternateClassCall2 = hasattr(self, "alternateClassCall2")
						if not hasalternateClassCall2:
							if self.multipleTargetSelect == 0:
								myClassCall = SCRIPT_INHERITED.SingleMIRVEvent
							else:
								myClassCall = SCRIPT_INHERITED.MultipleMIRVEvent
						else:
							myClassCall = self.alternateClassCall2

						if myClassCall != None:

							hasChkInterval = hasattr(self, "chkInterval")
							hasChkInterval2 = hasattr(self, "chkInterval2")

							hasShellLive = hasattr(self, "shellLive")
							hasSplitProx = hasattr(self, "splitProx")
							hasSpreadNumber = hasattr(self, "spreadNumber")
							hasSpreadDensity = hasattr(self, "spreadDensity")

							hasalternateClassCall1Extras = (hasattr(self, "alternateClassCall1Extras") and self.alternateClassCall1Extras != None and self.alternateClassCall1Extras == 1)
							if not hasChkInterval:
								self.chkInterval = 1

							if not hasChkInterval2:
								if self.multipleTargetSelect == 0:
									self.chkInterval2 = 0
								else:
									self.chkInterval2 = 1

							if not hasShellLive:
								self.shellLive = 0

							if not hasSplitProx:
								if self.multipleTargetSelect == 0:
									if hasalternateClassCall1 and hasalternateClassCall1Extras:
										self.splitProx = {"splitProx": 100, "extras": self}
									else:
										self.splitProx = 100
								else:
									if hasalternateClassCall1 and hasalternateClassCall1Extras:
										self.splitProx = {"splitProx": 250, "extras": self}
									else:
										self.splitProx = 250

							elif hasalternateClassCall1 and hasalternateClassCall1Extras:
								typeUS = type(self.splitProx)
								if type(1) == typeUS or type(1.0) == typeUS:
									oldVals = self.splitProx
									self.splitProx = {"splitProx": oldVals, "extras": self}

							if not hasSpreadNumber:
								self.spreadNumber = 1

							if not hasSpreadDensity:
								self.spreadDensity = 1

							FoundationTech.oEventQueue.Queue( # This is the input structure that self.alternateClassCall2 will need to handle
								self.alternateClassCall1(
									pTorpID,
									pTorp.GetTargetID(),
									myClassCall(pTorpID, self, self.chkInterval2),
									self.splitProx,
									self.chkInterval)
							)
								
			except:
				print __name__, ".", self.name, ".OnFire2 caught an Exception: "
				traceback.print_exc()

		def OnFire(self, pEvent, pTorp):
			debug(__name__ + ", OnFire")
			# Avoiding it counting twice.
			# Adding a fallback in case your SolidProjectiles is not patched
			if (not hasattr(self, "solidProjPatched")) or self.solidProjPatched == 0:
				print __name__, ".", self.name, ".OnFire called ",  __name__, ".", self.name, "OnFire2 because you don't have SolidProjectiles patched or updated"
				self.OnFire2(pEvent, pTorp)
			return

		def checkIfAScriptIsPatched(self):
			global ATTEMPT_SOLID_PROJ, DEPENDENCY_PATCHED, SCRIPT_DEPENDENCY
			if not hasattr(self, "solidProjPatched"):
				self.solidProjPatched = 0

			if ATTEMPT_SOLID_PROJ is None:
				try:
					ATTEMPT_SOLID_PROJ, SCRIPT_DEPENDENCY = getScriptToInherit(S_F_PATH_DEPENDENCY[0], S_F_PATH_DEPENDENCY[1])
				except:
					print __name__, " caught an Exception: "
					traceback.print_exc()
					ATTEMPT_SOLID_PROJ = -1
					SCRIPT_DEPENDENCY = None

			if ATTEMPT_SOLID_PROJ != None:
				
				if DEPENDENCY_PATCHED is None:
					 DEPENDENCY_PATCHED = isSolidProjectilesPatched(SCRIPT_DEPENDENCY, ATTEMPT_SOLID_PROJ, 1)

				if DEPENDENCY_PATCHED == 1:
					self.solidProjPatched = 1

#print __name__, " loaded (extension alternative to TiemdTorpedoes)"