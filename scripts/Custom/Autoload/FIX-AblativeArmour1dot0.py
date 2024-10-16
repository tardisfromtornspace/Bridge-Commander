# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 16th October 2024
# VERSION 0.2
# By Alex SL Gato
# AblativeArmour.py by Foundation Technologies team and Apollo's Advanced Technologies -> v1.1 fix
#
# Changes: 
# - Currently the armour does not heal at all, meaning that negligible bleedthrough damage through a shield will eventually deplete it. This file aims to fix that, by checking the status of the armour integrity hardpoint first, and then uses the highest of the values.
# - From Version 0.2 onwards, a singleton issue is fixed - however it might cause issues with other scripts if those already checekd on armour levels


from bcdebug import debug
import App
import FoundationTech
import Foundation

necessaryToUpdate = 0
try:
	from ftb.Tech import AblativeArmour
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
except:
    print "Unable to find ftb Tech AblativeArmour"
    pass

if necessaryToUpdate:
	from ftb.Tech import AblativeArmour
	original = AblativeArmour.AblativeDef.OnDefense
	originalAttach = AblativeArmour.AblativeDef.Attach

	def ReplacementOnDefense(self, pShip, pInstance, oYield, pEvent):
		debug(__name__ + ", OnDefense")
		repair = pInstance.__dict__['Ablative Armour L']

		print 'AblativeDef.OnDefense', pShip.GetName(), repair, pEvent.GetDamage()

		pSubName = self.GetSystemName()
		if str(repair)[0] == "[":
			pSubName = repair[1]
			repair = repair[0]
			
		if repair > 0.0:
			pIterator = pShip.StartGetSubsystemMatch(App.CT_SHIP_SUBSYSTEM)
			pSubsystem = pShip.GetNextSubsystemMatch(pIterator)

			foundMySubsystem = 0
			while pSubsystem:
				if pSubsystem.GetName() == pSubName:
					foundMySubsystem = 1
					# Alex SL Gato addition: to make it able to repair and know about it better
					temp = pSubsystem.GetCondition()
					if temp > repair:
						repair = temp
					if str(pInstance.__dict__['Ablative Armour L'])[0] == "[":
						pInstance.__dict__['Ablative Armour L'][0] = repair = repair - pEvent.GetDamage()
				
					else:
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
					pInstance.__dict__['Ablative Armour L'][0] = repair = repair - pEvent.GetDamage()
				
				else:
					pInstance.__dict__['Ablative Armour L'] = repair = repair - pEvent.GetDamage()
		else:
			pInstance.__dict__[self.GetSystemPointer()].SetCondition(repair)
			
			#self.DetachShip(pShip, pInstance)
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
			else:
				pInstanceDict['Ablative Armour L'] = pInstance.__dict__['Ablative Armour']

	AblativeArmour.AblativeDef.Attach = ReplacementAttach
