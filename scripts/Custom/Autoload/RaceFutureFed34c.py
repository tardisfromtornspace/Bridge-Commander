import Foundation

FutureFed34c = Foundation.RaceDef("FutureFed34c", "FutureFed34c")

class FutureFed34cShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = FutureFed34c
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (60.0, 40.0, 175.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (185.0, 40.0, 245.0)

Foundation.FutureFed34cRace = FutureFed34c
Foundation.FutureFed34cShipDef = FutureFed34cShipDef
