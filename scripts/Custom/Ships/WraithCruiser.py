#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 19.02.2009                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'WraithCruiser'
iconName = 'WraithCruiser'
longName = 'Wraith Cruiser'
shipFile = 'WraithCruiser' 
menuGroup = 'Stargate Ships'
playerMenuGroup = 'Stargate Ships'
SubMenu = "Wraith Ships"
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'WraithCruiser',
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
Foundation.ShipDef.WraithCruiser = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
# Wraith do not have shields used as actual shields. At most only used for forcefields to keep things in. This serves as an addendum to possibly add a tech later to prevent transporting.
Foundation.ShipDef.WraithCruiser.dTechs = {
	'SG Shields': { "RaceShieldTech": "Wraith" }
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.WraithCruiser.hasTGLName = 1
# Foundation.ShipDef.WraithCruiser.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.WraithCruiser.desc = 'Wraith cruisers are vessels that are used by the Wraith that function as escorts for Hive ships, specially during assaults or when feeding on a Human world. Beyond this role, they are also seen in the role of patrol ships that are sent to investigate disturbances near Wraith territory. They are also sent alone against Human worlds in order to cull its inhabitants that are incapable of mounting a defense against them. They are known to carry Wraith Darts on them which are deployed in combat engagements. Similar to other Wraith vessels, they require a Wraith or someone with their DNA to pilot it. Also, they do not possess shields and instead they rely on their organic hull to protect them from damage. Because of that, Wraith cruisers are not as powerful as equivalent ships of other races.'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WraithCruiser.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WraithCruiser.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
