import App
import Foundation
from bcdebug import debug

oRaceMESystemsAlliance = Foundation.RaceDef("ME Systems Alliance", "ME Systems Alliance")
Foundation.RaceMESystemsAlliance = oRaceMESystemsAlliance

class MESystemsAllianceShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = Foundation.RaceMESystemsAlliance
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (80.0, 80.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (112.0, 142.0, 255.0)

Foundation.MESystemsAllianceShipDef = MESystemsAllianceShipDef

