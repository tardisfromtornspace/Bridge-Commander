import App
from bcdebug import debug
import Foundation

MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

oTMEGhostShip = Foundation.RaceDef('TMEGhostShip', 'TMEGhostShip')

class oRaceTMEGhostShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = oTMEGhostShip
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
	def OverrideWarpFXColor(self, *args):
		return (255.0, 255.0, 255.0)

Foundation.TMEGhostShip = oTMEGhostShip
Foundation.TMEGhostShipDef = oRaceTMEGhostShipDef