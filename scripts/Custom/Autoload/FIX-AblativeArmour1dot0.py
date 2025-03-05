# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 5th March 2025
# VERSION 0.3
# By Alex SL Gato
# AblativeArmour.py by Foundation Technologies team and Apollo's Advanced Technologies -> v1.1 fix
#
# Changes: 
# - Currently the armour does not heal at all, meaning that negligible bleedthrough damage through a shield will eventually deplete it. This file aims to fix that, by checking the status of the armour integrity hardpoint first, and then uses the highest of the values.
# - From Version 0.2 onwards, a singleton issue is fixed - however it might cause issues with other scripts if those already checekd on armour levels.
# - From Version 0.3 onwars, the armor gauge issue is fixed, as long as the scripts.Custom-Autoload.FIX-FoundationTech20050703HullGaugeDetachShipFix file is present. 

from bcdebug import debug
import App
import FoundationTech
import Foundation

necessaryToUpdate = 0
AblativeArmour = None
try:
	try:
		AblativeArmour = __import__("ftb.Tech.AblativeArmour") #from ftb.Tech import AblativeArmour
	except:
		try:
			AblativeArmour = __import__("Custom.Techs.AblativeArmour")
		except:
			print "Could not find AblativeArmour tech to patch"
	if AblativeArmour != None:	
		if hasattr(AblativeArmour,"AblativeArmourVersion"):
			if AblativeArmour.AblativeArmourVersion == 1.0:
				necessaryToUpdate = 1
				print "fixing your AblativeArmour.py 1.0 lack of regeneration"
			else :
				necessaryToUpdate = 0
				print "Congrats! Your AblativeArmour.py version doesn't require of any fix we are aware of - feel free to delete FIX-AblativeArmour1dot0 from your Autoload folder"
		else:
			necessaryToUpdate = 1 # the oldest versions have no signature
			print "Updating your AblativeArmour.py <= 1.0 to regenerate"
	else:
		necessaryToUpdate = 0
		print "Unable to find ftb Tech AblativeArmour"
except:
	print "Unable to find ftb Tech AblativeArmour"
	pass

if necessaryToUpdate and AblativeArmour != None:
	original = AblativeArmour.AblativeDef.OnDefense
	originalAttach = AblativeArmour.AblativeDef.Attach

	def ReplacementOnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		repair = pInstance.__dict__['Ablative Armour L']

		#print 'AblativeDef.OnDefense', pShip.GetName(), repair, pEvent.GetDamage()

		pSubName = self.GetSystemName()
		if str(repair)[0] == "[":
			pSubName = repair[1]
			repair = repair[0]

		myOldHP = pInstance.__dict__[self.GetSystemPointer()]
			
		if repair > 0.0:
			oldRepair = pInstance.__dict__['Ablative Armour L']

			pSubNameO = self.GetSystemName()
			if str(oldRepair)[0] == "[":
				pSubNameO = oldRepair[1]
				oldRepair = oldRepair[0]
			
			if oldRepair <= 0.0 or not myOldHP:
				self.AttachShip(pShip, pInstance)

			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			foundMySubsystem = 0
			while pSubsystem:
				if pSubsystem.GetName() == pSubName:
					foundMySubsystem = 1
					# Alex SL Gato addition: to make it able to repair and know about it better
					temp = pSubsystem.GetCondition()
					if temp > repair:
						oldRepair = repair
						repair = temp
					if str(pInstance.__dict__['Ablative Armour L'])[0] == "[":
						oldRepair = repair
						pInstance.__dict__['Ablative Armour L Old'][0] = oldRepair
						pInstance.__dict__['Ablative Armour L'][0] = repair = repair - pEvent.GetDamage()
				
					else:
						oldRepair = repair
						pInstance.__dict__['Ablative Armour L Old'] = oldRepair
						pInstance.__dict__['Ablative Armour L'] = repair = repair - pEvent.GetDamage()

					pSubsystem.SetCondition(repair)
					# pSubsystem.SetCondition(pInstance.__dict__['Ablative Armour L'])
				elif pSubsystem.GetCondition() > 0.0 and not pSubsystem.IsDisabled():
					pSubsystem.SetCondition(pSubsystem.GetMaxCondition())
					iChildren = pSubsystem.GetNumChildSubsystems()
					if iChildren > 0:
						for iIndex in range(iChildren):
							pChild = pSubsystem.GetChildSubsystem(iIndex)
							if pChild.IsDisabled():
								continue
							pChild.SetCondition(pChild.GetMaxCondition())

				pSubsystem = pShip.GetNextSubsystemMatch(pIterator)
			pShip.EndGetSubsystemMatch(pIterator)

			# Alex SL Gato addition/modification: In case there's no subsystem for some reason, to prevent godmode ships
			if foundMySubsystem == 0:
				if str(pInstance.__dict__['Ablative Armour L'])[0] == "[":
					oldRepair = repair
					pInstance.__dict__['Ablative Armour L Old'][0] = oldRepair
					pInstance.__dict__['Ablative Armour L'][0] = repair = repair - pEvent.GetDamage()
				
				else:
					oldRepair = repair
					pInstance.__dict__['Ablative Armour L Old'] = oldRepair
					pInstance.__dict__['Ablative Armour L'] = repair = repair - pEvent.GetDamage()
		else:
			if str(pInstance.__dict__['Ablative Armour L Old'])[0] == "[":
				pInstance.__dict__['Ablative Armour L Old'][0] = -1
				pInstance.__dict__['Ablative Armour L'][0] = repair
			else:
				pInstance.__dict__['Ablative Armour L Old'] = -1
				pInstance.__dict__['Ablative Armour L'] = repair

			myOldHP = pInstance.__dict__[self.GetSystemPointer()]
			if myOldHP:
				pInstance.__dict__[self.GetSystemPointer()].SetCondition(repair)
			"""
			if self in pInstance.lHealthGauge:
				print "I am on the health gauges"
				pInstance.lHealthGauge.remove(self)
				if len(pInstance.lHealthGauge) > 0:
					if pInstance.pDisplay == None:
						if len(FoundationTech.dDisplays[pInstance.pShipID]) > 0:
							pInstance.pDisplay = FoundationTech.dDisplays[pInstance.pShipID][-1]
					if pInstance.pDisplay != None:
						pInstance.lHealthGauge[-1].SetGauge(pShip, pInstance, pInstance.pDisplay.GetHealthGauge())
			pInstance.__dict__[self.GetSystemPointer()] = None
			"""

			self.DetachShip(pShip, pInstance)
			#self.Detach(pInstance)

	AblativeArmour.AblativeDef.OnDefense = ReplacementOnDefense

	# 0.2 Addition!

	def ReplacementAttach(self, pInstance):
		debug(__name__ + ", Attach")
		originalAttach(self, pInstance)

		# Due to singletons, issues could happen
		pInstanceDict = pInstance.__dict__
		if not pInstanceDict.has_key("Ablative Armour L"):
			if str(pInstanceDict['Ablative Armour'])[0] == "[":
				pInstanceDict['Ablative Armour L'] = [0.0, "Ablative Armour"]
				pInstanceDict['Ablative Armour L'][0] = pInstance.__dict__['Ablative Armour'][0]
				pInstanceDict['Ablative Armour L'][1] = pInstance.__dict__['Ablative Armour'][1]

				pInstanceDict['Ablative Armour L Old'] = [0.0, "Ablative Armour"]
				pInstanceDict['Ablative Armour L Old'][0] = pInstance.__dict__['Ablative Armour'][0]
				pInstanceDict['Ablative Armour L Old'][1] = pInstance.__dict__['Ablative Armour'][1]
			else:
				pInstanceDict['Ablative Armour L'] = pInstance.__dict__['Ablative Armour']
				pInstanceDict['Ablative Armour L Old'] = pInstance.__dict__['Ablative Armour']

	AblativeArmour.AblativeDef.Attach = ReplacementAttach