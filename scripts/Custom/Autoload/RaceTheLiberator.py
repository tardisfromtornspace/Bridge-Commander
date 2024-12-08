import Foundation

oTheLiberatorRace = Foundation.RaceDef("TheLiberator", "TheLiberator")

class TheLiberatorShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTheLiberatorRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 130.0, 165.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (215.0, 130.0, 255.0)

Foundation.TheLiberatorRace = oTheLiberatorRace
Foundation.TheLiberatorShipDef = TheLiberatorShipDef
