#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 16/04/2005                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'EAHyperion'
iconName = 'EAHyperion'
longName = 'Hyperion Class'
shipFile = 'EAHyperion' 
menuGroup = 'Babylon 5'
playerMenuGroup = 'Babylon 5'
species = App.SPECIES_GALAXY
SubMenu = "Earth Alliance"
SubSubMenu = "Capital Ships"

#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'EAHyperion',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.EAHyperion = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu, "SubSubMenu": SubSubMenu })

Foundation.ShipDef.EAHyperion.dTechs = {
	'Defense Grid': 100,
	'Simulated Point Defence' : { "Distance": 45.0, "InnerDistance": 10.0, "Effectiveness": 0.9, "LimitTurn": 0.7, "LimitSpeed": 80, "LimitDamage": "400", "Period": 0.6, "MaxNumberTorps": 3, "Pulse": {"Priority": 1}},
	"Tachyon Sensors": 2.5
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.EAHyperion.hasTGLName = 1
# Foundation.ShipDef.EAHyperion.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.EAHyperion.desc = "The Hyperion-class heavy cruiser was an Earthforce warship manufactured by KarmaTech, primarily at the Neue Hanse Orbital Shipyard in Earth orbit. Before the introduction of the Omega and Warlock-class destroyers, the Hyperion-class heavy cruisers served as Earth's front line warships, often supported by the heavily armed Nova-class dreadnought. Hyperion heavy cruisers made up a proportion of the fleet that was assembled for the Battle of the Line and though a great many were destroyed, the ones that survived continued to serve alongside their successors as the workhorses of the Earthforce fleet. Even though the design was far past its prime it continued to be in service as late as 2281. Like most Earth Alliance ships of the period, the Hyperion lacked the capability to generate artificial gravity, either through the use of rotating sections or the later, more advanced gravitic drive systems. Though rotating sections were within Earthforce's technical capabilities of the time, they greatly reduced a ship's speed and effectiveness. As such the crew had to operate in a completely zero gravity environment, requiring the use of seat straps and handholds to work effectively. Several decks are dedicated to crew quarters and facilities. Crew were often granted leave time after a tour to adapt to gravity again. In later years, ships such as the Clarkstown were seen upgraded with newer weaponry such as the 52 mm plasma pulse cannon used on the Omega class Destroyer."
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.EAHyperion.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EAHyperion.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
