import Foundation

oMagmarianRace = Foundation.RaceDef("Magmarian", "Magmarian")

class MagmarianShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oMagmarianRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 85.0, 0.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 25.0, 0.0)

Foundation.MagmarianRace = oMagmarianRace
Foundation.MagmarianShipDef = MagmarianShipDef
