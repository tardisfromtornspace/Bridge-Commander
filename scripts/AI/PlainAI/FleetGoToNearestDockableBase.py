from bcdebug import debug
import App
import BaseAI
from Custom.GalaxyCharts.GalacticWarSimulator import *

#######################################################################################################################################################
class FleetGoToNearestDockableBase(BaseAI.BaseAI):
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
			pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is checking for nearest dockable bases.")
			#start by checking our current region for allied dockable bases.
			sShipRace = GetShipRaceByWarSim(pShip)
			pCurrentSet = pShip.GetContainingSet()
			if pCurrentSet == None:
				return App.ArtificialIntelligence.US_DONE
			pCurrentRegion = pCurrentSet.GetRegion()
			if pCurrentRegion == None:
				return App.ArtificialIntelligence.US_DONE
			if pCurrentRegion.RegionBattle.IsBattleOn() == 0:
				if sShipRace == pCurrentRegion.GetControllingEmpire() or AreRacesAllied(sShipRace, pCurrentRegion.GetControllingEmpire()) == 1:
					for pSetPlug in pCurrentRegion.GetAllSets():
						pSetObj = pSetPlug.GetSetObj()
						if pSetObj != None:
							lDocks = GetDockableBasesOfSet(pSetObj)
							if len(lDocks) >= 1:
								#can dock in set, travel to it.
								App.g_kTravelManager.EngageTravelToOfShip( pShip, pSetObj.GetRegionModule() )
								pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is travelling to base in: "+pSetObj.GetRegionModule())
								return App.ArtificialIntelligence.US_DONE

			# no allied dockable bases in current region, find closest region to go to.
			lAlliedRaces = GetAlliedRacesOf(sShipRace)
			lAlliedRaces.insert(0, sShipRace)
			fClosestDist = 1e+10
			pClosestBaseSet = None
			for sRace in lAlliedRaces:
				pRaceObj = GetRaceClassObj(sRace)
				for pRegion in pRaceObj.GetSystems():
					if pRegion.RegionBattle.IsBattleOn() == 0 and pRegion.GetName() != pCurrentRegion.GetName():
						vInLoc = pCurrentRegion.GetLocation()
						vGoLoc = pRegion.GetLocation()
						fDist = 1e+10
						if vInLoc != "DEFAULT" and vGoLoc != "DEFAULT":
							vDist = App.NiPoint2(vGoLoc.x - vInLoc.x, vGoLoc.y - vInLoc.y)
							fDist = vDist.Length()
						if fDist < fClosestDist:
							for pSetPlug in pRegion.GetAllSets():
								pSetObj = pSetPlug.GetSetObj()
								if pSetObj != None:
									lDocks = GetDockableBasesOfSet(pSetObj)
									if len(lDocks) >= 1:
										#can dock in set, update 'closest' variables.
										fClosestDist = fDist
										pClosestBaseSet = pSetObj
										break
			if pClosestBaseSet != None:
				App.g_kTravelManager.EngageTravelToOfShip( pShip, pClosestBaseSet.GetRegionModule() )
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is travelling to base in other region: "+pClosestBaseSet.GetRegionModule())
				return App.ArtificialIntelligence.US_DONE
		else:
			# We are not the lead or we don't have one...  Stop this AI.
			return App.ArtificialIntelligence.US_DONE

		return App.ArtificialIntelligence.US_ACTIVE

