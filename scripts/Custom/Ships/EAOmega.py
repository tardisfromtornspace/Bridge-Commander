import Foundation
import App

# Usually you need only edit these seven lines
abbrev = 'EAOmega'
iconName = 'EAOmega'
longName = 'Omega Class'
shipFile = 'EAOmega' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_GALAXY
SubMenu = "Earth Alliance"
SubSubMenu = "Capital Ships"

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'EAOmega',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.EAOmega = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EAOmega.dTechs = {
	"AutoTargeting": { "Phaser": [3, 1] },
	'Defense Grid': 150,
	'Simulated Point Defence' : { "Distance": 40.0, "InnerDistance": 15.0, "Effectiveness": 0.8, "LimitTurn": 0.5, "LimitSpeed": 80, "LimitDamage": "650", "Period": 1.2, "MaxNumberTorps": 2, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 1.66
}

# Uncomment these if you have TGL
# Foundation.ShipDef.EAOmega.hasTGLName = 1
# Foundation.ShipDef.EAOmega.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.EAOmega.desc = 'The Omega class destroyer was an Earth Alliance warship, manufactured by Rocketdyne at the Neue Hanse Orbital Shipyard in Earth orbit. Following the Earth-Minbari War, it became the most powerful and ubiquitous capital ship of the Earthforce fleet and one of the strongest ships ever built of the younger races. A continuation of many of the design elements from the Nova-class dreadnought, the Omega possessed a large rotating section, allowing the crew to operate in gravity, eliminating the constant need for handholds and straps that often hindered the older zero gravity warships. Ships of the Omega class were equipped with a DX-419 tracking system, supposedly an improvement over the standard XB7 units used during the war, though several officers have noted that they never worked right. By 2261 the system had at least begun to be upgraded. During the Earth-Minbari War, Earth did not have any ships that could lock onto Minbari vessels, due to the stealth technology the Minbari possessed. However, Earth ships still had the firepower to damage Minbari cruisers. The Omega Class Destroyer was the first Earth ship capable of locking onto a Minbari ship. Another lesson learned from the Earth-Minbari War was that the solid beam weapons used by the Minbari had proven to be deadly effective. Taking this lesson in hand, the Omega´s cannons could fire both in pulse mode and in solid beam, allowing for more precise and accurate fire.'

# These register the ship with the QuickBattle menus.  Don't touch them!!!

if menuGroup:           Foundation.ShipDef.EAOmega.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAOmega.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]