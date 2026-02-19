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
# ---- 'splitProx': minimum distance that the parent projectile about to split ("shell") needs to be from the target to split, default is 100 (if 'multipleTargetSelect': 0) or 250 (any other value). Seems to use in-game units, not km.
# ---- 'chkInterval': check how often the distance is verified, in seconds. Default is 1. Can also be used as a timer.
# -- Since this tech inherits from TimedTorpedoes, it also uses the following parameters (TimedTorpedoes does not seem to have default for these, but this techs adds defaults for itself):
# ---- 'spreadNumber': number of torpedoes the shell splits into. Default is 1.
# ---- 'spreadDensity': how packed together the new torps will be, regarding their directions. The higher its value, the more similar their initial directions will look like to the shell's. Default is 1.
# ---- 'shellLive': if set to 0 the shell will have its lifetime cut to 0 when splitting, effectively despawning the shell. Default is 0.
# HOW-TO- ADD
# At the bottom of your torpedo projectile file add this (Between the """ and """) and adjust its contents to your preferences:
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

##################################
#
MODINFO = { "Author": "\"ftb Team\", \"Apollo\", \"Greystar\", \"Alex SL Gato\" (andromedavirgoa@gmail.com)",
	    "Version": "0.1",
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

S_F_PATH = ["ftb.Tech.TimedTorpedoes", "Custom.Techs.TimedTorpedoes"] # TO-DO update some code below if these change, too
S_F_PATH_DEPENDENCY = ["ftb.Tech.SolidProjectiles", "Custom.Techs.SolidProjectiles"] # TO-DO update some code below if these change, too

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
			fndScriptS = __import__(backupPath)
			attempts = 1
		except:
			fndScriptS = None
			attempts = -1
	return attempts, fndScriptS

ATTEMPT_TIMED_TORP, SCRIPT_INHERITED = getScriptToInherit()

def isSolidProjectilesPatched(scriptOne, listi, notDone):
	isPatched = 0
	if scriptOne != None and hasattr(scriptOne, "MODINFO") and scriptOne.MODINFO.has_key("Version") and scriptOne.MODINFO["Version"] >= 0.4:
		if hasattr(scriptOne, "AuxInitiater") and hasattr(scriptOne.AuxInitiater, "TorpedoEnteredSet"):
			isPatched = 1

	if isPatched and notDone:
		if listi == 0: # TO-DO Update this if folders change
			import ftb.Tech.SolidProjectiles
		elif listi == 1: # TO-DO Update this if folders change
			import Custom.Techs.SolidProjectiles

	return isPatched



if SCRIPT_INHERITED != None and hasattr(SCRIPT_INHERITED, "MIRVMultiTargetTorpedo") and hasattr(SCRIPT_INHERITED, "SingleMIRVEvent") and hasattr(SCRIPT_INHERITED, "MultipleMIRVEvent"):

	class MIRVMultiSingleTargetTorpedoFire2(SCRIPT_INHERITED.MIRVMultiTargetTorpedo):
		def __init__(self, name, dict):
			SCRIPT_INHERITED.MIRVMultiTargetTorpedo(self, name, dict)
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

						myClassCall = None
						if self.multipleTargetSelect == 0:
							myClassCall = SCRIPT_INHERITED.SingleMIRVEvent
						else:
							myClassCall = SCRIPT_INHERITED.MultipleMIRVEvent

						if myClassCall != None:

							hasChkInterval = hasattr(self, "chkInterval")
							hasShellLive = hasattr(self, "shellLive")
							hasSplitProx = hasattr(self, "splitProx")
							hasSpreadNumber = hasattr(self, "spreadNumber")
							hasSpreadDensity = hasattr(self, "spreadDensity")


							if not hasChkInterval:
								self.chkInterval = 1

							if not hasShellLive:
								self.shellLive = 0

							if not hasSplitProx:
								if self.multipleTargetSelect == 0:
									self.splitProx = 100
								else:
									self.splitProx = 250

							if not hasSpreadNumber:
								self.spreadNumber = 1

							if not hasSpreadDensity:
								self.spreadDensity = 1

							FoundationTech.oEventQueue.Queue(
								TorpDistanceEvent(
									pTorpID,
									pTorp.GetTargetID(),
									myClassCall(pTorpID, self, self.multipleTargetSelect),
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