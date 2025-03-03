# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 20th June 2024, by Alex SL Gato (CharaToLoki), partially based on the Shield.py script by the Foundation Technologies team and Dasher42's Foundation script, and the FedAblativeArmor.py found in scripts/ftb/Tech in KM 2011.10
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech takes part on the defensive (and, from 0.9, OFFENSIVE and from 1.0, Scan) Borg adaptation. You can add your ship to an adaptable immunity list in order to keep the files unaltered...
# just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev - note the number indicates how fast it learns, make it 0 so it never helps into learning and negative values so it instead makes it more difficult for others to adapt :P
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Borg Adaptation": 1
}
"""

# If you want an specific yield or weapon to last more or less against adaptable Borg, then you need to add a file under the scripts\Custom\Techs\BorgAdaptationsDefensive directory; called with the name of the Yield,
# Special Technology or special specific function it may have inside (for example, if the special technology has an "IsPhaseYield" function which is a concrete way to determine it is such technology, you can call the
# file "IsPhaseYield.py"; on the other hand if you want a Tactical.Projectiles.PhotonTorpedo85 resist more or less, you would name the file "PhotonTorpedo85")
# Below there's an example used for the 8472Beam - note that for torpedoes and Disruptors it uses the filename, but for phasers it uses the sound name!
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 15 June 2023, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used along with the BorgAdaptation Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/BorgAdaptationsDefensive
def defenseCounterRdm(): # Establishes a random factor - values must be >= 0. The greater the value, the more range can happen between sessions.
	return 65000
def defenseCounter(): # Establishes the minimum number of strikes before it adapts, stacking along the random value above - please notice some weapons deal multi-strikes. Values must be >= 0
	return 195000
"""


# You can also add a ship's class resistance to the offensive side, in any of two ways:
# ***WAY 1***: thrugh a scripts\Custom\Techs\BorgAdaptationsDefensive file - this way is made for backwards compatibility without needing to update a bazillion ship mods; but will override way 2. 
# ALSO WAY 2 IS PREFERRED FOR FUTURE MODS, Because there may be a chance that a weapon and a ship share same name, and in that case, while you can perfectly fuse both files in 1, it is far dirtier.
# Note that on this case you must use the scripts/Ships "Name" value.
# On this case, the value given will make it harder for the Borg to adapt their weapons to be effective, while a smaller or negative value will make it faster.
# The example below is an extreme case used for the KM CA8472 bioship
"""
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 15 June 2023, by Alex SL Gato (CharaToLoki)
# Version: 1.0
# Meant to be used along with the BorgAdaptation Technology (located at scripts/Custom/Techs), this file must be under scripts/Custom/Techs/BorgAdaptationsDefensive
def defenseShipCounterRdm(): # Establishes a random factor - values must be >= 0. The greater the value, the more range can happen between sessions.
	return 1000
def defenseShipCounter(): # Establishes the minimum number of strikes before it adapts, stacking along the random value above - please notice some weapons deal multi-strikes. Values must be >= 0
	return 12000

"""
# ***WAY 2***: regular Foundation Technology call, like with "Borg Adaptation". On this case, the value given will make it harder for the Borg to adapt their weapons to be effective, while a smaller or negative value will make it faster.
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Borg Attack Resistance": 1
}
"""


MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "1.34",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

import App

import Foundation
import FoundationTech
import MissionLib

import nt
import math
import string

from bcdebug import debug
import traceback

maxCountdown = 65535 # we want to keep things moderate
maxCountdownModifier = 64 # for normal yields, allows a higher cap of max
yieldAdaptationCounter = 800.0 # default point before the Borg manage to prevent the special yield of a weapon
nonYieldAdaptationCounter = 100.0 # the point before the Borg manage to prevent 50% of the non-yield weapons damage
extraReductionAdaptationCycle = 8 # this is how many extra steps are taken after nonYieldAdaptationCounter has been reached - the first initial ones make a huge drop
yieldAttackAdaptationCounter = 1000.0 # default point before the Borg reach maximum weapon Damage output
extraDamage = 4.0 # How much damage is given when reaching max offensive peak, equivalent to original damage * (1 + extraDamage)

scanTargetMultiplierBoost = 100 # When an adaptive Borg vessel scans a target specifically, it gets info 100 times faster (basically it's as if it hit once with 100 times more learning power. Normal learning is unaffected)
scanAreaMultiplierBoost = 10 # When an adaptive Borg vessel scans a target specifically, it gets info 10 times faster (basically it's as if it hit once with 10 times more learning power. Normal learning is unaffected)
scanAreaRange = 50 # Range in km where the scan will be effective
ticksPerKilometer = 225/40 # 225 is approximately 40 km, so 225/40 is the number of ticks per kilometer

# THIS IS A GLOBAL LIST, WHICH WILL BE FILLED AUTOMATICALLY OR BY THE FILES IN scripts/Custom/Techs/BorgAdaptationsDefensive
adaptationProgress = {

}

normalWeaponAdaptation = {

}


impactingShipTypeDict = {

}

_g_dExcludeBorgPlugins = {
	# Some random plugins that I don't want to risk people attempting to load using this tech
	"000-Fixes20030217": 1,
	"000-Fixes20030221": 1,
	"000-Fixes20030305-FoundationTriggers": 1,
	"000-Fixes20030402-FoundationRedirect": 1,
	"000-Fixes20040627-ShipSubListV3Foundation": 1,
	"000-Fixes20040715": 1,
	"000-Fixes20230424-ShipSubListV4_7Foundation": 1,
	"000-Utilities-Debug-20040328": 1,
	"000-Utilities-FoundationMusic-20030410": 1,
	"000-Utilities-GetFileNames-20030402": 1,
	"000-Utilities-GetFolderNames-20040326": 1,
}

# based on the FedAblativeArmour.py script, a fragment probably imported from ATP Functions by Apollo
def NiPoint3ToTGPoint3(p):
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

# Based on LoadExtraPlugins by Dasher42, but heavily modified so it only imports a thing
def LoadExtraLimitedPlugins(dExcludePlugins=_g_dExcludeBorgPlugins):

	dir="scripts\\Custom\\Techs\\BorgAdaptationsDefensive" # I want to limit any vulnerability as much as I can while keeping functionality
	import string

	list = nt.listdir(dir)
	list.sort()

	dotPrefix = string.join(string.split(dir, "\\")[1:], ".") + "."

	for plugin in list:
		s = string.split(plugin, ".")
		if len(s) <= 1:
			continue
		
		# Indexing by -1 lets us be sure we're grabbing the extension. -Dasher42
		extension = s[-1]
		fileName = string.join(s[:-1], ".")

		# We don't want to accidentally load wrong things
		if (extension == "py") and not fileName == "__init__": # I am not allowing people to just use the .pyc directly, I don't want people to not include source scripts - Alex SL Gato
			#print "Borg are reviewing " + fileName + " of dir " + dir
			if dExcludePlugins.has_key(fileName):
				debug(__name__ + ": Ignoring outdated plugin" + fileName)
				continue

			try:
				if not adaptationProgress.has_key(fileName):
					myGoodPlugin = dotPrefix + fileName
					
					# I really wanted to make it so it only imports these two methods, but it is not letting me do it :(
					# The only other secure option I could think about is making random files with the name and those two values in the name and then splitting them up, but if there's an update you would end up with rubbish as well
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounterRdm"])
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounter"])

					try:
						banana = __import__(myGoodPlugin, globals(), locals(), ["defenseCounterRdm", "defenseShipCounterRdm"])
					except:
						try:
							banana = __import__(myGoodPlugin, globals(), locals(), ["defenseCounterRdm"])
						except:
							banana = __import__(myGoodPlugin, globals(), locals(), ["defenseShipCounterRdm"])
					#banana = __import__(myGoodPlugin, globals(), locals())

					if hasattr(banana, "defenseCounter"):
						randomness = 0
						if hasattr(banana, "defenseCounterRdm"):
							randomness = abs(banana.defenseCounterRdm())
						constantness = abs(banana.defenseCounter())
						trueRandomness = 0
						if randomness > 0:
							trueRandomness = App.g_kSystemWrapper.GetRandomNumber(randomness)
						#print constantness
						#print randomness
						#print trueRandomness
					
						# This standard is to call the file as "IsXXXXYield", with XXXX being the tech, that is "IsDrainYield", "IsPhasedYield", etc. Or call it like the Yield name (f.ex. "Hopping Torpedo")
						adaptationProgress[fileName] =  trueRandomness + constantness
						normalWeaponAdaptation[fileName] =  -(trueRandomness + constantness)

					if hasattr(banana, "defenseShipCounter"):
						randomness = 0
						if hasattr(banana, "defenseShipCounterRdm"):
							randomness = banana.defenseShipCounterRdm()
						constantness = banana.defenseShipCounter()
						trueRandomness = 0
						if randomness > 0:
							trueRandomness = App.g_kSystemWrapper.GetRandomNumber(randomness)
						impactingShipTypeDict[fileName] =  -(trueRandomness + constantness)

					
					#print "Borg reviewing of this tech is a success, adapting at the following number of shots: " + str(adaptationProgress[fileName])
			except:
				print "someone attempted to add more than they should to the Borg Adaptation script"
				traceback.print_exc()

	


LoadExtraLimitedPlugins()
#print adaptationProgress
#print impactingShipTypeDict


class BorgAdaptationDef(FoundationTech.TechDef):
	def __init__(self, name):
		debug(__name__ + ", Initiated Reality Bomb counter")
		FoundationTech.TechDef.__init__(self, name)
		self.pEventHandler = App.TGPythonInstanceWrapper()
		self.pEventHandler.SetPyWrapper(self)
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")
		App.g_kEventManager.RemoveBroadcastHandler(App.ET_SCAN, self.pEventHandler, "ScanProgress")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_WEAPON_HIT, self.pEventHandler, "OneWeaponHit")
		App.g_kEventManager.AddBroadcastPythonMethodHandler(App.ET_SCAN, self.pEventHandler, "ScanProgress")

	def OnDefense(self, pShip, pInstance, oYield, pEvent, itemName):
		global normalWeaponAdaptation, yieldAdaptationCounter, nonYieldAdaptationCounter, extraReductionAdaptationCycle
		# let's make it so people can customize how fast can a borg ship adapt, within reason
		learningFactor = pInstance.__dict__['Borg Adaptation']
		if learningFactor > maxCountdown:
			learningFactor = maxCountdown
		elif learningFactor < -maxCountdown:
			learningFactor = -maxCountdown

		borgAdapted = 0
		if oYield:
			try:
				for attre in adaptationProgress.keys():
					sameYield = 0
					if not FoundationTech.oTechs.has_key(attre):
						sameYield = (0 == 1) # For some reason it doesn't recognize False like that :/
					else:
						sameYield = (oYield == FoundationTech.oTechs[attre])

					if (hasattr(oYield, str(attre)) and getattr(oYield, str(attre))()) or sameYield:
						if not adaptationProgress.has_key(attre):
							adaptationProgress[attre] = yieldAdaptationCounter
						if adaptationProgress[attre] <= 0:
							adaptationProgress[attre] = -1
							#print "OH NO, THE BORG ADAPTED TO THIS WEAPON's SPECIAL YIELD"
							borgAdapted = 1
						elif adaptationProgress[attre] > maxCountdown:
							adaptationProgress[attre] = maxCountdown

						adaptationProgress[attre] = adaptationProgress[attre] - learningFactor

				if not (itemName == "None whatsoever") and not adaptationProgress.has_key(oYield):
					adaptationProgress[oYield] = yieldAdaptationCounter
			except:
				print "something went wrong with Borg Adaptation technology (special Yields)"
				traceback.print_exc()
		
	
		try:
			if not (itemName == "None whatsoever"):
				if not normalWeaponAdaptation.has_key(itemName):
					normalWeaponAdaptation[itemName] = 0

				#print normalWeaponAdaptation
				#print normalWeaponAdaptation[itemName]

				#fRadius = pEvent.GetRadius()
				#fDamage = abs(pEvent.GetDamage())
				#kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

				fRadius, fDamage, kPoint = self.EventInformation(pEvent)
				fDamage = abs(fDamage)

				if pEvent.IsHullHit():
					# get the systems
					lAffectedSystems, lNonTargetableAffeSys = self.FindAllAffectedSystems(pShip, kPoint, fRadius)

					#print lAffectedSystems
					#print lNonTargetableAffeSys
					normalWeaponAdaptation[itemName] = self.NormalLearningCalculation(itemName, normalWeaponAdaptation[itemName], learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle)

					# calculate the damage per radius
					fOffSet = 1 + fRadius
					fAllocatedFactor = fOffSet
					if fAllocatedFactor < 1:
						fAllocatedFactor = 1
					
					damageHealed = self.DamageCalculation(itemName, nonYieldAdaptationCounter, normalWeaponAdaptation, fDamage)
					# print "Event radius: " + str(fRadius)

					self.AdjustListedSubsystems(pShip, lAffectedSystems, lNonTargetableAffeSys, damageHealed, fAllocatedFactor, 0)
				else:
					theDmg = self.DamageCalculation(itemName, nonYieldAdaptationCounter, normalWeaponAdaptation, fDamage)
					self.shieldRecalculation(pShip, kPoint, theDmg, 0.35)

					normalWeaponAdaptation[itemName] = self.NormalLearningCalculation(itemName, normalWeaponAdaptation[itemName], learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle)
						
		except:
			print "something went wrong with Borg Adaptation technology (regular Yields)"
			traceback.print_exc()

		if borgAdapted:
			return 1

	def DamageCalculation(self, itemName, nonYieldAdaptationCounter, normalWeaponAdaptation, fDamage): # Defensive calculation
		damageControl = normalWeaponAdaptation[itemName]
		if damageControl < -10:
			damageControl = -10
		countDamage1 = ((nonYieldAdaptationCounter - damageControl) / nonYieldAdaptationCounter)
		if countDamage1 > 0:
			countDamage2 = countDamage1 ** (1.0/3.0)
		elif countDamage1 < 0:
			countDamage2 = -((-countDamage1) ** (1.0/3.0))
		else: # In case your python doesn't support this or makes it work differently
			countDamage2 = 0
		damageMultiplier = (countDamage2  + 1.0) * 0.5
		if nonYieldAdaptationCounter < normalWeaponAdaptation[itemName]:
			damageMultiplier = damageMultiplier - 0.01

		damageHealed = (fDamage * ( 1 - damageMultiplier))

		#print "dmg multiplier for " + str(itemName) + " stage " + str(normalWeaponAdaptation[itemName]) + " with " + str(countDamage1) + " and " + str(countDamage2) + ": " + str(damageMultiplier)
		return damageHealed

	def NormalLearningCalculation(self, itemName, normalWeaponAdaptationI, learningFactor, nonYieldAdaptationCounterI, extraReductionAdaptationCycleI):
		global maxCountdown, maxCountdownModifier
		normalWeaponAdaptationI = normalWeaponAdaptationI + learningFactor
		if normalWeaponAdaptationI < - (maxCountdownModifier * maxCountdown):
			normalWeaponAdaptationI = - (maxCountdownModifier * maxCountdown)
		elif normalWeaponAdaptationI > (nonYieldAdaptationCounterI + extraReductionAdaptationCycleI):
			#print "OH NO, THE BORG ADAPTED TO THIS WEAPON AND ITS SHIELD DAMAGE IS REDUCED"
			normalWeaponAdaptationI = nonYieldAdaptationCounterI + extraReductionAdaptationCycleI

		return normalWeaponAdaptationI

	def AreaScanFunctionLearning(self, pTarget, impactingShipTypeDicti, learningFactor, theBoost, yieldAttackAdaptationCounteri):

		itemName = findscriptsShipsField(pTarget, "Name")
					
		if itemName != None:

			if not impactingShipTypeDicti.has_key(itemName):
				pTargetInstance = findShipInstance(pTarget)
				if pTargetInstance and pTargetInstance.__dict__.has_key("Borg Attack Resistance"):
					impactingShipTypeDicti[itemName] = -pTargetInstance.__dict__["Borg Attack Resistance"]
				else:
					impactingShipTypeDicti[itemName] = 0

			#print "Before: ", impactingShipTypeDicti[itemName]
			impactingShipTypeDicti[itemName] = self.NormalLearningCalculation(itemName, impactingShipTypeDicti[itemName], abs(theBoost * learningFactor), yieldAttackAdaptationCounteri, 0)
			#print "After: ", impactingShipTypeDicti[itemName]

	def shieldRecalculation(self, pShip, kPoint, extraDamageHeal, shieldThreshold = 0.35):

		pShields = pShip.GetShields()
		shieldHitBroken = 0
		if pShields and not pShields.IsDisabled():
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
				shieldDir = lReferencias.index(pReferenciado)
				fCurr = pShields.GetCurShields(shieldDir)
				fMax = pShields.GetMaxShields(shieldDir)
				if fCurr > (shieldThreshold * fMax):
					resultHeal = fCurr + extraDamageHeal
					if resultHeal < 0.0:
						resultHeal = 0.0
					elif resultHeal > fMax:
						resultHeal = fMax
					pShields.SetCurShields(shieldDir, resultHeal)

	def AdjustListedSubsystems(self, pShip, lAffectedSystems, lNonTargetableAffeSys, damageHealed, fAllocatedFactor, hurt = 0):
		pHull=pShip.GetHull()
		notInThere = 0
		lenaffectedSys = len(lAffectedSystems)
		for pSystem in lAffectedSystems:
			if pSystem.GetName() == pHull.GetName():
				#print "It seems the hull is among targetable systems"
				notInThere = 1
			status = pSystem.GetConditionPercentage()
			# print "status" + str(status)
			if status > 0.0:
				fNewCondition = status + (damageHealed / pSystem.GetMaxCondition()) * fAllocatedFactor / lenaffectedSys
				#print "TARGETABLE " + str(status) +"-> fNewCondition = " + str(fNewCondition) + " for " + str(pSystem.GetName())
						
				if fNewCondition < 0:
					fNewCondition = 0
				elif fNewCondition > 1:
					fNewCondition = 1
				pSystem.SetConditionPercentage(fNewCondition)

		lenaffecteduntSys = len(lNonTargetableAffeSys)
		if hurt == 0:
			for pSystem in lNonTargetableAffeSys:
				iamHull = 0
				if pSystem.GetName() == pHull.GetName():
					#print "It seems the hull is among non-targetable systems, but in-range"
					notInThere = 1
					iamHull = 1
				status = pSystem.GetConditionPercentage()
				# print "status" + str(status)
				if status > 0.0:
					dividerIs = lenaffecteduntSys
					if iamHull:
						dividerIs = 1 + lenaffectedSys
					fNewCondition = status + (damageHealed / pSystem.GetMaxCondition()) * fAllocatedFactor / dividerIs
					#print "NOT TARGETABLE " + str(status) +"-> fNewCondition = " + str(fNewCondition) + "for" + str(pSystem.GetName())
							
					if fNewCondition < 0:
						fNewCondition = 0
					elif fNewCondition > 1:
						fNewCondition = 1
					pSystem.SetConditionPercentage(fNewCondition)

		if notInThere == 0: # hull hit but no targetable subsystems affected? We must guess it's the hull only, then!
			if not(pHull==None):
				#print "It seems the hull is among non-targetable systems, and not in-range"
				status = pHull.GetConditionPercentage()
				fNewCondition = status + (damageHealed / pHull.GetMaxCondition()) * fAllocatedFactor / (1 + lenaffectedSys)

				if fNewCondition < 0:
					fNewCondition = 0
				elif fNewCondition > 1.0:
					fNewCondition = 1.0
				pHull.SetConditionPercentage(fNewCondition)

		return 0

	def FindAllAffectedSystems(self, pShip, kPoint, fRadius, pEvent = None):
		lSystems = []
		
		kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		while (1):
			pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
			if not pSubsystem:
				break
			lSystems.append(pSubsystem)
					
			for i in range(pSubsystem.GetNumChildSubsystems()):
				pChild = pSubsystem.GetChildSubsystem(i)
				lSystems.append(pChild)

		pShip.EndGetSubsystemMatch(kIterator)
		# get affected systems
		lAffectedSystems = []
		lNonTargetableAffeSys = []
		if kPoint == None and pEvent != None:
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
		for pSystem in lSystems:
			vDifference = NiPoint3ToTGPoint3(pSystem.GetPosition())
			vDifference.Subtract(kPoint)
			if pSystem.GetRadius() + fRadius >= vDifference.Length():
				if pSystem.IsTargetable():
					lAffectedSystems.append(pSystem)
				else:
					lNonTargetableAffeSys.append(pSystem)

		
		#sysSubAux = [lAffectedSystems, lNonTargetableAffeSys]
		#return sysSubAux
		return lAffectedSystems, lNonTargetableAffeSys

	def EventInformation(self, pEvent):
		fRadius = pEvent.GetRadius()
		fDamage = abs(pEvent.GetDamage())
		kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

		return fRadius, fDamage, kPoint

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		try:
			pEmitter = App.PhaserBank_Cast(pEvent.GetSource())
			itemName = pEmitter.GetFireSound()
		except:
			itemName = "None whatsoever"
		return self.OnDefense(pShip, pInstance, oYield, pEvent, itemName)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		try:
			itemName = pTorp.GetModuleName()
		except:
			itemName = "None whatsoever"
		return self.OnDefense(pShip, pInstance, oYield, pEvent, itemName)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		try:
			itemName = pTorp.GetModuleName()
		except:
			itemName = "None whatsoever"
		return self.OnDefense(pShip, pInstance, oYield, pEvent, itemName)


	# TODO:  Make this an activated technology
	def Attach(self, pInstance):
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
		pInstance.lPulseDefense.insert(0, self)
		pInstance.lBeamDefense.insert(0, self)
		# print 'Attaching Borg Adaptation to', pInstance, pInstance.__dict__

	def OneWeaponHit(self, pEvent):
		debug(__name__ + ", OneWeaponHit")
		try:
			pAttacker = App.ShipClass_Cast(pEvent.GetFiringObject())
			pTarget = App.ShipClass_Cast(pEvent.GetDestination())

			if not pAttacker or not pTarget:
				return 0

			pAttackerInstance = findShipInstance(pAttacker)
			pTargetInstance = findShipInstance(pTarget)
			
			if not pAttackerInstance or not pAttackerInstance.__dict__.has_key("Borg Adaptation"):
				return 0

			itemName = findscriptsShipsField(pTarget, "Name")

			if itemName != None:
				global impactingShipTypeDict, extraDamage, yieldAttackAdaptationCounter

				learningFactor = pAttackerInstance.__dict__['Borg Adaptation']
				if learningFactor > maxCountdown:
					learningFactor = maxCountdown
				elif learningFactor < -maxCountdown:
					learningFactor = -maxCountdown
				
				if not impactingShipTypeDict.has_key(itemName):

					if pTargetInstance and pTargetInstance.__dict__.has_key("Borg Attack Resistance"):
						impactingShipTypeDict[itemName] = -pTargetInstance.__dict__["Borg Attack Resistance"]
					else:
						impactingShipTypeDict[itemName] = 0
				
				fRadius, fDamage, kPoint = self.EventInformation(pEvent)

				extraSteps = impactingShipTypeDict[itemName]/(1.0 * yieldAttackAdaptationCounter)
				if (extraSteps * extraDamage * 1.0) < -0.5:
					extraSteps = -0.5/(1.0 * extraDamage)
				
				finalAddedDamage = fDamage * ((extraDamage * extraSteps) + 0.0) # Offensive calculation
				#print "Ship type: ", pTarget, " with progress ", impactingShipTypeDict[itemName] , " and extra steps ", extraSteps , " Initial damage", fDamage, " -> Final damage ",  finalAddedDamage

				self.shieldRecalculation(pTarget, kPoint, -finalAddedDamage, 0.0)

				if pEvent.IsHullHit():
					lAffectedSystems, lNonTargetableAffeSys = self.FindAllAffectedSystems(pTarget, kPoint, fRadius)

					# calculate the damage per radius
					fOffSet = 1 + fRadius
					fAllocatedFactor = fOffSet
					if fAllocatedFactor < 1:
						fAllocatedFactor = 1

					self.AdjustListedSubsystems(pTarget, lAffectedSystems, lNonTargetableAffeSys, -finalAddedDamage, fAllocatedFactor, 1)
					
				impactingShipTypeDict[itemName] = self.NormalLearningCalculation(itemName, impactingShipTypeDict[itemName], learningFactor, yieldAttackAdaptationCounter, 0)
			
		except:
			print "	Error when handling Offensive Borg Weapon Hit"
			traceback.print_exc()
		return 0

		

	def ScanProgress(self, pEvent):
		debug(__name__ + ", ScanProgress")
		try:
			global maxCountdown
			#print "I got a scan"

			pPlayer = MissionLib.GetPlayer()

			pScanner = pEvent.GetDestination()
			if pScanner == None or not pScanner.IsTypeOf(App.CT_SHIP):
				pScanner = pPlayer

			pScannerInstance = findShipInstance(pScanner)
			if pScannerInstance == None or not pScannerInstance.__dict__.has_key('Borg Adaptation'):
				return 0
			
			learningFactor = pScannerInstance.__dict__['Borg Adaptation']
			if learningFactor > maxCountdown:
				learningFactor = maxCountdown
			elif learningFactor < -maxCountdown:
				learningFactor = -maxCountdown

			iScanType = pEvent.GetInt()
			if (iScanType == App.CharacterClass.EST_SCAN_AREA):
				#print "10 times the learning rate added for all ships closer than 80 kms" # get the trick from RealityBomb for distances

				pSet = pScanner.GetContainingSet()
				if not pSet:
					return

				pProx = pSet.GetProximityManager()
				if not pProx:
					return

				global scanAreaRange, ticksPerKilometer
				# For the sake of fairness and what was seen on-screen, the borg need to be close enough to get an area scan good for adapting, else they would just scan and adapt from the other side of the System
				# and the ProximityManager already should take care of distances, so not customizable for you
				#if not pScannerInstance.__dict__.has_key('Borg Adaptation Scan'):
				#	pScannerInstance.__dict__['Borg Adaptation Scan'] = scanAreaRange

				lshipsToAssess = []
				lprojectilesToAssess = []

				global ticksPerKilometer
				kIter = pProx.GetNearObjects(pScanner.GetWorldLocation(), scanAreaRange * ticksPerKilometer, 1) 
				while 1:
					pObject = pProx.GetNextObject(kIter)
					if not pObject:
						break

					if pObject.IsTypeOf(App.CT_SHIP):
						pkShip = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pObject.GetObjID()))
						if pkShip:
							lshipsToAssess.append(pkShip)

					elif pObject.IsTypeOf(App.CT_TORPEDO):
						# Torpedo scanning would just work like normal, with no buffs
						pTorp = App.Torpedo_Cast(App.TGObject_GetTGObjectPtr(pObject.GetObjID()))
						if pTorp:
							lprojectilesToAssess.append(pTorp)	

				pProx.EndObjectIteration(kIter)

				global extraReductionAdaptationCycle, impactingShipTypeDict, nonYieldAdaptationCounter, normalWeaponAdaptation, scanAreaMultiplierBoost, yieldAttackAdaptationCounter
				for pTarget in lshipsToAssess:
					try:
						self.AreaScanFunctionLearning(pTarget, impactingShipTypeDict, learningFactor, scanAreaMultiplierBoost, yieldAttackAdaptationCounter)
					except:
						print "Error while assesing area targets for Borg Adaptation Scan"
						traceback.print_exc()

				for pTorp in lprojectilesToAssess:
					try:
						itemName = pTorp.GetModuleName()
						if itemName != None:
							if not normalWeaponAdaptation.has_key(itemName):
								normalWeaponAdaptation[itemName] = 0
							normalWeaponAdaptation[itemName] = self.NormalLearningCalculation(itemName, normalWeaponAdaptation[itemName], learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle)
					except:
						print "Error while assesing area targets for Borg Adaptation Scan"
						traceback.print_exc()

			if (iScanType == App.CharacterClass.EST_SCAN_OBJECT):
				#print "100 times the learning rate added for this ship in particular"

				pTarget = App.ObjectClass_Cast(pEvent.GetSource())
				if not (pTarget): # Failsafe, scan target sometimes fails, while "scan object" doesn't. Weird.
					pTarget = pPlayer.GetTarget()

				if pTarget is None:
					return 0
	
				#print "Target", pTarget, "is being scanned by", pScanner

				if pTarget.IsTypeOf(App.CT_PLANET):
					#print "Planet"
					return 0
				if pTarget.IsTypeOf(App.CT_SHIP): 
					#print "A SHIP"
					global impactingShipTypeDict, yieldAttackAdaptationCounter, scanTargetMultiplierBoost

					pTarget = App.ShipClass_Cast(App.TGObject_GetTGObjectPtr(pTarget.GetObjID()))
					self.AreaScanFunctionLearning(pTarget, impactingShipTypeDict, learningFactor, scanTargetMultiplierBoost, yieldAttackAdaptationCounter)

					
				elif pTarget.IsTypeOf(App.CT_TORPEDO): # I do not know of any tech that allows to scan torpedoes, but if one ever appears, we will be ready
					# We will partially learn from the torpedo we scan, not special yields, but the damage
					#print "A TORPEDO"

					try:
						pTorp = App.Torpedo_Cast(pTarget)
						itemName = pTorp.GetModuleName()
						if itemName != None:
							if not normalWeaponAdaptation.has_key(itemName):
								normalWeaponAdaptation[itemName] = 0
							normalWeaponAdaptation[itemName] = self.NormalLearningCalculation(itemName, normalWeaponAdaptation[itemName], scanAreaMultiplierBoost*learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle)
					except:
						print "something went wrong with Borg Adaptation technology (torpedo Scan)"
						traceback.print_exc()

				else:
					print "We are scanning something different for sure..."
					return 0

		except:
			print "Error when handling Offensive Borg Scan"
			traceback.print_exc()
		return 0

def findShipInstance(pShip):
	pInstance = None
	try:
		pInstance = FoundationTech.dShips[pShip.GetName()]
		if pInstance == None:
			print "After looking, no pInstance for ship:", pShip.GetName(), "How odd..."
		
	except:
		#print "Error while looking for pInstance for Borg technology:"
		#traceback.print_exc()
		pass

		
	#finally:
	return pInstance

def findscriptsShipsField(pShip, thingToFind):
	thingFound = None
	pShipModule=__import__(pShip.GetScript())
	information = pShipModule.GetShipStats()
	if information != None and information.has_key(thingToFind):
		thingFound = information[thingToFind]
	return thingFound

oBorgAdaptation = BorgAdaptationDef('Borg Adaptation')