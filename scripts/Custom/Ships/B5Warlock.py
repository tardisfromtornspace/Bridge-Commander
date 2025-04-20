import App
import Foundation

# Usually you need only edit these seven lines
abbrev = 'B5Warlock'
iconName = 'B5Warlock'
longName = 'Warlock'
shipFile = 'B5Warlock' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
SubMenu = "Earth Alliance"
species = App.SPECIES_GALAXY
SubSubMenu = "Capital Ships"

# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'B5Warlock',   # The full name of your mod if applicable
	'author': '',              # Your name here
	'version': '1.0',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, Print a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.B5Warlock = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.B5Warlock.dTechs = {
	"AutoTargeting": { "Pulse": [3, 1] },
	'Defense Grid': 195,
	'Simulated Point Defence' : { "Distance": 60.0, "InnerDistance": 15.0, "Effectiveness": 0.8, "LimitTurn": 0.5, "LimitSpeed": 87, "LimitDamage": "650", "Period": 0.6, "MaxNumberTorps": 4, "Phaser": {"Priority": 1}, "Pulse": {"Priority": 2}},
	"Tachyon Sensors": 1.0
}

# Uncomment these if you have TGL  
# Foundation.ShipDef.B5Warlock.hasTGLName = 1
# Foundation.ShipDef.B5Warlock.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.B5Warlock.desc = "The Warlock-class destroyer is an advanced warship design produced by the Earth Alliance. Rushed into production immediately after the Earth Alliance Civil War, the Warlock-class destroyer incorporates some of the most advanced technology available. It was the first Earth Alliance ship to feature artificial gravity without rotating sections thanks to the technology the Minbari delivered. This allowed designers to greatly improve the Warlock's design. Among these improvements was the Warlock having greater speed and maneuverability compared to the older Omega-class destroyers. The Warlock's conventional particle thrust engines are supplemented by a pair of hybrid gravitic engines that, like the artificial gravity systems, are based on Minbari technology and propulsion theory but are designed and manufactured using Earth-based materials. The weapons systems aboard the Warlock feature a wide variety of offensive and defensive emplacements that include standard plasma cannons, railguns, and missiles. Perhaps the most notable armament is a pair of particle beam cannons originally designed for use on the Aegis orbital defense platforms that formed Earth's planetary defense grid. Prior to the development of the Warlock, the power requirements of these weapons were so high that only dedicated stationary platforms could accommodate them, and then only one unit per platform. Installing the cannons aboard the Warlock enabled a ship of the class to destroy multiple Drakh vessels with one shot each at the start of the Drakh War, and another to destroy a Centauri Vorchan-class with a single shot in a possible future battle. The ability to use such powerful weapons allows the Warlock to take ships from advanced races like Minbari with ease. In addition to human technology, an unknown Shadow device is buried somewhere in the Warlock's control systems. The exact purpose and function of this device is unclear."

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.B5Warlock.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.B5Warlock.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]