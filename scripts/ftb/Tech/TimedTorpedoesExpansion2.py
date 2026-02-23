# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE FOUNDATION LGPL LICENSE AS WELL
# TimedTorpedoesExpansion.py
# 23rd February 2026, by Alex SL Gato, based and depending on TimedTorpedoes (by the ftb team; scripts/ftb/Techs/TimedTorpedoes or scripts/Custom/Techs/TimedTorpedoes) to work
# This tech also depends on Alex SL Gato's TimedTorpedoesExpansion to work.
# This script depends on Alex SL Gato's updated SolidProjectiles (by the ftb team; scripts/ftb/Techs/SolidProjectiles or scripts/Custom/Techs/SolidProjectiles) to work fully
#################################################################################################################
# This script just adds an extra function, so you can call MIRV events which generate a sound, following the example from TimedTorpedoesExpansion.
# This adds a new parameter to the dict, 'RelaunchSound', which is the sound which will be heard when the shell splits.
#
import App
from bcdebug import debug
import traceback

sTTE = "TimedTorpedoesExpansion"
S_F_PATHTTE = ["ftb.Tech." + str(sTTE), "Custom.Techs." + str(sTTE)]

def getScriptToInherit(firstPath=S_F_PATHTTE[0], backupPath=S_F_PATHTTE[1]):
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

TimedTorpedoesExpansion = getScriptToInherit()

#if TimedTorpedoesExpansion and hasattr(TimedTorpedoesExpansion, "MIRVMultiSingleTargetTorpedoFire2") and TimedTorpedoesExpansion.MIRVMultiSingleTargetTorpedoFire2 != None and hasattr(TimedTorpedoesExpansion, "SCRIPT_INHERITED") and TimedTorpedoesExpansion.SCRIPT_INHERITED != None and hasattr(TimedTorpedoesExpansion.SCRIPT_INHERITED, "SingleMIRVEvent") and TimedTorpedoesExpansion.SCRIPT_INHERITED.SingleMIRVEvent != None and hasattr(TimedTorpedoesExpansion.SCRIPT_INHERITED, "MultipleMIRVEvent") and TimedTorpedoesExpansion.SCRIPT_INHERITED.MultipleMIRVEvent != None:
def newCustomFunctionFor2S(self, now, oTech, trpE)
	try:
		if oTech != None:
			if hasattr(oTech, 'RelaunchSound') and hasattr(self, 'pTorpID'):
				pTorp = App.Torpedo_GetObjectByID(None, self.pTorpID)
				if pTorp:
					pPlayer = App.Game_GetCurrentPlayer()
					if pPlayer and not pPlayer.IsDead() or pPlayer.IsDying():
						pSet = pTorp.GetContainingSet()
						pPlaSet = pPlayer.GetContainingSet()
						if pSet != None and pPlaSet != None and pSet.GetRegionModule() == pPlaSet.GetRegionModule():
							App.g_kSoundManager.PlaySound(self.oTech.RelaunchSound())

			if hasattr(oTech, 'multipleTargetSelect') and oTech.multipleTargetSelect != None and oTech.multipleTargetSelect != 0:
				TimedTorpedoesExpansion.SCRIPT_INHERITED.MultipleMIRVEvent.__call__(self, now)
			else:
				TimedTorpedoesExpansion.SCRIPT_INHERITED.SingleMIRVEvent.__call__(self, now)
	except:
		print __name__, " error while applying newCustomFunctionFor2S:"
		traceback.print_exc()

	trpE = 0
	return trpE