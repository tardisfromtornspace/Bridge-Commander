import Foundation

oInvertedTradoRace = Foundation.RaceDef("InvertedTrado", "InvertedTrado")

class InvertedTradoShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oInvertedTradoRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (225.0, 255.0, 0.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (250.0, 185.0, 135.0)

Foundation.InvertedTradoRace = oInvertedTradoRace
Foundation.InvertedTradoShipDef = InvertedTradoShipDef
