import Foundation
MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

CosmosASTO = Foundation.RaceDef('CosmosASTO', 'CosmosASTO')

class CosmosASTOShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = CosmosASTO
		Foundation.ShipDef.__init__(self, abbrev, species, dict)