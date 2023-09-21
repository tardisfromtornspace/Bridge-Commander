#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         DampeningAOEDefensiveField.py by Alex SL Gato
#         Version 0.3
#         21st September 2023
#         Based on scripts\ftb\Tech/Shields.py by MLeo Daalder, Apollo, Dasher, and the rest of the FoundationTechnologies team.
#         Special Thanks to USS Sovereign for telling me better tips to remove the need of a hardpoint-wise made-up axis.
#                          
#################################################################################################################
# What does this tech do: a variant of Multivectral shielding and Vree shields, but instead of uniforming all the shields with a chance, it distributes part of the conventional damage on a shield to the nearby ones (the furthest one is generally excluded) and doesn't try to do so on collapsed shields.
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file, but modify the values accordingly to what you want, and for actual values since the following is just a general example
# NOTE: replace "Galaxy" by the proper abbrev when doing so.
# - "Shield Transfer Ratio": OPTIONAL this script uses a formula where by default the more you go to the sides, the less is transferred - with this you can tweak that to make the transfer less the higher the value - even try 0 for equal values,
# and negative values if you want for it to transfer more to the sides! Very high values can also be used to heal the other shields, if balanced properly with Max Percentage Damage field.
# - "Max Percentage Damage": OPTIONAL this states how much part of the damage the shield hit closest can receive (of course, if you use a positive or neutral value in the previous "Shield Transfer Ratio" field). The numbers input are then
# considered in sixths, that is, if you set it to 1, that shield will only receive 1/6th of the damage, if it's 2, 2/6ths, and so on. You can even try negatives if you so desire.
# - "Collapse Threshold": OPTIONAL how much you need to have the shields down to consider that shield collapsed. Default is 0.25, that is, shield integrity at 25%. Minimum is 0%.
# - "Max Radians": OPTIONAL advanced, it makes it consider how far it extends the redistribution - the recommended value is 2 * math.pi/3.0, but you can try to do math.pi for total shield redistribution or more restrictive values. Unit is in radians, not degrees.
"""
Foundation.ShipDef.Galaxy.dTechs = {
	'Partially Distributed Shields': {"Shield Transfer Ratio": 1, "Max Percentage Damage": 2, "Collapse Threshold": 0.25, "Max Radians": 2.094395}
}
"""
from bcdebug import debug

import App
import FoundationTech
import math

from bcdebug import debug
import traceback

MODINFO = { "Author": "\"Alex SL Gato\" andromedavirgoa@gmail.com",
            "Version": "0.3",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

try:

	class PartDistribDef(FoundationTech.TechDef):

		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnDefense")

			if not pShip or (oYield and hasattr(oYield, "IsPhaseYield") and oYield.IsPhaseYield()):
				return

			pShields = pShip.GetShields()
			shieldHitBroken = 0

			if pEvent.IsHullHit() or not pShields or pShields.IsDisabled():
				return

			# orientation of the impact
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
			kPoint.Unitize()
			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()

			# get the nearest reference

			myXvalue = abs(kPoint.GetX())
			myYvalue = abs(kPoint.GetY())
			myZvalue = abs(kPoint.GetZ())

			distance = math.sqrt((myXvalue ** 2) + (myYvalue ** 2) + (myZvalue ** 2)) # THIS IS 1 IF UNITIZE WORKS TO-DO

			pointForward = App.TGPoint3_GetModelForward()
			pointBackward = App.TGPoint3_GetModelBackward()
			pointTop = App.TGPoint3_GetModelUp()
			pointBottom = App.TGPoint3_GetModelDown()
			pointRight = App.TGPoint3_GetModelRight()
			pointLeft = App.TGPoint3_GetModelLeft()
			lReferencias = [pointForward, pointBackward, pointTop, pointBottom, pointLeft, pointRight]

			listaCercanos = [None, None, None, None, None, None]

			i = 0
			for pPunto in lReferencias:
				pPunto.Subtract(kPoint)
				listaCercanos[i] = (pPunto.Length(), i)
				i = i + 1

			listaCercanos.sort()

			if listaCercanos[0] == None or listaCercanos[0][0] == None or listaCercanos[0][1] == None:
				return

			# Heal damage done on the shield
			shieldDir = listaCercanos[0][1]
			fCurr = pShields.GetCurShields(shieldDir)
			fMax = pShields.GetMaxShields(shieldDir)
			fNew = self.adjustShieldPower(fCurr, fMax, fDamage)
			pShields.SetCurShields(shieldDir, fNew)

			# Consider shield fields that can distribute the damage, and deal newly distributed damage according to distance and angle
			ignoreDistancePastThis = 2.0 * math.sin(math.pi/3.0) # with r=1 things simplify a lot 2 * r * sin (alpha/2)
			shieldTransferRatio = 1 # How much difference with respect to base (more muliplication equals more notable reduction). The lower, the less pronunced absorb difference between shields.
			maxPercentageDamage = 2 # How much percentage of the damage is absorbed in a max hit - by default it's 2, for 2/6ths on the best case.
			collapseLimit = 0.25 # limit before not considering shield redistribution

			if pInstance.__dict__.has_key("Partially Distributed Shields"):
				if pInstance.__dict__["Partially Distributed Shields"].has_key("Shield Transfer Ratio"):
					shieldTransferRatio = pInstance.__dict__["Partially Distributed Shields"]["Shield Transfer Ratio"]
				
				if pInstance.__dict__["Partially Distributed Shields"].has_key("Max Percentage Damage"):
					maxPercentageDamage = pInstance.__dict__["Partially Distributed Shields"]["Max Percentage Damage"]

				if pInstance.__dict__["Partially Distributed Shields"].has_key("Collapse Threshold"):
					collapseLimit = pInstance.__dict__["Partially Distributed Shields"]["Collapse Threshold"]
					if collapseLimit < 0.0:
						collapseLimit = 0.0

				if pInstance.__dict__["Partially Distributed Shields"].has_key("Max Radians"):
					if pInstance.__dict__["Partially Distributed Shields"]["Max Radians"] > math.pi:
						pInstance.__dict__["Partially Distributed Shields"]["Max Radians"] = math.pi
					ignoreDistancePastThis = abs(2.0 * math.sin(pInstance.__dict__["Partially Distributed Shields"]["Max Radians"]/2.0))

			numAvailableShields = 1
			for shieldField in listaCercanos: # All shields included, naturally
				shieldDir = shieldField[1]
				fCurr = pShields.GetCurShields(shieldDir)
				fMax = pShields.GetMaxShields(shieldDir)
				if fCurr/fMax > collapseLimit:
					numAvailableShields = numAvailableShields +1

			if numAvailableShields > 6: # done on purpose, so it works both both for equal distances to all shields where all damage is distributed equally, and when distances are not equal, in which case the furthest one does not count
				numAvailableShields == 6


			if distance == 0.0: # Absolute hit on the center of the shields, somehow
				for shieldField in listaCercanos: # All shields included, naturally
					shieldDir = shieldField[1]
					fCurr = pShields.GetCurShields(shieldDir)
					fMax = pShields.GetMaxShields(shieldDir)
					if fCurr/fMax <= collapseLimit and numAvailableShields > 0:		
						pShields.SetCurShields(shieldDir, self.adjustShieldPower(fCurr, fMax, -fDamage/numAvailableShields) )

				return			
			
			for shieldField in listaCercanos:
				shieldDir = shieldField[1]
				distanceField = shieldField[0]
				#if shieldDir == listaCercanos[-1][1] and distanceField > listaCercanos[-2][0] and distanceField > ignoreDistancePastThis:
				#	return
				fCurr = pShields.GetCurShields(shieldDir)
				fMax = pShields.GetMaxShields(shieldDir)
				if fCurr/fMax >= collapseLimit and numAvailableShields > 0:
					distributedDamage = 0
					#print "shield DAMAGING for shield before ", shieldDir,":", fCurr
					if distanceField == 0.0: # Absolute hit on the center of this shield, so we know it must deal a third of the damage on the best circumstances and all the damage in the worst case
						distributedDamage =  maxPercentageDamage * fDamage / (numAvailableShields)

					else:
	
						#print "partial hit - recalculating damage for shield ", shieldDir, " - distanceField <= ignoreDistancePastThis:", distanceField, "<=", ignoreDistancePastThis
						if distanceField <= ignoreDistancePastThis: # knowing we are correctly using this, then... I mean with current code it could be left to allow distance up to 2, but I don't want the shield on the other side to be drained normally

							reductionDmg = math.asin(distanceField/2.0) * 1.275 * shieldTransferRatio # combination of knowing the radians and adjusting so at pi/2 radians the damage is already reduced to 1/6th
							distributedDamage = fDamage * ( maxPercentageDamage - reductionDmg) / (numAvailableShields)
						#else:
						#	print "I IGNORE SHIELD ", shieldDir

					distributedDamage = self.adjustShieldPower(fCurr, fMax, -distributedDamage)
					pShields.SetCurShields(shieldDir, distributedDamage)

					#print "shield DAMAGING for shield AFTER ", shieldDir,":", distributedDamage


		def adjustShieldPower(self, fCurr, fMax, fDamage):
			actualAmount = fCurr + fDamage
			if actualAmount > fMax:
				actualAmount = fMax
			elif actualAmount < 0:
				actualAmount = 0

			return actualAmount	

		def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnBeamDefense")
			#if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Multivectral Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnPulseDefense")
			#if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Multivectral Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnTorpDefense")
			#if App.g_kSystemWrapper.GetRandomNumber(100) <= pInstance.__dict__['Multivectral Shields']:
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		# TODO:  Make this an activated technology
		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
			pInstance.lPulseDefense.insert(0, self)
			pInstance.lBeamDefense.insert(0, self)
			# print 'Attaching Partially Distributed Shields to', pInstance, pInstance.__dict__

		# def Activate(self):
		# 	FoundationTech.oWeaponHit.Start()
		# def Deactivate(self):
		# 	FoundationTech.oWeaponHit.Stop()

	def NiPoint3ToTGPoint3(p):
		debug(__name__ + ", NiPoint3ToTGPoint3")
		kPoint = App.TGPoint3()
		kPoint.SetXYZ(p.x, p.y, p.z)
		return kPoint

	oPartDistrib = PartDistribDef('Partially Distributed Shields')

except:
	print "Something went wrong wih Partially Distributed Shields technology"
	traceback.print_exc()