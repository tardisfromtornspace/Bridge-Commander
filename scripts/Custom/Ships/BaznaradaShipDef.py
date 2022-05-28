import Foundation
import BaznaradaRace

class BaznaradaShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = BaznaradaRace.oBaznaradaRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self):
        return (255.0, 0.0, 0.0)
	
    def OverridePlasmaFXColor(self):
        return (255.0, 0.0, 0.0)
