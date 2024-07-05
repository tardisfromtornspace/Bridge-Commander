import App
import Foundation
from bcdebug import debug

MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

CosmosASTO = Foundation.RaceDef('CosmosASTO', 'CosmosASTO')

class CosmosASTOShipDef(Foundation.ShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = CosmosASTO
		Foundation.ShipDef.__init__(self, abbrev, species, dict)

Foundation.CosmosASTO = CosmosASTO
Foundation.CosmosASTOShipDef = CosmosASTOShipDef