from bcdebug import debug
import App
import BaseAI
from Custom.GalaxyCharts.GalacticWarSimulator import *

import Custom.GalaxyCharts.WarpIntercept

# We inherit from WarpIntercept (from GC) rather than the regular Intercept module from stock BC because the WarpIntercept will overwrite the regular
# intercept anyway, however i'm not sure if that will already be done when this is loaded... So doing it this way makes sure it works.
      
class InterceptFleetLeadShip(Custom.GalaxyCharts.WarpIntercept.WarpIntercept):
	def __init__(self, pCodeAI):
		# Parent class init first.
		debug(__name__ + ", __init__")
		Custom.GalaxyCharts.WarpIntercept.WarpIntercept.__init__(self, pCodeAI)
	def Update(self):
		# we start by setting our target
		debug(__name__ + ", Update")
		pShip = self.pCodeAI.GetShip()
		if pShip == None:
			return App.ArtificialIntelligence.US_DONE
		bCanUpdate = 0
		pFleet = FleetManager.GetFleetOfShip(pShip)
		if pFleet != None:
			sLeadShipName = pFleet.GetLeadShipName()
			if sLeadShipName != "" and sLeadShipName != pShip.GetName():
				if self.sTargetName != sLeadShipName:
					self.sTargetName = sLeadShipName
				bCanUpdate = 1
		if bCanUpdate == 1:
			# and finishing calling our base update method to intercept our target, in case we have it.
			#pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is intercepting lead ship.")
			return Custom.GalaxyCharts.WarpIntercept.WarpIntercept.Update(self)
		else:
			return App.ArtificialIntelligence.US_DONE

	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is proceeding to intercept the lead ship.")

	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": has stopped intercepting the lead ship...")