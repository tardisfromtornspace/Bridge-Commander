from bcdebug import debug
import App
import BaseAI
from Custom.GalaxyCharts.GalacticWarSimulator import *


import AI.PlainAI.IntelligentCircleObject

class CircleFleetLeadShip(AI.PlainAI.IntelligentCircleObject.IntelligentCircleObject):
	def __init__(self, pCodeAI):
		# Parent class init first.
		debug(__name__ + ", __init__")
		AI.PlainAI.IntelligentCircleObject.IntelligentCircleObject.__init__(self, pCodeAI)
	def Update(self):
		# we start by setting our target...
		debug(__name__ + ", Update")
		pShip = self.pCodeAI.GetShip()
		if (pShip == None):
			return App.ArtificialIntelligence.US_DONE
		bCanUpdate = 0
		pFleet = FleetManager.GetFleetOfShip(pShip)
		if pFleet != None:
			sLeadShipName = pFleet.GetLeadShipName()
			if sLeadShipName != "" and sLeadShipName != pShip.GetName():
				if self.pcFollowObjectName != sLeadShipName:
					self.pcFollowObjectName = sLeadShipName
				bCanUpdate = 1
		if bCanUpdate == 1:
			# and finishing calling our base update method to circle our target, in case we have it.
			#pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is proceeding to circle the lead ship.")
			return AI.PlainAI.IntelligentCircleObject.IntelligentCircleObject.Update(self)
		else:
			return App.ArtificialIntelligence.US_DONE


	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is proceeding to circle the lead ship.")

	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": has stopped to circle the lead ship...")