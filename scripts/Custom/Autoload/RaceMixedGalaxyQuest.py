import Foundation
MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

MixedGalaxyQuest = Foundation.RaceDef('MixedGalaxyQuest', 'MixedGalaxyQuest')

class MixedGalaxyQuestShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = MixedGalaxyQuest
		Foundation.ShipDef.__init__(self, abbrev, species, dict)