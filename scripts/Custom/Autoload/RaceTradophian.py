import Foundation

oTradophianRace = Foundation.RaceDef("Tradophian", "Tradophian")

class TradophianShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTradophianRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (10.0, 255.0, 65.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 255.0, 205.0)

Foundation.TradophianRace = oTradophianRace
Foundation.TradophianShipDef = TradophianShipDef
