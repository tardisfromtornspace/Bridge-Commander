import Foundation

oZinthonianRace = Foundation.RaceDef("Zinthonian", "Zinthonian")

class ZinthonianShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oZinthonianRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 0.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 0.0, 255.0)

Foundation.ZinthonianRace = oZinthonianRace
Foundation.ZinthonianShipDef = ZinthonianShipDef
