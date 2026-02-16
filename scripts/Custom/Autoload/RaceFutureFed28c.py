import Foundation

FutureFed28c = Foundation.RaceDef("FutureFed28c", "FutureFed28c")

class FutureFed28cShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = FutureFed28c
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (155.0, 140.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 200.0, 255.0)

Foundation.FutureFed28cRace = FutureFed28c
Foundation.FutureFed28cShipDef = FutureFed28cShipDef
