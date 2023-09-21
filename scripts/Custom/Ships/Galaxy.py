from bcdebug import debug
import Foundation
import F_FedAttackLightCruiser


abbrev = Foundation.ShipDef.Galaxy.abbrev
species = Foundation.ShipDef.Galaxy.species
dict = Foundation.ShipDef.Galaxy.__dict__

Foundation.ShipDef.Galaxy = F_FedAttackLightCruiser.FedAttackLightCruiserAI(abbrev, species, dict)

Foundation.ShipDef.Galaxy.sBridge = 'GalaxyBridge'
Foundation.ShipDef.Galaxy.fMaxWarp = 9.6


