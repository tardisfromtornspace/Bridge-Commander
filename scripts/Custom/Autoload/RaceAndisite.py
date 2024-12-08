import Foundation

oAndisiteRace = Foundation.RaceDef("Andisite", "Andisite")

class AndisiteShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oAndisiteRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (0.0, 255.0, 230.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 255.0, 230.0)

Foundation.AndisiteRace = oAndisiteRace
Foundation.AndisiteShipDef = AndisiteShipDef
