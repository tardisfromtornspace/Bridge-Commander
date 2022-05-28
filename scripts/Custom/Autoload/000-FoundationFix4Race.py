# 000-FoundationFix4Race.by
# GPL - Defiant <erik@defiant.homedns.org>
#
# some overrides for Foundation.ShipDef()

import Foundation
MutatorDef = Foundation.MutatorDef
shipList = Foundation.shipList

def init(self, abbrev, species, dict = {}):
		self.abbrev = abbrev
		self.species = species
		self.race = None
		self.desc = ''
		self.hasTGLName = 0
		self.hasTGLDesc = 0
		self.menuGroup = None
		self.playerMenuGroup = None
		self.era = 0

		self.__dict__.update(dict)
		if not self.__dict__.has_key('iconName'):	self.iconName = abbrev
		if not self.__dict__.has_key('name'):		self.name = abbrev
		if not self.__dict__.has_key('shipFile'):	self.shipFile = abbrev
		if not self.__dict__.has_key('shipPrefix'):	self.shipPrefix = 'ships.'

		if dict.has_key('race'):
			self.race = dict['race']
			self.race.ships.append(self)

		self.sAttackModule = None
		
		self.friendlyDetails = [self.abbrev, self.name, self.StrFriendlyDestroyed(), self.StrFriendlyAI(), 'Friendly']
		self.enemyDetails = [self.abbrev, self.name, self.StrEnemyDestroyed(), self.StrEnemyAI(), 'Enemy']
		
		self.num = shipList.Register(self, abbrev)
		self.num = shipList.Register(self, abbrev)
		if shipList._keyList.has_key(self.name):
			self.friendlyDetails[2] = shipList[self.name].friendlyDetails[2]
			self.enemyDetails[2] = shipList[self.name].enemyDetails[2]

def RegisterQBPlayerShipMenu(self, group = None, mode = MutatorDef.QuickBattle):
		if not self.playerMenuGroup:
			self.playerMenuGroup = group
			
		if not shipList._keyList.has_key(self.abbrev):
			# If this failed, we know that there was an ImportError exception caught in ShipDef.__init__ -Dasher
			return
			
		if not group:
			group = self.MenuGroup()

		if mode.playerShipMenu.has_key(group):
			if mode.playerShipMenu[group][1].has_key(self.name):
				previous = mode.playerShipMenu[group][1][self.name]
				previous.shipFile = self.shipFile
				previous.iconName = self.iconName
				previous.species = self.species
				return

			mode.playerShipMenu[group][1][self.name] = self
			mode.playerShipMenu[group][0].append(self)
		else:
			mode.playerShipMenu[group] = ([ self ], { self.name: self } )
		if mode.elements.count(self) == 0:
			mode.elements.append(self)

def MenuGroup(self):
	return self.menuGroup

def GetShipFile(self):
	return self.shipFile

# thx for the override idea to Dasher42
if (int(Foundation.version[0:8]) <= 20041111):
    	Foundation.ShipDef.__init__ = init
	Foundation.ShipDef.MenuGroup = MenuGroup
	Foundation.ShipDef.GetShipFile = GetShipFile
	Foundation.ShipDef.RegisterQBPlayerShipMenu = RegisterQBPlayerShipMenu
