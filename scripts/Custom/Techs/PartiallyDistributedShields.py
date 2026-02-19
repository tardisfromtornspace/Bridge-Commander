#################################################################################################################
# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
#         PartiallyDistributedShields.py by Alex SL Gato
#         Version 0.42
#         19th February 2025
#         Based on scripts\ftb\Tech\Shields.py by MLeo Daalder, Apollo, Dasher, and the rest of the FoundationTechnologies team.
#         Special Thanks to USS Sovereign for telling me better tips to remove the need of a hardpoint-wise made-up axis.
#                          
#################################################################################################################
# What does this tech do: a variant of Multivectral shielding and Vree shields, but instead of uniforming all the shields with a chance, it distributes part of the conventional damage on a shield to the nearby ones (the furthest one is generally excluded) and doesn't try to do so on collapsed shields.
# Usage Example:  Add this to the dTechs attribute of your ShipDef, in the Ship plugin file, but modify the values accordingly to what you want, and for actual values since the following is just a general example
# NOTE: replace "Galaxy" by the proper abbrev when doing so.
# - "Shield Transfer Ratio": OPTIONAL this script uses a formula where by default the more you go to the sides, the less is transferred - with this you can tweak that to make the transfer less the higher the value - even try 0 for equal values, and negative values if you want for it to transfer more to the sides! Very high values can also be used to heal the other shields, if balanced properly with Max Percentage Damage field.
# - "Max Percentage Damage": OPTIONAL this states how much part of the damage the shield hit closest can receive (of course, if you use a positive or neutral value in the previous "Shield Transfer Ratio" field). The numbers input are then considered in sixths, that is, if you set it to 1, that shield will only receive 1/6th of the damage, if it's 2, 2/6ths, and so on. You can even try negatives if you so desire.
# - "Collapse Threshold": OPTIONAL how much you need to have the shields down to consider that shield collapsed. Default is 0.25, that is, shield integrity at 25%. Minimum before was considered 0%, but now you can set it in the engatives so it considers ONLY the facets that have reached or are below that threshold to redistribute.
# - "Always Heal Closest": OPTIONAL the shield that has been hit by a weapon will need to heal the damage first to redistribute it - however sometimes under certain thresholds you may not want to do that. typing 0 = yes, always heal (default); typing < 0, no, only when the current shield percentage is less than the collapse threshold. Any other value = only if the supposed value after heal multiplied by this value is greater or equal than the collapse threshold
# - "Max Radians": OPTIONAL advanced, it makes it consider how far it extends the redistribution - the recommended value is 2 * math.pi/3.0, but you can try to do math.pi for total shield redistribution or more restrictive values. Unit is in radians, not degrees.
# - "ModX", "ModY", "ModZ": OPTIONAL some vessels have weird shapes that generate oblong shield shapes that this script cannot take into account 100% accurately, so these values multiply the X (- left -> + right), Y (- aft -> + forward) and Z (- bottom -> + top) values to make their respective coordiante matter more. There are "Mod-X", "Mod-Y", "Mod-Z" which do exactly the same except when combined with the non-hyphen ones, then one handles the positive values and the - the negative ones; in case your shield bubble is something even weirder like an egg instead of an ellipsoid or if you want to make the shield distances be considered assymetrically.
# - "Emergency Redistribute Threshold": OPTIONAL if a facet is detected with a value equal or less than this threshold it will attempt to performa  full shield redistribution. Defualt is -1 (emergency redistribution disabled).
# - "Emergency Redistribute Chance": OPTIONAL if Emergency Redistribute threshold is reached, percent chance from 1 to 100 of actually happening. Default is 1 (1% chance).
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
            "Version": "0.42",
            "License": "LGPL",
            "Description": "Read the small title above for more info"
            }

try:

	class PartDistribDef(FoundationTech.TechDef):

		def OnDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnDefense")

			if not pShip or not pInstance or (oYield and hasattr(oYield, "IsPhaseYield") and oYield.IsPhaseYield()):
				return

			pShields = pShip.GetShields()
			shieldHitBroken = 0

			if not pShields or pShields.IsDisabled() or not pShields.IsOn():
				return

			if pEvent.IsHullHit():
				return

			fRadius = pEvent.GetRadius()
			fDamage = pEvent.GetDamage()

			# Consider shield fields that can distribute the damage, and deal newly distributed damage according to distance and angle
			ignoreDistancePastThis = 2.0 * math.sin(math.pi/3.0) # with r=1 things simplify a lot 2 * r * sin (alpha/2)
			shieldTransferRatio = 1 # How much difference with respect to base (more muliplication equals more notable reduction). The lower, the less pronunced absorb difference between shields.
			maxPercentageDamage = 2 # How much percentage of the damage is absorbed in a max hit - by default it's 2, for 2/6ths on the best case.
			collapseLimit = 0.25 # limit before not considering shield redistribution

			alwaysHealClosest = 0 # When the nearest shield is collapsed, do we want to heal the damage?
			emergencyThreshold = -1 # try to redistribute shields ala Multivectral shields if the threshold is too low?
			emergencyRedistributeChance = 1 # Chance of emergency redistributing

			sForwardScale = 1.0
			sBackwardScale = 1.0
			sTopScale = 1.0
			sBottomScale = 1.0
			sLeftScale = 1.0
			sRightScale = 1.0

			pIdict = pInstance.__dict__

			if pIdict.has_key("Partially Distributed Shields"):
				pIdictPDS = pIdict["Partially Distributed Shields"]
				if pIdictPDS.has_key("Shield Transfer Ratio"):
					shieldTransferRatio = pIdictPDS["Shield Transfer Ratio"]
				
				if pIdictPDS.has_key("Max Percentage Damage"):
					maxPercentageDamage = pIdictPDS["Max Percentage Damage"]

				if pIdictPDS.has_key("Collapse Threshold"):
					collapseLimit = pIdictPDS["Collapse Threshold"]

				if pIdictPDS.has_key("Emergency Redistribute Threshold"): # TO-DO CREATE THE CODE AND EXPLAIN
					emergencyThreshold = pIdictPDS["Emergency Redistribute Threshold"]

				if pIdictPDS.has_key("Emergency Redistribute Chance"):
					emergencyRedistributeChance = pIdictPDS["Emergency Redistribute Chance"]

				if pIdictPDS.has_key("Always Heal Closest"):
					alwaysHealClosest = -pIdictPDS["Always Heal Closest"]

				if pIdictPDS.has_key("Max Radians"):
					if pIdictPDS["Max Radians"] > math.pi:
						pIdict["Partially Distributed Shields"]["Max Radians"] = math.pi
					ignoreDistancePastThis = abs(2.0 * math.sin(pIdict["Partially Distributed Shields"]["Max Radians"]/2.0))

				hasDXmod = pIdictPDS.has_key("ModX")
				hasDmXmod = pIdictPDS.has_key("Mod-X")

				hasDYmod = pIdictPDS.has_key("ModY")
				hasDmYmod = pIdictPDS.has_key("Mod-Y")

				hasDZmod = pIdictPDS.has_key("ModZ")
				hasDmZmod = pIdictPDS.has_key("Mod-Z")

				if hasDXmod:
					sRightScale = pIdictPDS["ModX"]
					if not hasDmYmod:
						sLeftScale = sRightScale

				if hasDmXmod:
					sLeftScale = pIdictPDS["Mod-X"]
					if not hasDYmod:
						sRightScale = sLeftScale

				if hasDYmod:
					sForwardScale = pIdictPDS["ModY"]
					if not hasDmXmod:
						sBackwardScale = sForwardScale

				if hasDmYmod:
					sBackwardScale = pIdictPDS["Mod-Y"]
					if not hasDXmod:
						sForwardScale = sBackwardScale

				if hasDZmod:
					sTopScale = pIdictPDS["ModZ"]
					if not hasDmZmod:
						sBottomScale = sTopScale

				if hasDmZmod:
					sBottomScale = pIdictPDS["Mod-Z"]
					if not hasDZmod:
						sTopScale = sBottomScale

			# orientation of the impact
			kPoint = NiPoint3ToTGPoint3(pEvent.GetObjectHitPoint())
			kPoint.Unitize()

			# get the nearest reference

			myXvalue = kPoint.GetX()
			myYvalue = kPoint.GetY()
			myZvalue = kPoint.GetZ()

			#print "punto (", myXvalue, ",", myYvalue, ",", myZvalue, ")"

			myaXvalue = abs(kPoint.GetX())
			myaYvalue = abs(kPoint.GetY())
			myaZvalue = abs(kPoint.GetZ())

			distance = math.sqrt((myaXvalue ** 2) + (myaYvalue ** 2) + (myaZvalue ** 2))

			# Since shields are an ellipse and on this case redistribution really matters we have to consider stuff properly.
			kXMod = 1.0
			kYMod = 1.0
			kZMod = 1.0

			if myXvalue == myaXvalue:
				kXMod = sRightScale
			else:
				kXMod = sLeftScale
			if myYvalue == myaYvalue:
				kYMod = sForwardScale
			else:
				kYMod = sBackwardScale

			if myZvalue == myaZvalue:
				kZMod = sTopScale
			else:
				kZMod = sBottomScale

			kPoint.SetXYZ(myXvalue * kXMod, myYvalue * kYMod, myZvalue * kZMod)

			myX2value = kPoint.GetX() # TO-DO REMOVE
			myY2value = kPoint.GetY()
			myZ2value = kPoint.GetZ()

			#print "punto tras fix (", myX2value, ",", myY2value, ",", myZ2value, ")"

			kPoint.Unitize()

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

			numAvailableShields = 0
			emergencyRedistribute = 0
			totalEmRedis = 0
			for shieldField in listaCercanos: # All shields included, naturally
				shieldDir = shieldField[1]
				fCurr = pShields.GetCurShields(shieldDir)
				fMax = pShields.GetMaxShields(shieldDir)
				if fMax > 0:
					fPerc = fCurr/fMax
					itIsAvailable = 0
					if collapseLimit < 0.0:
						itIsAvailable = (fPerc <= -collapseLimit)
					else:
						itIsAvailable = (fPerc >= collapseLimit)

					if itIsAvailable:
						numAvailableShields = numAvailableShields +1
						totalEmRedis = totalEmRedis + fCurr

					emergencyCall = (fPerc <= emergencyThreshold)
					if emergencyCall:
						if not emergencyRedistribute:
							 emergencyRedistribute = (App.g_kSystemWrapper.GetRandomNumber(100) <= emergencyRedistributeChance)

			if numAvailableShields <= 0: # Naturally we cannot continue if there are no shields... wait then how did we not get a pEvent.IsHullHit()?
				return

			# Heal damage done on the shield
			shieldDirC = None
			fCMax = 0
			fCCurr = 0

			if not emergencyRedistribute:
				for i2 in range(i): # Fix for when a ship has different shield facets and some of them have no shields, the closest facet may not be the desired one!
					shieldiDir = listaCercanos[i2][1]
					fiCurr = pShields.GetCurShields(shieldiDir)
					fiMax = pShields.GetMaxShields(shieldiDir)
					if fDamage <= 0.0 or ((i2 + 1) == i):
						shieldDirC = shieldiDir
						fCCurr = fiCurr
						fCMax = fiMax
						break
					else:
						shieldiL = listaCercanos[i2][0]
						if fiMax > 0:
							shieldDirC = shieldiDir
							fCCurr = fiCurr
							fCMax = fiMax
							break

			closestGotHealed = -1
			if fCMax > 0:
				fNew = self.adjustShieldPower(fCCurr, fCMax, fDamage)
				fPerc = fCCurr/fCMax
				itIsAvailable = 0
				if collapseLimit < 0.0:
					itIsAvailable = (fPerc <= -collapseLimit)
				else:
					itIsAvailable = ((alwaysHealClosest == 0) or (fPerc > collapseLimit))
					if not itIsAvailable and alwaysHealClosest > 0:
						itIsAvailable = (fNew >= alwaysHealClosest * collapseLimit)
				if itIsAvailable:
					closestGotHealed = shieldiDir
					pShields.SetCurShields(shieldDirC, fNew)

					#print "closestGotHealed es ", closestGotHealed, " from ", fCCurr, "/", fCMax, " -> ", fNew, "/", fCMax

			if numAvailableShields > 6: # done on purpose, so it works both both for equal distances to all shields where all damage is distributed equally, and when distances are not equal, in which case the furthest one does not count
				numAvailableShields == 6

			#print "listaCercanos es ", listaCercanos, "numAvailableShields es ", numAvailableShields

			if distance == 0.0 or emergencyRedistribute: # Absolute hit on the center of the shields, somehow
				for shieldField in listaCercanos: # All shields included, naturally
					shieldDir = shieldField[1]
					fCurr = pShields.GetCurShields(shieldDir)
					fMax = pShields.GetMaxShields(shieldDir)
					if fMax > 0 and ((collapseLimit >= 0 and fCurr/fMax >= collapseLimit) or (collapseLimit >= 0 and fCurr/fMax <= -collapseLimit) or (shieldDir == closestGotHealed)):
						if emergencyRedistribute:
							pShields.SetCurShields(shieldDir, self.adjustShieldPower(0, fMax, totalEmRedis/numAvailableShields) )
						else:		
							pShields.SetCurShields(shieldDir, self.adjustShieldPower(fCurr, fMax, -fDamage/numAvailableShields) )

				return			
			else:
				for shieldField in listaCercanos:
					shieldDir = shieldField[1]
					distanceField = shieldField[0]

					fCurr = pShields.GetCurShields(shieldDir)
					fMax = pShields.GetMaxShields(shieldDir)
					if fMax > 0 and ((collapseLimit >= 0 and fCurr/fMax >= collapseLimit) or (collapseLimit >= 0 and fCurr/fMax <= -collapseLimit) or (shieldDir == closestGotHealed)):
						distributedDamage = 0
						#print "shield DAMAGING for shield before ", shieldDir,":", fCurr
						if distanceField == 0.0: # Absolute hit on the center of this shield, so we know it must deal a third of the damage on the best circumstances and all the damage in the worst case
							distributedDamage =  maxPercentageDamage * fDamage / (numAvailableShields)

						else:
							if distanceField <= ignoreDistancePastThis: # knowing we are correctly using this, then... I mean with current code it could be left to allow distance up to 2, but I don't want the shield on the other side to be drained normally unless told otherwise

								reductionDmg = math.asin(distanceField/2.0) * 1.275 * shieldTransferRatio # combination of knowing radians and adjusting so at pi/2 radians the damage is already reduced to 1/6th
								distributedDamage = fDamage * ( maxPercentageDamage - reductionDmg) / (numAvailableShields)

						distributedFDamage = self.adjustShieldPower(fCurr, fMax, -distributedDamage)
						pShields.SetCurShields(shieldDir, distributedFDamage)


		def adjustShieldPower(self, fCurr, fMax, fDamage):
			actualAmount = fCurr + fDamage
			if actualAmount > fMax:
				actualAmount = fMax
			elif actualAmount < 0:
				actualAmount = 0

			return actualAmount	

		def OnBeamDefense(self, pShip, pInstance, oYield, pEvent):
			debug(__name__ + ", OnBeamDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnPulseDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnPulseDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def OnTorpDefense(self, pShip, pInstance, pTorp, oYield, pEvent):
			debug(__name__ + ", OnTorpDefense")
			return self.OnDefense(pShip, pInstance, oYield, pEvent)

		def Attach(self, pInstance):
			debug(__name__ + ", Attach")
			pInstance.lTechs.append(self)
			pInstance.lTorpDefense.insert(0, self)		# Important to put shield-type weapons in the front
			pInstance.lPulseDefense.insert(0, self)
			pInstance.lBeamDefense.insert(0, self)
			# print 'Attaching ', __name__,".", self.name, " to ", pInstance, pInstance.__dict__

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