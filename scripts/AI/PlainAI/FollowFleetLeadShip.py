from bcdebug import debug
import App
import BaseAI
from Custom.GalaxyCharts.GalacticWarSimulator import *

#######################################################################################################################################################
class FollowFleetLeadShip(BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		# Parent class init first.
		debug(__name__ + ", __init__")
		BaseAI.BaseAI.__init__(self, pCodeAI)

		# Set default values for parameters that have them.
		self.SetupDefaultParams()
		self.SetRequiredParams()
		self.SetExternalFunctions()

		self.bCanLog = 1
		
		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)

	def GetNextUpdateTime(self):
		# return value in seconds
		debug(__name__ + ", GetNextUpdateTime")
		return 1.0

	def Update(self):
		debug(__name__ + ", Update")
		pShip = self.pCodeAI.GetShip()
		if pShip == None:
			return App.ArtificialIntelligence.US_DONE

		pLeadShip = None
		pFleet = FleetManager.GetFleetOfShip(pShip)
		if pFleet != None:
			pLeadShip = pFleet.GetLeadShipObj()
		if pLeadShip != None and pLeadShip.GetObjID() != pShip.GetObjID():
			#we gotta chase the lead ship
			if self.bCanLog == 1:
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is going to chase lead ship.")
				self.bCanLog = 0
			pTravel = App.g_kTravelManager.CreateChaser(pShip, pLeadShip)
			pChasedShip = pTravel.GetTarget()
			if pChasedShip == None or (pChasedShip != None and pChasedShip.GetObjID() != pLeadShip.GetObjID()):
				pTravel.SetTarget(pLeadShip)

			pSet = pShip.GetContainingSet()
			pLeadSet = pLeadShip.GetContainingSet()
			if pSet != None and pLeadSet != None:
				if pSet.GetRegionModule() == pLeadSet.GetRegionModule() and pTravel.IsTravelling() != 1:
					# we're in the same set than our lead ship, and are not travelling... Probably doesn't need this AI anymore.
					pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is already in same set than lead ship...")
					return App.ArtificialIntelligence.US_DONE
		else:
			# We are the lead or we don't have one...  Stop this AI.
			return App.ArtificialIntelligence.US_DONE

		return App.ArtificialIntelligence.US_ACTIVE

	def GotFocus(self):
		debug(__name__ + ", GotFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				self.bCanLog = 1

	def LostFocus(self):
		debug(__name__ + ", LostFocus")
		pShip = self.pCodeAI.GetShip()
		if pShip != None:
			pFleet = FleetManager.GetFleetOfShip(pShip)
			if pFleet != None:
				self.bCanLog = 1