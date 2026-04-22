import Foundation

oFut29thCBorgRace = Foundation.RaceDef("Fut29thCBorg", "Fut29thCBorg")

class Fut29thCBorgShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oFut29thCBorgRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (75.0, 135.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 255.0, 250.0)

Foundation.Fut29thCBorgRace = oFut29thCBorgRace
Foundation.Fut29thCBorgShipDef = Fut29thCBorgShipDef
