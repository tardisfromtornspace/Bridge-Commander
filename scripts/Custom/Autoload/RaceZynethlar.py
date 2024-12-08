import Foundation

oZynethlarRace = Foundation.RaceDef("Zynethlar", "Zynethlar")

class ZynethlarShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oZynethlarRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 0.0, 0.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (225.0, 225.0, 255.0)

Foundation.ZynethlarRace = oZynethlarRace
Foundation.ZynethlarShipDef = ZynethlarShipDef
