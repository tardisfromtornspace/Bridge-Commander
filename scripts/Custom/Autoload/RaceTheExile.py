import Foundation

oTheExileRace = Foundation.RaceDef("TheExile", "TheExile")

class TheExileShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTheExileRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 255.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (35.0, 0.0, 75.0)

Foundation.TheExileRace = oTheExileRace
Foundation.TheExileShipDef = TheExileShipDef
