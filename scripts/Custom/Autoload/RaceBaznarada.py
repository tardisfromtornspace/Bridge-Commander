import App
import Foundation
from bcdebug import debug

oBaznaradaRace = Foundation.RaceDef("Baznarada", "Bnar")

class BaznaradaShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oBaznaradaRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 0.0, 0.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 0.0, 0.0)

Foundation.BaznaradaRace = oBaznaradaRace
Foundation.BaznaradaShipDef = BaznaradaShipDef

