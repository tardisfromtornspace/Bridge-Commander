import Foundation

oFutAOHRace = Foundation.RaceDef("FutAOH", "FutAOH")

class FutAOHShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oFutAOHRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 0.0, 135.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (140.0, 0.0, 255.0)

Foundation.FutAOHRace = oFutAOHRace
Foundation.FutAOHShipDef = FutAOHShipDef
