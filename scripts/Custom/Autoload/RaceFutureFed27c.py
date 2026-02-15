import Foundation

oFutureFed27cRace = Foundation.RaceDef("FutureFed27c", "FutureFed27c")

class FutureFed27cShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oFutureFed27cRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (40.0, 85.0, 245.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (235.0, 145.0, 255.0)

Foundation.FutureFed27cRace = oFutureFed27cRace
Foundation.FutureFed27cShipDef = FutureFed27cShipDef
