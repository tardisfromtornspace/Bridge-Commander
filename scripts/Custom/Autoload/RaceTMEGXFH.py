import Foundation

oTMEGXFHRace = Foundation.RaceDef("TMEGXFH", "EGXFH")

class TMEGXFHShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTMEGXFHRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (10.0, 175.0, 25.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 0.0, 0.0)

Foundation.TMEGXFHRace = oTMEGXFHRace
Foundation.TMEGXFHShipDef = TMEGXFHShipDef
