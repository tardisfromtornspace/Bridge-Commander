import Foundation

oVortchianRace = Foundation.RaceDef("Vortchian", "Vortchian")

class VortchianShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oVortchianRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (0.0, 0.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 0.0, 255.0)

Foundation.VortchianRace = oVortchianRace
Foundation.VortchianShipDef = VortchianShipDef
