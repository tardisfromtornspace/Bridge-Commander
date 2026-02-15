import Foundation

oDTTosRomRace = Foundation.RaceDef("DTTosRom", "DTTosRom")

class DTTosRomShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oDTTosRomRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (245.0, 235.0, 40.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (40.0, 245.0, 210.0)

Foundation.DTTosRomRace = oDTTosRomRace
Foundation.DTTosRomShipDef = DTTosRomShipDef
