import Foundation

FutureFed29c = Foundation.RaceDef("FutureFed29c", "FutureFed29c")

class FutureFed29cShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = FutureFed29c
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (170.0, 80.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (60.0, 60.0, 255.0)

Foundation.FutureFed29cRace = FutureFed29c
Foundation.FutureFed29cShipDef = FutureFed29cShipDef
