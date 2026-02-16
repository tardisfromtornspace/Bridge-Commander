import Foundation

FutureFed26c = Foundation.RaceDef("FutureFed26c", "FutureFed26c")

class FutureFed26cShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = FutureFed26c
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (0.0, 0.0, 51.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 25.0, 51.0)

Foundation.FutureFed26cRace = FutureFed26c
Foundation.FutureFed26cShipDef = FutureFed26cShipDef
