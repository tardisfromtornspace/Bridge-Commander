# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 13th April 2025, by Alex SL Gato (CharaToLoki), based on BorgAdaptation.py (which was partially based on the Shield.py script by the Foundation Technologies team and Dasher42's Foundation script, and the FedAblativeArmor.py found in scripts/ftb/Tech in KM 2011.10) and inspired by SG1EMPulse.py, by wowsher.
##############################################################
# This tech takes part on the gimmicks from the Traveller from Sigma 957 - that is, when they scan you, you temporarily lose power. You can add your ship to an adaptable immunity list in order to keep the files unaltered...
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev - note the TO-DO UPDATE README
# * "% energy dmg": As a relative value on the 0-1 range, how much extra damage it deals on energy systems. That is, 0.15 would disable the system and then deal 15% extra damage.
# * "% energy drain": As a relative value on the 0-1 range, how much energy from the scanned ship's batteries this removes. That is, 0.15 would remove 15% power.
# * "raw energy drain": As a raw value, how much energy is drained from the scanned ship's batteries this removes. That is, 0.15 would remove 0.15 energy. Accepts negative values.
# If neither of the above are added, scanning will deal no effect. Now, the ones below indicate resistances when your own ship is scanned.
# * "% energy dmg resistance": A multiplier of the "% energy dmg" when self is scanned. That is, 0.15 would reduce the energy damage by 85%, 0 would make you immune to this effect and 2 would make you receive twice the damage.
# * "% energy drain resistance": A multiplier of the "% energy drain" when self is scanned. That is, 0.15 would reduce the energy drain by 85%, 0 would make you immune to this effect and 2 would make you receive twice the drain.
# * "raw energy drain resistance": A multiplier of the "raw energy drain" when self is scanned. That is, 0.15 would reduce the energy drain by 85%, 0 would make you immune to this effect and 2 would make you receive twice the drain.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Sigma 957 Walkers Molecular Scan": {
		"% energy dmg": 0.15,
		"% energy drain": 0.4,
		"raw energy drain": 5000,
		"% energy dmg resistance": 0,
		"% energy drain resistance": 0,
		"raw energy drain resistance": 0,
		
	}
}
"""

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.1",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

import App

import Foundation
import FoundationTech
import MissionLib
import Custom.NanoFXv2.NanoFX_Lib

import nt
import math
import string

from bcdebug import debug
import traceback

#TO-DO REMOVE DRIED LAVA
defaultXDmg = 0.15 
defaultAbsEnergyDrain = 0 # As a raw value, how much energy is drained on the surrounding ships from the scan.
defaultRelEnergyDrain = 0 # As a relative value on the 0-1 range, how much energy is drained on the surrounding ships from the scan.
scanTargetMultiplierBoost = 2 # How are ALL effects boosted if the ship is scanning a target and not just the area.

scanAreaRange = 50 # Range in km where the scan will be effective
ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer

myVisuals = "scripts/Custom/Babylon5/effects/"

def GetWellShipFromID(pShipID):
	pShip = App.ShipClass_GetObjectByID(App.SetClass_GetNull(), pShipID)
	if not pShip or pShip.IsDead() or pShip.IsDying():
		return None
	return pShip
	
def findShipInstance(pShip):
	debug(__name__ + ", findShipInstance")
	pInstance = None
	try:
		if not pShip:
			return pInstance
		if FoundationTech.dShips.has_key(pShip.GetName()):
			pInstance = FoundationTech.dShips[pShip.GetName()]
	except:
		pass
	return pInstance

def NiPoint3ToTGPoint3(p): # based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

def LoadGfx(iNumXFrames, iNumYFrames, leDirectory):
	fFiles = Foundation.GetFileNames(leDirectory, 'tga')       
	for aFile in fFiles:
		try:
			strFile = leDirectory + str(aFile)
			fX = 0.0
			fY = 0.0
			pContainer = App.g_kTextureAnimManager.AddContainer(strFile)   
			pTrack = pContainer.AddTextureTrack(iNumXFrames * iNumYFrames)
			for index in range(iNumXFrames * iNumYFrames):
				pTrack.SetFrame(index, fX, fY + (1.0 / iNumYFrames), fX + (1.0 / iNumXFrames), fY)
				fX = fX + (1.0 / iNumXFrames)
				if (fX == 1.0):
					fX = 0.0
					fY = fY + (1.0 / iNumYFrames)
		except:
			traceback.print_exc()

def energyDraining(batt_chg, batt_limit, draEff, rawDraEff):
	newMainBateryPwr = (batt_limit * (1 - draEff)) - rawDraEff

	if newMainBateryPwr > batt_chg:
		newMainBateryPwr = (batt_chg * (1 - draEff)) - rawDraEff

	if newMainBateryPwr <= 0.0:
		newMainBateryPwr = 0
	elif newMainBateryPwr > batt_limit:
		newMainBateryPwr = batt_limit

	return newMainBateryPwr

# Based on Effects.py
def CreateGFX(pShipID, sFile, fSize = 112, fSpeed = 1.0, fLifeTime = 1, fRed = 255.0, fGreen = 255.0, fBlue = 255.0, fBrightness = 0.8):
	pShip = GetWellShipFromID(pShipID)
	if not pShip:
		return 0

	pAttachTo = pShip.GetNode()
	if not pAttachTo:
		return 0		

	pEmitFrom = App.TGModelUtils_CastNodeToAVObject(pShip.GetNode())
	if not pEmitFrom:
		return 0

	pEffect = App.AnimTSParticleController_Create()
	pEffect.AddColorKey(0.0, fRed / 255, fGreen / 255, fBlue / 255)
	pEffect.AddColorKey(1.0, fRed / 255, fGreen / 255, fBlue / 255)
	pEffect.AddAlphaKey(0.0, 1.0)
	pEffect.AddAlphaKey(1.0, 1.0)
	pEffect.AddSizeKey(0.0, fSize)
	pEffect.AddSizeKey(1.0, fSize)
	pEffect.SetEmitLife(fSpeed)
	pEffect.SetEmitFrequency(1)
	pEffect.SetEffectLifeTime(fSpeed + fLifeTime)
	pEffect.SetInheritsVelocity(0)
	pEffect.SetDetachEmitObject(0)
	pEffect.CreateTarget(sFile)
	pEffect.SetTargetAlphaBlendModes(0, 7)
	pEffect.SetEmitFromObject(pEmitFrom)
	pEffect.AttachEffect(pAttachTo)               
	anEffect = App.EffectAction_Create(pEffect)
	if anEffect:
		pSequence = App.TGSequence_Create()   
		pSequence.AddAction(anEffect)
		pSequence.Play()

	return 0

def SafeAction(pAction, pShipID, pAnotherAction):
	if pAnotherAction == None:
		return 1
	pShip = GetShipFromID(pShipID)
	if not pShip:
		return 1
	try:
		pSeq = App.TGSequence_Create()
		pSeq.AddAction(pAnotherAction, App.TGAction_CreateNull(), 0.0)
		pSeq.Play()
	except:	
		traceback.print_exc()
			
	return 0

def PlaySound(pAction, pShipID, sound="scripts/Custom/Babylon5/effects/systems_shut_down.mp3", soundName = "SigScanEnabled"):
	pScanner = GetWellShipFromID(pShipID)
	if not pScanner:
		return 1
	try:
		pSound = App.TGSound_Create(sound, sound, 0)
		if pSound:
			pSound.Play()	
	except:
		traceback.print_exc()
	return 0

def AOEffects(pAction, pEvent, pShipID, iScanType, myXDmg, myAbsEnergyDrain, myRelEnergyDrain):
	pScanner = GetWellShipFromID(pShipID)
	if not pScanner:
		return 1
	try:
		CreateGFX(pShipID, myVisuals + "Nova_Sphere3a.tga")
	except:
		traceback.print_exc()

	fcvnss = 1.0
	lshipsToAssess = []
	
	pSet = pScanner.GetContainingSet()
	if not pSet:
		return 0

	pProx = pSet.GetProximityManager()
	if not pProx:
		return 0

	global scanAreaRange, ticksPerKilometer
	kIter = pProx.GetNearObjects(pScanner.GetWorldLocation(), scanAreaRange * ticksPerKilometer, 1) 
	while 1:
		pObject = pProx.GetNextObject(kIter)
		if not pObject:
			break

		if pObject.IsTypeOf(App.CT_SHIP):
			if hasattr(pObject, "GetObjID"):
				paTargetID = pObject.GetObjID()
				paTarget = GetWellShipFromID(paTargetID)
				if paTarget and paTargetID != pShipID:
					lshipsToAssess.append(paTarget)
	
	pProx.EndObjectIteration(kIter)

	for pTarget in lshipsToAssess:
		try:
			ourEMPEffect(pScanner, pTarget, myXDmg, myAbsEnergyDrain, myRelEnergyDrain, fcvnss)
		except:
			print "Error while applying effect to targets for Sigma 957 Walkers Scan"
			traceback.print_exc()
			
	return 0

def ourEMPEffect(pShip, pTarget, myXDmg, myAbsEnergyDrain, myRelEnergyDrain, fcvnss):

	dmgMul = 1.0
	drainMul = 1.0
	rawDrainMul = 1.0
	pScannedInstance = findShipInstance(pTarget)
	if pScannedInstance:
		pScannedInstanceDict = pScannedInstance.__dict__
		if pScannedInstanceDict.has_key('Sigma 957 Walkers Molecular Scan'):
			thisTech = pScannedInstanceDict['Sigma 957 Walkers Molecular Scan']
			if thisTech.has_key("% energy dmg resistance"):
				dmgMul = thisTech["% energy dmg resistance"]
			if thisTech.has_key("% energy drain resistance"):
				drainMul = thisTech["% energy drain resistance"]
			if thisTech.has_key("raw energy drain resistance"):
				rawDrainMul = thisTech["raw energy drain resistance"]
	
	lSys = [pTarget.GetPowerSubsystem(), pTarget.GetCloakingSubsystem()]
	for pSystem in lSys:
		if pSystem:
			if myXDmg != None and dmgMul != 0.0:
				pCurrStats = pSystem.GetConditionPercentage()	
				pDisabled = pSystem.GetDisabledPercentage()
				finalStatus = 1.0
				if pDisabled < pCurrStats:
					finalStatus = pDisabled-(myXDmg*fcvnss*dmgMul)
				else:
					finalStatus = pCurrStats-(myXDmg*fcvnss*dmgMul)

				if finalStatus < 0:
					finalStatus = 0
				elif finalStatus > 1.0:
					finalStatus = 1.0 
				pSystem.SetConditionPercentage(finalStatus)
			if (pSystem.IsTypeOf(App.CT_POWER_SUBSYSTEM)) and ((myRelEnergyDrain != None and myRelEnergyDrain != 0.0) or (myAbsEnergyDrain != None and myAbsEnergyDrain != 0.0)): # If it's an energy property, we should adjust the energy values.
				pESubsystem = App.PowerSubsystem_Cast(pSystem)
				if pESubsystem:
					batt_chg = pESubsystem.GetMainBatteryPower()
					batt_limit = pESubsystem.GetMainBatteryLimit()

					batt_back_limit = pESubsystem.GetBackupBatteryLimit()
					batt_back_chg = pESubsystem.GetBackupBatteryPower()

					draEff = 0
					if myRelEnergyDrain != None:
						draEff = myRelEnergyDrain * fcvnss * drainMul

					rawDraEff = 0
					if myAbsEnergyDrain != None:
						rawDraEff = myAbsEnergyDrain * fcvnss * rawDrainMul

					newMainBateryPwr = energyDraining(batt_chg, batt_limit, draEff, rawDraEff)
					newBckBateryPwr = energyDraining(batt_back_chg, batt_back_limit, draEff, rawDraEff)

					pESubsystem.SetMainBatteryPower(newMainBateryPwr)
					pESubsystem.SetBackupBatteryPower(newMainBateryPwr)

	
	
	try:
		Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pTarget, 1.5, sStatus = "Off")
	except:
		traceback.print_exc()

	return 0


class SigmaWalkersMolecularScan(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated Reality Bomb counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SCAN, self.pEventHandler, "ScanProgress")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SCAN, self.pEventHandler, "ScanProgress")
		try:
			LoadGfx(8, 4, myVisuals)
		except:
			traceback.print_exc()
					
	def ScanProgress(self, pEvent):
		debug(__name__ + ", ScanProgress")
		try:
			pPlayer = MissionLib.GetPlayer()

			pScanner = pEvent.GetDestination()
			if pScanner == None or not pScanner.IsTypeOf(App.CT_SHIP):
				pScanner = pPlayer

			if pScanner == None:
				return 0

			pShipID = None
			if hasattr(pScanner, "GetObjID"):
				pShipID = pScanner.GetObjID()
			else:
				return 0

			pScanner = GetWellShipFromID(pShipID)
			if pScanner == None:
				return 0

			pScannerInstance = findShipInstance(pScanner)
			if pScannerInstance == None or not pScannerInstance.__dict__.has_key('Sigma 957 Walkers Molecular Scan'):
				return 0
			
			thisTech = pScannerInstance.__dict__['Sigma 957 Walkers Molecular Scan']
			myXDmg = None
			myAbsEnergyDrain = None
			myRelEnergyDrain = None

			if thisTech.has_key("% energy dmg"):
				myXDmg = thisTech["% energy dmg"]

			if thisTech.has_key("% energy drain"):
				myRelEnergyDrain = thisTech["% energy drain"]

			if thisTech.has_key("raw energy drain"):
				myAbsEnergyDrain = thisTech["raw energy drain"]

			iScanType = pEvent.GetInt()
			self.ExplodingSequence(pShipID, pEvent, iScanType, myXDmg, myAbsEnergyDrain, myRelEnergyDrain)

			return 0
		except:
			print "Error when handling Sigma 957 Walkers Scan"
			traceback.print_exc()
		return 0

	def ExplodingSequence(self, pShipID, pEvent, iScanType, myXDmg, myAbsEnergyDrain, myRelEnergyDrain):

		pShip = GetWellShipFromID(pShipID)
		if pShip == None:
			return 0

		pSequence = App.TGSequence_Create()
		pSoundAction1 = App.TGScriptAction_Create(__name__, "PlaySound", pShipID, "scripts/Custom/Babylon5/effects/systems_shut_down.mp3", "SigScanEnabled")
		pSequence.AddAction(pSoundAction1, App.TGAction_CreateNull(), 0.0)
		pFlickAction1 = App.TGScriptAction_Create(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5, sStatus = "Off"))
		if pFlickAction1:
			pSafeAction1 = App.TGScriptAction_Create(__name__, "SafeAction", pShipID, pFlickAction1)
			pSequence.AddAction(pSafeAction1, App.TGAction_CreateNull(), 1.0)
		pSoundAction2 = App.TGScriptAction_Create(__name__, "PlaySound", pShipID, "scripts/Custom/Babylon5/effects/em_pulse_short.mp3", "SigScanPulse")
		pSequence.AddAction(pSoundAction2, App.TGAction_CreateNull(), 5.0)
		pFlickAction2 = App.TGScriptAction_Create(Custom.NanoFXv2.NanoFX_Lib.CreateFlickerSeq(pShip, 1.5, sStatus = "On"))
		if pFlickAction2:
			pSafeAction1 = App.TGScriptAction_Create(__name__, "SafeAction", pShipID, pFlickAction2)
			pSequence.AddAction(pSafeAction2, App.TGAction_CreateNull(), 7.5)

		pFinalAction = App.TGScriptAction_Create(__name__, "AOEffects", pEvent, pShipID, iScanType, myXDmg, myAbsEnergyDrain, myRelEnergyDrain)
		pSequence.AddAction(pFinalAction, App.TGAction_CreateNull(), 7.5)
		pSequence.Play()

		return 0

oSigmaWalkersScan = SigmaWalkersMolecularScan("Sigma 957 Walkers Molecular Scan") # TO-DO UPDATE, ALSO REMOVE DRIED LAVA