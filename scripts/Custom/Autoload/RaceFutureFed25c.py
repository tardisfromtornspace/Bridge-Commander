import Foundation

FutureFed25c = Foundation.RaceDef("FutureFed25c", "FutureFed25c")

class FutureFed25cShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = FutureFed25c
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (120.0, 180.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (100.0, 150.0, 255.0)

Foundation.FutureFed25cRace = FutureFed25c
Foundation.FutureFed25cShipDef = FutureFed25cShipDef
