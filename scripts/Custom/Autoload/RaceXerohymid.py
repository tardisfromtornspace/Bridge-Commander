import Foundation

oXerohymidRace = Foundation.RaceDef("Xerohymid", "Xerohymid")

class XerohymidShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oXerohymidRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (200.0, 200.0, 200.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (160.0, 255.0, 130.0)

Foundation.XerohymidRace = oXerohymidRace
Foundation.XerohymidShipDef = XerohymidShipDef
