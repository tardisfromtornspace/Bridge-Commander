import App
import Foundation
from bcdebug import debug

oRaceMETurian = Foundation.RaceDef("ME Turian", "ME Turian")
Foundation.RaceMETurian = oRaceMETurian

class RaceMETurianShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = Foundation.RaceMETurian
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (80.0, 80.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (112.0, 142.0, 255.0)

Foundation.RaceMETurianShipDef = RaceMETurianShipDef

