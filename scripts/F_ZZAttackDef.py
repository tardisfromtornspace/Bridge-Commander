# File: F (Python 1.5)

import Foundation
ShipDef = Foundation.ShipDef
Federation = Foundation.Federation

class ZZAttackDef(ShipDef):
    
    def __init__(self, abbrev, species, dict):
        dict['race'] = Federation
        ShipDef.__init__(self, abbrev, species, dict)

    
    def StrFriendlyAI(self):
        return 'ZZVeritexFAI'

    
    def StrEnemyAI(self):
        return 'ZZVeritexEAI'


