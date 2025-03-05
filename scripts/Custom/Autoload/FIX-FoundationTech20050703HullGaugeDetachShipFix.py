# THIS FILE IS NOT SUPPORTED BY ACTIVISION
# THIS FILE IS UNDER THE LGPL FOUNDATION LICENSE AS WELL
# 5th March 2025
# VERSION 0.1
# By Alex SL Gato
# FoundationTech.py by Dasher and the Foundation Technologies team -> GaugeTechDef.DetachShip fix
#
# Changes: 
# - As of FoundationTech 20050703:
# -- GaugeTechDef.DetachShip does not properly include the pDisplays, meaning the Display cannot be changed if you detach a GaugeTechDef tech, for example Ablative Armour. This has been corrected on this patch.


from bcdebug import debug
import App
import FoundationTech
import Foundation
import traceback

necessaryToUpdate = 0
try:

	if hasattr(Foundation,"version"):
		if int(Foundation.version[0:8]) < 20250305: # we are gonna assume the 2025 version and previous versions lack this
			necessaryToUpdate = 1
	else:
		necessaryToUpdate = 1 # the oldest versions have a signatre, except maybe some prototypes	

except:
    print "Unable to find FoundationTech.py install"
    pass

if necessaryToUpdate:
	original1 = FoundationTech.GaugeTechDef.DetachShip

	def DetachShip(self, pShip, pInstance):
		# print 'GaugeTechDef.DetachShip', self.name
		debug(__name__ + ", DetachShip")
		if self in pInstance.lHealthGauge:
			pInstance.lHealthGauge.remove(self)

			if len(pInstance.lHealthGauge) > 0:
				if pInstance.pDisplay == None:
					if len(FoundationTech.dDisplays[pInstance.pShipID]) > 0:
						myDi = FoundationTech.dDisplays[pInstance.pShipID]
						if myDi != None:
							pInstance.pDisplay = FoundationTech.dDisplays[pInstance.pShipID][-1]
				if pInstance.pDisplay != None:
					pInstance.lHealthGauge[-1].SetGauge(pShip, pInstance, pInstance.pDisplay.GetHealthGauge())

			if len(pInstance.lHealthGauge) > 0 and pInstance.pDisplay != None:
				pInstance.lHealthGauge[-1].SetGauge(pShip, pInstance, pInstance.pDisplay.GetHealthGauge())
		pInstance.__dict__[self.GetSystemPointer()] = None

	if original1 != None:
		FoundationTech.GaugeTechDef.DetachShip = DetachShip
		print "Updated FoundationTech.GaugeTechDef Detach-related fixes"
