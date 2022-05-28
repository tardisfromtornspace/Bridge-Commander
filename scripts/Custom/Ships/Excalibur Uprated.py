import App
import Foundation



# ArchangelA
abbrev = 'ArchangelA'
iconName = 'Excalibur'
longName = 'USS Archangel-A'
shipFile = 'ArchangelA' 
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

Foundation.ShipDef.ArchangelA = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.ArchangelA.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

# DFS, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.ArchangelA.desc = 'USS ArchangelA(NCC-85808-A)'

if menuGroup:           Foundation.ShipDef.ArchangelA.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.ArchangelA.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def ArchangelAIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/ArchangelAID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/ArchangelAID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/ArchangelAID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/ArchangelAID2_specular.tga"]]}
	return retval

Foundation.ShipDef.ArchangelA.__dict__["SDT Entry"] = ArchangelAIDSwap



# Ascension
abbrev = 'Ascension'
iconName = 'Excalibur'
longName = 'USS Ascension'
shipFile = 'Ascension' 
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

Foundation.ShipDef.Ascension = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Ascension.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

# DFS, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Ascension.desc = 'USS Ascension(NCC-97566)'

if menuGroup:           Foundation.ShipDef.Ascension.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Ascension.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AscensionIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/AscensionID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/AscensionID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/AscensionID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/AscensionID2_specular.tga"]]}
	return retval

Foundation.ShipDef.Ascension.__dict__["SDT Entry"] = AscensionIDSwap