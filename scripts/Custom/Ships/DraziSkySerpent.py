#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DraziSkySerpent"
iconName = "DraziSkySerpent"
longName = "Sky Serpent"
shipFile = "DraziSkySerpent"
species = App.SPECIES_SHUTTLE
menuGroup = "Babylon 5"
playerMenuGroup = "Babylon 5"
SubMenu = "League of Non-Aligned Worlds"
SubSubMenu = "Drazi Freehold"
Foundation.ShipDef.DraziSkySerpent = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })
Foundation.ShipDef.DraziSkySerpent.dTechs = {
	'Simulated Point Defence' : { "Distance": 10.0, "InnerDistance": 3.0, "Effectiveness": 0.6, "LimitTurn": 4.5, "LimitSpeed": 65, "LimitDamage": "-150", "Period": 0.5, "MaxNumberTorps": 1, "Pulse": {"Priority": 1}}
}
Foundation.ShipDef.DraziSkySerpent.desc = "The Drazi Sky Serpent is one of the most powerful fighters found in the League of Non-Aligned Worlds and is credited with changing the view of many worlds' approach to fighter construction. An undamaged Sky Serpent is capable of surviving after taking a direct hit from Centauri blockade platform's energy weapons. It is possible for a single Sky Serpent to be berthed with a Drazi Sun-Hawk variant."

if menuGroup:           Foundation.ShipDef.DraziSkySerpent.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DraziSkySerpent.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
