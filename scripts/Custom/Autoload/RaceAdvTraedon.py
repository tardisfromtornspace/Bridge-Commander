import Foundation

oAdvTraedonRace = Foundation.RaceDef("AdvTraedon", "AdvTraedon")

class AdvTraedonShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oAdvTraedonRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 190.0, 0.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 190.0, 0.0)

Foundation.AdvTraedonRace = oAdvTraedonRace
Foundation.AdvTraedonShipDef = AdvTraedonShipDef
