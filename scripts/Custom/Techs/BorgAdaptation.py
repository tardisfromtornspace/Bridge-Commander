# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 12th January 2024, by Alex SL Gato (CharaToLoki), partially based on the Shield.py script by the Foundation Technologies team and Dasher42's Foundation script, and the FedAblativeArmor.py found in scripts/ftb/Tech in KM 2011.10
#
# TODO: 1. Create Read Me
#	2. Create a clear guide on how to add this...
#
# Start on 2:
# This tech takes part on the defensive Borg adaptation. You can add your ship to an adaptable immunity list in order to keep the files unaltered... just add to your Custom/Ships/shipFileName.py this:
# NOTE: replace "Ambassador" with the abbrev - note the number indicates how fast it learns, make it 0 so it never helps into learning and negative values so it instead makes it more difficult for others to adapt :P
"""
Foundation.ShipDef.Ambassador.dTechs = {
	"Borg Adaptation": 1
}
"""
MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
	    "Version": "0.8",
	    "License": "LGPL",
	    "Description": "Read the small title above for more info"
	    }

import App

import Foundation
import FoundationTech

import nt
import math
import string

maxCountdown = 65535 # we want to keep things moderate
nonYieldAdaptationCounter = 100.0 # the point before the Borg manage to prevent 50% of the non-yield weapons damage
extraReductionAdaptationCycle = 8 # this is how many extra steps are taken after nonYieldAdaptationCounter has been reached - the first initial ones make a huge drop

# THIS IS A GLOBAL LIST, WHICH WILL BE FILLED AUTOMATICALLY OR BY THE FILES IN scripts/Custom/Techs/BorgAdaptationsDefensive
adaptationProgress = {
#"IsDrainYield" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                          # Immunity to breen drainer and similar drainers
#"Breen Damper" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                          
#"Damper Weapon" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                         
#"Breen Drainer Weapon" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,

#"IsChainReactionPulsarYield" : App.g_kSystemWrapper.GetRandomNumber(90) + 20,          # Immunity to chain reaction pulsar
#"Chain Reaction Pulsar": App.g_kSystemWrapper.GetRandomNumber(90) + 20,
#"CRP Projectile": App.g_kSystemWrapper.GetRandomNumber(90) + 20,              

#"IsChronitonYield" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                    # Immunity to Chroniton torpedoes
#"IsChronTorpYield" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,
#"Chroniton Torp" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                      
#"ChronitonTorpe" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                      
#"Chroniton Torpedo" : App.g_kSystemWrapper.GetRandomNumber(160) + 60,                   

#"IsCloakDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                  # Immunity to all cloak disablers
#"Cloak Disabler" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,
#"Cloak Disable" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                  

#"IsComputerVirusYield" : App.g_kSystemWrapper.GetRandomNumber(60) + 0,                 # Immunity to computer viruses
#"Computer Virus" : App.g_kSystemWrapper.GetRandomNumber(60) + 0,                 
#"PCVirus Weapon', " : App.g_kSystemWrapper.GetRandomNumber(60) + 0,

#"IsElectromagneticDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(5) + 0,        # Immunity against ElectroMagnetic attacks
#"Electro-Magnetic Pulse" : App.g_kSystemWrapper.GetRandomNumber(5) + 0,        
#"EMP Projectile" : App.g_kSystemWrapper.GetRandomNumber(5) + 0,

#"IsImpulseDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(11) + 0,                # Immunity to all impulse disablers
#"Impulse Disabler" : App.g_kSystemWrapper.GetRandomNumber(11) + 0,
#"Impulse Disable" : App.g_kSystemWrapper.GetRandomNumber(11) + 0,                

#"IsIonProjectileYield" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,                  # Immunity to all ion weapons
#"IsIonWeaponYield" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,                      
#"Ion Projectile" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,             
#"Ion Weapon" : App.g_kSystemWrapper.GetRandomNumber(20) + 0,  

#"IsIsokineticYield" : App.g_kSystemWrapper.GetRandomNumber(8) + 2,                     # Immunity to all kinds of isokinetic attacks, including isokinetic cannon rounds
#"Isokinetic Cannon Round" : App.g_kSystemWrapper.GetRandomNumber(8) + 2,

#"IsMultipleDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(32) + 5,              # Immunity to all multiple disablers
#"Multiple Disable" : App.g_kSystemWrapper.GetRandomNumber(32) + 5,

#"IsNanoprobeYield" : App.g_kSystemWrapper.GetRandomNumber(4) + 0,                      # Immunity to nanoprobes
#"Nanoprobe Projectile" : App.g_kSystemWrapper.GetRandomNumber(4) + 0,

#"Phalantium Wave" : App.g_kSystemWrapper.GetRandomNumber(52) + 160,                    # Immunity to Phalantium Wave

#"IsPhaseYield" : App.g_kSystemWrapper.GetRandomNumber(100) + 200,                       # Immunity to standard Phased weaponry (specifically torpedoes)
#"IsPhasedYield" : App.g_kSystemWrapper.GetRandomNumber(100) + 200,                      # Immunity to one alternative Phased Weaponry (probably a typo, better keep it)
#"Phased Torpedo" : App.g_kSystemWrapper.GetRandomNumber(100) + 200,

#"IsPowerDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(14) + 2,                  # Immunity to all power disablers
#"Power Disable" : App.g_kSystemWrapper.GetRandomNumber(14) + 2,

#"IsRandomDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(16) + 0,                 # Immunity to all strange disablers
#"Random Disable" : App.g_kSystemWrapper.GetRandomNumber(16) + 0,

#"IsRefluxWeaponYield" : App.g_kSystemWrapper.GetRandomNumber(100) + 100,                 # Immunity to Reflux weaponry (specifically torpedoes)

#"IsSensorDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(10) + 0,                 # Immunity to all sensor disablers
#"Sensor Disable" : App.g_kSystemWrapper.GetRandomNumber(10) + 0,

#"IsShieldDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,                 # Immunity to all shield disablers
#"Shield Disable" : App.g_kSystemWrapper.GetRandomNumber(12) + 0,

#"Spatial Charge" : App.g_kSystemWrapper.GetRandomNumber(40) + 40,                      # Immunity to Spatial Charge

#"IsTachyonProjectileYield" : App.g_kSystemWrapper.GetRandomNumber(120) + 0,             # Immunity against Tachyon weapons
#"Tachyon Weapon" : App.g_kSystemWrapper.GetRandomNumber(120) + 0,

#"IsTimeVortexYield" : App.g_kSystemWrapper.GetRandomNumber(1200) + 30000,               # Immunity against Time Vortex weaponry

#"IsTransphasicYield" : App.g_kSystemWrapper.GetRandomNumber(300) + 400,                # Immunity against Transphasic technology (specifically Transphasic Torpedoes)

#"IsWarpDisablerYield" : App.g_kSystemWrapper.GetRandomNumber(14) + 0,                   # Immunity to all warp disablers
#"Warp Disable" : App.g_kSystemWrapper.GetRandomNumber(14) + 0,


# TO-DO this is for offensive, leaving here just in case
#"Dicohesive Tech Shields": App.g_kSystemWrapper.GetRandomNumber(100) + 100, 

}

normalWeaponAdaptation = {

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

			import traceback
			try:
				if not adaptationProgress.has_key(fileName):
					myGoodPlugin = dotPrefix + fileName
					
					# I really wanted to make it so it only imports these two methods, but it is not letting me do it :(
					# The only other secure option I could think about is making random files with the name and those two values in the name and then splitting them up, but if there's an update you would end up with rubbish as well
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounterRdm"])
					# banana = __import__(myGoodPlugin, fromlist=["defenseCounter"])

					banana = __import__(myGoodPlugin, globals(), locals(), ["defenseCounterRdm"])

					randomness = abs(banana.defenseCounterRdm())
					constantness = abs(banana.defenseCounter())
					trueRandomness = App.g_kSystemWrapper.GetRandomNumber(randomness)
					#print constantness
					#print randomness
					#print trueRandomness
					
					# This standard is to call the file as "IsXXXXYield", with XXXX being the tech, that is "IsDrainYield", "IsPhasedYield", etc. Or call it like the Yield name (f.ex. "Hopping Torpedo")
					adaptationProgress[fileName] =  trueRandomness + constantness
					
					#print "Borg reviewing of this tech is a success, adapting at the following number of shots: " + str(adaptationProgress[fileName])
			except:
				print "someone attempted to add more than they should to the Borg Adaptation script"
				traceback.print_exc()


LoadExtraLimitedPlugins()
#print adaptationProgress


class BorgAdaptationDef(FoundationTech.TechDef):

	def OnDefense(self, pShip, pInstance, oYield, pEvent, itemName):
		global normalWeaponAdaptation, nonYieldAdaptationCounter, extraReductionAdaptationCycle
		# let's make it so people can customize how fast can a borg ship adapt, within reason
		learningFactor = pInstance.__dict__['Borg Adaptation']
		if learningFactor > maxCountdown:
			learningFactor = maxCountdown
		elif learningFactor < -maxCountdown:
			learningFactor = -maxCountdown

		borgAdapted = 0
		if oYield:
			import traceback
			try:
				for attre in adaptationProgress.keys():
					sameYield = 0
					if not FoundationTech.oTechs.has_key(attre):
						sameYield = (0 == 1) # For some reason it doesn't recognize False like that :/
					else:
						sameYield = (oYield == FoundationTech.oTechs[attre])

					if (hasattr(oYield, str(attre)) and getattr(oYield, str(attre))()) or sameYield:
						if not adaptationProgress.has_key(attre):
							adaptationProgress[attre] = 800
						if adaptationProgress[attre] <= 0:
							adaptationProgress[attre] = -1
							print "OH NO, THE BORG ADAPTED TO THIS WEAPON's SPECIAL YIELD"
							borgAdapted = 1
						elif adaptationProgress[attre] > maxCountdown:
							adaptationProgress[attre] = maxCountdown

						adaptationProgress[attre] = adaptationProgress[attre] - learningFactor

				if not (itemName == "None whatsoever") and not adaptationProgress.has_key(oYield):
					adaptationProgress[oYield] = 800
			except:
				print "something went wrong with Borg Adaptation technology"
				traceback.print_exc()
		
	
		import traceback
		try:
			if not (itemName == "None whatsoever"):
				if not normalWeaponAdaptation.has_key(itemName):
					normalWeaponAdaptation[itemName] = 0

				fRadius = pEvent.GetRadius()
				fDamage = abs(pEvent.GetDamage())
				kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())

				if pEvent.IsHullHit():
					# damage values


					# get the systems
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
					kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
					for pSystem in lSystems:
						vDifference = NiPoint3ToTGPoint3(pSystem.GetPosition())
						vDifference.Subtract(kPoint)

						if pSystem.GetRadius() + fRadius >= vDifference.Length():
							if pSystem.IsTargetable():
								lAffectedSystems.append(pSystem)
							else:
								lNonTargetableAffeSys.append(pSystem)

					print lAffectedSystems
					print lNonTargetableAffeSys

					normalWeaponAdaptation[itemName] = self.NormalLearningCalculation(itemName, normalWeaponAdaptation[itemName], learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle)

					# calculate the damage per radius
					fOffSet = 1 + fRadius
					fAllocatedFactor = fOffSet
					if fAllocatedFactor < 1:
						fAllocatedFactor = 1
					
					damageHealed = self.DamageCalculation(itemName, nonYieldAdaptationCounter, normalWeaponAdaptation, fDamage)
					# print "Event radius: " + str(fRadius)

					pHull=pShip.GetHull()
					notInThere = 0
					lenaffectedSys = len(lAffectedSystems)
					for pSystem in lAffectedSystems:
						if pSystem.GetName() == pHull.GetName():
							print "It seems the hull is here"
							notInThere = 1
						status = pSystem.GetConditionPercentage()
						# print "status" + str(status)
						if status > 0:
							fNewCondition = status + (damageHealed / pSystem.GetMaxCondition()) * fAllocatedFactor / lenaffectedSys
							print "TARGE " + str(status) +"-> fNewCondition = " + str(fNewCondition) + " for " + str(pSystem.GetName())
							
							if fNewCondition < 0:
								fNewCondition = 0
							elif fNewCondition > 1:
								fNewCondition = 1
							pSystem.SetConditionPercentage(fNewCondition)

					lenaffecteduntSys = len(lNonTargetableAffeSys)
					for pSystem in lNonTargetableAffeSys:
						iamHull = 0
						if pSystem.GetName() == pHull.GetName():
							print "It seems the hull is here"
							notInThere = 1
							iamHull = 1
						status = pSystem.GetConditionPercentage()
						# print "status" + str(status)
						if status > 0:
							dividerIs = lenaffecteduntSys
							if iamHull:
								dividerIs = 1
							fNewCondition = status + abs(damageHealed / pSystem.GetMaxCondition()) * fAllocatedFactor / dividerIs
							print "NOT TARGE " + str(status) +"-> fNewCondition = " + str(fNewCondition) + "for" + str(pSystem.GetName())
							
							if fNewCondition < 0:
								fNewCondition = 0
							elif fNewCondition > 1:
								fNewCondition = 1
							pSystem.SetConditionPercentage(fNewCondition)

					if len(lAffectedSystems) <= 0 or notInThere == 0: # hull hit but no subsystems affected? We must guess it's the hull only, then!
						if not(pHull==None):
							status = pHull.GetConditionPercentage()
							fNewCondition = status + (damageHealed / pHull.GetMaxCondition()) * fAllocatedFactor / (1 + lenaffectedSys)
							if fNewCondition > 1.0:
								fNewCondition = 1.0
							pHull.SetConditionPercentage(fNewCondition)
				else:

					pShields = pShip.GetShields()
					shieldHitBroken = 0
					if pShields and not pShields.IsDisabled():
						# get the nearest reference
						pReferenciado = None
						dMasCercano = 0
						bPlateDisabled = 0
						pointForward = App.TGPoint3_GetModelForward()
						pointBackward = App.TGPoint3_GetModelBackward()
						pointTop = App.TGPoint3_GetModelUp()
						pointBottom = App.TGPoint3_GetModelDown()
						pointRight = App.TGPoint3_GetModelRight()
						pointLeft = App.TGPoint3_GetModelLeft()
						lReferencias = [pointForward, pointBackward, pointTop, pointBottom, pointLeft, pointRight]

						for pPunto in lReferencias:
							#print lReferencias.index(pPunto)
							pPunto.Subtract(kPoint)
							#print pPunto.Length()
							if pReferenciado == None or pPunto.Length() < dMasCercano:
								dMasCercano = pPunto.Length()
								pReferenciado = pPunto

						if pReferenciado:
							shieldDir = lReferencias.index(pReferenciado)
							fCurr = pShields.GetCurShields(shieldDir)
							fMax = pShields.GetMaxShields(shieldDir)
							if fCurr > (0.35 * fMax):
								damageHealed = self.DamageCalculation(itemName, nonYieldAdaptationCounter, normalWeaponAdaptation, fDamage)
								resultHeal = fCurr + damageHealed
								if resultHeal < 0.0:
									resultHeal = 0.0
								elif resultHeal > fMax:
									resultHeal = fMax
								pShields.SetCurShields(shieldDir, resultHeal)

					normalWeaponAdaptation[itemName] = self.NormalLearningCalculation(itemName, normalWeaponAdaptation[itemName], learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle)
						
		except:
			print "something went wrong with Borg Adaptation technology"
			traceback.print_exc()

		if borgAdapted:
			return 1

	def DamageCalculation(self, itemName, nonYieldAdaptationCounter, normalWeaponAdaptation, fDamage):
		countDamage1 = ((nonYieldAdaptationCounter - normalWeaponAdaptation[itemName]) / nonYieldAdaptationCounter)
		if countDamage1 > 0:
			countDamage2 = countDamage1 ** (1.0/3.0)
		elif countDamage1 < 0:
			countDamage2 = -((-countDamage1) ** (1.0/3.0))
		else: # In case your python doesn't support this or makes it work differently
			countDamage2 = 0
		damageMultiplier = (countDamage2  + 1.0) * 0.5
		if nonYieldAdaptationCounter < normalWeaponAdaptation[itemName]:
			damageMultiplier = damageMultiplier - 0.08
		print "dmg multiplier for " + str(itemName) + " stage " + str(normalWeaponAdaptation[itemName]) + " with " + str(countDamage1) + " and " + str(countDamage2) + ": " + str(damageMultiplier)
		damageHealed = (fDamage * ( 1 - damageMultiplier))

		print "dmg multiplier for " + str(itemName) + " stage " + str(normalWeaponAdaptation[itemName]) + " with " + str(countDamage1) + " and " + str(countDamage2) + ": " + str(damageMultiplier)
		return damageHealed

	def NormalLearningCalculation(self, itemName, normalWeaponAdaptationI, learningFactor, nonYieldAdaptationCounter, extraReductionAdaptationCycle):
		normalWeaponAdaptationI = normalWeaponAdaptationI + learningFactor
		if normalWeaponAdaptationI < -10:
			normalWeaponAdaptationI = -10
		elif normalWeaponAdaptationI > (nonYieldAdaptationCounter + extraReductionAdaptationCycle):
			print "OH NO, THE BORG ADAPTED TO THIS WEAPON AND ITS SHIELD DAMAGE IS REDUCED"
			normalWeaponAdaptationI = nonYieldAdaptationCounter + extraReductionAdaptationCycle

		return normalWeaponAdaptationI

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

oBorgAdaptation = BorgAdaptationDef('Borg Adaptation')
