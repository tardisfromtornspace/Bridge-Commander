# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# TWEAK-ShuttleFrameworkDropShields.py
# 25th March 2026
# VERSION 0.11
# By Alex SL Gato
# ftb.LaunchShip.py by sleight42, and the Foundation Technologies team (probably, but not only on this case, Sim Rex, jwattsjr, Admiral Ames and Defiant) -> LaunchAIShip tweak.
#
# Changes: 
# - Now the shuttle framework will not lower the launcher ship shields if:
# -- Both the pLaunchedShip and pLaunchingShip have shields past a certain threshold, indicated by scripts/Custom/Ships file having a "shuttleLaunchShields" value indicating the shield facet strength:
# --- if "shutLauncherShields" set to -3, it will act as pre-patch (will always drop shields). Since this patch was made to apply to all mods
# --- if "shutLauncherShields" set to -2, it will never drop shields to launch a vessel.
# --- if "shutLauncherShields" set to any other value below 0 (but particularly between -1 and 0), it will consider it a threshold (-1 = 100% shield, 0 = 0% shield) - normally this would not affect much since usually vessels start at 100% shield strength.
# --- if "shutLauncherShields" set to any other value above 0 (or the value does not exist), it will consider if the absolute shield strength of each facet for a value (for example, if shutLauncherShields = 500, then if the left shield of the launching ship has 499 shield strength, it will consider the shields too weak to prevent a shuttle from going through) - default is 600 shield strength.
# --- "shutLauncherMultifacet" set to 0 means that it will only evaluate the closest launcher's shield facet to the shuttle launch point for this. Default is 1 (consider all shields).
# --- "shuttleLaunchMultifacet", similar to "shutLauncherMultifacet", but to evaluate the shuttle's closest shield, currently functionally unused except to maybe only consider the shuttle's front shield facet for evaluation. Default is 1 (consider all shields).
# --- "absLauncherShieldHeal", when the ship is launched, how much of the launcher's evaluated shields will gain (or lose, if on negatives) on shield strength. Default is 0 (no shield strength change).
# --- "percLauncherShieldHeal", similar to "absLauncherShieldHeal", but as a multiplier of the maximum, for example if set to 0.8, all evaluated shield facets would gain 80% of the max shield strength - default is 0 (no shield strength change)
# --- "percCurrLauncherShieldHeal", similar to "percLauncherShieldHeal", but uses the CURRENT shield strength (that is, if you had set it to 0.8, it would set the shield to 80% of the curent shield strength). Default is 1 (current shield strength, no changes)
# --- "absShuttleShieldHeal" is the shuttle's equivalent of "absLauncherShieldHeal".
# --- "percShuttleShieldHeal" is the shuttle's equivalent of "percLauncherShieldHeal".
# --- "percCurrShuttleShieldHeal" is the shuttle's equivalent of "percCurrLauncherShieldHeal"
# For "shutLauncherShields" >= -1, it can also consider another attribute, "felShutleLaunchShields", if "felShutleLaunchShields" has a value lesser than -1 it will use the same values used for "shutLauncherShields". If "felShutleLaunchShields" is >= -1 and lesser than 0, it will consider percentage thresholds. Greater values are the shield strength of the facet to evaluate. If it does not appear, it will use a value of 600.
# Also while "shutLauncherShields" is different from -3 and -2, it will check if the launched shuttle also has the "Launcher" parameters to use over the "Shuttle" ones.
"""
# How to change its behaviour:
Sample Setup:
# In scripts/Custom/ships/yourShip.py
# NOTE: replace "AMVoyager" with your abbrev
Foundation.ShipDef.AMVoyager.shutLauncherShields = -2
Foundation.ShipDef.AMVoyager.felShutleLaunchShields = -2
Foundation.ShipDef.AMVoyager.shutLauncherMultifacet = 1
Foundation.ShipDef.AMVoyager.shuttleLaunchMultifacet = 1

Foundation.ShipDef.AMVoyager.absLauncherShieldHeal = 0
Foundation.ShipDef.AMVoyager.percLauncherShieldHeal = 0
Foundation.ShipDef.AMVoyager.percCurrLauncherShieldHeal = 1

Foundation.ShipDef.AMVoyager.absShuttleShieldHeal = 0
Foundation.ShipDef.AMVoyager.percShuttleShieldHeal = 0
Foundation.ShipDef.AMVoyager.percCurrShuttleShieldHeal = 1

"""
#
#################################################################################################################
#
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "20260325",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }
#
#################################################################################################################
#

# Imports and global variables
from bcdebug import debug
import App
import Foundation
import MissionLib
#import ftb.FTB_MissionLib
import string
import traceback

# Lost_Jedi's version had these globals so, yeah, in case somebody used them on a script, so at least this script is compatible with those.
__author__      = MODINFO["Author"]
__copyright__   = ""
__license__     = MODINFO["License"]
__version__     = MODINFO["Version"]
__notes__       = MODINFO["Description"]


sFile = "LaunchShip"
sMainPath = "ftb." + str(sFile) 
sAlternatePath = "Custom.Techs." + str(sFile)

sAux = "Launcher"
sAuxMainPath = "ftb." + str(sAux) 
sAuxAlternatePath = "Custom.Techs." + str(sAux)

chosenPath = 0
isUtopiaEvent = 1 # 1 means we use App.UtopiaModule_GetNextEventType(), else we use App.Mission_GetNextEventType()

def fileExists(route1=sMainPath, route2=sAlternatePath):
	scriptToFind = None
	route = 0
	try:
		#import ftb.FTB_MissionLib # Somehow, not adding this field causes the script to not load
		scriptToFind = __import__(route1) #from ftb import LaunchShip
		route = 1
	except:
		try:
			#import ftb.FTB_MissionLib
			scriptToFind = __import__(route2)
			route = 2
		except:
			scriptToFind = None
			route = 0

	return scriptToFind, route


def verifyLaunchShipPatch(path1=sMainPath, path2=sAlternatePath):
	scriptToCheck, route = fileExists(route1=path1, route2=path2)

	updt = 0
	if scriptToCheck != None:
		try:
			version = 0
			hasPeskyEvent = hasattr(scriptToCheck, "ET_MAY_LAUNCH_SHUTTLE_AGAIN")
			hasMissionStart = hasattr(scriptToCheck, "MissionStart")
			hasLaunchAIShip = hasattr(scriptToCheck, "LaunchAIShip")

			if (hasPeskyEvent and hasMissionStart and hasLaunchAIShip):
				has_version = hasattr(scriptToCheck, "__version__")
				hasVersion = hasattr(scriptToCheck, "MODINFO") and hasattr(scriptToCheck.MODINFO, "Version")
				if (((not has_version) or scriptToCheck.__version__ < __version__) or ((not hasVersion) or scriptToCheck.MODINFO["Version"] < __version__)):
					updt = 1
		except:
			print __name__, ".verifyLaunchShipPatch ERROR:"
			traceback.print_exc()
			updt = 0

	return scriptToCheck, updt, route

def verifyLauncherPatch(path1=sAuxMainPath, path2=sAuxAlternatePath):
	scriptToCheck, route = fileExists(route1=path1, route2=path2)

	updt = 0
	if scriptToCheck != None:
		try:
			version = 0
			hasPeskyAttr = hasattr(scriptToCheck, "LaunchAIShip")

			if (hasPeskyAttr):
				has_version = hasattr(scriptToCheck, "__version__")
				hasVersion = hasattr(scriptToCheck, "MODINFO") and hasattr(scriptToCheck.MODINFO, "Version")
				if (((not has_version) or scriptToCheck.__version__ < __version__) or ((not hasVersion) or scriptToCheck.MODINFO["Version"] < __version__)):
					updt = 1
		except:
			print __name__, ".verifyLauncherPatch ERROR:"
			traceback.print_exc()
			updt = 0

	return scriptToCheck, updt, route


scriptAuxToPatch, necessaryToAuxUpdate, chosenAuxPath = verifyLauncherPatch(path1=sAuxMainPath, path2=sAuxAlternatePath)
scriptToPatch, necessaryToUpdate, chosenPath = verifyLaunchShipPatch(path1=sMainPath, path2=sAlternatePath)

if scriptToPatch and necessaryToUpdate:
	import ftb.FTB_MissionLib
	OLD_ET_MAY_LAUNCH_SHUTTLE_AGAIN = scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN
	OLDLaunchAIShip = scriptToPatch.LaunchAIShip
	OLDMissionStart = scriptToPatch.MissionStart

	if isUtopiaEvent == 1:
		scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN = App.UtopiaModule_GetNextEventType() # either this or setting it to None
	else:
		scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN = None

	def GetShipType(pShip):
		debug(__name__ + ", GetShipType")
		if pShip and pShip.GetScript():
			return string.split(pShip.GetScript(), '.')[-1]
		return None

	def shutLnchState(pShip, pShuttle=None, pOEPProperty=None):
		debug(__name__ + ", IsPlanetKiller")
		shutLaunchShields = 600
		felShutleLaunchShields = 600

		faceted = 1
		shuttleFaceted = 1 # doesn't make much sense

		absLauncherShieldHeal = 0
		percLauncherShieldHeal = 0
		percCurrLauncherShieldHeal = 1

		absShuttleShieldHeal = 0
		percShuttleShieldHeal = 0
		percCurrShuttleShieldHeal = 1

		pPoint = None
		pShutPoint = None
		if pShuttle == -1:
			shutLaunchShields = -4
			felShutleLaunchShields = -4
			faceted = -4
			shuttleFaceted = -4

			absLauncherShieldHeal = -4
			percLauncherShieldHeal = -4
			percCurrLauncherShieldHeal = -4

			absShuttleShieldHeal = -4
			percShuttleShieldHeal = -4
			percCurrShuttleShieldHeal = -4

			pPoint = -4
			pShutPoint = -4

		sShipType = GetShipType(pShip)
		if sShipType and Foundation.shipList.has_key(sShipType):
			pFoundationShip = Foundation.shipList[sShipType]
			if pFoundationShip:
				if hasattr(pFoundationShip, "shutLauncherShields"):
					shutLaunchShields = pFoundationShip.shutLauncherShields

				if hasattr(pFoundationShip, "felShutleLaunchShields"):
					felShutleLaunchShields = pFoundationShip.felShutleLaunchShields

				if hasattr(pFoundationShip, "shutLauncherMultifacet") and (pFoundationShip.shutLauncherMultifacet == 0 or pFoundationShip.shutLauncherMultifacet == 1):
					faceted = pFoundationShip.shutLauncherMultifacet

				if hasattr(pFoundationShip, "shuttleLaunchMultifacet") and (pFoundationShip.shuttleLaunchMultifacet == 0 or pFoundationShip.shuttleLaunchMultifacet == 1):
					shuttleFaceted = pFoundationShip.shuttleLaunchMultifacet

				if hasattr(pFoundationShip, "absLauncherShieldHeal"):
					absLauncherShieldHeal = pFoundationShip.absLauncherShieldHeal

				if hasattr(pFoundationShip, "percLauncherShieldHeal"):
					percLauncherShieldHeal = pFoundationShip.percLauncherShieldHeal

				if hasattr(pFoundationShip, "percCurrLauncherShieldHeal"):
					percCurrLauncherShieldHeal = pFoundationShip.percCurrLauncherShieldHeal

				if hasattr(pFoundationShip, "absShuttleShieldHeal"):
					absShuttleShieldHeal = pFoundationShip.absShuttleShieldHeal

				if hasattr(pFoundationShip, "percShuttleShieldHeal"):
					percShuttleShieldHeal = pFoundationShip.percShuttleShieldHeal

				if hasattr(pFoundationShip, "percCurrShuttleShieldHeal"):
					percCurrShuttleShieldHeal = pFoundationShip.percCurrShuttleShieldHeal

		if pShuttle != None and pShuttle != -1 and shutLaunchShields != -3 and shutLaunchShields != -2:
			shieldStatus, shuSt, facetedShield, shuFac, sttHeal, shuHeal, sttPercHeal, shuPercHeal, sttCurrPercHeal, shuCurrPercHeal, sttpPoint, shuPoint = shutLnchState(pShuttle, -1, pOEPProperty)
			if shieldStatus != -4:
				felShutleLaunchShields = shieldStatus

			if facetedShield != -4:
				shuttleFaceted = facetedShield

			if sttHeal != -4:
				absShuttleShieldHeal = sttHeal

			if sttPercHeal != -4:
				healShuttle = sttPercHeal

			if sttCurrPercHeal != -4:
				percShuttleShieldHeal = sttCurrPercHeal

			if sttpPoint != -4:
				percCurrShuttleShieldHeal = sttpPoint


		if pOEPProperty and pShuttle != -1:
			if faceted == 0:
				pPoint = pOEPProperty #.GetPosition()

			if shuttleFaceted == 0:
				pShutPoint = App.TGPoint3()
				pShutPoint.SetXYZ(0.000000, 0.000000, 0.000000)

		return shutLaunchShields, felShutleLaunchShields, faceted, shuttleFaceted, absLauncherShieldHeal, absShuttleShieldHeal, percLauncherShieldHeal, percShuttleShieldHeal, percCurrLauncherShieldHeal, percCurrShuttleShieldHeal, pPoint, pShutPoint


	def shieldsAreLesserThan(pShip, absThreshold, shieldThreshold=-1, multifacet = 1, damageSuffered = 0, multFactor = 0, multCurrFactor = 1, kPoint=None, shieldDirNearest = None):
		debug(__name__ + ", shieldsAreLesserThan")
		pShields = pShip.GetShields()
		shieldHitBroken = 0
		if pShields and not (pShields.IsDisabled() or not pShields.IsOn() or pShields.GetPowerPercentageWanted() <= 0.0):
			if multifacet == 0 and kPoint != None and shieldDirNearest == None:
				# get the nearest reference
				pReferenciado = None
				dMasCercano = 0
				pointForward = App.TGPoint3_GetModelForward()
				pointBackward = App.TGPoint3_GetModelBackward()
				pointTop = App.TGPoint3_GetModelUp()
				pointBottom = App.TGPoint3_GetModelDown()
				pointRight = App.TGPoint3_GetModelRight()
				pointLeft = App.TGPoint3_GetModelLeft()
				lReferencias = [pointForward, pointBackward, pointTop, pointBottom, pointLeft, pointRight]

				for pPunto in lReferencias:
					pPunto.Subtract(kPoint)
					if pReferenciado == None or pPunto.Length() < dMasCercano:
						dMasCercano = pPunto.Length()
						pReferenciado = pPunto

				
				if pReferenciado:
					shieldDirNearest = lReferencias.index(pReferenciado)
				else:
					shieldHitBroken = shieldHitBroken + 1

			if not shieldHitBroken:
				for shieldDir in range(App.ShieldClass.NUM_SHIELDS):
					if shieldDir == shieldDirNearest or multifacet != 0:
						fCurr = pShields.GetCurShields(shieldDir)
						fMax = pShields.GetMaxShields(shieldDir)
						if damageSuffered != 0.0 or multFactor != 0.0 or multCurrFactor != 1:
							resultHeal = (((fCurr + damageSuffered) * multCurrFactor) + (fMax * multFactor))
							if resultHeal < 0.0:
								resultHeal = 0.0
							elif resultHeal > fMax:
								resultHeal = fMax
							pShields.SetCurShields(shieldDir, resultHeal)
							fCurr = resultHeal
	
						if (fCurr <= 0.0 or fCurr <= absThreshold or fCurr < (shieldThreshold * fMax)):
							shieldHitBroken = 1
							break;
		else:
			shieldHitBroken = 1

		return shieldHitBroken


	def NewLaunchAIShip(pLaunchingShip, pOEPProperty, pLaunchSystem, sShipClass, iLaunchInterval, aiScriptName, commandable=None, bTimer=None, side="Friendly", sShipName=None, ForceDirectAI=0):
		debug(__name__ + ", LaunchAIShip")
		#global scriptToPatch.ShuttleCounter
		pPlayer = MissionLib.GetPlayer()
	
		scriptToPatch.ShuttleCounter = scriptToPatch.ShuttleCounter + 1
		#sShipName = "Ship " + str(scriptToPatch.ShuttleCounter)
		# Change by Occas
		if sShipName == None:
			sShipName = sShipClass + " - " + str(scriptToPatch.ShuttleCounter)
		while(MissionLib.GetShip(sShipName)):
			scriptToPatch.ShuttleCounter = scriptToPatch.ShuttleCounter + 1
			sShipName = sShipClass + " - " + str(scriptToPatch.ShuttleCounter)

		if scriptToPatch.LaunchShipByClass(pLaunchingShip, pOEPProperty, pLaunchSystem, sShipClass, sShipName) == -1:
			return -1
		pSet = pLaunchingShip.GetContainingSet()
		pLaunchedShip = App.ShipClass_GetObject(pSet, sShipName)
		if not pLaunchedShip:
			print("Unknown Shuttle Launching Error (LaunchShip.py): Ship was not created")
			return -1

		# flicker shields
		pShields = pLaunchingShip.GetShields()
		if pShields and pShields.IsOn():
			shieldStatus, shuttlePlans, facetedShield, shuttleFaceted, absLauncherShieldHeal, absShuttleShieldHeal, percLauncherShieldHeal, percShuttleShieldHeal, percCurrLauncherShieldHeal, percCurrShuttleShieldHeal, pPoint, pShutPoint = shutLnchState(pLaunchingShip, pLaunchedShip, pOEPProperty)
			doIt = 0
			if shieldStatus != -3:
				if shieldStatus != -2: # Conditional - do both of them have shields?
					percThres = -1
					absThres = -1

					percShutThres = -1
					absShutThres = -1

					pPoint = None
					if shieldStatus < 0:
						percThres = abs(shieldStatus)
					else:
						absThres = abs(shieldStatus)

					if shuttlePlans < -1:
						percShutThres = percThres
						absShutThres = absThres
					elif shuttlePlans < 0:
						percShutThres = abs(shieldStatus)
					else:
						absShutThres = abs(shieldStatus)
					
					launchinShieldBroken = shieldsAreLesserThan(pLaunchingShip, absThres, shieldThreshold=percThres, multifacet = facetedShield, damageSuffered = absLauncherShieldHeal, multFactor = absShuttleShieldHeal, multCurrFactor = percCurrLauncherShieldHeal, kPoint=pPoint, shieldDirNearest = None)
					launchedShieldBroken = shieldsAreLesserThan(pLaunchedShip, absShutThres, shieldThreshold=percShutThres, multifacet = shuttleFaceted, damageSuffered = absShuttleShieldHeal, multFactor = percShuttleShieldHeal, multCurrFactor = percCurrShuttleShieldHeal, kPoint=pShutPoint, shieldDirNearest = None)

					if launchinShieldBroken == 0: # We have good shields
						if launchedShieldBroken > 0: # Breached launched shields
							doIt = 1
						else:
							doIt = 0
					else:
						doIt = 0	
				else:
					doIt = 0
			else:
				doIt = 1
					
			if doIt:
				pShields.TurnOff()
				pSequence = App.TGSequence_Create()
				pSequence.AppendAction(App.TGScriptAction_Create("ftb.FTB_MissionLib", "TurnShieldsOn", pLaunchingShip.GetName()), 3)
				pSequence.Play()

		if side == "Friendly":
			ftb.FTB_MissionLib.AddObjectToFriendlyGroup(sShipName)
			if aiScriptName == "ftb.enemyAI":
				aiScriptName = "ftb.friendlyAI"
		elif side == "Neutral":
			ftb.FTB_MissionLib.AddObjectToNeutralGroup(sShipName)
		elif side == "Enemy":
			ftb.FTB_MissionLib.AddObjectToEnemyGroup(sShipName)
			if aiScriptName == "ftb.friendlyAI":
				aiScriptName = "ftb.enemyAI"
		if bTimer:
			scriptToPatch.StartLaunchIntervalTimer(pLaunchSystem, iLaunchInterval) 
		if commandable:
			MissionLib.AddCommandableShip(sShipName)
	
		if scriptToPatch.GetOnBoard and pPlayer.GetObjID() == pLaunchingShip.GetObjID():
			debug(__name__ + ", LaunchAIShip SetTarget")
			pPlayer.SetTarget(pLaunchingShip.GetName())
		else:
			pHull = pLaunchingShip.GetHull()
			pLauncherShipName = pLaunchingShip.GetName()
			pRadius = pHull.GetRadius()
			# set AI
			if not (scriptToPatch.GetOnBoard and pPlayer.GetObjID() == pLaunchingShip.GetObjID()):
				if ForceDirectAI == 0:
					pDoneAI = aiScriptName
					pTempAI = __import__ ("ftb.PassThroughAI")
					pAI = pTempAI.CreateAI(pLaunchedShip, pDoneAI, pRadius, pLauncherShipName)
					pLaunchingShip.SetAI(pAI)
				else:
					try:
						aiModule = __import__(aiScriptName)
						pLaunchingShip.SetAI(aiModule.CreateAI(pLaunchedShip))
					except ValueError:
						print "Error Loading", aiScriptName
		return 0

	scriptToPatch.LaunchAIShip = NewLaunchAIShip

	def NewMissionStart():
		#### REGISTER EVENT HANDLERS
		debug(__name__ + ", MissionStart")
		#global scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN
		noPrecedentEvents = 0
		if scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN == None:
			noPrecedentEvents = 1
			if isUtopiaEvent == 1:
				scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN = App.UtopiaModule_GetNextEventType()
			else:
				scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN = App.Mission_GetNextEventType()
		try:
			if noPrecedentEvents != 1 and isUtopiaEvent != 1:
				App.g_kEventManager.RemoveBroadcastHandler( scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN, App.Game_GetCurrentGame(), "ftb.LaunchShipHandlers.MayLaunchShuttleAgain")
				scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN = App.Mission_GetNextEventType()

			App.g_kEventManager.RemoveBroadcastHandler( scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN, App.Game_GetCurrentGame(), "ftb.LaunchShipHandlers.MayLaunchShuttleAgain")
		except:
			print __name__, ".NewMissionStart ERROR:"
			traceback.print_exc()

		App.g_kEventManager.AddBroadcastPythonFuncHandler( scriptToPatch.ET_MAY_LAUNCH_SHUTTLE_AGAIN, App.Game_GetCurrentGame(), "ftb.LaunchShipHandlers.MayLaunchShuttleAgain")

	scriptToPatch.MissionStart = NewMissionStart

	if scriptAuxToPatch and necessaryToAuxUpdate and chosenAuxPath: # Just in case, because they have looping dependencies
		scriptAuxToPatch.LaunchAIShip = scriptToPatch.LaunchAIShip

	print __name__, " tweaked Shuttle Launch Framework LaunchShip conditions."
		
