import App
import Foundation
from bcdebug import debug

MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

FedProdigy = Foundation.RaceDef('FedProdigy', 'FedProdigy')
Foundation.FedProdigy = FedProdigy

class FedProdigyShipDef(Foundation.FedShipDef):
	def __init__(self, abbrev, species, dict):
		debug(__name__ + ", __init__")
		dict['race'] = Foundation.FedProdigy
		Foundation.ShipDef.__init__(self, abbrev, species, dict)
	def GetBridge(self, *args):
		debug(__name__ + ", GetBridge")
		return 'USSProtostarBridge'

Foundation.FedProdigyShipDef = FedProdigyShipDef