import Foundation

oFutureFed25cRace = Foundation.RaceDef('FutureFed25c', 'Fed25c')

class FutureFed25cShipDef(Foundation.ShipDef):
    
    def __init__(self, abbrev, species, dict):
        dict['race'] = oFutureFed25cRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)

    
    def OverrideWarpFXColor(self, *args):
        return (10.0, 175.0, 255.0)

    
    def OverridePlasmaFXColor(self, *args):
        return (10.0, 175.0, 255.0)


Foundation.FutureFed25cRace = oFutureFed25cRace
Foundation.FutureFed25cShipDef = FutureFed25cShipDef