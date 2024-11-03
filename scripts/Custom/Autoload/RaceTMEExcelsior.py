#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation
from bcdebug import debug

MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

TMEExcelsior = Foundation.RaceDef('TMEExcelsior', 'TMEExcelsior')

class TMEExcelsiorShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = TMEExcelsior
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
	def OverrideWarpFXColor(self, *args):
		return (255.0, 175.0, 0.0)

Foundation.TMEExcelsior = TMEExcelsior
Foundation.TMEExcelsiorShipDef = TMEExcelsiorShipDef