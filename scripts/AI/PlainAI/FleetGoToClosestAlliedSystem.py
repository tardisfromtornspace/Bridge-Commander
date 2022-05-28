from bcdebug import debug
import App
import BaseAI
from Custom.GalaxyCharts.GalacticWarSimulator import *

#######################################################################################################################################################
class FleetGoToClosestAlliedSystem(BaseAI.BaseAI):
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
			#start by checking our current region for allied dockable bases.
			pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is proceeding to check for close allied systems.")
			sShipRace = GetShipRaceByWarSim(pShip)
			pCurrentSet = pShip.GetContainingSet()
			if pCurrentSet == None:
				return App.ArtificialIntelligence.US_DONE
			pCurrentRegion = pCurrentSet.GetRegion()
			if pCurrentRegion == None:
				return App.ArtificialIntelligence.US_DONE
			if sShipRace == pCurrentRegion.GetControllingEmpire() or AreRacesAllied(sShipRace, pCurrentRegion.GetControllingEmpire()) == 1:
				#we're already on an allied system... no need for travelling.
				pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": cancelling, is already on a allied system.")
				return App.ArtificialIntelligence.US_DONE

			# we're on an enemy or neutral system... most likely a neutral since this PlainAI should only be called in that case lol
			# anyway, find the closest allied system and travel to it.
			lAlliedRaces = GetAlliedRacesOf(sShipRace)
			lAlliedRaces.insert(0, sShipRace)
			fClosestDist = 1e+10
			pClosestRegion = None
			for sRace in lAlliedRaces:
				pRaceObj = GetRaceClassObj(sRace)
				for pRegion in pRaceObj.GetSystems():
					if pRegion.GetName() != pCurrentRegion.GetName():
						vInLoc = pCurrentRegion.GetLocation()
						vGoLoc = pRegion.GetLocation()
						fDist = 1e+10
						if vInLoc != "DEFAULT" and vGoLoc != "DEFAULT":
							vDist = App.NiPoint2(vGoLoc.x - vInLoc.x, vGoLoc.y - vInLoc.y)
							fDist = vDist.Length()
						if fDist < fClosestDist:
							#closer region acquired, update 'closest' variables.
							fClosestDist = fDist
							pClosestRegion = pRegion
			if pClosestRegion != None:
				pBorderSet = pClosestRegion.GetBorderSet()
				if pBorderSet:
					App.g_kTravelManager.EngageTravelToOfShip( pShip, pBorderSet.GetScriptFile() )
					pFleet.Logger.LogString("WarAI_"+pShip.GetName()+": is engaging travel to system: "+pClosestRegion.GetName())
				return App.ArtificialIntelligence.US_DONE
		else:
			# We are the lead or we don't have one...  Stop this AI.
			return App.ArtificialIntelligence.US_DONE

		return App.ArtificialIntelligence.US_ACTIVE
