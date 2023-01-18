import Foundation
MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

TimeLord = Foundation.RaceDef('TimeLord', 'TimeLord')

class TimeLordShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = TimeLord
		Foundation.ShipDef.__init__(self, abbrev, species, dict)