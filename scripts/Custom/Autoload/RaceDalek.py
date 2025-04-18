import App
import Foundation
from bcdebug import debug

MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

Dalek = Foundation.RaceDef('Dalek', 'Dalek')

class DalekShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = Dalek
		Foundation.ShipDef.__init__(self, abbrev, species, dict)

Foundation.Dalek = Dalek
Foundation.DalekShipDef = DalekShipDef