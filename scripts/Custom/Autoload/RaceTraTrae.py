import Foundation

oTraTraeRace = Foundation.RaceDef("TraTrae", "TraTrae")

class TraTraeShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTraTraeRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (165.0, 0.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 140.0, 35.0)

Foundation.TraTraeRace = oTraTraeRace
Foundation.TraTraeShipDef = TraTraeShipDef
