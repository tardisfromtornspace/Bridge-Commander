import Foundation

oWaythaeonRace = Foundation.RaceDef("Waythaeon", "Waythaeon")

class WaythaeonShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oWaythaeonRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (70.0, 190.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (70.0, 190.0, 255.0)

Foundation.WaythaeonRace = oWaythaeonRace
Foundation.WaythaeonShipDef = WaythaeonShipDef
