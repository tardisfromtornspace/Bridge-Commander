import App
import Foundation



# Belamir
abbrev = 'Belamir'
iconName = 'Transwarp Excalibur'
longName = 'USS Belamir'
shipFile = 'Belamir' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Excalibur"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'Excalibur Pack',
	'author': 'DFS',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Belamir = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Belamir.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

# DFS, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Belamir.desc = 'USS Belamir(NCC-91017)'

if menuGroup:           Foundation.ShipDef.Belamir.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Belamir.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def BelamirIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/BelamirID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/BelamirID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/BelamirID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/BelamirID2_specular.tga"]]}
	return retval

Foundation.ShipDef.Belamir.__dict__["SDT Entry"] = BelamirIDSwap



# Cochrene
abbrev = 'Cochrene'
iconName = 'Transwarp Excalibur'
longName = 'USS Cochrene'
shipFile = 'Cochrene' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Excalibur"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'Excalibur Pack',
	'author': 'DFS',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Cochrene = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Cochrene.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

# DFS, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Cochrene.desc = 'USS Cochrene(NCC-96402)'

if menuGroup:           Foundation.ShipDef.Cochrene.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Cochrene.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def CochreneIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/CochreneID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/CochreneID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/CochreneID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/CochreneID2_specular.tga"]]}
	return retval

Foundation.ShipDef.Cochrene.__dict__["SDT Entry"] = CochreneIDSwap



# Kirkland
abbrev = 'Kirkland'
iconName = 'Transwarp Excalibur'
longName = 'USS Kirkland'
shipFile = 'Kirkland' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
SubMenu = "Excalibur"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'Excalibur Pack',
	'author': 'DFS',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}

Foundation.ShipDef.Kirkland = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Kirkland.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

# DFS, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Kirkland.desc = 'USS Kirkland(NCC-32584)'

if menuGroup:           Foundation.ShipDef.Kirkland.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Kirkland.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def KirklandIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/KirklandID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/KirklandID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/KirklandID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/KirklandID2_specular.tga"]]}
	return retval

Foundation.ShipDef.Kirkland.__dict__["SDT Entry"] = KirklandIDSwap