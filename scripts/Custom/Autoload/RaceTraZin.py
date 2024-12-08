import Foundation

oTraZinRace = Foundation.RaceDef("TraZin", "TraZin")

class TraZinShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTraZinRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (10.0, 255.0, 65.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (40.0, 0.0, 255.0)

Foundation.TraZinRace = oTraZinRace
Foundation.TraZinShipDef = TraZinShipDef
