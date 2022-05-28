#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Excalibur"
iconName = "Excalibur"
longName = "USS Excalibur"
shipFile = "Excalibur"
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
SubMenu = "Excalibur"
species = App.SPECIES_SOVEREIGN
credits = {
	'modName': 'Excalibur Pack',
	'author': 'DFS',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
Foundation.ShipDef.Excalibur = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Excalibur.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

Foundation.ShipDef.Excalibur.desc = "The Excalibur-class was a Federation battleship that entered service in the late 24th century. In this case is the USS Excalibur (NX-90000)."


if menuGroup:           Foundation.ShipDef.Excalibur.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Excalibur.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
def ExcaliburIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/ExcaliburID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/ExcaliburID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/ExcaliburID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/ExcaliburID2_specular.tga"]]}
	return retval

Foundation.ShipDef.Excalibur.__dict__["SDT Entry"] = ExcaliburIDSwap



# Avalon
abbrev = 'Avalon'
iconName = 'Excalibur'
longName = 'USS Avalon'
shipFile = 'Avalon' 
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

Foundation.ShipDef.Avalon = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
Foundation.ShipDef.Avalon.dTechs = {
	'Breen Drainer Immune': 0,
	'Regenerative Shields': 10,
	'Multivectral Shields': 20,
}

# DFS, you need to edit the next line. You can add the description between the '' signs. An Enter is \n
Foundation.ShipDef.Avalon.desc = 'USS Avalon(NCC-93485)'

if menuGroup:           Foundation.ShipDef.Avalon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Avalon.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]

def AvalonIDSwap(self):
	retval = {"Textures": [["excalibur01", "data/models/SharedTextures/FedShips/Excalibur/AvalonID1_glow.tga"], ["excalibur03", "data/models/SharedTextures/FedShips/Excalibur/AvalonID2_glow.tga"], ["excalibur01_specular", "data/models/SharedTextures/FedShips/Excalibur/AvalonID1_specular.tga"], ["excalibur03_specular", "data/models/SharedTextures/FedShips/Excalibur/AvalonID2_specular.tga"]]}
	return retval

Foundation.ShipDef.Avalon.__dict__["SDT Entry"] = AvalonIDSwap
