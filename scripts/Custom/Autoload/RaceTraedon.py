import Foundation

oTraedonRace = Foundation.RaceDef("Traedon", "Traedon")

class TraedonShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oTraedonRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (255.0, 255.0, 0.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (255.0, 255.0, 0.0)

Foundation.TraedonRace = oTraedonRace
Foundation.TraedonShipDef = TraedonShipDef
