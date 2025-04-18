import Foundation

oHarmonyAscendantRace = Foundation.RaceDef("HarmonyAscendant", "HarmonyAscendant")

class HarmonyAscendantShipDef(Foundation.ShipDef):
    def __init__(self, abbrev, species, dict):
        dict['race'] = oHarmonyAscendantRace
        Foundation.ShipDef.__init__(self, abbrev, species, dict)
		
    def OverrideWarpFXColor(self, *args):
        return (135.0, 0.0, 255.0)
	
    def OverridePlasmaFXColor(self, *args):
        return (0.0, 0.0, 255.0)

Foundation.HarmonyAscendantRace = oHarmonyAscendantRace
Foundation.HarmonyAscendantShipDef = HarmonyAscendantShipDef
