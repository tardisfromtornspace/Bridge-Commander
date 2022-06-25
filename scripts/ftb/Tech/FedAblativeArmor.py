from bcdebug import debug
import App
import FoundationTech
import Foundation

NonSerializedObjects = (
"oAblative",
"oPolarizedHullPlating",
)

def NiPoint3ToTGPoint3(p):
	debug(__name__ + ", NiPoint3ToTGPoint3")
	kPoint = App.TGPoint3()
	kPoint.SetXYZ(p.x, p.y, p.z)
	return kPoint


class AblativeArmorDef(FoundationTech.TechDef):
	
	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		kTiming = App.TGProfilingInfo("AblativeArmorDef, OnDefense")
		if not pInstance.__dict__['Fed Ablative Armor'].has_key("Plates"):
			print "Ablative Armor Error: No Armor plates found"
			return
		# saved stuff
		if not pInstance.__dict__['Fed Ablative Armor'].has_key("Ships"):
			pInstance.__dict__['Fed Ablative Armor']["Ships"] = {}
		if not pInstance.__dict__['Fed Ablative Armor']["Ships"].has_key(pShip.GetObjID()):
			pInstance.__dict__['Fed Ablative Armor']["Ships"][pShip.GetObjID()] = {}
		dOldConditions = pInstance.__dict__['Fed Ablative Armor']["Ships"][pShip.GetObjID()]
		
		# armor plate names
		lArmorNames = pInstance.__dict__['Fed Ablative Armor']["Plates"]		
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
				lSystems.append(pChild)
		pShip.EndGetSubsystemMatch(kIterator)
		
		# get the armor covering the damage, could be done in above loop
		pProtectingPlate = None
		fHighestCondition = 0
		bPlateDisabled = 0
		for pPlate in lArmors:
			vDifference = NiPoint3ToTGPoint3(pPlate.GetPosition())
			vDifference.Subtract(kPoint)
			
			if fRadius + pPlate.GetRadius() > vDifference.Length() and pPlate.GetConditionPercentage() > fHighestCondition:
				pProtectingPlate = pPlate
				fHighestCondition = pProtectingPlate.GetConditionPercentage()
			if pPlate.IsDisabled():
				bPlateDisabled = 1
		
		if not pProtectingPlate:
			# no plate, but still record the current damage - we could need it later
			for pSystem in lSystems:
				dOldConditions[pSystem.GetName()] = pSystem.GetConditionPercentage()
			return
		# if this was not a hull hit, do nothing
		if not pEvent.IsHullHit():
			return

		# get affected systems
		lAffectedSystems = []
		kProtectingPlatePos = NiPoint3ToTGPoint3(pProtectingPlate.GetPosition())
		for pSystem in lSystems:
			vDifference = NiPoint3ToTGPoint3(pSystem.GetPosition())
			vDifference.Subtract(kProtectingPlatePos)

			if pProtectingPlate.GetRadius() + pSystem.GetRadius() > vDifference.Length():
				lAffectedSystems.append(pSystem)
		
		# remove visible damage if our plate is still intact
		#if not bPlateDisabled:
		#	pShip.RemoveVisibleDamage()
		
		# calculate the damage per radius
		fOffSet = 1 + fRadius
		fAllocatedFactor = -1 * pProtectingPlate.GetRadius() + fOffSet
		if fAllocatedFactor < 0:
			fAllocatedFactor = 0
		
		# now reallocate the damage
		for pSystem in lAffectedSystems:
			if not dOldConditions.has_key(pSystem.GetName()):
				dOldConditions[pSystem.GetName()] = 1.0
					
			fOldCondition = dOldConditions[pSystem.GetName()]
			if not pProtectingPlate.IsDisabled():
				fNewCondition = fOldCondition
			else:
				fDiff = 1 - fOldCondition + fDamage / pSystem.GetMaxCondition()
				# some of these calcs could be done outside the loop
				fNewCondition = fOldCondition - fDiff * (1-pProtectingPlate.GetConditionPercentage()) * fAllocatedFactor / len(lAffectedSystems)
			pSystem.SetConditionPercentage(fNewCondition)
			dOldConditions[pSystem.GetName()] = fNewCondition

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

	def GetSystemName(self):
		debug(__name__ + ", GetSystemName")
		return "Ablative Armour"

	def GetSystemPointer(self):
		debug(__name__ + ", GetSystemPointer")
		return 'pArmour'


oAblative = AblativeArmorDef('Fed Ablative Armor')

class PolarizedHullPlatingDef(FoundationTech.TechDef):
	
	def OnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		kTiming = App.TGProfilingInfo("PolarizedHullPlatingDef, OnDefense")
		if not pInstance.__dict__[self.name].has_key("Plates"):
			print "Polarized Hull Plating Error: No plates found"
			return
		# saved stuff
		if not pInstance.__dict__[self.name].has_key("Ships"):
			pInstance.__dict__[self.name]["Ships"] = {}
		if not pInstance.__dict__[self.name]["Ships"].has_key(pShip.GetObjID()):
			pInstance.__dict__[self.name]["Ships"][pShip.GetObjID()] = {}
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
				lSystems.append(pChild)
		pShip.EndGetSubsystemMatch(kIterator)
		
		# get the armor covering the damage, could be done in above loop
		pProtectingPlate = None
		fHighestCondition = 0
		bPlateDisabled = 0
                bPlateAtRange = 0
		for pPlate in lArmors:
			vDifference = NiPoint3ToTGPoint3(pPlate.GetPosition())
			vDifference.Subtract(kPoint)
			
			# if fRadius + pPlate.GetRadius() > vDifference.Length() and pPlate.GetConditionPercentage() > fHighestCondition:
                        # Yeah I know this is oversimplified, but it has been made as if all the polarized platings can work from a range
			if pPlate.GetConditionPercentage() > fHighestCondition:
				pProtectingPlate = pPlate
				fHighestCondition = pProtectingPlate.GetConditionPercentage()
                                if fRadius + pPlate.GetRadius() > vDifference.Length():
                                        bPlateAtRange = 1
                                else:
                                        bPlateAtRange = 0
			if pPlate.IsDisabled():
				bPlateDisabled = 1
		
		if not pProtectingPlate:
			# no plate, but still record the current damage - we could need it later
			for pSystem in lSystems:
				dOldConditions[pSystem.GetName()] = pSystem.GetConditionPercentage()
			return
		# if this was not a hull hit, do nothing
		if not pEvent.IsHullHit():
			return

		# get affected systems
		lAffectedSystems = []
		kProtectingPlatePos = NiPoint3ToTGPoint3(pProtectingPlate.GetPosition())
		for pSystem in lSystems:
			vDifference = NiPoint3ToTGPoint3(pSystem.GetPosition())
			vDifference.Subtract(kPoint)
                        # vDifference.Subtract(kProtectingPlatePos)

			# if pProtectingPlate.GetRadius() + pSystem.GetRadius() > vDifference.Length():
                        if fRadius + pSystem.GetRadius() > vDifference.Length():
				lAffectedSystems.append(pSystem)
		
		# remove visible damage if our plate is still intact
		#if not bPlateDisabled:
		#	pShip.RemoveVisibleDamage()
		
		# calculate the damage per radius
		#fOffSet = 1 + fRadius
		#fAllocatedFactor = -1 * pProtectingPlate.GetRadius() + fOffSet
		#if fAllocatedFactor < 0:
		#fAllocatedFactor = 0
                fAllocatedFactor = 1
		
		# now reallocate the damage
		for pSystem in lAffectedSystems:
			if not dOldConditions.has_key(pSystem.GetName()):
				dOldConditions[pSystem.GetName()] = 1.0
					
			fOldCondition = dOldConditions[pSystem.GetName()]
			if not pProtectingPlate.IsDisabled():
				fDiff = 1 - fOldCondition + fDamage / pSystem.GetMaxCondition()
				# some of these calcs could be done outside the loop
				fNewCondition = fOldCondition - 1.5 * fDiff * (1-pProtectingPlate.GetConditionPercentage()) * fAllocatedFactor / (1 + len(lAffectedSystems))
			else:
				fDiff = 1 - fOldCondition + fDamage / pSystem.GetMaxCondition()
				# some of these calcs could be done outside the loop
				fNewCondition = fOldCondition - 1.5 * fDiff * fAllocatedFactor / (1 + len(lAffectedSystems))
			pSystem.SetConditionPercentage(fNewCondition)
			dOldConditions[pSystem.GetName()] = fNewCondition
                if bPlateAtRange == 0:
			if not dOldConditions.has_key(pProtectingPlate.GetName()):
				dOldConditions[pProtectingPlate.GetName()] = 1.0
                        fOldCondition2 = dOldConditions[pProtectingPlate.GetName()]
                        fDiff2 = 1 - fOldCondition2 + fDamage / pProtectingPlate.GetMaxCondition()
                        fNewCondition2 = fOldCondition2 - 0.5 * fDiff2 / (len(lAffectedSystems) + 1)
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

	def GetSystemName(self):
		debug(__name__ + ", GetSystemName")
		return "Ablative Armour"

	def GetSystemPointer(self):
		debug(__name__ + ", GetSystemPointer")
		return 'pArmour'


oPolarizedHullPlating = PolarizedHullPlatingDef('Polarized Hull Plating')
