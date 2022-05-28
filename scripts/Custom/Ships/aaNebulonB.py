#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 5/27/2007                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'aaNebulonB'
iconName = 'aaNebulonB'
longName = 'Nebulon B Frigate'
shipFile = 'aaNebulonB' 
menuGroup = 'Star Wars Fleet'
playerMenuGroup = 'Star Wars Fleet'
species = App.SPECIES_GALAXY
SubMenu = "Rebel Alliance"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'aaNebulonB',
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
Foundation.ShipDef.aaNebulonB = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.aaNebulonB.hasTGLName = 1
# Foundation.ShipDef.aaNebulonB.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.aaNebulonB.desc = 'The EF76 Nebulon-B escort frigate was a 300-meter-long warship that was built by Kuat Drive Yards for use by the Imperial Navy, to protect convoys from Rebel Alliance starfighter actions. It was, however, used more famously by the Rebellion. The standard Nebulon-B frigate was armed with twelve turbolasers, twelve laser cannons, and two tractor beam projectors.While generally well-armed for a vessel of that size, the midsection connecting spar was an exploitable vulnerability. It could be split open by concentrated heavy weapons fire, venting the frigate´s atmosphere and killing most of the crew. '
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.aaNebulonB.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.aaNebulonB.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
