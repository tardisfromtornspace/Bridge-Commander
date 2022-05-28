from bcdebug import debug
import App
import BaseAI
from Custom.GalaxyCharts.GalacticWarSimulator import *

#######################################################################################################################################################
class FleetChaseEnemies(BaseAI.BaseAI):
	def __init__(self, pCodeAI):
		# Parent class init first.
		debug(__name__ + ", __init__")
		BaseAI.BaseAI.__init__(self, pCodeAI)

		# Set default values for parameters that have them.
		self.SetupDefaultParams()
		self.SetRequiredParams()
		self.SetExternalFunctions()

		# Save a reference to our module, so the module isn't
		# unloaded unexpectedly.
		self.pModule = __import__(__name__)
		
		self.sDestination = ""

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
		if pLeadShip != None and pLeadShip.GetObjID() == pShip.GetObjID():
			pTravel = App.g_kTravelManager.GetTravel(pShip)
			if pTravel != None and pTravel.IsTravelling() == 1:
				return App.ArtificialIntelligence.US_ACTIVE

			pSet = pShip.GetContainingSet()
			if pSet == None:
				return App.ArtificialIntelligence.US_DONE

			if self.sDestination != "":
				if pSet.GetRegionModule() == self.sDestination:
					pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": has arrived in set to chase enemy ships.")
					self.sDestination = ""
					return App.ArtificialIntelligence.US_DONE

			pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is checking to chase enemy ships.")
			pRegion = pSet.GetRegion()
			if pRegion == None:
				return App.ArtificialIntelligence.US_DONE
			iShipSideInBattle = pRegion.RegionBattle.IsShipInBattle(pShip)

			if pRegion.RegionBattle.IsBattleOn() == 1 and iShipSideInBattle != pRegion.RegionBattle.NOT_IN_BATTLE:
				for pShipObj in pSet.GetClassObjectList(App.CT_SHIP):
					if not pShipObj.IsDying() and not pShipObj.IsDead():
						iShipObjSide = pRegion.RegionBattle.IsShipInBattle(pShipObj)
						if iShipObjSide != pRegion.RegionBattle.NOT_IN_BATTLE and iShipObjSide != iShipSideInBattle:
							# there is enemy ships in our current set, don't travel anywhere.
							pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": cancelling, there still enemies in our set.")
							return App.ArtificialIntelligence.US_DONE

				# check others sets in this system for enemy ships.
				for pSetPlug in pRegion.GetAllSets():
					pSetObj = pSetPlug.GetSetObj()
					if pSetObj != None and pSetObj.GetRegionModule() != pSet.GetRegionModule():
						for pShipObj in pSetObj.GetClassObjectList(App.CT_SHIP):
							iShipObjSide = pRegion.RegionBattle.IsShipInBattle(pShipObj)
							if iShipObjSide != pRegion.RegionBattle.NOT_IN_BATTLE and iShipObjSide != iShipSideInBattle:
								# there is enemy ships in this set. Go to it.
								App.g_kTravelManager.EngageTravelToOfShip( pShip, pSetObj.GetRegionModule() )
								pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": OK going to chase enemy ships to: "+pSetObj.GetRegionModule())
								self.sDestination = pSetObj.GetRegionModule()
								#return App.ArtificialIntelligence.US_DONE
		else:
			# We are the lead or we don't have one...  Stop this AI.
			return App.ArtificialIntelligence.US_DONE

		return App.ArtificialIntelligence.US_ACTIVE


