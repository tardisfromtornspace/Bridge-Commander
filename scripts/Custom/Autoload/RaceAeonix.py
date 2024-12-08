import Foundation

oAeonixRace = Foundation.RaceDef("Aeonix", "Aeonix")

class AeonixShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oAeonixRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 0.0, 75.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 0.0, 75.0)

Foundation.AeonixRace = oAeonixRace
Foundation.AeonixShipDef = AeonixShipDef
