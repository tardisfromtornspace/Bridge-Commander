# THIS MOD IS NOT SUPPORTED BY ACTIVISION
# HullPolarizer.py
# Version 1.36
# By Alex SL Gato
# Based on FedAblativeArmour.py and AblativeArmour.py made by the FoundationTechnologies team (specifically, but not only, MLeo) and scripts/Custom/DS9FX/DS9FXLifeSupport/HandleShields.py by USS Sovereign
from bcdebug import debug
import App
import FoundationTech
import Foundation

MODINFO = {
		"Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
		"Version": "1.36",
		"License": "LGPL",
		"Description": "Read the small title above for more info"
	}

kEmptyColor = App.TGColorA()
kEmptyColor.SetRGBA(App.g_kSubsystemFillColor.r,App.g_kSubsystemFillColor.g,App.g_kSubsystemFillColor.b,App.g_kSubsystemFillColor.a)
kFillColor = App.TGColorA()
kFillColor.SetRGBA(210.0/255.0, 210.0/255.0, 210.0/255.0, App.g_kSubsystemFillColor.a)

NonSerializedObjects = (
"oPolarizedHullPlating",
)

def NiPoint3ToTGPoint3(p):
	debug(__name__ + ", NiPoint3ToTGPoint3")
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint

class PolarizedHullPlatingDef(FoundationTech.TechDef):
	
	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		kTiming = App.TGProfilingInfo("PolarizedHullPlatingDef, OnDefense")
		if not pInstance.__dict__[self.name].has_key("Plates"):
			print "Polarized Hull Plating Error: No plates found"
			return
		# saved stuff
		fixedAmount = None
		maxEffec = 1.0
		minEffec = 0.0
		if pInstance.__dict__[self.name].has_key("Fixed"):
			fixedAmount = pInstance.__dict__[self.name]["Fixed"]
		if pInstance.__dict__[self.name].has_key("minEffec"):
			minEffec = pInstance.__dict__[self.name]["minEffec"]
		if pInstance.__dict__[self.name].has_key("maxEffec"):
			maxEffec = pInstance.__dict__[self.name]["maxEffec"]
		if not pInstance.__dict__[self.name].has_key("Incremental"):
			pInstance.__dict__[self.name]["Incremental"] = 0
		if not pInstance.__dict__[self.name].has_key("PlatePosMatters"):
			pInstance.__dict__[self.name]["PlatePosMatters"] = 0
		if not pInstance.__dict__[self.name].has_key("Ships"):
			pInstance.__dict__[self.name]["Ships"] = {}
		if not pInstance.__dict__[self.name]["Ships"].has_key(pShip.GetObjID()):
			pInstance.__dict__[self.name]["Ships"][pShip.GetObjID()] = {}

                incremental = pInstance.__dict__[self.name]["Incremental"]
                placePosMatters = pInstance.__dict__[self.name]["PlatePosMatters"]
		dOldConditions = pInstance.__dict__[self.name]["Ships"][pShip.GetObjID()]
		
		# armor plate names
		lArmorNames = pInstance.__dict__[self.name]["Plates"]		
		# position of the impact
		kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
		# damage values
		fRadius = pEvent.GetRadius()
		fDamage = pEvent.GetDamage()

		# get the armors and other systems in the right lists
		lArmors = []
		lSystems = []
		kIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
		while (1):
			pSubsystem = pShip.GetNextSubsystemMatch(kIterator)
			if not pSubsystem:
				break
			
			if pSubsystem.GetName() in lArmorNames:
				lArmors.append(pSubsystem)
			else:
				lSystems.append(pSubsystem)
			
			for i in range(pSubsystem.GetNumChildSubsystems()):
				pChild = pSubsystem.GetChildSubsystem(i)

				if pChild.GetName() in lArmorNames:
					lArmors.append(pChild)
				else:
					lSystems.append(pChild)

		pShip.EndGetSubsystemMatch(kIterator)
		
		# get the armor covering the damage, could be done in above loop
		pProtectingPlate = None
		fHighestCondition = 0
		bPlateAtRange = 0
		bPlateE = 0
		for pPlate in lArmors:
			vDifference = NiPoint3ToTGPoint3(pPlate.GetPosition())
			vDifference.Subtract(kPoint)

			# if fRadius + pPlate.GetRadius() > vDifference.Length() and pPlate.GetConditionPercentage() > fHighestCondition:
			# Yeah I know this is oversimplified, but it has been made as if all the polarized platings can work from a range
			if ((not placePosMatters) or (fRadius + pPlate.GetRadius() > vDifference.Length())) and pPlate.GetConditionPercentage() > fHighestCondition:
				bPlateE = 1
				if not pPlate.IsDisabled():
					pProtectingPlate = pPlate
					fHighestCondition = pProtectingPlate.GetConditionPercentage()
					if fRadius + pPlate.GetRadius() >= vDifference.Length() and pPlate.IsTargetable():
						bPlateAtRange = 1
					else:
						bPlateAtRange = 0
		
		noAvailablePlate = (pProtectingPlate == None or not pProtectingPlate)
		if noAvailablePlate:
			# no plate or no actual damage, but still record the current damage - we could need it later
			pShipModule=__import__(pShip.GetScript())
			if fDamage > 0.0:
				try:
					kShipStats = pShipModule.GetShipStats()
					if kShipStats.has_key('DamageRadMod'):
						pShip.SetVisibleDamageRadiusModifier(kShipStats['DamageRadMod'])
					else:
						pShip.SetVisibleDamageRadiusModifier(1.0)
					if kShipStats.has_key('DamageStrMod'):
						pShip.SetVisibleDamageStrengthModifier(kShipStats['DamageStrMod'])
					else:
						pShip.SetVisibleDamageStrengthModifier(1.0)
				except:
					pShip.SetVisibleDamageRadiusModifier(1.0)
					pShip.SetVisibleDamageStrengthModifier(1.0)

			for pSystem in lSystems:
				dOldConditions[pSystem.GetName()] = pSystem.GetConditionPercentage()

			if (not incremental):
				return
			else:
				placePosMatters = 0

		pShields = pShip.GetShields()
		energyCommited = 1.0
		if pShields:
			energyCommited = pShields.GetPowerPercentageWanted()

		platingEffect = 1.0
		try:
			if noAvailablePlate:
				platingEffect = 0.0
			else:
				platingEffect = pProtectingPlate.GetConditionPercentage() * energyCommited
		except:
			return

		if not noAvailablePlate:
			damageRadiVal = 1 - 0.85 * platingEffect
			if damageRadiVal < 0.0:
				damageRadiVal = 0
			damageStreVal = 1 - 0.75 * platingEffect
			if damageStreVal < 0.0:
				damageStreVal = 0

			pShip.SetVisibleDamageRadiusModifier(damageRadiVal)
			pShip.SetVisibleDamageStrengthModifier(damageStreVal)

		# if this was not a hull hit, do nothing
		if not pEvent.IsHullHit():
			return

		if fDamage <= 0.0: # If it heals us or does nothing, do not prevent the hull polarizer from healing, just store damage values
			for pSystem in lSystems:
				dOldConditions[pSystem.GetName()] = pSystem.GetConditionPercentage()
			return

		# get affected systems
		lAffectedSystems = []
		kProtectingPlatePos = NiPoint3ToTGPoint3(pProtectingPlate.GetPosition())
		kProtectingPlateRad = pProtectingPlate.GetRadius()
		for pSystem in lSystems:
			if pSystem.IsTargetable():
				vDifference = NiPoint3ToTGPoint3(pSystem.GetPosition())
				auxEx = 0
				if (placePosMatters):
					vDifference.Subtract(kProtectingPlatePos)
					auxEx = kProtectingPlateRad
				else:
					vDifference.Subtract(kPoint)
					auxEx = fRadius

				if auxEx + pSystem.GetRadius() >= vDifference.Length():
					lAffectedSystems.append(pSystem)
				else:
					dOldConditions[pSystem.GetName()] = pSystem.GetConditionPercentage()

		pHull=pShip.GetHull()
		if (pHull != None and (not pHull.IsTargetable()) and (not (pHull.GetName() in lArmorNames))):
			lAffectedSystems.append(pHull)
		
		# calculate the damage per radius
		fAllocatedFactor = 0
		if (placePosMatters):
			fOffSet = 1 + fRadius
			fAllocatedFactor = -1 * kProtectingPlateRad + fOffSet
			if fAllocatedFactor < 0:
				fAllocatedFactor = 0
		else:
			fAllocatedFactor = 1

		# now reallocate the damage

		if noAvailablePlate:
			pProcPlateCP = 0
		else:
			pProcPlateCP = pProtectingPlate.GetConditionPercentage()
			dOldConditions[pProtectingPlate.GetName()] = pProcPlateCP

		if (fixedAmount is None):
			polarizerEffectiveness = (1-pProcPlateCP) * energyCommited
		else:
			polarizerEffectiveness = fixedAmount

		if polarizerEffectiveness > maxEffec:
			polarizerEffectiveness = maxEffec

		if polarizerEffectiveness < minEffec:
			polarizerEffectiveness = minEffec		

		if (fixedAmount is None):
			inversePlateCondition = 1-pProcPlateCP
		else:
			inversePlateCondition = 1

		lenTotalAffectedSystems = bPlateAtRange + len(lAffectedSystems)
		genericDamageReduction = 0
		if lenTotalAffectedSystems > 0:
			#TO-DO genericDamageReduction = 1.5 * inversePlateCondition * polarizerEffectiveness * fAllocatedFactor / lenTotalAffectedSystems
			genericDamageReduction = 1.5 * (fDamage * inversePlateCondition * polarizerEffectiveness * fAllocatedFactor / lenTotalAffectedSystems)

		for pSystem in lAffectedSystems:
			if not dOldConditions.has_key(pSystem.GetName()):
				dOldConditions[pSystem.GetName()] = 1.0

			if dOldConditions[pSystem.GetName()] < pSystem.GetConditionPercentage():
				dOldConditions[pSystem.GetName()] = pSystem.GetConditionPercentage()
					
			fOldCondition = dOldConditions[pSystem.GetName()]
			if fOldCondition > 0.0:
				if not pProtectingPlate.IsDisabled() and not pSystem.GetName() == pProtectingPlate.GetName():
					"""
					## TO-DO ORIGINAL KINDA CODE
					fDiff = 1 - fOldCondition + (fDamage / pSystem.GetMaxCondition()) # Percentage of total health damaged before + percentage of the new damage = current
					# some of these calcs could be done outside the loop
					fNewCondition = fOldCondition - (fDiff * genericDamageReduction)


					################33
					## TO-DO "THINK" CODE
					# Damage received is:
					perceivedDamage = (fDamage / pSystem.GetMaxCondition()) / lenTotalAffectedSystems
						# THAT IS EQUAL TO
					perceivedDamage = (fDamage / lenTotalAffectedSystems / pSystem.GetMaxCondition()
					# the "new" condition we are in would be then
					fNewCondition = fOldCondition - perceivedDamage

					# THE "alternative new" "reduced" damage condition would be something like:
					fNewCondition = fOldCondition - (perceivedDamage * genericDamageReduction))

					# Then the armour resistance would be like
					fNewCondition = fOldCondition - ((fDamage / lenTotalAffectedSystems / pSystem.GetMaxCondition()) * genericDamageReduction)
						# THAT IS EQUAL TO					
					fNewCondition = fOldCondition - ((fDamage * genericDamageReduction / lenTotalAffectedSystems) / pSystem.GetMaxCondition())
						# THAT IS EQUAL TO
					fNewCondition = fOldCondition - ((fDamage * genericDamageReduction / lenTotalAffectedSystems) / pSystem.GetMaxCondition())
						# THAT IS EQUAL TO	
					fNewCondition = fOldCondition - ((fDamage * inversePlateCondition * polarizerEffectiveness / lenTotalAffectedSystems) / pSystem.GetMaxCondition())
				

					fDiff = fOldCondition - ((fDamage / pSystem.GetMaxCondition())/ lenTotalAffectedSystems)

					#################33
					"""
					## TO-DO TEST LINES
					fNewCondition = fOldCondition - (genericDamageReduction / pSystem.GetMaxCondition())
					## TO-DO TEST LINES

					minAdminsible = (fDamage / pSystem.GetMaxCondition())
					if fNewCondition > (fOldCondition + minAdminsible):
						fNewCondition = fOldCondition

					minAdmisible = (fOldCondition - minAdminsible)
					if fNewCondition < minAdmisible:
						fNewCondition = minAdmisible

					if fNewCondition > 1.0:
						fNewCondition = 1.0

				elif pProtectingPlate.IsDisabled():
					fNewCondition = pSystem.GetConditionPercentage()

				pSystem.SetConditionPercentage(fNewCondition)
				dOldConditions[pSystem.GetName()] = fNewCondition

		if bPlateAtRange == 0 and len(lAffectedSystems) > 0:
			fOldCondition2 = dOldConditions[pProtectingPlate.GetName()]
			#fDiff2 = 1 - fOldCondition2 + fDamage / pProtectingPlate.GetMaxCondition()
			fDiff2 = fDamage / pProtectingPlate.GetMaxCondition()
			fNewCondition2 = fOldCondition2 - fDiff2 / (len(lAffectedSystems) + 1)
			
			pProtectingPlate.SetConditionPercentage(fNewCondition2)
			dOldConditions[pProtectingPlate.GetName()] = fNewCondition2

	def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnBeamDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		#if pEvent.IsHullHit():
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnPulseDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		#if pEvent.IsHullHit():
		return self.OnDefense(pShip, pInstance, oYield, pEvent)

	def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
		debug(__name__ + ", OnTorpDefense")
		if oYield:
		 	if oYield.IsPhaseYield() or oYield.IsDrainYield():
		 		return

		#if pEvent.IsHullHit():
		return self.OnDefense(pShip, pInstance, oYield, pEvent)


	def Attach(self, pInstance):
		debug(__name__ + ", Attach")
		pInstance.lTechs.append(self)
		pInstance.lTorpDefense.append(self)
		pInstance.lPulseDefense.append(self)
		pInstance.lBeamDefense.append(self)

	def Detach(self, pInstance):
		debug(__name__ + ", Detach")
		pInstance.lTechs.remove(self)
		pInstance.lTorpDefense.remove(self)
		pInstance.lPulseDefense.remove(self)
		pInstance.lBeamDefense.remove(self)

	def GetSystemName(self, *args):
		debug(__name__ + ", GetSystemName")
		return "Polarized Hull Plating"

	def GetSystemPointer(self, *args):
		debug(__name__ + ", GetSystemPointer")
		return 'pArmour'

	def GetFillColor(self, *args):
		debug(__name__ + ", GetFillColor")
		global kFillColor
		return kFillColor
		
	def GetEmptyColor(self, *args):
		debug(__name__ + ", GetEmptyColor")
		global kEmptyColor
		return kEmptyColor


oPolarizedHullPlating = PolarizedHullPlatingDef('Polarized Hull Plating')
