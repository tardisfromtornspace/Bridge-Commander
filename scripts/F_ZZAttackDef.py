# File: F (Python 1.5)

import Foundation
ShipDef = Foundation.ShipDef
Romulan = Foundation.Romulan

class ZZAttackDef(ShipDef):
    
    def __init__(self, abbrev, species, dict):
        dict['race'] = Romulan
        ShipDef.__init__(self, abbrev, species, dict)

    
    def StrFriendlyAI(self, *args):
        return 'ZZVeritexFAI'

    
    def StrEnemyAI(self, *args):
        return 'ZZVeritexEAI'


