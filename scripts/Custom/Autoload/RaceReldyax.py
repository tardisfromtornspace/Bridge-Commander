import Foundation

oReldyaxRace = Foundation.RaceDef("Reldyax", "Reldyax")

class ReldyaxShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oReldyaxRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (230.0, 215.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (230.0, 215.0, 255.0)

Foundation.ReldyaxRace = oReldyaxRace
Foundation.ReldyaxShipDef = ReldyaxShipDef
